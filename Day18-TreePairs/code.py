from binarytree import Node, get_parent
with open("input.txt", "r") as f:
    inputs = [line.strip() for line in f]

def splitLine(line):
    first = ''
    second = ''
    st = 0
    addToFirst = True
    for x in line:
        if(x == '['):
            st += 1
        if(x == ']'):
            st -= 1

        if(x == ',' and st == 0):
            addToFirst = False
            continue
        if addToFirst:
            first += x
        else:
            second += x
    return first, second

def getTree(line):
    if(',' not in line):
        num = int(line)
        root = Node(num)
        return root

    line = line[1:-1]
    leftPart, rightPart = splitLine(line)
    root = Node(-1)
    root.left = getTree(leftPart)
    root.right = getTree(rightPart)
    return root

def splitDfs(root, changed = False):
    if(root.left):
        if splitDfs(root.left, False):
            return True
    if(root.right):
        if splitDfs(root.right, False):
            return True
    if(not root.left and not root.right and root.value >= 10):
        left = root.value//2
        right = root.value - left
        newLeft = Node(left)
        newRight = Node(right)
        root.value = -1
        root.left = newLeft
        root.right = newRight
        return True
    return changed

def findRightMostLeaf(node):
    while(node.right):
        node = node.right
    return node

def findLeftMostLeaf(node):
    while(node.left):
        node = node.left
    return node

def findLeftNode(root, node):
    if(findLeftMostLeaf(root) == node):
        return None

    parent = get_parent(root, node)
    while True:
        if(parent.left != node):
            break
        if(parent == root):
            break
        node = parent
        parent = get_parent(root, parent)
    return findRightMostLeaf(parent.left)

def findRightNode(root, node):
    if(findRightMostLeaf(root) == node):
        return None

    parent = get_parent(root, node)
    while True:
        if(parent.right != node):
            break
        if(parent == root):
            break
        node = parent 
        parent = get_parent(root, parent)
    return findLeftMostLeaf(parent.right)

def explodeDfs(root, node, currDepth, changed = False):
    if(node.value != -1):
        return False
    if(node.left):
        if explodeDfs(root, node.left, currDepth+1, changed):
            return True    
    if(node.right):
        if explodeDfs(root, node.right, currDepth+1, changed):
            return True

    if(currDepth >= 4 and not changed):
        left = node.left.value
        right = node.right.value
        
        leftNode = findLeftNode(root, node.left)
        if leftNode:
            leftNode.value += left

        rightNode = findRightNode(root, node.right)
        if rightNode:
            rightNode.value += right

        node.value = 0
        node.left = None
        node.right = None
        return True
    return changed

def stringifyTree(root, s = ''):
    if(root is None):
        return "None"
    if(root.value != -1):
        return str(root.value)
    s += '['
    s += stringifyTree(root.left)
    s += ','
    s += stringifyTree(root.right)
    s += ']'
    return s

def reduce(root):
    while True:
        if(explodeDfs(root, root, 0)):
            continue
        if(splitDfs(root)):
            continue
        break

def treeValue(root):
    val = 0
    if root.left:
        val += 3*treeValue(root.left)
    if root.value != -1:
        val += root.value
    if root.right:
        val += 2*treeValue(root.right)
    return val

root = getTree(inputs[0])
cnt = len(inputs)
for line in inputs[1:]:
    cnt -= 1
    newRoot = Node(-1)
    newRoot.left = root
    newRoot.right = getTree(line)
    root = newRoot
    reduce(root)

maxSum = 0
cnt = len(inputs)
for line1 in inputs:
    cnt -= 1
    for line2 in inputs:
        if line1 == line2:
            continue
        newRoot = Node(-1)
        newRoot.left = getTree(line1)
        newRoot.right = getTree(line2)
        reduce(newRoot)
        maxSum = max(treeValue(newRoot), maxSum)

print("Part1: ", treeValue(root))
print("Part2: ", maxSum)

