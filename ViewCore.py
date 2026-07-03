import bpy

class ViewCore:
    _type = "ViewCore"

    def __init__( self, module=None ):
        print( "ViewCore - __init__" )
        self._module = module
        self._collection = bpy.data.collections.new( name=f"{module.UUID}" )

    @property
    def module ( self ):
        return self._module

    @property
    def type ( self ):
        return self._type
