import java.util.*;

public class LRUCache {
    
    HashMap<Integer, int[]> hm;
    LinkedList<int[]> ll;
    int capacity;
    
    public static void main(String[] args) {
        LRUCache lruc = new LRUCache(1);
        int r;
        lruc.set(2,1);
        r = lruc.get(2);
        System.out.println(r);
        lruc.set(3,2);
        r = lruc.get(2);
        System.out.println(r);
        r = lruc.get(3);
        System.out.println(r);
    }

    public LRUCache(int capacity) {
        this.hm = new HashMap<Integer, int[]>();
        this.ll = new LinkedList<int[]>();
        this.capacity = capacity;
    }
    
    public int get(int key) {
        /* If HashMap is null*/
        if(hm.size() == 0) {
            return -1;
        }
        
        if(hm.containsKey(key)) {
            if(hm.size() == 1) {
                /* If size of HashMap is 1*/
                return hm.get(key)[0];
            } else { 
                /* If size of HashMap > 1*/
                int[] node = hm.get(key);
                
                //re-attach in DLL
                int index = ll.indexOf(node);
                ll.remove(index);
                ll.addFirst(node);
                return node[0];
            }
        } else {
            return -1;
        }
    }
    
    public void set(int key, int value) {
        /* If capacity is 0*/
        if(capacity == 0) {
            return;
        }
        
        if(hm.containsKey(key)) {
            /* If already has the key  */
            int[] node = hm.get(key);
            int index = ll.indexOf(node);
            ll.remove(index);

            node[0] = value;
            ll.addFirst(node);
        } else {
            /* If is new key */
            int[] newNode = new int[]{value};
            hm.put(key, newNode);
            ll.addFirst(newNode);
            
            if(hm.size() > capacity) {
                ll.pollLast();
            }
        }
    }
    
}
