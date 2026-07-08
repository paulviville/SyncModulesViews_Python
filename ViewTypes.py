from .ViewCore import ViewCore
# from ..ScalarModule import ScalarModule
# from ..Vector3Module import Vector3Module
from .TransformView import TransformView
from .PrimitiveView import PrimitiveView
from .CameraView import CameraView
from .LineView import LineView

ViewTypes = {
	"ModuleCore": ViewCore,
	"TransformModule": TransformView,
	# "Vector3Module": Vector3Module,
	# "TransformModule": TransformModule,
	"PrimitiveModule": PrimitiveView,
	"CameraModule": CameraView,
	"LineModule": LineView
}