import java.util.*;

public class DivideTwoIntegers {
    
    public static void main(String[] args) {
        ArrayList<int[]> cases = new ArrayList<int[]>();
        cases.add(new int[]{1,2});
        cases.add(new int[]{2147483647,1});
        cases.add(new int[]{-2147483648, 1});
        cases.add(new int[]{-2147483648,2});
        cases.add(new int[]{-2147483648,3});
        cases.add(new int[]{2147483647, 2});
        cases.add(new int[]{2147483647, -2147483648});
        cases.add(new int[]{1,-2});

        DivideTwoIntegers test = new DivideTwoIntegers();
        for(int[] e : cases) {
            System.out.println();
            int r = test.divide(e[0], e[1]);
            System.out.printf("%d/%d=%d\n", e[0], e[1], r);
        }
    }

    public int divide(int dividend, int divisor) {
        if(divisor == 0) {
            return 0;
        }

        /* Because we let MIN_VALUE to be MAX_VALUE later && 
           abs MAX_VALUE = abs MIN_VALUE + 1 would change the value.
           When (0 < divisor <= 2), +1/-1 of the original value would change the result,
           so this is a special case. */
        // Case: divisor == 1
        if(divisor == 1) {
            return dividend;
        }
        // Case: divisor == 2
        if(divisor == 2) {
            return dividend >> 1;
        }        
        
        if(dividend == Integer.MAX_VALUE && divisor == Integer.MIN_VALUE) {
            return 0;
        }
        
        boolean negativeSign = false;
        if(dividend > 0 && divisor < 0 || dividend < 0 && divisor > 0) {
            negativeSign = true;
        }
        
        dividend = (dividend == Integer.MIN_VALUE) ? Integer.MAX_VALUE : Math.abs(dividend);
        divisor = (divisor == Integer.MIN_VALUE) ? Integer.MAX_VALUE : Math.abs(divisor);
        
        int r = (int)(double)Math.pow(Math.E, Math.log(dividend) - Math.log(divisor));
        System.out.println("log(divisor)=" + Math.log(divisor));
        System.out.println("log(dividend)=" + Math.log(dividend));
        System.out.println("dividend - divisor =" + (Math.log(dividend) - Math.log(divisor)));
        System.out.println("power =" + Math.pow(Math.E, Math.log(dividend) - Math.log(divisor)));
        System.out.println("power2=" + (double)Math.pow(Math.E, Math.log(dividend) - Math.log(divisor)) );
        System.out.println("int: " + r);

        return (negativeSign) ? -r : r;
    }

    public int divide2(int dividend, int divisor) {
        if(divisor == 0)
            return 0;
        if(divisor == 1)
            return dividend;
        if(dividend == divisor)
            return 1;
        if(divisor == 2)
            return dividend >> 1;
             
        boolean sign = false;
        if( (dividend > 0 && divisor < 0) ||
            (dividend < 0 && divisor > 0) )
            sign = true;
             
        if(dividend == Integer.MAX_VALUE && divisor == Integer.MIN_VALUE)
            return 0;
         
        dividend = dividend == Integer.MIN_VALUE ? Integer.MAX_VALUE : Math.abs(dividend);
        divisor = divisor == Integer.MIN_VALUE ? Integer.MAX_VALUE : Math.abs(divisor);
        int result = (int) Math.floor(Math.pow(Math.E, Math.log(dividend) - Math.log(divisor)));
        return sign ? -result : result;
    }

}
