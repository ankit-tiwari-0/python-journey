def servea_chai():
    yield "cu 1: jejjej"
    yield "cu 3: jejjej"
    yield "cu 2: jejjej"

stall = servea_chai()

for cup in stall:
    print(cup)


def get_chai_list():
        return ["cup 1", "cup 2", "cup 3"]
chhhh= get_chai_list() 
print(chhhh)

# generator function

def grt_chai_gen ():
     yield "Cup 1"
     yield "cup 2"
     yield "cup 3"

chai = grt_chai_gen()
print(next(chai))     
print(next(chai))     
print(next(chai))     
#print(next(chai))  give error   