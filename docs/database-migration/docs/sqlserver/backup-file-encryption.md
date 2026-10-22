---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/backup-file-encryption/
title: Use encrypted SQL Server backup files \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:41.871175+00:00
---

# Use encrypted SQL Server backup files  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/backup-file-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Use encrypted SQL Server backup files Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use encrypted backup files for migrating from self-managed or Amazon RDS sources to Cloud SQL for SQL Server.

Database Migration Service is fully compatible with encrypted SQL Server backups from self-managed and Amazon RDS sources. You can upload your encryption key to Google Cloud so that Database Migration Service can safely decrypt your data and load it to the Cloud SQL for SQL Server destination instance without compromising your data security.

If you want to use encrypted backup files, you must encrypt **every backup file** (full, differential, transaction log) you use for a specific database included in your migration. That is, if you want to encrypt your full backup file, then you must also encrypt the differential backup file and the transaction log files you use for that database. All backup files must be encrypted with the same key.

Backup encryption is evaluated per database. For example, if you migrate two databases from your source SQL Server instance: `my-business-database` and `my-other-database`, you can use encrypted backups independently for `my-business-database`, or `my-other-database`, or both databases.

To use encrypted backups for your migration, perform the following steps:

  1. Take the backup of your source SQL Server instance and use the encryption features. Save your encryption keys in a safe location to upload them later to Cloud Storage. See [ Backup encryption](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/backup-encryption) in Microsoft documentation.

  2. [Upload the encryption keys](https://docs.cloud.google.com/storage/docs/uploading-objects) to a Cloud Storage bucket.

  3. **Google Cloud CLI only** : Create a mapping file in the JSON format to match the encryption keys with their relevant databases included in your migration job. The mapping file is an array of objects that each represent mappings for a single database. Example configuration file:
         
         [
         {
           "database": "db1",
           "encryptionOptions": {
             "certPath": "Path to certificate 1",
             "pvkPath": "Path to certificate private key 1",
             "pvkPassword": "Private key password 1"
           }
         },
         {
           "database": "db2",
           "encryptionOptions": {
             "certPath": "Path to certificate 2",
             "pvkPath": "Path to certificate private key 2",
             "pvkPassword": "Private key password 2"
           }
         }
         ]
         

Where:

     * `database` is your database identifier. That identifier must match the [ database folder names in your Cloud Storage](https://docs.cloud.google.com/database-migration/docs/sqlserver/storage-buckets).
     * `certPath`, `pvkPath` and `pvkPassword` are Cloud Storage paths to the certificate files in the format `gs://BUCKET_NAME/OBJECT_NAME`. For example: `gs://my-bucket-name/certificate-folder/certificate-key-file1`. For more information, see [Object namespaces](https://docs.cloud.google.com/storage/docs/objects#namespace) in the Cloud Storage documentation.
  4. Provide the Cloud Storage paths to your encryption keys when you [ create the migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver/create-migration-job).

  5. When you create more backup files (the differential backup file or transaction log files), make sure you encrypt then with the same encryption key you used for the full backup.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
