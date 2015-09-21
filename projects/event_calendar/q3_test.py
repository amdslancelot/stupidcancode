import q3
if __name__ == "__main__":
  test = q3.IntercomCalendar("events.txt")
  tests = {"all":4, "past":3, "today":0, "future":1, "cancelled":1, "existing":3}
  for k,v in tests.items():
    count = test.get_event_counts(k)
    if (count != v):
      print "Test %s: Failed" % (k)
    else:
      print "Test %s: Passed" % (k)
