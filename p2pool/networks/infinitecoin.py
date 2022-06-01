from p2pool.bitcoin import networks

PARENT = networks.nets['infinitecoin']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = '1137d5ffc69234ff'.decode('hex')
PREFIX = '1237d5ffc69234ff'.decode('hex')
P2P_PORT = 9392
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 9391
BOOTSTRAP_ADDRS = '8.209.112.218 220.179.77.92 '.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-ifc'
VERSION_CHECK = lambda v: None if 100400 <= v else 'Infinitecoin version too old. Upgrade to 0.10.4 or newer!'
VERSION_WARNING = lambda v: None
