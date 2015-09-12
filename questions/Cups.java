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
 * Write a program to determine which cup is left after all others have been removed. Please send us 
 * the answer (in Java) and your working code to wxie@popsugar.com.
 * 
 * Your code should print the answer to the cup challenge when there are 100 cups. Also, please provide the answer to the cup challenge to Walt as well.
 * 
 * Example:
 * 
 * Cups are marked with a C, removed cups are marked as X. Not pictured in this example is that the cups wrap around in a circle.
 * 
 * Start: 
 * C C C C C C C C C C ...
 * 
 * Step 1: cup #1 is removed 
 * X C C C C C C C C C ...
 * 
 * Step 2: cup #2 is skipped, cup #3 is removed 
 * X C X C C C C C C C ...
 * 
 * Step 3: cups #4, #5 are skipped, cup #6 is removed 
 * X C X C C X C C C C ...
 * 
 * Step 3: cups #7, #8, #9 are skipped, cup #10 is removed 
 * X C X C C X C C C X ...
 * 
 * And so on.
 *
 */
public class Cups {
  
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

  public static LinkedNode[] createCups(int size) {
    LinkedNode start = null, end = null, prev = null;
    for(int i=0; i<size; i++) {
      LinkedNode ln = new LinkedNode(i+1);
     
      // Set start 
      if (i == 0) {
        start = ln;
      }

      if (prev != null) {
        prev.setNext(ln);
      }

      // Set end
      if (i == size-1) {
        ln.setNext(start);
        end = ln;
        
        System.out.println("Tail: " + ln.getValue());
        System.out.println("Tail's next: " + ln.getNext().getValue());
      }
      
      prev = ln;
    }

    // Print out
    int count = size;
    LinkedNode current = start;
    while (current.getNext() != null && count != 0) {
      System.out.print(current.getValue());
      if (count != 1) {
        System.out.print(",");
      }
      current = current.getNext();
      count--;
    }
    System.out.println();

    LinkedNode[] r = new LinkedNode[2];
    r[0] = start;
    r[1] = end;
    return r;
  }

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
      
      // Skip nodes
      for(int i=0; i<skip; i++) {
        System.out.println("Cup #" + current.getValue() + " skipped. (" + (i+1) + "/" + skip + ")");
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
    System.out.println("start=" + start.getValue());
    System.out.println("end=" + end.getValue());

    int r = cupChallenge(start, end, size);
    System.out.println("Ans:" + r);
  }
}
