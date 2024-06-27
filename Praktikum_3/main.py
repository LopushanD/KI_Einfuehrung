import gym
import fh_ac_ai_gym # type: ignore
from  KnowledgeBase import *


timeStamp:int = 0
kb = KnowledgeBase()
wumpus_env = gym.make('Wumpus-v0',disable_env_checker=True)
isTerminated = False
obs= wumpus_env.reset()
wumpus_env.render()
# while not isTerminated:
#     kb.tell(obs,timeStamp)
#     obs,reward,isTerminated,addInfo = wumpus_env.step(kb.ask(timeStamp))
#     wumpus_env.render()

kb.tell(obs,timeStamp)
# print(obs)    
# print(kb.kb)
# # print(kb.kb)
# print(obs,end='\n\n')
# # print(reward,end='\n\n')
# print(isTerminated,end='\n\n')
# # print(addInfo,end='\n\n')
# # wumpus_env.render()
# # wumpus_env.render()