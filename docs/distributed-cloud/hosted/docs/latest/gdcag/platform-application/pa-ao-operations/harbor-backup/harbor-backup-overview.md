---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/harbor-backup-overview/
title: Overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:11:41.861634+00:00
---

# Overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/harbor-backup-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of Harbor backup and restore operations.

Harbor backup and restore lets you create backups of your Harbor instance and restore that instance in the case of a disaster. Harbor instance backups offer the following benefits:

  * **Protect against data loss:** Create scheduled or manual backups to capture your data at a specific point in time.
  * **Long-term retention and archiving:** Use retention policies for long-term data retention and archiving, enabling you to meet regulatory compliance requirements and preserve historical data.
  * **Data consistency:** The backup operation handles the necessary Harbor quiesce and unquiesce steps to ensure data consistency.



## Features overview

Harbor backup and restore has the following features:

  * Set Harbor instances to back up automatically at a scheduled time.
  * Create manual backups on your Harbor instances on-demand to capture your Harbor instances in the exact chosen state.
  * Deploy retention policies to dictate when old backups get deleted and which backups are retained.
  * Restore the Harbor instance from a previously created backup.



To maintain data consistency, you can't perform write operations to Harbor while a backup is in progress. This restriction includes editing Harbor configurations, creating new Harbor instance projects, and pushing artifacts. For more information, see the Harbor documentation: <https://goharbor.io/docs/main/administration/backup-restore/#backup-harbor-instance>.

## Architecture overview

Harbor backup and restore leverages existing GDC backup and restore architecture. The system is a distributed backup solution designed for Kubernetes environments consisting of the following components:

  * Custom resources define and manage backups.
  * Backups target both database and artifact registry data sources in object storage.
  * System design addresses high availability and disaster recovery considerations.



The Harbor backup and restore system consists of the following components:

  1. A `HarborInstanceBackup` custom resource is the entry point to interact with the system. This custom resource points to a set of controllers used to reconcile Harbor backup objects. The system uses the `HarborInstanceBackup` resource to create both manual backups that you create, and automatic backups that are created according to backup plan schedule.
  2. The system uses this set of controllers to reconcile the Harbor backup objects: 
     1. The `HarborInstanceBackupRepository` controller monitors the `HarborInstanceBackupRepository` custom resource. The resource represents a backup storage target to reference in `HarborInstanceBackupPlan` and `HarborInstanceBackup`.
     2. The `HarborInstanceBackupPlan` controller monitors the `HarborInstanceBackupPlan` custom resource, which creates `HarborInstanceBackup` custom resources to the given Harbor instance according to the provided schedule and retention configuration.
     3. The `HarborInstanceBackup` controller monitors the `HarborInstanceBackup` custom resource to manage the two different backup flows for the persistent data sources of a single Harbor instance. These data sources are metadata in the Harbor database and artifact data in registry object storage.
  3. The system stores backups in S3-compatible objects storage buckets.



The restore architecture mirrors the design of the backup system.

## Create a backup repository

Harbor backup repository represents an S3-compatible storage location for your backups. Harbor instances, which manage container images essential for software deployment, require secure and reliable backup mechanisms. For more information, see [Create a backup repository](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-backup-repository-harbor).

## Create backup plans

Harbor backup plans provide the configuration, location, and management functions for Harbor instance backups. Use backup plans to create scheduled automatic backups. For more information, see [Create a backup plan](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-backup-plan-harbor).

## Create manual backups

Harbor backups contain your Harbor instance data. With backup plans, backups are created on a schedule that you define. You can also create manual backup on demand. For more information, see [Create a manual backup](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-manual-backup-harbor).

## Restore a backup

Restore a backup of a Harbor instance in GDC. Recover your Harbor instance to a previous state using an existing backup. The restore operation uses the data from the specified backup to recreate the Harbor instance. For more information, see [Create a restore](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-restore-harbor).

## What's next

  * [Create a backup repository](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-backup-repository-harbor)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
