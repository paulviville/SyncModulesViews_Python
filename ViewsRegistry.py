import bpy
from .ViewCore import ViewCore

class ViewsRegistry ( ViewCore ):
    def __init__( self, modulesRegistry ):
        ViewCore.__init__( self, modulesRegistry )
        print(self._collection)
        root = bpy.data.objects.new( "R egistryRoot", None )
        self._collection.objects.link(root)