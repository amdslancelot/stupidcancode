import argparse

def init(fname, n):
  r = []
  with open(fname, 'r') as fh:
    #f = fh.readlines()
    #print f[-10:]
    fh.seek(0,2)
    buf_size = 128
    buf = []
    file_size = fh.tell()
    print "file size:", file_size

    while n > 0 and file_size > 0:
      if buf_size > file_size:
        buf_size = file_size
      
      t = ""
      if len(buf) == 1:
        t = buf[0]
        buf = []

      fh.seek(-1*buf_size, 1)
      buf_str = fh.read(buf_size)
      fh.seek(-1*buf_size, 1)
      buf += buf_str.split("\n")
      
      count = len(buf)
      buf[count-1] = buf[count-1] + t
      while count > 1:
        r.insert(0, buf[count-1])

        n -= 1
        count -= 1
        file_size -= buf_size
      
      buf = [buf[0]]
  

  return r

if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="Tail", description="The tail utility displays the contents of file or, by default, its standard input, to the standard output.")
  
  parser.add_argument("fname", help="The file name as input")
  parser.add_argument("-f", action="store_true",
                      help="The -f option causes tail to not stop when end of file is reached, but rather to wait for additional data to be appended to the input.")
  parser.add_argument("-b", type=int, default=512, nargs='?',
                      help="The location is number 512-byte blocks.")
  parser.add_argument("-c", type=int, default=0, nargs='?',
                      help="The location is number bytes.")
  parser.add_argument("-n", type=int, default=10, nargs='?',
                      help="The location is number lines.")

  args = parser.parse_args()
  if args.fname:
    print args.fname
  if args.f:
    print args.f
  if args.b:
    print args.b
  if args.c:
    print args.c
  if args.n:
    print args.n
  else:
    print "error"
   
  r = init(args.fname, args.n)
  for e in r:
    print "ans:", e
