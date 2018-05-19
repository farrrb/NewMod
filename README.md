NewMod
======

A Sublime Text 3 Plugin.

The purpose of NewMod is to create new source (and / or) header files for your language of choice. For now
only one language at a time is allowed. I plan to alter the code in order to support multiple languages.

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
3. Type in your module name (note: whitespaces are note allowed!) and confirm with `ENTER`
4. Done

Predefined Symbols
------------------

For now there are three predefined symbols:
- `${name}` - the name you typed for the new module (e.g. MyModule)
- `${NAME}` - the same thing as above, but in uppercase
- `${date}` - the date in the format DD.MM.YYYY

User-defined Symbols
--------------------

For each entry in the configuration (e.g. "author") the plugin creates automatically two symbols for you,
which can be used in the template.
1. `${your_symbol}`
2. `${YOUR_SYMBOL}`

For example if you add the following code to your user configuration

```
// NewMod Settings - User
{
  "config" :
  {
     "co_author": "John Doe" ,
  }
}
```
the plugin will automatically create
1. `${co_author}` - "John Doe"
2. `${CO_AUTHOR}` - "JOHN DOE"
