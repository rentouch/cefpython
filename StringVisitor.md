Project will move to github. Find this wiki page at the new address: https://github.com/cztomczak/cefpython/wiki/StringVisitor


---


# StringVisitor callbacks #

See [Frame](Frame.md).`GetSource()` and [Frame](Frame.md).`GetText()`.

You must keep a strong reference to the `StringVisitor` object
while visiting strings, otherwise it gets destroyed and the
`StringVisitor` callbacks won't be called.

## CEF 3 ##

bool **Visit**(string value)

> Method that will be executed.