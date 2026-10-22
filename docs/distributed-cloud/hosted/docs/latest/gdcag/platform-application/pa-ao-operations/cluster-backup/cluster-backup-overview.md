---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/cluster-backup-overview/
title: Overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:27.155744+00:00
---

# Overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/cluster-backup-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of cluster backup and restore operations for Google Distributed Cloud (GDC) air-gapped.

Kubernetes cluster backups protect your data by capturing the state of your applications, ensuring both crash and application consistency. Backups are stored in S3-compatible repositories and managed through backup plans, which define their scope and schedule. Restore plans provide pre-configured recovery scenarios for quick and efficient cluster restoration.

Kubernetes cluster backups offer the following:

  * **Crash consistency:** backups capture the state of your data as if the system had suddenly crashed or lost power at the moment the backup was initiated.
  * **Application consistency:** ensures that all in-flight writes and transactions are completed before the backup is taken, leading to a more reliable and recoverable backup.
  * **Customized pre and post hooks:** use specific pre-execution and post-execution hooks and define custom behavior for quiescing, backing up, or restoring a stateful workload.
  * **Multiple strategies:** deploy protected application strategies to customize how backups are taken and what resources get restored.



## Backup repositories

A backup repository represents an S3-compatible storage location for your backups. Backup repositories store records of backups, backup plans, restore plans, and restores. Clusters can have multiple backup repositories with different import rules. These import rules dictate what actions can be performed.

For more information, see [Add a backup repository](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/add-backup-repository).

## Backup plans

Backup plans provide the configuration, location, and management functions for a sequence of backups. A backup plan contains a backup configuration, including the source cluster and the selection of workloads to back up. Google recommends providing every cluster with at least one backup plan. Create one or more backup plans for each cluster. A single cluster or VM can belong to one or more backup plans. If your backup plan defines a schedule for the backup, the backups are automatically created according to that schedule.

For more information, see [Plan a set of backups](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/plan-backups).

## Restore plans

Restore plans are pre-configured restore scenarios for a corresponding line of backups. Create a restore plan using an existing backup plan resource. Customize the behavior of restores by changing the configuration of the restore in the GDC console or API.

For more information, see [Restore a backup](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/restore-backup).

## Backup Service API overview

The Backup Service API provides key functions that are critical for the backup and restore processes. You can add new APIs such as the Backup, GKE Backup Agent, and Backup Control Plane APIs to a Kubernetes cluster. These APIs are used to manage the lifecycle of backups, and to create backup repositories, policies, and plans.

For more information, see [Backup API overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/backup/backup-api-overview).

## What's next

  * [Install backup and restore components](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/install-backup-restore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
