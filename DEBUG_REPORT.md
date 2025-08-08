# OnionSkinRenderer 2023: Debug Report and Improvements

This document outlines the bugs fixed and improvements made to the OnionSkinRenderer for the 2023 version.

## Summary

The codebase for the Maya 2023 compatibility update is functional and includes significant improvements, particularly in state management and PySide version handling. The debugging process focused on improving code quality, fixing latent bugs, and increasing maintainability.

---

##  Bugs Fixed

### 1. Critical: Incorrect Widget Parenting

*   **File Affected**: `onionSkinRenderer/controller.py`
*   **Issue**: The `OnionListFrame` and `TargetObjectListWidget` classes incorrectly used `getMayaMainWindow()` as their default parent. This is a bad practice that can lead to memory leaks, incorrect UI behavior, and potential crashes. Child widgets should always be parented to the window or layout that contains them.
*   **Fix**: The default parent was removed from the `__init__` method signature. The parent is now correctly passed during instantiation within the `OSRController`.

### 2. Readability: Magic Number in Callback

*   **File Affected**: `onionSkinRenderer/core.py`
*   **Issue**: The `cameraMovedCB` function used the magic number `2056` to check the message type from the callback. This makes the code difficult to understand.
*   **Fix**: Replaced `2056` with the named constant `om.MNodeMessage.kAttributeSet`, making the code self-documenting.

### 3. Process: Fragile UI File Manually Edited

*   **File Affected**: `onionSkinRenderer/ui_window.py`
*   **Issue**: The auto-generated UI file had been manually edited to include PySide2/PySide6 compatibility code. This is a fragile workflow, as regenerating the UI from the `.ui` file would delete these critical changes.
*   **Fix**: Added a prominent warning header to `ui_window.py` to prevent developers from accidentally overwriting the manual edits. The long-term solution is to automate this process.

---

## Code Improvements

### 1. Refactoring for Clarity in `core.py`

*   **File Affected**: `onionSkinRenderer/core.py`
*   **Change**: The `setup()` method in `ViewRenderOverride` was very long and handled many tasks. It has been refactored into smaller, more focused helper methods:
    *   `_update_render_targets()`: Handles resizing of render targets.
    *   `_setup_relative_blend_passes()`: Configures the blending for relative frames.
    *   `_setup_absolute_blend_passes()`: Configures the blending for absolute frames.
*   **Benefit**: This improves readability and makes the core rendering logic easier to maintain and debug.

### 2. Refactoring for Maintainability in `controller.py`

*   **File Affected**: `onionSkinRenderer/controller.py`
*   **Change**: The `OSRController` class was overly large. The settings management logic has been extracted into a new, dedicated `SettingsManager` class.
*   **Benefit**: This follows the Single Responsibility Principle, making the controller class smaller and more focused on UI logic. The `SettingsManager` can be easily tested and extended independently.

### 3. API Consistency (PyMel vs. OpenMaya)

*   **File Affected**: `onionSkinRenderer/core.py`
*   **Investigation**: An investigation was made into replacing `pymel.core` calls (specifically `pm.findKeyframe`) with `maya.api.OpenMaya` equivalents to improve performance.
*   **Decision**: The change was *not* made. The PyMel function `pm.findKeyframe(timeSlider=True)` has specific behavior (querying global keys from the time slider) that is not easily replicated with `MAnimUtil` without risking a change in functionality (e.g., making it selection-dependent).
*   **Benefit**: By avoiding a risky change, the tool's stability is preserved. This is noted as an area for future optimization, but the current implementation is correct and readable.

### 4. Documentation of Disabled Feature

*   **File Affected**: `onionSkinRenderer/controller.py`
*   **Change**: The `mayaDetectionTimer` feature, which was disabled due to bugs, has been thoroughly documented.
*   **Benefit**: Future developers will now understand why this feature is disabled and will have a clear starting point for how to correctly re-implement it, preventing "window jumping" issues.

---

This concludes the debugging and improvement pass on the codebase. The tool is now more robust, readable, and easier to maintain.
