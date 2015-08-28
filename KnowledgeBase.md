Project will move to github. Find this wiki page at the new address: https://github.com/cztomczak/cefpython/wiki/KnowledgeBase


---


# Knowledge Base #

## Black/White browser screen ##

If you get a black or white screen then this may be caused by incompatible GPU (video card) drivers. There are following solutions to this:

1. When CEF Python is updated to a newer Chrome version then the problem may be fixed. Check with current Google Chrome if this is the case.

2. Try updating your video card drivers to the latest version available.

3. You can disable GPU hardware acceleration by adding the "disable-gpu" and "disable-gpu-compositing" command line switches. See the CommandLineSwitches wiki page. Note that this will degrade performance if you're using any advanced 3D features. It will affect 2d accelerated content as well.

Note that when web page uses WebGL then the black screen may still appear even after disabling GPU hardware acceleration. However that shouldn't be a concern as it's not supposed to work anyway. Though you may not see a nice message about WebGL not being supported. All other websites that do not use webgl will work fine.