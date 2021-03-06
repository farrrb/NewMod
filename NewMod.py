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

  def create_dictionary(self, name, date, time, subst):
    # create dictionary
    dic = {}
    dic['name'] = name;
    dic['NAME'] = name.upper()
    dic['date'] = date
    dic['time'] = time

    # parse substitution dictionary and add entries in the template substitution dictionary
    if subst is not None:
      for key in subst:
        dic[key.lower()] = subst[key]          # key lowercase and value as it is
        dic[key.upper()] = subst[key].upper()  # uppercase

    return dic

  def substitute_template(self, path, dic):
    try:
      # open the file in read only mode
      file = open(path, 'r')
      template = file.read()
      file.close()
      # do the template substitution
      template = Template(template).safe_substitute(dic)

      return template
    except IOError:
      self.throw_error("Couldn't open template file \"" + path + "\"")

  def set_options(self, view, encoding, syntax):
    # set options
    if encoding:
      view.set_encoding(encoding)

    # set syntax if available
    if syntax:
      view.set_syntax_file(syntax)

  def throw_error(self, error_message):
    sublime.error_message("NewMod:\n" + error_message)

  def run(self, edit, name, type):
    # extract settings
    settings    = sublime.load_settings(PACKAGE_NAME + '.sublime-settings')
    encoding    = settings.get("encoding",            "UTF-8")
    syntax      = settings.get(type + "_syntax",      "")
    date_format = settings.get("date_format",         "%d.%m.%Y")
    time_format = settings.get("time_format",         "%H:%M")
    subst       = settings.get("substitutions")

    # get template files
    template_names = settings.get(type + "_templates", "")

    # generate date
    now   = datetime.datetime.now()
    date  = now.strftime(date_format)
    time  = now.strftime(time_format)

    # generate name: prefix + name + suffix
    name = settings.get(type + "_prefix", "") + name + settings.get(type + "_suffix", "")

    # generate dictionary
    dic = self.create_dictionary(name, date, time, subst)

    # get current window
    window = self.view.window()

    # iterate over every template
    if len(template_names):
      for tpl in template_names:
        # get file extension from template
        parts = tpl.split(".")
        if len(parts) > 1:
          extension = "." + parts[-1]
        else:
          extension = ""

        # read template & do text substitution
        path  = os.path.join(BASE_PATH, TEMPLATE_DIR, type, tpl)
        tpl_string = self.substitute_template(path, dic)

        # create new file (in a new tab)
        view = window.new_file()
        view.set_name(name + extension)

        # set options to the new view
        self.set_options(view, encoding, syntax)

        view.insert(edit, 0, tpl_string)
    else:
      self.throw_error("No template files were found, please check your configuration.")
