import gym
import fh_ac_ai_gym # type: ignore
from  KnowledgeBase import *

"""
Known bugs: 
"""

timeStamp:int = 0
kb = KnowledgeBase()
wumpus_env = gym.make('Wumpus-v0',disable_env_checker=True)
isTerminated = False
obs= wumpus_env.reset()
wumpus_env.render()
kb.tell(obs,0,timeStamp)
print(f"Knowledge base after step {kb.kb}")
# while not isTerminated:
#     kb.tell(obs,timeStamp)
#     obs,reward,isTerminated,addInfo = wumpus_env.step(kb.ask(timeStamp))
#     wumpus_env.render()
while True:
    action = int(input("What to do? WALK  0 TURNLEFT  1 TURNRIGHT  2 GRAB  3 SHOOT  4 CLIMB  5\n"))
    timeStamp+=1
    obs,reward,isTerminated,addInfo = wumpus_env.step(action)
    wumpus_env.render()
    kb.tell(obs,reward,timeStamp)
    print(f"Knowledge base after step {kb.kb}")
    # print(f"reward: {reward}")
    