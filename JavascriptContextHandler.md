Project will move to github. Find this wiki page at the new address: https://github.com/cztomczak/cefpython/wiki/JavascriptContextHandler


---


# JavascriptContextHandler callbacks #

Implement this interface to handle javascript exceptions globally.

For an example of how to implement handler see [cefpython](cefpython.md).CreateBrowser(). For a list of all handler interfaces see [API > Client handlers](API#Client_handlers.md).

void **OnContextCreated**([Browser](Browser.md) `browser`, [Frame](Frame.md) `frame`)

> In CEF 1 called immediately after the V8 context for a frame has been created.

> In CEF 3 called shortly after (process message delay) the V8 context for a frame has been created.

void **OnContextReleased**([Browser](Browser.md) `browser`, [Frame](Frame.md) `frame`)

> In CEF 1 called immediately before the V8 context for a frame is released.

> In CEF 3 called shortly after (process message delay) the V8 context for a frame was released.

> Due to multi-process architecture in CEF 3, this function won't
> get called for the main frame in main browser. To send a message
> from the renderer process a parent browser is used. If this is
> the main frame then this would mean that the browser is being
> destroyed, thus we can't send a process message using this browser.
> There is no guarantee that this will get called for frames in the
> main browser, if the browser is destroyed shortly after the frames
> were released.

void **OnUncaughtException**([Browser](Browser.md) `browser`, [Frame](Frame.md) `frame`, dict `exception`, list `stackTrace`)

> Not yet implemented in CEF Python 3.

> Called for global uncaught exceptions. Execution of this callback is disabled by default. To enable set ApplicationSettings.uncaught\_exception\_stack\_size > 0.

> `exception` is a dictionary with following keys: lineNumber, message, scriptResourceName, sourceLine.

> `stackTrace` is in the same format as returned by [cefpython](cefpython.md).GetJavascriptStackTrace(), see description of that function for more details. To get a string call [cefpython](cefpython.md).FormatJavascriptStackTrace().