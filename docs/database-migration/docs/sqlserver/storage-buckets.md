---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/storage-buckets/
title: Store backup files in a Cloud Storage bucket \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:20:45.589933+00:00
---

# Store backup files in a Cloud Storage bucket  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/storage-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Store backup files in a Cloud Storage bucket Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service replicates data from SQL Server backup and transaction log files that you upload to a Cloud Storage bucket. This page describes how to prepare your bucket for migration procedures, and what folder structure is required for Database Migration Service to recognize your backup files for migrating from self-managed or Amazon RDS sources.

To prepare a storage bucket for migration, perform the following steps:

  1. [Create your bucket](https://docs.cloud.google.com/storage/docs/creating-buckets). Make sure you use the same region as the one where you intend to create your destination Cloud SQL for SQL Server instance.

Database Migration Service is a fully-regional product, meaning that all entities related to your migration (source and destination connection profiles, migration jobs, destination databases, storage buckets for backup files) must be saved in a single region.

  2. [ Create the folder structure](https://docs.cloud.google.com/storage/docs/objects#simulated-folders) to hold your backup files.

     * Database Migration Service expects a folder structure where every folder present at the bucket's root level represents one database to migrate.

     * The database folder at minimum must contain two folders: `full` for the full backup file, and `log` for transaction log backup files that you later upload for the incremental load phase.

     * The database folder can also optionally contain a `diff` folder for the differential backup file.

     * If you use striped full or differential backup files, their respective `full` or `diff` folders must contain an additional folder whose name is a Unix timestamp in seconds.

For example, if you use a single full backup file, put it directly in the `full` folder. The same rule applies to the differential backup file:
    
    Cloud Storage bucket root/
    |- my-business-database/
    |  |- full/
    |  |  |- full_backup_file
    |  |- diff/
    |  |  |- diff_backup_file
    |  |- log/
    |  |  |- transaction_log_file
    |- my-other-database/
    |  |- full/
    |  |  |- full_backup_file
    |  |- diff/
    |  |  |- diff_backup_file
    |  |- log/
    |  |  |- transaction_log_file
    

If you use striped full backup files, then use an additional folder in the `full` folder. The same rule applies to the differential backup file:
    
    Cloud Storage bucket root/
    |- my-business-database/
    |  |- full/
    |  |  |- 1712649600/
    |  |  |  |- my_full_backup_file_stripe1
    |  |  |  |- my_full_backup_file_stripe2
    |  |- diff/
    |  |  |- 1706967833/
    |  |  |  |- firstDiffStripe.bak
    |  |  |  |- other_diff_stripe.diff
    |  |- log/
    |  |  |- transaction_log_file
    |- my-other-database/
    |  |- full/
    |  |  |- 1715250742/
    |  |  |  |- my_full_backup_file_stripe1
    |  |  |  |- my_full_backup_file_stripe2
    |  |- diff/
    |  |  |- 1706967833/
    |  |  |  |- firstDiffStripe.bak
    |  |  |  |- other_diff_stripe.diff
    |  |- log/
    |  |  |- transaction_log_file
    

In these examples, Database Migration Service creates two databases in your destination Cloud SQL instance: `my-business-database` and `my-other-database`. Each database is populated with data pulled from their individual `full`, `diff`, and `log` folders.

You can mix the single file or striped file conventions for full and differential backup files. Differential backup files are optional, so you can also leave the `diff` folder empty:
    
    Cloud Storage bucket root/
    |- my-business-database/
    |  |- full/
    |  |  |- full_backup_file
    |  |- diff/
    |  |  |- 1706967833/
    |  |  |  |- firstDiffStripe.bak
    |  |  |  |- other_diff_stripe.diff
    |  |- log/
    |  |  |- transaction_log_file
    |- my-other-database/
    |  |- full/
    |  |  |- 1712649600/
    |  |  |  |- my_full_backup_file_stripe1
    |  |  |  |- my_full_backup_file_stripe2
    |  |- diff/
    |  |  |- diff_backup_file
    |  |- log/
    |  |  |- transaction_log_file
    |- third-database/
    |  |- full/
    |  |  |- full_backup_file
    |  |- log/
    |  |  |- transaction_log_file
    

In this example, the `third-database` doesn't use a differential backup file for migration, so it doesn't have the `diff` folder.

  3. [Upload your backup files](https://docs.cloud.google.com/storage/docs/uploading-objects) to their respective folders:

     * Put the full backup file in the `full` folder.
     * Put the differential backup file in the `diff` folder.
     * Put the transaction log files in the `log` folder.
**Note:** You can upload the differential backup file at a later time - after you create the migration job, but before you start uploading transaction log files.

Make sure your full backup, differential, and transaction log files follow the naming conventions required by Database Migration Service. See [ Backup files naming requirements](https://docs.cloud.google.com/database-migration/docs/sqlserver/export-backup-files).




## What's next?

  * [Schedule regular transaction log transfers](https://docs.cloud.google.com/database-migration/docs/sqlserver/automate-backup-exports).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
