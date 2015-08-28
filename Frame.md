Project will move to github. Find this wiki page at the new address: https://github.com/cztomczak/cefpython/wiki/Frame


---



# `Frame` object #



## Methods ##

### Copy() (void) ###

> Execute copy in this frame.

### Cut() (void) ###

> Execute cut in this frame.

### Delete() (void) ###

> Execute delete in this frame.

### ExecuteFunction(string `funcName`, `[`mixed param `[`, mixed `param` `[, ..]]]`) (void) ###

> Call javascript function asynchronously. This can also call object's methods, just pass "object.method" as `funcName`. Any valid javascript syntax is allowed as `funcName`, you could even pass an anonymous function here.

> For a list of allowed types for `mixed` see [JavascriptBindings](JavascriptBindings.md).IsValueAllowed() (except function, method and instance).

> Passing a python function here is not allowed, it is only possible through JavascriptCallback object.

### ExecuteJavascript(string `jsCode`, string `scriptURL`=None, int `startLine`=None) (void) ###

> Execute a string of JavaScript code in this frame. The `sciptURL` parameter is the URL where the script in question can be found, if any. The renderer may request this URL to show the developer the source of the error.  The `startLine` parameter is the base line number to use for error reporting.

> This function executes asynchronously so there is no way to get the returned value.

> Calling javascript from native code synchronously is not possible in CEF 3. It is also not possible doing it synchronously the other way around ie. js->native.

### GetBrowser() (Browser) ###

> Returns the [browser](Browser.md) that this frame belongs to.

### GetParent() (Frame) ###

> Returns the parent of this [frame](Frame.md) or None if this is the main (top-level) frame.

### GetIdentifier() (int) ###

> Frame identifiers are unique per render process, they are not
> globally unique.

### GetBrowserIdentifier() (int) ###

> Returns the globally unique identifier for the browser hosting this frame.

### GetName() (string) ###

> Returns the name for this frame. If the frame has an assigned name (for example, set via the iframe "name" attribute) then that value will be returned. Otherwise a unique name will be constructed based on the frame parent hierarchy. The main (top-level) frame will always have an empty name value.

### GetParent() (Frame) ###

> Not yet implemented. Returns the parent of this frame or None if this is the main (top-level) frame. This method should only be called on the UI thread.

### GetProperty(string name) (mixed) ###

> Get property of the `window` object in javascript.

> For a list of allowed types for `mixed` see [JavascriptBindings](JavascriptBindings.md).IsValueAllowed() (except function, method and instance).

> If you try to get some javascript native property that its value cannot be converted to the python types above, you will get an error.

### GetSource(`StringVisitor` visitor) (void) ###

> CEF 3. Retrieve this frame's HTML source as a string sent to the specified
> visitor. See [StringVisitor](StringVisitor.md) interface.

### GetText(`StringVisitor` visitor) (void) ###

> CEF 3. Retrieve this frame's display text as a string sent to the specified
> visitor. See [StringVisitor](StringVisitor.md) interface.

### GetSource() (string) ###

> CEF 1. Returns this frame's HTML source as a string. This method should only be called on the UI thread.

### GetText() (string) ###

> CEF 1. Returns this frame's display text as a string. This method should only be called on the UI thread.

### GetUrl() (string) ###

> Returns the url currently loaded in this frame.

### IsFocused() (bool) ###

> Returns true if this is the focused frame. This method should only be called on the UI thread.

### IsMain() (bool) ###

> Returns true if this is the main (top-level) frame.

### IsValid() (bool) ###

> Available only in CEF 3.

> True if this object is currently attached to a valid frame.

### LoadRequest(Request `request`) (void) ###

> Not yet ported.

> Load the request represented by the |request| object. This is similar to `LoadUrl()`, but gives you  possibility to set custom headears, make a POST request and set the post data. See the [Request](Request.md) class.

### LoadStream(StreamReader `stream`, string `url`) (void) ###

> Not yet ported.

> Load the contents of |stream| with the optional dummy target |url|.

### LoadString(string `value`, string `url`) (void) ###

> Load the contents of |value| with the specified dummy |url|. |url|
> should have a standard scheme (for example, http scheme) or behaviors like
> link clicks and web security restrictions may not behave as expected.

> In CEF 3 `LoadString()` can be called only after the Renderer process has been created.

### LoadUrl(string `url`) (void) ###

> Load the specified |url|.

### Paste() (void) ###

> Execute paste in this frame.

### Print() (void) ###

> Available only in CEF 1. In CEF 3 use [Browser](Browser.md).`Print()`.

> Execute printing in the this frame.  The user will be prompted with the print dialog appropriate to the operating system.

### Redo() (void) ###

> Execute redo in this frame.

### SelectAll() (void) ###

> Execute select all in this frame.

### SetProperty(string name, mixed value) (void) ###

> Set property of the `window` object in javascript. You can also set properties before browser is created by using [JavascriptBindings](JavascriptBindings.md).SetProperty().

> For a list of allowed types for `mixed` see [JavascriptBindings](JavascriptBindings.md).IsValueAllowed() (except instance).

### Undo() (void) ###

> Execute undo in this frame.

### ViewSource() (void) ###

> Save this frame's HTML source to a temporary file and open it in the default text viewing application.

### VisitDom(DomVisitor `visitor`) (void) ###

> Not yet ported. CEF DOM handling is prone to memory leaks, thus this function most probably won't be ported. It is recommended to the DOM management through javascript and communicate with the native code through [javascript bindings](JavascriptBindings.md).

> Visit the DOM document.

