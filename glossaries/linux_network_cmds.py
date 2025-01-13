glossary = {
    # Network Commands
    'ping':                 'Check the connectivity between two devices. \n\t\t'
                            'Syntax: ping [-aAbBdDfhLnOqrRUvV46] [-c count] [-F flowlabel] \n\t\t'
                            '[-i interval] [-I interface] [-l preload] [-m mark] \n\t\t'
                            '[-M pmtudisc_option] [-N nodeinfo_option] [-w deadline] \n\t\t'
                            '[-W timeout] [-p pattern] [-Q tos] [-s packetsize] [-S sndbuf] \n\t\t'
                            '[-t ttl] [-T timestamp option] [hop...] {destination} \n\t\t'
                            '-D: "Don\'t fragment." Used to test the PMTU of the hops along the route.',

    'traceroute':           'Trace the network route from hop to hop from the host to the desired \n\t\t'
                            'destination. \n\t\t'
                            'Syntax: traceroute [-46dFITUnreAV] [-f first_ttl] [-g gate,...] \n\t\t'
                            '[-i device] [-m max_ttl] [-p port] [-s src_addr] [-q nqueries] \n\t\t'
                            '[-N squeries] [-t tos] [-l flow_label] [-w waittimes] [-z sendwait] \n\t\t'
                            '[-UL] [-D] [-P proto] [--sport=port] [-M method] \n\t\t'
                            '[--mtu] [--back] host [packet_len]',

    'tracepath':            'Traces path to a network host discovering MTU along the way. \n\t\t'
                            'Syntax: tracepath [-4] [-6] [-n] [-b] [-l pktlen] [-m max_hops] \n\t\t'
                            '[-p port] [-V] {destination} \n\t\t'
                            '-4: Use IP4 only. \n\t\t'
                            '-6: Use IP6 only. \n\t\t'
                            '-n: Print primarily IP addresses numerically. \n\t\t'
                            '-b: Print both host names and IP addresses. \n\t\t'
                            '-l pktlen: Specifies packet length: replaces IP4: 65535 IP6: 128000 \n\t\t'
                            '-m max_hops: Sets TTL to something other than default 30. \n\t\t'
                            '-p port: Sets initial destination port. \n\t\t'
                            '-V: Prints version and exits.',

    'ifconfig':             'Configure, debug, and tune the kernel network interfaces. \n\t\t'
                            'Being sidestepped for ip addr.',

    'iptables':             'Create rules for IP packet filtering. \n\t\t'
                            'Typical filter types include: \n\t\t'
                            '- Packet type \n\t\t'
                            '- Packet source \n\t\t'
                            '- Target: Specifies the action to be taken on matching packets. \n\t\t'
                            'Common Syntax: \n\t\t'
                            'iptables [-t <table-name>] <command> <chain-name> <parameter-1> \\\n\t\t'
                            '<option-1> <parameter-n> <option-n>',

    'ip addr':              'Very similar to ifconfig but more modern.',

    'arp':                  'Displays IP to MAC address mappings for hosts in the ARP cache. \n\t\t'
                            '-a: Displays current ARP entries in the host\'s ARP table. \n\t\t'
                            '-n: Displays network addresses as numbers instead of symbols. \n\t\t'
                            '-i interface: Limits the ARP command to a specific interface. \n\t\t'
                            '-d: Deletes an entry for a host. Using * will delete all. \n\t\t'
                            '-s: Statically adds an entry. Requires both hostname and eth_addr. \n\t\t'
                            'ifscope interface: Limits the ARP call to a specific interface. \n\t\t'
                            'temp: Used with -s, specifies a temporary static ARP entry. \n\t\t'
                            'reject: Traffic to this destination is rejected, and sender is notified. \n\t\t'
                            'blackhole: Similar to reject, but sender is not notified. \n\t\t'
                            '-f filename: Imports ARP entries from a file. Format: hostname eth_addr.',

    'netstat':              'Shows information about active ports and their state. \n\t\t'
                            'Run without flags is the same as -a. \n\t\t'
                            '-a: Shows all connections and listening ports. \n\t\t'
                            '-p protocol: Specifies a protocol. \n\t\t'
                            '-s: Displays network statistics. \n\t\t'
                            '-t: Displays only TCP sessions. \n\t\t'
                            '-u: Displays only UDP sessions.',

    'nslookup':             'Displays DNS information. Useful for mapping names to IP addresses.',

    'dig':                  'Replacement for nslookup. Displays more detailed information.',

    'host':                 'Resolves FQDNs to IP addresses.',

    'whois':                'Displays ownership information for a domain or block of IP addresses.',

    'route':                'Displays the current routing table on a host. \n\t\t'
                            'Can add or remove routes or create static routes.',

    'scp':                  'Secure Copy Protocol. Securely copies files between servers using SSH \n\t\t'
                            'for authentication and encryption.',

    'ftp':                  'Copies files from one host to another. Data is in clear text. \n\t\t'
                            'Use sftp for encrypted transfers.',

    'tftp':                 'Transfers files between a client and a server.',

    'finger':               'Displays information about users on a remote system, including username \n\t\t'
                            'and last login.',

    'nmap':                 'Scans networks for hosts and open ports. \n\t\t'
                            'Common Syntax: nmap [Scan Type(s)] [Options] {target specifications}.',

    'tcpdump':              'Displays TCP/IP and other network packets flowing through the system. \n\t\t'
                            'Common Syntax: tcpdump [-adeflnNOpqRStuvxX] [ -c count] [ -C file_size] \n\t\t'
                            '[ -F file] [ -i interface] [ -m module] [ -r file] [ -s snaplen] \n\t\t'
                            '[ -T type] [ -U user] [ -w file] [ -E algo:secret] [ expression].',

    'telnet/ssh':           'Provides remote access via a terminal interface. \n\t\t'
                            'Telnet is in clear text, while SSH is encrypted (usually with AES).',
}

