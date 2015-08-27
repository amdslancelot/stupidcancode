import java.util.*;
public class PalindromeInt {

    public static void main(String[] args) {
        PalindromeInt test = new PalindromeInt();
        boolean r = test.isPalindrome(9999);
        System.out.println(r);
    }

    public boolean isPalindrome(int x) {
        if(x<0) {
            return false;
        }
        
        int l = (int)(Math.log(x) / Math.log(10));
        if(l==0) {
            return true;
        }
        
        for(int i=1; i<=(l+1)/2; i++) {
            int v1 = (x % (int)Math.pow(10,i)) / (int)(Math.pow(10, i-1));
            int v2 = (x / (int)Math.pow(10, l-(i-1)) ) % 10;
            System.out.println(v1);
            System.out.println(v2);
            
            if(v1 != v2) {
                return false;
            }
        }
        return true;
    }
}
