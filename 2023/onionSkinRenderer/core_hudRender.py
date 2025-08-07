import maya.api.OpenMayaRender as omr

"""
Adding HUD elements
Maya 2023 compatible version
"""
class viewRenderHUDRender(omr.MHUDRender):
    def __init__(self):
        omr.MHUDRender.__init__(self)

        self.target = None

    def __del__(self):
        self.target = None

    def targetOverrideList(self):
        if self.target is not None:
            return [self.target]
        return None

    def setRenderTarget(self, target):
        self.target = target
