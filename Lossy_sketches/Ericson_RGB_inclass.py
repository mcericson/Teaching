
#Arch 441//Medium//Fall 2021//Ericson
#
#Mark Ericson
#10.25.21
#
#Attractor RGB Cube
#This project creates an object by deforming and altering an RGB cube with a point attractor
#
#Source:  
#Source:
#source:
#
#*****************************************************************************
#imported Libraries
#
import rhinoscriptsyntax as rs
import Rhino  
import System
import scriptcontext as sc
import math
#
#*****************************************************************************
#Functions:


def Cube(Center,Radius):
    #Function to create cube centered on a point. 
    
    #get the x,y,z values from the inputed tuple "center"
    Cx = rs.PointCoordinates(Center)[0]
    Cy = rs.PointCoordinates(Center)[1]
    Cz = rs.PointCoordinates(Center)[2]
    
    #lower 4 points
    p1 = (Cx-Radius,Cy-Radius,Cz-Radius)
    p2 = (Cx+Radius,Cy-Radius,Cz-Radius)
    p3 = (Cx+Radius,Cy+Radius,Cz-Radius)
    p4 = (Cx-Radius,Cy+Radius,Cz-Radius)
    
    #upper 4 points
    p5 = (Cx-Radius,Cy-Radius,Cz+Radius)
    p6 = (Cx+Radius,Cy-Radius,Cz+Radius)
    p7 = (Cx+Radius,Cy+Radius,Cz+Radius)
    p8 = (Cx-Radius,Cy+Radius,Cz+Radius)
    
    #make a box
    Box = rs.AddBox([p1,p2,p3,p4,p5,p6,p7,p8])
    
    #return the box
    return(Box)

def TupleMult(Tuple1,Tuple2):
    Values = []
    for i in range(len(Tuple1)):
        value = float(Tuple1[i]) * float(Tuple2[i])
        Values.append(abs(value))
        Tup = tuple(Values)
    return(Tup)

def ThreeDGrid(Xnumber,Ynumber,Znumber,Space):
    
    Xn = int(Xnumber)
    Yn = int(Ynumber)
    Zn = int(Znumber)
    
    Sp = int(Space)
    Points = []
    for i in range(0,Xn,Space):
        x = i
    
        for i in range(0,Yn,Space):
            y = i
        
            for i in range(0,Zn,Space):
                z = i
                Points.append((x,y,z))
    return(Points)



#*****************************************************************************
#MAIN
#Place all functions to be called inside the Main() function.
#Call the Main function when complete50
def Main():
    CubeSize = rs.GetInteger("What size should each cube be",minimum=1, maximum=50)
    Number = rs.GetInteger("How many cubes along a single edge of the cube", minimum=2, maximum=20)


    #BaseColor
    
    R = float(255)
    G = float(255)
    B = float(255)
    BaseColor = (R,G,B)


    #Create a 3D grid of coordinates

    Points1 = ThreeDGrid(Number, Number, Number,CubeSize)


    #place a cube centered on each coordinate and color based on its position in space relative to the RGB scalar

    for i in Points1:

        point = rs.AddPoint(i)
        Box = Cube(point,.5)
        Scale = float(1.0)/float((CubeSize*Number))
        Point = rs.PointCoordinates(point)
        Scalar = TupleMult(Point,(Scale,Scale,Scale))
        RColor = TupleMult(Scalar,BaseColor)
        Color = rs.CreateColor(RColor)
        rs.AddMaterialToObject(Box)
        Index = rs.ObjectMaterialIndex(Box)
        rs.MaterialColor(Index,Color)





Main()
#*****************************************************************************
#End