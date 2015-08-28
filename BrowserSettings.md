Project will move to github. Find this wiki page at the new address: https://github.com/cztomczak/cefpython/wiki/BrowserSettings


---


# Browser settings #



## Introduction ##

These settings can be passed to [cefpython](cefpython.md).`CreateBrowser()`.

In some cases, the default values of settings that are suggested by its name may not always be correct. This is because in one of CEF releases naming of these settings changed, and they started to accept states (enabled or disabled), instead of the state being included in its name (some\_option\_disabled). Cefpython tries to be backwards compatible, that's why the old naming convention is still used. Read description of setting and if you see that it mentions command line switch that starts with "disable-", it means that its default state is "enabled". If the command line switch starts with "enable-" then its default state is "disabled".

## Settings ##

### accelerated\_compositing\_disabled (bool) ###

> Available only in CEF 3.

> Controls whether content that depends on accelerated compositing can be
> used. Note that accelerated compositing requires hardware support and may
> not work on all systems even when enabled. Also configurable using the
> "disable-accelerated-compositing" [command-line switch](CommandLineSwitches.md).

### accelerated\_compositing\_enabled (bool) ###

> Available only in CEF 1.

> Set to true (1) to enable accelerated compositing. This is turned off by default because the current in-process GPU implementation does not support it correctly.

### accelerated\_layers\_disabled (bool) ###

> Available only in CEF 1. Set to True to disable accelerated layers. This affects features like 3D CSS transforms.

### accelerated\_video\_disabled (bool) ###

> Available only in CEF 1. Set to True to disable accelerated video.

### accelerated\_2d\_canvas\_disabled (bool) ###

> Available only in CEF 1. Set to True to disable accelerated 2d canvas.

### accelerated\_filters\_disabled (bool) ###

> Available only in CEF 1. Set to True to disable accelerated filters.

### accelerated\_plugins\_disabled (bool) ###

> Available only in CEF 1. Set to True to disable accelerated plugins.

### animation\_frame\_rate (int) ###

> Available only in CEF 1. The number of frames per second (fps) for animation and windowless rendering. When window rendering is enabled and the JavaScript requestAnimationFrame method is used the browser client area will be invalidated at the rate specified. When window rendering is disabled the CefRenderHandler::OnPaint() method will be called at the rate specified. This value must be between 0 and 90. Specify a value of zero for the default frame rate of 30 fps. Changing this value may affect display performance and/or CPU usage.

### application\_cache\_disabled (bool) ###

> Controls whether the application cache can be used. Also configurable using
> the "disable-application-cache" [command-line switch](CommandLineSwitches.md).

### author\_and\_user\_styles\_disabled (bool) ###

> Controls whether style sheets can be used. Also configurable using the
> "disable-author-and-user-styles" [command-line switch](CommandLineSwitches.md).

> This setting was removed in Chrome 33. Soon it will be removed from cefpython as well.

### caret\_browsing\_enabled (bool) ###

> Controls whether the caret position will be drawn. Also configurable using
> the "enable-caret-browsing" [command-line switch](CommandLineSwitches.md).

### databases\_disabled (bool) ###

> Controls whether databases can be used. Also configurable using the
> "disable-databases" [command-line switch](CommandLineSwitches.md).

### default\_encoding (string) ###

> Default encoding for Web content. If empty "ISO-8859-1" will be used. Also
> configurable using the "default-encoding" [command-line switch](CommandLineSwitches.md).

### developer\_tools\_disabled (bool) ###

> Available only in CEF 1.

> Controls whether developer tools (WebKit inspector) can be used. Also
> configurable using the "disable-developer-tools" command-line switch.

### dom\_paste\_disabled (bool) ###

> Controls whether DOM pasting is supported in the editor via
> execCommand("paste"). The |javascript\_access\_clipboard\_disallowed| setting must also
> be set (to true or false). Also configurable using the "disable-javascript-dom-paste"
> [command-line switch](CommandLineSwitches.md).

### drag\_drop\_disabled (bool) ###

> Available only in CEF 1. Disable drag & drop of URLs from other windows.

### encoding\_detector\_enabled (bool) ###

> Available only in CEF 1. Set to True to attempt automatic detection of content encoding

### file\_access\_from\_file\_urls\_allowed (bool) ###

> Controls whether file URLs will have access to other file URLs. Also
> configurable using the "allow-access-from-files" [command-line switch](CommandLineSwitches.md).

> This option seems to be missing in the latest Chromium. New flags are: --allow-file-access and --allow-file-access-from-files.

### fullscreen\_enabled (bool) ###

> Available only in CEF 1. Set to True to enable fullscreen mode. To go fullscreen call [Browser](Browser.md).ToggleFullscreen().

### history\_disabled (bool) ###

> Available only in CEF 1. Disable history back/forward navigation.

### hyperlink\_auditing\_disabled (bool) ###

> Available only in CEF 1. Set to True to disable hyperlink pings (<a ping> and window.sendPing).

### image\_load\_disabled (bool) ###

> Controls whether image URLs will be loaded from the network. A cached image
> will still be rendered if requested. Also configurable using the
> "disable-image-loading" [command-line switch](CommandLineSwitches.md).

### javascript\_disabled (bool) ###

> Controls whether Javascript can be executed. Also configurable using the
> "disable-javascript" [command-line switch](CommandLineSwitches.md).

### javascript\_open\_windows\_disallowed (bool) ###

> Controls whether Javascript can be used for opening windows. Also
> configurable using the "disable-javascript-open-windows" [command-line switch](CommandLineSwitches.md).

### javascript\_close\_windows\_disallowed (bool) ###

> Controls whether Javascript can be used to close windows that were not
> opened via Javascript. Javascript can still be used to close windows that
> were opened via Javascript. Also configurable using the
> "disable-javascript-close-windows" [command-line switch](CommandLineSwitches.md).

### javascript\_access\_clipboard\_disallowed (bool) ###

> Controls whether Javascript can access the clipboard. Also configurable
> using the "disable-javascript-access-clipboard" [command-line switch](CommandLineSwitches.md).

### java\_disabled (bool) ###

> Controls whether the Java plugin will be loaded. Also configurable using
> the "disable-java" [command-line switch](CommandLineSwitches.md).

### load\_drops\_disabled (bool) ###

> Available only in CEF 1. Disable default navigation resulting from drag & drop of URLs.

### local\_storage\_disabled (bool) ###

> Controls whether local storage can be used. Also configurable using the
> "disable-local-storage" [command-line switch](CommandLineSwitches.md).

### page\_cache\_disabled (bool) ###

> Available only in CEF 1.

> Controls whether the fastback (back/forward) page cache will be used. Also configurable using the "enable-fastback" command-line switch.

### plugins\_disabled (bool) ###

> Controls whether any plugins will be loaded. Also configurable using the
> "disable-plugins" [command-line switch](CommandLineSwitches.md).

### remote\_fonts (bool) ###

> Available only in CEF 3.

> Controls the loading of fonts from remote sources. Also configurable using
> the "disable-remote-fonts" [command-line switch](CommandLineSwitches.md).

### remote\_fonts\_disabled (bool) ###

> Available only in CEF 1. Set to True to disable loading of fonts from remote sources.

### shrink\_standalone\_images\_to\_fit (bool) ###

> Controls whether standalone images will be shrunk to fit the page. Also
> configurable using the "image-shrink-standalone-to-fit" [command-line switch](CommandLineSwitches.md).

### site\_specific\_quirks\_disabled (bool) ###

> Available only in CEF 1. Set to True to disable browser backwards compatibility features.

### tab\_to\_links\_disabled (bool) ###

> Controls whether the tab key can advance focus to links. Also configurable
> using the "disable-tab-to-links" [command-line switch](CommandLineSwitches.md).

### text\_area\_resize\_disabled (bool) ###

> Controls whether text areas can be resized. Also configurable using the
> "disable-text-area-resize" [command-line switch](CommandLineSwitches.md).

### universal\_access\_from\_file\_urls\_allowed (bool) ###

> Controls whether file URLs will have access to all URLs. Also configurable
> using the "allow-universal-access-from-files" [command-line switch](CommandLineSwitches.md).

> This option seems to be missing in the latest Chromium. New flags are: --allow-file-access and --allow-file-access-from-files.

### user\_style\_sheet\_enabled (bool) ###

> Available only in CEF 1. Set to True to enable the user style sheet for all pages.

### user\_style\_sheet\_location (string) ###

> Location of the user style sheet that will be used for all pages. This must
> be a data URL of the form "data:text/css;charset=utf-8;base64,csscontent"
> where "csscontent" is the base64 encoded contents of the CSS file. Also
> configurable using the "user-style-sheet-location" command-line switch.

> This setting was removed in Chrome 33. Soon it will be removed from cefpython as well.

### web\_security\_disabled (bool) ###

> Controls whether web security restrictions (same-origin policy) will be
> enforced. Disabling this setting is not recommend as it will allow risky
> security behavior such as cross-site scripting (XSS). Also configurable
> using the "disable-web-security" [command-line switch](CommandLineSwitches.md).

### webgl\_disabled (bool) ###

> Controls whether WebGL can be used. Note that WebGL requires hardware
> support and may not work on all systems even when enabled. Also
> configurable using the "disable-webgl" [command-line switch](CommandLineSwitches.md).

### xss\_auditor\_enabled (bool) ###

> Available only in CEF 1. Set to True to enable console warnings about XSS attempts.


## Font settings ##

### standard\_font\_family (string) ###
### fixed\_font\_family (string) ###
### serif\_font\_family (string) ###
### sans\_serif\_font\_family (string) ###
### cursive\_font\_family (string) ###
### fantasy\_font\_family (string) ###
### default\_font\_size (int) ###
### default\_fixed\_font\_size (int) ###
### minimum\_font\_size (int) ###
### minimum\_logical\_font\_size (int) ###