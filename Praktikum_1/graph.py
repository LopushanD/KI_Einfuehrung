from prettytable import PrettyTable
from utils import *


class Node:
   """Each node includes edges that connect nodes"""
   def __init__(self, name):
       self.parent = 0 #cost of the way until now
       self.name = name #name of our node
       self.edges = [] # options where to go : (ourNode,otherNode,cost)
       self.value = 0 # ??
       self.explored=False
       
   def printNode(self):
      print("name, value, parent")
      print(self.name,end=' ')
      print(self.value,end=' ')
      print(self.parent)
      print("edges, costs")
      for edge in self.edges:
         edge.printEdge()
      
    

class Edge:
   """Part of corresponding code"""
   def __init__(self, edge):
      self.start = edge[0]
      self.end = edge[1]
      self.value = edge[2]
   
   def printEdge(self):
      print(self.start.name,end=' -> ')
      print(self.end.name,end=' ')
      print(self.value)


class Graph:
   """Group of nodes"""
   def __init__(self, node_list, edges):
      self.nodes:Node = []
      for name in node_list:
         self.nodes.append(Node(name))

      for e in edges:
        e = (getNode(e[0],self.nodes), getNode(e[1], self.nodes), e[2])        

        self.nodes[next((i for i,v in enumerate(self.nodes) if v.name == e[0].name), -1)].edges.append(Edge(e))
        self.nodes[next((i for i,v in enumerate(self.nodes) if v.name == e[1].name), -1)].edges.append(Edge((e[1], e[0], e[2])))


   def print(self):
      node_list = self.nodes
      
      t = PrettyTable(['  '] +[i.name for i in node_list])
      for node in node_list:
         edge_values = ['X'] * len(node_list)
         for edge in node.edges:
            edge_values[ next((i for i,e in enumerate(node_list) if e.name == edge.end.name) , -1)] = edge.value           
         t.add_row([node.name] + edge_values)
      print(t)
            
         
def bfs(cities:Graph,start:Node,end:Node,tracker:Tracker) -> int: # type: ignore # later change return value to int
    if(start.name == end.name):
        return start.parent
    # start.explored = True
    nextNode:Node = start
    q = Queue()
    q.fifoEnque(start)
    while(q.fifoNotEmpty()):
        nextNode = q.fifoDeque()
        nextNode.explored = True
        # tracker.update(nextNode)
        for edge in nextNode.edges:
            
            q.fifoEnque(edge.end)
        
    
    return -1  
    
    
                   
            