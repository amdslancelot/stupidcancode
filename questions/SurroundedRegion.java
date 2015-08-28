import java.util.*;

public class SurroundedRegion {

    public static void main(String args[]) {
        ArrayList<char[][]> cases = new ArrayList<char[][]>();
        cases.add(new char[][]{{'X', 'X', 'X', 'X'},
                               {'X', 'O', 'O', 'X'},
                               {'X', 'X', 'O', 'X'},
                               {'X', 'O', 'X', 'X'}});
        cases.add(new char[][]{{'X', 'X', 'X', 'X', 'X'},
                               {'X', 'O', 'O', 'O', 'X'},
                               {'X', 'X', 'O', 'O', 'X'},
                               {'X', 'O', 'X', 'X', 'X'},
                               {'X', 'O', 'X', 'X', 'X'}});
        //cases.add(new char[][]{});

        SurroundedRegion test = new SurroundedRegion();
        int n = 0;
        for(char[][] e : cases) {
            test.solve(e);
            for(char[] ee : e) {
                System.out.printf("board%d:%s", n, Arrays.toString(ee));
                System.out.println();
            }
            n++;
        }
    }

    public void solve(char[][] board) {
        for(int i=1; i<board.length-1; i++) {
            for(int j=1; j<board[0].length-1; j++) {
                if(board[i][j] == 'O') {
                   isSurrounded_Recursive(board, i, j);
                }
            }
        }
    }

    public static boolean isSurrounded(char[][] board, int i, int j) {
        return true;    
    }
    
    public static boolean isSurrounded_Recursive(char[][] board, int i, int j) {
        if(board[i][j] == 'X') {
            // Case: is "X"
            return true;
        } else if(i==0 || i==board.length-1 || j==0 || j==board.length-1) {
            // Case: (is "O") && (is the edge)
            return false;
        } else {
            // Case: (is "O") && (is NOT the edge)
            board[i][j] = 'X';
            
            if(isSurrounded_Recursive(board, i-1, j) &&
               isSurrounded_Recursive(board, i+1, j) &&
               isSurrounded_Recursive(board, i, j-1) &&
               isSurrounded_Recursive(board, i, j+1) ) {
                return true;
            } else {
                board[i][j] = 'O';
                return false;
            }
        }
    }

}
