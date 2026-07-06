from .ViewCore import ViewCore
# from ..ScalarModule import ScalarModule
# from ..Vector3Module import Vector3Module
from .TransformView import TransformView
# from ..PrimitiveModule import PrimitiveModule
# from ..CameraModule import CameraModule
# from ..LineModule import LineModule

ViewTypes = {
	"ModuleCore": ViewCore,
	"TransformModule": TransformView,
	# "ScalarModule": ScalarModule,
	# "Vector3Module": Vector3Module,
	# "TransformModule": TransformModule,
	# "PrimitiveModule": PrimitiveModule,
	# "CameraModule": CameraModule,
	# "LineModule": LineModule
}