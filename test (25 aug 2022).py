#!/usr/bin/env python
# coding: utf-8

# In[23]:


def findMax(arr):
    max = 0
    for i in arr:
        if i > max:
            max = i
    return max


# In[25]:


findMax([8,5,9,2,3,7,0,1,900,902])


# In[11]:


def char(string):
    char = 0
    digits = 0
    for s in string:
        if s.isalpha():
            char += 1
        elif s.isdigit():
            digits += 1
    return f"Letters: {char} \nDigits: {digits}" 


# In[28]:


char("hfhghrt456565njhjhj")


# In[29]:


def maxWord(string):
    string = string.split(" ")
    maxword = ''
    for s in string:
        if len(s) > len(maxword):
            maxword = s
    return maxword


# In[30]:


maxWord("Hello there i am here what are you looking for ")


# In[21]:


print(findMax([8,5,2,3,7,0,1]))


# In[22]:


print(findMax([8,5,9,2,3,7,0,1,900]))


# In[12]:


print(char('hello world! 123'))


# In[18]:


print(maxWord("The quick brownaa fox jumps over the lazy dog."))


# In[92]:


class Line():
    def __init__(self, x1, y1, x2, y2):
        self.coord1 = (x1, y1)
        self.coord2 = (x2, y2)
        
    def isLine(self):
        if self.coord1 == self.coord2:
            return "Not a Line"
        else:
            return "Line"
        
    def length(self):
        dx = (self.coord2[0] - self.coord1[0]) **2
        dy = (self.coord2[1] - self.coord1[1]) **2
        d = (dx + dy) ** 1/2
        return d
    
    def slop(self):
        dy = self.coord2[1] - self.coord1[1]
        dx = self.coord2[0] - self.coord1[0]
        m = dy / dx
        return  m
    
    def isParallel(self,Line):
        if slop1 == slop2:
            return "Lines are parallel"
        else:
            return "Lines are not parallel"
        
    def line_relationship(self, slop1, slop2):
        if slop1 * slop2 == -1:
            return "Lines are Perpendicular"
        elif slop1 == slop2:
                return "Lines are parallel"
        else:
            return "Neither Parallel nor perpendicular"
        


# In[93]:


line = Line(2,3, 4,5)


# In[94]:


line.isLine()


# In[95]:


line.length()


# In[96]:


line.slop()


# In[97]:


line2 = Line(2, 3, 4, 5)


# In[98]:


slop1 = line.slop()


# In[99]:


slop2 = line2.slop()


# In[88]:


line.isParallel(slop1, slop2)


# In[89]:


line + line2


# In[100]:


line.line_relationship(slop1,slop2)


# In[ ]:




