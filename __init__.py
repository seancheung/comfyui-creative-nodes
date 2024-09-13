from .nodes.flow import *
from .nodes.resolution import *
from .server import *

NODE_CLASS_MAPPINGS = {
    "CreativeStopFlow": StopFlow,
    "CreativeSkipFromFlow": SkipFromFlow,
    "CreativeSkipToFlow": SkipToFlow,
    "ResolutionSelector": ResolutionSelector,
    "ResolutionXLSelector": ResolutionXLSelector,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "CreativeStopFlow": "Stop Flow",
    "CreativeSkipFromFlow": "Skip From Flow",
    "CreativeSkipToFlow": "Skip To Flow",
    "ResolutionSelector": "Resolution Selector",
    "ResolutionXLSelector": "ResolutionXL Selector",
}
WEB_DIRECTORY = "./js"
