/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

import java.util.*;
public class ConstructBinaryTreeFromPreorderAndInorder {

    public static void main(String[] args) {
        ArrayList<ArrayList<int[]>> cases = new ArrayList<ArrayList<int[]>>();
        ArrayList<int[]> case1 = new ArrayList<int[]>();
        case1.add(new int[]{1,2,3,4}); //preorder
        case1.add(new int[]{1,2,3,4}); //inorder
        cases.add(case1);
        ArrayList<int[]> case2 = new ArrayList<int[]>();
        case2.add(new int[]{1,2,3}); //preorder
        case2.add(new int[]{2,1,3}); //inorder
        cases.add(case2);

        ConstructBinaryTreeFromPreorderAndInorder test = new ConstructBinaryTreeFromPreorderAndInorder();
        for(ArrayList<int[]> e : cases) {
            test.buildTree(e.get(0), e.get(1));
        }
    }

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if(preorder == null || inorder == null || preorder.length == 0 || inorder.length == 0) {
            return null;
        }
        
        TreeNode root = new TreeNode(preorder[0]);
        if(preorder.length == 1 || inorder.length == 1) {
            return root;
        }
        
        return func(preorder, inorder, root, 0);
    }
    
    public static TreeNode func(int[] preorder, int[] a, TreeNode root, int keyIndex) {
        int rootIndex = findIndex(preorder[keyIndex], a);
        int rightTreeRootIndex;
        if(rootIndex != 0) {
            // There is left tree
            rightTreeRootIndex = findIndex(a[rootIndex - 1], preorder) + 1;
        } else {
            rightTreeRootIndex = rootIndex + 1;
        }
        
        int[] leftTree = Arrays.copyOfRange(a, 0, rootIndex);
        int[] rightTree = Arrays.copyOfRange(a, rootIndex+1, a.length);
        
        int nextIndex = findIndex(preorder[keyIndex+1], a);
        if(nextIndex != -1 && nextIndex < rootIndex) {
            /* Next item in preorder is in left tree of inorder array */
            root.left = new TreeNode(preorder[keyIndex+1]);
            if(keyIndex + 1 < preorder.length - 1) {
                func(preorder, leftTree, root.left, keyIndex+1);
            }
        } else if (nextIndex != -1 && nextIndex > rootIndex){
            /* Next item in preorder is in right tree of inorder array */
            root.right = new TreeNode(preorder[rightTreeRootIndex]);
            if(keyIndex + 1 < preorder.length - 1) {
                func(preorder, rightTree, root.right, keyIndex+1);
            }
        } else {
            System.out.printf("error: %d", nextIndex);
        }
        
        return root;
    }
    
    public static int findIndex(int key, int[] a) {
        for(int i=0; i<a.length; i++) {
            if(a[i] == key) {
                return i;
            }
        }
        return -1;
    }
}
