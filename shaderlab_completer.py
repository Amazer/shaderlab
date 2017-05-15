from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from builtins import *  # noqa
from future.utils import iteritems

from collections import defaultdict
import ycm_core
import re
import os.path
import textwrap
import io
from ycmd import responses
from ycmd import extra_conf_store
from ycmd.utils import ToCppStringCompatible, ToUnicode
from ycmd.completers.completer import Completer
from ycmd.completers.completer_utils import GetIncludeStatementValue
from ycmd.completers.cpp.flags import Flags, PrepareFlagsForClang
from ycmd.completers.cpp.ephemeral_values_set import EphemeralValuesSet
from ycmd.responses import NoExtraConfDetected, UnknownExtraConf

import xml.etree.ElementTree
import vim

SHADER_LAB_FILETYPE = set(['shaderlab'])


class ShaderCompleter(Completer):
    def __init__(self, user_options):
        super(ShaderCompleter, self).__init__(user_options)
        self._completer = ycm_core.ShaderCompleter()
        '''
         self._files_being_compiled = EphemeralValuesSet()
        '''

    def SupportedFiletypes(self):
        return SHADER_LAB_FILETYPE

    def Shutdown(self):
#         vim.eval("")
        print('shaderlab completer shutdown')

    '''
    _TranslateRequestForJediHTTP
    path = request_data[ 'filepath' ]
    source = request_data[ 'file_data' ][ path ][ 'contents' ]
    line = request_data[ 'line_num' ]
    col = request_data[ 'start_codepoint' ] - 1
    return {
      'source': source,
      'line': line,
      'col': col,
      'source_path': path
    }
    '''
    def ComputeCandidatesInner(self, request_data):
        print ('ComputeCandidatesInner, request_data:%s'% request_data)
        if not request_data:
            return []
        testlis=['cyc','abc','cyc2']
        return testlis

#     def ShouldUseNowInner(self,request_data):
#         pass
#         print "ComputeCandidatesInner, request_data: %s" % request_data
