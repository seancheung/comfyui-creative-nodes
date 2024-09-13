from .ns import PACKAGE_NAMESPACE, any_type

class StopFlow:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input": (any_type,),
                "enabled": ("BOOLEAN", {"default": False, "label_on": "on", "label_off": "off" }),
            },
        }
    RETURN_TYPES = (any_type,)
    FUNCTION = "run"
    CATEGORY = PACKAGE_NAMESPACE

    def run(self, input, enabled):
        return None if enabled else [input]
    
class SkipFromFlow:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input": (any_type,),
                "enabled": ("BOOLEAN", {"default": False, "label_on": "on", "label_off": "off" }),
            }
        }
    RETURN_TYPES = (any_type, "SKIP_FROM")
    FUNCTION = "run"
    CATEGORY = PACKAGE_NAMESPACE
    
    def run(self, input, enabled):
        skip_from = { "input": input }
        return (None if enabled else input, skip_from if enabled else None)
    
class SkipToFlow:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input": (any_type,),
                "skip_from": ("SKIP_FROM",),
                "none_if_skipped": ("BOOLEAN", {"default": False, "label_on": "yes", "label_off": "no" })
            }
        }
    RETURN_TYPES = (any_type,)
    FUNCTION = "run"
    CATEGORY = PACKAGE_NAMESPACE
    
    def run(self, input, skip_from, none_if_skipped):
        if skip_from:
            return None if none_if_skipped else skip_from["input"]
        return input