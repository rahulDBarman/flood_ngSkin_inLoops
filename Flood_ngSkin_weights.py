
## https://github.com/rahulDBarman/flood_ngSkin_inLoops
## Author: Rahul deb Barman
## Year: 2026

from maya import cmds
import maya.api.OpenMaya as om
from ngSkinTools2.api import (
    Layers,
    PaintModeSettings,
    flood_weights,
    PaintMode,
    list_influences,
    add_influences
)
"""
jnts = cmds.ls(sl=True)

edges = cmds.ls(sl=True)

flood_ngSkin_inLoops(jnts, edges)

"""

def rd_flood_ngSkin_inLoops(jnts, edges, **kwargs):

    jnts = cmds.ls(jnts, l=True)
    
    edges = cmds.ls(edges, fl= True)
    mesh = edges[0].split(".e[")[0]

    layers = Layers(mesh)
    layer = kwargs.get("layer", layers.current_layer())

    # build settings for the flood
    settings = PaintModeSettings()
    settings.mode = PaintMode.replace
    settings.intensity = 1.0

    inflns = list_influences(mesh)

    add_influences(jnts, mesh)

    nearest_edges = rd_sort_joints_by_nearest_edge(edges, jnts)
    for i, jnt in enumerate(jnts):
        for infJnt in inflns:
            if jnt == infJnt.path:
                cmds.select(nearest_edges[i])
                cmds.SelectContiguousEdges()
                flood_weights(target=layer, influence=infJnt.logicalIndex, settings=settings)

    cmds.select(mesh)
                


def rd_get_edge_midpoint(mesh_name, edge_id):
    sel = om.MSelectionList()
    sel.add(mesh_name)
    dag = sel.getDagPath(0)
    
    mesh_fn = om.MFnMesh(dag)
    edge_verts = mesh_fn.getEdgeVertices(edge_id)
    
    startPoint = mesh_fn.getPoint(edge_verts[0], om.MSpace.kWorld)
    endPoint = mesh_fn.getPoint(edge_verts[1], om.MSpace.kWorld)

    mid = om.MPoint((om.Vector(startPoint)+om.vector(endPoint))/2)

    return mid



def rd_sort_joints_by_nearest_edge(edges, joints):
    parsed_edges = []
    for edge_comp in edges:
        parts = edge_comp.split(".e[")
        if len(parts) != 2:
            cmds.warning("Skipping invalid edge component: {}".format(edge_comp))
            continue
        mesh = parts[0]
        edge_id = int(parts[1].rstrip("]"))
        midpoint = rd_get_edge_midpoint(mesh, edge_id)
        parsed_edges.append((edge_comp, midpoint))


    results = []
    for joint in joints:
        if not cmds.ls(joint, type = "joint"):
            cmds.warning("Joint not found, skipping: {}".format(joint))
            continue

        j_pos = om.MPoint(cmds.xform(joint, q=True, ws=True, t=True))

        # Find nearest edge midpoint
        nearest_edge = None
        min_dist = float("inf")
        for edge_comp, midpoint in parsed_edges:
            dist = j_pos.distanceTo(midpoint)
            if dist < min_dist:
                min_dist = dist
                nearest_edge = edge_comp

        results.append(nearest_edge)

    return results