#----------------------------------------------------------
# File meshes.py modified
#----------------------------------------------------------
import bpy
import random
import copy

def createMesh(name, origin, verts, edges, faces):
    # Create mesh and object
    me = bpy.data.meshes.new(name+'Mesh')
    ob = bpy.data.objects.new(name, me)
    ob.location = origin
    ob.show_name = True
    # Link object to scene
    bpy.context.scene.objects.link(ob)

    # Create mesh from given verts, edges, faces. Either edges or
    # faces should be [], or you ask for problems
    me.from_pydata(verts, edges, faces)

    # Update mesh with new data
    me.update(calc_edges=True)
    return ob

def vertsGen(num):
	verts =[]
	for i in range(num):
		if(num%2==0):
			verts.append((random.random(),random.random(),random.random()))
		else:
			verts.append((random.random()/2+.5,random.random()/2+.5,random.random()/2+.5))
	return verts
def facesGen(n,verts):

	points = list(range(n))
	points = points*3
	faces, face =[],[]
	for j in range(3):
			newPt = random.choice(points)
			while(newPt in face):
				newPt = random.choice(points)
			face.append(newPt)
			points.remove(newPt)
	faces.append(face)
	for i in range(n-1):
		face = copy.deepcopy(faces[-1])
		random.shuffle(face)
		face.pop()
		newPt = random.choice(points)
		while(newPt in face):
			newPt = random.choice(points)
		face.append(newPt)
		points.remove(newPt)
		faces.append(face)
	return faces

def run(origin):
    numOfFaces = random.randint(10,30)
    verts1 = vertsGen(3*numOfFaces)
    faces1 = facesGen(numOfFaces,verts1)
    ob1 = createMesh('Solid', origin, verts1, [], faces1)
    return

if __name__ == "__main__":
    run((0,0,0))
    # x = 1
    # print(facesGen(5,[(x,x,-1), (x,-x,-1), (-x,-x,-1), (-x,x,-1), (0,0,1)]))