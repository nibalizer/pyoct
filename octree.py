
# -*- coding: utf-8 -*-
#python octree implementation
# Code © Spencer Krum June 2011
# Released underl GPLv3 See LICENSE file in this repository

class node():
    """
    Class to be a node in my octree
    """

    def __init__(self,parent, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit):
        self.parent = parent
        self.Xupperlimit = Xupperlimit
        self.Yupperlimit = Yupperlimit
        self.Zupperlimit = Zupperlimit
        self.Xlowerlimit = Xlowerlimit
        self.Ylowerlimit = Ylowerlimit
        self.Zlowerlimit = Zlowerlimit
        self.Xcenter = self.Xlowerlimit - self.Xupperlimit
        self.Ycenter = self.Ylowerlimit - self.Yupperlimit
        self.Zcenter = self.Zlowerlimit - self.Xupperlimit

    parent = None
    value = None
    
    #children
    posXposYposZ = None
    posXposYnegZ = None
    posXnegYposZ = None
    posXposYnegZ = None
    negXposYposZ = None
    negXposYnegZ = None
    negXnegYposZ = None
    negXnegYnegZ = None

    #position in space
    Xupperlimit = None
    Yupperlimit = None
    Zupperlimit = None
    
    Xlowerlimit = None
    Ylowerlimit = None
    Zlowerlimit = None

    def add(self, payload, coord, level):
        
        """
        Create a subnode
        """

        if level == 0:
            self.value = payload
            self.Xcenter = coord[0]
            self.Ycenter = coord[1]
            self.Zcenter = coord[2]

        else:
            level -= 1
            #Determine quadrant
            if coord[0] <= self.Xcenter:
                #negX
                if coord[1] <= self.Ycenter:
                    #negY
                    if coord[2] <= self.Zcenter:
                        #negZ
                        Xupperlimit = self.Xcenter
                        Yupperlimit = self.Ycenter
                        Zupperlimit = self.Zcenter
                        Xlowerlimit = self.Xlowerlimit
                        Ylowerlimit = self.Ylowerlimit
                        Zlowerlimit = self.Zlowerlimit
                        self.negXnegYnegZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.negXnegYnegZ.add(payload, coord, level)
                    else:
                        #posZ
                        Xupperlimit = self.Xcenter
                        Yupperlimit = self.Ycenter
                        Zupperlimit = self.Zupperlimit
                        Xlowerlimit = self.Xlowerlimit
                        Ylowerlimit = self.Ylowerlimit
                        Zlowerlimit = self.Zcenter
                        self.negXnegYposZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.negXnegYposZ.add(payload, coord, level)
                else:
                    #posY
                    if coord[2] <= self.Zcenter:
                        #negZ
                        Xupperlimit = self.Xcenter
                        Yupperlimit = self.Yupperlimit
                        Zupperlimit = self.Zcenter
                        Xlowerlimit = self.Xlowerlimit
                        Ylowerlimit = self.Ycenter
                        Zlowerlimit = self.Zlowerlimit
                        self.negXposYnegZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.negXposYnegZ.add(payload, coord, level)

                    else:
                        #posZ
                        Xupperlimit = self.Xcenter
                        Yupperlimit = self.Yupperlimit
                        Zupperlimit = self.Zupperlimit
                        Xlowerlimit = self.Xlowerlimit
                        Ylowerlimit = self.Ycenter
                        Zlowerlimit = self.Zcenter
                        self.negXposYposZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.negXposYposZ.add(payload, coord, level)


            else:
                #posX
                if coord[1] <= self.Ycenter:
                    #negY
                    if coord[2] <= self.Zcenter:
                        #negZ
                        Xupperlimit = self.Xupperlimit
                        Yupperlimit = self.Ycenter
                        Zupperlimit = self.Zcenter
                        Xlowerlimit = self.Xcenter
                        Ylowerlimit = self.Ylowerlimit
                        Zlowerlimit = self.Zlowerlimit
                        self.posXnegYnegZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.posXnegYnegZ.add(payload, coord, level)

                    else:
                        #posZ
                        Xupperlimit = self.Xupperlimit
                        Yupperlimit = self.Ycenter
                        Zupperlimit = self.Zupperlimit
                        Xlowerlimit = self.Xcenter
                        Ylowerlimit = self.Ylowerlimit
                        Zlowerlimit = self.Zcenter
                        self.posXnegYposZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.posXnegYposZ.add(payload, coord, level)

                else:
                    #posY
                    if coord[2] <= self.Zcenter:
                        #negZ
                        Xupperlimit = self.Xupperlimit
                        Yupperlimit = self.Yupperlimit
                        Zupperlimit = self.Zcenter
                        Xlowerlimit = self.Zcenter
                        Ylowerlimit = self.Ycenter
                        Zlowerlimit = self.Zlowerlimit
                        self.posXposYnegZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.posXposYnegZ.add(payload, coord, level)

                    else:
                        #posZ
                        Xupperlimit = self.Xupperlimit
                        Yupperlimit = self.Yupperlimit
                        Zupperlimit = self.Zupperlimit
                        Xlowerlimit = self.Xcenter
                        Ylowerlimit = self.Ycenter
                        Zlowerlimit = self.Zcenter
                        self.posXposYposZ = node(self.negXnegYnegZ, Xupperlimit, Yupperlimit, Zupperlimit, Xlowerlimit, Ylowerlimit, Zlowerlimit)
                        self.posXposYposZ.add(payload, coord, level)


        

            
            


class octree():
    """
    class to hold the whole tree
    """
    
    def __init__(self, Xmax, Ymax, Zmax, Xmin, Ymin, Zmin, root_coords=(0,0,0), maxiter=7):
        self.Xmax = Xmax
        self.Ymax = Ymax
        self.Zmax = Xmax
        self.Xmin = Xmin
        self.Ymin = Ymin
        self.Zmin = Zmin
        self.root_coords = root_coords
        self.maxiter = maxiter
        
        self.root = node('root', Xmax, Ymax, Zmax, Xmin, Ymin, Zmin)

    def add_item(self, payload, coord):
        """
        Create a subnode
        """

        self.root.add(payload, coord, self.maxiter)
        



if __name__ == "__main__":
    print "Creating octree"
    tree = octree(100,100,100, -100, -100, -100)
    print "inserting node"
    tree.add_item("derp", (10.34251,10.1234,10.9876))
    print "Great success"




