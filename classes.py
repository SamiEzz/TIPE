import matplotlib.pyplot as plt
import numpy as np

class Position:
    def __init__(self,_x,_y,_text,_plotStyle="x"):
        self.x = _x
        self.y = _y
        self.text = _text
        self.plotStyle = _plotStyle
    def plot(self):
        plt.plot(self.x,self.y,self.plotStyle)
        plt.text(self.x+2,self.y+2,self.text)
        plt.plot()

class Balise:
    def __init__(self,_position,_errorPercent,_plotStyle="o"):
        self.position = _position
        self.errorPercent = _errorPercent
        self.plotStyle = _plotStyle
        
    def plot(self):
        plt.plot(self.position.x,self.position.y,self.plotStyle)
        
        plt.plot()

class Cercle:
    def __init__(self,_position,_rayon,_plotStyle="--"):
        self.position = _position
        self.rayon = _rayon
        self.plotStyle = _plotStyle
    def plot(self):
        tVect = np.linspace(0,2*np.pi,360)
        xVect=np.cos(tVect)
        yVect=np.sin(tVect)
        plt.plot(xVect,yVect,self.plotStyle)
        plt.plot()

