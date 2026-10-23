---
url: https://docs.cloud.google.com/vpc/docs/ts-vm-vm-internal/
title: Troubleshoot internal connectivity between VMs \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:28.483443+00:00
---

# Troubleshoot internal connectivity between VMs  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/ts-vm-vm-internal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot internal connectivity between VMs

This document provides troubleshooting steps for connectivity issues between Compute Engine VMs that are in the same Virtual Private Cloud (VPC) network (either Shared VPC or standalone) or two VPC networks connected with VPC Network Peering. It assumes that the VMs are communicating using the internal IP addresses of their respective virtual network interface controllers (vNICs).

The steps in this guide apply to both Compute Engine VMs and Google Kubernetes Engine nodes.

If you would like to see specific additional troubleshooting scenarios, click the **Send feedback** link at the bottom of the page and let us know.

The following VM and VPC configurations are applicable to this guide:

  * VM-to-VM connections using internal IP addresses in a single VPC network.
  * VM-to-VM connections using internal IP addresses within a Shared VPC network.
  * VM-to-VM connections using internal IP addresses in different VPC networks peered using VPC Network Peering.



Commands used in this guide are available on all Google-provided OS images. If you are using your own OS image, you might have to install the tools.

**Note:** When troubleshooting, it's useful to record the commands you run and the results you get in a document. You can use this document to check your own work and to let others know what you've researched. In addition, if you do need to open a support ticket, the document can speed up resolving your issue.

## Quantify the problem

  * If you think you have complete packet loss, go to Troubleshoot complete connection failure.
  * If you are experiencing latency, only partial packet loss, or timeouts occurring mid-connection, go to Troubleshoot network latency or loss causing throughput issues.



## Troubleshoot complete connection failure

The following sections provide steps for troubleshooting complete internal connectivity failure between VMs. If you are instead experiencing increased latency or intermittent connection timeouts, skip to Troubleshoot network latency or loss causing throughput issues.

### Determine connection values

First gather the following information:

  * From the [VM instances page](https://console.cloud.google.com/compute/instances), gather the following for both VMs: 
    * VM names
    * VM zones
    * Internal IP addresses for the vNICs that are communicating
  * From the configuration of the destination server software, gather the following information:

    * Layer 4 protocol
    * Destination port

For example, if your destination is an HTTPS server, the protocol is TCP and the port is usually `443`, but your specific configuration might use a different port.




If you're seeing issues with multiple VMs, pick a single source and single destination VM that are experiencing issues and use those values. In general, you shouldn't need the source port of the connection.

Once you have this information, proceed to Investigate issues with the underlying Google network.

### Investigate issues with the underlying Google network

If your setup is an existing one that hasn't changed recently, then the issue might be with the underlying Google network. Check the Network Intelligence Center [](https://console.cloud.google.com/net-intelligence/performance/dashboard/packet-loss)[Performance Dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard) for [packet loss](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/using-performance-dashboard#packet-loss) between the VM zones. If there is an increase in packet loss between the zones during the timeframe when you experienced network timeouts, it might indicate that the problem was with the physical network underlying your virtual network. Check the [Google Cloud Status Dashboard](https://status.cloud.google.com) for known issues before filing a support case.

If the issue does not seem to be with the underlying Google network, proceed to Check for misconfigured Google Cloud firewall rules.

### Check for misconfigured firewall rules in Google Cloud

**Note:** This section uses Connectivity Tests, which can incur charges. For pricing details, see [Network Intelligence Center pricing](https://cloud.google.com/network-intelligence-center/pricing).

Connectivity Tests analyzes the VPC network path configuration between two VMs and shows whether the programmed configuration _should_ allow the traffic or not. If the traffic is not allowed, the results show whether a Google Cloud egress or ingress firewall rule is blocking the traffic or if a route isn't available.

Connectivity Tests might also dynamically test the path by sending packets between the hypervisors of the VMs. If these tests are performed, then the results of those tests are displayed.

Connectivity Tests examines the configuration of the VPC network only. It does not test the operating system firewall or operating system routes or the server software on the VM.

The following procedure runs Connectivity Tests from Google Cloud console. For other ways to run tests, see [Running Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests#running-conn-test).

Use the following procedure to create and run a test:

  1. In the Google Cloud console, go to the **Connectivity Tests** page.

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. In the project pull-down menu, confirm you are in the correct project or specify the correct one.

  3. Click **Create connectivity test**.

  4. Give the test a name.

  5. Specify the following:

     1. Protocol
     2. Source endpoint IP address
     3. Source project and VPC network
     4. Destination endpoint IP address
     5. Destination project and VPC network
     6. Destination port
  6. Click **Create**.




The test runs immediately. To see the result diagram, click **View** in the in the **Result details** column.

  * If the results say the connection is dropped by a Google Cloud firewall rule, determine if your intended security setup _should_ allow the connection. You might have to ask your security or network administrator for details. If the traffic should be allowed, then check the following: 
    * Check the [Always blocked traffic](https://docs.cloud.google.com/vpc/docs/firewalls#blockedtraffic) list. If the traffic is blocked by Google Cloud as described in the always blocked traffic list, then your existing configuration won't work.
    * [Go to the Firewall policies page](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list) and review your firewall rules. If the firewall is misconfigured, create or modify a firewall rule to allow the connection. This rule can be a [VPC firewall rule](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) or a [hierarchical firewall policy rule](https://docs.cloud.google.com/vpc/docs/using-firewall-policies#create-policy).
  * If there is a correctly configured firewall rule that blocks this traffic, check with your security or network administrator. If the security requirements of your organization mean that the VMs shouldn't reach each other, you might need to redesign your setup.
  * If the results indicate that there are no issues with the VPC connectivity path, then the issue might be one of the following. 
    * Issues with the guest OS configuration, such as issues with firewall software.
    * Issues with the client or server applications, such as the application being frozen or configured to listen on the wrong port.



Subsequent steps walk you through examining each of these possibilities. Continue with Test TCP connectivity from inside the VM.

### Test TCP connectivity from inside the VM

If your VM-VM Connectivity Test did not detect a VPC configuration issue, start testing OS-OS connectivity. The following steps help you determine the following:

  * If a TCP server is listening at the indicated port
  * If the server-side firewall software is allowing connections to that port from the client VM
  * If the client-side firewall software is allowing connections to that port on the server
  * If the server-side route table is correctly configured to forward packets
  * If the client-side route table is correctly configured to forward packets



You can test the TCP handshake using `curl` with Linux or Windows 2019, or using the `New-Object System.Net.Sockets.TcpClient` command with Windows Powershell. The workflow in this section should result in one of the following outcomes: connection success, connection timeout, or connection reset.

  * **Success:** If the TCP handshake completes successfully, then an OS firewall rule is not blocking the connection, the OS is correctly forwarding packets, and a server of some kind is listening on the destination port. If this is the case, then the issue might be with the application itself. To check, see Check server logging for information about server behavior.
  * **Timeout:** If your connection times out, it usually means one of the following: 
    * There's no machine at that IP address
    * There's a firewall somewhere silently discarding your packets
    * OS packet routing is sending the packets to a destination that can't process them, or asymmetric routing is sending the return packet on an invalid path
  * **Reset:** If the connection is being reset, it means that the destination IP is receiving packets, but an OS or an application is rejecting the packets. This can mean one of the following:

    * The packets are arriving at the wrong machine and it is not configured to respond to that protocol on that port
    * The packets are arriving at the correct machine, but no server is listening on that port
    * The packets are arriving at the correct machine and port, but higher level protocols (such as SSL) aren't completing their handshake
    * A firewall is resetting the connection. This is less likely than a firewall silently discarding the packets, but it can happen.



###  Linux 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Ensure that there is a [firewall rule that allows SSH connections from IAP](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#create-firewall-rule) to your VM or create a new one.

  3. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  4. Find your source VM.

  5. Click **SSH** in the **Connect** column for that VM.

  6. From the client machine command line, run the following command. Replace DEST_IP:DEST_PORT with your destination IP address and port.
         
         curl -vso /dev/null --connect-timeout 5 DEST_IP:DEST_PORT
         




###  Windows 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Find your source VM.

  3. Use one of the methods described in [Connecting to Windows VMs](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) to connect to your VM.

  4. From the client machine command line, run the following:

     * Windows 2019:   

           
           curl -vso /dev/null --connect-timeout 5 DEST_IP:DEST_PORT
           

     * Windows 2012 or Windows 2016 Powershell:   

           
           PS C:> New-Object System.Net.Sockets.TcpClient('DEST_IP',DEST_PORT)`
           




#### Connection success

The following results indicate a successful TCP handshake. If the TCP handshake completes successfully, then the issue is not related to TCP connection timeout or reset. Instead, the timeout issue is occurring within the application layers. If you get a successful connection, proceed to Check server logging for information about server behavior.

###  Linux and Windows 2019 
    
    
    $ curl -vso /dev/null --connect-timeout 5 192.168.0.4:443
    

The "Connected to" line indicates a successful TCP handshake.
    
    
    Expire in 0 ms for 6 (transfer 0x558b3289ffb0)
    Expire in 5000 ms for 2 (transfer 0x558b3289ffb0)
      Trying 192.168.0.4...
    TCP_NODELAY set
    Expire in 200 ms for 4 (transfer 0x558b3289ffb0)
    Connected to 192.168.0.4 (192.168.0.4) port 443 (#0)
    > GET / HTTP/1.1
    > Host: 192.168.0.4:443
    > User-Agent: curl/7.64.0
    > Accept: */*
    >
    Empty reply from server
    Connection #0 to host 192.168.0.4 left intact
    

###  Windows 2012 and 2016 
    
    
    PS C:\> New-Object System.Net.Sockets.TcpClient('DEST_IP_ADDRESS', PORT)
    

Connection successful result. The "Connected: True" line is relevant.
    
    
    Available           : 0
    Client              : System.Net.Sockets.Socket
    Connected           : True
    ExclusiveAddressUse : False
    ReceiveBufferSize   : 131072
    SendBufferSize      : 131072
    ReceiveTimeout      : 0
    SendTimeout         : 0
    LingerState         : System.Net.Sockets.LingerOption
    NoDelay             : False
    

#### Connection timeout

The following results indicate that the connection has timed out. If your connection is timing out, proceed to Verify server IP address and port.

###  Linux and Windows 2019 
    
    
    $ curl -vso /dev/null --connect-timeout 5 DEST_IP_ADDRESS:PORT
    

Connection timeout result:
    
    
    Trying 192.168.0.4:443...
    Connection timed out after 5000 milliseconds
    Closing connection 0
    

###  Windows 2012 and 2016 
    
    
    PS C:\> New-Object System.Net.Sockets.TcpClient('DEST_IP_ADDRESS', PORT)
    

Connection timeout result:
    
    
    New-Object: Exception calling ".ctor" with "2" argument(s): "A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond. 192.168.0.4:443"
    

#### Connection reset

A reset is when a device sends a RST packet back to the client, informing the client that the connection has been terminated. The connection might be reset for one of the following reasons:

  * The receiving server was not configured to accept connections for that protocol on that port. This could be because the packet was sent to the wrong server or the wrong port, or the server software was misconfigured.
  * Firewall software rejected the connection attempt



If the connection was reset, proceed to Verify that you are accessing the correct IP address and port.

###  Linux and Windows 2019 
    
    
    $ curl -vso /dev/null --connect-timeout 5 DEST_IP_ADDRESS:PORT
    

Connection reset result:
    
    
    Trying 192.168.0.4:443...
    connect to 192.168.0.4 port 443 failed: Connection refused
    Failed to connect to 192.168.0.4 port 443: Connection refused
    Closing connection 0
    

###  Windows 2012 and 2016 
    
    
    PS C:\> New-Object System.Net.Sockets.TcpClientt('DEST_IP_ADDRESS', PORT)
    

Connection reset result:
    
    
    New-Object: Exception calling ".ctor" with "2" argument(s): "No connection could be made because the target machine actively refused it. 192.168.0.4:443"
    

### Verify server IP address and port

Run one of the following commands on your server. They indicate if there is a server listening on the necessary port.

###  Linux 
    
    
    $ sudo netstat -ltuvnp
    

The output shows that a TCP server is listening to any destination IP address (`0.0.0.0`) at port 22, accepting connections from any source address (`0.0.0.0`) and any source port (`*`). The _PID/Program name_ column specifies the executable bound to the socket.
    
    
    Active Internet connections (only servers)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
    tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      588/sshd
    tcp6       0      0 :::22                   :::*                    LISTEN      588/sshd
    udp        0      0 0.0.0.0:68              0.0.0.0:*                           334/dhclient
    udp        0      0 127.0.0.1:323           0.0.0.0:*                           429/chronyd
    udp6       0      0 ::1:323                 :::*                                429/chronyd
    

###  Windows 

**Note:** If you are using a UDP based server, Windows also offers the "Get-NetUdpEndpoint" command.
    
    
    PS C:\> Get-NetTcpConnection -State "LISTEN" -LocalPort DEST_PORT
    

Output shows results of command run with DEST_PORT set to `443`. This output shows that a TCP server is listening to any address (`0.0.0.0`) at port `443`, accepting connections from any source address (`0.0.0.0`) and any source port (`0`). The _OwningProcess_ column indicates the process ID of the process listening to the socket.
    
    
    LocalAddress LocalPort RemoteAddress RemotePort State  AppliedSetting OwningProcess
    ------------ --------- ------------- ---------- -----  -------------- -------------
    ::           443       ::            0          Listen                928
    0.0.0.0      443       0.0.0.0       0          Listen                928
    

If you see that the server is not bound to the correct port or IP, or that the remote prefix does not match your client, consult the server's documentation or vendor to resolve the issue. The server must be bound to the IP address of a particular interface or to `0.0.0.0`, and it must accept connections from the correct client IP prefix or `0.0.0.0`.

If the application server is bound to the correct IP address and port, it might be that the client is accessing the wrong port, that a higher-level protocol (frequently TLS) is actively refusing the connection, or that there is a firewall rejecting the connection.

Check that the client and server are using the same TLS version and encryption formation.

Check that your client is accessing the correct port.

If the preceding steps don't resolve the problem, proceed to Check firewall on client and server for packet discards.

### Check firewall on client and server for packet discards

If the server is unreachable from the client VM but is listening on the correct port, one of the VMs might be running firewall software that is discarding packets associated with the connection. Check the firewall on both the client and server VMs using the following commands.

If a rule is blocking your traffic, you can update the firewall software to allow the traffic. If you do update the firewall, proceed cautiously as you prepare and execute the commands because a misconfigured firewall can block unexpected traffic. Consider setting up [VM Serial Console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console) access before proceeding.

###  Linux iptables 

Check packet counts for the number of packets processed for each installed iptables chain and rule. Determine which DROP rules are being matched against by comparing source and destination IP addresses and ports with the prefixes and ports specified by iptables rules.

If a matched rule is showing increasing discards with connection timeouts, consult the iptables documentation to apply the correct `allow` rule to the appropriate connections.
    
    
    $ sudo iptables -L -n -v -x
    

This example INPUT chain shows that packets from any IP address to any IP address using destination TCP port `5000` will be discarded at the firewall. The pkts column indicates that the rule has dropped 10342 packets. As a test, if you create connections that are discarded by this rule, you will see the pkts counter increase, confirming the behavior.
    
    
    Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
     pkts   bytes  target prot opt in  out  source      destination
    10342 2078513    DROP  tcp  --  *  *    0.0.0.0/0   0.0.0.0/0 tcp dpt:5000
    

You can add an ingress or egress rule to iptables with the following commands:

Ingress rule:
    
    
    $ sudo iptables -A INPUT -p tcp -s SOURCE_IP_PREFIX --dport SERVER_PORT -j ACCEPT
    

Egress rule:
    
    
    $ sudo iptables -A OUTPUT -p tcp -d DEST_IP_PREFIX --dport DEST_PORT -j ACCEPT
    

###  Windows Firewall 

Check in _Windows Firewall_ that the connection is permitted to egress from the client and ingress to the server. If a rule is blocking your traffic, make the needed corrections in Windows Firewall to allow the connections. You can also enable Windows Firewall Logging.

The default DENY behavior of Windows Firewall is to silently discard denied packets, resulting in timeouts.

This command checks the server. To check the egress rules on the client VM, change the `-match` value to `Outbound`.
    
    
    PS C:\> Get-NetFirewallPortFilter | `
    >>   Where-Object LocalPort -match  "PORT" | `
    >>   Get-NetFirewallRule | `
    >>   Where-Object {$_.Direction -match "Inbound" -and $_.Profile -match "Any"}
    
    
    
    Name                  : {80D79988-C7A5-4391-902D-382369B4E4A3}
    DisplayName           : iperf3 udp
    Description           :
    DisplayGroup          :
    Group                 :
    Enabled               : True
    Profile               : Any
    Platform              : {}
    Direction             : Inbound
    Action                : Allow
    EdgeTraversalPolicy   : Block
    LooseSourceMapping    : False
    LocalOnlyMapping      : False
    Owner                 :
    PrimaryStatus         : OK
    Status                : The rule was parsed successfully from the store. (65536)
    EnforcementStatus     : NotApplicable
    PolicyStoreSource     : PersistentStore
    PolicyStoreSourceType : Local
    

You can add a new firewall rules to Windows with the following commands.

Egress Rule:
    
    
    PS C:\> netsh advfirewall firewall add rule name="My Firewall Rule" dir=out action=allow protocol=TCP remoteport=DEST_PORT
    

Ingress Rule:
    
    
    PS C:\> netsh advfirewall firewall add rule name="My Firewall Rule" dir=in action=allow protocol=TCP localport=PORT
    

###  Third-party software 

Third-party application firewalls or antivirus software can also drop or reject connections. Consult the documentation provided by your vendor.

If you find a problem with firewall rules and correct it, retest your connectivity. If firewall rules don't seem to be the problem, proceed to Check configuration of OS routing.

### Check OS routing configuration

Operating system routing issues can come from one of the following situations:

  * Routing issues are most common on VMs with multiple network interfaces because of the additional routing complexity
  * On a VM created in Google Cloud with a single network interface, routing issues normally only happen if someone has manually modified the default routing table
  * On a VM that was migrated from on-premises, the VM might carry over routing or MTU settings that were needed on premises but which are causing problems in the VPC network



If you are using a VM with multiple network interfaces, routes must be configured to egress to the correct vNIC and subnet. For example, a VM might have routes configured so that traffic intended for internal subnets is sent to one vNIC, but the default gateway (destination `0.0.0.0/0`) is configured on another vNIC which has an external IP address or access to Cloud NAT.

You can review routes by checking individual routes one at a time or by looking at the entire VM routing table. If either approach reveals issues with the routing table, consult the steps in Update routing tables if needed for instructions.

#### Review all routes

List all your routes to understand what routes already exist on your VM.

###  Linux 
    
    
    $ ip route show table all
    
    
    
    default via 10.3.0.1 dev ens4
    10.3.0.1 dev ens4 scope link
    local 10.3.0.19 dev ens4 table local proto kernel scope host src 10.3.0.19
    broadcast 10.3.0.19 dev ens4 table local proto kernel scope link src 10.3.0.19
    broadcast 127.0.0.0 dev lo table local proto kernel scope link src 127.0.0.1
    local 127.0.0.0/8 dev lo table local proto kernel scope host src 127.0.0.1
    local 127.0.0.1 dev lo table local proto kernel scope host src 127.0.0.1
    broadcast 127.255.255.255 dev lo table local proto kernel scope link src 127.0.0.1
    ::1 dev lo proto kernel metric 256 pref medium
    fe80::/64 dev ens4 proto kernel metric 256 pref medium
    local ::1 dev lo table local proto kernel metric 0 pref medium
    local fe80::4001:aff:fe03:13 dev ens4 table local proto kernel metric 0 pref medium
    multicast ff00::/8 dev ens4 table local proto kernel metric 256 pref medium
    

###  Windows 
    
    
    PS C:\> Get-NetRoute
    
    
    
    ifIndex DestinationPrefix             NextHop  RouteMetric ifMetric PolicyStore
    ------- -----------------             -------  ----------- -------- -----------
    4       255.255.255.255/32            0.0.0.0          256 5        ActiveStore
    1       255.255.255.255/32            0.0.0.0          256 75       ActiveStore
    4       224.0.0.0/4                   0.0.0.0          256 5        ActiveStore
    1       224.0.0.0/4                   0.0.0.0          256 75       ActiveStore
    4       169.254.169.254/32            0.0.0.0            1 5        ActiveStore
    1       127.255.255.255/32            0.0.0.0          256 75       ActiveStore
    1       127.0.0.1/32                  0.0.0.0          256 75       ActiveStore
    1       127.0.0.0/8                   0.0.0.0          256 75       ActiveStore
    4       10.3.0.255/32                 0.0.0.0          256 5        ActiveStore
    4       10.3.0.31/32                  0.0.0.0          256 5        ActiveStore
    4       10.3.0.1/32                   0.0.0.0            1 5        ActiveStore
    4       10.3.0.0/24                   0.0.0.0          256 5        ActiveStore
    4       0.0.0.0/0                     10.3.0.1           0 5        ActiveStore
    4       ff00::/8                      ::               256 5        ActiveStore
    1       ff00::/8                      ::               256 75       ActiveStore
    4       fe80::b991:6a71:ca62:f23f/128 ::               256 5        ActiveStore
    4       fe80::/64                     ::               256 5        ActiveStore
    1       ::1/128                       ::               256 75       ActiveStore
    

#### Check individual routes

If a particular IP prefix seems to be the problem, check that proper routes exists for the source and destination IPs within the client and server VMs.

###  Linux 
    
    
    $ ip route get DEST_IP
    

Good result:

A valid route is shown. In this case, the packets egress from interface `ens4`.
    
    
    10.3.0.34 via 10.3.0.1 dev ens4 src 10.3.0.26 uid 1000
       cache
    

Bad result:

This result confirms that packets are being discarded because there is no pathway to the destination network. Confirm that your route table contains a path to the correct egress interface.
    
    
    **RTNETLINK answers: Network is unreachable
    

###  Windows 
    
    
    PS C:\> Find-NetRoute -RemoteIpAddress "DEST_IP"
    

Good result:
    
    
    IPAddress         : 192.168.0.2
    InterfaceIndex    : 4
    InterfaceAlias    : Ethernet
    AddressFamily     : IPv4
    Type              : Unicast
    PrefixLength      : 24
    PrefixOrigin      : Dhcp
    SuffixOrigin      : Dhcp
    AddressState      : Preferred
    ValidLifetime     : 12:53:13
    PreferredLifetime : 12:53:13
    SkipAsSource      : False
    PolicyStore       : ActiveStore
    
    Caption            :
    Description        :
    ElementName        :
    InstanceID         : ;:8=8:8:9<>55>55:8:8:8:55;
    AdminDistance      :
    DestinationAddress :
    IsStatic           :
    RouteMetric        : 256
    TypeOfRoute        : 3
    AddressFamily      : IPv4
    CompartmentId      : 1
    DestinationPrefix  : 192.168.0.0/24
    InterfaceAlias     : Ethernet
    InterfaceIndex     : 4
    InterfaceMetric    : 5
    NextHop            : 0.0.0.0
    PreferredLifetime  : 10675199.02:48:05.4775807
    Protocol           : Local
    Publish            : No
    State              : Alive
    Store              : ActiveStore
    ValidLifetime      : 10675199.02:48:05.4775807
    PSComputerName     :
    ifIndex            : 4
    

Bad result:
    
    
    
    Find-NetRoute : The network location cannot be reached. For information about network troubleshooting, see Windows Help.
    At line:1 char:1
    + Find-NetRoute -RemoteIpAddress "192.168.0.4"
    + ----------------------------------------
        + CategoryInfo          : NotSpecified: (MSFT_NetRoute:ROOT/StandardCimv2/MSFT_NetRoute) [Find-NetRoute], CimException
        + FullyQualifiedErrorId : Windows System Error 1231,Find-NetRoute
    
    

This command confirms that packets are being discarded because there is no pathway to the destination IP address. Check that you have a default gateway, and the gateway is applied to the correct vNIC and network.

#### Update routing tables

If needed, you can add a route to your operating system's route table. Before running a command to update the routing VM's routing table, we recommend you familiarize yourself with the commands and develop an understanding of the possible implications. Improper use of route update commands might cause unexpected problems or disconnection to the VM. Consider setting up [VM Serial Console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console) access before proceeding.

Consult your operating system documentation for instructions on updating routes.

If you find a problem with routes and correct it, retest your connectivity. If routes don't seem to be the problem, proceed to Check interface MTU.

### Check MTU

A VM's interface MTU should match the MTU of the VPC network it is attached to. Ideally, VMs that are communicating with each other also have matching MTUs. Mismatched MTUs are normally not an issue for TCP, but can be for UDP.

Check the MTU of the VPC. If the VMs are in two different networks, check both networks.
    
    
    gcloud compute networks describe NET_NAME --format="table(name,mtu)"
    

Check the MTU configuration for your client and server network interfaces.

###  Linux 
    
    
    $ netstat -i
    

The lo (loopback) interface always has an MTU of 65536 and can be ignored for this step.
    
    
    Kernel Interface table
    Iface      MTU    RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
    ens4      1460  8720854      0      0 0      18270406      0      0      0 BMRU
    lo       65536       53      0      0 0            53      0      0      0 LRU
    

###  Windows 
    
    
    PS C:\> Get-NetIpInterface
    

Loopback Pseudo-Interfaces always have an MTU of 4294967295 and can be ignored for this step.
    
    
    ifIndex InterfaceAlias              Address NlMtu(Bytes) Interface Dhcp     Connection PolicyStore
                                        Family               Metric             State
    ------- --------------              ------- ------------ --------- ----     ---------- -----------
    4       Ethernet                    IPv6            1500         5 Enabled  Connected  ActiveStore
    1       Loopback Pseudo-Interface 1 IPv6      4294967295        75 Disabled Connected  ActiveStore
    4       Ethernet                    IPv4            1460         5 Enabled  Connected  ActiveStore
    1       Loopback Pseudo-Interface 1 IPv4      4294967295        75 Disabled Connected  Active
    

If the interface and network MTUs don't match, you can reconfigure the interface MTU. For more information, see [VMs and MTU settings](https://docs.cloud.google.com/vpc/docs/mtu#vms_and_mtu_settings). If they do match, and if you have followed the troubleshooting steps this far, then the issue is likely with the server itself. For guidance on troubleshooting server issues, proceed to Check server logging for information about server behavior.

### Check server logging for information about server behavior

If the preceding steps don't resolve an issue, the application might be causing the timeouts. Check server and application logs for behavior that would explain what you're seeing.

Log sources to check:

  * [Cloud Logging for the VM](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface)
  * [VM Serial Logs](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output)
  * Linux syslog and kern.log, or Windows Event Viewer



### If you're still having issues

If you're still having issues, see [Getting support](https://docs.cloud.google.com/compute/docs/getting-support) for next steps. It's useful to have the output from the preceding troubleshooting steps available to share with other collaborators.

## Troubleshoot network latency or loss causing throughput issues

Network latency or loss issues are typically caused by resource exhaustion or bottlenecks within a VM or network path. Occasionally, network loss can cause intermittent connection timeouts. Causes like vCPU exhaustion or vNIC saturation result in increased latency and packet loss leading to a reduction in network performance.

The following instructions assume that connections are not consistently timing out and you are instead seeing issues of limited capacity or performance. If you are seeing complete packet loss, see Troubleshoot complete connection failure.

Small variations in latency, such as latencies varying by a few milliseconds, are normal. Latencies vary because of network load or queuing inside the VM.

### Determine connection values

First gather the following information:

  * From the [VM instances page](https://console.cloud.google.com/compute/instances), gather the following for both VMs: 
    * VM names
    * VM zones
    * Internal IP addresses for the vNICs that are communicating
  * From the configuration of the destination server software, gather the following information: 
    * Layer 4 protocol
    * Destination port



If you're seeing issues with multiple VMs, pick a single source and single destination VM that are experiencing issues and use those values. In general, you shouldn't need the source port of the connection.

Once you have this information, proceed to Investigate issues with the underlying Google network.

### Investigate issues with the underlying Google network

If your setup is an existing one that hasn't changed recently, then the issue might be with the underlying Google network. Check the Network Intelligence Center [](https://console.cloud.google.com/net-intelligence/performance/dashboard/packet-loss)[Performance Dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard) for [packet loss](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/using-performance-dashboard#packet-loss) between the VM zones. If there is an increase in packet loss between the zones during the timeframe where you experienced network timeouts, it might indicate that the problem is with the physical network underlying your virtual network. Check the [Google Cloud Status Dashboard](https://status.cloud.google.com) for known issues before filing a support case.

If the issue does not seem to be with the underlying Google network, proceed to Check handshake latency.

### Check handshake latency

All connection-based protocols incur some latency while they do their connection setup handshake. Each protocol handshake adds to the overhead. For SSL/TLS connections, for example, the TCP handshake has to complete before the SSL/TLS handshake can start, then the TLS handshake has to complete before data can be transmitted.

Handshake latency in the same Google Cloud zone is usually negligible, but handshakes to globally distant locations might add greater delays at connection initiation. If you have resources in distant regions, you can check to see if the latency you're seeing is due to protocol handshake.

###  Linux and Windows 2019 
    
    
    $ curl -o /dev/null -Lvs -w 'tcp_handshake: %{time_connect}s, application_handshake: %{time_appconnect}s' DEST_IP:PORT
    
    
    
    tcp_handshake: 0.035489s, application_handshake: 0.051321s
    

  * tcp_handshake is duration from when the client sends the initial SYN packet to when the client sends the ACK of the TCP handshake.
  * application_handshake is the time from the first SYN packet of the TCP handshake to the completion of the TLS (typically) handshake.
  * additional handshake time = application_handshake - tcp_handshake



###  Windows 2012 and 2016 

Not available with default OS tooling. ICMP round-trip time can be used as a reference if firewall rules allow.

If the latency is more than the handshakes would account for, proceed to Determine the maximum throughput of your VM type.

### Determine the maximum throughput of your VM type

VM network _egress_ throughput is limited by the VM CPU architecture and vCPU count. Determine the potential egress bandwidth of your VM by consulting the [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth) page.

If your VM is not capable of meeting your egress requirements, consider upgrading to a VM with greater capacity. For instructions, see [Changing the machine type of an instance](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance).

If your machine type should allow sufficient egress bandwidth, then investigate whether Persistent Disk usage is interfering with your network egress. Persistent Disk operations are allowed to occupy up to 60% of the total network throughput of your VM. To determine if Persistent Disk operations might be interfering with network throughput, see Check Persistent Disk performance.

Network _ingress_ to a VM is not limited by the VPC network or the VM instance type. Instead, it is determined by the packet queuing and processing performance of the VM operating system or application. If your egress bandwidth is adequate but you're seeing ingress issues, see Check server logging for information about server behavior.

### Check interface MTU

The MTU of a VPC network is configurable. The MTU of interface on the VM should match the MTU value for the VPC network it is attached to. In a VPC Network Peering situation, VMs in different networks can have different MTUs. When this scenario occurs, apply the smaller MTU value to the associated interfaces. MTU mismatches are normally not an issue for TCP, but can be for UDP.

Check the MTU of the VPC. If the VMs are in two different networks, check both networks.
    
    
    gcloud compute networks describe NET_NAME --format="table(name,mtu)"
    

Check the MTU configuration for your network interface.

###  Linux 

The lo (loopback) interface always has an MTU of 65536 and can be ignored for this step.
    
    
    $ netstat -i
    
    
    
    Kernel Interface table
    Iface      MTU    RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
    ens4      1460  8720854      0      0 0      18270406      0      0      0 BMRU
    lo       65536       53      0      0 0            53      0      0      0 LRU
    

###  Windows 
    
    
    PS C:\> Get-NetIpInterface
    

Loopback Pseudo-Interfaces always have an MTU of 4294967295 and can be ignored for this step.
    
    
    ifIndex InterfaceAlias              Address NlMtu(Bytes) Interface Dhcp     Connection PolicyStore
                                        Family               Metric             State
    ------- --------------              ------- ------------ --------- ----     ---------- -----------
    4       Ethernet                    IPv6            1500         5 Enabled  Connected  ActiveStore
    1       Loopback Pseudo-Interface 1 IPv6      4294967295        75 Disabled Connected  ActiveStore
    4       Ethernet                    IPv4            1460         5 Enabled  Connected  ActiveStore
    1       Loopback Pseudo-Interface 1 IPv4      4294967295        75 Disabled Connected  Active
    

If the interface and network MTUs don't match, you can reconfigure the interface MTU. For instructions on updating MTU for Windows VMs, see [VMs and MTU settings](https://docs.cloud.google.com/vpc/docs/vpc#vms_and_mtu_settings). If they do match, then the issue is likely might be server availability. The next step is to Check logs to see if a VM was rebooted, stopped, or live migrated to see if anything happened to your VM during the relevant time.

### Check logs to see if a VM was rebooted, stopped, or live migrated

During the lifecycle of a VM, a VM can be user-rebooted, live-migrated for Google Cloud maintenance, or, in rare circumstances, a VM might be lost and recreated if there is a failure within the physical host containing your VM. These events might cause a brief increase in latency or connection timeouts. If any of these things happens to the VM, the event is logged.

To view logs for your VM, do the following:

  1. In the Google Cloud console, go to the **Logging** page.

[Go to Logging](https://console.cloud.google.com/logs/query)

  2. Choose the timeframe of when the latency occurred.

  3. Use the following Logging query to determine if a VM event occurred near the timeframe when the latency occurred: 
         
         resource.labels.instance_id:"INSTANCE_NAME"
         resource.type="gce_instance"
         (
           protoPayload.methodName:"compute.instances.hostError" OR
           protoPayload.methodName:"compute.instances.OnHostMaintenance" OR
           protoPayload.methodName:"compute.instances.migrateOnHostMaintenance" OR
           protoPayload.methodName:"compute.instances.terminateOnHostMaintenance" OR
           protoPayload.methodName:"compute.instances.stop" OR
           protoPayload.methodName:"compute.instances.reset" OR
           protoPayload.methodName:"compute.instances.automaticRestart" OR
           protoPayload.methodName:"compute.instances.guestTerminate" OR
           protoPayload.methodName:"compute.instances.instanceManagerHaltForRestart" OR
           protoPayload.methodName:"compute.instances.preempted"
         )
         




If VMs didn't restart or migrate during the relevant time, the issue might be with resource exhaustion. To check, proceed to Check network and OS statistics for packet discards due to resource exhaustion.

### Check network and OS statistics for packet discards due to resource exhaustion

_Resource exhaustion_ is a general term that means that some resource on the VM, such as egress bandwidth, is being asked to handle more than it can. Resource exhaustion can result in the periodic discards of packets, which causes connection latency or timeouts. These timeouts might not be visible at client or server startup, but might appear over time as a system exhausts resources.

The following is a list of commands which display packet counters and statistics. Some of these commands duplicate the results of other commands. In such cases, you can use whichever command works better for you. See the notes within each section to better understand the intended outcome of running the command. It can be useful to run the commands at different times to see if discards or errors are occurring at the same time as the issue.

###  Linux 

  1. Use the `netstat` command to view network statistics.
         
         $ netstat -s
         
         
         TcpExt:
           341976 packets pruned from receive queue because of socket buffer overrun
           6 ICMP packets dropped because they were out-of-window
           45675 TCP sockets finished time wait in fast timer
           3380 packets rejected in established connections because of timestamp
           50065 delayed acks sent
         

The netstat command outputs network statistics containing values for discarded packets by protocol. Discarded packets might be the result of resource exhaustion by the application or network interface. View the counter reason for indication of why a counter was incremented.

  2. Check kern.log for logs matching `nf_conntrack: table full, dropping packet`.

Debian: `cat /var/log/kern.log | grep "dropping packet"`

CentOS: `sudo cat /var/log/dmesg | grep "dropping packet"`

This log indicates that the connection tracking table for VM has reached the maximum connections that can be tracked. Further connections to and from this VM might timeout. If conntrack has been enabled, the maximum connection count can be found with: `sudo sysctl net.netfilter.nf_conntrack_max`

You can increase the value for maximum tracked connections by modifying sysctl `net.netfilter.nf_conntrack_max` or by spreading a VMs workload across multiple VMs to reduce load.




###  Windows UI 

Perfmon

  1. Using the Windows menu, search for "perfmon" and open the program.
  2. On the left-menu, select **Performance > Monitoring Tools > Performance Monitor**.
  3. In the main view, click the green plus "+" to add performance counters to the monitoring graph. The following counters are of interest: 
     * Network Adapter 
       * Output Queue Length
       * Packets Outbound Discarded
       * Packets Outbound Errors
       * Packets Received Discarded
       * Packets Received Errors
       * Packets Received Unknown
     * Network Interface 
       * Output Queue Length
       * Packets Outbound Discarded
       * Packets Outbound Errors
       * Packets Received Discarded
       * Packets Received Errors
       * Packets Received Unknown
     * Per Processor Network Interface Card Activity 
       * Low Resource Receive Indications per sec
       * Low Resource Received Packets per sec
     * Processor 
       * % Interrupt Time
       * % Privileged Time
       * % Processor Time
       * % User Time



Pefmon lets you plot the preceding counters on a time series graph. This can be beneficial to watch when testing is occurring or a server is impacted. Spikes in CPU-related counters such as Interrupt Time and Privileged Time can indicate saturation issues as the VM reaches CPU throughput limitations. Packet discards and errors can occur when the CPU is saturated, which forces packets to be lost before being processed by the client or server sockets. Finally, Output Queue Length will also grow during CPU saturation as more packets are queued for processing.

###  Windows Powershell 
    
    
    PS C:\> netstat -s
    
    
    
    IPv4 Statistics
    
      Packets Received                   = 56183
      Received Header Errors             = 0
      Received Address Errors            = 0
      Datagrams Forwarded                = 0
      Unknown Protocols Received         = 0
      Received Packets Discarded         = 25
      Received Packets Delivered         = 56297
      Output Requests                    = 47994
      Routing Discards                   = 0
      Discarded Output Packets           = 0
      Output Packet No Route             = 0
      Reassembly Required                = 0
      Reassembly Successful              = 0
      Reassembly Failures                = 0
      Datagrams Successfully Fragmented  = 0
      Datagrams Failing Fragmentation    = 0
      Fragments Created                  = 0
    

The netstat command outputs network statistics containing values for discarded packets by protocol. Discarded packets might be the result of resource exhaustion by the application or network interface.

If you are seeing resource exhaustion, you can try spreading your workload across more instances, upgrading the VM to one with more resources, tuning the OS or application for specific performance needs, entering the error message into a search engine to look for possible solutions, or ask for help using one of the methods described in If you're still having issues.

If resource exhaustion doesn't seem to be the problem, the issue might be with the server software itself. For guidance on troubleshooting server software issues, proceed to Check server logging for information about server behavior.

### Check server logging for information about server behavior

If the preceding steps don't reveal an issue, the timeouts might be caused by application behavior such as processing stalls caused by vCPU exhaustion. Check the server and applications logs for indications of the behavior you are experiencing.

As an example, a server experiencing increased latency due to an upstream system, such as a database under load, might queue an excessive amount of requests which can cause increased memory usage and CPU wait times. These factors might result in failed connections or socket buffer overrun.

TCP connections occasionally lose a packet, but selective acknowledgement and packet retransmission usually recovers lost packets, avoiding connection timeout. Instead, consider that timeouts might have been the result of the application server failing or being redeployed, causing a momentary failure for connections.

If your server application relies on a connection to a database or other service, confirm that coupled services are not performing poorly. Your application might track these metrics.

### If you're still having issues

If you're still having issues, see [Getting support](https://docs.cloud.google.com/compute/docs/getting-support) for next steps. It's useful to have the output from the troubleshooting steps available to share with other collaborators.

## What's next

  * If you are still having trouble, see the [Resources](https://docs.cloud.google.com/vpc/docs/resources) page.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
