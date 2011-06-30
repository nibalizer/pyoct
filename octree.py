
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
        self.Xcenter = (self.Xupperlimit + self.Xlowerlimit)/2.
        self.Ycenter = (self.Yupperlimit + self.Ylowerlimit)/2.
        self.Zcenter = (self.Zupperlimit + self.Xlowerlimit)/2.

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

    #array of children
    chidren = [posXposYposZ,posXposYnegZ,posXnegYposZ,posXposYnegZ,negXposYposZ,negXposYnegZ,negXnegYposZ,negXnegYnegZ]

    #position in space
    Xupperlimit = None
    Yupperlimit = None
    Zupperlimit = None
    
    Xlowerlimit = None
    Ylowerlimit = None
    Zlowerlimit = None
    def get_array_of_children(self):
        """
        helper function to return array of children
        because there is some weird issue where just setting an 
        array variable isn't cutting it
        """
        children = [self.posXposYposZ,self.posXposYnegZ,self.posXnegYposZ,self.posXposYnegZ,self.negXposYposZ,self.negXposYnegZ,self.negXnegYposZ,self.negXnegYnegZ ]        
        return children

    def print_types(self):
        """
        helper function to printout types of children
        I know, terribly unpythonic of me, rabble rabble
        """
        print type(self.posXposYposZ)
        print type(self.posXposYnegZ)
        print type(self.posXnegYposZ)
        print type(self.posXposYnegZ)
        print type(self.negXposYposZ)
        print type(self.negXposYnegZ)
        print type(self.negXnegYposZ)
        print type(self.negXnegYnegZ)
    def print_info(self):
        """
        helper function to dump node paramaters
        """

        print "parent:\t {0}".format(self.parent)
        print "value:\t {0}".format(self.value)
        
        #children
        print "posXposYposZ: \t {0}".format(self.posXposYposZ)
        print "posXposYnegz: \t {0}".format(self.posXposYnegZ)
        print "posXnegYposZ: \t {0}".format(self.posXnegYposZ)
        print "posXposYnegZ: \t {0}".format(self.posXposYnegZ)
        print "negXposYposZ: \t {0}".format(self.negXposYposZ)
        print "negXposYnegZ: \t {0}".format(self.negXposYnegZ)
        print "negXnegYposZ: \t {0}".format(self.negXnegYposZ)
        print "negXnegYnegZ: \t {0}".format(self.negXnegYnegZ) 

        #position in space
        print "Xupperlimit: \t {0}".format(self.Xupperlimit)
        print "Yupperlimit: \t {0}".format(self.Yupperlimit)
        print "Zupperlimit: \t {0}".format(self.Zupperlimit)
        
        print "Xlowerlimit: \t {0}".format(self.Xlowerlimit)
        print "Ylowerlimit: \t {0}".format(self.Ylowerlimit)
        print "Zlowerlimit: \t {0}".format(self.Zlowerlimit)

        print "Xcenter: \t {0}".format(self.Xcenter)
        print "Ycenter: \t {0}".format(self.Ycenter)
        print "Zcenter: \t {0}".format(self.Zcenter)

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
        Create recursively create subnodes until maxiter is reached
        then deposit payload in that node
        """

        self.root.add(payload, coord, self.maxiter)
        

def find_closest_three(x, y, z, tree):
    """
    function to find the closest three data points to
    a given data point
    """
    #brief sanity checking
    if (x >= tree.Xmax or x <= tree.Xmin):
        print "Fail, out of range"
    if (y >= tree.Ymax or y <= tree.Ymin):
        print "Fail, out of range"
    if (z >= tree.Zmax or z <= tree.Zmin):
        print "Fail, out of range"

    #find the node by coords
    for level in range(tree.maxiter):
        pass



    


if __name__ == "__main__":
    print "Creating octree"
    tree = octree(100,100,100, -100, -100, -100)
    print "inserting node"
    tree.add_item("derp", (10.34251,10.1234,10.9876))
    print "Great success"
    
    #get some data
    tree.root.print_info()
    for child in tree.root.chidren:
        print type(child)
    tree.root.print_types()
    for child in tree.root.get_array_of_children():
        try:
            grandchild = child.get_array_of_children()
        except AttributeError:
            print type(child)



