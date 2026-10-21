---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/application-aware-mounts/
title: Mount application-aware backups from the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:44:51.670838+00:00
---

# Mount application-aware backups from the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/application-aware-mounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mount application-aware backups from the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Application aware mounts allow you to rapidly mount a database backup as a virtual application. This approach lets you quickly bring a database online without having to move the data and without having to manually configure a new instance of the database. An application aware mount addresses the challenges of creating and managing copies of production databases without manual intervention by database, server, and storage administrators. Application aware mounts are initiated exactly like standard mounts.

Application aware mounts are particularly useful in test and development environments where multiple copies of a database must be quickly brought online.

Consistency groups that contain databases can be mounted together in an application aware mount. An individual database in a consistency group can be mounted as a virtual application as part of an application aware mount provided all databases in the group are the same application type. If a mount of a database instance or consistency group mounts multiple databases, then the mount creates a new consistency group.

Virtual applications can be protected like any other application. If a virtual application is mounted to a host that has been added to a backup/recovery appliance, then the virtual application appears in the list of available applications in the **App Manager**.

The backup, application mount, sequence can be repeated as needed. Any one of the virtual application generations can be modified or deleted without affecting its parent or descendants. Each generation is independent and can be accessed and its data can change as it is used.

**Note:** The database descendant level limit—children and grandchildren—that defines the supported number of generations is restricted to five.

The details for creating an application aware mount varies by the database selected, see instructions in following procedures:

  * [Mount a virtual Microsoft SQL Server database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/sql-access#VirData)
  * [Mount a virtual Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount-virtualdb)
  * [Mount a virtual SAP HANA database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/sap-hana-mounts)
  * [Mount other databases as application-aware virtual databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/otherdb-mounts#block-based)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
