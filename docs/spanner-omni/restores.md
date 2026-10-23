---
url: https://docs.cloud.google.com/spanner-omni/restores/
title: Restore a Spanner Omni backup \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:11.760968+00:00
---

# Restore a Spanner Omni backup  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/restores/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Restore a Spanner Omni backup Stay organized with collections  Save and categorize content based on your preferences. 

You can restore a backup of a Spanner Omni database into a new database. The restored database has all the data and schema information from the original database at the `versionTime` of the backup, including all database options you set with the `ALTER DATABASE SET OPTIONS` command.

The following items aren't included in a restored database:

  * IAM permissions. You must apply appropriate IAM permissions after the restore completes.

  * Internal data of any change streams.

  * Time to live (TTL) defined by a row deletion policy. You must reconfigure these policies after the restore completes.

  * Split points you create when pre-splitting a database.




## How restoration works

When you restore a Spanner Omni database, you must specify a source backup and a new target database. You cannot restore to an existing database.

The restore process provides high availability. You can restore the database provided that the majority quorum of the regions and zones in the target is available.

## Restoration states

A restored database transitions through three states, tracked by two long-running operations.

State | Description  
---|---  
`CREATING` |  Spanner Omni begins restoring by creating a new database and mounting files from the backup. During this state, the restored database is not yet ready for use. Once complete, your database is ready to use.   
  
**Note:** Spanner Omni doesn't allow you to delete the backup while it restores. You can delete it after the restore completes and the database enters the `READY` state.   
`READY_OPTIMIZING` |  After mounting the backup, Spanner Omni starts copying data into the new database while optimizing its stored size. Your database is ready for use during this process.   
  
**Caveats:**

  * Read latencies might be slightly higher than usual.
  * Storage metrics display the size of the new database, not the backup. Results might not reflect the total size of all your data during transfer.
  * You cannot delete the mounted backup during this state.

  
`READY` |  Once the copy-and-optimize operation completes, the database transitions to the `READY` state. The database is fully restored and no longer requires the backup.   
  
To track progress during the `CREATING` state, you can query the long-running restore operation, which returns a `RestoreDatabaseMetadata` object. During the `READY_OPTIMIZING` state, the operation returns an `OptimizeRestoredDatabaseMetadata` object.

## Access control (IAM)

The following roles provide the permissions required for Spanner Omni restore operations:

IAM role | Permissions  
---|---  
`roles/spanner.restoreAdmin` | Permission to restore from a backup.  
`roles/spanner.admin` | Full access to restore operations and all other Spanner Omni resources.  
`owner` | Full access to restore operations.  
`editor` | Full access to restore operations.  
`viewer` | Permission to view restore operations. Cannot create, update, delete, or copy a backup.  
  
## Restore a database from a backup

To restore a database, use the `spanner databases restore` command:
    
    
    spanner databases restore \
      --destination-database=RESTORE_DATABASE_NAME \
      --source-backup=BACKUP_NAME \
      --async
    

## What's next

  * [Create and manage Spanner Omni backups](https://docs.cloud.google.com/spanner-omni/backups)
  * [Replicate data from Spanner to Spanner Omni](https://docs.cloud.google.com/spanner-omni/replicate-data)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
