# Automating ngskin weights in each loop
The script will help you in flooding ngSkin weights in each loops with each joint

## How to Use:

### Set Maya continue edges:
Go to : Select > Contiguous Edges > Switch On (Limit number of edges)



The code use Maya contiguous edges, so make sure parameter are set correctly. 

Maya doesn't allow to expose contiguous edges,  this is the current way only.


### Select the NG layer:
Select the ng layer which you want to flood the weights:


Select Edge Ring:
Select all the edge ring which are nearest to joints. Check below image for reference.

Run:   edges = cmds.ls(sl=True)


### Select Joints or Mention Joints name:

Don't worry about joints and edges list order, it calculates joint to edge distance.

Few Tips:
If the Joints are not overlapping each other, we can flood weights all together.

Example: Orbital area has no overlapping joint.



If the Joints are overlapping each others.

Example: Upper and lower eyelid

Run the code for upper and lower one by one.
