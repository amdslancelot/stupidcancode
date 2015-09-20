import sys, pprint, time, ast, os.path
from datetime import datetime
pprinter = pprint.PrettyPrinter(indent=4)


class IntercomCalendar:

  def __init__(self, data):
    self.output = [[],[],[],[],[]] #data structure
    self.maxOcaLen = 0 #for printing
    self.maxInviCount = 0 #for printing

    dt_now = datetime.utcnow()
    ts_now = (dt_now - datetime(1970, 1, 1)).total_seconds()
   
    # Compose data structure
    data = self.read(data)
    for e in data:
      #Get max str length of occasion
      if len(e["occasion"]) > self.maxOcaLen:
        self.maxOcaLen = len(e["occasion"])

      #Get max str length of Invited Count
      if int(e["invited_count"]) > self.maxInviCount:
        self.maxInviCount = int(e["invited_count"])
      
      # Get ts from year, month, day
      date_str = str(e["year"]) + "/" + str(e["month"]) + "/" + str(e["day"])
      dt = datetime.strptime(date_str, "%Y/%m/%d")
      ts = (dt - datetime(1970, 1, 1)).total_seconds()
      e["dt"] = dt
      e["ts"] = ts
      
      # Grouping by date
      if ts < ts_now:
        self.output[0].append(e) #past
      elif ts > ts_now:
        self.output[2].append(e) #future
      else:
        self.output[1].append(e) #now
    
      # Grouping by cancelled
      if "cancelled" in e and e["cancelled"]:
        self.output[3].append(e) #cancelled
      else:
        self.output[4].append(e) #existing

    # For printing
    self.oca_spaces = " " * (self.maxOcaLen - len("Occasion"))
    self.date_spaces = " " * 6

    # Remove from memory
    del data

  def read(self, fname):
    '''
    Read file and return dictionary
    '''
    with open(fname, 'r') as content_file:
      content = content_file.read()
      content = content.replace('"cancelled": true', '"cancelled": True')
      return ast.literal_eval(content)['events']

  def get_event_counts(self, command):
    if command == "all":
      return len(self.output[0]) + len(self.output[1]) + len(self.output[2])
    elif command == "past":
      return len(self.output[0])
    elif command == "today":
      return len(self.output[1])
    elif command == "future":
      return len(self.output[2])
    elif command == "cancelled":
      return len(self.output[3])
    elif command == "existing":
      return len(self.output[4])
    else:
      return None

  def print_events_by_command(self, command):
    if command == "all":
      self.print_calendar([self.output[0], self.output[1], self.output[2], None, None])
    elif command == "past":
      self.print_calendar([self.output[0], None, None, None, None])
    elif command == "today":
      self.print_calendar([None, self.output[1], None, None, None])
    elif command == "future":
      self.print_calendar([None, None, self.output[2], None, None])
    elif command == "cancelled":
      self.print_calendar([None, None, None, self.output[3], None])
    elif command == "existing":
      self.print_calendar([None, None, None, None, self.output[4]])
    else:
      pass

  def event_tostring(self, e):
    '''
    Convert event in data structure to output string
    '''
    tag = "           "
    if 'cancelled' in e and e['cancelled']:
      tag = "(cancelled)"

    space_oca = self.maxOcaLen - len(e["occasion"])
    occasion = e["occasion"] + " "*space_oca

    star_num = int(e["invited_count"])
    star_num /= 10
    if star_num % 10 != 0:
      star_num += 1
    party_bar = "*"*star_num

    return "    %s %s | %s | %s(%s)" % (tag, occasion, e["dt"].strftime("%Y/%m/%d"), party_bar, e["invited_count"])
    

  def print_calendar(self, data):
    '''
    Print calendar to console according to input data
    '''
    dt_now = datetime.utcnow()
    past      = data[0]
    today     = data[1]
    future    = data[2]
    cancelled = data[3]
    existing  = data[4]

    print 
    print     "======================="
    print     "Intercom Event Calendar"
    print     "======================="
    print     "Date: %s" % (dt_now.strftime("%Y/%m/%d"))
    print 
    print 
    print
    if not today == None:
      print   "    Today's events:"
      self.print_events(today)
      print 
      print 
      print 
    if future:
      print   "    Upcoming events:"
      self.print_events(future)
      print 
      print 
      print
    if past:
      print   "    Past events:"
      self.print_events(past)
      print 
      print 
      print 
    if cancelled:
      print   "    Cancelled events:"
      self.print_events(cancelled)
      print 
      print 
      print 
    if existing:
      print   "    Existing events:"
      self.print_events(existing)
      print 
      print 
      print 

  def print_events(self, events):
    '''
    Print event table
    '''
    cancelled_count = 0
    if len(events) > 0:
      print
      print   "                --------------------------------------------------------------------------"
      print   "                Occasion%s | Date%s | Invited Count" % (self.oca_spaces, self.date_spaces)
      print   "                --------------------------------------------------------------------------"
      for e in events:
        print self.event_tostring(e)
        if 'cancelled' in e and e['cancelled']:
          cancelled_count += 1
      print   "                --------------------------------------------------------------------------" 
    else:
      print
      print   "                ( no events )"

if __name__ == "__main__":
  if len(sys.argv) <= 1 or not os.path.isfile(sys.argv[1]):
    print "[ERROR] Please enter input file name."
    exit(1)

  calendar = IntercomCalendar(sys.argv[1])
  if len(sys.argv) == 2:
    calendar.print_events_by_command("all")
    exit(0)
  
  if sys.argv[2] == "-h":
    print
    print "usage:"
    print "  python q3.py <INPUT_FILENAME> <COMMAND_TYPE> <COMMAND_NAME>"
    print 
    print '  COMMAND_TYPE:'
    print '                -h - help/manual'
    print '                -c - return events by type'
    print '  COMMAND_NAME:'
    print '                all       - return all events'
    print '                past      - return past events only'
    print '                today     - return today\'s events only'
    print '                future    - return upcoming events only'
    print '                cancelled - return all cancelled events'
    print '                existing  - return all un-cancelled events'
    print
    exit(0)

  if sys.argv[2] == "-c":
    command = sys.argv[3]
    if command in ["past", "today", "future", "cancelled", "existing", "all"]:
      calendar.print_events_by_command(command)
      exit(0)
    else:
      print "[ERROR] Cannot recognize command: %s" % (command)
      exit(1)
  
