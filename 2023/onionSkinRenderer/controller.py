import pymel.core as pm
import maya.cmds as cmds
import maya.api.OpenMaya as om  # เอมิลี่เพิ่มสำหรับ sync with core
import os
import json
import inspect

# Maya version compatibility - เอมิลี่จัดให้นะคะ~
try:
    # Maya 2024+ uses PySide6
    from PySide6 import QtWidgets, QtCore, QtGui
    from shiboken6 import wrapInstance
    PYSIDE_VERSION = 6
    print("🎯 OnionSkinRenderer: Using PySide6 (Maya 2024+)")
except ImportError:
    try:
        # Maya 2023 and earlier use PySide2
        from PySide2 import QtWidgets, QtCore, QtGui
        from shiboken2 import wrapInstance
        PYSIDE_VERSION = 2
        print("🎯 OnionSkinRenderer: Using PySide2 (Maya 2023)")
    except ImportError:
        raise ImportError("❌ Neither PySide6 nor PySide2 found. Please check your Maya installation.")

import maya.OpenMayaUI as omui
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

import onionSkinRenderer.core as core
try:
    import onionSkinRenderer.ui_window as ui_window
    import onionSkinRenderer.wdgt_Frame as wdgt_Frame
    import onionSkinRenderer.wdgt_MeshListObj as wdgt_MeshListObj
    import onionSkinRenderer.wdgt_Preferences as wdgt_Preferences
    import onionSkinRenderer.core_clearRender as clearRender
    import onionSkinRenderer.core_hudRender as hudRender
    import onionSkinRenderer.core_presentTarget as presentTarget
    import onionSkinRenderer.core_quadRender as quadRender
    import onionSkinRenderer.core_sceneRender as sceneRender
except ImportError as e:
    print(f"OnionSkinRenderer: Import error - {e}")
    raise


'''
2023 Version
Compatible with Maya 2023 (PySide2) and Maya 2024+ (PySide6)
using Python 3
'''

'''
Naming Conventions:
    Global variables: are in caps, seperated by "_"
    os: abbreviation for onion skin
    osr: abbreviation for onion skin renderer
'''


DEBUG_ALL = False  # Fixed: Disabled auto-detection to prevent window issues


# wrapper to get mayas main window
def getMayaMainWindow():
    mayaPtr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(mayaPtr), QtWidgets.QWidget)



# global variable holding the instance of the window
OSR_WINDOW = None

def closeExistingWindow():
    """🧹 Proper cleanup of existing window - เอมิลี่จัดให้เลยนะคะ~"""
    global OSR_WINDOW
    
    if OSR_WINDOW is not None:
        print("🗑️ OnionSkinRenderer: Cleaning up existing window...")
        
        try:
            # 🚨 Mark this as a reopen scenario to preserve core
            OSR_WINDOW._isReopeningWindow = True
            
            # 1. Stop detection timer
            if hasattr(OSR_WINDOW, 'mayaDetectionTimer'):
                OSR_WINDOW.mayaDetectionTimer.stop()
                OSR_WINDOW.mayaDetectionTimer.deleteLater()
            
            # 2. Disconnect signals
            try:
                OSR_WINDOW.disconnect()
            except:
                pass
            
            # 3. Close and delete the window
            if OSR_WINDOW.isVisible():
                OSR_WINDOW.close()
            
            # 4. Force deletion from Qt object tree
            OSR_WINDOW.setParent(None)
            OSR_WINDOW.deleteLater()
            
            # 5. Clear the global reference
            OSR_WINDOW = None
            
            # 6. Force garbage collection (optional but recommended)
            import gc
            gc.collect()
            
            print("✅ OnionSkinRenderer: Window cleanup completed (core preserved)")
            
        except Exception as e:
            print(f"⚠️ OnionSkinRenderer: Cleanup warning - {e}")
            # Force clear the reference even if cleanup fails
            OSR_WINDOW = None

# convenient function to open the osr ui
def show(develop = False, dockable = False):
    """🚀 Show OnionSkinRenderer with proper window management"""
    global OSR_WINDOW

    if develop:
        print("🔄 OnionSkinRenderer: Hot reloading modules...")
        import importlib
        importlib.reload(core)
        importlib.reload(clearRender)
        importlib.reload(hudRender)
        importlib.reload(presentTarget)
        importlib.reload(quadRender)
        importlib.reload(sceneRender)
        importlib.reload(wdgt_Frame)
        importlib.reload(ui_window)	
        importlib.reload(wdgt_MeshListObj)
        importlib.reload(wdgt_Preferences)

    # 🧹 Clean up any existing window first
    closeExistingWindow()
    
    # 🆕 Create new window instance
    print("🎨 OnionSkinRenderer: Creating new window...")
    OSR_WINDOW = OSRController()
    # if somebody reads this because they want to make it dockable
    # please contact me. I'd like to have it dockable as well
    # but it just never works
    OSR_WINDOW.show(dockable = False)
    print("✨ OnionSkinRenderer: Window opened successfully")
    
    return OSR_WINDOW
    


class SettingsManager(object):
    """
    Handles loading and saving of the tool's settings to a JSON file.
    """
    def __init__(self, controller):
        self.controller = controller
        self.toolPath = controller.toolPath
        self.preferences = {}

    def loadSettings(self):
        """Load settings from settings.txt and apply them to the UI and core."""
        try:
            with open(os.path.join(self.toolPath, 'settings.txt')) as json_file:
                self.preferences = json.load(json_file)
        except (IOError, ValueError):
            self.preferences = {} # Start with empty prefs if file doesn't exist or is corrupt

        c = self.controller
        c.preferences = self.preferences # Also assign to controller for window geometry compatibility.

        c.settings_autoClearBuffer.setChecked(self.preferences.setdefault('autoClearBuffer', True))
        core.OSR_INSTANCE.setAutoClearBuffer(self.preferences.setdefault('autoClearBuffer', True))

        c.relative_keyframes_chkbx.setChecked(self.preferences.setdefault('displayKeyframes', True))
        core.OSR_INSTANCE.setRelativeDisplayMode(self.preferences.setdefault('displayKeyframes', True))

        c.setOnionSkinColor(c.relative_futureTint_btn, self.preferences.setdefault('rFutureTint', [0, 0, 125]))
        c.setOnionSkinColor(c.relative_pastTint_btn, self.preferences.setdefault('rPastTint', [0, 125, 0]))
        c.setOnionSkinColor(c.absolute_tint_btn, self.preferences.setdefault('aTint', [125, 0, 0]))
        core.OSR_INSTANCE.setTintSeed(self.preferences.setdefault('tintSeed', 0))
        c.tint_type_cBox.setCurrentIndex(self.preferences.setdefault('tintType', 0))

        c.onionType_cBox.setCurrentIndex(self.preferences.setdefault('onionType', 1))
        c.drawBehind_chkBx.setChecked(self.preferences.setdefault('drawBehind', True))

        c.relativeFrameCount = self.preferences.setdefault('relativeFrameAmount', 4) * 2
        c.refreshRelativeFrame()
        activeRelativeFrames = self.preferences.setdefault('activeRelativeFrames', [])
        for child in c.relative_frame.findChildren(OnionListFrame):
            if int(child.frame_number.text()) in activeRelativeFrames:
                child.frame_visibility_btn.setChecked(True)

        c.relative_step_spinBox.setValue(self.preferences.setdefault('relativeStep', 1))

        core.OSR_INSTANCE.setMaxBuffer(self.preferences.setdefault('maxBufferSize', 200))
        core.OSR_INSTANCE.setOutlineWidth(self.preferences.setdefault('outlineWidth', 3))

    def saveSettings(self):
        """Save the current UI and core settings to settings.txt."""
        if DEBUG_ALL: print('start save')
        c = self.controller
        data = {}
        data['autoClearBuffer'] = c.settings_autoClearBuffer.isChecked()
        data['displayKeyframes'] = c.relative_keyframes_chkbx.isChecked()
        data['rFutureTint'] = self._extractRGBFromStylesheet(c.relative_futureTint_btn.styleSheet())
        data['rPastTint'] = self._extractRGBFromStylesheet(c.relative_pastTint_btn.styleSheet())
        data['aTint'] = self._extractRGBFromStylesheet(c.absolute_tint_btn.styleSheet())
        data['tintSeed'] = core.OSR_INSTANCE.getTintSeed()
        data['tintType'] = c.tint_type_cBox.currentIndex()
        data['relativeFrameAmount'] = c.relativeFrameCount // 2
        data['relativeStep'] = c.relative_step_spinBox.value()
        data['maxBufferSize'] = core.OSR_INSTANCE.getMaxBuffer()
        data['outlineWidth'] = core.OSR_INSTANCE.getOutlineWidth()
        data['onionType'] = c.onionType_cBox.currentIndex()
        data['drawBehind'] = c.drawBehind_chkBx.isChecked()
        data['activeRelativeFrames'] = c.getActiveRelativeFrameIndices()

        # The controller updates its own 'preferences' dictionary with window geometry.
        # We'll pull that in here before saving.
        if 'windowGeometry' in c.preferences:
            data['windowGeometry'] = c.preferences['windowGeometry']

        try:
            with open(os.path.join(self.toolPath, 'settings.txt'), 'w') as outfile:
                json.dump(data, outfile, indent=4)
            if DEBUG_ALL: print('end save - success')
        except Exception as e:
            if DEBUG_ALL: print(f'Settings save error: {e}')

    def _extractRGBFromStylesheet(self, s):
        """Utility to get an RGB list from a Qt stylesheet color string."""
        return [int(x) for x in (s[s.find("(") + 1:s.find(")")]).split(',')]


'''
ONION SKIN RENDERER MAIN UI
This class is the main ui window. It manages all user events and links to the core
'''
class OSRController(MayaQWidgetDockableMixin, QtWidgets.QMainWindow, ui_window.Ui_onionSkinRenderer):

    # 
    def __init__(self, parent = getMayaMainWindow()):
        super(OSRController, self).__init__(parent)
        # the dockable feature creates this control that needs to be deleted manually
        # otherwise it throws an error that this name already exists
        self.deleteControl('onionSkinRendererWorkspaceControl')
        
        # 🚨 Smart Core Management - only initialize if not exists
        if core.OSR_INSTANCE is None:
            print('🆕 OnionSkinRenderer: Initializing new core instance')
            core.initializeOverride()
        else:
            print('🔄 OnionSkinRenderer: Reusing existing core instance')
        
        # member variables
        self.targetObjectsSet = set()
        self.absoluteFramesSet = set()
        self.preferences = {}
        self.relativeFrameCount = 8
        self.toolPath = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
        self.activeEditor = None
        
        # Auto Maya detection functionality - เอมิลี่จัดให้เลยนะคะ~ (Simple & Reliable)
        self.autoDetectMaya = True  # Always enabled
        self.mayaMainWindow = parent
        self.lastMayaState = True  # Assume Maya active at start
        
        # Check if Windows process detection is available
        try:
            import ctypes
            self._checkWindowsProcess = self._checkWindowsProcess  # Enable Windows detection
            if DEBUG_ALL: print('🔍 Windows process detection enabled')
        except ImportError:
            if DEBUG_ALL: print('🔍 Windows process detection not available')
        
        # --- Maya Activity Detection Timer (Currently Disabled) ---
        # This timer is intended to automatically toggle the window's "Always on Top" state
        # based on whether Maya is the active application. It is currently disabled because
        # the implementation caused bugs, including the window "jumping" or moving unexpectedly
        # when the state changed.
        #
        # Future work to re-enable this feature should focus on:
        # 1. A more reliable method of checking if Maya is the active application. The current
        #    `isMayaCurrentlyActive` method is complex and uses multiple fallbacks.
        # 2. Ensuring that changing window flags with `setWindowFlags` does not reset the
        #    window's position or size. The code attempts to save and restore geometry, but
        #    this was not fully effective and led to the "jumping" issue. A robust solution
        #    might involve platform-specific API calls or a different approach to managing
        #    the "Always on Top" state that doesn't require recreating the window.
        #
        self.mayaDetectionTimer = QtCore.QTimer()
        self.mayaDetectionTimer.timeout.connect(self.detectMayaActivity)
        # self.mayaDetectionTimer.start(800) # DISABLED due to window position bugs.
        
        # create the ui from the compiled qt designer file
        self.setupUi(self)

        # Qt attribute compatibility
        if PYSIDE_VERSION == 6:
            self.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose)
        else:
            self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # Setup the settings manager BEFORE creating connections that use it.
        self.settings_manager = SettingsManager(self)

        self.createConnections()

        # Set unique object name for identification - เอมิลี่จัดให้เลยนะคะ~
        self.setObjectName("onionSkinRendererMainWindow")
        
        # FIXED: Remove default always on top - user controls manually
        # self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        
        # Load settings now that UI and connections are established.
        self.settings_manager.loadSettings()
        
        # 🔧 Restore window geometry from previous session
        self.restoreWindowGeometry()
        
        # 🔄 Sync UI state with Core state - เอมิลี่จัดให้เลยนะคะ~
        self.syncWithCore()
        
        # 🎬 Setup scene change detection
        self.setupSceneChangeDetection()

    def detectMayaActivity(self):
        """Detect if Maya is currently active - เอมิลี่จัดให้เลยนะคะ~"""
        try:
            mayaIsActive = self.isMayaCurrentlyActive()
            
            # Only update if state changed to avoid unnecessary window operations
            if mayaIsActive != self.lastMayaState:
                self.lastMayaState = mayaIsActive
                self.updateWindowState(mayaIsActive)
                
        except Exception as e:
            if DEBUG_ALL: print(f'🔍 Maya detection error: {e}')
    
    def isMayaCurrentlyActive(self):
        """Check if Maya is the currently active application"""
        try:
            # Method 1: Check if Maya main window is active (most reliable)
            if self.mayaMainWindow.isActiveWindow():
                return True
            
            # Method 2: Check if any Maya child window is active
            activeWindow = QtWidgets.QApplication.activeWindow()
            if activeWindow and self.isWindowRelatedToMaya(activeWindow):
                return True
            
            # Method 3: Process-level check - if another app is clearly active, Maya is not
            try:
                app = QtWidgets.QApplication.instance()
                appState = app.applicationState()
                
                # If Qt says the application is not active, Maya is definitely not active
                if appState != QtCore.Qt.ApplicationActive:
                    return False
                    
            except Exception as e:
                if DEBUG_ALL: print(f'🔍 App state check error: {e}')
            
            # Method 4: Windows-specific process check (more accurate)
            if hasattr(self, '_checkWindowsProcess'):
                return self._checkWindowsProcess()
            
            # Method 5: Final fallback - check if our window is visible but not active
            # This indicates another app might be active
            if self.isVisible() and not self.isActiveWindow():
                # Check if any other non-Maya window might be active
                try:
                    activeWidget = QtWidgets.QApplication.activeWidget()
                    if activeWidget and not self.isWindowRelatedToMaya(activeWidget):
                        return False
                except:
                    pass
            
            # Conservative fallback: assume Maya is active
            return True
            
        except Exception as e:
            if DEBUG_ALL: print(f'🔍 Maya activity check error: {e}')
            return True  # Conservative fallback
    
    def _checkWindowsProcess(self):
        """Windows-specific method to check if Maya is the foreground process"""
        try:
            import ctypes
            import ctypes.wintypes
            import os
            
            # Get foreground window handle
            user32 = ctypes.windll.user32
            hwnd = user32.GetForegroundWindow()
            
            if not hwnd:
                return True  # Can't determine, assume Maya is active
            
            # Get process ID of foreground window
            foreground_pid = ctypes.wintypes.DWORD()
            user32.GetWindowThreadProcessId(hwnd, ctypes.byref(foreground_pid))
            
            # Get current Maya process ID
            current_pid = os.getpid()
            
            # Maya is active only if foreground process is Maya
            is_maya_active = (foreground_pid.value == current_pid)
            
            if DEBUG_ALL:
                print(f'🔍 Windows check: Maya PID={current_pid}, Foreground PID={foreground_pid.value}, Maya Active={is_maya_active}')
            
            return is_maya_active
            
        except ImportError:
            # Not Windows or missing libraries
            if DEBUG_ALL: print('🔍 Windows libraries not available')
            return True
        except Exception as e:
            if DEBUG_ALL: print(f'🔍 Windows process check error: {e}')
            return True
    
    def isWindowRelatedToMaya(self, window):
        """Check if a window belongs to Maya"""
        try:
            if not window:
                return False
            
            # Check window hierarchy
            current = window
            for _ in range(10):  # Limit depth to avoid infinite loops
                if current == self.mayaMainWindow:
                    return True
                    
                # Check object name for Maya indicators
                objName = current.objectName()
                if objName and ('maya' in objName.lower() or 'MayaWindow' in objName):
                    return True
                    
                # Check window title for Maya indicators
                title = current.windowTitle()
                if title and ('maya' in title.lower() or 'autodesk' in title.lower()):
                    return True
                
                parent = current.parent()
                if not parent or parent == current:
                    break
                current = parent
            
            return False
        except:
            return False
    
    def updateWindowState(self, mayaIsActive):
        """Update window always-on-top state based on Maya activity - Fixed window movement"""
        try:
            currentFlags = self.windowFlags()
            hasAlwaysOnTop = bool(currentFlags & QtCore.Qt.WindowStaysOnTopHint)
            
            if mayaIsActive and not hasAlwaysOnTop:
                # Maya is active, enable always on top
                # 🔧 FIXED: Properly save and restore window geometry
                savedGeometry = self.saveGeometry()  # This includes position, size, and window state
                savedWindowState = self.saveState() if hasattr(self, 'saveState') else None
                
                # Change the window flags
                self.setWindowFlags(currentFlags | QtCore.Qt.WindowStaysOnTopHint)
                
                # Show the window (required after setWindowFlags)
                self.show()
                
                # 🔧 FIXED: Restore the exact geometry and state
                self.restoreGeometry(savedGeometry)
                if savedWindowState:
                    self.restoreState(savedWindowState)
                
                # 🔧 FIXED: Force window to activate and stay in correct position
                self.activateWindow()
                self.raise_()
                
                if DEBUG_ALL: print("🔼 OnionSkinRenderer: Auto-enabled (Maya active) - Position preserved")
                
            elif not mayaIsActive and hasAlwaysOnTop:
                # Maya not active, disable always on top
                # 🔧 FIXED: Properly save and restore window geometry
                savedGeometry = self.saveGeometry()  # This includes position, size, and window state
                savedWindowState = self.saveState() if hasattr(self, 'saveState') else None
                
                # Change the window flags
                self.setWindowFlags(currentFlags & ~QtCore.Qt.WindowStaysOnTopHint)
                
                # Show the window (required after setWindowFlags)
                self.show()
                
                # 🔧 FIXED: Restore the exact geometry and state
                self.restoreGeometry(savedGeometry)
                if savedWindowState:
                    self.restoreState(savedWindowState)
                
                if DEBUG_ALL: print("🔽 OnionSkinRenderer: Auto-disabled (Maya inactive) - Position preserved")
                
        except Exception as e:
            if DEBUG_ALL: print(f'🔍 Window state update error: {e}')

    #
    def closeEvent(self, event):
        """🚪 Enhanced close event handler with geometry saving - เอมิลี่จัดให้เลยนะคะ~"""
        if DEBUG_ALL: print('🚪 OnionSkinRenderer: Close event triggered')
        
        # 🔧 Save window geometry before closing
        self.saveWindowGeometry()
        
        # 🚨 Check if this is a "reopen" scenario vs actual close
        self.isReopeningWindow = getattr(self, '_isReopeningWindow', False)
        
        try:
            # 1. Stop detection timer
            if hasattr(self, 'mayaDetectionTimer'):
                self.mayaDetectionTimer.stop()
                self.mayaDetectionTimer.deleteLater()
            
            # 1.5. Clean up scene change callbacks
            if hasattr(self, 'sceneCallback'):
                import maya.OpenMaya as om
                om.MMessage.removeCallback(self.sceneCallback)
                om.MMessage.removeCallback(self.sceneCallback2)
                if DEBUG_ALL: print('🎬 Scene callbacks cleaned up')
            
            # 2. Save settings before closing (now includes geometry)
            self.settings_manager.saveSettings()
            
            # 3. 🚨 ONLY uninitialize Core if this is a REAL close, not a reopen
            if not self.isReopeningWindow:
                print('🚨 OnionSkinRenderer: Real close - uninitializing core')
                core.uninitializeOverride()
            else:
                print('🔄 OnionSkinRenderer: Reopen close - preserving core')
            
            # 4. Disconnect all signals
            try:
                self.disconnect()
            except:
                pass
            
            # 5. Clear global reference
            global OSR_WINDOW
            if OSR_WINDOW is self:
                OSR_WINDOW = None
            
            if DEBUG_ALL: print('✅ OnionSkinRenderer: Close event completed')
            
        except Exception as e:
            if DEBUG_ALL: print(f'⚠️ OnionSkinRenderer: Close event warning - {e}')
        
        # Accept the close event
        event.accept()
    
    # special event for the dockable feature
    def dockCloseEventTriggered(self, event):
        """🚪 Enhanced dock close event handler"""
        if DEBUG_ALL: print('🚪 OnionSkinRenderer: Dock close event triggered')
        
        try:
            # Stop detection timer
            if hasattr(self, 'mayaDetectionTimer'):
                self.mayaDetectionTimer.stop()
                self.mayaDetectionTimer.deleteLater()
            
            # Save and cleanup
            self.settings_manager.saveSettings()
            core.uninitializeOverride()
            
            # Clear global reference
            global OSR_WINDOW
            if OSR_WINDOW is self:
                OSR_WINDOW = None
                
            if DEBUG_ALL: print('✅ OnionSkinRenderer: Dock close completed')
            
        except Exception as e:
            if DEBUG_ALL: print(f'⚠️ OnionSkinRenderer: Dock close warning - {e}')

    # code from https://gist.github.com/liorbenhorin/217bfb7e54c6f75b9b1b2b3d73a1a43a
    def deleteControl(self, control):
        if DEBUG_ALL: print('delete Control')
        if cmds.workspaceControl(control, q=True, exists=True):
            cmds.workspaceControl(control, e=True, close=True)
            cmds.deleteUI(control, control=True)

    #
    def createConnections(self):
        self.targetObjects_add_btn.clicked.connect(self.addSelectedToTargetObjects)
        self.targetObjects_remove_btn.clicked.connect(self.removeSelectedFromTargetObjects)
        self.targetObjects_clear_btn.clicked.connect(self.clearTargetObjects)

        self.toggleRenderer_btn.clicked.connect(self.toggleRenderer)
        self.globalOpacity_slider.sliderMoved.connect(self.setGlobalOpacity)
        self.onionType_cBox.currentTextChanged.connect(self.setOnionSkinDisplayMode)
        self.drawBehind_chkBx.stateChanged.connect(self.setDrawBehind)

        self.tint_type_cBox.currentTextChanged.connect(self.setTintType)
        self.relative_futureTint_btn.clicked.connect(self.pickColor)
        self.relative_pastTint_btn.clicked.connect(self.pickColor)
        self.relative_tint_strength_slider.sliderMoved.connect(self.setTintStrength)
        self.relative_keyframes_chkbx.clicked.connect(self.toggleRelativeKeyframeDisplay)
        self.relative_step_spinBox.valueChanged.connect(self.setRelativeStep)

        self.absolute_tint_btn.clicked.connect(self.pickColor)
        self.absolute_addCrnt_btn.clicked.connect(self.addAbsoluteTargetFrame)
        self.absolute_add_btn.clicked.connect(self.addAbsoluteTargetFrameFromSpinbox)
        self.absolute_clear_btn.clicked.connect(self.clearAbsoluteTargetFrames)

        self.settings_clearBuffer.triggered.connect(self.clearBuffer)
        self.settings_autoClearBuffer.triggered.connect(self.setAutoClearBuffer)
        self.settings_preferences.triggered.connect(self.changePrefs)  # FIXED: Connect preferences menu
        self.settings_saveSettings.triggered.connect(self.settings_manager.saveSettings)

        self.targetObjects_grp.clicked.connect(self.toggleGroupBox)
        self.onionSkinFrames_grp.clicked.connect(self.toggleGroupBox)
        self.onionSkinSettings_grp.clicked.connect(self.toggleGroupBox)



    # ------------------
    # UI REFRESH

    # 
    def refreshObjectList(self):
        self.targetObjects_list.clear()
        for obj in self.targetObjectsSet:
            listWidget = TargetObjectListWidget()
            listWidget.object_label.setText(obj.nodeName())
            listWidget.object_remove_btn.clicked.connect(lambda b_obj = obj: self.removeTargetObject(b_obj))
            listItem = QtWidgets.QListWidgetItem()
            listItem.setSizeHint(listWidget.sizeHint())
            self.targetObjects_list.addItem(listItem)
            self.targetObjects_list.setItemWidget(listItem, listWidget)

    # 
    def refreshRelativeFrame(self):
        activeFrames = []
        # clear the frame of all widgets first
        for child in self.relative_frame.findChildren(OnionListFrame):
            if child.frame_visibility_btn.isChecked():
                activeFrames.append(int(child.frame_number.text()))
            child.setParent(None)
        
        # fill the relative frames list
        for index in range(self.relativeFrameCount + 1):
            if not index-self.relativeFrameCount//2 == 0:
                listWidget = OnionListFrame()
                frame = index-self.relativeFrameCount//2
                listWidget.frame_number.setText(str(frame))
                listWidget.frame_opacity_slider.setValue(75//abs(index-self.relativeFrameCount//2))
                listWidget.frame_visibility_btn.toggled.connect(self.toggleRelativeTargetFrame)
                if frame in activeFrames: 
                    listWidget.frame_visibility_btn.setChecked(True)
                    activeFrames.remove(frame)
                listWidget.frame_opacity_slider.sliderMoved.connect(self.setOpacityForRelativeTargetFrame)
                self.relative_frame_layout.addWidget(listWidget)

        # remove all remaining frames from onion skin renderer
        # since their visibility is no longer accesible from ui
        for frame in activeFrames:
            core.OSR_INSTANCE.removeRelativeOnion(frame)

    # 
    def refreshAbsoluteFrameTargetsList(self):
        # remove any entries that don't exist anymore
        framesInList = []
        for i in reversed(range(self.absolute_list.count())):
            frame = self.absolute_list.item(i).data(QtCore.Qt.UserRole)
            framesInList.append(frame)
            if frame not in self.absoluteFramesSet:
                self.absolute_list.takeItem(i)
        
        # add any missing entry
        for frame in self.absoluteFramesSet:
            if frame not in framesInList:
                listWidget = OnionListFrame()
                listWidget.frame_number.setText(str(int(frame)))
                listWidget.frame_opacity_slider.setValue(core.OSR_INSTANCE.getOpacityOfAbsoluteFrame(int(frame)))
                listWidget.addRemoveButton()
                listWidget.frame_visibility_btn.setChecked(core.OSR_INSTANCE.absoluteTargetFrameExists(int(frame)))
                listWidget.frame_remove_btn.clicked.connect(lambda b_frame = frame: self.removeAbsoluteTargetFrame(b_frame))
                listWidget.frame_visibility_btn.toggled.connect(self.toggleAbsoluteTargetFrame)
                listWidget.frame_opacity_slider.sliderMoved.connect(self.setOpacityForAbsoluteTargetFrame)
                listItem = QtWidgets.QListWidgetItem()
                listItem.setData(QtCore.Qt.UserRole, int(frame))
                listItem.setSizeHint(listWidget.sizeHint())
                # insert item at correct position
                correctRow = 0
                for i in range(self.absolute_list.count()):
                    if frame < self.absolute_list.item(i).data(QtCore.Qt.UserRole):
                        break
                    correctRow = i+1
                
                self.absolute_list.insertItem(correctRow, listItem)
                self.absolute_list.setItemWidget(listItem, listWidget)




    # ---------------------------
    # CONNECTIONS

    # 
    def addSelectedToTargetObjects(self):
        core.OSR_INSTANCE.addSelectedTargetObject()
        for obj in pm.selected():
            self.targetObjectsSet.add(obj)
        self.refreshObjectList()
    
    # 
    def removeSelectedFromTargetObjects(self):
        core.OSR_INSTANCE.removeSelectedTargetObject()
        for obj in pm.selected():
            if obj in self.targetObjectsSet:
                self.targetObjectsSet.remove(obj)
        self.refreshObjectList()

    #
    def removeTargetObject(self, obj):
        try:
            core.OSR_INSTANCE.removeTargetObject(obj.fullPath())
        except:
            core.OSR_INSTANCE.removeTargetObject(obj.nodeName())
        self.targetObjectsSet.remove(obj)
        self.refreshObjectList()

    #
    def clearTargetObjects(self):
        core.OSR_INSTANCE.clearTargetObjects()
        self.targetObjectsSet.clear()
        self.refreshObjectList()

    # 
    def toggleRelativeTargetFrame(self):
        sender = self.sender()
        frame = sender.parent().findChild(QtWidgets.QLabel, 'frame_number').text()
        sliderValue = sender.parent().findChild(QtWidgets.QSlider, 'frame_opacity_slider').value()
        if sender.isChecked():
            core.OSR_INSTANCE.addRelativeTargetFrame(frame, sliderValue)
        else:
            core.OSR_INSTANCE.removeRelativeTargetFrame(frame)

    #
    def toggleRelativeKeyframeDisplay(self):
        sender = self.sender()
        core.OSR_INSTANCE.setRelativeDisplayMode(self.sender().isChecked())
        self.settings_manager.saveSettings()

    # 
    def addAbsoluteTargetFrame(self, **kwargs):
        frame = kwargs.setdefault('frame', pm.animation.getCurrentTime())
        if int(frame) not in self.absoluteFramesSet:
            core.OSR_INSTANCE.addAbsoluteTargetFrame(frame, 50)
            self.absoluteFramesSet.add(frame)
            self.refreshAbsoluteFrameTargetsList()

    #
    def addAbsoluteTargetFrameFromSpinbox(self):
        frame = self.sender().parent().findChild(QtWidgets.QSpinBox, 'absolute_add_spinBox').value()
        self.addAbsoluteTargetFrame(frame = frame)

    #
    def toggleAbsoluteTargetFrame(self):
        sender = self.sender()
        frame = sender.parent().findChild(QtWidgets.QLabel, 'frame_number').text()
        sliderValue = sender.parent().findChild(QtWidgets.QSlider, 'frame_opacity_slider').value()
        if sender.isChecked():
            core.OSR_INSTANCE.addAbsoluteTargetFrame(frame, sliderValue)
        else:
            core.OSR_INSTANCE.removeAbsoluteTargetFrame(frame)
    
    #
    def removeAbsoluteTargetFrame(self, frame):
        core.OSR_INSTANCE.removeAbsoluteTargetFrame(frame)
        self.absoluteFramesSet.remove(frame)
        self.refreshAbsoluteFrameTargetsList()

    #
    def clearAbsoluteTargetFrames(self):
        core.OSR_INSTANCE.clearAbsoluteTargetFrames()
        self.absoluteFramesSet.clear()
        self.refreshAbsoluteFrameTargetsList()

    # 
    def clearBuffer(self):
        core.OSR_INSTANCE.clearOnionSkinBuffer()

    # 
    def pickColor(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self.setOnionSkinColor(self.sender(), color.getRgb())
        self.settings_manager.saveSettings()

    #
    def setOpacityForRelativeTargetFrame(self):
        opacity = self.sender().value()
        frame = self.sender().parent().findChild(QtWidgets.QLabel, 'frame_number').text()
        core.OSR_INSTANCE.setOpacityForRelativeTargetFrame(frame, opacity)

    #
    def setOpacityForAbsoluteTargetFrame(self):
        opacity = self.sender().value()
        frame = self.sender().parent().findChild(QtWidgets.QLabel, 'frame_number').text()
        core.OSR_INSTANCE.setOpacityForAbsoluteTargetFrame(int(frame), opacity)

    # 
    def setTintStrength(self):
        core.OSR_INSTANCE.setTintStrength(
            self.sender().value()
        )

    # 
    def setAutoClearBuffer(self):
        value = self.sender().isChecked()
        core.OSR_INSTANCE.setAutoClearBuffer(value)

    #
    def changePrefs(self):
        prefUi = PreferencesWindow(self)
        if prefUi.exec():
            values = prefUi.getValues()
            core.OSR_INSTANCE.setMaxBuffer(values['maxBuffer'])
            core.OSR_INSTANCE.setOutlineWidth(values['outlineWidth'])
            core.OSR_INSTANCE.setTintSeed(values['tintSeed'])
            self.relativeFrameCount = values['relativeKeyCount']*2
            self.refreshRelativeFrame()
            self.settings_manager.saveSettings()
            
    #     
    def setRelativeStep(self):
        core.OSR_INSTANCE.setRelativeStep(self.sender().value())
        self.settings_manager.saveSettings()

    # togle active or saved editor between onion Skin Renderer and vp2
    def toggleRenderer(self):
        modelPanelList = []
        modelEditorList = pm.lsUI(editors=True)
        # find all model panels
        for myModelPanel in modelEditorList:
            if myModelPanel.find('modelPanel') != -1:
                modelPanelList.append(myModelPanel)

        onionPanel = None
        # if any of those is already set to onion skin renderer
        for modelPanel in modelPanelList:
            if pm.uitypes.ModelEditor(modelPanel).getRendererOverrideName() == 'onionSkinRenderer':
                onionPanel = pm.uitypes.ModelEditor(modelPanel)
                break

        # if there is a panel with the onion skin renderer
        # deactivate it and save the panel
        if onionPanel:
            try:
                # Always better to try in the case of active panel operations
                # as the active panel might not be a viewport.
                onionPanel.setRendererOverrideName('')
                self.activeEditor = onionPanel
            except Exception as e:
                # Handle exception
                print(e)
        else:
            # if there is a saved editor panel activate the renderer on it
            if self.activeEditor:
                self.activeEditor.setRendererOverrideName('onionSkinRenderer')
            # else toggle the active one
            else:
                for modelPanel in modelPanelList:
                    if pm.uitypes.ModelEditor(modelPanel).getActiveView():
                        try:
                            if pm.uitypes.ModelEditor(modelPanel).getRendererOverrideName() == '':
                                pm.uitypes.ModelEditor(modelPanel).setRendererOverrideName('onionSkinRenderer')
                            else:
                                pm.uitypes.ModelEditor(modelPanel).setRendererOverrideName('')
                        except Exception as e:
                            # Handle exception
                            print(e)   


    # 
    def setGlobalOpacity(self):
        core.OSR_INSTANCE.setGlobalOpacity(self.sender().value())

    #
    def setOnionSkinDisplayMode(self):
        core.OSR_INSTANCE.setOnionSkinDisplayMode(self.onionType_cBox.currentIndex())

    #
    def setDrawBehind(self):
        core.OSR_INSTANCE.setDrawBehind(self.drawBehind_chkBx.isChecked())

    #
    def toggleGroupBox(self):
        h = self.sender().maximumHeight()

        if h > 100000:
            self.sender().setMaximumHeight(14)
        else:
            self.sender().setMaximumHeight(200000)

    #
    def setTintType(self):
        tintType = self.tint_type_cBox.currentIndex()
        if tintType == 0:
            self.constant_col_widget.setMaximumHeight(16777215)
            self.constant_col_widget.setEnabled(True)
        else:
            self.constant_col_widget.setMaximumHeight(0)    
            self.constant_col_widget.setEnabled(False)
        core.OSR_INSTANCE.setTintType(tintType)
    
    # 🎬 ADDED: Scene change detection to clear onion skin
    def setupSceneChangeDetection(self):
        """Setup detection for when Maya scene changes"""
        try:
            # Add callback for scene changes
            import maya.OpenMaya as om
            self.sceneCallback = om.MSceneMessage.addCallback(
                om.MSceneMessage.kAfterNew, self.onSceneChanged
            )
            self.sceneCallback2 = om.MSceneMessage.addCallback(
                om.MSceneMessage.kAfterOpen, self.onSceneChanged
            )
            if DEBUG_ALL: print("🎬 Scene change detection enabled")
        except Exception as e:
            if DEBUG_ALL: print(f'🎬 Scene change detection error: {e}')
    
    def onSceneChanged(self, *args):
        """Called when Maya scene changes - clear onion skin data"""
        try:
            if core.OSR_INSTANCE:
                # Clear all onion skin data
                core.OSR_INSTANCE.clearTargetObjects()
                core.OSR_INSTANCE.clearAbsoluteTargetFrames()
                core.OSR_INSTANCE.clearOnionSkinBuffer()
                
                # Clear relative frames
                for onion in list(core.OSR_INSTANCE.relativeBlendPasses.keys()):
                    core.OSR_INSTANCE.removeRelativeTargetFrame(onion)
                
                # Clear UI
                self.targetObjectsSet.clear()
                self.absoluteFramesSet.clear()
                self.refreshObjectList()
                self.refreshAbsoluteFrameTargetsList()
                self.refreshRelativeFrame()
                
                print("🎬 OnionSkinRenderer: Cleared data for new scene")
        except Exception as e:
            if DEBUG_ALL: print(f'🎬 Scene change clear error: {e}')

            
            



    # UTILITY
    # 
    def setOnionSkinColor(self, btn, rgba):
            btn.setStyleSheet('background-color: rgb(%s,%s,%s);'%(rgba[0], rgba[1], rgba[2]))
            core.OSR_INSTANCE.setTint(rgba, btn.objectName())

    def getActiveRelativeFrameIndices(self):
        activeFrames = []
        # clear the frame of all widgets first
        for child in self.relative_frame.findChildren(OnionListFrame):
            if child.frame_visibility_btn.isChecked():
                activeFrames.append(int(child.frame_number.text()))
        return activeFrames
    
    # 🔧 BONUS: Enhanced window positioning system with persistent settings
    def saveWindowGeometry(self):
        """Save window geometry to settings - Enhanced version"""
        try:
            # Save to both Qt built-in geometry and custom position
            geometry = self.saveGeometry()
            
            # Also save individual components for extra reliability  
            windowData = {
                'geometry': geometry.toHex().data().decode() if hasattr(geometry, 'toHex') else str(geometry),
                'pos_x': self.pos().x(),
                'pos_y': self.pos().y(),
                'width': self.size().width(),
                'height': self.size().height(),
                'isMaximized': self.isMaximized(),
                'isMinimized': self.isMinimized()
            }
            
            # Save to your existing settings
            self.preferences['windowGeometry'] = windowData
            
            if DEBUG_ALL: print(f"🔧 Saved window geometry: pos({windowData['pos_x']}, {windowData['pos_y']}) size({windowData['width']}, {windowData['height']})")
            
        except Exception as e:
            if DEBUG_ALL: print(f'🔧 Save geometry error: {e}')

    def restoreWindowGeometry(self):
        """Restore window geometry from settings - Enhanced version"""
        try:
            if 'windowGeometry' in self.preferences:
                windowData = self.preferences['windowGeometry']
                
                # Try Qt's built-in restore first
                if 'geometry' in windowData:
                    try:
                        geometryBytes = QtCore.QByteArray.fromHex(windowData['geometry'].encode()) if isinstance(windowData['geometry'], str) else windowData['geometry']
                        self.restoreGeometry(geometryBytes)
                    except:
                        pass
                
                # Fallback to manual positioning
                if 'pos_x' in windowData and 'pos_y' in windowData:
                    self.move(int(windowData['pos_x']), int(windowData['pos_y']))
                
                if 'width' in windowData and 'height' in windowData:
                    self.resize(int(windowData['width']), int(windowData['height']))
                
                if DEBUG_ALL: print(f"🔧 Restored window geometry: pos({windowData.get('pos_x', 0)}, {windowData.get('pos_y', 0)}) size({windowData.get('width', 400)}, {windowData.get('height', 600)})")
        
        except Exception as e:
            if DEBUG_ALL: print(f'🔧 Restore geometry error: {e}')

    # 🔄 Enhanced State Management - เอมิลี่จัดให้เลยนะคะ~
    def syncWithCore(self):
        """🔄 Sync UI state with existing Core state - เอมิลี่จัดให้เลยนะคะ~"""
        if core.OSR_INSTANCE is None:
            print('🔄 OnionSkinRenderer: No core instance to sync with')
            return
            
        print('🔄 OnionSkinRenderer: Starting UI sync with core...')
        
        try:
            # Debug: Check what's in core
            self.debugCoreState()
            
            # 1. Restore target objects from core to UI
            self.restoreTargetObjectsFromCore()
            
            # 2. Restore relative frames from core
            self.restoreRelativeFramesFromCore()
            
            # 3. Restore absolute frames from core
            self.restoreAbsoluteFramesFromCore()
            
            print('✅ OnionSkinRenderer: UI sync with core completed')
            
        except Exception as e:
            print(f'⚠️ OnionSkinRenderer: Sync error - {e}')
            import traceback
            traceback.print_exc()
    
    def debugCoreState(self):
        """🔍 Debug what's actually in the core"""
        try:
            if hasattr(core.OSR_INSTANCE, 'onionObjectBuffer'):
                buffer = core.OSR_INSTANCE.onionObjectBuffer
                bufferLength = buffer.length()
                print(f'🔍 Core onionObjectBuffer has {bufferLength} items')
                
                if bufferLength > 0:
                    # Try to get object names from buffer
                    selIter = om.MItSelectionList(buffer)
                    objectNames = []
                    while not selIter.isDone():
                        try:
                            dagPath = selIter.getDagPath()
                            objectNames.append(dagPath.fullPathName())
                        except:
                            try:
                                # Try getting as dependency node
                                depNode = selIter.getDependNode()
                                fnDep = om.MFnDependencyNode(depNode)
                                objectNames.append(fnDep.name())
                            except:
                                objectNames.append("<unknown object>")
                        selIter.next()
                    
                    print(f'🔍 Objects in core buffer: {objectNames}')
                else:
                    print('🔍 Core buffer is empty')
            
            if hasattr(core.OSR_INSTANCE, 'onionObjectList'):
                listLength = core.OSR_INSTANCE.onionObjectList.length()
                print(f'🔍 Core onionObjectList has {listLength} items')
                
        except Exception as e:
            print(f'⚠️ Debug core state error: {e}')
    
    def restoreTargetObjectsFromCore(self):
        """🔄 Restore target objects from core to UI - Enhanced version"""
        print('🔄 Starting target objects restoration...')
        
        try:
            restored_count = 0
            
            # Method 1: Try onionObjectBuffer first
            if hasattr(core.OSR_INSTANCE, 'onionObjectBuffer'):
                buffer = core.OSR_INSTANCE.onionObjectBuffer
                if buffer.length() > 0:
                    print(f'🔄 Found {buffer.length()} objects in onionObjectBuffer')
                    restored_count += self._restoreFromSelectionList(buffer, "onionObjectBuffer")
            
            # Method 2: If that didn't work, try onionObjectList
            if restored_count == 0 and hasattr(core.OSR_INSTANCE, 'onionObjectList'):
                objectList = core.OSR_INSTANCE.onionObjectList
                if objectList.length() > 0:
                    print(f'🔄 Found {objectList.length()} objects in onionObjectList')
                    restored_count += self._restoreFromSelectionList(objectList, "onionObjectList")
            
            # Refresh UI
            if restored_count > 0:
                self.refreshObjectList()
                print(f'✅ Restored {restored_count} target objects to UI')
            else:
                print('ℹ️ No objects found in core to restore')
                
        except Exception as e:
            print(f'⚠️ Restore objects error: {e}')
            import traceback
            traceback.print_exc()
    
    def _restoreFromSelectionList(self, selectionList, source_name):
        """🔄 Helper function to restore objects from a Maya selection list"""
        restored_count = 0
        
        try:
            selIter = om.MItSelectionList(selectionList)
            
            while not selIter.isDone():
                try:
                    # Method 1: Try as DAG object
                    if selIter.itemType() == om.MItSelectionList.kDagSelectionItem:
                        dagPath = selIter.getDagPath()
                        objectName = dagPath.fullPathName()
                        
                        # Check if object still exists in Maya
                        if pm.objExists(objectName):
                            pmObj = pm.PyNode(objectName)
                            self.targetObjectsSet.add(pmObj)
                            restored_count += 1
                            print(f'✅ Restored DAG object: {objectName}')
                        else:
                            print(f'⚠️ Object no longer exists: {objectName}')
                    
                    # Method 2: Try as dependency node
                    elif selIter.itemType() == om.MItSelectionList.kDNselectionItem:
                        depNode = selIter.getDependNode()
                        fnDep = om.MFnDependencyNode(depNode)
                        objectName = fnDep.name()
                        
                        if pm.objExists(objectName):
                            pmObj = pm.PyNode(objectName)
                            self.targetObjectsSet.add(pmObj)
                            restored_count += 1
                            print(f'✅ Restored dependency node: {objectName}')
                        else:
                            print(f'⚠️ Object no longer exists: {objectName}')
                    
                    else:
                        print(f'⚠️ Unknown selection item type: {selIter.itemType()}')
                        
                except Exception as e:
                    print(f'⚠️ Error processing item from {source_name}: {e}')
                
                selIter.next()
                
        except Exception as e:
            print(f'⚠️ Error iterating through {source_name}: {e}')
        
        return restored_count
    
    def restoreRelativeFramesFromCore(self):
        """🔄 Restore relative frames from core to UI"""
        print('🔄 Starting relative frames restoration...')
        
        try:
            if hasattr(core.OSR_INSTANCE, 'relativeBlendPasses'):
                relativeFrames = core.OSR_INSTANCE.relativeBlendPasses
                
                if len(relativeFrames) > 0:
                    print(f'🔄 Found {len(relativeFrames)} relative frames in core')
                    
                    # Refresh relative frames with core data
                    self.refreshRelativeFrame()
                    
                    # Activate frames that exist in core
                    activated_count = 0
                    for frameOffset in relativeFrames.keys():
                        for child in self.relative_frame.findChildren(OnionListFrame):
                            if int(child.frame_number.text()) == frameOffset:
                                child.frame_visibility_btn.setChecked(True)
                                activated_count += 1
                                print(f'✅ Activated relative frame: {frameOffset}')
                                break
                    
                    print(f'✅ Restored {activated_count} relative frames to UI')
                else:
                    print('ℹ️ No relative frames found in core')
            else:
                print('ℹ️ Core has no relativeBlendPasses attribute')
                
        except Exception as e:
            print(f'⚠️ Restore relative frames error: {e}')
            import traceback
            traceback.print_exc()
    
    def restoreAbsoluteFramesFromCore(self):
        """🔄 Restore absolute frames from core to UI"""
        print('🔄 Starting absolute frames restoration...')
        
        try:
            if hasattr(core.OSR_INSTANCE, 'absoluteBlendPasses'):
                absoluteFrames = core.OSR_INSTANCE.absoluteBlendPasses
                
                if len(absoluteFrames) > 0:
                    print(f'🔄 Found {len(absoluteFrames)} absolute frames in core')
                    
                    # Add frames from core to UI
                    for frame in absoluteFrames.keys():
                        self.absoluteFramesSet.add(frame)
                        print(f'✅ Added absolute frame to UI set: {frame}')
                    
                    # Refresh UI list
                    self.refreshAbsoluteFrameTargetsList()
                    
                    print(f'✅ Restored {len(absoluteFrames)} absolute frames to UI')
                else:
                    print('ℹ️ No absolute frames found in core')
            else:
                print('ℹ️ Core has no absoluteBlendPasses attribute')
                
        except Exception as e:
            print(f'⚠️ Restore absolute frames error: {e}')
            import traceback
            traceback.print_exc()
    
    def forceResetAndRestart(self):
        """🚨 Force reset core and restart clean"""
        try:
            # Reset core state
            resetCore()
            
            # Clear UI state
            self.targetObjectsSet.clear()
            self.absoluteFramesSet.clear()
            
            # Refresh all UI elements
            self.refreshObjectList()
            self.refreshRelativeFrame()
            self.refreshAbsoluteFrameTargetsList()
            
            print("✅ OnionSkinRenderer: Force reset completed")
            
        except Exception as e:
            print(f"⚠️ OnionSkinRenderer: Force reset error - {e}")



'''
FRAME WIDGET
the widget for displaying a frame in a list. includes visibility, opacity slider
and on demand a remove button   
'''
class OnionListFrame(QtWidgets.QWidget, wdgt_Frame.Ui_onionSkinFrame_layout):
    def __init__(self, parent=None):
        super(OnionListFrame, self).__init__(parent)
        self.setupUi(self)

    def addRemoveButton(self):
        self.frame_remove_btn = QtWidgets.QPushButton('rm')
        if PYSIDE_VERSION == 6:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        else:
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_remove_btn.sizePolicy().hasHeightForWidth())
        self.frame_remove_btn.setSizePolicy(sizePolicy)
        self.frame_remove_btn.setMinimumSize(QtCore.QSize(16, 16))
        self.frame_remove_btn.setMaximumSize(QtCore.QSize(16, 16))
        self.frame_widget_layout.addWidget(self.frame_remove_btn)
        


'''
OBJECT WIDGET
the widget for displaying an object in a list
'''
class TargetObjectListWidget(QtWidgets.QWidget, wdgt_MeshListObj.Ui_onionSkinObject_layout):
    def __init__(self, parent=None):
        super(TargetObjectListWidget, self).__init__(parent)
        self.setupUi(self)



'''
Settings Dialog
in this window the user can set some preferences
'''
class PreferencesWindow(QtWidgets.QDialog, wdgt_Preferences.Ui_onionSkinRendererPreferences):
    def __init__(self, parent):
        super(PreferencesWindow, self).__init__(parent)
        self.setupUi(self)
        self.relativeKeyCount_spinBox.setValue(parent.relativeFrameCount//2)
        self.maxBuffer_spinBox.setValue(core.OSR_INSTANCE.getMaxBuffer())
        self.outlineWidth_spinBox.setValue(core.OSR_INSTANCE.getOutlineWidth())
        self.tintSeed_spinBox.setValue(core.OSR_INSTANCE.getTintSeed())

    def getValues(self):
        values = {}
        values['maxBuffer'] = self.maxBuffer_spinBox.value()
        values['relativeKeyCount'] = self.relativeKeyCount_spinBox.value()
        values['outlineWidth'] = self.outlineWidth_spinBox.value()
        values['tintSeed'] = self.tintSeed_spinBox.value()
        return values


# 🛠️ Utility functions for debugging and emergency cleanup
def getWindowState():
    """Get current window state for debugging"""
    global OSR_WINDOW
    
    if OSR_WINDOW is None:
        return "No window instance"
    
    return {
        "exists": OSR_WINDOW is not None,
        "visible": OSR_WINDOW.isVisible() if OSR_WINDOW else False,
        "object_name": OSR_WINDOW.objectName() if OSR_WINDOW else "None",
        "window_title": OSR_WINDOW.windowTitle() if OSR_WINDOW else "None",
        "parent": str(OSR_WINDOW.parent()) if OSR_WINDOW else "None"
    }

def debugCoreAndUI():
    """🔍 Debug both core and UI state"""
    global OSR_WINDOW
    
    print("🔍 ========== DEBUG CORE AND UI STATE ==========")
    
    if core.OSR_INSTANCE is None:
        print("⚠️ No core instance found")
    else:
        print("✅ Core instance exists")
        
        # Debug core buffers
        if hasattr(core.OSR_INSTANCE, 'onionObjectBuffer'):
            bufferLength = core.OSR_INSTANCE.onionObjectBuffer.length()
            print(f"🔍 Core onionObjectBuffer: {bufferLength} items")
        
        if hasattr(core.OSR_INSTANCE, 'onionObjectList'):
            listLength = core.OSR_INSTANCE.onionObjectList.length()
            print(f"🔍 Core onionObjectList: {listLength} items")
    
    if OSR_WINDOW is None:
        print("⚠️ No UI window found")
    else:
        print("✅ UI window exists")
        print(f"🔍 UI targetObjectsSet: {len(OSR_WINDOW.targetObjectsSet)} items")
        
        for obj in OSR_WINDOW.targetObjectsSet:
            print(f"  - {obj.nodeName()}")
    
    print("🔍 =============================================")

def forceSyncWithCore():
    """🔄 Force manual sync with core - for debugging"""
    global OSR_WINDOW
    
    if OSR_WINDOW is None:
        print("⚠️ No window instance to sync")
        return
    
    print("🔄 ===== FORCING MANUAL SYNC WITH CORE =====")
    OSR_WINDOW.syncWithCore()
    print("🔄 =========================================")

def forceCleanup():
    """🚨 Emergency cleanup function"""
    global OSR_WINDOW
    
    print("🚨 OnionSkinRenderer: Force cleanup initiated...")
    
    # Method 1: Try normal cleanup
    closeExistingWindow()
    
    # Method 2: Find any remaining windows by object name
    try:
        mayaMain = getMayaMainWindow()
        for child in mayaMain.findChildren(QtWidgets.QMainWindow):
            if hasattr(child, 'objectName') and 'onionSkin' in child.objectName().lower():
                print(f"🔍 Found orphaned window: {child}")
                try:
                    child.close()
                    child.deleteLater()
                except:
                    pass
    except:
        pass
    
    # Method 3: Clear global reference
    OSR_WINDOW = None
    
    # Method 4: Force garbage collection
    import gc
    gc.collect()
    
    print("✅ OnionSkinRenderer: Force cleanup completed")

# 🔄 Enhanced Core Management Functions
def resetCore():
    """🚨 Reset core state completely"""
    
    print("🔄 OnionSkinRenderer: Resetting core state...")
    
    if core.OSR_INSTANCE is not None:
        try:
            # Clear all onion objects and targets
            core.OSR_INSTANCE.clearTargetObjects()
            core.OSR_INSTANCE.clearAbsoluteTargetFrames()
            
            # Clear relative blend passes
            for onion in list(core.OSR_INSTANCE.relativeBlendPasses.keys()):
                core.OSR_INSTANCE.removeRelativeTargetFrame(onion)
            
            # Clear onion skin buffer
            core.OSR_INSTANCE.clearOnionSkinBuffer()
            
            print("✅ OnionSkinRenderer: Core state reset completed")
            
        except Exception as e:
            print(f"⚠️ OnionSkinRenderer: Core reset warning - {e}")
    else:
        print("ℹ️ OnionSkinRenderer: No core instance to reset")

# 🛠️ Debug and testing functions
def testObjectRestore():
    """🧪 Test function to verify object restoration"""
    print("🧪 ===== TESTING OBJECT RESTORATION =====")
    
    # Check current selection
    currentSel = pm.selected()
    print(f"🔍 Current Maya selection: {[obj.nodeName() for obj in currentSel]}")
    
    # Check core state
    debugCoreAndUI()
    
    # Try to add current selection to core
    if currentSel and core.OSR_INSTANCE:
        print("🔄 Adding current selection to core...")
        core.OSR_INSTANCE.addSelectedTargetObject()
        debugCoreAndUI()
    
    print("🧪 =====================================")

# 📋 Usage Examples and Documentation:
"""
🎯 **Usage Examples:**

# 🔄 Normal usage (auto-sync with core):
import onionSkinRenderer.controller as ctl
ctl.show()  # Will automatically sync UI with existing core state

# 🔍 Debug the sync issue:
ctl.debugCoreAndUI()     # See what's in core vs UI
ctl.forceSyncWithCore()  # Force manual sync

# 🚨 If you experience weird behavior:
ctl.resetCore()  # Reset core state completely
ctl.show()       # Then open fresh UI

# 🔍 Debug utilities:
print(ctl.getWindowState())  # Check window state
ctl.forceCleanup()          # Emergency cleanup

# 🚨 Nuclear option (if everything breaks):
ctl.forceCleanup()
ctl.resetCore()
ctl.show()

# 🔥 Force reset from within UI:
ctl.OSR_WINDOW.forceResetAndRestart()  # Reset core and refresh UI

# 🔧 Debugging workflow for object sync issues:
# 1. Add objects to onion skin in Maya
# 2. Check what's in core: ctl.debugCoreAndUI()
# 3. Reopen script: ctl.show()
# 4. If objects missing, debug again: ctl.debugCoreAndUI()
# 5. Force sync: ctl.forceSyncWithCore()

"""
