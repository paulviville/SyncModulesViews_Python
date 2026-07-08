import bpy
from .ViewCore import ViewCore

class LineView ( ViewCore ):
	_type = "LineView"

	def __init__ ( self, lineModule ):
		print( "LineView - __init__" )
		ViewCore.__init__( self, lineModule )

		curveData = bpy.data.curves.new( "Line", type="CURVE" )
		curveData.dimensions = "3D"

		self._lineData = curveData.splines.new( "POLY" )
		self._lineData.points.add( 1 )

		self._line = bpy.data.objects.new( "Line", curveData )
		print(self._line)
		self._collection.objects.link( self._line )

		self._updateLine( lineModule.line )

	def setCallbacks( self ):
		self._module.setOnChange( self.module.commands.updateLine, self._updateLine )
	
	def _updateLine ( self, line ):
		origin = line.get( "origin" )
		end = line.get( "end" )

		if origin is not None:
			self._lineData.points[ 0 ].co = ( *origin, 1 )
		if end is not None:
			self._lineData.points[ 1 ].co = ( *end, 1 )