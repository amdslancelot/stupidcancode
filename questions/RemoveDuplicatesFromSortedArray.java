import java.util.*;

public class RemoveDuplicatesFromSortedArray {
    
    public static void main(String[] args) {
        ArrayList<int[]> cases = new ArrayList<int[]>();
        cases.add(new int[]{1,1,2});
        cases.add(new int[]{1,2,3});

        RemoveDuplicatesFromSortedArray test = new RemoveDuplicatesFromSortedArray();
        for(int[] e : cases) {
            int r = test.removeDuplicates(e);
            System.out.println("r=" + r);
        }
    }

    public int removeDuplicates(int[] A) {
        if(A.length == 0) {
            return 0;
        }

        int start = 0, count = 1;
        for(int i=0; i<A.length; i++) {
            if(A[i] != A[start]) {
                /* swap */
                ++start;
                int t = A[start];
                A[start] = A[i];
                A[i] = t;

                /* update count */
                count++;
            }
        }

        return count;
    }
}
