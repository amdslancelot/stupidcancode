import java.util.*;

public class PalindromePartition2 {

    public static void main(String[] args) {
        PalindromePartition2 test = new PalindromePartition2();
        String s = "bb";
        System.out.println(s);
        int cut = test.minCut(s);
        System.out.println(cut);
    }

    public int minCut(String s) {
        int s_len = s.length();
        int[] dp = new int[s_len];
        boolean[][] palin = new boolean[s_len][s_len];
        
        for(int i=s_len-1; i>=0; i--) {
            dp[i] = s_len-1 - i;
        }

        System.out.println(Arrays.toString(dp));
        
        for(int i=s_len-1; i>=0; i--) {
            for(int j=i; j<s_len; j++) {
                if(s.charAt(i) == s.charAt(j) && (j-i<2 || palin[i+1][j-1])) {
                    palin[i][j] = true;
                    dp[i] = Math.min(dp[i], dp[j+1]+1);
                }
            }
        }
        System.out.println(Arrays.toString(dp));
        
        return dp[0];
    }

    public int minCut2(String s) {
        if(s.length() == 1) {
            return 0;
        }
        
        boolean[] map = new boolean[s.length()];
        Arrays.fill(map, Boolean.FALSE);
        
        int cut = 0;
        for(int i=1; i<s.length(); i++) {
            //Find palindromes start with 2 letters
            if(i >= 1 && !map[i] && findPalindromesStartWith(i-1, i, map, s)) {
                System.out.println("A, i=" + i);
                cut++;
            }
            
            //Find palindromes start with 3 letters
            if(i >= 2 && !map[i-1] && findPalindromesStartWith(i-2, i, map, s)) {
                System.out.println("B, i=" + i);
                cut++;
            }
        }
        
        int cut2 = 0;
        for(int i=0; i<s.length(); i++) {
            if(!map[i]) {
                map[i] = true;
                cut2++;
            }
        }

        System.out.println("cut=" + cut + ", cut2=" + cut2);
        
        cut = (cut > 0 && cut2 == 0) ? cut-1 : cut;
        cut2 = (cut == 0 && cut2 > 0) ? cut2-1 : cut2;
        cut = (cut > 0 && cut2 > 0) ? cut + cut2 - 1 : cut + cut2;
        
        return cut;
    }
    
    public boolean findPalindromesStartWith(int i1, int i2, boolean[] map, String s) {
        System.out.println("i1=" + i1 + ", i2=" + i2 + ": " + Arrays.toString(map));
        if(i1 >= 0 && i2 < s.length() && !map[i1] && !map[i2] && s.charAt(i2) == s.charAt(i1)) {
            if( ( (i2+1 < s.length() && s.charAt(i2+1) == s.charAt(i2)) || 
                  (i1-1 >= 0 && s.charAt(i1-1) == s.charAt(i1)) ) &&
                (i2-i1) / 2 == 0
                ) {
                return false;
            }
            
            if(i2 == i1 + 2) {
                map[i2-1] = true;
            }
            
            map[i2] = true;
            map[i1] = true;
            findPalindromesStartWith(i1-1, i2+1, map, s);
            return true;
        }
        return false;
    }


}
