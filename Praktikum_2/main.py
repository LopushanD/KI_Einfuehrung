from GeneticAlgorithm import *
import seaborn
import pandas
import matplotlib.pyplot as plt

"""
    
"""
    
queens = []
queens2 = ['11111111',"22222222",'33333333','44444444','55555555','66666666','77777777','88888888']
for i in range(8):
    queens.append('')
    for j in range(8):
        queens[i]+= str(random.randint(1,8))


alg = GeneticAlgorithm(queens2,iterationsNumber=100)

# board = Board()
# board.updateBoard(queens[0])
# board.printBoard()

# visualization
data= alg.geneticAlgorithm()
frame = pandas.Series(data)
seaborn.scatterplot(data=frame)
plt.show()



# print(random.random())