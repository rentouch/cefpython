Project will move to github. Find this wiki page at the new address: https://github.com/cztomczak/cefpython/wiki/WindowInfo


---


# WindowInfo class #

This class is passed to functions: [cefpython](cefpython.md).CreateBrowserSync(), LifespanHandler.OnBeforePopup().

To instantiate this class call: [cefpython](cefpython.md).WindowInfo().

void **SetAsChild**(int `parentWindowHandle`, list `windowRect`=None)

> `windowRect` param is optional on Windows. On Linux & Mac it is required. Example value: [left, top, right, bottom].

> This is the method you want to call in most cases.

void **SetAsPopup**(int `parentWindowHandle`, string `windowName`)

> Available only on Windows.

void **SetAsOffscreen**(int `parentWindowHandle`)

> Available in CEF 1 only on Windows & Mac.

> Call this method to disable window rendering and to use RenderHandler. See the [Panda3D](Panda3D.md) / [Kivy](Kivy.md) examples.

> You can pass 0 to `parentWindowHandle`, but then some things like context menus and plugins may not display correctly.

void **SetTransparentPainting**(bool `transparentPainting`)

> This method is intended for use with off-screen rendering. (not sure if it works with windowed rendering)