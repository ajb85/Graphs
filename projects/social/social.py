import random

class Queue:
    def __init__(self):
        self.storage = []
    def enqueue(self, value):
            self.storage.append(value)
    def dequeue(self):
        if(len(self.storage) > 0):
            return self.storage.pop(0)
        return None
    def size(self):
        return len(self.storage)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph

        # Instead of creating all possible combinations, I wanted to try generating a random 
        # number of random user numbers.  While I do have 3 nested loops (n*avgNumFriends*randomNumber), n should stay
        # relatively small.  If I created a list of all possible friends, I'd have an (n^2) operation
        # and I believe my random number approach will scale better. 
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        for i in range(1, numUsers+1):
            self.users[i] = set()
        n = avgFriendships*numUsers // 2
        for user in range(1, numUsers+1):
            numFriends = n if user == numUsers else random.randint(0,avgFriendships)
            for f in range(numFriends):
                if(n > 0):
                    newFriend = random.randint(1, numUsers)
                    while(newFriend in self.users[user] or newFriend == user):
                        newFriend = random.randint(1, numUsers)
                    self.users[user].add(newFriend)
                    self.users[newFriend].add(user)
                    n -=1

    def getAllSocialPaths(self, userID):
        
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        q.enqueue([userID])
        while(q.size()>0):
            print("q>0", q.size())
            path = q.dequeue()
            u = path[-1]
            if(u not in visited):
                visited[u] = path
                for friend in self.users[u]:
                    q.enqueue([*path, friend])
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
