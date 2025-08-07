"""
OnionSkinRenderer 2023 - Installation and Test Script
For Maya 2023 (PySide2) and Maya 2024+ (PySide6) compatibility

เอมิลี่จัดให้เลยนะคะ~ Fixed for Maya 2023 PySide2 compatibility!

Installation Instructions:
1. Copy the onionSkinRenderer folder to your Maya scripts directory:
   Windows: C:\\Users\\[username]\\Documents\\maya\\2023\\scripts\\
   Mac: /Users/[UserName]/Library/Preferences/Autodesk/maya/2023/scripts/
   Linux: /home/[username]/maya/2023/scripts/

2. Run this script in Maya's Script Editor (Python tab)
"""

import sys
import os
import maya.cmds as cmds

def check_maya_version():
    """Check Maya version and PySide compatibility"""
    maya_version = cmds.about(version=True)
    print(f"🎯 Maya Version: {maya_version}")
    
    # Check PySide availability
    pyside_version = None
    try:
        from PySide6 import QtWidgets
        pyside_version = "PySide6"
        print("✅ PySide6 detected (Maya 2024+)")
    except ImportError:
        try:
            from PySide2 import QtWidgets
            pyside_version = "PySide2"
            print("✅ PySide2 detected (Maya 2023)")
        except ImportError:
            print("❌ No PySide version found!")
            return maya_version, None
    
    return maya_version, pyside_version

def install_onion_skin_renderer():
    """Install and test OnionSkinRenderer"""
    print("🧅 Installing OnionSkinRenderer for Maya 2023...")
    
    # Check prerequisites
    maya_version, pyside_version = check_maya_version()
    if not pyside_version:
        print("❌ PySide not available - required for Maya 2023+")
        return False
    
    try:
        # Try to import the module
        import onionSkinRenderer.controller as ctl
        
        # Show the UI
        ctl.show(develop=False, dockable=False)
        
        print("✅ OnionSkinRenderer installed successfully!")
        print(f"📱 UI window should now be visible (using {pyside_version})")
        print()
        print("🎨 Quick Start Guide:")
        print("1. Select objects you want to onion skin")
        print("2. Click 'Add Selected' in Onion Skin Objects")
        print("3. Click 'Toggle Renderer' button")
        print("4. Use the 'v' buttons to activate relative frames")
        print("5. Scrub timeline to see onion skins!")
        print()
        print("💡 Tips for Maya 2023:")
        print("- Use 'Shape' mode for best skinned mesh visibility")
        print("- Adjust Global Opacity for better blend")
        print("- Try different tint types for visual variety")
        print("- Works great with rigged characters!")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print()
        print("🔧 Troubleshooting:")
        print("1. Make sure onionSkinRenderer folder is in your scripts directory")
        print("2. Check that all files are present in the folder")
        print("3. Restart Maya after copying files")
        print("4. Verify Maya 2023+ is being used")
        return False
    
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def create_test_scene():
    """Create a simple test scene for onion skinning"""
    print("🎬 Creating test scene...")
    
    # Clear scene
    cmds.file(new=True, force=True)
    
    # Create a simple character setup
    cube = cmds.polyCube(name="OnionTestCube")[0]
    cmds.move(0, 1, 0, cube)
    
    # Add some keyframes
    cmds.setKeyframe(cube + ".translateX", time=1, value=-3)
    cmds.setKeyframe(cube + ".translateX", time=10, value=0)
    cmds.setKeyframe(cube + ".translateX", time=20, value=3)
    cmds.setKeyframe(cube + ".translateX", time=30, value=0)
    
    cmds.setKeyframe(cube + ".rotateY", time=1, value=0)
    cmds.setKeyframe(cube + ".rotateY", time=20, value=180)
    cmds.setKeyframe(cube + ".rotateY", time=30, value=360)
    
    # Set frame range
    cmds.playbackOptions(minTime=1, maxTime=30)
    cmds.currentTime(15)
    
    # Select the cube
    cmds.select(cube)
    
    print(f"✅ Test scene created with animated cube: {cube}")
    print("🎯 Cube is selected and ready for onion skinning!")
    print("📽️ Timeline: 1-30 frames with translation and rotation animation")

if __name__ == "__main__":
    print("=" * 60)
    print("🧅 OnionSkinRenderer 2023 - Installation Script")
    print("   Maya 2023 (PySide2) & Maya 2024+ (PySide6) Compatible")
    print("=" * 60)
    print()
    
    # Install
    success = install_onion_skin_renderer()
    
    if success:
        print()
        # Ask if user wants test scene
        result = cmds.confirmDialog(
            title="OnionSkinRenderer Test Scene",
            message="Would you like to create a test scene with animated cube?",
            button=['Yes', 'No'],
            defaultButton='Yes',
            cancelButton='No',
            dismissString='No'
        )
        
        if result == 'Yes':
            create_test_scene()
    
    print()
    print("=" * 60)
    print("🎨 Enjoy your enhanced animation workflow!")
    print("   Fixed for Maya 2023 PySide2 compatibility! ✨")
    print("=" * 60)