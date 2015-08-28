Project will move to github. Find this wiki page at the new address: https://github.com/cztomczak/cefpython/wiki/WebRequest


---


# WebRequest class #

## CEF 3 ##

Class used to make a URL request. URL requests are not associated with a
browser instance so no client handler callbacks will be executed. URL requests
can be created on any valid CEF thread in either the browser or render
process. Once created the methods of the URL request object must be accessed
on the same thread that created it.

The `WebRequest` example can be found in the `wxpython-response.py` script on Linux.

static [WebRequest](WebRequest.md) **Create**([Request](Request.md) request, [WebRequestClient](WebRequestClient.md) handler)

> You cannot instantiate [WebRequest](WebRequest.md) class directly, use this static
> method instead by calling `cefpython.WebRequest.Create()`.

> The first parameter is a [Request](Request.md) object that needs to be created
> by calling `cefpython.Request.CreateRequest()`.

> The [WebRequestClient](WebRequestClient.md) handler is a python class that implements
> the [WebRequestClient](WebRequestClient.md) callbacks.

> You must keep a strong reference to the [WebRequest](WebRequest.md) object
> during the request, otherwise it gets destroyed and
> the [WebRequestClient](WebRequestClient.md) callbacks won't get called.

[Request](Request.md) **GetRequest**()

> Returns the request object used to create this URL request. The returned
> object is read-only and should not be modified.

`RequestStatus` **GetRequestStatus**()

> Returns the request status. `RequestStatus` can be one of:

> `cefpython.WebRequest.Status["Unknown"]` - Unknown status.<br>
<blockquote><code>cefpython.WebRequest.Status["Success"]</code> - Request succeeded.<br>
<code>cefpython.WebRequest.Status["Pending"]</code> - An IO request is pending, and the caller will be informed when it is completed.<br>
<code>cefpython.WebRequest.Status["Canceled"]</code> - Request was canceled programatically.<br>
<code>cefpython.WebRequest.Status["Failed"]</code> - Request failed for some reason.<br></blockquote>

<a href='NetworkError.md'>NetworkError</a> <b>GetRequestError</b>()<br>
<br>
<blockquote>Returns the request error if status is "Canceled" or "Failed", or 0<br>
otherwise.</blockquote>

<a href='Response.md'>Response</a> <b>GetResponse</b>()<br>
<br>
<blockquote>Returns the response, or None if no response information is available.<br>
Response information will only be available after the upload has completed.<br>
The returned object is read-only and should not be modified.</blockquote>

void <b>Cancel</b>()<br>
<br>
<blockquote>Cancel the request.</blockquote>


<h2>CEF 1</h2>

Class used to make a web url request. Web url requests are not<br>
associated with a browser instance so no Client Handler callbacks<br>
will be executed. The methods of this class may be called on<br>
any thread.<br>
<br>
The <code>WebRequest</code> test can be found in the wxpython.py script.<br>
<br>
static <a href='WebRequest.md'>WebRequest</a> <b>CreateWebRequest</b>(<a href='Request.md'>Request</a> request, <a href='WebRequestClient.md'>WebRequestClient</a> handler)<br>
<br>
<blockquote>You cannot instantiate <a href='WebRequest.md'>WebRequest</a> class directly, use this static<br>
method instead by calling <code>cefpython.WebRequest.CreateWebRequest()</code>.</blockquote>

<blockquote>The first parameter is a <a href='Request.md'>Request</a> object that needs to be created<br>
by calling <code>cefpython.Request.CreateRequest()</code>.</blockquote>

<blockquote>The <a href='WebRequestClient.md'>WebRequestClient</a> handler is a python class that implements<br>
one/all/none of the <a href='WebRequestClient.md'>WebRequestClient</a> callbacks.</blockquote>

<blockquote>You must keep a strong reference to the <a href='WebRequest.md'>WebRequest</a> object<br>
during the request, otherwise it gets destroyed and<br>
the <a href='WebRequestClient.md'>WebRequestClient</a> callbacks won't be called.</blockquote>

void <b>Cancel</b>()<br>
<br>
<blockquote>Cancels the request.</blockquote>

<code>RequestState</code> <b>GetState</b>()<br>
<br>
<blockquote>Returns the current ready state of the request.</blockquote>

<blockquote><code>RequestState</code> is one of:</blockquote>

<blockquote><code>cefpython.WebRequest.State["Unsent"]</code><br>
<code>cefpython.WebRequest.State["Started"]</code><br>
<code>cefpython.WebRequest.State["HeadersReceived"]</code><br>
<code>cefpython.WebRequest.State["Loading"]</code><br>
<code>cefpython.WebRequest.State["Done"]</code><br>
<code>cefpython.WebRequest.State["Error"]</code><br>
<code>cefpython.WebRequest.State["Abort"]</code><br>