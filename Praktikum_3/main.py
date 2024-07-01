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
    query = []
    try:
        action = int(input("What to do? WALK  0 TURNLEFT  1 TURNRIGHT  2 GRAB  3 SHOOT  4 CLIMB  5\n"))
    except :
        continue
    if(action == 99):
        query.append(input("Input your query\n"))
    elif(action >=0 and action <=5):
        obs,reward,isTerminated,addInfo = wumpus_env.step(action)
    else:
        continue
    wumpus_env.render()
    kb.tell(obs,reward)
    isEntailed = kb.askNew(query=query)
    if(action == 99):
        print(isEntailed)
    print(f"Knowledge base after step {kb.kb}")
    # print(f"reward: {reward}")
    
