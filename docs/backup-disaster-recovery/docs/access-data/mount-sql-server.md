---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sql-server/
title: Mount Microsoft SQL Server databases in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:51.759110+00:00
---

# Mount Microsoft SQL Server databases in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-sql-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mount Microsoft SQL Server databases in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This section describes how to mount captured Microsoft SQL server:

  * Instances
  * Primary databases of an AlwaysOn Availability Group
  * Consistency groups
  * Individual members of a consistency group
  * System databases
  * User databases



## Mount captured Microsoft SQL Server data

With a standard mount you can mount the Microsoft SQL Server data to another server where it can be picked up and used by another Microsoft SQL Server. To mount just the captured Microsoft SQL data, follow these steps:

  1. Open the **App Manager** to the **Applications List**.

  2. Right-click a SQL Server Server instance, user database, system database, cluster, or availability group and select **Access**. Use the filters to find the database you need.

  3. On the runway, select the specific backup to be mounted, then select **Mount**.

**Note:** You can use the calendar widget in the upper left corner to narrow the range of backups.**Note:** OnVault backups can be mounted very efficiently from backup/recovery appliances. You may choose how the snapshot pool is used in this kind of mount, with options including storage optimized, balanced, performance optimized, and maximum performance. The first three options result in a mount that takes place quickly, and uses varying amount of storage in the snapshot pool to boost performance. The last option, maximum performance, copies all data to the snapshot pool before the mount is performed.**Note:** The 'Maximum performance' option is only supported for OnVault backups.
  4. Optionally, enter a label that lets you clearly identify this mounted data.

  5. In the **Application Options** section of the **Mount Image** dialog, don't select **Create New Virtual Application**. To mount the Microsoft SQL data as a virtual database, see Mount a SQL server database as a new virtual database.

  6. Complete the **Mapping Options** and **Item Selection** fields if applicable.

Options presented vary according to the source that is selected. For example, databases on VMware VMs have a **Map to all ESX hosts** option. Clustered databases have the **Map to Cluster Nodes** option.

  7. Click **Submit** and the mount job is submitted.

  8. Once the mount operation is successful, log onto the database server and verify that the mounted backup is available in the Active Mounts.




## Mount a SQL Server database as a new virtual database

A virtual application mount operation mounts a captured database as a virtual application. It lets you bring a database online quickly without having to actually move the data and without having to manually configure a new instance of the database. A virtual application mount addresses the challenges of creating and managing copies of production databases without manual intervention by database, server, and storage administrators.

This section describes how to mount a captured Microsoft SQL Server database as a virtual application. You can mount the following for Microsoft SQL Server:

  * Instances
  * System databases
  * User databases
  * Consistency groups
  * Individual members of a consistency group
  * Databases in AlwaysOn Availability groups



Before mounting a backup, ensure that iSCSI has been configured on the host where the backups are mounted, or NFS datastores in VMware have been configured.

**Note:** A database mounted to a protected SQL instance as a virtual application is not be protected with the SQL instance.

If you want to mount just the Microsoft SQL data files without adding any database to a SQL Server instance, see Mount captured Microsoft SQL data.

For corrupt or deleted databases, mounting a SQL Server database as a virtual application to its original server is an efficient alternative to performing a restore of the database.

To mount a captured Microsoft SQL Server database as a virtual application, follow these steps:

  1. Open the appliance management console to the **App Manager** > **Applications** list.

  2. Right-click a SQL Server instance, user database, system database, cluster, or availability group, and select **Access**. Use the filters to find the database you need.

  3. On the runway of backups, select the backup to be mounted. On the right side, select **Mount**. You can use the calendar widget in the upper left corner to narrow the range of backups.

**Note:** OnVault backups can be mounted very efficiently from backup/recovery appliances. You can choose how the snapshot pool is used in this kind of mount, with options including storage optimized, balanced, performance optimized, and maximum performance. The first three options result in a mount that takes place quickly, and uses varying amount of storage in the snapshot pool to boost performance. The last option, maximum performance, copies all data to the snapshot pool before the mount is performed.**Note:** The 'Maximum performance' option is only supported for OnVault backups.
  4. In the **Application Options** section, optionally enter a label that lets you clearly identify this mounted data.

  5. Select **Create New Virtual Application**.

  6. If the database was captured along with its logs, the **App Options** dialog provides an option to roll the logs to a specific point in time based on when and how often logs were captured.

  7. From the **SQL Server Instance Name** drop-down list, select the SQL Server instance that the new database should be added into. If the required instance name is not included in the drop-down, you can type the name manually in the space provided.

  8. If you are mounting a single database, then enter a name for your new virtual database into the **SQL Server Database Name** field.

If you are mounting multiple databases, then enter a name for a new consistency group that contains your virtual databases into the **Name of Consistency Group** field.

**Note:** Valid characters include letters, numbers, @, #, -, _. Leading and trailing spaces are not allowed.
  9. The virtual application mount is a new virtual database. To protect the new virtual databases, select **Manage New Application** , and select the template and profile to use.

The virtual application mount is a new database. The snapshots of the database are incremental.

The virtual application appears in the **Application Manager** list of applications.

If you don't select **Manage New Application** then it appears in the **Application Manager** as an unprotected application. It can be protected like any other application.

Virtual SQL Server databases mounted to a SQL Server instance are always protected separately from the instances' user and system databases.

  10. **Recover Database After Restore** : Leave this selected—default—if you want to bring the database to an online state ready to process transactions. Clear this to leave the database in a restoring state, so additional transaction log backups can be manually applied to roll the database forward to a specific point in time.

  11. **Recover User Logins** : If you have enabled the policy option **Backup SQL Server Logins** , then selecting this option results in a restore of those logins to the target SQL Server instance. For domain accounts, the user accounts only are restored if the target instance is on a server in the same domain, or in a domain with a trust relationship to the source SQL server. SQL local accounts are always be restored. Use this option if you want to ensure all users who could access the original source database can access the new virtual database.

  12. In the **Username and Password** fields enter a username and password only if needed. If the Backup and DR agent account does not have privileges to detach the database during an unmount operation, or to apply transaction logs, then enter credentials here for an account with those privileges. See [Required SQL Server roles for the Windows user](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/sql-permissions) for details.

  13. Select a **Recovery Model** if you want to change the recovery model of the new virtual databases. The default is to retain the original database's recovery model.

  14. For **Overwrite Existing Database** , indicate when to overwrite a database on the target server or instance that has the same name as the new databases being mounted: **Yes** , **No** , or **Only if it's Stale**.

  15. In the **Mapping Options** , you can enter a **Mount Location**. If an application has only one volume, you can only specify the mount location here. If an application has multiple volumes, you can:

     * Enter a mount location. All volumes are automatically mounted at the specified mount location, using sequential drive letters or numbered directories at the specified mount point.

     * Leave this space blank and in the **Advanced Options** , manually specify a mount location for each volume.

  16. Click **Submit** and the job is submitted.

  17. When the mount job is finished, log onto the database server and verify that mounted backup is available in the Active Mounts.


**Note:** When performing a virtual application mount of a SQL Server database to a SQL Server failover instance, if you specify a custom mount point, the custom mount point must reside on a volume that is a cluster resource. This is required to allow the SQL Server instance to move to other cluster nodes in case of failover.

## Management of the active mounts

Once you have created a mount, you can track the backup from the **App Manager** > **Active Mounts**. Ideally, don't leave any backup mounted indefinitely. This is because the backup that the mount was created from cannot expire until all its mounts have been deleted. When you have finished using the mounted backup then either:

  * [Unmount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount) the backup. You can [remount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#remount) it if needed. You can then [delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#delete) the backup later when you are certain it is no longer needed.
  * [Unmount and delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount-delete) the backup. This deletes the mounted backup, not the backup that the mount is based on.
  * [Migrate](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate) the backup. This is only for Microsoft SQL Server Mounts.



## Mount encrypted SQL Server data

Backup/recovery appliances capture encrypted SQL Server databases but don't capture their private keys, encryption certificates, or passwords.

This section describes the following:

  * Determining if SQL TDE is enabled

  * Troubleshooting SQL Server encryption

  * SQL Server master key, encryption certificate, and password procedures




If you are restoring an encrypted SQL Server database over an existing SQL Server database, the private key, encryption certificate, and password are already present on the SQL Server instance and once the restore operation finishes, the SQL Server database works as expected.

If you are performing a virtual application mount of an encrypted database, or a mount of just the encrypted SQL Server data, the SQL Server instance on which the encrypted database or data is mounted must have the following:

  * **Transparent Data Encryption** (TDE) enabled

  * A copy of the **Private Key** from the source SQL Server database

  * A copy of the encryption certificate from the source SQL Server database

  * Provide the password of the source SQL Server database




Procedures are in SQL Server master key, encryption certificate, and password procedures.

**Note:** If you are not mounting the database back to the source SQL Server instance, then the private key and encryption certificate must be manually copied from the source SQL Server instance to the new SQL Server instance.

## Determine if SQL Server TDE is enabled

To determine if TDE is enabled on a SQL Server instance, you can use Microsoft's SQL Server management studio's user interface (SSMS), or you can use a manual query to determine if encryption is enabled on a database. For example:
    
    
            SELECT
             DB_NAME(database_id)AS dbname,
             encryption_state,
             case encryption_state
               WHEN 0 THEN 'Unencrypted (no
            database encryption key present)'
               WHEN 1 THEN 'Unencrypted'
               WHEN 2 THEN 'Encryption in Progress'
               WHEN 3 THEN 'Encrypted'
               WHEN 4 THEN 'Key Change in Progress'
               WHEN 5 THEN 'Decryption in Progress'
               ELSE CAST(encryption_state AS
            varchar(20))
             END AS encryption_state,
             key_algorithm,
             key_length
             FROM sys.dm_database_encryption_keys
    

### SSMS

To use SSMS to determine if encryption is enabled on a database, follow these steps:

  1. From SSMS right-click on the database name.

  2. From the drop-down menu select **Properties** and the database's properties are displayed.

  3. Under **Select a Page** , click **Options** and the options for the database are displayed.

  4. Under **State** , ensure that **Encryption Enabled** is set to **True**.




### Troubleshoot SQL Server encryption

The following are two common errors:

  * **SQL error 24583** : This indicates a missing encryption certificate. The following 24583 SQL Server error indicates that you are trying to perform a mount to a SQL Server instance that does not have the encryption certificate of the source SQL Server instance.

  * **SQL error 33117** : The transparent data encryption not enabled. The following 33117 SQL Server error indicates that you are trying to perform a mount of an encrypted SQL Server database to a SQL Server instance that does not have **Transparent Data Encryption** enabled.




### SQL Server master key, encryption certificate, and password procedures

Creating and copying master keys and encryption certificates are standard Microsoft SQL Server procedures that are not unique to backup/recovery appliances. They are provided here as a convenience:

  * Create a new master key

  * Create a new encryption certificate

  * Apply server master key and encryption certificate

  * Create a copy of the server master key, encryption certificate, and provide source password

  * Copy the encryption certificate, private key, and provide source password




For more information, see Microsoft's detailed information on security certificates and keys: https://msdn.microsoft.com/en-us/library/ff848768.aspx

#### Create a new master key
    
    
            use master;
            go
            create master key encryption by password = 'SMKSourcePassword';
            go
    

#### Create a new encryption certificate
    
    
            use master;
            go
            create certificate sourcedbcert with subject = 'Act Test Cert';
            go
    

#### Apply server master key and encryption certificate
    
    
            use DATABASENAME;
            go
            CREATE DATABASE ENCRYPTION KEY
            WITH ALGORITHM = AES_128
            ENCRYPTION BY SERVER CERTIFICATE sourcedbcert;
            go
            alter database DATABASENAME
            set encryption on;
            go
    

#### Create copy of server master key, encryption certificate, and provide source password

If a SQL Server database on one SQL Server instance is mounted to another SQL Server instance, you must manually copy the to-be-mounted database's server master key, encryption certificate, and password. Then copy the server master key, encryption certificate, and password to the other SQL Server instance.

To make a copy of a server master key, encryption certification, and password, complete the following:
    
    
            use master;
            go
            backup certificate sourcedbcert to file = 'E:\Enc\Sourcecert'
            with PRIVATE KEY (file='E:\Enc\Privatekey',
            ENCRYPTION BY PASSWORD='SecurePassword');
            go
    

#### Copy encryption certificate, private key, and provide source password

If an encryption-enabled SQL Server database or data is mounted to a new SQL Server instance, the new instance must have a copy of the source SQL Server instance's server master key, encryption certificate, and password. Manually copy the encryption certificate and password copies you made on the source SQL Server instance in the previous section to the new SQL Server instance. From the new SQL Server instance, complete the following:
    
    
            create certificate destinationdbcert
            FROM file = 'C:\Program Files\Backup and DR\sqlenc\Sourcecert'
            with private key (file = 'C:\Program Files\Backup and DR\sqlenc\Privatekey',
            decryption by password = 'SecurePassword')
            go
    

## Other documentation for Backup and DR for Microsoft SQL Server

This page is one in a series of pages specific to protecting and recovering Microsoft SQL server databases and supporting binaries with Backup and DR. You can find additional information in the following pages:

  * [Backup and DR for Microsoft SQL Server](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/sql-intro)
  * [Prepare SQL server databases for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-sql-server)
  * [Add a SQL server database host and discover databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/sql-discovery)
  * [Configure backup plans for Microsoft SQL Server instances and databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/sql-protect)
  * [Mount a SQL Server database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/sql-access)
  * [Mount databases into SQL Always On availability groups](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/sql-create-AAG-mount)
  * [Manage an active mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts)
  * [Migrate a SQL server database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/sql-server-mount-and-migrate)
  * [Clone SQL server databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/sql-cloning)
  * [Recover SQL server backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/sql-restore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
