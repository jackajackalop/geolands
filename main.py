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
        # self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
 
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
 
        # # Create the four lerp intervals needed for the panda to
        # # walk back and forth.
        # pandaPosInterval1 = self.pandaActor.posInterval(13,
        #                                                 Point3(0, -10, 0),
        #                                                 startPos=Point3(0, 10, 0))
        # pandaPosInterval2 = self.pandaActor.posInterval(13,
        #                                                 Point3(0, 10, 0),
        #                                                 startPos=Point3(0, -10, 0))
        # pandaHprInterval1 = self.pandaActor.hprInterval(3,
        #                                                 Point3(180, 0, 0),
        #                                                 startHpr=Point3(0, 0, 0))
        # pandaHprInterval2 = self.pandaActor.hprInterval(3,
        #                                                 Point3(0, 0, 0),
        #                                                 startHpr=Point3(180, 0, 0))
 
        # # Create and play the sequence that coordinates the intervals.
        # self.pandaPace = Sequence(pandaPosInterval1,
        #                           pandaHprInterval1,
        #                           pandaPosInterval2,
        #                           pandaHprInterval2,
        #                           name="pandaPace")
        # self.pandaPace.loop()
        ambientLight = AmbientLight('ambientLight')
        ambientLight.setColor(Vec4(0.6, 0.6, 0.6, 1))
        ambientLightNP = render.attachNewNode(ambientLight)
        self.render.setLight(ambientLightNP)

        plight = PointLight('plight')
        plight.setColor(VBase4(0.6, 0.6, 0.6, 1))
        plnp = render.attachNewNode(plight)
        plnp.setPos(10, 20, 0)
        self.render.setLight(plnp)
 
    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont
 
app = MyApp()
app.run()