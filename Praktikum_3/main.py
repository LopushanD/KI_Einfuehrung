import gym
import fh_ac_ai_gym # type: ignore
from  KnowledgeBase import *


timeStamp:int = 0
kb = KnowledgeBase()
wumpus_env = gym.make('Wumpus-v0',disable_env_checker=True)
isTerminated = False
obs= wumpus_env.reset()
kb.tell(obs,0,timeStamp)
wumpus_env.render()
print(kb.kb)
# while not isTerminated:
#     kb.tell(obs,timeStamp)
#     obs,reward,isTerminated,addInfo = wumpus_env.step(kb.ask(timeStamp))
#     wumpus_env.render()
while True:
    action = int(input("What to do? WALK  0 TURNLEFT  1 TURNRIGHT  2 GRAB  3 SHOOT  4 CLIMB  5\n"))
    timeStamp+=1
    obs,reward,isTerminated,addInfo = wumpus_env.step(action)
    kb.tell(obs,reward,timeStamp)
    wumpus_env.render()
    print(kb.kb)
    print(f"reward: {reward}")
    
    
    """
    For now if we have some fact like W10, assumptions like W10 v W12 v W21 will be added. Need to implement scanning of facts, before assumptions are added
    """
    

# kb.tell(obs,timeStamp)
# print(obs)    
# print(kb.kb)
# # print(kb.kb)
# print(obs,end='\n\n')
# # print(reward,end='\n\n')
# print(isTerminated,end='\n\n')
# # print(addInfo,end='\n\n')
# # wumpus_env.render()
# # wumpus_env.render()