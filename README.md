# Automation
automating AWS with Python using boto3 library 

boto3.py menu output:
```
$ python3 testall.py 

- - - - - - - - - - - - - - - - - - - - 
menu:
~~~~~
1.deploy instances
2.terminate instance
3.start instance
4.stop instance
5.get information about instance
- - - - - - - - - - - - - - - - - - - -

choose(1-5):1

available images:

name: Ubuntu Server 18.04 (simple)
ID:   ami-0dd9f0e7df0f0a138

name: Ubuntu Server 18.04 (with Docker [private ami])
ID:   ami-019f6f20ec51566bc

name: Red Hat Enterprise Linux 8 (HVM)
ID:   ami-03d64741867e7bb94
    
insert ImageID: ami-0dd9f0e7df0f0a138
insert amount: 3

answer: 1

do you want to exit? (yes/no)
answer: no

- - - - - - - - - - - - - - - - - - - - 
menu:
~~~~~
1.deploy instances
2.terminate instance
3.start instance
4.stop instance
5.get information about instance
- - - - - - - - - - - - - - - - - - - -

choose(1-5):5

ID: i-0b6884a18d1aff5ac
Public IP Address: no connection
Status: stopped

--------------------------------------

ID: i-0375b3f0ad6d50e57
Public IP Address: no connection
Status: stopped

--------------------------------------

ID: i-04ef2cf2320a18de2
Public IP Address: no connection
Status: stopped

--------------------------------------

ID: i-091147d609daa023d
Public IP Address: no connection
Status: stopped

--------------------------------------

ID: i-0ecf788273bc0a653
Public IP Address: 3.17.78.185
Status: pending

--------------------------------------

ID: i-07080605da442dd8a
Public IP Address: 18.216.198.248
Status: pending

--------------------------------------

ID: i-0221a463087a3344d
Public IP Address: 18.222.113.251
Status: pending

--------------------------------------

ID: i-0f4e90724874287be
Public IP Address: 13.58.125.125
Status: running

--------------------------------------

ID: i-02323027775bb85e3
Public IP Address: 18.218.228.238
Status: running

--------------------------------------

do you want to exit? (yes/no)
answer: yes
Bye..


```
