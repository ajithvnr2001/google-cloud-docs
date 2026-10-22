---
url: https://docs.cloud.google.com/filestore/docs/filestore-maintenance/
title: Maintain Filestore instances \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:33.691490+00:00
---

# Maintain Filestore instances  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/filestore-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Maintain Filestore instances Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of maintenance for Filestore instances. It covers maintenance categories, tier impact, network persistence, and best practices.

## Overview

Filestore routinely updates instances to ensure that the file share service is reliable, secure, and up-to-date. Maintenance updates typically occur every one to two weeks.

Filestore maintenance is fully managed by Google. You can't configure custom maintenance windows, or manually defer or reschedule maintenance.

Maintenance updates fall into the following categories:

  * **Filestore software updates:** System optimizations, performance improvements, and new features.
  * **Operating system patches:** Continuous monitoring and patching of underlying virtual machine (VM) operating systems to protect against security vulnerabilities.
  * **Infrastructure upgrades:** Underlying virtual machine migrations, hardware maintenance, and network updates.



## Maintenance impact by service tier

The impact of a maintenance update depends on your instance's [service tier](https://docs.cloud.google.com/filestore/docs/service-tiers). 

Because Basic tier instances experience brief downtime during maintenance, we recommend using Basic tier primarily for development, testing, and non-critical workloads. For production workloads that require high availability and uninterrupted file access, use Regional, Enterprise, or Zonal tiers.

### Zonal, Regional, and Enterprise tiers

Zonal, Regional, and Enterprise service tiers use non-disruptive upgrades (NDU).

During maintenance, instances in these tiers remain fully available and continue serving file requests with near-zero downtime. Maintenance updates are applied in the background, making the upgrade process transparent to connected Network File System (NFS) clients.

### Basic tiers

Basic tier instances are backed by single-node storage without automated failover. When underlying host migrations, system patches, or software updates occur, file operations pause temporarily until the update completes.

During a maintenance event, Basic HDD and Basic SSD tier instances undergo a brief period of unavailability that typically lasts between 2 and 5 minutes.

During this maintenance window:

  * File operations, such as reads, writes, and directory listings, temporarily pause or freeze.
  * Connected clients that use default retry mechanisms wait for the instance to resume responding.



## Network and instance persistence

The internal IP address assigned to your Filestore instance remains persistent throughout maintenance and doesn't change. Connected NFS clients don't need to update mount configurations or remount file shares after an update.

## Service level agreement (SLA)

In accordance with the [Filestore Service Level Agreement (SLA)](https://cloud.google.com/filestore/sla), downtime resulting from scheduled maintenance is excluded from downtime calculations.

## Best practices for handling maintenance

Because you can't schedule or delay Filestore maintenance, configure your NFS clients and infrastructure to handle transient unavailability gracefully:

  * **Use hard mounts** : When mounting a Filestore file share on a client, specify the `hard` mount option rather than `soft`. With a hard mount, if the file server becomes temporarily unavailable, the NFS client retries requests indefinitely until the server responds. This preserves data integrity and prevents application I/O errors.
  * **Configure NFS client timeouts and retries** : Configure [timeout and retransmission mount options](https://docs.cloud.google.com/filestore/docs/mounting-fileshares) on your NFS clients so that transient delays during maintenance don't cause client timeouts.
  * **Implement application retries** : Build retry logic with exponential backoff into your client applications to handle temporary storage delays smoothly.
  * **Monitor instance health and maintenance** : Monitor instance performance and status in the Google Cloud console or by using [Cloud Monitoring](https://docs.cloud.google.com/filestore/docs/monitoring-instances). On Basic tier instances, you might observe a brief latency spike or temporary pause in file operations during the update window.



## What's next

  * Learn more about [Filestore service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers).
  * Learn how to mount file shares on [Compute Engine VMs](https://docs.cloud.google.com/filestore/docs/mounting-fileshares).
  * Learn how to mount file shares on [Google Kubernetes Engine clusters](https://docs.cloud.google.com/filestore/docs/filestore-for-gke).
  * Learn how to monitor [Filestore instances](https://docs.cloud.google.com/filestore/docs/monitoring-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
