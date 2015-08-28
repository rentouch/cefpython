Project will move to github. Find this wiki page at the new address: https://github.com/cztomczak/cefpython/wiki/ArchitectureFeatures


---


# Architecture & Features #

Table of contents: 

## CEF 3 summary ##
  * supports html5 audio/video, good performance of webgl and other accelerated content
  * uses multi process architecture and [Chromium Content API](http://www.chromium.org/developers/content-module/content-api), thus giving performance and features similar to Chrome
  * V8 engine is runing in a separate process so javascript integration can be done only through asynchronous messaging between processes, in CEF 1 you can call javascript and python back synchronously
  * single process is for debugging purposes only, it is unstable, it will likely be fixed in the future as Chromium for mobile devices needs a stable single-process mode

CEF 3 comes with the the latest version of Chrome.


For more information on CEF architecture see this wiki page on the Chromium Embedded project:
http://code.google.com/p/chromiumembedded/wiki/Architecture

## CEF 3 features ported in CEF Python 3 ##

  * [Frame](Frame.md) object
  * [Browser](Browser.md) object
  * [ApplicationSettings](ApplicationSettings.md)
  * [BrowserSettings](BrowserSettings.md)
  * [DownloadHandler](DownloadHandler.md)
  * [JavascriptBindings](JavascriptBindings.md)
  * [JavascriptCallback](JavascriptCallback.md)
  * Python callbacks
  * [JavascriptContextHandler](JavascriptContextHandler.md) (partially)
  * JavascriptDialogHandler
  * [RequestHandler](RequestHandler.md)
  * [Request](Request.md) object
  * [WebPluginInfo](WebPluginInfo.md)
  * [Cookie](Cookie.md)
  * [CookieManager](CookieManager.md)
  * [CookieVisitor](CookieVisitor.md)
  * [LoadHandler](LoadHandler.md)
  * [RenderHandler](RenderHandler.md)
  * [ResourceHandler](ResourceHandler.md)
  * [Response](Response.md) object
  * [WebRequest](WebRequest.md) and [WebRequestClient](WebRequestClient.md)
  * [LifespanHandler](LifespanHandler.md) (partially)

## CEF 3 features not yet ported to CEF Python 3 ##

  * [context menu handler](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef3/include/cef_context_menu_handler.h) & [menu model](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef3/include/cef_menu_model.h) - API is not provided, but context menu is configurable, see ApplicationSettings.`context_menu`
  * [dialog handler](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef3/include/cef_dialog_handler.h)
  * [dom manipulation](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef3/include/cef_dom.h) - won't be implemented as it was deprecated and has memory leaks. The recommended way is to manipulate DOM through javascript and report to python through javascript bindings.

  * [focus handler](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef3/include/cef_focus_handler.h)
  * [geolocation](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef3/include/cef_geolocation.h) & [geolocation handler](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef3/include/cef_geolocation_handler.h)
  * [origin whitelist](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef3/include/cef_origin_whitelist.h)
  * [proxy handler](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef3/include/cef_proxy_handler.h)
  * [render process handler](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef3/include/cef_render_process_handler.h)
  * [resource bundle handler](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef3/include/cef_resource_bundle_handler.h)
  * [custom scheme](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef3/include/cef_scheme.h)
  * [stream reader & writer](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef3/include/cef_stream.h) for request response
  * [trace notifications](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef3/include/cef_trace.h) & [trace event](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef3/include/cef_trace_event.h)
  * [web plugin](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef3/include/cef_web_plugin.h) (WebPluginInfo already implemented)
  * [xml reader](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef3/include/cef_xml_reader.h)
  * [zip reader](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef3/include/cef_zip_reader.h)

## CEF 1 summary ##
  * single process architecture
  * more feature complete API than in CEF 3 (as of the moment)
  * html5 audio and video support was removed (see [Issue 18](https://code.google.com/p/cefpython/issues/detail?id=18))
  * uses Webkit API
  * reduced memory usage and closer integration with the client application
  * [reduced performance](http://code.google.com/p/chromiumembedded/issues/detail?id=304) with certain types of accelerated content and [crashes](http://code.google.com/p/chromiumembedded/issues/detail?id=242) due to plugins like Flash running in the same process.

CEF 1 is currently in maintenance mode and the latest version available includes Chrome 27.

## Known problems in CEF 1 ##

Flash plugin will crash on Linux, see [Issue 553 in CEF Issue Tracker](http://code.google.com/p/chromiumembedded/issues/detail?id=553). However, Pepper Flash Player might work in CEF 3 on Linux (not yet tested).

## CEF 1 features ported to CEF Python 1 ##

  * [Frame](Frame.md) object
  * [Browser](Browser.md) object
  * [application settings](ApplicationSettings.md)
  * [browser settings](BrowserSettings.md)
  * [javascript bindings](JavascriptBindings.md)
  * [javascript callbacks](JavascriptCallback.md) & python callbacks
  * [display handler](DisplayHandler.md)
  * [keyboard handler](KeyboardHandler.md)
  * [lifespan handler](LifespanHandler.md) (partially)
  * [load handler](LoadHandler.md)
  * [render handler](RenderHandler.md)
  * [request handler](RequestHandler.md) (partially)
  * [Response](Response.md) object
  * [javascript context handler](JavascriptContextHandler.md) (partially)
  * [ContentFilter](ContentFilter.md) for resource response
  * [Request](Request.md) object
  * [StreamReader](StreamReader.md) for request response
  * [WebRequest](WebRequest.md)
  * [Cookie](Cookie.md) class
  * [CookieManager](CookieManager.md) class
  * [CookieVisitor](CookieVisitor.md) callbacks
  * [DownloadHandler](DownloadHandler.md)
  * [DragHandler](DragHandler.md)
  * [DragData](DragData.md)

## CEF 1 features not yet ported to CEF Python 1 ##

  * [dom manipulation](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef1/include/cef_dom.h) - won't be implemented as it was deprecated and has memory leaks. The recommended way is to manipulate DOM through javascript and report to python through javascript bindings.
  * [find handler](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef1/include/cef_find_handler.h)
  * [focus handler](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef1/include/cef_focus_handler.h)
  * [geolocation](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef1/include/cef_geolocation.h) & [geolocation handler](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef1/include/cef_geolocation_handler.h)
  * [jsdialog handler](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef1/include/cef_jsdialog_handler.h)
  * [menu handler](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef1/include/cef_menu_handler.h)
  * [plugin info](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef1/include/cef_nplugin.h)
  * [origin whitelist](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef1/include/cef_origin_whitelist.h)
  * [javascript extensions](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef1/include/cef_v8.h?r=972#53)
  * [permission handler for extensions](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef1/include/cef_permission_handler.h)
  * [print handler](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef1/include/cef_print_handler.h)
  * [proxy handler](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef1/include/cef_proxy_handler.h)
  * [resource bundle handler](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef1/include/cef_resource_bundle_handler.h)
  * [custom scheme](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef1/include/cef_scheme.h)
  * [web plugin](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef1/include/cef_web_plugin.h)
  * [xml reader](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef1/include/cef_xml_reader.h)
  * [zip reader](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef1/include/cef_zip_reader.h)
  * [zoom handler](http://code.google.com/p/chromiumembedded/source/browse/trunk/cef1/include/cef_zoom_handler.h)