---
url: https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-concurrency/
title: Linux NFS concurrency \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:03.074547+00:00
---

# Linux NFS concurrency  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-concurrency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Linux NFS concurrency Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to tune Linux NFS client concurrency for NetApp Volumes.

Concurrency is the number of NFS operations that can be outstanding between a client and the volume at one time. Tuning concurrency helps you align the client with server limits and avoid performance degradation from excessive queue depth.

On Linux, concurrency is controlled by slot table entries (NFSv3) or NFSv4.1 session slots, instead of mount options. Configure these settings before you mount, or remount NFS file systems after you change them.

To learn about mount options, such as `nconnect`, see [Linux NFS mount options](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-mount-options). For more information about configuration order, see [Optimize Linux NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/optimize-linux-nfs-clients).

## Terminology

The following key terms are related to Linux NFS concurrency:

  * **RPC slot table** : per-TCP-connection limit on outstanding NFS RPC operations on the client (NFSv3).

  * **Session slots** : NFSv4.1 limit on outstanding commands negotiated for a session between the client and the server.

  * **Storage endpoint** : a single volume IP address that clients mount.

  * **nconnect** : a mount option that opens multiple TCP connections to the same endpoint; it multiplies the concurrency per connection.




## Linux parameters

The following table lists the parameters and configuration files used to configure NFS concurrency for each protocol version:

Protocol | Parameter | Configuration  
---|---|---  
NFSv3 | `sunrpc.tcp_max_slot_table_entries` | `/etc/sysctl.conf`, `sysctl -p`  
NFSv3 | `sunrpc.tcp_slot_table_entries` | Some distributions; see your distribution documentation  
NFSv4.1 | `max_session_slots` | `/etc/modprobe.d/` (for example, `nfsclient.conf`), reboot  
  
## NFSv3

The following sections describe NFSv3 client and server limits, how `nconnect` affects concurrency, how to estimate concurrency requirements, and how to configure slot limits.

### Client and server limits

NFSv3 doesn't negotiate concurrency between client and server. Each side applies its own limit.

  * **NetApp Volumes NFSv3 server** : up to 128 execution contexts per TCP connection.

  * **Modern Linux client (default)** : `sunrpc.tcp_max_slot_table_entries = 65536`.




A default client slot count that exceeds the server limit is unnecessary. If the client sends more outstanding operations than the server handles efficiently, the server can reduce the TCP window, which affects performance.

**Recommendation** : set `sunrpc.tcp_max_slot_table_entries` to 128 or less per connection. For environments with many clients and connections, keep the total outstanding slot usage per storage endpoint at 10,000 or less.

### How nconnect affects NFSv3 concurrency

The approximate maximum concurrency for one client is calculated as follows:

(`sunrpc.tcp_max_slot_table_entries per connection`) x (`nconnect value`)

The concurrency value is capped by the server per connection (128) and by your workload requirements.

#### Example 1: Default slots, no nconnect

  * One TCP connection.

  * The client can attempt up to 65,536 outstanding operations, but the server accepts up to 128 per connection.

  * The effective concurrency bounded by the server limit of 128.




#### Example 2: 128 slots, no nconnect

  * `sunrpc.tcp_max_slot_table_entries=128`

  * One connection.

  * The client and server align at 128 outstanding operations.




#### Example 3: 100 slots, nconnect=8

  * Eight TCP connections.

  * Up to 100 outstanding operations per connection.

  * Up to 800 outstanding operations from one client (8 x 100), subject to per-connection server limit of 128.




#### Example 4: Many clients (EDA-style)

  * 250 clients, each with `sunrpc.tcp_max_slot_table_entries=8` and without `nconnect`.

  * Each client has up to eight outstanding operations per connection.

  * Total across clients: up to 2,000 outstanding operations to one volume IP (250 x 8), which is within the 10,000-slot endpoint guideline.




When you scale out clients, use lower per-client slot values. Use `nconnect` on individual high-throughput clients, not as a substitute for farm-wide slot planning.

### Estimate required concurrency using Little's Law

Use the following formula to estimate the concurrency required for your workload:

Concurrency = (operation_rate) x (latency_in_seconds)

#### Example: Many clients, one endpoint

Target 4,000 MiBps with 256 KiB average I/O and 10 ms latency:

  * Operation rate: approximately 16,000 IOPS.

  * Concurrency: approximately 16,000 x 0.010 = 160.

  * With 1,250 clients: 160 / 1,250 = approximately 0.13 slots per client if split evenly. Use a small integer per client, such as 2, 4, or 8, to maintain headroom under the 10,000 slot ceiling.




### Set sunrpc.tcp_max_slot_table_entries (NFSv3)

On many Linux distributions, `systemd-sysctl` runs before the `sunrpc` kernel module is loaded. Entries in `/etc/sysctl.conf` or `/etc/sysctl.d/` for `sunrpc.*` are ignored at boot. Running `sysctl -p` after boot works only until the next reboot if you don't use one of the following persistence methods.

**Method 1** : If testing shows that a value lower than 128 is sufficient, use that value. Set both `tcp_slot_table_entries` and `tcp_max_slot_table_entries` to the same value unless your distribution documentation says otherwise.

Mount or remount NFS file systems after you change these settings. Slot settings apply to RPC transports that are created after the setting is in effect.

**Method 2 (Recommended)** : module options in `/etc/modprobe.d/`

Module parameters are applied when `sunrpc` loads on the first NFS use after boot. These settings persist across reboots, which avoids the need for boot-time `sysctl` configuration.

  1. Create `/etc/modprobe.d/sunrpc.conf`:
         
         options sunrpc tcp_slot_table_entries=128 tcp_max_slot_table_entries=128
         

  2. Rebuild the initramfs if your distribution requires it after modprobe changes, which is common on RHEL when the module is in the initramfs. For more information, see your Linux vendor documentation.

  3. Reboot, or unload and reload `sunrpc` only if you have no active NFS mounts and your runbook allows it.

  4. Verify that `sunrpc` is loaded and the intended values are set:
         
         cat /proc/sys/sunrpc/tcp_slot_table_entries
         cat /proc/sys/sunrpc/tcp_max_slot_table_entries
         

  5. Mount or remount the NetApp Volumes exports.




## NFSv4.1

The following sections describe how NFSv4.1 session negotiation works, provide performance optimization examples, and explain how to configure session slot limits.

### Session negotiation

NFSv4.1 establishes sessions between the client and the server. The client and the server negotiate the maximum number of outstanding commands (`max_reqs`) by selecting the lower of the two supported values.

  * **NetApp Volumes NFSv4.1 server** : 180 commands per session.

  * **Linux client default** : 64 (`max_session_slots`).

  * **Negotiated session** : the minimum of the client and server values, which is often 64 with the default client.




Each TCP connection to the server supports up to 128 outstanding NFS commands. With the default of 64 session slots and a single connection, concurrency is limited to 64. To use more session slots across connections, use `nconnect=2` or higher only for non-Kerberos mounts. For more information about mount options, see [Linux NFS mount options](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-mount-options).

**Important:** Don't use `nconnect` with `sec=krb5`, `krb5i`, or `krb5p`.

**Example 1** : **Default 64 session slots, no nconnect**

  * One connection.

  * Up to 64 outstanding commands for the session.




**Example 2** : **64 session slots, nconnect=2**

  * The session remains limited to 64 total slots, which are split across two connections, or approximately 32 per connection.

  * This configuration improves latency by lowering queue depth per connection without increasing total concurrency.




**Example 3** : **max_session_slots=180, no nconnect**

  * The session allows 180 commands, and one connection is limited to 128 outstanding operations.

  * The effective limit is 128.




**Example 4** : **max_session_slots=180, nconnect=2**

  * The session can use up to 180 commands across two connections, or approximately 90 per connection.

  * This configuration is needed to exceed the single-connection 128 cap at the session level.




To achieve maximum NFSv4.1 concurrency on the NetApp Volumes without Kerberos, set `max_session_slots=180` and use `nconnect=2` or higher. Test this configuration with your workload.

## Set max session slots for NFSv4.1

  1. Create `/etc/modprobe.d/nfsclient.conf`:
         
         options nfs max_session_slots=180
         

**Important:** Don't use quotation marks around the value in this file.
  2. Reboot the client.

  3. Verify the configuration after at least one NFSv4.1 mount exists:
         
         systool -v -m nfs
         

  4. Confirm that `max_session_slots` appears in the output.




These changes require a reboot on standard Linux NFS client packaging. Plan your maintenance accordingly.

## Multi-client and large capacity volumes

  * **Multiple VMs, one volume IP** : reduce `sunrpc.tcp_max_slot_table_entries` per client.

  * **Large capacity volumes with multiple IPs** : slot limits apply per client-to-IP connection. Spread clients across endpoints when possible. For more information, see [Connect large capacity volumes with multiple storage endpoints](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-large-capacity-volumes).




## What's next

  * [Linux NFS mount options](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-mount-options).

  * [Linux NFS read-ahead](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-read-ahead).

  * [Optimize Linux NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/optimize-linux-nfs-clients).

  * [Connect NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients).

  * [Performance benchmarks](https://docs.cloud.google.com/netapp/volumes/docs/performance/performance-benchmarks).

  * [Monitor performance](https://docs.cloud.google.com/netapp/volumes/docs/performance/monitor-performance).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
