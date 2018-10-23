"""
Sublime Text package to format Python code using `black`
https://github.com/ambv/black formatter.
"""
import filecmp
import logging
import os
import sublime
import sublime_plugin
import shutil
import sys
import zipfile


#: name of the plugin
PLUGIN_NAME = "sublime_black"
#: path where the plugin is meant to be installed
INSTALLED_PLUGIN_NAME = "{0}.sublime-package".format(PLUGIN_NAME)
#: package installation path
PACKAGES_PATH = sublime.packages_path()
#: plugin installation path
PLUGIN_PATH = os.path.join(PACKAGES_PATH, PLUGIN_NAME)
#: path of the plugin file
INSTALLED_PLUGIN_PATH = os.path.abspath(os.path.dirname(__file__))
#: settings filename
SETTINGS = "black.sublime-settings"

logger = logging.getLogger(__name__)

sys.path.insert(0, PLUGIN_PATH)


def plugin_loaded():
    """Execute when Plugin is loaded.
    Make sure all Plugin files are in the main package directory of Sublimetext.
    This is mainly for the default settings file.
    """
    if INSTALLED_PLUGIN_PATH != PLUGIN_PATH:
        # check if installed plugin is the same as this file
        installed_plugin_path = os.path.join(PLUGIN_PATH, INSTALLED_PLUGIN_NAME)
        if os.path.exists(installed_plugin_path) and filecmp.cmp(
            installed_plugin_path, INSTALLED_PLUGIN_PATH
        ):
            return

        # remove old package data
        if os.path.exists(PLUGIN_PATH):
            try:
                shutil.rmtree(PLUGIN_PATH)
            except:  # noqa: E722
                logger.error("Could not remove old Plugin directory")

        # create new plugin dir
        if not os.path.exists(PLUGIN_PATH):
            os.mkdir(PLUGIN_PATH)

        z = zipfile.ZipFile(INSTALLED_PLUGIN_PATH, "r")
        for f in z.namelist():
            z.extract(f, PLUGIN_PATH)
        z.close()

    shutil.copyfile(INSTALLED_PLUGIN_PATH, installed_plugin_path)


def load_user_settings():
    """Method to procure user settings for black."""
    return sublime.load_settings(SETTINGS)


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
