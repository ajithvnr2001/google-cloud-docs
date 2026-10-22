---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/calculate-network-throughput-over-interconnect/
title: Calculate network throughput over Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:21.675129+00:00
---

# Calculate network throughput over Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/calculate-network-throughput-over-interconnect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Calculate network throughput over Interconnect Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how to calculate network throughput, both within Google Cloud and to your on-premises or third-party cloud locations that are connected using Cloud Interconnect. This document describes how to analyze results, lists the variables that can affect network performance, and provides some troubleshooting tips.

## Limitations and considerations

  * Cloud Interconnect limitations apply. For more information, see [Cloud Interconnect quotas](https://docs.cloud.google.com/network-connectivity/docs/interconnect/quotas#limits).
  * NIC limits: Google Cloud accounts for bandwidth of each virtual machine (VM) instance, not for each network interface (NIC) or IP address. A VM's machine type defines its maximum egress rate; however, that rate can only be achieved in specific situations. See this [table](https://docs.cloud.google.com/compute/docs/machine-types#machine_type_comparison) for the number of vCPUs per machine type.
  * Other devices in the path (firewall, switches with small buffers, and other vendors' devices) and their limitations apply. Perform the following tasks to mitigate those limitations.

    * Gather network statistics on firewalls and switches in the path.
    * For Cloud Interconnect testing, bypass as many devices as possible between the on-premises host and the Google Edge device.
    * Identify and verify all the devices in the path between the on-premises network and the Google Cloud VM if they can be the source of throughput issues.



## Overview of tools for measuring network throughput

This tutorial demonstrates the use of the following tools for calculating network throughput:

  * [iPerf3](https://iperf.fr/): A network testing tool that can create TCP/UDP data streams (single-thread or multi-thread) and measure the throughput of the network that carries them.

  * [Netperf](https://hewlettpackard.github.io/netperf/): A tool that is similar to iPerf3 but appropriate for throughput testing on multi-CPU instances that are CPU-bound on a single CPU.

  * [tcpdump](https://en.wikipedia.org/wiki/Tcpdump): A command-line packet analyzer that captures packet details and TCP/IP communications for more advanced troubleshooting. The tcpdump tool is compatible with other tools, such as Wireshark.

  * [Netstat](https://en.wikipedia.org/wiki/Netstat): A command-line network utility that displays network connections for Transmission Control Protocol (both incoming and outgoing), routing tables, and several network interface (network interface controller or software-defined network interface) and network protocol statistics.

  * [mtr](https://en.wikipedia.org/wiki/MTR_\(software\)): A networking diagnostic tool that performs both traceroute and ping functions. It probes routers on the route path by limiting the number of hops individual packets may traverse, and listens to the responses of their expiry.




## Measure throughput with iPerf3

Follow this procedure to measure throughput from a single VM instance.

### Choose a large machine type

To perform throughput tests, use a large machine type, such as **n1-standard-8**. This machine type provides a maximum egress throughput limit of 16 Gbps, so the per-VM egress throughput does not interfere with the tests.

### Install the tools

#### Install iPerf3, mtr, netstat, and tcpdump on a Linux VM instance

For Debian-based distributions, run the following commands:
    
    
        sudo apt-get update
        sudo apt-get install iperf3 tcpdump mtr netstat
    

For Redhat-based distributions, run the following commands:
    
    
        yum update
        yum install iperf3 tcpdump mtr netstat
    

#### Install netperf

**Note:** You only need to compile this tool from the source to enable the demo option.

For Debian-based distributions, run the following commands:
    
    
        sudo apt-get install git build-essential autoconf texinfo -y
        git clone https://github.com/HewlettPackard/netperf.git
        cd netperf
        ./autogen.sh
        ./configure --enable-histogram --enable-demo=yes
        make
        cp src/netserver ~/.local/bin
        cp src/netperf ~/.local/bin
    

For Redhat-based distributions, run the following commands:
    
    
        sudo yum install git build-essential autoconf texinfo -y
        git clone https://github.com/HewlettPackard/netperf.git
        cd netperf
        ./autogen.sh
        ./configure --enable-histogram --enable-demo=yes
        make
        cp src/netserver ~/.local/bin
        cp src/netperf ~/.local/bin
    

### Run the prerequisite tests

  1. Make sure the VLAN attachment sizes are configured correctly. For more information, see [Modifying VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-vlan-attachments).
  2. On both ends of the connection (each terminal), run the `top` or `htop` command to monitor CPU usage.
  3. Gather network statistics using the `netstat` command before running any tests.
         
         netstat -s >> netstat.log
         

  4. In another terminal, run the `tcpdump` command before any capture with the `snaplen` parameter value of `128`.

Run this command on both of the endpoints.
         
         sudo /usr/sbin/tcpdump -s 128 -i [DEVICE_INTERFACE] host [IP_ADDRESS of remote side] -w mycap.pcap
         

  5. Get the read and write memory size on the source and destination hosts.
         
         $ sysctl net.ipv4.tcp_rmem
         $ sysctl net.ipv4.tcp_wmem
         $ sysctl net.core.rmem_max
         $ sysctl net.core.rmem_default
         $ net.core.wmem_max
         $ net.core.wmem_default
         $ uname -r
         $ cat /etc/os-release
         




### Run the iperf3 tests

We recommend that you run multiple parallel streams of `iperf3` tests. We recommend that you run a minimum of four tests and a maximum of ten tests to get useful results.

  1. In another terminal, run `iperf3` server on one end of the connection (a VM, or an on-premises machine). Multiple streams require multiple `iperf3` servers.

  2. Run the iPerf3 tool with the `udp` flag for Cloud Interconnect testing. If the chosen throughput with UDP is achieved, you need to perform further troubleshooting steps.

  3. To run the multiple `iperf3` servers from the command line, run the following commands:
         
         $ iperf3 -s -p 5101&; iperf3 -s -t 30 -p 5102&; iperf3 -s  -p 5103 &
         

  4. Use the following bash script to run multiple iperf3 servers:
         
         #!/bin/bash
         #start iperf3 server running in background
         
         for i in `seq 0 9`;
         do
                 iperf3 -s  -B 10.0.100.35 -t 30 -u -p 521$i &
         done
         




The `iperf3 client` runs for 10 seconds by default, which may not be enough for TCP to reach the maximum throughput. Set the `DURATION` value to at least 30 seconds to achieve more reliable results.
    
    
        iperf3 -c [server IP address] -P [THREADS] -t [DURATION]
    

#### Bash script to run multiple iperf3 UDP streams
    
    
    echo "UDP iperf test - 10 streams"
    for i in `seq 0 9`;
    do
           iperf3 -B 10.0.100.35 -c 192.168.50.3 --logfile ~/gcpvm_client-521$i.log -u -b 1G  -l 1390 -t10 -p 521$i    &
    
    done
    

#### Bash script to run multiple iperf3 TCP streams
    
    
    echo "UDP iperf test - 10 streams"
    for i in `seq 0 9`;
    do
           iperf3 -B 10.0.100.35 -c 192.168.50.3 --logfile ~/gcpvm_client-521$i.log -b 1G  -l 1390 -t10 -p 521$i    &
    
    done
    

While the `iperf3` test is running, monitor the CPU load on both of the devices. If the CPU load is close to 100%, CPU is a bottleneck for one iperf3 thread. In this case, use the Netperf tool, because it supports multiple CPUs.

If you can't run Netperf, then you can you can start multiple iPerf3 servers and clients on different terminals and different ports simultaneously.

### Analyze the test results

Perform the following steps.

  1. Check `iperf3` client results for bandwidth and packet loss.
  2. Check `iperf3` server results for any out-of-order packets.
  3. Perform packet capture analysis. Run the following command to convert the pcap file to a text file.
         
         tcpdump -A -[PCAP-FILENAME].pcap > [TXT-FILENAME].txt
         

  4. Run the following command to get the total of packets and out-of-order packets.
         
         grep -e "Total" -A1 pcap [TXT-FILENAME]
         

The output is the following:
         
         gcpvm-send-5210.txt:Total UDP packets: 874032
         gcpvm-send-5210.txt:Total out-of-order packets: 0, missing packets: 0
         gcpvm-send-5211.txt:Total UDP packets: 791218
         gcpvm-send-5211.txt:Total out-of-order packets: 0, missing packets: 0
         gcpvm-send-5212.txt:Total UDP packets: 961510
         gcpvm-send-5212.txt:Total out-of-order packets: 0, missing packets: 0
         gcpvm-send-5213.txt:Total UDP packets: 961517
         gcpvm-send-5213.txt:Total out-of-order packets: 0, missing packets: 0
         gcpvm-send-5214.txt:Total UDP packets: 961501
         gcpvm-send-5214.txt:Total out-of-order packets: 0, missing packets: 0
         gcpvm-send-5215.txt:Total UDP packets: 961521
         gcpvm-send-5215.txt:Total out-of-order packets: 0, missing packets: 0
         gcpvm-send-5216.txt:Total UDP packets: 889932
         gcpvm-send-5216.txt:Total out-of-order packets: 0, missing packets: 0
         gcpvm-send-5217.txt:Total UDP packets: 961483
         gcpvm-send-5217.txt:Total out-of-order packets: 0, missing packets: 0
         gcpvm-send-5218.txt:Total UDP packets: 961479
         gcpvm-send-5218.txt:Total out-of-order packets: 0, missing packets: 0
         gcpvm-send-5219.txt:Total UDP packets: 961518
         gcpvm-send-5219.txt:Total out-of-order packets: 0, missing packets: 0
         

The following analysis shows packet loss during a performance test:
         
         $ grep -e "Total" -A1 onPrem-send-*.txt
         

The output is the following:
         
         "Total" -A1 onPrem-send-*.txt
         onPrem-send-5210.txt:Total UDP packets: 858698
         onPrem-send-5210.txt:Total out-of-order packets: 0, missing packets: 5408
         --
         onPrem-send-5211.txt:Total UDP packets: 857667
         onPrem-send-5211.txt:Total out-of-order packets: 0, missing packets: 4929
         --
         onPrem-send-5212.txt:Total UDP packets: 857126
         onPrem-send-5212.txt:Total out-of-order packets: 0, missing packets: 5349
         --
         onPrem-send-5213.txt:Total UDP packets: 857424
         onPrem-send-5213.txt:Total out-of-order packets: 0, missing packets: 5495
         --
         onPrem-send-5214.txt:Total UDP packets: 857139
         onPrem-send-5214.txt:Total out-of-order packets: 0, missing packets: 4692
         --
         onPrem-send-5215.txt:Total UDP packets: 857175
         onPrem-send-5215.txt:Total out-of-order packets: 0, missing packets: 4789
         --
         onPrem-send-5216.txt:Total UDP packets: 857104
         onPrem-send-5216.txt:Total out-of-order packets: 0, missing packets: 5196
         --
         onPrem-send-5217.txt:Total UDP packets: 857122
         onPrem-send-5217.txt:Total out-of-order packets: 0, missing packets: 5423
         --
         onPrem-send-5218.txt:Total UDP packets: 857383
         onPrem-send-5218.txt:Total out-of-order packets: 0, missing packets: 5283
         --
         onPrem-send-5219.txt:Total UDP packets: 857313
         onPrem-send-5219.txt:Total out-of-order packets: 0, missing packets: 4934
         

  5. Access the device page to check the port throughput.

  6. If the `netstat` output shows read/write errors, TCP/UDP bulk flow tuning may be required.

  7. If there are out-of-order packets, the packet captures should be performed in the VPN Gateways for further analysis. For more information about performing packet captures in the VPN Gateways, [open a support case](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/getting-support). 

  8. If the `iperf3` UDP test achieves the desired throughput, the issue must be elsewhere and TCP tuning may be required.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
