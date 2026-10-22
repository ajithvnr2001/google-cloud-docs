---
url: https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-mount-options/
title: Linux NFS mount options \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:55.277377+00:00
---

# Linux NFS mount options  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-mount-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Linux NFS mount options Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Linux NFS mount options that affect performance and behavior when mounting NetApp Volumes exports. You set these options when running the `mount` command or by adding them to `/etc/fstab`.

For the recommended setup order and information about how mount options interact with kernel concurrency and read-ahead, see [Optimize Linux NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/optimize-linux-nfs-clients).

For mount commands and export access examples, see [Connect NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients).

## Before you begin

Complete the following requirements before you mount NetApp Volumes:

  * Use the mount command from the Google Cloud console mount instructions unless your workload needs different options.

  * If you tune concurrency with slot table or session slot settings, configure those settings before mounting. For more information, see [Linux NFS concurrency](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-concurrency).

  * Test any changes in a non-production environment. The effect of mount options can vary based on the workload, Linux version, and network latency.




## Quick reference

The following table provides a quick reference of common mount options based on your workload goals:

Goal | Options to consider | Notes  
---|---|---  
General purpose | Use Google Cloud console mount instructions | Includes protocol-appropriate defaults  
Higher throughput or IOPS from one VM | `nconnect=8` to `nconnect=16`, tune `rsize` and `wsize` | Set slot table first; see [Linux NFS concurrency](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-concurrency)  
Lower latency for databases | `rsize=262144`, `wsize=262144`, `hard`, `timeo=600`, `vers=4.1` | Test for your specific application  
Specify NFS version | `vers=3` or `vers=4.1` | Linux mounts the highest version available by default  
NFSv3 without advisory locks | `vers=3`, `nolock` | For firewall and lock manager guidance, see [Connect NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients)  
Kerberos NFSv4.1 | `sec=krb5`, `krb5i`, or `krb5p` | Don't use with `nconnect`  
Read-mostly data with known coherency trade-offs | `nocto`, `actimeo=` | Advanced; understand cache behavior first  
  
Always include `tcp` when you mount NFSv3. Although Linux uses TCP for NFS traffic by default, explicitly adding `tcp` helps ensure the mount process uses TCP instead of UDP. This helps improve performance when many systems attempt to mount at the same time. Include `noatime` to reduce metadata operations.

## Recommended mount profiles

The following mount profiles provide recommended options based on your performance requirements, protocol versions, and client scale. When executing these commands, replace `VOLUME_IP` and `/export_path` with the actual values from the mount instructions in the Google Cloud console.

**Profile A** : **Default (console)**

Run the mount command provided in the Google Cloud console without changes.

**Profile B** : **Performance-oriented (single Linux client)**

Example for NFSv3, aligned with performance benchmarks test configuration:
    
    
     sudo mount -t nfs -o hard,tcp,vers=3,rsize=262144,wsize=262144,nconnect=16 \
     VOLUME_IP:/export_path /mnt/volume
    

Benchmarks use `nconnect=16` and 64 KiB `rsize` and `wsize`. Many workloads perform well with `nconnect=8`. Test both values.

**Profile C** : **NFSv4.1 with explicit version**
    
    
     sudo mount -t nfs -o vers=4.1,hard,rsize=262144,wsize=262144 \
     VOLUME_IP:/export_path /mnt/volume
    

To prevent the automatic mount of NFSv4.2 when it's enabled on the volume, specify `vers=4.1`. For more information, see [Connect NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients).

**Profile D** : **NFSv3 for compute farms**

If you connect a large number of clients to a volume (for example, hundreds), don't use `nconnect` to prevent exhausting the available TCP sessions on the volume.
    
    
     sudo mount -t nfs -o vers=3,nolock,hard,tcp,rsize=262144,wsize=262144 \
     VOLUME_IP:/export_path /mnt/volume
    

## Persist in /etc/fstab

The following example shows an /etc/fstab line for NFSv4.1:
    
    
     VOLUME_IP:/export_path  /mnt/volume  nfs  vers=4.1,hard,tcp,rsize=262144,wsize=262144,timeo=600,_netdev  0  0
    

Use the `_netdev` option so that the system waits for networking before mounting.

## nconnect

The `nconnect` mount option lets you control the number of TCP connections the NFS client opens to the same storage endpoint, which is the volume IP address. Each connection handles multiple NFS operations at the same time, up to a set limit. Increasing the number of connections improves I/O concurrency and throughput from a single client.

### Recommendations

Consider the following recommendations when configuring the `nconnect` mount option:

  * Test `nconnect=8` and `nconnect=16`. Values up to 16 are supported.

  * Use `nconnect` only for dedicated high-performance clients. If many clients, for example a compute farm, connect to the same storage, avoid using `nconnect`.

  * Perform the first mount operation to a given volume IP to set the `nconnect` value for that IP on that client. Later mounts to the same IP use the same value, even if they specify a different one. Mount the export with the selected `nconnect` value first, or use the same option for all mounts to that IP.

  * Note that setting `nconnect` for one volume IP doesn't affect mounts to a different volume IP.

  * Verify that your Linux distribution supports `nconnect` before using it.


**Caution:** Don't use `nconnect` with Kerberos mount security (`sec=krb5`, `sec=krb5i`, or `sec=krb5p`). The Generic Security Services (GSS) security context is shared across `nconnect` connections. Out-of-order packets might force security context renegotiation and negatively affect performance.

For more information about slot limits per connection, see [Linux NFS concurrency](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-concurrency).

## rsize and wsize

The `rsize` and `wsize` mount options set the maximum transfer size for NFS read and write operations. If you omit them, the client and server negotiate the largest size both support, which is up to 1 MiB on Linux clients and NetApp Volumes.

### Recommendations

Consider the following recommendations when configuring the `rsize` and `wsize` mount options:

  * Test `rsize=262144` and `wsize=262144` (256 KiB) to tune throughput and latency for latency-sensitive applications.

  * Use values larger than 256 KiB with caution because they can increase latency or reduce throughput for some workloads; measure the performance before deployment.

  * Use `rsize=65536` and `wsize=65536` (64 KiB) for NFSv3 tests, as these values were used in [performance benchmarks](https://docs.cloud.google.com/netapp/volumes/docs/performance/performance-benchmarks).




Note that these settings have minimal effect on random workloads, which typically use smaller operation sizes than `rsize` and `wsize`, while sequential I/O through the page cache often uses operation sizes up to `rsize` and `wsize`.

The `rsize` mount option affects read-ahead behavior. For more information, see [Linux NFS read-ahead](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-read-ahead).

## Protocol version

The following table lists the `vers` option values and their corresponding protocol versions:

Option | Use  
---|---  
`vers=3` | NFSv3  
`vers=4.1` | NFSv4.1  
`vers=4.2` | NFSv4.2  
  
If you don't set `vers`, the Linux `mount` command uses the highest NFS version supported by the client and volume. Flex Unified, Standard, Premium, and Extreme volumes with NFSv4.1 enabled also support NFSv4.2. You can mount NFSv4.2 unless you specify `vers=4.1`.

For more information about NFSv4.1 identity mapping, Kerberos, and numeric IDs, see [Connect NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients).

## hard, timeo, and retrans

The `hard`, `timeo`, and `retrans` mount options manage client behavior and timeout retry logic when connection issues occur:

  * `hard`: retries NFS requests until they succeed. This option is typical for data integrity on production workloads.

  * `timeo`: specifies the timeout in tenths of a second before a request is retried. Database-oriented workloads often use `timeo=600` (60 seconds).

  * `retrans`: specifies the number of retries. Google Cloud console defaults are usually sufficient unless your runbooks specify otherwise.




## NFSv3 nolock option

NFSv3 advisory locking uses the Network Lock Manager (NLM) and requires client-side `rpc.statd` and [firewall rules](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients#firewall_rules_for_nfs_volumes_access) for callback ports. If you don't use advisory locks, mount with `nolock` to avoid lock manager traffic.

NFSv4.1 implements locking in the protocol on port `2049`; clients don't need separate lock manager ingress rules.

For more information about advisory lock use with NFSv3 and firewall rules for NFS volumes access, see [Connect NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients).

## Cache and consistency using nocto and actimeo

The NFS client uses a loose consistency model. Attribute cache timers determine how long the client trusts file and directory metadata before it contacts the server. The default close-to-open consistency (`cto`) refreshes file data when you open a file.

  * `nocto`: the client doesn't force server consistency on open. This reduces `getattr` calls but increases the risk of stale data.

  * `actimeo=N`: configures all attribute cache timers to `N` seconds (`acregmin`, `acregmax`, `acdirmin`, and `acdirmax`).




Consider using `nocto` and higher `actimeo` values in the following scenarios:

  * A single writer or read-only consumers that receive updates through another path.

  * Large static datasets, such as EDA libraries, web content, or render textures, if brief staleness is acceptable.


**Caution:** Don't use `nocto` or higher `actimeo` on shared read and write data unless you understand your application's coherency requirements. Incorrect use can cause applications to read stale metadata or directory listings.

In most cases, use the recommended Linux defaults for attribute caching:

  * **Regular files minimum and maximum** : `acregmin=3` seconds and `acregmax=60` seconds

  * **Directories minimum and maximum** : `acdirmin=30` seconds and `acdirmax=60` seconds




Lowering these values increases the load on the NFS server and can reduce performance. Avoid `actimeo=0` except for very specific use cases where you understand the impact.

## Other common options

The following other common mount options are available for NFS clients:

  * `rw` or `ro`: read-write or read-only mount.

  * `noatime`: don't update the access time on read, as this reduces metadata operations and is a recommended practice.

  * `sec=sys`: AUTH_SYS, that is the default for non-Kerberos exports.

  * `_netdev`: use this in `fstab` to mount after the network is available.




## What's next

  * [Linux NFS read-ahead](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-read-ahead).

  * [Linux NFS concurrency](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-concurrency).

  * [Optimize Linux NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/optimize-linux-nfs-clients).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
