---
url: https://docs.cloud.google.com/managed-lustre/docs/release-notes/
title: Google Cloud Managed Lustre release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:00.889366+00:00
---

# Google Cloud Managed Lustre release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)
  * [ Resources ](https://docs.cloud.google.com/managed-lustre/docs/resources)



Send feedback 

#  Google Cloud Managed Lustre release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Google Cloud Managed Lustre. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

## July 13, 2026

Change

Google Cloud Managed Lustre quota management has been simplified. Per-performance-tier storage capacity quotas have been replaced by two new quotas that are shared across all performance tiers: **Throughput** (measured in GBps) and **Capacity** (measured in GiB). These quotas are applied per-zone and per-VPC network. You can request increases for throughput and capacity independently, and use your quota to create instances in any performance tier.

For more information, see [Quotas and limits](https://docs.cloud.google.com/managed-lustre/docs/quotas).

## June 04, 2026

Feature

Google Cloud Managed Lustre now supports advanced notification of maintenance events, and the ability to control when maintenance events occur on your instances.

For more information, see [Maintenance events and policies](https://docs.cloud.google.com/managed-lustre/docs/maintenance).

## May 21, 2026

Change

The storage capacity step size threshold has been increased.

For more details on step sizes, see [Performance tiers](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers).

To calculate valid values for instance capacity, use the [capacity calculator](https://docs.cloud.google.com/managed-lustre/docs/create-instance#capacity_calculator).

## April 23, 2026

Feature

Managed Lustre now supports the Dynamic tier. This tier provides capacity scaling and high-performance caching for data-intensive, cacheable workloads.

Key features of the Dynamic tier include:

  * **Scalable capacity** : Support for storage capacities up to 84,016,000 GiB (80.1 PiB).
  * **Integrated cache** : Fast I/O and metadata performance using a high-performance caching layer.
  * **Cache monitoring** : New metrics are available to monitor cache performance and utilization.



For more information, see [Performance tiers](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers).

## April 22, 2026

Feature

The maximum throughput and the maximum storage capacities for Google Cloud Managed Lustre instances have been increased:

  * Maximum throughput has been increased to 10 TBps.
  * The maximum storage capacity is now 40,032,000 GiB (38.2 PiB), for instances in the 250 MBps per TiB performance tier. The 500 and 1000 MBps per TiB tiers have increased proportionally. The 125 tier remains unchanged.



See [Performance tiers](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers) for more details.

## April 06, 2026

Change

The required CIDR range for creating a Managed Lustre instance has been updated from /24 to /23.

We recommend using a /20 range (4096 addresses) for VPC peering to allow for multiple instances and other services.

For more details, see [Create and configure the VPC](https://docs.cloud.google.com/managed-lustre/docs/vpc#create-and-configure-the-vpc).

## March 16, 2026

Feature

Managed Lustre now supports file system quota monitoring via Cloud Monitoring. You can track storage consumption and inode usage for individual users, groups, or projects through metrics in the Cloud Monitoring console.

For more information, see [Monitor file system quotas](https://docs.cloud.google.com/managed-lustre/docs/file-system-quotas#monitor-quotas-in-cloud-monitoring).

## March 04, 2026

Feature

Google Cloud Managed Lustre now supports Lustre Jobstats metrics. These metrics provide read, write, and metadata statistics per JobID, as configured on the client, helping monitor performance at the job level.

For more details, see [Monitor instances and operations](https://docs.cloud.google.com/managed-lustre/docs/monitoring#jobstats-metrics).

## February 13, 2026

Feature

The maximum throughput and the maximum storage capacities for Managed Lustre instances have been increased:

  * Maximum throughput has been increased to 1.5 TBps.
  * The largest storage capacity is now 12,240,000 GiB, for instances in the 125 MBps per TiB performance tier. Other tiers have increased proportionally.



See [Performance tiers and maximum storage capacities](https://docs.cloud.google.com/managed-lustre/docs/create-instance#performance-tiers) for more details.

## February 11, 2026

Feature

Managed Lustre now supports [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) in [Preview](https://cloud.google.com/products#product-launch-stages).

For more details, see [Secure instances with a service perimeter](https://docs.cloud.google.com/managed-lustre/docs/vpc-sc).

## January 29, 2026

Feature

Managed Lustre now supports customer-managed encryption keys (CMEK) to protect your Managed Lustre file systems.

For more details, see [Customer-managed encryption keys for Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/cmek).

## October 27, 2025

Feature

Managed Lustre now supports IP-based access control through the root-squash feature. Root squash prevents a root user on a client VM from having root privileges on a Managed Lustre file system.

For more details, see [IP-based access control](https://docs.cloud.google.com/managed-lustre/docs/ip-based-access-control).

Feature

Added Red Hat Enterprise Linux 9 as a supported image type when [connecting from a Compute Engine VM](https://docs.cloud.google.com/managed-lustre/docs/connect-from-compute-engine).

## October 13, 2025

Fixed

Google Cloud Managed Lustre now fully supports data transfers to and from Cloud Storage buckets that have Object Lifecycle Management (OLM) or Autoclass enabled.

## September 23, 2025

Feature

Google Cloud Managed Lustre now supports file system quotas, allowing you to set limits on the amount of disk space and the number of files that users, groups, or projects can consume within your file system.

For details, see [File system quotas](https://docs.cloud.google.com/managed-lustre/docs/file-system-quotas) in the Managed Lustre documentation.

## August 28, 2025

Feature

You can now increase the storage capacity of your Managed Lustre instances after they've been created.

See [Increase the capacity of a Managed Lustre instance](https://docs.cloud.google.com/managed-lustre/docs/increase-capacity).

## June 30, 2025

Announcement

Google Cloud Managed Lustre is now Generally Available (GA) to all customers with the following new features:

  * New performance tiers with maximum throughput speeds from 125 MBps per TiB to 1000 MBps per TiB.
  * Increased storage capacity, up to 7,632,000 GiB (~8 PiB).



Learn more about [performance tiers and maximum capacities](https://docs.cloud.google.com/managed-lustre/docs/create-instance#performance-tiers).

## April 08, 2025

Change

[Google Cloud Managed Lustre](https://docs.cloud.google.com/managed-lustre) is now Generally Available (GA) with access by invitation.

Managed Lustre provides a fully managed parallel file system optimized for AI and HPC applications, with storage capacity up to 1 PB.

To request access to Managed Lustre in your Google Cloud project, contact your sales representative.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
