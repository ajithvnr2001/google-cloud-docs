---
url: https://docs.cloud.google.com/compute/docs/instances/backup-plans-for-instances/
title: About Backup and DR Service backup plans \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:00:27.693218+00:00
---

# About Backup and DR Service backup plans  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/backup-plans-for-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About Backup and DR Service backup plans Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of Backup and DR Service backup plans and how you can use them to back up Compute Engine instances.

Use Backup and DR Service backup plans to create rule-based and indelible backups of your Compute Engine instances and then store those backups in secure and isolated storage locations.

To back up your compute instances for system maintenance or compute instance cloning, use [machine images](https://docs.cloud.google.com/compute/docs/machine-images) instead. Learn more about choosing the correct [data protection option](https://docs.cloud.google.com/compute/docs/disks/data-protection#options) for your use case.

## Limitations

  * You can use only those backup plans that are in the same region as the compute instance.
  * Backup and DR Service doesn't support backing up compute instances to a backup vault if the compute instance uses any of the following configurations:

    * Compute instances with Extreme Persistent Disk volumes attached.
    * Compute instances with any Hyperdisk Extreme volumes attached.
    * Compute instances that use a C3D, H3, A3, A4, or Z3 machine type.
    * Compute instances with customer-supplied encryption keys (CSEKs)([Deprecated](https://docs.cloud.google.com/compute/docs/deprecations)).
    * Compute instances without any attached disks.
    * Compute instances larger than 200 tebibytes (TiB).



## How backup plans work

Backup and DR backup plans provide enhanced protection against cyberattacks by storing immutable and indelible backups of your compute instances. You also get a built-in backup solution with access to seamless backup management across projects.

Backup and DR backup plans let you define advanced backup strategies to store your Compute Engine instances in secure storage locations called backup vaults. You can configure backup rules such as the following:

  * How often to back up your compute instance resources
  * How long to retain the backups
  * Where and how to replicate the backed up data



You first define your backup rules in the backup plan configuration. By doing so, you can configure how frequently you want to schedule backups for your compute instance. You then apply that plan to your compute instances. Backup and DR then automatically backs up your compute instance resources and retains those backups based on these rules.

After you apply a backup plan to a compute instance, you can also use the backup plan to create on-demand backups of that compute instance.

To learn more about backup plans and backup vaults, see [Backup and DR overview](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr) in the Backup and DR Service documentation.

To learn how to use your compute instance's backup plan to schedule or create a backup in a backup vault, see [Back up Compute Engine instances to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup).

## Methods for applying backup plans to compute instances

You can apply backup plans to both new and existing compute instances, as follows:

  * For new compute instances, you can [apply a backup plan while creating the compute instance](https://docs.cloud.google.com/compute/docs/instances/create-instance-with-gcbdr-backup-plan).
  * For existing compute instances, you can edit the compute instance configuration to [apply or change the backup plan](https://docs.cloud.google.com/compute/docs/instances/change-backup-plan-for-instance).



## What's next

  * Learn how to [apply a backup plan while creating a compute instance](https://docs.cloud.google.com/compute/docs/instances/create-instance-with-gcbdr-backup-plan).
  * Learn how to [apply or change the backup plan for an existing instance](https://docs.cloud.google.com/compute/docs/instances/change-backup-plan-for-instance).
  * Learn about the other [compute instance protection options provided by Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-compute-engine).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
