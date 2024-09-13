from .ns import PACKAGE_NAMESPACE

SD_RESOLUTION = [
    (512, 512),
    (688, 512),
    (768, 512),
    (912, 512),
    (512, 688),
    (512, 768),
    (512, 912),
]

SDXL_RESOLUTION = [
    (704, 1408),
    (704, 1344),
    (768, 1344),
    (768, 1280),
    (832, 1216),
    (832, 1152),
    (896, 1152),
    (896, 1088),
    (960, 1088),
    (960, 1024),
    (1024, 1024),
    (1024, 960),
    (1088, 960),
    (1088, 896),
    (1152, 896),
    (1152, 832),
    (1216, 832),
    (1280, 768),
    (1344, 768),
    (1344, 704),
    (1408, 704),
    (1472, 704),
    (1536, 640),
    (1600, 640),
    (1664, 576),
    (1728, 576),
]

class ResolutionSelector:
    """
    A node to provide a drop-down list of resolutions and returns two int values (width and height).
    """
    resolution_strings = []

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        """
        Return a dictionary which contains config for all input fields.
        """
        resolution_strings = [ f"{width} x {height}" for width, height in SD_RESOLUTION ]
        
        return {
            "required": {
                "resolution": (resolution_strings,),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "select_resolution"
    CATEGORY = PACKAGE_NAMESPACE

    def select_resolution(self, resolution):
        """
        Returns the width and height based on the selected resolution and adjustment.

        Args:
            resolution (str): Selected resolution in the format "width x height".

        Returns:
            Tuple[int, int]: Adjusted width and height.
        """
        try:
            width, height = map(int, resolution.split(' x '))
        except ValueError:
            raise ValueError("Invalid resolution format.")
        return width, height


class ResolutionXLSelector(ResolutionSelector):
    @classmethod
    def INPUT_TYPES(cls):
        """
        Return a dictionary which contains config for all input fields.
        """
        resolution_strings = [ f"{width} x {height}" for width, height in SDXL_RESOLUTION ]
        
        return {
            "required": {
                "resolution": (resolution_strings,),
            }
        }