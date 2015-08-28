Project will move to github. Find this wiki page at the new address: https://github.com/cztomczak/cefpython/wiki/cefpython


---


# cefpython module #

Table of contents:


## Functions ##

### CreateBrowser() (bool) ###

> This function was not yet ported to CEF Python.

> Create browser asynchronously. The actual window will be created on the UI thread. This method call will not block.

### CreateBrowserSync(WindowInfo `windowInfo`, dict [browserSettings](BrowserSettings.md), string `navigateUrl`, void `requestContext`) ([Browser](Browser.md)) ###

> This function should only be called on the UI thread.

> The `requestContext` parameter is not yet implemented.

> You must first create a window and initialize `windowInfo` by calling
> WindowInfo.`SetAsChild`.

> After the call to CreateBrowserSync() the page is not yet loaded, if you want your next lines of code to do some stuff on the webpage you will have to implement [LoadHandler](LoadHandler.md).OnLoadEnd() callback, see example below:

```
	def OnLoadEnd(browser, frame, httpCode):
		if frame == browser.GetMainFrame():
			print "Finished loading main frame: %s (http code = %d)" % (frame.GetUrl(), httpCode)

	browser = cefpython.CreateBrowserSync(windowInfo, settings, url)
        browser.SetClientCallback("OnLoadEnd", OnLoadEnd)
```

### FormatJavascriptStackTrace(list stackTrace) (string) ###

> Returns stack trace as a nicely formatted string. Call GetJavascriptStackTrace() to get stack trace as a list.

### GetAppSetting(string `key`) (object) ###

> Returns ApplicationSettings option that was passed to `Initialize()`. Returns None if key is not found.

### GetBrowserByWindowHandle(long `windowHandle`) ###

> Get browser by outer or inner window handle. An outer window handle is the one that was passed to `CreateBrowserSync()`. An inner window handle is a CEF internal window handle.

### GetCommandLineSwitch(string `key`) (object) ###

> Returns the CommandLineSwitches switch that was passed to `Initialize()`. Returns None if key is not found.

### GetGlobalClientCallback(string `name`) (object) ###

> Returns a global client callback that was set using `SetGlobalClientCallback()`. Returns None if callback was not set.

### GetJavascriptStackTrace(int `frameLimit`=100) (list) ###

> Returns the stack trace for the currently active context. |frameLimit| is the maximum number of frames that will be captured. This function may be called only on the UI thread.

> Frames in the returned list are of type dictionary with following keys:<br>
<blockquote>- script<br>
- scriptOrSourceUrl (the name of the script or the sourceUrl value if the script name is undefined and its source ends with "//@ sourceURL=...".)<br>
- function<br>
- line<br>
- column<br>
- isEval (whether function was compiled using eval())<br>
- isConstructor (whether function was called as a constructor via "new")</blockquote>

<h3>GetModuleDirectory() (string)</h3>

<blockquote>Get the cefpython module directory. This method is useful to get full path to CEF binaries. This is required when setting options like ApplicationSettings.browser_subprocess_path / resources_dir_path / locales_dir_path.</blockquote>

<h3>Initialize(dict <a href='ApplicationSettings.md'>applicationSettings</a>=None, dict <a href='CommandLineSwitches.md'>commandLineSwitches</a>=None) (bool)</h3>

<blockquote>This function should be called on the main application thread (UI thread) to initialize CEF when the application is started.</blockquote>

<blockquote>A call to <code>Initialize()</code> must have a corresponding call to <code>Shutdown()</code>, otherwise when application closes, the process might freeze (experienced on Windows XP).</blockquote>

<blockquote>The commandLineSwitches param is a dictionary with switch name as key. The switch name should not containt the "-" or "--" prefix. Switch value may be an empty string, if switch doesn't require a value. These switches are set for the main process and all subprocesses. With switches you can set various options in Chromium. For example a proxy can be set with the "proxy-server" switch. The default of using IE proxy settings can be disabld with the "no-proxy-server" switch. To enable Enable media (webrtc/audio) streaming set the "enable-media-stream" switch. See the <a href='CommandLineSwitches.md'>CommandLineSwitches</a> wiki page for a list of all available switches that can be set.</blockquote>

<blockquote>When debbugging is On, the whole command line string will be displayed in console, with both CEF switches set internally, and the ones appended by cefpython. On Linux you will also see in console the command line string for subprocesses. On Windows, command line strings for subprocesses won't be seen in console, you can view them by opening the debug.log file. Example command line strings from debug logs, for the main process and the renderer process:</blockquote>

<pre><code># Main process<br>
python --browser-subprocess-path="C:\cefpython\cefpython\cef3\windows\binaries/subprocess"<br>
--lang=en-US --log-file="C:\cefpython\cefpython\cef3\windows\binaries\debug.log"<br>
--log-severity=info --enable-release-dcheck --no-sandbox wxpython.py<br>
<br>
# Renderer process<br>
"C:\cefpython\cefpython\cef3\windows\binaries/subprocess" --type=renderer --no-sandbox<br>
--lang=en-US --lang=en-US --log-file="C:\cefpython\cefpython\cef3\windows\binaries\debug.log"<br>
--log-severity=info --enable-release-dcheck --channel="4152.0.209609692\1183564454"<br>
/prefetch:673131151<br>
</code></pre>

<h3>IsThread(int threadID) (bool)</h3>

<blockquote>Returns true if called on the specified thread.</blockquote>

<blockquote>CEF maintains multiple internal threads that are used for handling different types of tasks. The UI thread creates the browser window and is used for all interaction with the webkit rendering engine and V8 Javascript engine (The UI thread will be the same as the main application thread if CefInitialize() is called with a <a href='ApplicationSettings.md'>ApplicationSettings</a>.multi_threaded_message_loop value of false.) The IO thread is used for handling schema and network requests. The FILE thread is used for the application cache and other miscellaneous activities.</blockquote>

List of threads in the Browser process. These are constants defined in the cefpython module:<br>
<br>
<ul><li>TID_UI: The main thread in the browser. This will be the same as the main application thread if cefpython.Initialize() is called with a ApplicationSettings.multi_threaded_message_loop value of false.<br>
</li><li>TID_DB: Used to interact with the database.<br>
</li><li>TID_FILE: Used to interact with the file system.<br>
</li><li>TID_FILE_USER_BLOCKING: Used for file system operations that block user interactions. Responsiveness of this thread affects users.<br>
</li><li>TID_PROCESS_LAUNCHER: Used to launch and terminate browser processes.<br>
</li><li>TID_CACHE: Used to handle slow HTTP cache operations.<br>
</li><li>TID_IO: Used to process IPC and network messages.</li></ul>

List of threads in the Renderer process:<br>
<ul><li>TID_RENDERER: The main thread in the renderer. Used for all webkit and V8 interaction.</li></ul>

<h3>IsKeyModifier(int key, int modifiers) (bool)</h3>

<blockquote>For use with <a href='KeyboardHandler.md'>KeyboardHandler</a> to check whether ALT, SHIFT or CTRL are pressed.</blockquote>

<h3>MessageLoop() (void)</h3>

<blockquote>Run the CEF message loop. Use this function instead of an application-<br>
provided message loop to get the best balance between performance and CPU usage. This function should only be called on the main application thread (UI thread) and only if cefpython.Initialize() is called with a<br>
<a href='ApplicationSettings.md'>ApplicationSettings</a>.multi_threaded_message_loop value of false. This function will block until a quit message is received by the system.</blockquote>

<h3>MessageLoopWork() (void)</h3>

<blockquote>Perform a single iteration of CEF message loop processing. This function is used to integrate the CEF message loop into an existing application message loop. Care must be taken to balance performance against excessive CPU usage. This function should only be called on the main application thread (UI thread) and only if cefpython.Initialize() is called with a <a href='ApplicationSettings.md'>ApplicationSettings</a>.multi_threaded_message_loop value of false. This function will not block.</blockquote>

<blockquote>Alternatively you could create a periodic timer (with 10 ms interval) that calls cefpython.MessageLoopWork().</blockquote>

<blockquote>CefDoMessageLoopWork is not tested on OS X and there are known issues - according to  <a href='http://www.magpcss.org/ceforum/viewtopic.php?p=27124#p27124'>this comment by Marshall</a>.</blockquote>

<h3>PostTask(int threadId, object func [,args..]) (void)</h3>

<blockquote>Post a task for execution on the thread associated with this task runner. Execution will occur asynchronously. Only Browser process threads are allowed, see <code>IsThread()</code> for a list of available threads and their descriptions.</blockquote>

<blockquote>An example usage is in the wxpython.py example on Windows, in implementation of LifespanHandler.<code>OnBeforePopup</code>.</blockquote>

<h3>QuitMessageLoop() (void)</h3>

<blockquote>Quit the CEF message loop that was started by calling cefpython.MessageLoop(). This function should only be called on the main application thread (UI thread) and only if cefpython.MessageLoop() was used.</blockquote>

<h3>SetGlobalClientCallback(string name, function callback) (void)</h3>

<blockquote>Current CEF Python implementation is limited in handling callbacks that occur during browser creation, in such cases a callback set with Browser.<code>SetClientCallback()</code> or Browser.<code>SetClientHandler()</code> won't work, as this methods can be called only after browser was created. An example of such callback is LifespanHandler.<code>OnAfterCreated</code>.</blockquote>

<blockquote>Some client callbacks are not associated with any browser. In such case use this function<br>
instead of the <a href='Browser.md'>Browser</a>.<code>SetClientCallback()</code> / <code>SetClientHandler()</code> methods. An example of such callback is <a href='RequestHandler.md'>RequestHandler</a>.<code>OnCertificateError</code>.</blockquote>

<blockquote>Example of using SetGlobalClientCallback is provided in the wxpython.py example.</blockquote>

<h3>SetOsModalLoop(bool modalLoop) (void)</h3>

<blockquote>Set to true before calling Windows APIs like <code>TrackPopupMenu</code> that enter a<br>
modal message loop. Set to false after exiting the modal message loop.</blockquote>

<h3>Shutdown() (void)</h3>

<blockquote>This function should be called on the main application thread (UI thread) to shut down CEF before the application exits.</blockquote>

<blockquote>You must call this function so that CEF shuts down cleanly. Remember also to delete all CEF browsers references for the browsers to shut down cleanly. For an example see wxpython.py > <code>MainFrame.OnClose()</code>.