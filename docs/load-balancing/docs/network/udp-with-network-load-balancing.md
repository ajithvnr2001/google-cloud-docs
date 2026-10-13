---
url: https://docs.cloud.google.com/load-balancing/docs/network/udp-with-network-load-balancing/
title: Use UDP with regional external passthrough Network Load Balancers \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:27:22.593849+00:00
---

# Use UDP with regional external passthrough Network Load Balancers  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/network/udp-with-network-load-balancing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Use UDP with regional external passthrough Network Load Balancers Stay organized with collections  Save and categorize content based on your preferences. 

This document discusses how to work with [regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network) by using the User Datagram Protocol (UDP). The document is intended for app developers, app operators, and network administrators.

## About UDP

UDP is used commonly in apps. The protocol, which is described in [RFC-768](https://tools.ietf.org/html/rfc768), implements a stateless, unreliable datagram packet service. For example, Google's [QUIC](https://wikipedia.org/wiki/QUIC) protocol improves the user experience by using UDP to speed up stream-based apps.

The stateless part of UDP means that the transport layer doesn't maintain a state. Therefore, each packet in a UDP "connection" is independent. In fact, there is no real connection in UDP. Instead, its participants usually use a 2-tuple (`ip:port`) or a 4-tuple (`src-ip:src-port`, `dest-ip:dest-port`) to recognize each other.

Like TCP-based apps, UDP-based apps can also benefit from a load balancer, which is why regional external passthrough Network Load Balancers are used in UDP scenarios.

## Regional external passthrough Network Load Balancer

Regional external passthrough Network Load Balancers are passthrough load balancers; they process incoming packets and deliver them to backend servers with the packets intact. The backend servers then send the returning packets directly to the clients. This technique is called Direct Server Return (DSR). On each Linux virtual machine (VM) running on Compute Engine that is a backend of a Google Cloud regional external passthrough Network Load Balancer, an entry in the local routing table routes traffic that's destined for the load balancer's IP address to the network interface controller (NIC). The following example demonstrates this technique:
    
    
    root@backend-server:~# ip ro ls table local
    local 10.128.0.2 dev eth0 proto kernel scope host src 10.128.0.2
    broadcast 10.128.0.2 dev eth0 proto kernel scope link src 10.128.0.2
    local 198.51.100.2 dev eth0 proto 66 scope host
    broadcast 127.0.0.0 dev lo proto kernel scope link src 127.0.0.1
    local 127.0.0.0/8 dev lo proto kernel scope host src 127.0.0.1
    local 127.0.0.1 dev lo proto kernel scope host src 127.0.0.1
    broadcast 127.255.255.255 dev lo proto kernel scope link src 127.0.0.1
    

In the preceding example, `198.51.100.2` is the load balancer's IP address. The `google-network-daemon.service` agent is responsible for adding this entry. However, as the following example shows, the VM does not actually have an interface that owns the load balancer's IP address:
    
    
    root@backend-server:~# ip ad ls
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host
           valid_lft forever preferred_lft forever
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1460 qdisc mq state UP group default qlen 1000
        link/ether 42:01:0a:80:00:02 brd ff:ff:ff:ff:ff:ff
        inet 10.128.0.2/32 brd 10.128.0.2 scope global eth0
           valid_lft forever preferred_lft forever
        inet6 fe80::4001:aff:fe80:2/64 scope link
           valid_lft forever preferred_lft forever
    

The regional external passthrough Network Load Balancer transmits the incoming packets, with the destination address untouched, to the backend server. The local routing table entry routes the packet to the correct app process, and the response packets from the app are sent directly to the client.

The following diagram shows how regional external passthrough Network Load Balancers work. The incoming packets are processed by a load balancer called [Maglev](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/44824.pdf), which distributes the packets to the backend servers. Outgoing packets are then sent directly to the clients through DSR.

![Maglev distributes incoming packets to backend servers, which distribute the packets through DSR.](https://docs.cloud.google.com/static/architecture/images/balancing-udp-traffic-maglev.svg)

## An issue with UDP return packets

When you work with DSR, there is a slight difference between how the Linux kernel treats TCP and UDP connections. Because TCP is a stateful protocol, the kernel has all the information it needs about the TCP connection, including the client address, client port, server address, and server port. This information is recorded in the socket data structure that represents the connection. Thus, each returning packet of a TCP connection has the source address correctly set to the server address. For a load balancer, that address is the load balancer's IP address.

Recall that UDP is stateless, however, so the socket objects that are created in the app process for UDP connections don't have the connection information. The kernel doesn't have the information about the source address of an outgoing packet, and it doesn't know the relation to a previously received packet. For the packet's source address, the kernel can only fill in the address of the interface that the returning UDP packet goes to. Or if the app previously bound the socket to a certain address, the kernel uses that address as the source address.

The following code shows a simple echo program:
    
    
    #!/usr/bin/python3
    import socket,struct
    def loop_on_socket(s):
      while True:
        d, addr = s.recvfrom(1500)
        print(d, addr)
        s.sendto("ECHO: ".encode('utf8')+d, addr)
    
    if __name__ == "__main__":
       HOST, PORT = "0.0.0.0", 60002
       sock = socket.socket(type=socket.SocketKind.SOCK_DGRAM)
       sock.bind((HOST, PORT))
       loop_on_socket(sock)
    

Following is the `tcpdump` output during a UDP conversation:
    
    
    14:50:04.758029 IP 203.0.113.2.40695 > 198.51.100.2.60002: UDP, length 3
    14:50:04.758396 IP 10.128.0.2.60002 > 203.0.113.2.40695: UDP, length 2T
    

`198.51.100.2` is the load balancer's IP address, and `203.0.113.2` is the client IP address.

After the packets leave the VM, another NAT device–a Compute Engine gateway–in the Google Cloud network translates the source address to the external address. The gateway doesn't know which external address should be used, so only the VM's external address (not the load balancer's) can be used.

From the client side, if you check the output from `tcpdump`, the packets from the server look like the following:
    
    
    23:05:37.072787 IP 203.0.113.2.40695 > 198.51.100.2.60002: UDP, length 5
    23:05:37.344148 IP 198.51.100.3.60002 > 203.0.113.2.40695: UDP, length 4
    

`198.51.100.3` is the VM's external IP address.

From the client's point of view, the UDP packets are not coming from an address that the client sent them to. This causes problems: the kernel drops these packets, and if the client is behind a NAT device, so does the NAT device. As a result, the client app gets no response from the server. The following diagram shows this process where the client rejects returning packets because of address mismatches.

![Client rejects returning packets.](https://docs.cloud.google.com/static/load-balancing/images/balancing-udp-traffic-rejected-packets.svg)

## Solving the UDP problem

To solve the no-response problem, you must rewrite the source address of outgoing packets to the load balancer's IP address at the server that's hosting the app. Following are several options that you can use to accomplish this header rewrite. The first solution uses a Linux-based approach with `iptables`; the other solutions take app-based approaches.

**Note:** The last two examples in this document are written in Python 3 but can be written in most programming languages.

The following diagram shows the core idea of these options: rewrite the source IP address of the returning packets in order to match the load balancer's IP address.

![Rewrite the source IP address of the returning packets in order to match the load balancer's
IP address.](https://docs.cloud.google.com/static/load-balancing/images/balancing-udp-traffic-rewrite-source-ip-address.svg)

### Use NAT policy in the backend server

The NAT policy solution is to use the Linux `iptables` command to rewrite the destination address from the load balancer's IP address to the VM's IP address. In the following example, you add an `iptables` DNAT rule to change the destination address of the incoming packets:
    
    
    iptables -t nat -A POSTROUTING -j RETURN -d 10.128.0.2 -p udp --dport 60002
    iptables -t nat -A PREROUTING -j DNAT --to-destination 10.128.0.2 -d 198.51.100.2 -p udp --dport 60002
    

This command adds two rules to the NAT table of the `iptables` system. The first rule bypasses all incoming packets that target the local `eth0` address. As a result, traffic that doesn't come from the load balancer isn't affected. The second rule changes the destination IP address of incoming packets to the VM's internal IP address. The DNAT rules are stateful, which means that the kernel tracks the connections and rewrites the returning packets' source address automatically.

Pros | Cons  
---|---  
The kernel translates the address, with no change required to apps.  | Extra CPU is used to do the NAT. And because DNAT is stateful, memory consumption might also be high.   
Supports multiple load balancers. |   
  
### Use `nftables` to statelessly mangle the IP header fields

In the `nftables` solution, you use the `nftables` command to mangle the source address in the IP header of outgoing packets. This mangling is stateless, so it consumes fewer resources than using DNAT. To use `nftables`, you need a Linux kernel version greater than 4.10.

You use the following commands:
    
    
    nft add table raw
    nft add chain raw postrouting {type filter hook postrouting priority 300)
    nft add rule raw postrouting ip saddr 10.128.0.2 udp sport 60002 ip saddr set 198.51.100.2
    

Pros | Cons  
---|---  
The kernel translates the address, with no change required to apps. | Does not support multiple load balancers.  
The address translation process is stateless, so resource consumption is much lower.  | Extra CPU is used to do the NAT.  
| `nftables` are available only to newer Linux kernel versions. Some distros, like Centos 7.x, cannot use `nftables`.   
  
### Let the app explicitly bind to the load balancer's IP address

In the binding solution, you modify your app so that it binds explicitly to the load balancer's IP address. For a UDP socket, the `bind` operation lets the kernel know which address to use as the source address when sending UDP packets that use that socket.

The following example shows how to bind to a specific address in Python:
    
    
    #!/usr/bin/python3
    import socket
    def loop_on_socket(s):
      while True:
        d, addr = s.recvfrom(1500)
        print(d, addr)
        s.sendto("ECHO: ".encode('utf8')+d, addr)
    
    if __name__ == "__main__":
       # Instead of setting HOST to "0.0.0.0",
       # we set HOST to the Load Balancer IP
       HOST, PORT = "198.51.100.2", 60002
       sock = socket.socket(type=socket.SocketKind.SOCK_DGRAM)
       sock.bind((HOST, PORT))
       loop_on_socket(sock)
    
    # 198.51.100.2 is the load balancer's IP address
    # You can also use the DNS name of the load balancer's IP address
    

The preceding code is a UDP server; it echoes back the bytes received, with a preceding `"ECHO: "`. Pay attention to lines 12 and 13, where the server is bound to the address `198.51.100.2`, which is the load balancer's IP address.

Pros | Cons  
---|---  
Can be achieved with a simple code change to the app. | Does not support multiple load balancers.  
  
### Use `recvmsg`/`sendmsg` instead of `recvfrom`/`sendto` to specify the address

In this solution, you use `recvmsg`/`sendmsg` calls instead of `recvfrom`/`sendto` calls. In comparison to `recvfrom`/`sendto` calls, the `recvmsg`/`sendmsg` calls can handle ancillary control messages along with the payload data. These ancillary control messages include the source or destination address of the packets. This solution lets you fetch destination addresses from incoming packets, and because those addresses are real load balancer addresses, you can use them as source addresses when sending replies.

The following example program demonstrates this solution:
    
    
    #!/usr/bin/python3
    import socket,struct
    def loop_on_socket(s):
      while True:
        d, ctl, flg, addr = s.recvmsg(1500, 1024)
        # ctl contains the destination address information
        s.sendmsg(["ECHO: ".encode("utf8"),d], ctl, 0, addr)
    
    if __name__ == "__main__":
       HOST, PORT = "0.0.0.0", 60002
       s = socket.socket(type=socket.SocketKind.SOCK_DGRAM)
       s.setsockopt(0,   # level is 0 (IPPROTO_IP)
                    8,   # optname is 8 (IP_PKTINFO)
                    1)
    
       s.bind((HOST, PORT))
       loop_on_socket(s)
    

This program demonstrates how to use `recvmsg`/`sendmsg` calls. In order to fetch address information from packets, you must use the `setsockopt` call to set the `IP_PKTINFO` option.

Pros | Cons  
---|---  
Works even if there are multiple load balancers–for example, when there are both internal and external load balancers configured to the same backend.  | Requires you to make complex changes to the app. In some cases, this might not be possible.   
  
## What's next

  * Learn how to configure a regional external passthrough Network Load Balancer and distribute traffic in [Set up a regional external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network).
  * Read more about [regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network).
  * Read more about the [Maglev](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/44824.pdf) technique behind regional external passthrough Network Load Balancers.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
