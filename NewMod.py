import sublime
import sublime_plugin

PACKAGE_NAME = "NewMod"

class NewModCommand(sublime_plugin.TextCommand):
  def run(self, edit, text):
    settings = sublime.load_settings(PACKAGE_NAME + '.sublime-settings')
    encoding = settings.get("encoding", "UTF-8")
    syntax   = settings.get("syntax",   "C.sublime-syntax")

    # get current window
    window = self.view.window()

    # create new file
    window.new_file()

    # get active active_view
    active_view = window.active_view()

    # set options
    active_view.set_encoding(encoding)
    active_view.set_syntax_file(syntax)

    print(text)

  def input(self, args):
    return sublime_plugin.TextInputHandler()

