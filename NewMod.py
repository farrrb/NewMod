# Sublime API imports
import sublime
import sublime_plugin

# Custom imports
import os
import datetime
from string import Template

PACKAGE_NAME = "NewMod"
TEMPLATE_DIR = "templates"
BASE_PATH    = os.path.abspath(os.path.dirname(__file__))

# Input handler for capture of the module name
class NewModInputHandler(sublime_plugin.TextInputHandler):

  def __init__(self, view):
    self.view = view

  def name(self):
    return "name"

  def placeholder(self):
    return "File name"

  def initial_text(self):
    return "MyModule"

  def validate(self, name):
    # empty strings and strings containing whitespace(s) are not allowed
    if name == "" or " " in name:
      return False
    # string is valid
    return True

# Main class of the plugin
class NewModCommand(sublime_plugin.TextCommand):

  def input(self, args):
    return NewModInputHandler(self.view)

  def read_template(self, path, mode='r'):
    file = open(path, mode)
    template = file.read()
    file.close()
    return template

  def run(self, edit, name):

    # extract settings
    settings = sublime.load_settings(PACKAGE_NAME + '.sublime-settings')
    encoding = settings.get("encoding")
    syntax   = settings.get("syntax")

    # settings for template creation
    config = settings.get('config')

    # get template files
    template_names = settings.get('templates')

    # generate timestamp
    timestamp = datetime.date.today()
    date      = '{:02d}'.format(timestamp.day) + "." + '{:02d}'.format(timestamp.month) + "." + '{:4d}'.format(timestamp.year)

    # create dictionary
    dic = {}
    dic['name']   = name;
    dic['NAME']   = name.upper()
    dic['date']   = date

    # parse config dictionary and add entries in the template substitution dictionary
    for key in config:
      dic[key.lower()] = config[key]          # key lowercase and value as it is
      dic[key.upper()] = config[key].upper()  # uppercase

    # get current window
    window = self.view.window()

    for tpl in template_names:

      # get file extension from template
      parts = tpl.split(".")
      if len(parts) > 1:
        extension = "." + parts[1]
      else:
        extension = ""

      # read template
      tpl_string = self.read_template(os.path.join(BASE_PATH, TEMPLATE_DIR, tpl))

      # do the template substitution
      tpl_string = Template(tpl_string).safe_substitute(dic)

      # create new file
      view = window.new_file()
      view.set_name(dic['name'] + extension)

      # set options
      if encoding:
        view.set_encoding(encoding)

      # set syntax if available
      if syntax:
        view.set_syntax_file(syntax)

      view.insert(edit, 0, tpl_string)
