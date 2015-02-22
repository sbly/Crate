import bpy

verts = bpy.data.objects["crate"].data.vertices
polys = bpy.data.objects["crate"].data.polygons

for vert in verts:
    print("(" + str(vert.co.x) + ", " + str(vert.co.y) + ", " + str(vert.co.z) + ")")

for poly in polys:
    print(poly)