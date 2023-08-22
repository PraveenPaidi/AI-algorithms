#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.f = 0
    def __eq__(self, other):
        return self.position == other.position

    
#This function return the path of the search
def return_path(Frontier_node,maze):
    path = []
    no_rows, no_columns = np.shape(maze)
    result = [[-1 for i in range(no_columns)] for j in range(no_rows)]
    Frontier = Frontier_node
    
    while Frontier is not None:
        path.append(Frontier.position)
        Frontier = Frontier.parent

    path = path[::-1]
    start_value = 0
    
    for i in range(len(path)):
        result[path[i][0]][path[i][1]] = start_value
        start_value += 1
    return result

def visit(unexplored_list, explored_list):
    
    unexplored_list = sorted(unexplored_list, key=lambda x: x.f)      
    Frontier_node = unexplored_list[0]
    del unexplored_list[0]
    explored_list.append(Frontier_node)
    
    return explored_list, unexplored_list,Frontier_node

def Chidren_nodes(no_rows,no_columns, node_position, Frontier_node):
    if 0 <= node_position[0] < no_rows and 0<= node_position[1] < no_columns and maze[node_position[0]][node_position[1]]==0:
                
        # Create new node
        new_node = Node(Frontier_node, node_position)
        return new_node
    else:
        return None
        
    
def Total_cost(Frontier_node, cost, child, end_node):
    # Finding only the absolute value from the start node to the current node
    child.f = Frontier_node.f + cost
    
    return child.f
    
def search(maze, cost, start, end):

    start_node = Node(None, tuple(start))
    end_node = Node(None, tuple(end))
    unexplored_list = []  
    explored_list = [] 
    unexplored_list.append(start_node)
    move  =  [[-1, 0 ], [ 0, -1],  [ 1, 0 ],[ 0, 1 ]]  # UP, left, Down, right 
    no_rows, no_columns = np.shape(maze)
    
    i=0
    while len(unexplored_list) > 0:
                      
        explored_list, unexplored_list, Frontier_node= visit(unexplored_list, explored_list)
                  
        if Frontier_node == end_node:
            return return_path(Frontier_node,maze)
        
        # Generate children from all adjacent squares
        children = []

        for new_position in move: 
            
            # Get node position
            node_position = (Frontier_node.position[0] + new_position[0], Frontier_node.position[1] + new_position[1])
            chi= Chidren_nodes(no_rows,no_columns, node_position, Frontier_node)
            
            if chi is not None:
                children.append(chi)


        # Loop through children
        for child in children:
            
            j=0
                       
            for i in explored_list:
                if i == child:
                    j=1      
                    
            if j==1:
                continue
           
            
            child.f =Total_cost(Frontier_node, cost, child, end_node)
            
            j=0
            # Child is already in the unexplored list and g cost is already lower
            for i in unexplored_list:
                if i == child and child.f > i.f:
                    j=1
                   
                    
            if j==1:
                continue
            

            # Add the child to the unexplored list
            unexplored_list.append(child)
            

            
if __name__ == '__main__':

    maze = [[0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0]]
    
    start = [0, 0] # starting position
    end = [4,5] # ending position
    cost = 1 # cost per movement

    path = search(maze,cost, start, end)
    print('\n'.join([''.join(["{:" ">3d}".format(item) for item in row]) 
      for row in path]))
    


# In[ ]:




