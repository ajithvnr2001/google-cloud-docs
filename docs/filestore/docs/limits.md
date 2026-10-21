---
url: https://docs.cloud.google.com/filestore/docs/limits/
title: Quotas and limits \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:27:08.400470+00:00
---

# Quotas and limits  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Resources ](https://docs.cloud.google.com/filestore/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the quotas and limits of Filestore.

## Number of instances

The number of instances you can create is limited only by the amount of Filestore quota for a given project and region as well as the minimum file share capacity. For example, if you have 32 TiB of quota in a given region, you can create 32 instances each with 1 TiB of capacity. To see your available per project, per region quota, go to [the Quotas page](https://console.cloud.google.com/iam-admin/quotas).

## Number of snapshots

Service tier | Maximum recommended number of [snapshots](https://docs.cloud.google.com/filestore/docs/snapshots) per instance  
---|---  
Basic HDD | Not supported  
Basic SSD | Not supported  
Zonal | 240  
Regional | 240  
Enterprise | 240  
  
## Number of clients

Maximum number of client connections for instances Service tier | Instances with [custom performance](https://docs.cloud.google.com/filestore/docs/custom-performance) off | Instances with custom performance on  
---|---|---  
Basic HDD | 500 connections per instance | Custom performance not supported  
Basic SSD | 500 connections per instance | Custom performance not supported  
Zonal (1 TiB to 9.75 TiB) | 2,000 connections per 1 TiB   
Scales in increments of 500 for up to 19,500 connections per instance | 100 connections per 1,000 purchased IOPS  
Zonal (10 TiB to 100 TiB)  
(previously high scale SSD) | 8,000 connections per 10 TiB  
Scales in increments of 2,000 for up to 80,000 connections per instance | 100 connections per 1,000 purchased IOPS  
Regional (100 GiB to 10,239 GiB) | 2,000 connections per 1 TiB  
Scales in increments of 500 for up to 19,500 connections per instance | 100 connections per 1,000 purchased IOPS  
Regional (10 TiB to 100 TiB) | 8,000 connections per 10 TiB  
Scales in increments of 2,000 for up to 80,000 connections per instance | 100 connections per 1,000 purchased IOPS  
Enterprise | 2,000 connections per 1 TiB  
Scales in increments of 500 for up to 20,000 connections per instance | Custom performance not supported  
  
## Number of VPC networks used with Filestore

You can create Filestore instances on no more than 49 unique VPC networks, even if previously used networks are deleted. If you think that you've reached this limit, see the troubleshooting guide topic on [`error code 13`](https://docs.cloud.google.com/filestore/docs/create-instance-issues) for possible solutions.

## File share capacity

Service tier | Capacity  
---|---  
Basic HDD | 1 TiB to 63.9 TiB  
Basic SSD | 2.5 TiB to 63.9 TiB  
Zonal with a lower capacity range | 1 TiB to 9.75 TiB  
Zonal with a higher capacity range | 10 TiB to 100 TiB  
Regional with a lower capacity range | 100 GiB to 10,239 GiB  
Regional with a higher capacity range | 10 TiB to 100 TiB  
Enterprise | 1 TiB to 10 TiB  
  
Enterprise instances combined with the Filestore multishares feature can support a minimum share capacity of 10 GiB.

For more information, see [Filestore multishares](https://docs.cloud.google.com/filestore/docs/multishares#storageclasses_and_dynamic_volume_provisioning).

## File size

Service tier | Maximum supported file size  
---|---  
Basic HDD | Up to 16 TiB  
Basic SSD | Up to 16 TiB  
Zonal | Up to the size of instance capacity  
Regional | Up to the size of instance capacity  
Enterprise | Up to the size of instance capacity  
  
## Number of files

Service tier | Maximum file limit  
---|---  
Basic HDD | 67,108,864 files per 1 TiB of capacity  
Basic SSD | 67,108,864 files per 1 TiB of capacity  
Zonal | Approximately 89,000,000 files per 1 TiB of capacity  
Regional | Approximately 89,000,000 files per 1 TiB of capacity  
Enterprise | Approximately 89,000,000 files per 1 TiB of capacity  
  
  * The number of files listed is an indication of the maximum number of supported connections to small or empty files. The number of supported file connections decreases as file size increases.

  * While no practical limit exists across service tiers, instance performance may be delayed when supporting a large number of files.




To check your usage, run the following command:
    
    
      df -i
    

`IUsed` reflects the current number of files you have and `IFree` reflects the number of additional files that you can store.

## File locks

A [file-locking](https://en.wikipedia.org/wiki/File_locking) client is a client with at least one acquired or requested file lock. Anything greater than the maximum recommended limit listed introduces inconsistent locking behaviors that may result in production outages when the instance undergoes maintenance:

Service tier | Maximum recommended number of file-locking clients per instance  
---|---  
Basic HDD | 128  
Basic SSD | 128  
Zonal | 250  
Regional | 250  
Enterprise | 250  
  
## Rate limits for backups

The following [backups](https://docs.cloud.google.com/filestore/docs/backups) operations have a rate limit of once per 10 minutes in the steady state:

  * Creating a backup of Filestore instance
  * Restoring a Filestore instance from a backup (in-place restore)
  * Creating a new Filestore instance from a backup



If you want to issue a burst of requests to back up your file shares, you can issue at most 6 requests in 60 minutes.

For more information, see [Backups feature limitations](https://docs.cloud.google.com/filestore/docs/backups#feature_limitations).

## Filestore agent volumes limits

Filestore agent volumes introduces high-density elastic NFS file storage backed by regional volume pools:

Resource or metric | Limit  
---|---  
Maximum volume pool capacity | Up to 100 TB per volume pool  
Maximum volumes per volume pool | Up to 1,000,000 volumes  
Minimum volume size | 100 MiB  
Volume attachment latency | Under 100 ms  
Volume creation and deletion latency | Under 1 second  
Mount protocol | NFSv3  
Supported access modes | ReadWriteMany (RWX), ReadOnlyMany (ROX)  
  
For more information, see [About Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/agent-volumes-overview).

## What's next

  * [About Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/agent-volumes-overview)
  * [Service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers)
  * [Known issues](https://docs.cloud.google.com/filestore/docs/known-issues)
  * [Troubleshoot performance-related issues](https://docs.cloud.google.com/filestore/docs/troubleshooting)
  * [Scale capacity](https://docs.cloud.google.com/filestore/docs/scale)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
