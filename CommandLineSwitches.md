Project will move to github. Find this wiki page at the new address: https://github.com/cztomczak/cefpython/wiki/CommandLineSwitches


---


# Command line switches #

There are many settings that can be customized through Chromium command line switches. These switches can only be set programmatically by passing a dictionary of switches as a second argument to [cefpython](cefpython.md).Initialize(applicationSettings, commandLineSwitches). The `commandLineSwitches param` is a dictionary with switch name as a key. The switch name should not contain the "-" or "--" prefix, otherwise it will be ignored. Switch value may be an empty string, if the switch doesn't require a value. These switches are set for the main process and all subprocesses. See the description of the [cefpython](cefpython.md).Initialize() function to see how to preview the final command line strings formed by CEF.

There are two types of switches, Chromium switches and CEF switches:
  * An assembled list of all Chromium switches can be found on this webite: [peter.sh/experiments/chromium-command-line-switches](http://peter.sh/experiments/chromium-command-line-switches/)
  * A list of all CEF switches can be found in [cef\_switches.cc](https://code.google.com/p/chromiumembedded/source/browse/trunk/cef3/libcef/common/cef_switches.cc)

Some of the switches in Chromium are experimental, and may crash application if used inappropriately.

## Example switches ##

### enable-media-stream ###

To enable media (WebRTC audio/video) streaming set the "enable-media-stream" CEF switch. This will enable the `getUserMedia` function in javascript.

### proxy-server ###

To set custom proxy set the "proxy-server" Chromium switch to "socks5://127.0.0.1:8888" for example. See also [Proxy Resolution](https://code.google.com/p/chromiumembedded/wiki/GeneralUsage#Proxy_Resolution) page.

### no-proxy-server ###

By default Chromium uses the IE proxy settings (set in Internet Explorer options), to disable that set the "no-proxy-server" Chromium switch. See also [Proxy Resolution](https://code.google.com/p/chromiumembedded/wiki/GeneralUsage#Proxy_Resolution) page.

### disable-gpu ###

Disable GPU rendering and switch to CPU software rendering. This flag can fix the [black/white browser screen](https://code.google.com/p/cefpython/wiki/KnowledgeBase#Black/White_browser_screen) issue.

## Chromium switches by category ##

The peter.sh website should list all Chromium switches that are assembled from many Chromium files. Though, some switches may be missing there. Here is a list (in some way categorized) of all Chromium source files that define switches (list assembled on January 16, 2014):

  * [apps/switches.cc](https://src.chromium.org/svn/trunk/src/apps/switches.cc)
  * [ash/ash\_switches.cc](https://src.chromium.org/svn/trunk/src/ash/ash_switches.cc)
  * [base/base\_switches.cc](https://src.chromium.org/svn/trunk/src/base/base_switches.cc)
  * [cc/base/switches.cc](https://src.chromium.org/svn/trunk/src/cc/base/switches.cc)
  * [chrome/common/chrome\_switches.cc](https://src.chromium.org/svn/trunk/src/chrome/common/chrome_switches.cc)
  * [components/autofill/core/common/autofill\_switches.cc](https://src.chromium.org/svn/trunk/src/components/autofill/core/common/autofill_switches.cc)
  * [components/nacl/common/nacl\_switches.cc](https://src.chromium.org/svn/trunk/src/components/nacl/common/nacl_switches.cc)
  * [content/public/common/content\_switches.cc](https://src.chromium.org/svn/trunk/src/content/public/common/content_switches.cc)
  * [google\_apis/gaia/gaia\_switches.cc](https://src.chromium.org/svn/trunk/src/google_apis/gaia/gaia_switches.cc)
  * [gpu/command\_buffer/service/gpu\_switches.cc](https://src.chromium.org/svn/trunk/src/gpu/command_buffer/service/gpu_switches.cc)
  * [ipc/ipc\_switches.cc](https://src.chromium.org/svn/trunk/src/ipc/ipc_switches.cc)
  * [media/base/media\_switches.cc](https://src.chromium.org/svn/trunk/src/media/base/media_switches.cc)
  * [ppapi/shared\_impl/ppapi\_switches.cc](https://src.chromium.org/svn/trunk/src/ppapi/shared_impl/ppapi_switches.cc)
  * [ui/base/ui\_base\_switches.cc](https://src.chromium.org/svn/trunk/src/ui/base/ui_base_switches.cc)
  * [ui/base/ui\_base\_switches\_util.cc](https://src.chromium.org/svn/trunk/src/ui/base/ui_base_switches_util.cc)
  * [ui/compositor/compositor\_switches.cc](https://src.chromium.org/svn/trunk/src/ui/compositor/compositor_switches.cc)
  * [ui/gfx/switches.cc](https://src.chromium.org/svn/trunk/src/ui/gfx/switches.cc)
  * [ui/gl/gl\_switches.cc](https://src.chromium.org/svn/trunk/src/ui/gl/gl_switches.cc)
  * [ui/keyboard/keyboard\_switches.cc](https://src.chromium.org/svn/trunk/src/ui/keyboard/keyboard_switches.cc)