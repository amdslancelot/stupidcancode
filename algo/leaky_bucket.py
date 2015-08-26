from time import time, sleep

class LeakyBucket:

    def __init__(self, rate):
        self.timestamp = time()
        self.rate = rate
        self.bucketSize = 0 

    def add(self, data):
        print "\nadd:", data
        now = time()
        delta = now - self.timestamp
        self.bucketSize += data
        newRate = self.bucketSize/delta
        print "newRate", newRate, "self.bucketSize", self.bucketSize, "delta", delta, "now", now, "self.timestamp", self.timestamp
        if newRate > self.rate:
            print "exceed!", newRate
            self.timestamp = now
            self.bucketSize = 0
            return False
        return True

    def getSize(self):
        return self.bucketSize

bucket = LeakyBucket(10)
print "size", bucket.getSize()
print bucket.add(5)
print "size", bucket.getSize()
print "sleep(1)"
sleep(1)
print "size", bucket.getSize()
print bucket.add(5)
print "size", bucket.getSize()
print bucket.add(30)
print "size", bucket.getSize()
print bucket.add(0)
print "size", bucket.getSize()
print bucket.add(0)
print "size", bucket.getSize()
print bucket.add(0)
print "size", bucket.getSize()
print bucket.add(0)
print "size", bucket.getSize()
print "sleep(1)"
sleep(1)
print bucket.add(5)
print "size", bucket.getSize()

