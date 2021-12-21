import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

/**
 * Node
 */
class Node {
    private char[][] state;
    private int cost;
    private int fval;

    public Node(char[][] state,int cost,int fval){
        this.state = state;
        this.cost = cost;
        this.fval = fval;
    }

    boolean isEqual(Node goalState){
        char[][] goalStateMatrix = goalState.state;
        for(int i=0;i<this.state.length;i++){
            for(int j=0;j<this.state[0].length;j++){
                if(this.state[i][j]==goalStateMatrix[i][j]){
                    return false;
                }
            }
        }
        return true;
    }
    private char[][] copyBoard(){
        char[][] returnArray = new char[state.length][state[0].length];
        for (int i = 0, j = 0; i*j < 9 ; i++, j++){
            // deep copy of row:
            returnArray[i] = Arrays.copyOf(state[i], state[i].length);
        }
        return returnArray;
    }

    List<Node> getChildren(){
        List<Node> children = new ArrayList<Node>();
        List<Integer> coordinates = getSpaceCoordinates();
        int[][] directions = {
            {coordinates.get(0),coordinates.get(1)+1},
            {coordinates.get(0),coordinates.get(1)-1},
            {coordinates.get(0)+1,coordinates.get(1)},
            {coordinates.get(0)-1,coordinates.get(1)}
        };
        
        for(int[] direction : directions){
            if(
                (direction[0] < this.state.length && direction[0]>=0) && 
                (direction[1] < this.state[0].length && direction[1]>=0)
            ){
                char[][] dup = copyBoard();
                char temp = dup[coordinates.get(0)][coordinates.get(1)];
                dup[coordinates.get(0)][coordinates.get(1)] = dup[direction[0]][direction[1]];
                dup[direction[0]][direction[1]] = temp;
                children.add(new Node(dup,this.cost+1,0));
            }
        }
        return children;
    }

    int getHeuristic(Node goalState){
        char[][] goalStateMatrix = goalState.state;
        int score=0;
        for(int i=0;i<this.state.length;i++){
            for(int j=0;j<this.state[0].length;j++){
                if(this.state[i][j]!=goalStateMatrix[i][j] && this.state[i][j]!='_'){
                    score++;
                }
            }
        }
        return score;
    }

    char [][] getState(){
        return state;
    }

    int getCost(){
        return cost;
    }
    void setFValue(Node goalState){
        this.fval = this.cost + getHeuristic(goalState);
    }
    int getFValue(){
        return this.fval;
    }
    // get row and column values of space 
    List<Integer> getSpaceCoordinates(){
        List<Integer> coordinates = new ArrayList<Integer>();
        for(int i=0;i<this.state.length;i++){
            for(int j=0;j<this.state[0].length;j++){
                if(this.state[i][j]=='_'){
                    coordinates.add(i);
                    coordinates.add(j);
                    return coordinates;
                }
            }
        }
        return coordinates;
    }
    
}


class EightPuzzle implements Comparator<Node>{
    Node startState;
    Node goalState;
    List<Node> open;
    List<Node> closed;

    public EightPuzzle(){}
    public EightPuzzle(char[][] startStateMatrix,char[][] goalStateMatrix){
        this.goalState = new Node(goalStateMatrix, 0,0);
        this.startState = new Node(startStateMatrix,0,0);
        open = new ArrayList<Node>();
        open.add(this.startState);
        closed = new ArrayList<Node>();
    }
    void print(Node node){
        char[][] state = node.getState();
        for(int i=0;i<state.length;i++){
            for(int j=0;j<state[0].length;j++){
                System.out.print(state[i][j] + " ");
            }
            System.out.println("");
        }
    }
    void solve(){
        if(startState.isEqual(goalState)){
            System.out.println("Start and Goal States are Equal...");
            return;
        }
        
        while(true){
            Node parent = open.get(0);
            System.out.println("");
            System.out.println("State " + parent.getCost());
            print(parent);
            if(parent.getCost()>10){
                System.out.println("Goal State is Unreachable...");
                return;
            }

            if(parent.getHeuristic(goalState)==0){
                return;
            }

            List<Node> children = parent.getChildren();
            for(Node node : children){
                node.setFValue(goalState);
                open.add(node);
            }
            open.remove(0);
            closed.add(parent);
            Collections.sort(open,this);
        }
    }
    @Override
    public int compare(Node o1, Node o2) {
        // TODO Auto-generated method stub
        if(o1.getFValue() <= o2.getFValue()){
            return 1;
        }
        return 0;
    }
}

public class AStar {
    public static Scanner scanner = new Scanner(System.in);

    static char [][] accept(char[][] state){
        for(int i=0;i<state.length;i++){
            for(int j=0;j<state[0].length;j++){
                state[i][j]  = scanner.next().charAt(0);
            }
        }
        return state;
    }

    public static void main(String[] args) {
        // char [][] goalState = new char[3][3];
        // char [][] startState =  new char[3][3];
        // startState = accept(startState);
        // goalState = accept(goalState);
        char [][] startState = {{'1','2','3'},{'_','4','6'},{'7','5','8'}};
        char [][] goalState = {{'1','2','3'},{'4','5','6'},{'7','8','_'}};
        EightPuzzle puzzle = new EightPuzzle(startState, goalState);
        puzzle.solve();
    }
}