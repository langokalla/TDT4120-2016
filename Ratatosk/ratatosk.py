from sys import stdin


class Node:
    def __init__(self):
        self.child = []
        self.ratatosk = False
        self.next_child = 0


def dfs(root):
    stack = [root]
    while stack:
        this = stack[len(stack) - 1]
        if this.ratatosk:
            return len(stack) - 1
        if this.next_child == len(this.child):
            stack.pop()
        else:
            stack.append(this.child[this.next_child])
            this.next_child += 1


def bfs(root):
    queue = [(root, 0)]
    while len(queue) > 0:
        this, depth = queue.pop(0)
        if this.ratatosk:
            return depth
        for c in this.child:
            queue.append((c, depth + 1))


function = stdin.readline().strip()
number_of_nodes = int(stdin.readline())
nodes = []
for i in range(number_of_nodes):
    nodes.append(Node())
start_node = nodes[int(stdin.readline())]
ratatosk_node = nodes[int(stdin.readline())]
ratatosk_node.ratatosk = True
for line in stdin:
    number = line.split()
    temp_node = nodes[int(number.pop(0))]
    for child_number in number:
        temp_node.child.append(nodes[int(child_number)])

if function == 'dfs':
    print(dfs(start_node))
elif function == 'bfs':
    print(bfs(start_node))
elif function == 'velg':
    print(bfs(start_node))