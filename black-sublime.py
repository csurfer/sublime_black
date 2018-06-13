"""
Sublime Text package to format Python code using `black`
https://github.com/ambv/black formatter.
"""
import sublime
import sublime_plugin


def load_user_settings():
    """Method to procure user settings for black."""
    return sublime.load_settings("black.sublime-settings")


def execute(window, encoding, command, file_name):
    """Command to execute in window."""

    # TODO(vishwas): Once Sublime text starts supporting Python3.6+ extend
    # the same to format view strings in addition to the files. This is
    # currently not possible as any python module imported within plugin
    # would run in Python3.3 which doesn't support `black`.
    if not file_name:
        sublime.message_dialog(
            "Black formatter can currently be run only on saved files."
        )
        return

    # Check to ensure command is run only on python files.
    if not file_name.endswith(".py"):
        sublime.message_dialog(
            "Black formatter can be used to format `.py` files only."
        )
        return

    cmd = []
    # To ensure we don't have any issues with respect to click's
    # http://click.pocoo.org/5/python3/#python-3-surrogate-handling
    if encoding:
        cmd.append(encoding)

    cmd.append(command)
    cmd.append('"{0}"'.format(file_name))
    window.run_command("exec", {"shell_cmd": " ".join(cmd)})


class black_format(sublime_plugin.WindowCommand):
    """Command to format files in place using `black`."""

    def run(self):
        self.settings = load_user_settings()
        self.file_name = self.window.active_view().file_name()

        execute(
            self.window,
            self.settings.get("encoding", None),
            "black -l {0}{1}".format(
                self.settings.get("line_length", 88),
                " -S" if self.settings.get("skip_string_normalization", False) else "",
            ),
            self.file_name,
        )


class black_diff(sublime_plugin.WindowCommand):
    """Command to show what would be different if formatted using `black`."""

    def run(self):
        self.settings = load_user_settings()
        self.file_name = self.window.active_view().file_name()

        execute(
            self.window,
            self.settings.get("encoding", None),
            "black --diff -l {0}{1}".format(
                self.settings.get("line_length", 88),
                " -S" if self.settings.get("skip_string_normalization", False) else "",
            ),
            self.file_name,
        )
