from graph import *

"""
   Problems:
      BFS doesn't find optimal solution, only 2nd optimal. Presumably it has to do with the fact that python works with references and
      nodes get value from other branch searches and that's why they don't pass cycle detection check.
      
      after we go through path Bu->Fa->Si->Ri ... the Ri value gets overwritten (its 390) and it is never changed to proper value 198.
      
      the problem appears only if we look past Si (like Ze or Ti). If we look for Si, then everything is correct and Path is  278 (optimal one)
      
      different approaches were tried: change complex structures (like node.parent.value) to basic ones (like int), reseting previous Nodes
      after we visit them
"""

romania = Graph( ['Or', 'Ne', 'Ze', 'Ia', 'Ar', 'Si', 'Fa',
 'Va', 'Ri', 'Ti', 'Lu', 'Pi', 'Ur', 'Hi',
 'Me', 'Bu', 'Dr', 'Ef', 'Cr', 'Gi'],
[
   ('Or', 'Ze', 71), ('Or', 'Si', 151),
   ('Ne', 'Ia', 87), ('Ze', 'Ar', 75),
   ('Ia', 'Va', 92), ('Ar', 'Si', 140),
   ('Ar', 'Ti', 118), ('Si', 'Fa', 99),
   ('Si', 'Ri', 80), ('Fa', 'Bu', 211),
   ('Va', 'Ur', 142), ('Ri', 'Pi', 97),
   ('Ri', 'Cr', 146), ('Ti', 'Lu', 111),
   ('Lu', 'Me', 70), ('Me', 'Dr', 75),
   ('Dr', 'Cr', 120), ('Cr', 'Pi', 138),
   ('Pi', 'Bu', 101), ('Bu', 'Gi', 90),
   ('Bu', 'Ur', 85), ('Ur', 'Hi', 98),
   ('Hi', 'Ef', 86)
] )
# romania = Graph( ['Or', 'Ne', 'Ze', 'Ia', 'Ar', 'Si', 'Fa',
#  'Va', 'Ri', 'Ti', 'Lu', 'Pi', 'Ur', 'Hi',
#  'Me', 'Bu', 'Dr', 'Ef', 'Cr', 'Gi'],
# [
#    ('Or', 'Ze', 71), 
#    ('Ne', 'Ia', 87), 
#    ('Ia', 'Va', 92), ('Ar', 'Si', 140),
#    ('Ar', 'Ti', 118), ('Si', 'Fa', 99),
#    ('Si', 'Ri', 80), ('Fa', 'Bu', 211),
#    ('Va', 'Ur', 142), ('Ri', 'Pi', 97),
#    ('Lu', 'Me', 70), ('Me', 'Dr', 75),
#    ('Dr', 'Cr', 120), 
#    ('Pi', 'Bu', 101), 
#     ('Ur', 'Hi', 98),
#    ('Hi', 'Ef', 86)
# ] )

start = "Bu"
end = "Ti"
startNodeIndex = 0
endNodeIndex = 0

for node in romania.nodes:
   if(node.name == start):
      break
   startNodeIndex+=1

for node in romania.nodes:
   if(node.name == end):
      break
   endNodeIndex+=1

romania.print()

print(f"The Lowest Cost way from {start} to {end} is: "+str(bfs(romania.nodes[startNodeIndex],romania.nodes[endNodeIndex])))