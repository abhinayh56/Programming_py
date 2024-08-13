import math

def inch2cm(inch):
    return inch * 2.54

def cm2inch(cm):
    return cm/2.54

class Angle:
    def rad2deg(self, rad):
        return rad*180.0/math.pi
    
    def deg2rad(self, deg):
        return deg*math.pi/180.0