Project will move to github. Find this wiki page at the new address: https://github.com/cztomczak/cefpython/wiki/WebPluginInfo


---


# WebPluginInfo object #

See [RequestHandler](RequestHandler.md).`OnBeforePluginLoad()`.

string **GetName**()

> Returns the plugin name (i.e. Flash).

string **GetPath**()

> Returns the plugin file path (DLL/bundle/library).

string **GetVersion**()

> Returns the version of the plugin (may be OS-specific).

string **GetDescription**()

> Returns a description of the plugin from the version information.