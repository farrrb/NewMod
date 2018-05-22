NewMod
======
A Sublime Text 3 plugin for creating new (empty) modules.

The purpose of NewMod is to create new source (and / or) header files for your language of choice. It is
extensible so you can add your languages of choice to the module. For now the default languages that are
supported are:
- C
- C++
- Default (Plain Text)
- Python

Installation Instructions
-------------------------

*Github*

1. Open Sublime Text 3
2. In the menu bar click on `Preferences` and then on `Browse Packages` to go into the "Packages" directory
3. Open a terminal in this folder in order to clone the Github repository
4. Type `$ git clone https://github.com/farrrb/NewMod.git` in your terminal and press `ENTER`
5. Done


Usage
-----

1. Open the Command Palette (Windows / Linux: `CTRL + SHIFT + P` / Mac: `CMD + SHIFT + P`)
2. Enter `NewMod: Create` and press `ENTER`
3. Type in your module name (note: whitespaces are not allowed!) and confirm with `ENTER`
4. Done

Predefined Symbols
------------------
For now there are the following predefined symbols:

- `${name}` - the name you typed for the new module (e.g. MyModule)
- `${NAME}` - the same thing as above, but in uppercase
- `${date}` - today's date
- `${time}` - the current time

User-defined Symbols
--------------------
For each entry in the substitution configuration (e.g. "author") the plugin
automatically creates two symbols for you, which can be used in the template:

1. `${your_symbol}`
2. `${YOUR_SYMBOL}`

For example if you add the following code to your user configuration

```
// NewMod Settings - User
{
  "substitutions" :
  {
     "author": "John Doe" ,
  }
}
```
the plugin will automatically create:
1. `${author}` (expands to "John Doe")
2. `${AUTHOR}` (expands to "JOHN DOE")

Date and Time Formats
---------------------
The date and the current time will be formatted using pythons strftime() function.
If you want to customize the behavior of `${date}` or `${time}`, take a look at this
[link](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior)
for further information.

The default format string for the date is `"$d.%m.%Y"` which expands to DD.MM.YYYY (e.g. 19.05.2018).

The default format string for the current time is `"%H:%M` which expands to HH.MM (e.g. 22:47).
