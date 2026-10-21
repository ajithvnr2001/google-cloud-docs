---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/migration/vms/disk-migrations/
title: gcloud alpha migration vms disk-migrations \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:57:24.820236+00:00
---

# gcloud alpha migration vms disk-migrations  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/migration/vms/disk-migrations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha migration vms disk-migrations Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha migration vms disk-migrations - migrates disks to Compute Engine 
SYNOPSIS
    

`gcloud alpha migration vms disk-migrations` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The gcloud alpha migration vms disk-migrations command lets you create and manage disk migration resource. You must create a disk migration resource before you can migrate your disk from any migration source to a Compute Engine disk. The disk migration resource tracks the progress of the disk migration. To use this command, you must enable VM Migration API in your project. 

Note that this command only creates a disk migration resource. It does not initiate the disk migration process. After creating the disk migration resource, you must initiate the migration process using the run command. The disk is migrated to a Google Cloud Project, designated by the Target Project resource. To get a list of Target Projects, run the gcloud alpha migration vms target-projects list command. For information on adding target projects, see <https://cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/target-project>. 

A project can support a maximum of 200 Disk/VM Migration active resources per project; 1000 ready disk migration resources, and 500 finished disk migration resources. Hence we recommend that you delete a completed disk migrations to avoid reaching the disk migration resources limit. Deletion of disk migration resource does not affect the migrated disk. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[cancel](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/migration/vms/disk-migrations/cancel)`
     `(ALPHA)` Cancel a disk migration resource process. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/migration/vms/disk-migrations/create)`
     `(ALPHA)` Create a disk migration resource to migrate a disk to Compute Engine. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/migration/vms/disk-migrations/delete)`
     `(ALPHA)` Delete a disk migration resource. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/migration/vms/disk-migrations/describe)`
     `(ALPHA)` Describe a disk migration resource. 
`[fetch-inventory](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/migration/vms/disk-migrations/fetch-inventory)`
     `(ALPHA)` Lists source environment volume inventory. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/migration/vms/disk-migrations/list)`
     `(ALPHA)` List disk migration resources. 
`[run](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/migration/vms/disk-migrations/run)`
     `(ALPHA)` Run a disk migration resource process. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/migration/vms/disk-migrations/update)`
     `(ALPHA)` Update a disk migration resource target details. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
