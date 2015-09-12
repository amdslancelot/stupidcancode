/**
 * Take Home Question: Cup Challenge
 * 
 * You are in a room with a circle of 100 cups. The cups are numbered sequentially from 1 to 100.
 * 
 * At some point in time, cup #1 is taken away. Cup #2 is skipped, then cup #3 is taken away. Then 
 * two cups are skipped, and cup #6 is taken away. Then three cups are skipped, and the next one is 
 * taken away. This pattern of removing cups and skipping more cups continues until only one cup 
 * remains. A cup that is removed from the circle is gone forever, and is not considered in subsequent 
 * skipping calculations.
 * 
 * Write a program to determine which cup is left after all others have been removed. 
 * 
 * @author  Lans
 * @version 1.0
 * @since   2015.09.11
 */
public class CupChallenge {
  
  /**
   * Datastrucutre(single Linked List) to present cups.
   *
   */
  public static class LinkedNode {
    private LinkedNode next;
    private int value;

    public LinkedNode(int value) {
      this.value = value;
    }

    public LinkedNode getNext() {
      return next;
    }

    public void setNext(LinkedNode next) {
      this.next = next;
    }
    
    public int getValue() {
      return value;
    }

    public void setValue(int value) {
      this.value = value;
    }
  }
  
  /**
   * Initialize a list of cups base on size.
   *
   * @param size num of cups
   * @return LinkedNode[] start node and end node
   */
  public static LinkedNode[] createCups(int size) {
    LinkedNode start = null, end = null, prev = null;
    for(int i=0; i<size; i++) {
      LinkedNode ln = new LinkedNode(i+1);
     
      // Set start 
      if (i == 0) {
        start = ln;
      }

      // Link node
      if (prev != null) {
        prev.setNext(ln);
      }

      // Set end
      if (i == size-1) {
        ln.setNext(start);
        end = ln;
      }
      
      prev = ln;
    }

    LinkedNode[] r = new LinkedNode[2];
    r[0] = start;
    r[1] = end;
    return r;
  }

  /**
   * Algorithm to remove cups until there's only 1 cup left.
   * P.S Use remain ([num to skip]/[size]) to accelerate in 2nd half of the process when [num to skip] is bigger than [size]
   *
   * @param  start
   * @param  end
   * @param  size
   * @return the number of the last cup
   */
  public static int cupChallenge(LinkedNode start, LinkedNode end, int size) {
    int skip = 1;
    LinkedNode current = start, prev = end, next = null;
    
    while (current.getNext() != current) {
      // Remove current node
      System.out.println("Cup #" + current.getValue() + " removed.");
      prev.setNext(current.getNext());
      next = current.getNext();
      current.setNext(null);
      current = next;
      size--;

      // Check status
      if (current.getNext() == current) {
        continue;
      }
      
      // Accelerate
      int remain = skip;
      if (skip >= size) {
        remain = skip % size;
      }

      // Skip Nodes
      for(int i=0; i<remain; i++) {
        System.out.println("Cup #" + current.getValue() + " skipped. (" + (i+1) + "/" + remain + " of total:" + size + ")");
        prev = current;
        current = current.getNext();
      }
      skip++;
    }

    return current.getValue();
  }

  public static void main(String[] args) {
    if (args.length != 1) {
      System.out.println("[ERROR] Please input the num of cups.");
      return;
    }

    int size = Integer.parseInt(args[0]);
    LinkedNode[] nodes = createCups(size);
    LinkedNode start = nodes[0];
    LinkedNode end = nodes[1];

    int r = cupChallenge(start, end, size);
    System.out.println();
    System.out.println("Ans:" + r);
  }
}
