Project will move to github. Find this wiki page at the new address: https://github.com/cztomczak/cefpython/wiki/ContentFilterHandler


---


# ContentFilterHandler callbacks #

See the [ContentFilter](ContentFilter.md) object.

You must keep a strong reference to the [ContentFilterHandler](ContentFilterHandler.md)
object, otherwise it gets destroyed and callbacks are not called,
CEF Python keeps only a weak reference to this object.

## CEF 1 ##

The methods of this handler will always be called on the UI thread.

void **OnData**(str data, [StreamReader](StreamReader.md) substitute\_data)

> Set |substitute\_data| to the replacement for the data in |data| if data
> should be modified.

void **OnDrain**([StreamReader](StreamReader.md) remainder)

> Called when there is no more data to be processed. It is expected
> that whatever data was retained in the last `OnData()` call,
> it should be returned now by setting |remainder| if appropriate.