# -*- coding: iso-8859-1 -*-
# Copyright (C) 2005-2006 Bastian Kleineidam
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""
File and path utilities.
"""

import os
import fnmatch


def write_file (filename, content, backup=False, callback=None):
    """
    Overwrite a possibly existing file with new content. Do this
    in a manner that does not leave truncated or broken files behind.
    @param filename: name of file to write
    @type filename: string
    @param content: file content to write
    @type content: string
    @param backup: if backup file should be left
    @type backup: bool
    @param callback: non-default storage function
    @type callback: None or function taking two parameters (fileobj, content)
    """
    # first write in a temp file
    f = file(filename+".tmp", 'wb')
    if callback is None:
        f.write(content)
    else:
        callback(f, content)
    f.close()
    # move orig file to backup
    if os.path.exists(filename):
        os.rename(filename, filename+".bak")
    # move temp file to orig
    os.rename(filename+".tmp", filename)
    # remove backup
    if not backup and os.path.exists(filename+".bak"):
        os.remove(filename+".bak")


def has_module (name):
    """
    Test if given module can be imported.
    @return: flag if import is successful
    @rtype: bool
    """
    try:
        exec "import %s" % name
	return True
    except ImportError:
        return False


class GlobDirectoryWalker (object):
    # a forward iterator that traverses a directory tree

    def __init__ (self, directory, pattern="*"):
        self.stack = [directory]
        self.pattern = pattern
        self.files = []
        self.index = 0

    def __getitem__ (self, index):
        while True:
            try:
                filename = self.files[self.index]
                self.index += 1
            except IndexError:
                # pop next directory from stack
                self.directory = self.stack.pop()
                self.files = os.listdir(self.directory)
                self.index = 0
            else:
                # got a filename
                fullname = os.path.join(self.directory, filename)
                if os.path.isdir(fullname) and not os.path.islink(fullname):
                    self.stack.append(fullname)
                if fnmatch.fnmatch(filename, self.pattern):
                    return fullname


def rglob (directory, pattern):
    return GlobDirectoryWalker(directory, pattern=pattern)