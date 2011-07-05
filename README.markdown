# PyOct

octree in python

## Overview

This set of classes and functions allows one to search and insert 3D space quickly

* Node() class creates a node object
* octree() creates a new octree root with subnodes

## Invocation

import octree

p = Octree(Arguments)

p.add(thing)

p.find_within_range(area, space)

### Particulars

#### Tree creation

The arguments to create a tree are:

tree = Octree(Xmax, Ymax, Zmax, Xmin, Ymin, Zmin, root_coords=(0,0,0), maxiter=7):

* Xmax =  the maximum X ceiling of your dataset
* Ymax =  the maximum Y ceiling of your dataset
* Zmax =  the maximum Z ceiling of your dataset
* Xmin =  the minimum X basement of your dataset
* Ymin =  the minimum Y basement of your dataset
* Zmin =  the minimum Z basement of your dataset
* root_coords=(0,0,0) = where you want the center of the root node to be, best not to touch this actually
** Its a (float,float,float) tupple for (Xpos,Ypos,Zpos)
* maxiter=7 = the maximum depth it will make nodes to, so maxiter=7 means 8^7 nodes are possible

#### Add item to tree
The arguments to add a 'payload' to the tree are:

tree.add_item(payload, coord)

* payload = whatever you want the payload to be, its python it will just roll with it
* coord   = the (float,float,float) tupple of where you want the payload to 'be'


#### Search in tree for things

tree.find_within_range(center, size, shape)

* center = Where you want to center the search on
** Not optimized to search closer to this center fastest(YET) TODO
** (float, float, float) tupple
** for (xposition, yposition, zposition)
* size = distance away from the center to draw search space
** in spherical shapes that's radius
** in cube shapes that's distance from center of face to center
* shape = Shape of searching slice
** only "cube" implemented now
** hopefully "sphere" soon TODO
** also would like to make it possible to give 'doughnut' shapes that mean "all of this space, minus this space"

## Examples

<pre>
print "Creating octree"
tree = Octree(100,100,100, -100, -100, -100)
print "inserting node"
tree.add_item("derp", (10.34251,10.1234,10.9876))
print "Great success"
results = tree.find_within_range((0,0,0), 50, "cube")
for result in results:
    print result
</pre>

## License

This software is released under the GPLv3 or any latter license. 

## Further Documentation

See the documentation internal to the source code for more information.

## Helping 

If you have a patch, or a pull request on github, it has a VERY high chance
of being accepted. Or just email me.

## Use

If you use this code, please let me know! It would be great to know if I
helped someone or saved them some time.


Source code
-----------

The source code for this module is available online at
    http://github.com/nibalizer/pyoct

You can checkout the source code by installing the `git` distributed version
control system and running:

    git clone git://github.com/nibalizer/pyoct.git

Authors
-------

 *   Spencer Krum <krum.spencer@gmail.com>
