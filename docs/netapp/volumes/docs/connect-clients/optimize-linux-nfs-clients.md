---
url: https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/optimize-linux-nfs-clients/
title: Optimize Linux NFS clients \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:52.110877+00:00
---

# Optimize Linux NFS clients  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/optimize-linux-nfs-clients/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Optimize Linux NFS clients Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to tune Linux NFS clients that mount NetApp Volumes exports. For many workloads, tuning isn't required. Unless you need higher throughput, more IOPS, lower metadata load on the volume, or specific caching behavior, use the mount command from the Google Cloud console.

For more information about connection steps, export policy setup, and mount commands, see [Connect NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients).

## Configure clients

Configure Linux NFS settings in the following order:

  1. **Kernel concurrency** : before mounting the file system, set the number of NFS request slots (slot table entries for NFSv3 or session slots for NFSv4.1). If you change settings, you must remount the file system. For more information, see [Linux NFS concurrency](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-concurrency).

  2. **Mount options** : choose the protocol version, I/O size, TCP connection count, locking, and cache-related options at mount time. For more information, see [Linux NFS mount options](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-mount-options).

  3. **Read-ahead** : adjust the sequential read prefetch per mount point after the volume is mounted. For more information, see [Linux NFS read-ahead](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-read-ahead).




The following table summarizes these configuration steps:

Step | When | What it controls | Where to configure | Guide  
---|---|---|---|---  
1 | Before the first mount, or before remount | Outstanding RPC operations per TCP connection; NFSv4.1 commands per session | `/etc/sysctl.conf`,  
`/etc/modprobe.d/` | [Linux NFS concurrency](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-concurrency)  
2 | At mount | Protocol, I/O transfer size, number of connections, locking, and attribute cache | `mount -o`, `/etc/fstab` | [Linux NFS mount options](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/\(/netapp/volumes/docs/connect-clients/linux-nfs-mount-options\))  
3 | After mount | Sequential read prefetch | `/sys/class/bdi/.../read_ahead_kb`, udev rules | [Linux NFS read-ahead](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-read-ahead)  
**Note:** Step 1 in the preceding table only applies to mounts created after the kernel setting takes effect. Changes to NFSv4.1 `max_session_slots` might require a reboot.

## How the settings work together

The Linux kernel defines per-connection concurrency (Step 1 in the preceding table). The `nconnect` mount option (Step 2 in the preceding table) lets you open multiple TCP connections from one client to the same volume IP address.

The approximate concurrency for one client is calculated as follows:

(`slots per connection`) x (`nconnect value`)

Each TCP connection to a NetApp Volumes NFS endpoint supports up to 128 outstanding operations per connection for NFSv3. NFSv4.1 also negotiates session-level limits; a single TCP connection can cap effective concurrency below the session maximum. For more information, see [Linux NFS concurrency](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-concurrency).

If multiple clients mount the same volume IP address, use a lower per-client slot limit so that the total outstanding operations across the client fleet remains within recommended limits.

You configure read-ahead per mount point (Step 3 in the preceding table). It depends on your `rsize` mount option and on Linux distribution defaults. Some distributions use a fixed 128 KiB read-ahead regardless of `rsize`, which can reduce sequential read performance until you adjust it.

Mount options and kernel settings don't change export policies, Kerberos configuration, firewall requirements, or volume service-level throughput and IOPS limits.

## Workload starting points

The following table provides starting points. Validate settings with your application, Linux distribution, and network path.

Workload | Kernel concurrency | Mount options | Read-ahead  
---|---|---|---  
General purpose | Operating system default | Use the mount instructions from the Google Cloud console | Operating system default  
Single VM, high throughput/IOPS | 

  * Cap per-connection slot table at 128 or less
  * For NFSv4.1, set `max_session_slots` up to server maximum
  * Use `nconnect=2` or higher if you need more than 128 outstanding operations

| 

  * `nconnect=8` to `nconnect=16`
  * Adjust `rsize` and `wsize`

| Tune if workloads are sequential-read bound  
Many clients (EDA/HPC/render farm) | 

  * Low slots per client (for example, 8)
  * Keep total slots per volume IP under recommended limits

| 

  * Often NFSv3
  * No `nconnect`
  * Spread clients across multiple volume IPs for large capacity volumes

| Often higher for large, static datasets  
Kerberos NFSv4.1 | 

  * Tune `max_session_slots`
  * Don't rely on `nconnect` for performance

| 

  * `sec=krb5`, `krb5i`, or `krb5p`
  * Don't combine with `nconnect`

| As needed for sequential reads  
NFSv3 without advisory locks | Operating system default | 

  * `vers=3`, `nolock` if you don't use lock manager
  * See [Connect NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients)

| As needed  
  
## Measure and validate tuning

After you update client settings, complete the following steps:

  * Run `nfsiostat`, `mountstats`, and `nfsstat` on the client. For more information, see [Monitor performance](https://docs.cloud.google.com/netapp/volumes/docs/performance/monitor-performance).

  * Compare your results to [performance benchmarks](https://docs.cloud.google.com/netapp/volumes/docs/performance/performance-benchmarks). These benchmarks used `nconnect=16`, `rsize=65536`, and `wsize=65536` for some NFSv3 tests on Red Hat Enterprise Linux 9.




Tuning the client improves the efficiency of the network path usage to the volume for a virtual machine (VM). Volume capacity, service level, storage pool limits, and Compute Engine VM size might still limit results.

## What's next

  * Tune concurrency: [Linux NFS concurrency](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-concurrency).

  * Tune mount options: [Linux NFS mount options](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-mount-options).

  * Tune sequential reads: [Linux NFS read-ahead](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-read-ahead).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
