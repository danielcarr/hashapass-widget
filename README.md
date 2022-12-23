# Hashapass Widget

A cross-platform GUI implementation of the [hashapass](http://hashapass.com/en/about.html) password generator, with extensions for more complex passwords.

I've been using a lightly modified version of the script recommended on the hashapass [website](http://hashapass.com/en/cmd.html) for years so that I can use unguessable and unique passwords without a proprietary password manager.

The original implementation is hardcoded to 8 character long passwords, but many websites require more than that (which is also generally a good thing), so I've extended it to allow for variable password length. I also send the output straight to the clipboard so that I don't have to copy it after generating it (which means showing it on screen can also be optional).

This is a GUI widget to replace and improve upon the terminal instance running a script I have been using. But the generated passwords will be compatible.

## See also
- The [Hashapass website](http://hashapass.com).
- My modified [script](https://gist.github.com/danielcarr/6fd7f55d070248f91f60) version.
- My (very WIP) implementation of [the same thing as a Gtk3 panel applet](https://github.com/danielcarr/PasswordGeneratorApplet/blob/master/password-generator-applet.py) for the Mate desktop environment. 
