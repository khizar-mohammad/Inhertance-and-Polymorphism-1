#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy
class Circle:
  self._raduis = 1.0
  self._color = ""
  def __init__(self):
    pass
  def __init__(self,radius):
    self._radius = radius
  def __init__(self,radius,color):
    self._radius = radius
    self._color = color
  def GetRadius(self):
    return self._radius
  def setRadius(self,radius):
    self._radius = radius
  def GetColor(self):
    return self._color
  def SetColor(self,color):
    self._color = color
  def Area(self):
    return np.pi*(self._radius**2)

class cylinder(Circle):
  self.__height = 1.0
  Circle.__init__(self,radius,color)
  def __init__(self):
    pass
  def __init__(self,radius):
    self._radius = radius
  def __init__(self,radius,height):
    self._radius = radius
    self.__height = height
  def __init__(self,radius,height,color):
    self._radius = radius
    self._color = color
    self.__height = height
  def GetHeight(self):
    return self.__height
  def SetHeight(self,height):
    self.__height = height
  def GetVolume(self):
    return np.pi*(self._radius**2)*self.__height

