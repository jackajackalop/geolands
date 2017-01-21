from math import pi, sin, cos
 
from direct.showbase.ShowBase import ShowBase
# import direct.directbase.DirectStart
from panda3d.core import *
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
 
class MyApp(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)
		self.x,self.y,self.angleDegrees,self.angleRadians =0,0,90,pi/2
		# Disable the camera trackball controls.
		# self.disableMouse()
 
		# Load the environment model.
		self.scene = self.loader.loadModel("land/1.egg")
		# Reparent the model to render.
		self.scene.reparentTo(self.render)
		# Apply scale and position transforms on the model.
		self.scene.setScale(1, 1, 1)
		self.scene.setPos(-8, 42, 0)
		self.scene.setColor(.95, .85, .9, 1.0)

		tex = loader.loadTexture('land/5.jpg')
		self.scene.setTexGen(TextureStage.getDefault(), TexGenAttrib.MWorldPosition)
		self.scene.setTexture(tex)


		# # Use a 512x512 resolution shadow map
		# plight.setShadowCaster(True, 512, 512)
		# # Enable the shader generator for the receiving nodes
		# self.render.setShaderAuto()
 
		# Add the spinCameraTask procedure to the task manager.
		self.taskMgr.add(self.moveCameraTask, "moveCameraTask")
 
		# Load and transform the panda actor.
		self.basicActor = Actor("person.egg",
								{"walk": "person-Anim1.egg"})
		# Reparent the model to render.
		self.basicActor.reparentTo(self.render)
		# Apply scale and position transforms on the model.
		self.basicActor.setScale(1, 1, 1)
		self.basicActor.setPos(-8, 42, 0)
		self.basicActor.setColorScale(.95, .92, .99, 1.0)

		tex = loader.loadTexture('land/16.jpg')
		self.basicActor.setTexGen(TextureStage.getDefault(), TexGenAttrib.MWorldPosition)
		self.basicActor.setTexture(tex)

		# Loop its animation.
		self.basicActor.loop("walk")
 
		
		ambientLight = AmbientLight('ambientLight')
		ambientLight.setColor(Vec4(0.6, 0.6, 0.6, 1))
		ambientLightNP = render.attachNewNode(ambientLight)
		self.render.setLight(ambientLightNP)

		plight = PointLight('plight')
		plight.setColor(VBase4(0.6, 0.6, 0.6, 1))
		plnp = render.attachNewNode(plight)
		plnp.setPos(10, 20, 0)
		self.render.setLight(plnp)

		self.keyMap = {"w" : False, "s" : False, "a" : False, "d" : False,}
		self.accept("w", self.setKey, ["w", True])
		self.accept("s", self.setKey, ["s", True])   
		self.accept("a", self.setKey, ["a", True])   
		self.accept("d", self.setKey, ["d", True])

		self.accept("w-up", self.setKey, ["w", False])
		self.accept("s-up", self.setKey, ["s", False])
		self.accept("a-up", self.setKey, ["a", False])
		self.accept("d-up", self.setKey, ["d", False])

	def setKey(self, key, value):
	  self.keyMap[key] = value
   
	# Define a procedure to move the camera.
	def moveCameraTask(self, task):
		if(self.keyMap["w"] == True):
			self.y+=1
		elif(self.keyMap["s"] == True):
			self.y-=1
		elif(self.keyMap["a"] == True):
			self.angleDegrees+=1
			self.angleRadians+=2*pi/360
		elif(self.keyMap["d"] == True):
			self.angleDegrees-=1
			self.angleRadians-=2*pi/360
		self.camera.setPos(self.y*cos(self.angleRadians), self.y*sin(self.angleRadians),3)
		self.camera.setHpr(self.angleDegrees-90, 0, 0)
		return task.cont

app = MyApp()
app.run()