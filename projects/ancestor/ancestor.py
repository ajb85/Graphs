class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Ancestry:
    def __init__(self):
        self.people = {}
    
    def add_people(self, people):
        if(people not in self.people):
            self.people[people] = set()
        else:
            print(f"{people} already in the Ancestry")
    
    def add_edge(self, parent, child):
        if(parent not in self.people or child not in self.people):
            print ("Both parent and child must exist before creating a connection")
            return
        elif(len(self.people[child]) >= 2):
            print("Child already has two parents.")
            return
        self.people[child].add(parent)

    def earliest_ancestor(self, starting_people):
        visited = set()
        s = Stack()
        s.push([starting_people])
        lineages = {}
        while(s.size() > 0):
            lineage = s.pop()
            c = lineage[-1]
            if(not c in visited):
                visited.add(c)
                if(not len(self.people[c])):
                    length = len(lineage)
                    if(length in lineages):
                        lineages[length].append(lineage)
                    else:
                        lineages[length] = [lineage]
                else:
                    for parent in self.people[c]:
                        s.push([*lineage, parent])
        longest = max(lineages.keys())
        last = []
        for line in lineages[longest]:
            last.append(line[-1])
        return last[0] if len(last) == 1 else last


ancestors = Ancestry()

for i in range(1,12):
    ancestors.add_people(i)

ancestors.add_edge(10, 1)
ancestors.add_edge(1, 3)
ancestors.add_edge(2, 3)
ancestors.add_edge(4, 5)
ancestors.add_edge(4, 8)
ancestors.add_edge(11, 8)
ancestors.add_edge(3, 6)
ancestors.add_edge(5, 6)
ancestors.add_edge(5, 7)
ancestors.add_edge(8, 9)

print(ancestors.people)

print(ancestors.earliest_ancestor(6))