---
url: https://docs.cloud.google.com/netapp/volumes/docs/performance/monitor-performance/
title: Monitor performance \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:37.165422+00:00
---

# Monitor performance  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/performance/monitor-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Monitor performance Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to monitor Google Cloud NetApp Volumes performance to keep your applications running efficiently. Tracking key metrics helps you identify and resolve performance issues.

Use Cloud Monitoring for an overview of performance trends.

## Use Cloud Monitoring to track volume performance statistics

[Cloud Monitoring](https://console.cloud.google.com/monitoring) tracks multiple performance metrics per volume that let you observe current and short-lived performance events. Metrics update every five minutes and provide an overview of performance trends, for periods of one day or longer. For more information, see [NetApp Volumes Cloud Monitoring metrics](https://docs.cloud.google.com/netapp/volumes/docs/monitor/cloud-monitoring-metrics).

## Collect NFS performance statistics on your Linux operating system

You can collect Network File System (NFS) performance statistics on your Linux operating system using the following statistics:

  * **`nfsiostat`** : provides IOPS (`ops/s`), throughput (`kB/s`), blocksize (`kB/op`), and latency (average round-trip time (`ms`)) metrics. The information is split into read and write per NFS mount and is used to monitor traffic in real time.

  * **`mountstats`** : provides details about each NFS mount by NFS operation type. Each operation type shows the number of requests, the average number of transferred bytes, and the average latency.

  * **`nfsstat`** : provides details on how often NFS operations are called. This statistic can be used to determine the read and write ratio of your workload and helps to determine how metadata-intensive (metadata operations versus read and write) it is.




If your Linux installation doesn't provide these tools, consult your distributions package management system to determine which package provides them. For Debian-based systems like Ubuntu, they are provided in `nfs-common`.

## Review SMB performance statistics using Windows

Windows clients provide real-time performance metrics through [Windows Performance Monitor](https://learn.microsoft.com/en-us/training/modules/monitor-windows-server-performance/2-use-performance-monitor-to-identify-performance-problems).

The Performance Monitor application and command line can be used to access the metrics, show real-time graphs, and collect data to create reports. For more information, see [perfmon](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/perfmon).

You can map a network share to see performance metrics like IOPS and latency. Server Message Block (SMB) metrics are found under **SMB Client Shares** and metrics are available for every mapped share.

The following table shows the NetApp Volumes metrics and their corresponding names in the Windows Performance Monitor.

Metric | SMB client shares performance monitor name  
---|---  
Block size | Average data bytes per request  
Latency | Average seconds per data request. Use scale 1,000 for milliseconds  
IOPS | Data requests per second  
Throughput | Data bytes per second  
Concurrency | Average data queue length and current data queue length  
Read and write ratio | Read bytes per second versus write bytes per second  
Non-read and write requests, like listing a directory, reading file attributes, and deleting files | Metadata requests per second  
  
## What's next

[Optimize performance](https://docs.cloud.google.com/netapp/volumes/docs/performance/optimize-performance).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
