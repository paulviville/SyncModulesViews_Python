import bpy

class ViewCore:
	_type = "ViewCore"

	def __init__( self, module=None ):
		print( "ViewCore - __init__" )
		self._module = module
		self._collection = bpy.data.collections.new( name=f"{ module.type }-{ module.UUID }" )
		self.setCallbacks( )
		print(self._collection)

	@property
	def module ( self ):
		return self._module

	@property
	def type ( self ):
		return self._type
	
	def setCallbacks ( self ):
		print( "viewcore placeholder")
		
	def delete ( self ):
		for obj in list( self._collection.objects ):
			bpy.data.objects.remove( obj, do_unlink=True )
		
		bpy.data.collections.remove( self._collection )