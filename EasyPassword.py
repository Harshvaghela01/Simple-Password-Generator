#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install SimpleGUICS2pygame


# In[ ]:





# In[5]:


import random


# In[7]:


import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# In[8]:


import math


# In[12]:


import random

def generate_random_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=[]{}|:;,.<>?/"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()_-+=[]{}|:;,.<>?/" for char in password)

    strength = 0
    if length >= 8:
        strength += 1
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    return strength

# Generate a random password
password_length = 10
password = generate_random_password(password_length)

# Check the strength of the password
password_strength = check_password_strength(password)

# Print the generated password and its strength
print("Generated Password:", password)
print("Password Strength:", password_strength)


# In[ ]:





# In[ ]:




