import bpy
import bmesh
from .ViewCore import ViewCore

class PointsView ( ViewCore ):
	_type = "PointsView"

	def __init__ ( self, pointsModule ):
		print( "PointsView - __init__" )
		super( ).__init__( pointsModule )

		# self._mesh = bpy.ops.mesh.primitive_uv_sphere
		self._pointsObj = { }
		self._mesh = bpy.data.meshes.new( "Point" )
		
		bm = bmesh.new( )
		bmesh.ops.create_icosphere( bm, subdivisions=3, radius=0.1 )
		bm.to_mesh( self._mesh )
		bm.free( )

	def setCallbacks(self):
		print( "PointsView - setCallbacks" )
		self._module.setOnChange( self.module.commands.addPoints, self._updatePoints )
		self._module.setOnChange( self.module.commands.removePoints, self._updatePoints )
		# return super().setCallbacks()

	def _updatePoints ( self, points ):
		for point in points:
			UUID = point[ "UUID" ]
			pointObj = self._pointsObj.get( UUID )
			
			if pointObj is None:
				pointObj = bpy.data.objects.new( f"Point-{ UUID }", self._mesh )
				self._pointsObj[ UUID ] = pointObj
				self._collection.objects.link( pointObj )

			pointObj.location = point[ "position" ]

			 
		print( "PointsView - _updatePoints" )

	def _clear ( self, points ):
		print( "PointsView - _updatePoints" )
