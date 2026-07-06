import bpy
from .ViewCore import ViewCore
from .ViewTypes import ViewTypes

class ViewsRegistry ( ViewCore ):
	_type = "ViewsRegistry"

	def __init__ ( self, modulesRegistry ):
		ViewCore.__init__( self, modulesRegistry )
		bpy.context.scene.collection.children.link( self._collection )

		self._views = { }
		# self.setCallbacks( )

		root = bpy.data.objects.new( "RegistryRoot", None )
		self._collection.objects.link( root )

	def setCallbacks ( self ):
		print("registry setCallbacks")
		self._module.setOnChange( self.module.commands.addModule, self._addModuleView)
		self._module.setOnChange( self.module.commands.removeModule, self._removeModuleView)

	def getView ( self, moduleUUID ):
		return self._views.get( moduleUUID )

	def _addModuleView ( self, module ):
		print( "_addModuleView" )
		print( module.type )

		type = module.type
		UUID = module.UUID

		view = None
		if type in ViewTypes:
			view = ViewTypes[ type ]( module )
		else:
			view = ViewCore( module )

		self._views[ UUID ] = view
		self._collection.children.link( view._collection )

	def _removeModuleView ( self, module ):
		print( "_removeModuleView" )

		UUID = module.UUID

		view = self._views[ UUID ]
		view.delete( )
		del( self._views[ UUID ] )