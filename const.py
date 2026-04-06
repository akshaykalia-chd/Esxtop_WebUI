from pathlib import Path
home = Path.home()
LOG_FILE = f'{home}/esxtop_drill.log'

# Default object name fragments used to filter out ESXi system/background objects.
SYSTEM_OBJECT_PATTERNS = [
    ':system', ':helper', ':drivers', ':ft', ':vmotion', ':init', ':vmsyslogd', ':sh', ':vobd', ':vmkeventd',
    ':vmkdevmgr', ':net-lacp', ':dhclient-uw', ':vmkiscsid', ':nfsgssd', ':busybox', ':ntpd',
    ':vmware-usbarbitrator', ':ioFilterVPServer', ':swapobjd', ':storageRM', ':hostdCgiServer', ':sensord',
    ':net-lbt', ':hostd', ':rhttpproxy', ':slpd', ':net-cdp', ':nscd', ':smartd', ':lwsmd', ':pktcap-agent',
    ':netcpa', ':vdpi', ':logchannellogger', ':logger', ':dcui', ':vpxa', ':fdm', ':vsfwd', ':sfcbd',
    ':sfcb-sfcb', ':sfcb-ProviderMa', ':openwsmand', ':sshd', ':esxtop', ':gzip', ':sdrsInjector', ':timeout'
]
