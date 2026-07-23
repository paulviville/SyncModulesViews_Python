import bpy
import bmesh
from .ViewCore import ViewCore
from .TransformView import TransformView

class PrimitiveView ( TransformView ):
	_type = "PrimitiveView"

	def __init__ ( self, primitiveModule ):
		print( "PrimitiveView - __init__" )
		super( ).__init__( primitiveModule )

		self._root = bpy.data.objects.new( "Transform Root", None )
		self._root.rotation_mode = "QUATERNION"
		self._collection.objects.link( self._root )


		self._mesh = bpy.data.meshes.new( "Primitive" )


		self._primitive = bpy.data.objects.new( "Primitive", self._mesh )
		self._collection.objects.link( self._primitive )
		self._primitive.parent = self._root

		self._updatePrimitive( primitiveModule.primitive )
	
	def setCallbacks( self ):
		print( "PrimitiveView - setCallbacks" )
		super( ).setCallbacks(  )
		self._module.setOnChange( self.module.commands.updatePrimitive, self._updatePrimitive )

	def _updatePrimitive ( self, primitive ):
		types = self._module.primitiveTypes
		print(primitive)
		bm = bmesh.new( )
		match primitive:
			case types.Box:
				print( "box primitive" )
				bmesh.ops.create_cube( bm, size=1.0 )
			case types.Sphere | _:
				print( "sphere primitive" )
				bmesh.ops.create_icosphere( bm, subdivisions=3, radius=1.0 )
		bm.to_mesh( self._mesh )
		bm.free( )

		print( self._module.primitiveTypes )
