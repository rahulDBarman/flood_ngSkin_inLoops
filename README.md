# Automating ngskin weights in each loop
The script will help you in flooding ngSkin weights in each loops with each joint

<img width="856" height="553" alt="peek_3" src="https://github.com/user-attachments/assets/b87afae2-3920-40b5-a419-c0ba2241353c" />


## How to Use:

### Set Maya continue edges:
Go to : Select > Contiguous Edges > Switch On (Limit number of edges)

<img width="462" height="384" alt="Screenshot 2026-06-21 085626" src="https://github.com/user-attachments/assets/12a1b3da-75e2-4f71-b420-c121e16b4503" />



The code use Maya contiguous edges, so make sure parameter are set correctly. 

Maya doesn't allow to expose contiguous edges,  this is the current way only.


### Select the NG layer:
Select the ng layer which you want to flood the weights:

<img width="436" height="576" alt="Screenshot 2026-06-21 085555" src="https://github.com/user-attachments/assets/5c727a31-adeb-4f87-ad4b-c090d001800c" />


### Select Edge Ring:
Select all the edge ring which are nearest to joints. Check below image for reference.

Run:
```python
  edges = cmds.ls(sl=True)
```


### Select Joints or Mention Joints name:
```python
  ## select joints and put in jnts list
  edges = cmds.ls(sl=True)
  jnts = cmds.ls(sl=True)
  rd_flood_ngSkin_inLoops(jnts, edges)
   
  or
   
  ## directly list joints in arguments
  edges = cmds.ls(sl=True)
  rd_flood_ngSkin_inLoops(("L_eyelid_orb*Crv??Translate_env","L_eyelid_*Orbital_env"), edges)
```

Don't worry about joints and edges list order, it calculates joint to edge distance.


## Demo Video
<a href="https:/youtu.be/wO3k0r_dRqc">
  <img width="1330" height="733" alt="Screenshot 2026-06-21 084326" src="https://github.com/user-attachments/assets/5730b4ca-40be-40b9-a66f-ed36cc978f07" />
</a>


### Few Tips:
If the Joints are not overlapping each other, we can flood weights all together.
Example: Orbital area has no overlapping joint.

If the Joints are overlapping each others.
Example: Upper and lower lip
Run the code for upper and lower one by one.

