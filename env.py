#!/usr/bin/env python
# coding: utf-8

# In[4]:


# import lib

import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import time


# In[5]:


SIZE = 25           # screen size


# In[6]:


class Env:
    def __init__(self):
        self.x = np.random.randint(0, SIZE)
        self.y = np.random.randint(0, SIZE)
        
    def __str__(self):
        return f"{self.x},{self.y}"
        
    def __sub__(self, other):
        return (self.x-other.x, self.y-other.y)
    
    def action_A(self, action):   # agent_A can perform 4 actions with 2x speed
        if action == 0:
            self.move_A(x=2, y=0)
        elif action == 1:
            self.move_A(x=-2, y=0)
        elif action == 2:
            self.move_A(x=0, y=2)
        elif action == 3:
            self.move_A(x=0, y=-2)
        return self.x, self.y
            
    def move_A(self, x=False, y=False):
        if not x:
            
            self.x += np.random.randint(-1, 2)
            
        else:
            self.x += x
            
        if not y:
            self.y += np.random.randint(-1, 2)
        else:
            self.y += y
            
        if self.x < 0:                             # we dont wont to go off screen!
            self.x = 0
        elif self.x > SIZE-1:
            self.x = SIZE-1
        if self.y < 0:
            self.y = 0
        elif self.y > SIZE-1:
            self.y = SIZE-1

        return self.x, self.y
    
    def action_B(self, action):   # agent_B can perform 4 actions with 1x speed
        if action == 0:
            self.move_B(x=1, y=0)
        elif action == 1:
            self.move_B(x=-1, y=0)
        elif action == 2:
            self.move_B(x=0, y=1)
        elif action == 3:
            self.move_B(x=0, y=-1)
        return self.x, self.y
            
    def move_B(self, x=False, y=False):
        if not x:
            
            self.x += np.random.randint(-1, 2)
            
        else:
            self.x += x
            
        if not y:
            self.y += np.random.randint(-1, 2)
        else:
            self.y += y
            
        if self.x < 0:                             # we dont wont to go off screen!
            self.x = 0
        elif self.x > SIZE-1:
            self.x = SIZE-1
        if self.y < 0:
            self.y = 0
        elif self.y > SIZE-1:
            self.y = SIZE-1

        return self.x, self.y
    
    
    
    def enemy_move(self):                          # optional if you want to move your enemy rendomly!!
        self.x += np.random.randint(-1, 2)
        self.y += np.random.randint(-1, 2)
        
        if self.x < 0:
            self.x = 0
        elif self.x > SIZE-1:
            self.x = SIZE-1
        if self.y < 0:
            self.y = 0
        elif self.y > SIZE-1:
            self.y = SIZE-1
        return self.x, self.y


# In[7]:


Agent_A = Env()             # to check everything is all right!!
Agent_B = Env()
Enemy = Env()

print(Agent_A)
print(Agent_B)
print(Enemy)

print(Agent_A.move_A)
print(Agent_B.move_B)
print(Enemy.enemy_move)

print(Agent_A.action_A(2))
print(Agent_B.action_B(2))



# In[ ]:




