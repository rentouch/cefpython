Project will move to github. Find this wiki page at the new address: https://github.com/cztomczak/cefpython/wiki/PaintBuffer


---


# PaintBuffer object #

This object is related to: [Browser](Browser.md).GetImage() and [RenderHandler](RenderHandler.md).OnPaint().

long **GetIntPointer**()

> Get int pointer to the `void*` buffer.

object **GetString**(string `mode`="bgra", string `origin`="top-left")

> Converts the `void*` buffer to string. In Py2 returns 'str' type, in Py3 returns 'bytes' type.

> `origin` may be one of: "top-left", "bottom-left".

> `mode` may be one of: "bgra", "rgba".