import bpy
from .ViewCore import ViewCore

class TransformView ( ViewCore ):
	_type = "TransformView"

	def __init__ ( self, transformModule ):
		print( "TransformView - __init__" )
		ViewCore.__init__( self, transformModule )

		self._root = bpy.data.objects.new( "Transform Root", None )
		self._root.rotation_mode = "QUATERNION"

		self._collection.objects.link( self._root )
	
	def setCallbacks(self):
		self._module.setOnChange( self.module.commands.updateTransform, self._updateTransform )

	def _updateTransform ( self, transform ):
		print( "self._updateTransform")
		translation = transform.get( "translation" )
		rotation = transform.get( "rotation" )
		scale = transform.get( "scale" )

		if translation is not None:
			self._root.location = ( translation[ 0 ], translation[ 1 ], translation[ 2 ] )
		if rotation is not None:
			self._root.rotation_quaternion = ( rotation[ 3 ], rotation[ 0 ], rotation[ 1 ], rotation[ 2 ] )
		if scale is not None:
			self._root.scale = ( scale[ 0 ], scale[ 1 ], scale[ 2 ] )

	# @property
	# def root ( self ):
	# 	return self._root