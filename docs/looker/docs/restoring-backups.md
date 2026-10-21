---
url: https://docs.cloud.google.com/looker/docs/restoring-backups/
title: Restoring backups \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:12:48.183644+00:00
---

# Restoring backups  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/restoring-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Restoring backups Stay organized with collections  Save and categorize content based on your preferences. 

**Warning:** If your instance is customer-hosted, do not modify LookML files directly on the filesystem of your instance. This can cause unexpected errors in your Git workflow. To make changes to your LookML files, follow the steps at [Using version control and deploying](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes).

To learn about _creating_ Looker backups, see the [Creating backups](https://docs.cloud.google.com/looker/docs/creating-backups) documentation page.

To _restore_ a customer-hosted Looker instance to a new host, complete only these steps of the [Looker installation instructions](https://docs.cloud.google.com/looker/docs/installing-looker-application):

  * Verify that the new server complies with the minimum server specifications.
  * Enable ntpd or chronyd.
  * Create the **looker** user, group, and home directory.
  * Skip downloading the Looker application and all remaining installation steps.



Once the new host is prepared:

  * Restore the files from backup.
  * Start Looker:
        
        sudo su - looker
        cd looker
        ./looker start
        




## Clustered environments

To restore the MySQL database for a clustered environment:

  * Stop any running Lookers in the cluster.
  * Restore the database.
  * Start the Looker instances one at a time.



See the [MySQL documentation](https://dev.mysql.com/doc/refman/5.0/en/backup-and-recovery.html) for more details on how to restore MySQL databases.

## Restoring a keystore-independent backup

Customer-hosted installations that have [migrated to AES-256 GCM encryption](https://docs.cloud.google.com/looker/docs/migrating-to-aes-256-gcm-encryption) and [generated a keystore-independent backup](https://docs.cloud.google.com/looker/docs/creating-backups#generating_a_keystore-independent_backup) need to update Looker's internal database after performing a restore.

After restoring a keystore-independent backup, follow this procedure to decrypt the KEK, re-encrypt it using the new local keystore, and update the key entry in the internal database:

  1. Stop Looker:
         
         cd looker
         ./looker stop
         

If Looker is clustered, make sure to stop every node before proceeding.

If any nodes are still running when you later issue the `restore_dr_backup` command, the command will fail with the message, "There are other live nodes connected to this backend Looker database. If Looker was shutdown within the last minute, try again shortly, otherwise verify all nodes in the cluster are shut down."

  2. Ensure that Looker can access the CMK used for the local keystore of the location where you restored Looker. If the CMK of the restore location is stored in a file, you can use the environment variable `LKR_MASTER_KEY_FILE` to point to the path of the CMK file:
         
         export LKR_MASTER_KEY_FILE=<path_to_CMK_file>
         

or, if you want to provide the CMK of the restore location directly in an environment variable, you can use the `LKR_MASTER_KEY_ENV` environment variable:
         
         export LKR_MASTER_KEY_ENV=<CMK_value>
         

  3. Update the internal database:
         
         ./looker restore_dr_backup <path_to_CMK_file>
         

where `<path_to_CMK_file>` is the path and filename of the plain text key file created when the keystore-independent backup was made. The key file has the following format:
         
         {"dbmk":"vr1LUwO3q6weY8iS3JykVljSjiD4m6eGk227Cs7Qu9Q=\n","backup_uid":"XCXvRa38mNeqT6+HRBCo2Q=="}
         

where the value for `dbmk` is a Base64 encoding 256-bit encryption key and `backup_uid` is a unique name used when saving the key to the database.




After you have updated Looker's internal database, you can start Looker normally. Once Looker is running, we recommend that you delete the plaintext key file used to create the keystore-independent backup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
