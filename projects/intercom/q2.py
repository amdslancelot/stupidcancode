import sys, os.path, json, math, pprint
range = 100
office_coor = [53.3381985, -6.2592576]

class InterComParty:
  
  def __init__(self, filename, coor, range):
    self.coor       = coor     #Intercom Dublin office
    self.earth_r    = 6371     #unit:km
    self.range      = range    #unit:km
    self.filename   = filename                
    self.guest_list = []       #Invite list

  def formula(self, coor1, coor2):
    c1_lat  = math.radians(coor1[0])
    c1_lon = math.radians(coor1[1])
    c2_lat  = math.radians(coor2[0])
    c2_long = math.radians(coor2[1])
    
    delta_long = abs(c2_long - c1_lon)
    y = math.sqrt( ( math.cos(c2_lat)*math.sin(delta_long) )**2 + ( math.cos(c1_lat)*math.sin(c2_lat) - math.sin(c1_lat)*math.cos(c2_lat)*math.cos(delta_long) )**2 )
    x = math.sin(c1_lat)*math.sin(c2_lat) + math.cos(c1_lat)*math.cos(c2_lat)*math.cos(delta_long)
    return math.atan2(y,x) * self.earth_r

  def pick_guest(self):
    with open(self.filename) as f:
      for line in f:
        data = json.loads(line)
        uid  = data['user_id']
        name = data['name']
        lat  = data['latitude']
        lon  = data['longitude']
        
        distance = self.formula(self.coor, [ float(lat), float(lon) ])
        if distance <= float(self.range):
          self.guest_list.append(
            {
              "user_id"   : str(uid), 
              "name"      : str(name), 
              "latitude"  : float(lat), 
              "longitude" : float(lon), 
              "distance"  : float(distance)
            }
          )

    self.guest_list = sorted(self.guest_list, key=lambda k: int(k['user_id']))
  
  def get_guest_list(self, format=format):
    self.pick_guest()
    
    if format == "json":
      return json.dumps(self.guest_list)
    return self.guest_list

if __name__ == '__main__':
  if len(sys.argv) <= 1 or not os.path.isfile(sys.argv[1]):
    print "[ERROR] Please enter input file name."
    exit(1)

  event = InterComParty(sys.argv[1], office_coor, range)
  r = event.get_guest_list()

  print "Guests within", range, "km:"
  pprinter = pprint.PrettyPrinter(indent=4) #printer
  for e in r:
    pprinter.pprint(e)

  print "Total %s guests" % (len(r))
