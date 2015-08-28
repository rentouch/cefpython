Project will move to github: https://github.com/cztomczak/cefpython


---


<table cellpadding='0' cellspacing='0' align='left' border='0' width='100%'><tr>
<td width='180'>
<h1>CEF Python</h1>
</td>
<td valign='top'>
<br>
<a href='https://twitter.com/intent/tweet?text=Python+bindings+for+embedding+Chromium+browser+in+desktop+applications&url=https://code.google.com/p/cefpython/' title='Tweet'><img src='https://phpdesktop.googlecode.com/git/var/share-buttons/tweet.jpg' width='71' height='24' /></a>
<a href='https://delicious.com/save?v=5&provider=cefpython&noui&jump=close&url=https://code.google.com/p/cefpython/&title=Python+bindings+for+embedding+Chromium+browser+in+desktop+applications' title='Delicious'><img src='https://phpdesktop.googlecode.com/git/var/share-buttons/delicious.png' width='102' height='24' /></a>
<a href='http://www.reddit.com/submit?url=https://code.google.com/p/cefpython/' title='Reddit this!'><img src='https://phpdesktop.googlecode.com/git/var/share-buttons/reddit.gif?x=1' width='94' height='24' /></a>
</td>
</tr></table>

## Introduction ##

CEF Python is an open source project founded by [Czarek Tomczak](http://www.linkedin.com/in/czarektomczak) in 2012 to provide python bindings for the [Chromium Embedded Framework](http://code.google.com/p/chromiumembedded/). See the growing list of [applications using CEF](http://en.wikipedia.org/wiki/Chromium_Embedded_Framework#Applications_using_CEF) on wikipedia. Examples of embedding CEF browser are available for many popular GUI toolkits including: [wxPython](wxPython.md), [PyGTK](PyGTK.md), [PyQt](PyQt.md), [PySide](PySide.md), [Kivy](Kivy.md), [Panda3D](Panda3D.md) and [PyWin32](https://code.google.com/p/cefpython/source/browse/cefpython/cef3/windows/binaries_32bit/pywin32.py).

Some use cases for CEF:
  * Embed a web browser control with great HTML5 support (based on Chromium)
  * Use it to create a HTML5 based GUI in an application. This can act as a replacement for GUI toolkits like wxWidgets/Qt/Gtk. For native communication between javascript and python use [javascript bindings](JavascriptBindings.md). Another option is to run an internal python web server and use websockets/XMLHttpRequest for js<>python communication. This way you can write a desktop app in the same way you write web apps.
  * Render web content off-screen in applications that use custom drawing frameworks. See the [Kivy](Kivy.md) and [Panda3D](Panda3D.md) examples.
  * Use it for automated testing of existing web applications. Use it for web scraping, or as a web crawler or other kind of internet bots.

## Supported Python versions and platforms ##

  * Supported Python versions: 2.7 (Python 3.4 will be supported soon, see [Issue 121](https://code.google.com/p/cefpython/issues/detail?id=121))
  * Supported platforms: Windows, Linux, Mac (both 32bit and 64bit binaries are available for all platforms)

## Downloads ##

  * For Windows: see the [Download\_CEF3\_Windows](Download_CEF3_Windows.md) wiki page.
  * For Linux: see the [Download\_CEF3\_Linux](Download_CEF3_Linux.md) wiki page.
  * For Mac: see the [Download\_CEF3\_Mac](Download_CEF3_Mac.md) wiki page.

## Help ##

  * Documentation is on the [wiki pages](http://code.google.com/p/cefpython/w/list). Start with the [API](API.md) page.
  * Ask questions and report problems on the [CEF Python Forum](https://groups.google.com/group/cefpython).
  * Please do not use the [Issue Tracker](http://code.google.com/p/cefpython/issues/list) for asking questions.
  * Instructions on how to enable Flash Player are on the [Plugins](Plugins.md) wiki page.
  * Having problems with playing audio or video? See the [AudioVideo](AudioVideo.md) wiki page.

## Watch the project ##

  * To watch all issues updates subscribe to the [issueupdates RSS feed](https://code.google.com/feeds/p/cefpython/issueupdates/basic)
  * To watch Git commits subscribe to the [gitchanges RSS feed](https://code.google.com/feeds/p/cefpython/gitchanges/basic)
  * Starring issue gets you email notifications when issue is updated
  * Join the [Forum](http://groups.google.com/group/cefpython) and set membership settings to send Daily summaries via email

## Support development ##

<a href='https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=95W9VHNSFWRUN'><img src='https://www.paypalobjects.com/en_US/GB/i/btn/btn_donateCC_LG.gif' align='right' /></a> If you are interested in donating time to help with the CEF Python development please see the [InternalDevelopment](InternalDevelopment.md) wiki page. If you would like to support general CEF Python development efforts by making a donation please click the Paypal "Donate" button to the right. At this time CEF Python is unable to accept donations that sponsor the development of specific features. If you are interested in sponsorship opportunities please contact Czarek directly.

### Thanks ###

  * Thanks to the numerous individuals that made a Paypal donation: Walter Purvis, Rokas Stupuras, Alex Rattray, Greg Kacy, Paul Korzhyk.
  * Thanks to those that have donated their time through code contributions: see the  [AUTHORS.txt](https://code.google.com/p/cefpython/source/browse/cefpython/AUTHORS.txt) file. Patches can be attached in the issue tracker.
  * <a href='http://www.cyaninc.com/'><img width='200' align='right' height='42' src='https://cefpython.googlecode.com/git/cefpython/var/cyan_new_logo.png' /></a>Many thanks to [Cyan Inc.](http://www.cyaninc.com/) for sponsoring this project, making CEF Python 3 more mature. Lots of new features were added, including javascript bindings and Linux support.
  * Thanks to [Rentouch GmbH](http://www.rentouch.ch/) for sponsoring the development of the off-screen rendering support in CEF Python 3.
  * Thanks to Thomas Wusatiuk for sponsoring the development of the web response reading features in CEF Python 3.
  * Thanks to Adam Duston for donating a Macbook to aid the development of the Mac port.

## Built a cool app? ##

Built a cool app using CEF Python and would like to share info with the community? Talk about it on the [CEF Python Forum](https://groups.google.com/group/cefpython?hl=en).

## Familiar with PHP or Go? ##

The author of CEF Python is also working on CEF bindings for other languages such as PHP and Go. For PHP take a look at the [PHP Desktop](http://code.google.com/p/phpdesktop/) project. For Go see the [CEF2go](https://github.com/CzarekTomczak/cef2go) project on GitHub.