import bpy
import math

from .TransformView import TransformView

class CameraView ( TransformView ):
	_type = "CameraView"

	def __init__( self, cameraModule ):
		print( "CameraView - __init__" )
		TransformView.__init__( self, cameraModule )

		self._camera_data = bpy.data.cameras.new( "Camera" )
		self._camera = bpy.data.objects.new( "Camera", self._camera_data )

		self._collection.objects.link( self._camera )
		self._camera.parent = self._root

		self._updateCamera( cameraModule.camera )

	def setCallbacks( self ):
		TransformView.setCallbacks( self )
		self._module.setOnChange( self.module.commands.updateCamera, self._updateCamera )

	def _updateCamera ( self, camera ):
		print( "self._updateCamera")

		fov = camera.get( "fov" )
		near = camera.get( "near" )
		far = camera.get( "far" )

		if fov is not None:
			self._camera.data.angle = math.radians( fov )
		if near is not None:
			self._camera.data.clip_start = near
		if far is not None:
			self._camera.data.clip_end = far