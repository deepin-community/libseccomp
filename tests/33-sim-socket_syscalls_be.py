#!/usr/bin/env python

#
# Seccomp Library test program
#
# Copyright (c) 2016 Red Hat <pmoore@redhat.com>
# Author: Paul Moore <paul@paul-moore.com>
#

#
# This library is free software; you can redistribute it and/or modify it
# under the terms of version 2.1 of the GNU Lesser General Public License as
# published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library; if not, see <http://www.gnu.org/licenses>.
#

import argparse
import sys

import util

from seccomp import *

def test(args):
    f = SyscallFilter(KILL)
    f.remove_arch(Arch())
    f.add_arch(Arch("s390"))
    f.add_arch(Arch("s390x"))
    f.add_arch(Arch("ppc"))
    f.add_rule(ALLOW, "socket")
    f.add_rule(ALLOW, "connect")
    f.add_rule(ALLOW, "accept")
    f.add_rule(ALLOW, "accept4")
    f.add_rule(ALLOW, "shutdown")
    return f

args = util.get_opt()
ctx = test(args)
util.filter_output(args, ctx)

# kate: syntax python;
# kate: indent-mode python; space-indent on; indent-width 4; mixedindent off;
