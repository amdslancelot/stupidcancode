/*

Given a string S, find the longest palindromic substring in S.

palindrome = anagram = 回文
*/

public class LongestPalindromicSubstring {
    
    public static void main(String[] args) {
        LongestPalindromicSubstring q = new LongestPalindromicSubstring();
        String s = "fgfdcabacdfgdcaba";
        String ans = q.longestPalindromeDP(s);
        System.out.println("ans=" + ans);
        
    }

    String longestPalindromeDP(String str) {
        char[] s = str.toCharArray();
        int n = str.length();
        int longestBegin = 0;
        int maxLen = 1;

        //Create a table of establishing the relation of each letter and its neighbor 
        boolean[][] table =  new boolean[1000][1000];
        for (int i = 0; i < n; i++) {
            table[i][i] = true;
        }

        /* starting from checking the case that if "2 letters next to each other is an anagram" (same chars) */
        for (int i = 0; i < n-1; i++) {
            if (s[i] == s[i+1]) {
                table[i][i+1] = true;
                longestBegin = i;
                maxLen = 2;
            }
        }
        
        /* starting from checking the case that "3 letters next to each other are anagram" */
        for (int len = 3; len <= n; len++) { //starting from len = 3
            for (int i = 0; i < n-len+1; i++) { //create loops to iterating all cases for that len
                int j = i+len-1;
                if (s[i] == s[j] && table[i+1][j-1]) {
                    System.out.printf("s[%s](%s) == s[%s](%s) && table[%s+1][%s-1](%s)\n", i, s[i], j, s[j], i, j, table[i+1][j-1]);
                    table[i][j] = true;
                    longestBegin = i;
                    maxLen = len;
                }
            }
        }
        System.out.printf("longestBegin=%s, maxLen=%s\n", longestBegin, maxLen );
        return str.substring(longestBegin, longestBegin + maxLen);
    }
}
