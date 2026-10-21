---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/backup-restore-overview/
title: Back up and restore overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:43:56.251354+00:00
---

# Back up and restore overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/backup-restore-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Back up and restore overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview about backup and restore capabilities in Google Distributed Cloud (GDC) air-gapped.

GDC enables the backup and restoration of Kubernetes cluster workloads, Harbor registry instances, and virtual machine (VM) instances to S3-compatible objects storage buckets.

Backups of your workloads are useful for disaster recovery, CI/CD pipelines, replicating workloads, and upgrade scenarios. Protect your workloads to help you achieve business-critical recovery point objectives.

## Supported data types

GDC backup and restore supports the following data types:

  * Kubernetes cluster workload configuration information such as Deployments, StatefulSets, Secrets, ConfigMaps, and custom resources.
  * Virtual machine (VM) instances and local snapshots of VM disks.
  * Harbor registry instances.



## Supported backup policies

GDC backup and restore supports the following policies to manage your data:

  * Set backups to occur on a regular schedule.
  * Deploy automated backups.
  * Perform manual backup and restore requests.
  * Use data retention policies to keep or remove data for specific periods of time.
  * Control the backup data location. Store backup data in S3-compatible buckets on local, remote, or disconnected GDC instances.



## Cluster backup

Kubernetes cluster backups safeguard your data by capturing the state of your applications, providing both crash consistency and application consistency. You can customize the backup process using pre and post execution hooks and multiple protected application strategies.

Backups are stored in S3-compatible repositories and managed through backup plans, which define their scope and schedule. Restore plans offer pre-configured recovery scenarios, allowing for quick and efficient cluster restoration.

For more information, see [Cluster backup overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/cluster-backup-overview).

## VM backup

GDC VM backups let you back up virtual machine workloads, including their configurations, disk images, and persistent volumes. Manage backups through backup plans, scheduling them regularly or creating them on-demand. Restore VMs to a previous state or recover individual disk snapshots. To begin protecting your VMs, create a backup repository and define your preferred backup plan.

For more information, see [VM backup overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/vm-backup-overview).

## Harbor instance backup

Harbor backups provide comprehensive protection for your Harbor registry instances, safeguarding against data loss and ensuring business continuity. Schedule automatic backups or create them manually.

Define retention policies for long-term data management. In the event of a disaster, restore your Harbor instance, including all artifacts and metadata, from a previously created backup.

For more information, see [Harbor backup overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/harbor-backup-overview).

## What's next

  * [Cluster backup overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/cluster-backup-overview)
  * [VM backup overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/vm-backup-overview)
  * [Harbor backup overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/harbor-backup-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
