from prettytable import PrettyTable
from utils import *
import heapq


class Node:
   """Each node includes edges that connect nodes"""
   def __init__(self, name):
       self.parent = None # Parent Node
       self.name = name #name of our node
       self.edges = [] # options where to go : (ourNode,otherNode,cost)
           
    

class Edge:
   """Part of corresponding code"""
   def __init__(self, edge):
      self.start = edge[0]
      self.end = edge[1]
      self.value:int = edge[2]
   
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
            
         
def bfs(start:Node,end:Node) -> int: # type: ignore 
   if(start.name == end.name):
      return start.value
   
   #initialization
   currentNode:Node = start
   currentNode.parent = currentNode
   minCosts = {start.name: 0}  # Dictionary to store the minimum costs to each node
   exploredWays = []
   q = Queue()
   q.fifoEnque(currentNode)
   
   while(q.fifoNotEmpty()):
      currentNode = q.fifoDeque()
      #print(currentNode.name)
      current_cost = minCosts[currentNode.name]
      
      for edge in currentNode.edges:
         nextNode = edge.end
         newCost = current_cost + edge.value
         # expand all neighboors if they don't lead to cycle
         if(isNotCycle(currentNode,nextNode,newCost,exploredWays)):
            
            # Add or update path cost to the node
            if nextNode.name not in minCosts or newCost < minCosts[nextNode.name]:
                     minCosts[nextNode.name] = newCost
                     nextNode.parent = currentNode 
            #mark way between nodes as explored 
            exploredWays.append((currentNode,nextNode,newCost))
            q.fifoEnque(nextNode)
      
               
   return  minCosts[end.name]
  
def dfs(start:Node,end:Node) -> int: # type: ignore
   if(start.name == end.name):
      return start.value
   currentNode:Node = start
   currentNode.parent = currentNode
   minCosts = {start.name: 0}  # Dictionary to store the minimum costs to each node
   exploredWays = []
   
   q = Queue()
   q.lifoEnque(currentNode)
   
   while(q.lifoNotEmpty()):
      currentNode = q.lifoDeque()
      #print(currentNode.name)
      current_cost = minCosts[currentNode.name]

      for edge in currentNode.edges:
         nextNode = edge.end
         newCost = current_cost + edge.value
         # expand all neighboors if they don't lead to cycle
         if(isNotCycle(currentNode,nextNode,newCost,exploredWays)):
            
            # Add or update path cost to the node
            if nextNode.name not in minCosts or newCost < minCosts[nextNode.name]:
                     minCosts[nextNode.name] = newCost
                     nextNode.parent = currentNode
            #mark way between nodes as explored 
            exploredWays.append((currentNode,nextNode,newCost))
            q.lifoEnque(nextNode)
                  
   return  minCosts[end.name]

def prioSearch(start:Node,end:Node):
   if(start.name == end.name):
      return start.value
   
   currentNode:Node = start
   currentNode.parent = currentNode
   minCosts = {start.name: 0}  # Dictionary to store the minimum costs to each node
   exploredWays = []
   q = Queue()
   q.fifoEnque(currentNode)
   
   while(q.fifoNotEmpty()):
      currentNode = q.fifoDeque()

      nextNodeList:list[tuple] = []
      newCostList:int = []
      currentCost = minCosts[currentNode.name]
      
      for edge in currentNode.edges:
         nextNode = edge.end
         newCost = currentCost + edge.value
         
         # expand all neighboors if they don't lead to cycle
         if(isNotCycle(currentNode,nextNode,newCost,exploredWays)):
            newCostList.append(newCost)
            nextNodeList.append((nextNode,newCost))
            
            # Add or update path cost to the node
            if nextNode.name not in minCosts or newCost < minCosts[nextNode.name]:
                     minCosts[nextNode.name] = newCost
                     nextNode.parent = currentNode  
            exploredWays.append((currentNode,nextNode,newCost))
      # 
      newCostList =sorted(newCostList)
      #sortedNextNodeList = []
      
      # imitate priority queue by inserting lowest cost node into regular queue first
      # like thirdLowest -> secondLowest -> lowest
      for i in newCostList:
         # n - node, ii- cost
         for n,ii in nextNodeList:
            #needed because newCostList is sorted, but nextNodeList is in chaotic order.
            if(i == ii):
               q.fifoEnque(n)
               break
               

               
               
         #q.fifoEnque(nextNode)
   return  minCosts[end.name]
    
                   
            