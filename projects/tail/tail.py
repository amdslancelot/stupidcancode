import argparse, sys, re

def toParam(s):
  if not re.match(r'(\+|\-)?[0-9]+', s):
    return None
  if s[0] == "+":
    return int(s)
  if s[0] == "-":
    return int(s)
  if re.match(r'[0-9]+', s):
    return -1*(int(s))
  return int(s)

def init(fname, n, buf_size=128):
  buf = ""
  pos = 0
  block_count = 0
  direction = 1

  with open(fname, 'r') as fh:
    fh.seek(0,2)
    file_size = fh.tell()
    print "file size:", file_size
    
    if n >= 0:
      fh.seek(0,0)
      direction = 1
      pos = 0
    else:
      fh.seek(0,2)
      direction = -1
      pos = file_size
    n = abs(n)

    while block_count <= n and file_size > 0:
      if buf_size > file_size:
        buf_size = file_size

      if direction == 1:
        buf_read = fh.read(buf_size)
      else:
        fh.seek(direction*buf_size, 1)
        buf_read = fh.read(buf_size)
        fh.seek(direction*buf_size, 1)

      block_count += buf_read.count("\n")
      pos = fh.tell()
      
      if direction == 1:
        buf = buf + buf_read
      else:
        buf = buf_read + buf

    if direction == 1:
      count = block_count - n + 1
      while count > 0:
        pos = buf.rfind("\n")-1
        buf = buf[:pos+1]
        count -= 1
      fh.seek(pos+2,0)
      return fh.read()
    else:
      count = block_count - n
      while count > 0:
        pos = buf.find("\n")
        buf = buf[pos+1:]
        count -= 1
      return buf
  return buf
      

def init2(fname, n, buf_size=128):
  buf = ""
  block_count = 0
  direction = 1

  with open(fname, 'r') as fh:
    fh.seek(0,2)
    file_size = fh.tell()
    print "file size:", file_size
    
    if n >= 0:
      fh.seek(0,0)
      direction = 1
    else:
      fh.seek(0,2)
      direction = -1
    n = abs(n)

    while block_count <= n and file_size > 0:
      if buf_size > file_size:
        buf_size = file_size
      
      fh.seek(direction*buf_size, 1)
      buf_read = fh.read(buf_size)
      fh.seek(direction*buf_size, 1)
      
      block_count += buf_read.count("\n")
      file_size -= buf_size
      buf = buf_read + buf

  count = block_count - n
  pos = 0
  while count > 0:
    pos = buf.find("\n")
    buf = buf[pos+1:]
    count -= 1
  return buf

if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="Tail", description="The tail utility displays the contents of file or, by default, its standard input, to the standard output.")
  
  parser.add_argument("fname", help="The file name as input")
  parser.add_argument("-f", action="store_true",
                      help="The -f option causes tail to not stop when end of file is reached, but rather to wait for additional data to be appended to the input.")
  parser.add_argument("-b", type=toParam, default="512", nargs='?',
                      help="The location is number 512-byte blocks.")
  parser.add_argument("-c", type=toParam, default="0", nargs='?',
                      help="The location is number bytes.")
  parser.add_argument("-n", type=toParam, default="10", nargs='?',
                      help="The location is number lines.")

  args = parser.parse_args()
  if args.fname:
    print "fname:", args.fname
  if args.f:
    print "f:", args.f
  if args.b:
    print "b:", args.b
  if args.c:
    print "c:", args.c
  if args.n:
    print "n:", args.n
  else:
    print "error"
  
  r = init(args.fname, args.n)
  sys.stdout.write(r)
