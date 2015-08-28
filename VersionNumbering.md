Project will move to github. Find this wiki page at the new address: https://github.com/cztomczak/cefpython/wiki/VersionNumbering


---


# Version numbering #

The naming convention for CEF Python versions is XX.YY (for example 29.4), where XX is the Chromium major version, and YY is the cefpython internal version.

An example Chromium version is 29.0.1547.80, where 29 is the major version, 0 is the minor version (this one never changes), 1547 is the build version (otherwise known as branch), and 80 is the patch version.

CEF versions consist of [CEF branch](https://code.google.com/p/chromiumembedded/source/browse/branches/) and [CEF SVN revision](https://code.google.com/p/chromiumembedded/source/list). The branch is the one from the Chromium version.

When building CEF and CEF Python from sources, you should use the CEF and Chromium versions listed in the [BUILD\_COMPATIBILITY.txt](https://code.google.com/p/cefpython/source/browse/cefpython/cef3/BUILD_COMPATIBILITY.txt) file.