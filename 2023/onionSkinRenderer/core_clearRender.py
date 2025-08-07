import maya.api.OpenMayaRender as omr

"""
Fill the render with a color
Maya 2023 compatible version
"""
class viewRenderClearRender(omr.MClearOperation):
    def __init__(self, name):
        omr.MClearOperation.__init__(self, name)

        self.target = None

    def __del__(self):
        self.target = None

    def targetOverrideList(self):
        if self.target is not None:
            return [self.target]
        return None

    def setRenderTarget(self, target):
        self.target = target
