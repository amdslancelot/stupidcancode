#from q2 import InterComParty
import q2
if __name__ == "__main__":
  test = q2.InterComParty("customers.txt", q2.office_coor, q2.range)
  r = len(test.get_guest_list())
  if (r == 16):
    print "Passed"
  else:
    print "Failed"
