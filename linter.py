#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Adam Hollett
# Copyright (c) 2017 Adam Hollett
#
# License: MIT
#

"""This module exports the Vale plugin class."""

from SublimeLinter.lint import NodeLinter, util


class Vale(NodeLinter):
    """Provides an interface to vale."""

    defaults = {
        'selector': 'text.plain, text.html.markdown',
    }
    # cmd = 'vale --no-wrap'
    cmd = ('vale', '${args}', '${temp_file}')
    # executable = None
    # version_args = '--version'
    # version_re = r'(?P<version>\d+\.\d+\.\d+)'
    # version_requirement = '>= 0.5.0'
    #regex = (
    #    r'(?P<line>\d+):(?P<col>\d+)\s{2,}'
    #    r'((?P<error>error)|(?P<warning>warning))\s{2,}'
    #    r'(?P<message>.+?)(?=$)'
    #)
    regex = r'.+?(?:[:](?P<line>\d+))(?:[:](?P<col>\d+))?\s+(?P<error>MD\d+)?[/]?(?P<message>.+)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = 'md'
    # error_stream = util.STREAM_BOTH
    error_stream = util.STREAM_STDERR
    word_re = None
    # inline_settings = None
    # inline_overrides = None
    # comment_re = None
