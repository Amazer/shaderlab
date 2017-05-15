# shaderlab completer by Amazer
# Auther Amazer
# 2017.5.14

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import *  # noqa

from ycmd.completers.shaderlab.shaderlab_completer import ShaderCompleter

def GetCompleter( user_options ):
  return ShaderCompleter( user_options )

