---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/clones-vmware-sql-server/
title: About clones of VMware VMs or Microsoft SQL Server databases \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:08.977449+00:00
---

# About clones of VMware VMs or Microsoft SQL Server databases  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/clones-vmware-sql-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  About clones of VMware VMs or Microsoft SQL Server databases Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

A clone is a full copy of a managed application. Unlike LiveClones, clones cannot be refreshed and they don't permit prep-mounting. A clone consumes as much storage as the original application data. This is different from a mount operation which uses a virtual copy that does not require additional storage.

Use the clone function to create an independent copy of a dataset. The most common uses are the following:

  * Application development and testing
  * Data audit for compliance
  * Data warehousing
  * E-discovery
  * User acceptance testing



A clone of a VMware VM backup creates an entirely new VMware VM that has no dependency on the backup/recovery appliance. It is very similar to a restore operation in that it needs to copy all the data before the VM is available. See [Clone a backup of a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-image-of-a-vm).

A clone of a Microsoft SQL server database creates an entirely new database that has no dependency on the backup/recovery appliance. It is very similar to a restore operation in that it needs to copy all the data before the database is available. See [Clone Microsoft SQL Server Databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/sql-cloning).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
