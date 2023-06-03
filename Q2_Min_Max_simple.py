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
        return str(self.value)+' , '+chr(id)

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
    
listofvalues=[3, 5, 2, 9, 12, 5, 23, 23]
is_max=True
id=ord('A')
list_of_nodes=[]
for i in range(0,len(listofvalues),2):
    node1=Node(listofvalues[i],chr(id))
    id+=1
    node2=Node(listofvalues[i+1],chr(id))
    id+=1
    Pnode=ParentNode(is_max,chr(id))
    Pnode.set_chooseNode(node1,node2)
    list_of_nodes.append(Pnode)
    id+=1
is_max=False
root_node=None

while True:
    templist=[]
    for i in range(0,len(list_of_nodes),2):
        node1=list_of_nodes[i]
        node2=list_of_nodes[i+1]
        Pnode=ParentNode(is_max,chr(id))
        Pnode.set_chooseNode(node1,node2)
        id+=1
        templist.append(Pnode)
    list_of_nodes=templist
    is_max=not is_max
    if len(templist)==1:
        root_node=templist[0]
        break
    
print_tree(root_node)
