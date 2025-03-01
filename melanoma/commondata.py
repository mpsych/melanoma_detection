import melanoma as mel
from enum import Enum

from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet import ResNet101, ResNet152
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications.xception import Xception
from tensorflow.keras.applications.efficientnet \
    import EfficientNetB0, EfficientNetB1, EfficientNetB2, EfficientNetB3, \
        EfficientNetB4, EfficientNetB5, EfficientNetB6, EfficientNetB7
# from tensorflow.keras.applications.efficientnet_v2 import EfficientNetV2B0, EfficientNetV2B1, EfficientNetV2B2, \
#         EfficientNetV2B3, EfficientNetV2S, EfficientNetV2M, EfficientNetV2L
from tensorflow.keras.applications.resnet_v2 \
    import ResNet50V2, ResNet101V2, ResNet152V2
# from tensorflow.keras.applications.resnet_v2 import InceptionResNetV2
from tensorflow.keras.applications.mobilenet import MobileNet
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.applications.densenet import DenseNet121, DenseNet169, \
    DenseNet201
from tensorflow.keras.applications.nasnet import NASNetMobile, NASNetLarge
# from tensorflow.keras.applications.convnext import ConvNeXtTiny, ConvNeXtSmall, \
#     ConvNeXtBase, ConvNeXtLarge, ConvNeXtXLarge

class DatasetType(Enum):
	HAM10000 = 1
	ISIC2016= 2
	ISIC2017=3
	ISIC2018 = 4
	ISIC2019 = 5
	ISIC2020 = 6
	PH2 = 7
	_7_point_criteria = 8
	PAD_UFES_20 = 9
	MEDNODE = 10
	KaggleMB = 11

class NetworkType(Enum):
	ResNet50 = 1
	ResNet101 = 2
	ResNet152 = 3
	Xception = 4
	InceptionV3 = 5
	VGG16 = 6
	VGG19 = 7
	EfficientNetB0 = 8
	EfficientNetB1 = 9
	EfficientNetB2 = 10
	EfficientNetB3 = 11
	EfficientNetB4 = 12
	EfficientNetB5 = 13
	EfficientNetB6 = 14
	EfficientNetB7 = 15
	# EfficientNetV2B0 = 16
	# EfficientNetV2B1 = 17
	# EfficientNetV2B2 = 18
	# EfficientNetV2B3 = 19
	# EfficientNetV2S = 20
	# EfficientNetV2M = 21
	# EfficientNetV2L = 22
	ResNet50V2 = 23
	ResNet101V2 = 24
	ResNet152V2 = 25
	# InceptionResNetV2 = 26
	MobileNet = 27
	MobileNetV2 = 28
	DenseNet121 = 29
	DenseNet169 = 30
	DenseNet201 = 31
	NASNetMobile = 32
	NASNetLarge = 33
	MeshNet = 34
	# ConvNeXtTiny = 34
	# ConvNeXtSmall = 35
	# ConvNeXtBase = 36
	# ConvNeXtLarge = 37
	# ConvNeXtXLarge = 38
    

class CommonData:
    def __init__(self):
      self.classifierDict = {
            mel.NetworkType.ResNet50.name: ResNet50,
            mel.NetworkType.ResNet101.name: ResNet101,
            mel.NetworkType.ResNet152.name: ResNet152,
            mel.NetworkType.Xception.name: Xception,
            mel.NetworkType.InceptionV3.name: InceptionV3,
            mel.NetworkType.VGG16.name: VGG16,
            mel.NetworkType.VGG19.name: VGG19,
            mel.NetworkType.EfficientNetB0.name: EfficientNetB0,
            mel.NetworkType.EfficientNetB1.name: EfficientNetB1,
            mel.NetworkType.EfficientNetB2.name: EfficientNetB2,
            mel.NetworkType.EfficientNetB3.name: EfficientNetB3,
            mel.NetworkType.EfficientNetB4.name: EfficientNetB4,
            mel.NetworkType.EfficientNetB5.name: EfficientNetB5,
            mel.NetworkType.EfficientNetB6.name: EfficientNetB6,
            mel.NetworkType.EfficientNetB7.name: EfficientNetB7,

            mel.NetworkType.ResNet50V2.name: ResNet50V2,
            mel.NetworkType.ResNet101V2.name: ResNet101V2,
            mel.NetworkType.ResNet152V2.name: ResNet152V2,

            mel.NetworkType.MobileNet.name: MobileNet,
            mel.NetworkType.MobileNetV2.name: MobileNetV2,

            mel.NetworkType.DenseNet121.name: DenseNet121,
            mel.NetworkType.DenseNet169.name: DenseNet169,
            mel.NetworkType.DenseNet201.name: DenseNet201,

            mel.NetworkType.NASNetMobile.name: NASNetMobile,
            mel.NetworkType.NASNetLarge.name: NASNetLarge,
      }
      self.DBpreprocessorDict = {
        mel.NetworkType.ResNet50.name: mel.NetworkType.ResNet50.name,
        mel.NetworkType.ResNet101.name: mel.NetworkType.ResNet50.name,
        mel.NetworkType.ResNet152.name: mel.NetworkType.ResNet50.name,
        mel.NetworkType.Xception.name: mel.NetworkType.Xception.name,
        mel.NetworkType.InceptionV3.name: mel.NetworkType.InceptionV3.name,
        mel.NetworkType.VGG16.name: mel.NetworkType.VGG16.name,
        mel.NetworkType.VGG19.name: mel.NetworkType.VGG19.name,
        mel.NetworkType.EfficientNetB0.name: mel.NetworkType.EfficientNetB0.name,
        mel.NetworkType.EfficientNetB1.name: mel.NetworkType.EfficientNetB0.name,
        mel.NetworkType.EfficientNetB2.name: mel.NetworkType.EfficientNetB0.name,
        mel.NetworkType.EfficientNetB3.name: mel.NetworkType.EfficientNetB0.name,
        mel.NetworkType.EfficientNetB4.name: mel.NetworkType.EfficientNetB0.name,
        mel.NetworkType.EfficientNetB5.name: mel.NetworkType.EfficientNetB0.name,
        mel.NetworkType.EfficientNetB6.name: mel.NetworkType.EfficientNetB0.name,
        mel.NetworkType.EfficientNetB7.name: mel.NetworkType.EfficientNetB0.name,

        mel.NetworkType.ResNet50V2.name: mel.NetworkType.ResNet50V2.name,
        mel.NetworkType.ResNet101V2.name: mel.NetworkType.ResNet50V2.name,
        mel.NetworkType.ResNet152V2.name: mel.NetworkType.ResNet50V2.name,

        mel.NetworkType.MobileNet.name: mel.NetworkType.MobileNet.name,
        mel.NetworkType.MobileNetV2.name: mel.NetworkType.MobileNetV2.name,

        mel.NetworkType.DenseNet121.name: mel.NetworkType.DenseNet121.name,
        mel.NetworkType.DenseNet169.name: mel.NetworkType.DenseNet121.name,
        mel.NetworkType.DenseNet201.name: mel.NetworkType.DenseNet121.name,

        mel.NetworkType.NASNetMobile.name: mel.NetworkType.NASNetMobile.name,
        mel.NetworkType.NASNetLarge.name: mel.NetworkType.NASNetMobile.name,

        mel.NetworkType.MeshNet.name: mel.NetworkType.VGG16.name,
      }