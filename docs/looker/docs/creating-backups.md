---
url: https://docs.cloud.google.com/looker/docs/creating-backups/
title: Creating backups \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:03:19.432529+00:00
---

# Creating backups  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/creating-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Creating backups Stay organized with collections  Save and categorize content based on your preferences. 

If your Looker instance is Looker-hosted, Looker automatically performs regular backups for your instance. See the Automatic backups for Looker-hosted instances section for more information.

If your instance is customer-hosted, then you will need to create your own backups. See the Backup strategy for customer-hosted instances section for more information.

## Automatic backups for Looker-hosted instances

Looker-hosted instances are backed up automatically, once every 24 hours. Each backup contains a record of all the data in the instance's internal database and in the instance's file server, which is most of the operational data for the Looker instance. However, the data for [Elite System Activity](https://docs.cloud.google.com/looker/docs/elite-system-activity) is not backed up.

Backups are retained for 30 days. To access and restore a backup, [contact Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details).

**Caution:** Disabling the Looker API disables the ability to create instance backups.

## Backup strategy for customer-hosted instances

**Warning:** If your instance is customer-hosted, do not modify LookML files directly on the filesystem of your instance. This can cause unexpected errors in your Git workflow. To make changes to your LookML files, follow the steps at [Using version control and deploying](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes).

For customer-hosted instances, you can create a backup of a basic Looker installation simply by making a copy of the Looker user's home directory (including all normal and hidden subdirectories). You can use `scp`, `rsync`, or any standard backup application. Similarly, restoring a basic Looker installation just requires restoring the files and starting up Looker.

In some configurations, including clustered environments, Looker uses an external MySQL database for application settings, user accounts, and other data. In this case we recommend creating a backup of the MySQL database, in addition to the Looker home directory.

We highly recommend that you create these backups daily. We also recommend performing a test restoration once per quarter.

### Directory structure

The standard subdirectories under the Looker user's home directory (usually **/home/looker**) are described here.

  * _folder_ home 
    * _folder_ looker
    * _folder_ .ssh
    * _folder_ looker 
      * _folder_ .cache
      * _folder_ .db
      * _folder_ .ssl
      * _folder_ .tmp
      * _folder_ deploy_keys
      * _folder_ log
      * _folder_ models
      * _folder_ models-user-1

Directory | Backup Required | Change Frequency | Description  
---|---|---|---  
.ssh | Yes | Rare | ssh keys used for authenticating to Git for LookML projects created with Looker 4.6 or older  
looker/.cache | No | Frequent | Temporary cache files  
looker/.db | Yes, unless backend DB has been [migrated to MySQL](https://docs.cloud.google.com/looker/docs/migrating-looker-backend-db-to-mysql) | Frequent | Looker internal database  
looker/.snapshots | No | On Update | A backup copy of the Looker jar and .db directory are stored here during updates  
looker/.ssl | Maybe | Rare | Self-signed SSL certificates (see note)  
looker/.tmp | No | Frequent | Temporary files  
looker/deploy_keys | Yes | Rare | ssh keys used for authenticating to Git for LookML projects created with Looker 4.8 or later  
looker/log | Maybe | Frequent | Log files; only needed if required by your retention policies  
looker/models | No | Variable | Production models, copied from the source repository (usually GitHub)  
looker/models-user-* | Yes | Variable | Each user's development models are stored in separate directories with the user's ID number  
  
**SSL Note:** By default the SSL directory only contains a self-signed SSL cert, which does not need to be retained. However, if you store any additional files in this directory — such as SSL certificates signed by a certificate authority — this directory should be added to your backup.

Files outside of the Looker home directory, which should be added to your backup, include the following:

Directory | Backup Required | Change Frequency | Description  
---|---|---|---  
/etc/init.d/looker | Yes | Rare | System startup script for Looker  
SSL Certificates | Yes | Rare | If you are using SSL certificates, ensure all required files are included  
  
> Although it doesn't typically cause problems, some customers have reported issues if they include the `looker/.db/looker.lck` file in their backups. You can safely exclude this file if necessary.

### Creating a backup

You can create a backup of your Looker instance with any standard backup application, as well as with command line tools such as rsync.

It is best for the backup process to run when the application is as lightly used as possible. In addition to normal user interaction, consider the times that scheduled Looks might be running, derived tables might be rebuilding, etc.

#### Clustered environments

Clustered Looker instances store their application configuration, user accounts, and other data in an external MySQL database. We recommend creating a backup of this database at the same time as the Looker application. See the [MySQL documentation](https://dev.mysql.com/doc/refman/5.0/en/backup-and-recovery.html) for more details on how to back up MySQL databases.

### Generating a keystore-independent backup

A customer-hosted installation that has [migrated to AES-256 GCM encryption](https://docs.cloud.google.com/looker/docs/migrating-to-aes-256-gcm-encryption) and is not using AWS KMS can use this procedure to create a backup of their Looker instance that is independent of their local Customer Master Key (CMK). This procedure provides a method for migrating a customer-hosted instance to a Looker-hosted instance without having to provide a CMK, or for moving a customer-hosted instance to a new host that does not have access to the same local keystore.

To create a keystore-independent backup:

  1. Stop Looker:
         
         cd looker
         ./looker stop
         

> If your Looker instance is clustered, make sure to stop every node before proceeding.

  2. Ensure that your Looker instance can access your CMK. If your CMK is stored in a file, you can use the environment variable `LKR_MASTER_KEY_FILE` to point to the path of your CMK file:
         
         export LKR_MASTER_KEY_FILE=<path_to_CMK_file>
         

Or, to provide your CMK directly in an environment variable, you can use the `LKR_MASTER_KEY_ENV` environment variable:
         
         export LKR_MASTER_KEY_ENV=<CMK_value>
         

  3. Generate a new key file that will be used to re-encrypt the Key Encryption Key (KEK):
         
         ./looker generate_keyfile_for_backup <key_file_name>
         

Where `<key_file_name>` is the name you want to use for the file that Looker will create and then use to write the new key.

The contents of the new key file will look like:
         
         {"dbmk":"vr1LUwO3q6weY8iS3JykVljSjiD4m6eGk227Cs7Qu9Q=\n","backup_uid":"XCXvRa38mNeqT6+HRBCo2Q=="}
         

Where the value for `dbmk` is a Base64 encoding 256 bit encryption key and `backup_uid` is a unique name used when saving the key to the database.

  4. Use the new key file to create a new key entry in Looker's internal database:
         
         ./looker keystore_independent_recrypt <key_file_name>
         

Where `<key_file_name>` is the key file created earlier.

This decrypts the KEK in the internal database using the CMK, then re-encrypts the KEK with the new key and persists that encrypted value to the database.

  5. Create a backup of your Looker instance using your regular backup method.




To [restore this keystore-independent backup](https://docs.cloud.google.com/looker/docs/restoring-backups#restoring_a_keystore-independent_backup), you will need the new key file created earlier.

### Restoring backups

To restore a backup of your Looker instance, see the [Restoring backups](https://docs.cloud.google.com/looker/docs/restoring-backups) documentation page.

## Next steps

After you have set up backups, you will be ready to [ensure that your Looker instance can access necessary services](https://docs.cloud.google.com/looker/docs/outbound-port-requirements).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
