class SimpleAspectRatio:
    """
    A simple aspect ratio node

    Class methods
    -------------
    INPUT_TYPES (dict):
        Tell the main program input parameters of nodes.

    Attributes
    ----------
    RETURN_TYPES (`tuple`):
        The type of each element in the output tulple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tulple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        """
        Return a dictionary which contains config for all input fields.
        Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
        Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
        The type can be a list for selection.

        Returns: `dict`:
            - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
            - Value input_fields (`dict`): Contains input fields config:
                * Key field_name (`string`): Name of a entry-point method's argument
                * Value field_config (`tuple`):
                    + First value is a string indicate the type of field or a list for selection.
                    + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """

        ASPECT_RATIO_LIST = [
            "1:1 - 512x512",
            "1:1 - 768x768",
            "1:1 - 1024x1024",
            "3:2 - 768x512",
            "3:2 - 1216x832",
            "4:3 - 768x576",
            "4:3 - 1024x768",
            "4:3 - 1152x896",
            "8:5 - 1216x768",
            "16:9 - 1024x576",
            "16:9 - 1344x768",
        ]
        ORIENTATION = ["portrait", "landscape"]

        return {
            "required": {
                "aspectRatio": (ASPECT_RATIO_LIST,),
                "orientation": (ORIENTATION,),
            }
        }

    RETURN_TYPES = (
        "INT",
        "INT",
    )
    RETURN_NAMES = (
        "width",
        "height",
    )

    FUNCTION = "get_size"

    # OUTPUT_NODE = False

    CATEGORY = "utils"

    def get_size(self, aspectRatio, orientation):
        [width, height] = aspectRatio.split(" - ")[1].split("x")
        if orientation == "landscape":
            width, height = height, width
        return (int(width), int(height))


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {"SimpleAspectRatio": SimpleAspectRatio}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {"SimpleAspectRatio": "Simple Aspect Ratio"}
