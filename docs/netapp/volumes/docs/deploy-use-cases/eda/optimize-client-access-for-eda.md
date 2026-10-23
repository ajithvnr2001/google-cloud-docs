---
url: https://docs.cloud.google.com/netapp/volumes/docs/deploy-use-cases/eda/optimize-client-access-for-eda/
title: Optimize Linux NFS client access for electronic design automation workloads \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:15.663284+00:00
---

# Optimize Linux NFS client access for electronic design automation workloads  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/deploy-use-cases/eda/optimize-client-access-for-eda/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Optimize Linux NFS client access for electronic design automation workloads Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to optimize Linux NFS client access for electronic design automation (EDA) workloads. This document is intended for storage administrators, cloud architects, and system engineers who are responsible for configuring Linux compute nodes and managing high-performance EDA environments on Google Cloud.

## Client best practices

Linux nodes and interactive VMs mount NetApp Volumes over NFS. Client tuning doesn't increase volume throughput limits, but it helps prevent metadata storms, slot overload on a single storage endpoint, and poor sequential read behavior on large libraries.

Configure clients in the following order:

  1. Kernel concurrency (before mount): [Linux NFS concurrency](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-concurrency)

For Cluster Toolkit and Slurm compute images, include slot-table settings in the compute image or startup scripts before the first mount.

  2. Mount options (at mount): [Linux NFS mount options](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-mount-options)

  3. Read-ahead (after mount, optional): [Linux NFS read-ahead](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-read-ahead)




For more information about NFS client optimization, see [Optimize Linux NFS clients for NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/optimize-linux-nfs-clients).

For mount commands and export policies, see [Connect NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients). To spread clients across large volumes, see [Connect large capacity volumes with multiple storage endpoints](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-large-capacity-volumes) and [EDA architectural patterns](https://docs.cloud.google.com/netapp/volumes/docs/deploy-use-cases/eda/architectural-patterns-eda).

### Optimize EDA farms with many clients

Use the following settings for large-scale deployments with hundreds or thousands of compute nodes that share the same exports. These configurations don't match single-VM benchmark setups, which typically use the `nconnect=16` mount option on a single host.

Area | Recommended starting point  
---|---  
Protocol | NFSv3 (`vers=3`) unless you require NFSv4.1 features  
Concurrency (NFSv3) | Low RPC slot table per client; for example, 8 entries in `/etc/modprobe.d/sunrpc.conf`  
Connections | One TCP connection per client per storage endpoint; don't use `nconnect`  
Large capacity volumes | Mount by DNS or static groups to distribute nodes across [multiple storage endpoints](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-large-capacity-volumes)  
Transfer size | Set `rsize=262144` and `wsize=262144`  
Reliability | Use `hard`, `tcp`, `timeo=600`, or Google Cloud console defaults  
Metadata load | Use `noatime` on libraries and scratch if the application allows  
Locks (NFSv3) | Use `nolock` if you don't use advisory locks and Network Status Monitor (NSM) isn't configured  
Read-ahead | Increase for read-mostly libraries after mounting if sequential reads are slow  
  
Validate your setup by using the `nfsiostat` command and the metrics described in [Monitor performance](https://docs.cloud.google.com/netapp/volumes/docs/performance/monitor-performance) while running a regression test that represents your typical production workload.

**Note:** For single-node performance testing or debugging (for example, comparing to [Performance benchmarks](https://docs.cloud.google.com/netapp/volumes/docs/performance/performance-benchmarks)), you can use higher slot limits and `nconnect=8-16` on a single VM. Don't copy these settings to the entire Slurm fleet.

### Optimize clients by data tier

The following table lists client focus areas and typical mount options by data tier:

Tier | Client focus | Typical mount-related options  
---|---|---  
Libraries | Reduce `GETATTR` and metadata round trips; sequential read of large files | `vers=3`, `hard`, `tcp`, `noatime`, `rsize`, and `wsize`; consider `actimeo=600` and `nocto` only if data is read-mostly and coherency rules allow  
Scratch | Many writers; coherency matters | `vers=3`, `hard`, `tcp`, and `noatime`; don't use aggressive attribute caching; keep slot count low per node  
Tools | Read-mostly, similar to the libraries | `vers=3`, `hard`, `tcp`, `noatime`, `rsize=262144`, and `wsize=262144`; consider `actimeo=600` and `nocto` only if data is read-mostly and coherency rules allow; maintain stable mount options across the cluster image  
Home | Mixed small I/O | Google Cloud console defaults usually suffice; use low slots if home shares an endpoint with scratch  
  
Use Kerberos (`sec=krb5`, `krb5i`, or `krb5p`) only when required by policy. Don't combine Kerberos with `nconnect`. For more information, see [Linux NFS mount options](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/linux-nfs-mount-options).

## What's next

  * For benchmark results, see [Electronic design automation workload benchmarks](https://docs.cloud.google.com/netapp/volumes/docs/performance/performance-benchmarks#electronic_design_automation_workload_benchmarks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
