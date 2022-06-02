import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fbc0b6db'.decode('hex')
P2P_PORT = 9321
ADDRESS_VERSION = 102
RPC_PORT = 9322
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'infinitecoin' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 524288*100000000 >> (height + 1)//86400
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 30 # s
SYMBOL = 'IFC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Infinitecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Infinitecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.infinitecoin'), 'infinitecoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/ifc/block.dws?'
ADDRESS_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/ifc/address.dws?'
TX_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/ifc/tx.dws?'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
