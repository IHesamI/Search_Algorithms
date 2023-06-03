def get_min_node(Node1,Node2):
    if Node1.value<Node2.value:
        return Node1
    return Node2

def get_max_node(Node1,Node2):
    if Node1.value>Node2.value:
        return Node1
    return Node2

class Node :
    def __init__(self,value,id) -> None:
        self.id=id
        self.value=value
        self.choosenNode=None
    def __str__(self) -> str:
        return 'Optimal value: '+  str(self.value)+' , '+self.id
    def get_id(self):
        return self.id
class ParentNode(Node):
    def __init__(self, is_maxinmiser ,id,value=None) -> None:
        super().__init__(value,id)
        self.is_maxinmiser:bool=is_maxinmiser
        self.choosenNode:Node=None
    
    def set_chooseNode(self,Node1:Node,Node2:Node):
        if self.is_maxinmiser:
            self.choosenNode=get_max_node(Node1,Node2)
        else:
            self.choosenNode=get_min_node(Node1,Node2)
        self.value=self.choosenNode.value    
    
    def __str__(self) -> str:
        return self.id

def print_tree(root:ParentNode):
    node=root
    while node!=None:
        print(node)
        node=node.choosenNode
    
def Min_Max_Simple(list_of_nodes,is_max,id):
    root_=None
    while True:
        templist=[]
        for i in range(0,len(list_of_nodes),2):
            node1=list_of_nodes[i]
            node2=list_of_nodes[i+1]
            Pnode=ParentNode(is_max,chr(id))
            Pnode.set_chooseNode(node1,node2)
            pnodes.append(Pnode.get_id())
            id+=1        
            templist.append(Pnode)
        list_of_nodes=templist
        is_max=not is_max
        if len(templist)==1:
            root_=templist[0]
            break
    return root_

def display_tree(chars):
    num_levels = 0
    total_nodes = 0

    while total_nodes < len(chars):
        num_levels += 1
        total_nodes += 2 ** num_levels

    current_index = len(chars) - 1
    for level in range(num_levels):
        level_nodes = 2 ** level
        level_chars = chars[current_index - level_nodes + 1: current_index + 1]
        print(" " * (num_levels - level), end="")
        print(" ".join(level_chars))
        current_index -= level_nodes


tree=[]
pnodes=[]
listofvalues=[3, 5, 2, 9, 12, 5, 23, 23]
is_max=True
id=ord('A')
list_of_nodes=[]
for i in range(0,len(listofvalues),2):
    # print(i,listofvalues[i])
    node1=Node(listofvalues[i],chr(id))
    tree.append(node1.get_id())
    id+=1
    node2=Node(listofvalues[i+1],chr(id))
    tree.append(node2.get_id())
    id+=1
    Pnode=ParentNode(is_max,chr(id))
    pnodes.append(Pnode.get_id())
    Pnode.set_chooseNode(node1,node2)
    list_of_nodes.append(Pnode)
    id+=1
is_max=False
root_node=Min_Max_Simple(list_of_nodes,is_max,id)
tree.extend(pnodes)    
display_tree(tree)   
print('--------------') 
print_tree(root_node)
