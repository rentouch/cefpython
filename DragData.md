Project will move to github. Find this wiki page at the new address: https://github.com/cztomczak/cefpython/wiki/DragData


---


# DragData object #

Object used to represent drag data. The methods of this class
may be called on any thread.

See [DragHandler](DragHandler.md).`OnDragStart()` and [DragHandler](DragHandler.md).`OnDragEnter`.

## CEF 1 ##

bool **IsLink**()

> Returns true if the drag data is a link.

bool **IsFragment**()

> Returns true if the drag data is a text or html fragment.

bool **IsFile**()

> Returns true if the drag data is a file.

str **GetLinkUrl**()

> Return the link url that is being dragged.

str **GetLinkTitle**()

> Return the metadata, if any, associated with the link being dragged.

str **GetLinkMetadata**()

> Return the metadata, if any, associated with the link being dragged.

str **GetFragmentText**()

> Return the plain text fragment that is being dragged.

str **GetFragmentHtml**()

> Return the text/html fragment that is being dragged.

str **GetFragmentBaseUrl**()

> Return the base url that the fragment came from. This value is
> used for resolving relative urls and may be empty.

str **GetFile**()

> Return the file being dragged out of the browser window.

list **GetFiles**()

> Retrieve the list of files that are being dragged into the browser
> window.