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

from ycmd.completers.shaderlab.Debug import Debug

from ycmd import responses
from ycmd import extra_conf_store
from ycmd.utils import ToCppStringCompatible, ToUnicode
from ycmd.completers.completer import Completer
from ycmd.completers.completer_utils import GetIncludeStatementValue
from ycmd.completers.cpp.flags import Flags, PrepareFlagsForClang
from ycmd.completers.cpp.ephemeral_values_set import EphemeralValuesSet
from ycmd.responses import NoExtraConfDetected, UnknownExtraConf

import xml.etree.ElementTree

SHADER_LAB_FILETYPE = set(['shaderlab'])


logger=Debug.GetLogger()
class ShaderCompleter(Completer):
    def __init__(self, user_options):
        super(ShaderCompleter, self).__init__(user_options)
        logger.info('shader completer , init...')
#         self._completer = ycm_core.ShaderCompleter()
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
        self.PrintRequestData(request_data)
        testlis=['cyc','abc','cyc2']
        return testlis

    def ShouldUseNowInner(self,request_data):
        return True

    def PrintRequestData(self,request_data):
        if not request_data:
            logger.info('not request_data')
        else:
            logger.info('parse request_data')

            line_val=request_data['line_value']
            if line_val:
                logger.info('line val:%s'%line_val)

            codePoint=request_data['start_codepoint']
            if codePoint:
                logger.info('codePoint:%s'%codePoint)

            column_codePint=request_data['column_codepoint']
            if column_codePint:
                logger.info('column codepoint:%s'%column_codePint)

            line_byte=request_data['line_bytes']
            if line_byte:
                logger.info('line_byte:%s'%line_byte)
                logger.info('line_byte str:%s'%(ToUnicode(line_byte)))

            start_column=request_data['start_column']
            if start_column:
                logger.info('start_column:%s'%start_column)
                logger.info('start_column str:%s'%(ToUnicode(start_column)))

            column_num=request_data['column_num']
            if column_num:
                logger.info('column_num:%s'%column_num)
                logger.info('column_num str:%s'%(ToUnicode(column_num)))

            filetype=request_data['filetypes']
            if filetype:
                '''
                [u'shaderlab']
                '''
                logger.info('filetypes:%s'%filetype)

            filepath=request_data['filepath']
            if filepath:
                '''
                file full path
                c://...../...transparent.shader
                '''
                logger.info('filepath:%s'%filepath)


            file_data=request_data['file_data']
            if file_data:
                '''
                {u'filepath':{u'filetypes':'u[shaderlab]',u'contents':'u'xxxshadercontent'}}
                '''
                logger.info('file data...to long')
                logger.info('file data...to long')
#                 logger.info('file_data:%s'%file_data)
#                 logger.info('file_data str:%s'%(ToUnicode(file_data)))

#             line=request_data['line_num']
#             source = request_data[ 'file_data' ][ path ][ 'contents' ]
#             col=request_data['start_codepoint']-1
