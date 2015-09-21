# Intercom Coding Assignment

### Test

Q2:
```sh
$ python q2_test.py 
Passed
```

Q3:
```sh
$ python q3_test.py 
Test all: Passed
Test existing: Passed
Test past: Passed
Test future: Passed
Test cancelled: Passed
Test today: Passed
```
### Run

Q2:
```sh
$ python q2.py customers.txt
```

Q3:
```sh
$ python q3.py events.txt -h

usage:
  python q3.py <INPUT_FILENAME> <COMMAND_TYPE> <COMMAND_NAME>

  COMMAND_TYPE:
                -h - help/manual
                -c - return events by type
  COMMAND_NAME:
                all       - return all events
                past      - return past events only
                today     - return today's events only
                future    - return upcoming events only
                cancelled - return all cancelled events
                existing  - return all un-cancelled events
```
Can also try:
```sh
$ python q3.py events.txt -c all
$ python q3.py events.txt -c past
$ python q3.py events.txt -c today
$ python q3.py events.txt -c future
$ python q3.py events.txt -c cancelled
$ python q3.py events.txt -c existing
```
