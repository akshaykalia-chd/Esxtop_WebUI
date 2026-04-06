from pathlib import Path
home = Path.home()
LOG_FILE = f'{home}/esxtop_drill.log'

# Data source and parsing defaults
COUNTER_MAP_FILE = 'c_map.csv'
TIME_COLUMN_NAME = '(PDH-CSV 4.0) (UTC)(0)'
CSV_ENCODINGS = ['ISO-8859-1']
SUPPORT_CONTACT = 'akshay.kalia@broadcom.com'

# Fault finder domain values
COUNTER_TYPE_BOOL = 'Bool'
COUNTER_TYPE_NUM_CAL = 'Num_cal'
COUNTER_SCOPE_OBJ_HIGHER_IS_BETTER = 'obj_hig'
SPECIAL_COUNTER_VM_WAIT = '% VmWait'
SPECIAL_COUNTER_ADAPTER_Q_DEPTH = 'Adapter Q Depth'
SPECIAL_COUNTER_COMMANDS_PER_SEC = 'Commands/sec'
HBA_OVERLOAD_MESSAGE = 'Possible HBA overload'

# Default object name fragments used to filter out ESXi system/background objects.
SYSTEM_OBJECT_PATTERNS = [
    ':system', ':helper', ':drivers', ':ft', ':vmotion', ':init', ':vmsyslogd', ':sh', ':vobd', ':vmkeventd',
    ':vmkdevmgr', ':net-lacp', ':dhclient-uw', ':vmkiscsid', ':nfsgssd', ':busybox', ':ntpd',
    ':vmware-usbarbitrator', ':ioFilterVPServer', ':swapobjd', ':storageRM', ':hostdCgiServer', ':sensord',
    ':net-lbt', ':hostd', ':rhttpproxy', ':slpd', ':net-cdp', ':nscd', ':smartd', ':lwsmd', ':pktcap-agent',
    ':netcpa', ':vdpi', ':logchannellogger', ':logger', ':dcui', ':vpxa', ':fdm', ':vsfwd', ':sfcbd',
    ':sfcb-sfcb', ':sfcb-ProviderMa', ':openwsmand', ':sshd', ':esxtop', ':gzip', ':sdrsInjector', ':timeout'
]
