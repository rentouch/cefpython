Project will move to github. Find this wiki page at the new address: https://github.com/cztomczak/cefpython/wiki/AudioVideo


---


# Audio and Video support #

Table of contents: 

## CEF 3 ##

CEF 3 supports WebM & Ogg Theora video codecs. MPEG-4 & H.264
are proprietary codecs and are not included in Chromium builds,
as there are licensing issues:

> Codecs like MP3 and AAC are included in Google Chrome releases but
> not Chromium builds. This is because these formats are not open and
> require licensing. Distributing these codecs with your application
> without a licensing agreement may violate the law in certain countries.
> You should discuss with a lawyer if appropriate.

The quote above is from comment #7 in the CEF [Issue 371](https://code.google.com/p/cefpython/issues/detail?id=371):<br>
"Cannot play proprietary audio or video formats"<br>
<a href='http://code.google.com/p/chromiumembedded/issues/detail?id=371'>http://code.google.com/p/chromiumembedded/issues/detail?id=371</a>

<h4>Audio support</h4>

Open <a href='http://html5test.com/'>http://html5test.com/</a> in CEF 3 and go to audio section, results as of cefpython3 v0.12:<br>
<br>
audio element - <font color='green'>Yes</font> ✔ <br>
PCM audio support - <font color='green'>Yes</font> ✔ <br>
AAC support - <font color='red'>No</font> ✘ <br>
MP3 support - <font color='red'>No</font> ✘ <br>
Ogg Vorbis support - <font color='green'>Yes</font> ✔ <br>
Ogg Opus support - <font color='red'>No</font> ✘ <br>
WebM support - <font color='green'>Yes</font> ✔ <br>

<h4>Video support</h4>

Open <a href='http://html5test.com/'>http://html5test.com/</a> in CEF 3 and go to video section, results as of cefpython3 v0.12:<br>
<br>
video element -	<font color='green'>Yes</font> ✔ <br>
Subtitle support - <font color='green'>Yes</font> ✔ <br>
Poster image support - <font color='green'>Yes</font> ✔ <br>
MPEG-4 support - <font color='red'>No</font> ✘ <br>
H.264 support - <font color='red'>No</font> ✘ <br>
Ogg Theora support - <font color='green'>Yes</font> ✔ <br>
WebM support - <font color='green'>Yes</font> ✔ <br>


<h2>CEF 1</h2>

Support for audio & video was removed from CEF 1, see <a href='https://code.google.com/p/cefpython/issues/detail?id=18'>Issue 18</a>.