Project will move to github. Find this wiki page at the new address: https://github.com/cztomczak/cefpython/wiki/DragHandler


---



# DragHandler callbacks #

Implement this interface to handle events related to dragging. The
methods of this class will be called on the UI thread.

For an example of how to implement a handler see [cefpython](cefpython.md).`CreateBrowser()`. For a list of all handler interfaces
see [API > Client handlers](API#Client_handlers.md).

The `DragHandler` tests can be found in the wxpython.py script.

## CEF 1 ##

bool **OnDragStart**([Browser](Browser.md) browser, [DragData](DragData.md) dragData, `DragOperation` mask)

> Called when the browser window initiates a drag event. |dragData|
> contains the drag event data and |mask| represents the type of drag
> operation. Return false for default drag handling behavior or true to
> cancel the drag event.

> The `DragOperation` mask can be checked against `cefpython.Drag.Operation`
> dictionary that consists of following keys:

> None<br>
<blockquote>Copy<br>
Link<br>
Generic<br>
Private<br>
Move<br>
Delete<br>
Every<br></blockquote>

bool <b>OnDragEnter</b>(<a href='Browser.md'>Browser</a> browser, <a href='DragData.md'>DragData</a> dragData, <code>DragOperation</code> mask)<br>
<br>
<blockquote>Called when an external drag event enters the browser window. |dragData|<br>
contains the drag event data and |mask| represents the type of drag<br>
operation. Return false for default drag handling behavior or true to<br>
cancel the drag event.</blockquote>

<blockquote>For the <code>DragOperation</code> mask values see the <code>OnDragStart()</code> description.