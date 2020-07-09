#!/usr/bin/env python
# coding: utf-8

# In[1]:


def check_not_a_number(*args):
    for x in args:
        if not (isinstance(x, (int, float))):
            return False
    return True


def add_numbers(*args):
    s = 0
    for x in args:
        s += x
    return s


my_name = "Python Course"

