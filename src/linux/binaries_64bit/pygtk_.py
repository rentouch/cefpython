# An example of embedding the CEF browser in PyGTK on Linux.
# Tested with GTK "2.24.10".

# The official CEF Python binaries come with tcmalloc hook
# disabled. But if you've built custom binaries and kept tcmalloc
# hook enabled, then be aware that in such case it is required
# for the cefpython module to be the very first import in
# python scripts. See Issue 73 in the CEF Python Issue Tracker
# for more details.

import ctypes, os, sys
cur_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
libcef_so = os.path.join(cur_dir, 'libcef.so')
if os.path.exists(libcef_so):
    LD_LIBRARY_PATH = os.environ.get('LD_LIBRARY_PATH', None)
    if not LD_LIBRARY_PATH:
        LD_LIBRARY_PATH = cur_dir
    else:
        LD_LIBRARY_PATH += os.pathsep + cur_dir
    os.putenv('LD_LIBRARY_PATH', LD_LIBRARY_PATH)
    
    # Import local module
    ctypes.CDLL(libcef_so, ctypes.RTLD_GLOBAL)
    if 0x02070000 <= sys.hexversion < 0x03000000:
        import cefpython_py27 as cefpython
    else:
        raise Exception("Unsupported python version: %s" % sys.version)
else:
    # Import from package
    from cefpython3 import cefpython

import pygtk
pygtk.require('2.0')
import gtk
import gobject
import re

def GetApplicationPath(file=None):
    import re, os, platform
    # On Windows after downloading file and calling Browser.GoForward(),
    # current working directory is set to %UserProfile%.
    # Calling os.path.dirname(os.path.realpath(__file__))
    # returns for eg. "C:\Users\user\Downloads". A solution
    # is to cache path on first call.
    if not hasattr(GetApplicationPath, "dir"):
        if hasattr(sys, "frozen"):
            dir = os.path.dirname(sys.executable)
        elif "__file__" in globals():
            dir = os.path.dirname(os.path.realpath(__file__))
        else:
            dir = os.getcwd()
        GetApplicationPath.dir = dir
    # If file is None return current directory without trailing slash.
    if file is None:
        file = ""
    # Only when relative path.
    if not file.startswith("/") and not file.startswith("\\") and (
            not re.search(r"^[\w-]+:", file)):
        path = GetApplicationPath.dir + os.sep + file
        if platform.system() == "Windows":
            path = re.sub(r"[/\\]+", re.escape(os.sep), path)
        path = re.sub(r"[/\\]+$", "", path)
        return path
    return str(file)

def ExceptHook(excType, excValue, traceObject):
    import traceback, os, time, codecs
    # This hook does the following: in case of exception write it to
    # the "error.log" file, display it to the console, shutdown CEF
    # and exit application immediately by ignoring "finally" (_exit()).
    errorMsg = "\n".join(traceback.format_exception(excType, excValue,
            traceObject))
    errorFile = GetApplicationPath("error.log")
    try:
        appEncoding = cefpython.g_applicationSettings["string_encoding"]
    except:
        appEncoding = "utf-8"
    if type(errorMsg) == bytes:
        errorMsg = errorMsg.decode(encoding=appEncoding, errors="replace")
    try:
        with codecs.open(errorFile, mode="a", encoding=appEncoding) as fp:
            fp.write("\n[%s] %s\n" % (
                    time.strftime("%Y-%m-%d %H:%M:%S"), errorMsg))
    except:
        print("[pygtk_.py]: WARNING: failed writing to error file: %s" % (
                errorFile))
    # Convert error message to ascii before printing, otherwise
    # you may get error like this:
    # | UnicodeEncodeError: 'charmap' codec can't encode characters
    errorMsg = errorMsg.encode("ascii", errors="replace")
    errorMsg = errorMsg.decode("ascii", errors="replace")
    print("\n"+errorMsg+"\n")
    cefpython.QuitMessageLoop()
    cefpython.Shutdown()
    os._exit(1)

class PyGTKExample:
    mainWindow = None
    container = None
    browser = None
    exiting = None
    searchEntry = None
    vbox = None
    menubar = None
    menubar_height = None

    def __init__(self):
        self.mainWindow = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.mainWindow.connect('focus-in-event', self.OnFocusIn)
        self.mainWindow.connect('configure-event', self.OnConfigure)
        self.mainWindow.connect('destroy', self.OnExit)
        self.mainWindow.set_size_request(width=800, height=600)
        self.mainWindow.set_title('PyGTK CEF example')
        self.mainWindow.realize()

        self.vbox = gtk.VBox(False, 0)
        self.vbox.connect('size-allocate', self.OnVBoxSize)
        self.menubar = self.CreateMenu()
        self.menubar.connect('size-allocate', self.OnMenubarSize)
        self.vbox.pack_start(self.menubar, False, False, 0)
        self.mainWindow.add(self.vbox)

        windowInfo = cefpython.WindowInfo()
        windowInfo.SetAsChild(self.mainWindow.window.xid, [0,0,0,0])
        # Linux requires adding "file://" for local files,
        # otherwise /home/some will be replaced as http://home/some
        self.browser = cefpython.CreateBrowserSync(
            windowInfo,
            browserSettings={},
            navigateUrl="file://"+GetApplicationPath("example.html"))

        self.vbox.show()
        self.mainWindow.show()
        self.vbox.get_window().focus()
        self.mainWindow.get_window().focus()
        gobject.timeout_add(10, self.OnTimer)

    def CreateMenu(self):
        file = gtk.MenuItem('File')
        file.show()
        filemenu = gtk.Menu()
        item = gtk.MenuItem('Open')
        filemenu.append(item)
        item.show()
        item = gtk.MenuItem('Exit')
        filemenu.append(item)
        item.show()
        file.set_submenu(filemenu)

        about = gtk.MenuItem('About')
        about.show()
        aboutmenu = gtk.Menu()
        item = gtk.MenuItem('CEF Python')
        aboutmenu.append(item)
        item.show()
        about.set_submenu(aboutmenu)

        menubar = gtk.MenuBar()
        menubar.append(file)
        menubar.append(about)
        menubar.show()

        return menubar

    def OnTimer(self):
        if self.exiting:
            return False
        cefpython.MessageLoopWork()
        return True

    def OnFocusIn(self, widget, data):
        if self.browser:
            self.browser.SetFocus(True)
            return True
        return False

    def OnConfigure(self, widget, data):
        if self.browser:
            self.browser.NotifyMoveOrResizeStarted()
        return False

    def OnVBoxSize(self, widget, data):
        if self.browser:
            x = data.x
            y = data.y + self.menubar_height
            width = data.width
            height = data.height - self.menubar_height
            self.browser.SetBounds(x, y, width, height)
            print("%s %s %s %s" % (x,y,width,height))

    def OnMenubarSize(self, widget, data):
        self.menubar_height = data.height

    def OnExit(self, widget, data=None):
        self.exiting = True
        gtk.main_quit()

if __name__ == '__main__':
    version = '.'.join(map(str, list(gtk.gtk_version)))
    print('[pygtk_.py] GTK version: %s' % version)

    # Intercept python exceptions. Exit app immediately when exception
    # happens on any of the threads.
    sys.excepthook = ExceptHook

    # Application settings
    settings = {
        "debug": True, # cefpython debug messages in console and in log_file
        "log_severity": cefpython.LOGSEVERITY_INFO, # LOGSEVERITY_VERBOSE
        "log_file": GetApplicationPath("debug.log"), # Set to "" to disable
        # This directories must be set on Linux
        "locales_dir_path": cefpython.GetModuleDirectory()+"/locales",
        "resources_dir_path": cefpython.GetModuleDirectory(),
        "browser_subprocess_path": "%s/%s" % (
            cefpython.GetModuleDirectory(), "subprocess"),
    }

    cefpython.Initialize(settings)
    cefpython.WindowUtils.InstallX11ErrorHandlers()

    gobject.threads_init() # Timer for the message loop
    PyGTKExample()
    gtk.main()

    cefpython.Shutdown()
