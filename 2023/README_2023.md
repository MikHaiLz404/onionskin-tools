# OnionSkinRenderer 2023 - Maya 2023 Compatible Version

<img src="../onionskin_renderer_icon_32.png" alt="OnionSkin Renderer" width="32"/> **Advanced 3D Onion Skinning for Maya 2023**

---

## 🎯 **Fixed for Maya 2023!**

### ✅ **PySide2/PySide6 Dual Compatibility**
- **Maya 2023**: Uses PySide2 (now properly supported!)
- **Maya 2024+**: Uses PySide6 (future-ready)
- **Automatic detection** - plugin automatically detects and uses correct PySide version
- **Enhanced error handling** with clear compatibility messages

### 🔧 **Critical Fixes Applied**
- ✅ **PySide Import Error FIXED** - No more "No module named 'PySide6'" error in Maya 2023
- ✅ **Qt Enum Compatibility** - Proper handling of Qt constants across versions
- ✅ **Signal Connection Updates** - Compatible signal syntax for both PySide versions
- ✅ **UI Element Compatibility** - All widgets work correctly in both environments

---

## 🚀 **Installation**

### **Quick Install (Recommended)**
1. Copy the `onionSkinRenderer` folder to your Maya 2023 scripts directory:
   ```
   Windows: C:\Users\[username]\Documents\maya\2023\scripts\
   Mac: /Users/[username]/Library/Preferences/Autodesk/maya/2023/scripts/
   Linux: /home/[username]/maya/2023/scripts/
   ```

2. In Maya Script Editor (Python tab):
   ```python
   import onionSkinRenderer.controller as ctl
   ctl.show()
   ```

3. Or run the installation test script:
   ```python
   exec(open(r"C:\path\to\install_test_maya2023.py").read())
   ```

---

## 🎨 **What You Can Do Now**

### **Perfect for Character Animation** 🏃‍♂️
- **Skinned Mesh Support**: See deformation through animation frames
- **Pose Comparison**: Compare character poses across time
- **Arc Visualization**: Track movement paths and arcs
- **Timing Analysis**: Perfect timing with visual frame overlays

### **Onion Skin Display Modes**
- **Shape Mode**: Clean silhouettes (recommended for characters)
- **Shaded Mode**: Full material display with transparency
- **Outline Mode**: Edge-based visualization

### **Smart Frame Management**
- **Relative Frames**: Show -2, -1, +1, +2 frames relative to current
- **Absolute Frames**: Pin specific frame numbers
- **Keyframe Mode**: Automatically target keyframe positions
- **Custom Opacity**: Individual frame transparency control

---

## 🛠️ **Maya 2023 Compatibility Notes**

### **System Requirements**
- ✅ **Maya 2023** or newer
- ✅ **Python 3.7+** (included with Maya 2023)
- ✅ **PySide2** (included with Maya 2023)
- ✅ **Viewport 2.0** enabled

### **Performance Optimized for Maya 2023**
- **VRAM Buffering**: Efficient memory usage
- **Auto-cleanup**: Smart buffer management
- **Camera Integration**: Works with Maya 2023 viewport

---

## 🎯 **Usage Examples**

### **Character Animation Workflow**
```python
# Launch OnionSkinRenderer
import onionSkinRenderer.controller as ctl
ctl.show()

# Basic setup:
# 1. Select your character rig
# 2. Click "Add Selected" 
# 3. Click "Toggle Renderer"
# 4. Activate relative frames with 'v' buttons
# 5. Animate and see onion skins!
```

### **Recommended Settings for Character Work**
- **Onion Skin Type**: Shape
- **Global Opacity**: 60-80%
- **Tint Type**: Relative Random
- **Draw Behind**: Enabled
- **Buffer Size**: 100-200 frames

---

## 🐛 **Troubleshooting Maya 2023**

### **Fixed Issues ✅**
- ❌ ~~"No module named 'PySide6'"~~ → ✅ **FIXED**: Auto-detects PySide2 in Maya 2023
- ❌ ~~Qt enum errors~~ → ✅ **FIXED**: Compatible Qt constants
- ❌ ~~UI layout issues~~ → ✅ **FIXED**: Proper widget handling

### **Common Setup Issues**
| Issue | Solution |
|-------|----------|
| "Module not found" | Copy folder to correct scripts directory |
| UI doesn't appear | Run `ctl.show()` command |
| No onion skins visible | Click "Toggle Renderer" and activate frames |
| Poor performance | Reduce buffer size in preferences |

---

## 💡 **Pro Tips for Maya 2023**

### **Best Practices**
1. **Use Shape Mode** for character animation
2. **Enable Keyframe Mode** for pose-to-pose work
3. **Set Draw Behind** for better depth perception
4. **Adjust Global Opacity** based on scene complexity
5. **Use Relative Step=2** for cleaner display

### **Memory Management**
- Start with 50-100 frame buffer for testing
- Increase buffer size based on available VRAM
- Enable auto-clear for camera movements
- Clear buffer manually when switching scenes

---

## 🎭 **Perfect for Maya 2023 Animation**

### **Character Animation**
- ✅ Rig-friendly onion skinning
- ✅ Deformation visualization
- ✅ Pose flow analysis
- ✅ Timing refinement

### **Motion Graphics**
- ✅ Object transformation paths
- ✅ Camera movement visualization
- ✅ Mechanical animation timing
- ✅ Layout and blocking

---

## 📞 **Support**

### **If You Encounter Issues**
1. **Check Maya Version**: Ensure you're using Maya 2023+
2. **Verify Installation**: Confirm files are in scripts directory
3. **Run Test Script**: Use `install_test_maya2023.py` for diagnostics
4. **Check Script Editor**: Look for detailed error messages

### **Performance Tips**
- **Reduce Buffer Size** if experiencing slowdowns
- **Use Shape Mode** instead of Shaded for better performance
- **Enable Auto Clear Buffer** for camera movement workflows
- **Restart Maya** if you encounter persistent issues

---

## 🎉 **Version History**

### **2023.1** (Current - Maya 2023 Compatible)
- ✅ **PySide2/PySide6 dual compatibility**
- ✅ **Maya 2023 native support**
- ✅ **Enhanced error handling**
- ✅ **Automatic version detection**
- ✅ **All original features preserved**

---

*เอมิลี่แก้ไขให้แล้วนะคะ~ Now perfectly compatible with Maya 2023! 🎨✨*

**Ready to enhance your animation workflow in Maya 2023!** 🧅