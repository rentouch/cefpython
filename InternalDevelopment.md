Project will move to github. Find this wiki page at the new address: https://github.com/cztomczak/cefpython/wiki/InternalDevelopment


---


# Internal development #

Table of contents:


## Build instructions ##

See build instructions on these wiki pages:
  * [BuildOnWindows](BuildOnWindows.md)
  * [BuildOnLinux](BuildOnLinux.md)
  * [BuildOnMac](BuildOnMac.md)

## Sending patches ##

When attaching a patch in the Issue Tracker please also provide tests for the new functionality if applies. It can be a manual test added to the wxpython.py example or a unit test (see [Issue 59](https://code.google.com/p/cefpython/issues/detail?id=59)). Please ensure that all new functionality was tested.

See also code style guidelines below.

## Python/Cython style guidelines ##

  * try to comply with the [PEP 8 style guide](http://www.python.org/dev/peps/pep-0008/)
  * use 4 spaces for indentation
  * commit unix-style newlines (\n)
  * limit all lines to a maximum of 79 characters (comments should be shorter, max 60-65 chars)
  * do your best for the new code to be consistent with existing code base

## Track project updates ##

To track Git commits subscribe to [this RSS feed](https://code.google.com/feeds/p/cefpython/gitchanges/basic).

To track the Issue Tracker updates subscribe to [this RSS feed](https://code.google.com/feeds/p/cefpython/issueupdates/basic).

## Debug CEF stack trace ##

  1. Install gdb with the command "sudo apt-get install gdb"
  1. Type "gdb python"
  1. Inside gdb type "run pyqt.py"
  1. On segmentation fault to display stack trace type "bt"

## Debug Cython ##

Debugging Cython is currently supported only on Linux.

Before you can debug you have to install the following packages:

```
python-dbg
python-wxgtk2.8-dbg
```

Install Cython with the debug version of Python:
```
cd Cython-0.19.2/
sudo python-dbg setup.py install
```

To debug CEF Python add the "debug" argument to the "compile.py" script:

```
python-dbg compile.py 99.99 --debug
```

After a while you should see a GDB console awaiting a command, to run the app type:

```
cy run
```

To get the stack trace type:

```
cy backtrace
```

The command for running and debugging script is:
```
cygdb . --args python-dbg wxpython.py
```

To run commands automatically in gdb add "-x gdb.cmds" flag. An example gdb.cmds file:
```
cy run
quit
```

The final command would look like:
```
cygdb . -x gdb.cmds --args python-dbg wxpython.py
```

For more commands see the "Using the debugger" section in the Cython documentation:
http://docs.cython.org/src/userguide/debugging.html#using-the-debugger

## Updating to a newer CEF version ##

To see changes in the CEF API compare "cefpython/ce3/include/" directory with the new CEF "include/" directory. When doing so compare the CEF header files downloaded directly from the CEF SVN repository, as the CEF "include/" directory obtained from binary build will not include platform specific header files. For example to fetch CEF 3 branch 1650 revision `1639` use this command:

```
svn checkout http://chromiumembedded.googlecode.com/svn/branches/1650@1639 cef3-b1650-r1639
```