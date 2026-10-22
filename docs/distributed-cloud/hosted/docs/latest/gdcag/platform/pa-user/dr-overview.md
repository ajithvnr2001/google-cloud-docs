---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dr-overview/
title: Overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:29.382724+00:00
---

# Overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dr-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of disaster recovery (DR) operations in Google Distributed Cloud (GDC) air-gapped. It describes the different tasks to consider when performing DR-related activities. Disaster Recovery operations are essential for maintaining business continuity and data protection when deploying projects in a Distributed Cloud environment.

This page is intended for developers in platform administrator or application operator groups that manage disaster recovery operations. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Disaster recovery planning

You must have sufficient capacity to back up workload data, given the size of the data and its retention period. GDC provides backup capabilities for customer workloads to compatible object storage buckets. 

These backups are incremental, with the first backup being a full backup and all subsequent backups being incremental, capturing only the changes made since the last backup. The storage containing the backups must have enough capacity to accommodate the initial full backup and to accommodate the accumulated changes (deltas) between backups for the given backup frequency and retention periods. You must account for potential growth of the data being backed up to ensure the backups don't exceed the storage capacity.

If you are planning on using object storage on a remote GDC instance, you must create the storage buckets within the same organization on the target instance where the workloads are running in the source instance, so billing functions correctly. The organization control plane on one GDC instance must be backed up into buckets hosted in the same organization on another instance. You can also create buckets for backing up workloads in the same organization on the control plane backup instance.

You must also have sufficient capacity such as compute and storage to run any failed workloads on a separate GDC instance that you want to be able to restore to in the case of a disaster. For example, if you have two GDC instances and you want to be able to run all workloads while only one of the instances is available, the capacity of both instances individually must be greater than or equal to the overall capacity needed to run all of the workloads. However, if only some workloads must be recovered during a system failure, your planning can include temporarily shutting down less critical applications to free up resources until the failing systems are functioning again.

## Restore user workloads

User workloads are a collection of services that interact together based on business logic that you define. GDC is not able to provide complete automation out-of-the-box to restore user workloads. However, the `Backup4GDC` service can recover an entire cluster at once, or recover one namespace at a time if more granularity is needed.

To automate the restoration of a workload, an end user can design pods as `init` containers, which are specialized containers that run before app containers in a pod. A pod then validates dependencies before starting its long-running container that results in a self-orchestrated structure.

Add your startup logic directly into your workloads as code to restore an entire cluster at once and have your application self-check and validate prerequisites before it starts. For example, start the web server after confirming that your database and credit card servers are serving traffic.

## Manage version differences

The GDC versions of different clusters can be different. Disaster recovery requires both sites to be running the same GDC version for all corresponding clusters. You must manually control the synchronization process.

The clusters being restored might have different versions when a disaster occurs. Be mindful of version differences when transferring workloads. GDC is backward compatible, but not forward compatible.

A backup with an older version can be restored in a cluster with a newer version. However, a backup with a newer version can't be restored in a cluster with an older version. You must find compatible backups when you transfer workloads.

## Back up and restore

Backup and restore in GDC enables the backup and restoration of Kubernetes cluster workloads, Harbor registry instances, and virtual machine (VM) instances to S3-compatible object storage buckets.

### Cluster backup overview

Kubernetes cluster backups safeguard your data by capturing the state of your applications, providing both crash consistency and application consistency. You can customize the backup process using pre and post execution hooks and multiple protected application strategies.

Backups are stored in S3-compatible repositories and managed through backup plans, which define their scope and schedule. Restore plans offer pre-configured recovery scenarios, allowing for quick and efficient cluster restoration.

For more information, see [Cluster backup overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/cluster-backup-overview).

### VM backup overview

GDC VM backups let you back up virtual machine workloads, including their configurations, disk images, and persistent volumes. Manage backups through backup plans, scheduling them regularly or creating them on-demand. Restore VMs to a previous state or recover individual disk snapshots.

For more information, see [VM backup overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/vm-backup-overview).

### Harbor backup overview

Harbor backups provide comprehensive protection for your Harbor registry instances, safeguarding against data loss and ensuring business continuity. Schedule automatic backups or create them manually.

Define retention policies for long-term data management. In the event of a disaster, restore your Harbor instance, including all artifacts and metadata, from a previously created backup.

For more information, see [Harbor backup overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/harbor-backup-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
