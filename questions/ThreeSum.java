/*
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

*Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
*The solution set must not contain duplicate triplets.

For example, given array S = {-1 0 1 2 -1 -4},

A solution set is:
(-1, 0, 1)
(-1, -1, 2)
*/

import java.util.*;

public class ThreeSum {
    
    public static void main(String[] args) {
        int[] case1 = new int[]{-1, 0, 1, 2, -1, -4};
        int[] case2 = new int[]{30,7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,
                             -4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,
                              2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,
                             -8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,
                             14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,
                             -8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6};
        int[] case3 = {-1,0,1};
        ThreeSum test = new ThreeSum();
        System.out.println("test 1:");
        test.threeSum(case1);
        System.out.println("test 2:");
        test.threeSum(case2);
        System.out.println("test 3:");
        test.threeSum(case3);

    }

    public ArrayList<ArrayList<Integer>> threeSum(int[] num) {
        /* Turn the array into a hashmap */
        HashMap<Integer, Integer> hm = createHashTable(num);
        // time: O(n)
        System.out.println(hm.toString());

        /* */
        Arrays.sort(num);
        System.out.println("sorted:" + Arrays.toString(num));
        // java use merge sort: O(nlogn)

        /* 1. generate all the pairs
              {-1 0 1 2 -1 -4} => {-1, 0} {-1, 1} {-1, 2} .....
           2. Find complementary in the hashtable */
        ArrayList<ArrayList<Integer>> r = findComplementary(num, hm, 0);
        // time: O(n^2)
        
        //return r;

        ArrayList<ArrayList<Integer>> rr = new ArrayList<ArrayList<Integer>>();
        HashMap<String, ArrayList<Integer>> dedupMap = new HashMap<String, ArrayList<Integer>>();
        for(ArrayList<Integer> e : r) {
            ArrayList<Integer> set = sort3Nums(new int[]{e.get(0), e.get(1), e.get(2)});
            String str_key = set.get(0) + "_" + set.get(1) + "_" + set.get(2);
                
            if(!dedupMap.containsKey(str_key)) {
                dedupMap.put(str_key, set);
                rr.add(set);
            }
        }
        System.out.println("rr: " + rr.toString());

        return rr;

    }
  
    public static ArrayList<ArrayList<Integer>> findComplementary(int[] num, HashMap<Integer, Integer> hm, int key) {
        ArrayList<ArrayList<Integer>> rr = new ArrayList<ArrayList<Integer>>();
        HashMap<String, ArrayList<Integer>> dedupMap = new HashMap<String, ArrayList<Integer>>();

        for(int i=0; i<num.length; i++) {
            //if(i>0 && num[i] == num[i-1]) continue; // Skip the same num[i] here.
            //if(num[i]>0) break; // Break if num[i] > 0 (pick the first number num[i] < 0 first)

            for(int j=i+1; j<num.length; j++) {
                //if(j>i+1 && num[j] == num[j-1]) continue; // Skip the same num[j] here.

                int t = key - (num[i] + num[j]); //pick the second number num[j]
                //if( t < num[j] ) {
                //    break; //If the negative sum of the first 2 nums is still smaller than the second num,
                             //the negative sum of the first 2 nums won't be possible to be > the third num,
                             //(the second num must be smaller than the third num (sorted array)),
                             //so no possible answers afterwards.
                //}

                int c1 = hm.get(num[i]);
                hm.put(num[i], --c1);
                int c2 = hm.get(num[j]);
                hm.put(num[j], --c2);

                if(hm.containsKey(t) && hm.get(t) > 0) {
                    System.out.println("findComplementary:{" + num[i] + "," + num[j] + "," + t + "}");
                    //If 3 nums are complementary
                    ArrayList<Integer> set = new ArrayList<Integer>();
                    set.add(num[i]);
                    set.add(num[j]);
                    set.add(t);
                    
                    rr.add(set);
                }
                
                hm.put(num[i], ++c1);
                hm.put(num[j], ++c2);
            }
        }

        return rr;
    }
    
    public static HashMap<Integer, Integer> createHashTable(int[] num) {
        HashMap<Integer, Integer> r = new HashMap<Integer, Integer>();
        for(int e : num) {
            if(r.containsKey(e)) {
                int count = r.get(e);
                r.put(e, ++count);
            } else {
                r.put(e, 1);
            }
        }
        return r;
    }

    public static ArrayList<Integer> sort3Nums(int[] nums) {
        //System.out.println("sort: {" + nums[0] + "," + nums[1] + "," + nums[2] + "}");
        ArrayList<Integer> orders = new ArrayList<Integer>();
        orders.add(-99999);
        orders.add(-99999);
        orders.add(-99999);
        int l = orders.size();
        for(int e : nums) {
            for(int key=0; key<l; key++) {
                if(e > orders.get(key)) {
                    orders = replaceNLargest(orders, key, e, l-1);
                    break;
                }
            }
            //System.out.println("sorted: {" + orders.get(0) + "," + orders.get(1) + "," + orders.get(2) + "}");
        }
        return orders;
    }

    public static ArrayList<Integer> replaceNLargest(ArrayList<Integer> orders, int key, int value, int n) {
        //System.out.println("key=" + key + ", value=" + value + ", n=" + n);
        if(n == key) {
            orders.set(key, value);
            return orders;
        } else {
            int l = orders.size();
            orders.set(n, orders.get(n-1));
            return replaceNLargest(orders, key, value, n-1);
        }
    }

}
