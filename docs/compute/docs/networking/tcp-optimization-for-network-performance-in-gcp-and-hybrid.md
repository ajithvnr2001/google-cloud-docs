---
url: https://docs.cloud.google.com/compute/docs/networking/tcp-optimization-for-network-performance-in-gcp-and-hybrid/
title: TCP optimization for network performance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:16.143378+00:00
---

# TCP optimization for network performance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/networking/tcp-optimization-for-network-performance-in-gcp-and-hybrid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  TCP optimization for network performance Stay organized with collections  Save and categorize content based on your preferences. 

The [global network](https://cloud.google.com/about/locations/#meet-our-network) in Google Cloud provides high reliability and low latency by connecting applications across regions and zones without leaving the Google network. However, the default Linux TCP/IP settings are often tuned for on-premises environments and can cause performance bottlenecks in the cloud.

For the best performance in Google Cloud, use the TCP/IP settings in this document which are specifically optimized for the cloud environment.

The settings mentioned in this document have been tested for use in the Google Cloud environment. The settings are primarily for internal instance communications and don't necessarily apply to communication between Compute Engine instances and external addresses.

## Understanding the Throughput Limit

TCP uses a "windowing" mechanism to manage data flow between a sender and receiver. The maximum achievable throughput is governed by the following relationship:
    
    
    Throughput <= window size / round-trip time (RTT) latency
    

In the original TCP design, the maximum window size is limited to 65535 bytes (64 KiB - 1), which often leaves modern high-speed networks underutilized as the sender waits for window updates.

## Shell script to optimize TCP performance

The following TCP configurations are recommended to improve performance:

  * Reduce MinRTO: Recover faster from packet loss by reducing retransmission delays.
  * Enable Fair Queueing: minimize congestion and drops due to application bursts.
  * Disable slow start after idle: restart at the last known good transfer rate after a connection idle period.
  * Disable TCP Cubic HyStart ACK train: ignore false-positive congestion signals when ramping up the data transfer rate.
  * Increase socket memory budgets: increase the maximum allowed amount of in-flight data per connection.
  * Enable hardware GRO: increase the efficiency of TCP/IP receive processing for large flows by combining data in fewer, larger packets.
  * Increase MTU to 4082 bytes: Increase transfer efficiency for large throughput flows.



You can enable these suggested settings with the following shell script. Before you run the script, make sure to replace `eth0` with the primary network interface for your compute instance.
    
    
    # Set DEV to your primary network interface
    DEV=eth0
    
    # 1. Reduce MinRTO
    sysctl -w net.ipv4.tcp_rto_min_us=5000
    
    # 2. Enable Fair Queueing
    tc qdisc replace dev $DEV root fq
    
    # 3. Disable slow start after idle
    sysctl -w net.ipv4.tcp_slow_start_after_idle=0
    
    # 4. Disable TCP Cubic HyStart ACK train
    echo 2 > /sys/module/tcp_cubic/parameters/hystart_detect
    
    # 5. Increase socket memory budgets
    echo 4194304 > /proc/sys/net/core/rmem_max
    echo 4194304 > /proc/sys/net/core/wmem_max
    echo 4194304 > /proc/sys/net/ipv4/tcp_notsent_lowat
    echo "4096 262144 16777216" > /proc/sys/net/ipv4/tcp_rmem
    echo "4096 262144 33554432" > /proc/sys/net/ipv4/tcp_wmem
    
    # 6. Enable hardware GRO
    ethtool -K $DEV rx-gro-hw on
    

The following sections describe each of the suggested configuration settings in more detail.

### Reduce MinRTO

Recover faster from packet loss by reducing retransmission delays.

The TCP retransmission timeout (RTO) controls how long a TCP sender waits for an `ACK` signal before retransmitting. Linux initializes the RTO to one second (per RFC 6298 section 2.1), then adjusts it over time to the round-trip time (RTT) plus a safety margin.

The Minimum RTO (MinRTO) implements a lower bound on this adjustment. If the RTO estimation is too low, it can introduce spurious retransmits, where the sender retransmits packets while the response is still in process.

The default MinRTO is 200 ms, which is unnecessarily conservative for modern cloud networks. A value of 5 ms has been extensively tested within Google Cloud and is a safe default for connections between modern Linux servers within Google Cloud.

Another factor is delayed ACKs, where the peer delays `ACK` responses. This delay allows batching ACKs across multiple data packets or combining an `ACK` with a data packet in the reverse direction. Delayed ACK timers are based on RTT, similar to the RTO timer.

Lowering the MinRTO speeds up loss repair on low RTT connections, such as connections within a zone or region. This adjustment does not affect behavior for connections that experience a high RTT, as it does not change their estimated RTT.

#### Configuring MinRTO

**Caution:** Setting the RTO timer too low can cause spurious retransmissions. You can use SNMP counters on Linux to detect the retransmissions. Likely indicators include the `TCPDSACKRecvSegs` and `TCPSpuriousRTOs` metrics.

You can configure MinRTO using one of two methods:

  1. **Using`sysctl` (Linux 6.11 and later):**

You can configure the default MinRTO using a `sysctl` command:
         
         sysctl -w net.ipv4.tcp_rto_min_us=5000
         

  2. **Using`ip route` (per-route control, or Linux versions earlier than 6.11):**

Alternatively, for older Linux versions or per-route control, MinRTO can be set on a per-route basis:
         
         ip route change default rto_min 5ms
         




The per-route approach is preferable in environments where connections might leave Google Cloud or communicate with non-Linux TCP/IP stacks. These systems might have different delayed ACK timers. For broad public Internet deployment, it is advised to keep the conservative default minRTO setting and apply the 5 ms setting only for routes within the Google Cloud Virtual Private Cloud (VPC).

### Enable fair queueing

Minimize congestion and packet drops caused by application bursts.

Unlike standard FIFO (First-In, First-Out) queues, Fair Queueing (FQ) distributes bandwidth fairly among different flows. It also paces traffic by enabling each TCP connection to compute its optimal delivery rate and time for each packet. If FQ is present, then the TCP stack relies on FQ to hold packets until their optimal delivery time. This pacing reduces bursts within a flow, which in turn minimizes packet drops and retransmissions.

To set the FQ traffic shaper as the network device traffic shaper, use the following `tc` (traffic control) command:
    
    
    tc qdisc replace dev $DEV root fq
    

On large instances with high egress bandwidth, the network device may have multiple transmit queues. For these instances it may be preferable to shard traffic shaping across transmit queues, by installing the Multi Queue (MQ) traffic shaper. This is a multiplexer which attaches an independent traffic shaper to each transmit queue. Per queue traffic shapers reduce contention on locks and cachelines across CPUs.

### Disable slow start after idle

Maintain high transfer rates after a connection has been idle.

To avoid congestion, TCP connections begin by sending data at a low rate and then exponentially increase the rate until packet loss is detected. This initial phase is known as _Slow Start_.

By default, TCP reverts to conservative "Slow Start" settings after an idle period. An idle period can be as short as one retransmission timeout (RTO), as defined in RFC 2581. Disabling this feature allows the connection to immediately resume at the last known good rate.

Where possible, applications should use long-lived connections over repeated connection establishment to the same peer. This avoids the cost of connection establishment, and maintains the congestion information. However, even with long-lived connections, after an idle period TCP forgets congestion information by default and reverts to the initial conservative setting and "Slow Start" phase.

**Caution:** Disabling `tcp_slow_start_after_idle` can cause a connection to send a large, line-rate burst of traffic (typically the full congestion window) when restarting from an idle state. This burst can lead to significant packet loss. To mitigate this risk, ensure the FQ packet scheduler is installed before enabling this optimization.

To disable the slow start after idle feature, use the following command:
    
    
    sysctl -w net.ipv4.tcp_slow_start_after_idle=0
    

### Disable TCP Cubic HyStart ACK train

Scale quickly to high transfer rates by ignoring false positive congestion signals.

The exponential growth rate of the "Slow Start" phase can be aggressive, potentially overshooting the optimal target rate. Hybrid Start (HyStart) is an additional mechanism designed to exit the "Slow Start" phase earlier by using two key congestion signals:

  * **Round Trip Time (RTT) delay** : measures the propagation delay of packets through the network. During periods of network congestion, packet queues build up at bottleneck links. This causes the RTT to increase which can signal the presence of congestion.
  * **ACK spacing** : relies on signals that packets are being delayed at a bottleneck, but focuses on the response ACKs. This mechanism assumes that, without congestion, ACKs will arrive with the same spacing as the original data packets. This pattern is often referred to as an ACK train. If ACKs are delayed beyond this expected pattern, it indicates that congestion might be present.

**Note:** ACK train detection has proven to be an unreliable congestion signal and is now considered obsolete. On Linux systems, TCP Cubic is the default congestion control algorithm; it provides options to disable all of HyStart or to selectively disable specific signals. On Windows systems, the HyStart++ algorithm, which is the default since 2021, has removed ACK train detection.

To optimize performance, disable ACK packet train detection while keeping the RTT delay mechanism enabled.
    
    
    echo 2 > /sys/module/tcp_cubic/parameters/hystart_detect
    

### Increase socket memory budgets

Increase maximum throughput on high RTT links by allowing more in-flight data.

The amount of data in-flight is a function of bandwidth and propagation delay, referred to as the _bandwidth delay product_ (BDP). The BDP is calculated as the bandwidth multiplied by the round-trip time (RTT), resulting in a value that specifies the optimal number of bits to send to fill the pipe:
    
    
    BDP (bits) = bandwidth (bits/second) * RTT (seconds)
    

All in-flight data has to remain buffered on the sender in case it has to be retransmitted. The TCP socket memory limits can directly limit achievable throughput by determining how much in-flight data can be buffered.

In Linux, the TCP socket memory limits are configured with the following `sysctl(8)` settings:

  * `net.core.rmem_max`
  * `net.core.wmem_max`
  * `net.ipv4.tcp_rmem`
  * `net.ipv4.tcp_wmem`



These TCP socket memory limits exist to avoid using up all system memory and causing out-of-memory (OOM) conditions, especially in workloads with many connections. Increasing these limits can increase throughput especially over high RTT paths. Unless the connection count is in the millions, there is little risk in increasing these limits.

These variables set upper bounds on socket buffer size, not direct memory allocation. Increasing these values does not affect the actual memory allocation for connections with low RTT, such as those within a Google Cloud zone.

The first two tunable parameters affect the maximum TCP window size for applications that set the TCP window size directly, which relatively few applications do. These limits bound what an application can explicitly ask for with socket options `SO_RCVBUF` and `SO_SNDBUF`.

For Linux kernel versions 6.18 and later, `net.core.rmem_max` and `net.core.wmem_max` default to 4 MB. Based on years of experience, these settings are considered safe. For earlier Linux versions, we recommend increasing these limits to 4 MB on modern platforms:
    
    
    echo 4194304 > /proc/sys/net/core/rmem_max
    echo 4194304 > /proc/sys/net/core/wmem_max
    

The second set of limits, `net.ipv4.tcp_rmem` and `net.ipv4.tcp_wmem`, manages the TCP send and receive buffer auto-tuning limits.

Each of these settings takes three values: minimum, initial default, and maximum socket memory size. The default maximum values are often more conservative than needed on modern platforms, for example:

  * `tcp_rmem`: 4096, 131072, 6291456
  * `tcp_wmem`: 4096, 16384, 4194304



The TCP stack autosizes the TCP send and receive buffers based on estimates of RTT and congestion window. A maximum write buffer size of 4194304, or 4 MB, is small for high RTT connections; with a 100 ms RTT, this setting limits throughput to 40 MB/s in the best case. Instead of trying to calculate what values to use, a simpler approach is to use safe defaults for modern servers that have many GB of RAM.

As an extra precaution, we recommend limiting the amount of data that can be queued in the socket but not yet sent. While the goal of increasing maximum `wmem` is to allow more data in-flight, a process can write to the socket faster than TCP can send it, causing a queue of unsent data to build up on the host and waste memory. To prevent this, limit the amount of not-yet-sent data by setting `tcp_notsent_lowat`, and then increase the overall `wmem` limit to allow for larger in-flight buffers

Unless a server has millions of connections, the following settings should be safe. But, if you experience out-of-memory conditions with many connections, then use a lower maximum buffer size.
    
    
    echo 4194304 > /proc/sys/net/ipv4/tcp_notsent_lowat
    
    echo "4096 262144 16777216" > /proc/sys/net/ipv4/tcp_rmem
    echo "4096 262144 33554432" > /proc/sys/net/ipv4/tcp_wmem
    

### Enable hardware GRO

Increase efficiency of TCP/IP receive processing for large flows. Reduce CPU overhead by batching received packets

For most TCP/IP operations, CPU cycle cost scales with packet rate, not byte rate. To mitigate this overhead on transmission, modern operating systems send TCP data through the transmit path in large packets that hold multiple TCP segments. These can range up to 64KB, or even hundreds of Kilobytes with Linux BIG-TCP.

Such large packets exceed the maximum packet size on the network, the MTU. This operating system optimization relies on network device support to split up these packets and send them out as a train of smaller packets, each holding a single TCP segment. This support, TCP Segmentation Offload (TSO), is widely available and enabled by default.

On reception, GVNIC devices on third generation and newer platforms can perform the inverse: briefly buffer segments in the device to see if consecutive segments arrive, and if so combine them and forward them as multi-segment packets to the host. This feature is variously known as Receive Segment Coalescing (RSC) in Windows, Large Receive Offload (LRO) or Hardware Generic Receive Offload (HW-GRO) in Linux. HW-GRO is a more strict refinement of LRO.

HW-GRO is safe to be enabled by default. This eventually happens where available.

In the meantime, on platforms with GVNIC devices that support the feature, enable HW-GRO using ethtool. Depending on the kernel and driver version, the feature is advertised as LRO or HW-GRO. The implementation is the same regardless of the name.
    
    
        ethtool -K $DEV large-receive-offload on
        ethtool -K $DEV rx-gro-hw on
    

### Increase MTU size to 4082 bytes

Increase data transfer efficiency for large throughput flows.

Increasing the packet size, similar to TSO and HW-GRO optimizations, boosts transfer efficiency because most processing work is done per packet, not per byte.

Google Cloud VPC networks can support packets up to 8898 bytes, which is significantly larger than the default MTU of 1460 bytes. Using a larger network packet size reduces the CPU cycles spent per byte of throughput (goodput).

#### Optimal packet size considerations

While larger packets are generally better, the maximum possible MTU is not always the optimal choice. The efficiency gained from sending fewer packets must be balanced against the following costs:

  * **Memory Usage** : Larger buffers require more memory assigned to the network device for packet reception. If you have many queues, a substantial amount of memory can be left unused (stranded).
  * **Small Packet Handling** : Larger buffers handle small packets, such as pure acknowledgements (ACKs), less efficiently.
  * **CPU Allocation Costs** : Datapath costs are significantly impacted by memory allocation and freeing. Aligning the packet size to a multiple of memory pages helps optimize this CPU cost.
  * **TSO Interaction** : Packet size subtly affects TCP Segmentation Offload (TSO). To build the largest possible TSO packet, you might need to choose a smaller maximum segment size (MSS). For example, given the largest possible IP packet of 64 KB including headers, a 4 KB MSS results in a larger payload (60 KB) than an 8 KB MSS (56 KB).



For most workloads, the difference in efficiency between 4 KB, 8 KB, or 9 KB MTUs is small. However, any of these is a significant improvement over the default 1460-byte packets.

#### Recommendation for page sized packets

As a robust and generally efficient option, we advise [setting the MTU size](https://docs.cloud.google.com/vpc/docs/change-mtu-vpc-network) for your VPC network to 4082 bytes. This size is recommended because it allows the entire Ethernet packet to fit within a 4096-byte memory page, which optimizes memory page allocation. This recommendation is for the Layer-3 MTU, which includes the IP header, but excludes the 14-byte Ethernet link layer.

#### IP MTU configuration

You can configure the MTU for each VPC network directly through the Google Cloud console.

For most Linux distributions in Google Cloud, no manual configuration is needed on the compute instance. The instance automatically learns the network MTU using DHCP during boot (using option 26). The instance then sets the network device MTU to match. We recommend using this auto-configuration.

If manual configuration is necessary, the network device MTU can be set to a value lower than the VPC network MTU using the following command:
    
    
    ip link set dev $DEV mtu 4082
    

#### Set different MTU sizes for specific routes

If your compute instance communicates externally outside the VPC, where the path MTU might be lower, then setting MTU on specific routes is the preferred option. In this scenario, set the default MTU to the conservative 1460 bytes and apply the higher MTU, for example, 4082 bytes, only for intra-VPC routes:
    
    
    #Set intra-VPC route MTU:
    ip -4 route change $SUBNET/$MASK dev $DEV mtu 4082
    #Set default route MTU:
    ip -4 route change default dev $DEV mtu 1460
    

#### Configure the TCP Maximum Segment Size (MSS)

The TCP Maximum Segment Size (MSS) determines the packet payload size for a TCP connection. Since TCP/IP packets must not exceed the MTU size to prevent fragmentation or packet drops, the MSS must be scaled accordingly.

In general, you don't need to configure TCP MSS manually, because the operating system automatically derives it from the path MTU.

MSS covers the payload and TCP options, but _excludes_ the 20-byte IPv4 header and 20-byte TCP header. Therefore, on an IPv4 network, the MSS is typically 40 bytes smaller than the MTU.

If you prefer a smaller MSS for specific traffic, you can configure it on a per-route basis. For example, if your VPC network and device MTU use the maximum (8896 bytes) for general traffic, but you want to use 4 KB MTU for TCP traffic, you can use the following command:
    
    
    ip -4 route change default dev $DEV advmss 4042
    

#### Header split mode

The gVNIC `gve` driver in Linux kernel versions 6.9 and later supports TCP header-data split (`tcp-data-split`), which is disabled by default.

**Caution:** On Linux kernel versions before 7.1, enabling `tcp-data-split` and LRO or hardware GRO (HW-GRO) at the same time on gVNIC network interfaces can lead to data corruption and severe performance degradation. If you need to enable receive header split on these kernel versions, then you must disable hardware GRO using commands such as the following:

  * `ethtool -K $DEV rx-gro-hw off`
  * `ethtool -K $DEV large-receive-offload off`



Header split separates packet headers and data into distinct buffers. This enables filling an entire memory page with 4096 bytes of data. This separation enables crucial optimizations, such as replacing expensive kernel-to-userspace copying operations with cheaper memory page mapping operations (for example, using Linux `TCP_ZEROCOPY_RECEIVE`).

When the receive header split feature is enabled, the MTU calculation changes. The optimal MTU is one where all headers map onto the header buffer and the payload buffer fills a whole page of data. With header split enabled:

  * A header buffer holds: 
    * Ethernet (14 bytes)
    * IPv4 (20 bytes)
    * TCP (20 bytes) headers
    * Common TCP options (12 bytes for default configuration with TCP timestamps)
  * The data buffer holds 4096 bytes of payload data.



This results in a total frame size of 4162 bytes, and thus an MTU of 4148 bytes.

## What's next

  * Read the blog post on [5 steps to better Google Cloud networking performance](https://cloud.google.com/blog/products/gcp/5-steps-to-better-gcp-network-performance).
  * Learn about [Global Networking Products](https://cloud.google.com/products/networking/).
  * Learn about [Networking Tiers](https://cloud.google.com/blog/products/gcp/introducing-network-service-tiers-your-cloud-network-your-way) on Google Cloud.
  * Learn how to [benchmark network performance](https://docs.cloud.google.com/compute/docs/networking/benchmarking-higher-bandwidth-vms).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
