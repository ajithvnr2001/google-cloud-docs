---
url: https://docs.cloud.google.com/compute/docs/instances/sql-server/migrate-sql-server-database-from-windows-to-linux/
title: Migrate a SQL database from Windows to Linux \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:22.772498+00:00
---

# Migrate a SQL database from Windows to Linux  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/sql-server/migrate-sql-server-database-from-windows-to-linux/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Migrate a SQL database from Windows to Linux Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial guides you through two distinct approaches for migrating a SQL Server database from a Windows Server to a Linux Server. 

This page discusses the following methods:

  * [Export and import a database](https://docs.cloud.google.com/compute/docs/instances/sql-server/migrate-sql-server-database-from-windows-to-linux#export_and_import_the_database)
  * [Migrate using the SQL backup and restore feature](https://docs.cloud.google.com/compute/docs/instances/sql-server/migrate-sql-server-database-from-windows-to-linux#migrate_using_sql_backup_and_restore)



The ideal migration method is influenced by the acceptable downtime for a specific database and its size. The most frequently employed technique is the backup and restore method.

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://docs.cloud.google.com/compute/all-pricing)
  * [SQL Server VMs](https://cloud.google.com/sql-server)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

Ensure that you have the following:

  * A Google Cloud project and virtual private cloud (VPC) with connectivity to your Active Directory domain controllers.
  * A subnet to use for the Windows Server Failover Cluster (WSFC) virtual machine (VM) instances.



To complete the guide, you also need a Google Cloud project:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




When you finish this tutorial, you can avoid continued billing by deleting the resources you created. For more information, see Cleaning up.

The following sections discuss how to migrate a SQL Server database from a Windows-based server to a Linux-based one.

## Import a SQL database to Linux

This section discusses how to export a SQL database from a Windows-based SQL Server, and import it to a Linux-based SQL Server using SQL Server Management Studio (SSMS).

### Prerequisites

To import a SQL database to Linux, you need the following:

  * Windows machine with the following:

    * SQL Server installed.
    * [SSMS](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16) installed.
    * The SQL database that you want to migrate is present on this machine. This tutorial uses a sample [AdventureWorks2022](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms) database.
  * Linux machine with SQL Server installed.




### Export a SQL database from a Windows-based SQL Server

To export a SQL database from a Windows-based SQL Server, use the following steps:

  1. On the Windows machine, create a new folder on the C: drive and name it `export` (`c:\export`).
  2. Open SSMS.
  3. In the Connection window, enter localhost and click **Connect**.
  4. In Object Explorer, expand **Databases**.
  5. Right-click your target database, select **Tasks** , and then click **Export Data-Tier Application...**. The Export Data wizard opens.

![Export Data.](https://docs.cloud.google.com/static/compute/images/sql-server-export-data-tier.png)

  6. In the Export Data wizard, select **Next**.

  7. In the Settings tab, configure the Export Data wizard to save the backup package (BACPAC) file (.bacpac) to local disk.

  8. Specify folder and filename, as follows:
         
         c:\export\MigrationFile.bacpac
         

  9. Click **Next**.

  10. Review the specified settings and click **Finish** to start the export process. The .bacpac file is successfully created at the location you chose. You can now import it into a target SQL Server.




### Import a database to a Linux

To import a SQL database to a Linux-based SQL Server, use the following steps:

  1. Open SSMS.
  2. In the Connection window, enter the IP address of the target server and click **Connect**.
  3. Right-click the **Databases** folder in the Object Explorer and select **Import Data-tier Application...**.
  4. Specify the .bacpac file created in the export procedure.
         
         c:\export\MigrationFile.bacpac
         

  5. Click **Next**.

  6. Specify **AdventureWorks2022**.
         
         AdventureWorks2022
         

  7. Verify that the data and log path shows the default settings from the Linux instance.

  8. Click **Next**.

  9. Review the import settings and click **Finish** to start the import.

![Import bacpac file settings.](https://docs.cloud.google.com/static/compute/images/sql-server-import-bacpac-settings.png)

  10. Click **Close** to close import wizard. The database is ready for connections.




## Migrate using SQL backup and restore

You can migrate a database from SQL Server on Windows to SQL Server on Linux using the backup and restore feature. This section provides a step-by-step guide to help you transfer your database to the Linux environment using this method.

### Prerequisites

To migrate a database using the backup and restore method, you need the following:

  * Windows machine with the following:

    * SQL Server installed.
    * [SQL Server Management Studio](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16) (SSMS) installed.
    * Database to migrate. This document uses [AdventureWorks2022](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms) database.
  * A Linux machine with SQL Server installed.




### Backup your database on your Windows machine

You can backup a database to a file with Windows using SSMS, as follows:

  1. Open SSMS on the Windows machine.
  2. In the Connection window, enter localhost.
  3. In Object Explorer, expand **Databases**.
  4. Right-click your target database, select **Tasks** , and then click **Back Up...**.

![Create Backup.](https://docs.cloud.google.com/static/compute/images/sql-server-create-database-backup.png)

  5. In the Backup Database window, verify that **Backup type** is set to **Full** and **Back up to** is set to **Disk**. Take note of the name and location of the backup file. For example, a database backup on SQL Server 2022 has a default location of **C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\Backup**.

![SQL database backup options.](https://docs.cloud.google.com/static/compute/images/sql-server-database-backup-options.png)

  6. Click **OK** to begin the backup.




### Copy the backup file to your Linux machine

You can use a Secure Copy Protocol (SCP) client to upload the backup file to your Linux machine. The following procedure uses and SCP command line client. However, you can also use [WinSCP](https://winscp.net/) or the [Git Bash Shell](https://git-scm.com/downloads) to upload the file.

  1. Open new command prompt on your Windows machine and navigate to the directory containing the backup file created in section Backup your database on your Windows machine. For example:
         
         cd 'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\Backup\'
         

  2. Use the `scp` command to copy the file to the target Linux machine. The following example uses `MigrationBackup.bak` file created earlier.
         
         scp MigrationBackup.bak sysadmin@LINUX_INTERNAL_IP:./
         

Replace LINUX_INTERNAL_IP with the IP of your Linux machine.

![Copy backup file to target machine.](https://docs.cloud.google.com/static/compute/images/sql-server-scp-copy-file-to-linux.png)


**Note:** You can also use a Cloud Storage bucket as temporary storage to transfer a backup file from a Windows machine to a Linux machine.

### Move backup file

To restore the database to SQL Server on a Linux machine, you must ensure that the backup file is in the default location owned by `mssql` user, that is, `/var/opt/mssql`.

To move the backup file to the `mssql` directory, use the following steps:

  1. From the Windows machine connect to the target Linux machine using SSH.
         
         ssh sysadmin@LINUX_INTERNAL_IP
         

Replace LINUX_INTERNAL_IP with the IP of your Linux machine.

  2. Create a new backup directory.
         
         sudo mkdir -p /var/opt/mssql/backup
         

  3. Move the backup file to the newly created directory.
         
         sudo mv ~/MigrationBackup.bak /var/opt/mssql/backup
         




### Restore the database

You can restore the database on a Linux machine using SSMS using the following steps:

  1. Open SSMS on your Windows machine.
  2. In the Connection window, enter the IP address or hostname of the Linux machine.
  3. Specify the **Login** information and **Password**.
  4. Click **Connect**.

![Select backup file to restore.](https://docs.cloud.google.com/static/compute/images/sql-server-login-to-linux-machine.png)

  5. In Object Explorer, right-click the **Databases** folder and select **Restore Database...**

  6. In the Restore Database window, set **Source** to **Device** , click **...** to open backup selection dialog.

  7. In the Select backup device dialog, click **Add**.

  8. In the file browser, click the **\var\opt\mssql\backup** directory and select uploaded backup file.

  9. Click **OK** to accept the selection and close the dialog.

  10. Review the populated backup media and click **OK**.

![Select backup file to restore.](https://docs.cloud.google.com/static/compute/images/sql-server-select-backup-file-to-restore.png)




Before you begin restoring your database on a Linux machine, you must update the location of the restored database files on your Linux machine because the path from the Windows server does not exist on the Linux server.

  1. In the left menu click **Files**.
  2. Select **Relocate all files to folder** to move the restored files to the SQL Server default data directory.
  3. Click **OK** to begin restore process.
  4. Verify the restoration by listing all of the databases on the server. The restored database should be listed.
         
         SELECT Name FROM sys.Databases
         GO
         

  5. Run other queries on your migrated database.
         
         USE AdventureWorks2022
         SELECT top 100 * FROM [Person].[Person]
         GO
         




## Clean up

After you finish the tutorial, you can clean up the resources that you created so that they stop using quota and incurring charges. The following sections describe how to delete or turn off these resources. 

## Deleting the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Learn how you can [Set up a SQL Server cluster on Linux with Always On availability groups and Pacemaker](https://docs.cloud.google.com/compute/docs/tutorials/high-availability-linux-pacemaker).
  * Learn how you can [configure a SQL Server failover cluster instance that uses Persistent Disk in multi-writer mode](https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-failover-cluster-instance-pd-multi-writer).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
