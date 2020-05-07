def check1(l):
    List = []
    count = 0
    index = 0
    for i in l:
        for j in i:
            List.append(j)
    for i in range(0, len(List)):
        for j in range(i, len(List)):
            if (List[i] != 0 and List[j] != 0):
                if (List[i] > List[j]):
                    count += 1
            else:
                if (List[i] == 0):
                    index = i
                else:
                    index = j
    if (count % 2 == 0):
        if (0 in l[1]):
            return True
        if (0 in l[3]):
            return True
        return False
    else:
        if (0 in l[0]):
            return True
        if (0 in l[2]):
            return True
        return False
    
def check2(l):
    List = []
    count = 0
    index = 0
    for i in l:
        for j in i:
            List.append(j)
    for i in range(0, len(List)):
        for j in range(i, len(List)):
            if (List[i] != 0 and List[j] != 0):
                if (List[i] > List[j]):
                    count += 1
            else:
                if (List[i] == 0):
                    index = i
                else:
                    index = j
    if (count % 2 == 0):
        if (0 in l[0]):
            return True
        if (0 in l[2]):
            return True
        return False
    else:
        if (0 in l[1]):
            return True
        if (0 in l[3]):
            return True
        return False

import copy

def moveLeft(x):
    i, j = 0, 0
    for k in range(0, 4):
        if 0 in x[k]:
            i = k
            j = x[k].index(0)
    try:
        x[i][j], x[i][j-1] = x[i][j-1], x[i][j]
        return x
    except:
        return None

def moveRight(x):
    i, j = 0, 0
    for k in range(0, 4):
        if 0 in x[k]:
            i = k
            j = x[k].index(0)
    try:
        x[i][j], x[i][j+1] = x[i][j+1], x[i][j]
        return x
    except:
        return None
    
def moveUP(x):
    i, j = 0, 0
    for k in range(0, 4):
        if 0 in x[k]:
            i = k
            j = x[k].index(0)
    try:
        x[i][j], x[i-1][j] = x[i-1][j], x[i][j]
        return x
    except:
        return None

def moveDown(x):
    i, j = 0, 0
    for k in range(0, 4):
        if 0 in x[k]:
            i = k
            j = x[k].index(0)
    try:
        x[i][j], x[i+1][j] = x[i+1][j], x[i][j]
        return x
    except:
        return None


class Node:
    def __init__(self,key):
        self.first = None
        self.third = None
        self.fourth = None
        self.second = None
        self.val = key

queue = []
ans = ""

def run(goal, s):
    global root
    global ans
    c = 0
    if (0 in goal[0]):
        if (check2(root.val) == False):
            print ("Not Possible")
            return False
    elif (check1(root.val) == False):
        print ("Not Possible")
        return False
    while (ans == ""):
        solve(root, goal, s, c)
        c += 1
    print ("Answer: ", ans, "Answer Found At Depth: ", c-1)
    root = None
    queue = None
    ans = ""

def solve(root, goal, s, level = 0):
    global queue
    global ans
    if (root == None):
            return
    if (ans != ""):
        return
    if (level == -1):
        return
    if (level == 0):
        if (root.val not in queue):
            queue.append(copy.deepcopy(root.val))
        if (root.val == goal):
            queue.clear()
            ans = s
            return
        queue.pop(0)
        temp = moveLeft(copy.deepcopy(root.val))
        if (temp != None):
            insert(root, Node(copy.deepcopy(temp)))
            queue.append(copy.deepcopy(temp))
        temp = []
        temp = moveRight(copy.deepcopy(root.val))
        if (temp != None):
            insert(root, Node(moveRight(copy.deepcopy(root.val))))
            queue.append(copy.deepcopy(temp))
        temp = []
        temp = moveUP(copy.deepcopy(root.val))
        if (temp != None):
            insert(root, Node(moveUP(copy.deepcopy(root.val))))
            queue.append(copy.deepcopy(temp))
        temp = []
        temp = moveDown(copy.deepcopy(root.val))
        if (temp != None):
            insert(root, Node(moveDown(copy.deepcopy(root.val))))
            queue.append(copy.deepcopy(temp))
        temp = []
    solve(root.first, goal, s + "Left ", level - 1)
    solve(root.second, goal, s + "Right ", level - 1)
    solve(root.third, goal, s + "UP ", level - 1)
    solve(root.fourth, goal, s + "Down ", level - 1)

def insert(root,node):
    if root is None:
        root = node
        return
    if (root.first is None):
        root.first = node
        return
    if (root.second is None):
        root.second = node
        return
    if (root.third is None):
        root.third = node
        return
    if (root.fourth is None):
        root.fourth = node
        return

    
####                             Test Case 1

root = Node([[4,1,2,3],[5,6,10,7],[8,13,9,11],[12,0,14,15]])
goal = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
run(goal, "")


####                             Test Case 2

root = Node([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,0, 15]])
goal = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
run(goal, "")

####                              Test Case 3

root = Node([[1,2,3,0],[4,5,6,7],[8,9,10,11],[12,13,14,15]])
goal = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
run(goal, "")

####                              Test Case 4

root = Node([[0,9,8,1],[4,5,6,7],[2,3,10,11],[12,13,14,15]])
goal = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
run(goal, "")
