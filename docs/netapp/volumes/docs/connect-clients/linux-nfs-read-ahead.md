---
url: https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-read-ahead/
title: Linux NFS read-ahead \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:31.516200+00:00
---

# Linux NFS read-ahead  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-read-ahead/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Linux NFS read-ahead Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to tune NFS read-ahead on Linux clients that mount NetApp Volumes. Read-ahead lets the kernel prefetch file blocks before an application requests them, which improves sequential read throughput. Read-ahead doesn't replace mount options or concurrency tuning; configure those first. For more information, see [Optimize Linux NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/optimize-linux-nfs-clients).

## Before you begin

Complete the following prerequisites before you tune NFS read-ahead:

  * If you plan to tune the slot table or session slots, complete [Linux NFS concurrency](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-concurrency) first.

  * Mount the volume with appropriate Linux NFS mount options, including `rsize`. For more information, see [Linux NFS mount options](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-mount-options).

  * Tune read-ahead after you mount the volume.




## Read-ahead overview

When an application reads a file sequentially, the Linux NFS client can request additional data beyond the current read. This hides network latency and raises throughput for sequential workloads, such as log playback, media streaming, bulk copy, and some analytics scans.

Read-ahead is configured per mount point. It is less effective for random-read workloads than for sequential read workloads.

## Defaults and rsize

Many Linux distributions set read-ahead to approximately 15 times `rsize`. Some distributions use a fixed 128 KiB read-ahead regardless of `rsize`, which can reduce sequential read performance after an upgrade. Check the current value on your mounted file system before you change it.

## View read-ahead for a mount

Each NFS mount point has a corresponding backing block device under `/sys/class/bdi/`. To find the backing block device identifier (BDI) and view the current `read_ahead_kb` value, complete the following steps:

  1. Locate the mount in `/proc/self/mountinfo` and note the BDI identifier in the third field.

  2. Read the value in kilobytes:
         
         cat /sys/class/bdi/BDEV/read_ahead_kb
         




## Choose a read-ahead value

Use the following guidelines to select an appropriate read-ahead value for your workload:

  * If you don't need maximum performance, keep your distribution's default and don't tune read-ahead.

  * Start with 15 times `rsize` (in KiB) if your distribution no longer sets it automatically.

  * For `rsize=1048576` (1 MiB), 15 times `rsize` is approximately 15,360 KiB (15 MiB).

  * Increase or decrease the value in steps and measure performance using your application and `nfsiostat`. Test values larger than 15,360 KiB before production use.




Read-ahead interacts with the page cache. Workloads that bypass the cache (`O_DIRECT`) don't benefit from read-ahead as sequential cached reads do.

## Persist read-ahead across reboots

Dynamic changes apply until you unmount or reboot. To persist these changes for NFS mounts, create a `udev` rule.

  1. Create `/etc/udev/rules.d/99-nfs-readahead.rules` and adjust the `read_ahead_kb` value as needed:
         
         SUBSYSTEM=="bdi", ACTION=="add", PROGRAM="/usr/bin/awk -v bdi=$kernel 'BEGIN{ret=1} {if ($4 == bdi) {ret=0}} END{exit ret}' /proc/fs/nfsfs/volumes", ATTR{read_ahead_kb}="15360"
         

  2. Use an absolute path to `awk` on your system in the `PROGRAM=` attribute.

  3. Reload `udev`:
         
         sudo udevadm control --reload
         

  4. Remount the NFS volumes or reboot to trigger the rules for new BDI devices.




Test the `udev` rules on a non-production host first. Incorrect rules might affect non-NFS block devices if the match expression is wrong.

## Workload guidance

Consider the following guidance based on your workload type when tuning read-ahead:

  * **Random reads (OLTP, small random I/O)** : keep the default read-ahead.

  * **Sequential reads (media, bulk copy, and some high performance computing)** : increase to 15 times `rsize` and measure.

  * **Mixed** : tune only if profiling shows a sequential-read bottleneck.

  * **Low`rsize` (64 KiB) with a 128 KiB default read-ahead**: consider increasing read-ahead to 960 KiB or higher.




Combine read-ahead tuning with appropriate `rsize`, `nconnect`, and concurrency settings.

## What's next

  * [Optimize Linux NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/optimize-linux-nfs-clients).

  * [Linux NFS concurrency](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-concurrency).

  * [Linux NFS mount options](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-mount-options).

  * [Connect NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients).

  * [Performance benchmarks](https://docs.cloud.google.com/netapp/volumes/docs/performance/performance-benchmarks).

  * [Monitor performance](https://docs.cloud.google.com/netapp/volumes/docs/performance/monitor-performance).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
