import sys

if 'install' not in sys.argv and 'egg_info' not in sys.argv:
    from .voice import VoiceInput
    from .voice import VoiceOutput

__version__ = '0.0.1'
__author__ = 'Mallikarjunarao Kosuri'
__email__ = 'venkatamallikarjunarao.kosuri@adtran.com'