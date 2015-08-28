Project will move to github. Find this wiki page at the new address: https://github.com/cztomczak/cefpython/wiki/WebRequestClient


---


# WebRequestClient callbacks #

See [WebRequest](WebRequest.md).`CreateWebRequest()`.

You must keep a strong reference to the [WebRequest](WebRequest.md) object
during the request, otherwise it gets destroyed and
the [WebRequestClient](WebRequestClient.md) callbacks won't get called.

## CEF 3 ##

The methods of this class will be called on the same thread that
created the request unless otherwise documented.

void **OnUploadProgress**([WebRequest](WebRequest.md) webRequest, long current, long total)

Notifies the client of upload progress. |current| denotes the number of
bytes sent so far and |total| is the total size of uploading data (or -1 if
chunked upload is enabled). This method will only be called if the
`ReportUploadProgress` flag is set on the request (see [Request](Request.md).`GetFlags()`
and `SetFlags()`)

void **OnDownloadProgress**([WebRequest](WebRequest.md) webRequest, long current, long total)

Notifies the client of download progress. |current| denotes the number of
bytes received up to the call and |total| is the expected total size of the
response (or -1 if not determined).

void **OnDownloadData**([WebRequest](WebRequest.md) webRequest, string data)

Called when some part of the response is read. |data| contains the current
bytes received since the last call. This method will not be called if the
`NoDownloadData` flag is set on the request (see [Request](Request.md).`GetFlags()`
and `SetFlags()`).

void **OnRequestComplete**([WebRequest](WebRequest.md) webRequest)

Notifies the client that the request has completed. Use the
[WebRequest](WebRequest.md).`GetRequestStatus()` method to determine if the request was
successful or not.

bool **GetAuthCredentials**(bool isProxy, string host, int port, string realm, string scheme, [Callback](Callback.md) callback)

> Called on the IO thread when the browser needs credentials from the user.
> |isProxy| indicates whether the host is a proxy server. |host| contains the
> hostname and |port| contains the port number. Return true to continue the
> request and call [Callback](Callback.md).`Continue()` when the authentication
> information is available. Return false to cancel the request. This method
> will only be called for requests initiated from the browser process.

## CEF 1 ##

The methods of this class will always be called on the UI thread.

void **OnStateChange**([WebRequest](WebRequest.md) webRequest, `RequestState` state)

> Notifies the client that the request state has changed. State change
> notifications will always be sent before the below notification methods
> are called.

> `RequestState` is one of:

> `cefpython.WebRequest.State["Unsent"]`<br>
<blockquote><code>cefpython.WebRequest.State["Started"]</code><br>
<code>cefpython.WebRequest.State["HeadersReceived"]</code><br>
<code>cefpython.WebRequest.State["Loading"]</code><br>
<code>cefpython.WebRequest.State["Done"]</code><br>
<code>cefpython.WebRequest.State["Error"]</code><br>
<code>cefpython.WebRequest.State["Abort"]</code><br></blockquote>

void <b>OnRedirect</b>(<a href='WebRequest.md'>WebRequest</a> webRequest, <a href='Request.md'>Request</a> request, <a href='Response.md'>Response</a> response)<br>
<br>
<blockquote>Notifies the client that the request has been redirected and<br>
provides a chance to change the request parameters.</blockquote>

void <b>OnHeadersReceived</b>(<a href='WebRequest.md'>WebRequest</a> webRequest, <a href='Response.md'>Response</a> response)<br>
<br>
<blockquote>Notifies the client of the response data.</blockquote>

void <b>OnProgress</b>(<a href='WebRequest.md'>WebRequest</a> webRequest, long bytesSent, long totalBytesToBeSent)<br>
<br>
<blockquote>Notifies the client of the upload progress.</blockquote>

void <b>OnData</b>(<a href='WebRequest.md'>WebRequest</a> webRequest, str data)<br>
<br>
<blockquote>Notifies the client that content has been received.</blockquote>

void <b>OnError</b>(<a href='WebRequest.md'>WebRequest</a> webRequest, <a href='NetworkError.md'>NetworkError</a> errorCode)<br>
<br>
<blockquote>Notifies the client that the request ended with an error.