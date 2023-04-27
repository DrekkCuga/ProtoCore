from Outputs import Output
import cv2
import numpy as np

class CvOutput(Output.Output):
    
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

    def getName(self):
        return "Tk output"
    
    def Input(self, frame):
        frame = frame.resize((frame.width*self.scale, frame.height*self.scale))
        cv2.imshow(self.name, cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR))
        cv2.waitKey(1)
    
    def getArgs(self):
        return {
            "scale": {
                "types": [float, int],
                "default": 1
            }
        }