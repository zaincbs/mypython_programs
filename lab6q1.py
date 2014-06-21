# lab 6 _ 3

def LastFirst(name):
    parts = name.split()
    return parts[-1] + ', ' +' '.join(parts[:-1])

names = ["zain ijaz", "hamza nauman", "arfa karim",
         "Asfa bibi", "Bullah Shah"]


print Last 
for name in sorted(names, key=LastFirst):
    print LastFirst(name)
