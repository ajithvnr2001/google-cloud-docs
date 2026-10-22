---
url: https://docs.cloud.google.com/compute/docs/instances/sql-server/cloning-a-microsoft-sql-server-database-on-compute-engine/
title: Cloning a Microsoft SQL Server database on Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:25.703616+00:00
---

# Cloning a Microsoft SQL Server database on Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/sql-server/cloning-a-microsoft-sql-server-database-on-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Cloning a Microsoft SQL Server database on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows two ways to clone a [Microsoft SQL Server database](https://en.wikipedia.org/wiki/Microsoft_SQL_Server) running on Compute Engine. One method uses [persistent disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots). The other method uses native SQL Server backup and restore, transferring the backup using [Cloud Storage](https://docs.cloud.google.com/storage). Cloud Storage is Google Cloud's object storage service. It offers a straightforward, security-enhanced, durable, and highly available way to store files.

Cloning is the process of copying an online database onto another server. The copy is independent of the existing database and is preserved as a point-in-time snapshot. You can use a cloned database for various purposes without putting a load on the production server or risking the integrity of production data. Some of these purposes include the following:

  * Performing analytical queries
  * Load testing or integration testing of your apps
  * Data extraction for populating data warehouses
  * Running experiments on the data



Each cloning method described in this tutorial has advantages and disadvantages. The ideal method for you depends on your situation. The following table highlights some key issues.

**Issue** | **Method 1: Disk snapshots** | **Method 2: Backup and restore using Cloud Storage**  
---|---|---  
Additional disk space required on SQL Server instances | No additional disk space required | Additional space required for storing the backup file when creating and restoring  
Additional load on source SQL Server instances during cloning | No additional load | Additional load on CPU and I/O when creating and uploading backup files  
Duration of cloning | Relatively fast for large databases | Relatively slow for large databases  
Can clone from SQL Server instances external to Google Cloud | No | Yes  
Complexity | A complex sequence of commands for attaching cloned disks | A relatively straightforward set of commands for cloning  
Can leverage existing backup systems | Yes, if backup system uses Google Cloud disk snapshots | Yes, if backup system writes native SQL Server backup files to Cloud Storage  
Granularity of cloning | Can clone only entire disks | Can clone only the specified database  
Data consistency | Consistent at point of snapshot | Consistent at point of backup  
  
This tutorial assumes you're familiar with [Microsoft Windows](https://www.microsoft.com/windows) system administration, PowerShell, and Microsoft SQL Server administration using Microsoft [SQL Server Management Studio](https://docs.microsoft.com/sql/ssms/sql-server-management-studio-ssms).

## Objectives

  * Learn how to run a SQL Server instance on Google Cloud.
  * Learn how to create a demo database on a secondary disk.
  * Learn how to clone a SQL Server database using [Compute Engine disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).
  * Learn how to clone a SQL Server database by transferring a backup using Cloud Storage.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://docs.cloud.google.com/compute/pricing)
  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)
  * Microsoft Windows and SQL server licenses



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

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

  6. Enable the Compute Engine API.
[ Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com) 


Ensure that you're meeting these additional prerequisites:

  * You use the [Google Chrome](https://www.google.com/chrome/) browser.
  * Install a Remote Desktop Protocol (RDP) client of your choice. For more information, see [Microsoft Remote Desktop clients](https://docs.microsoft.com/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients). If you already have an RDP client installed, you can skip this task. 



## Setting up the environment

To complete this tutorial, you need to set up your computing environment with the following:

  * A SQL Server instance on Compute Engine (named `sql-server-prod`) to represent your production database server.
  * An additional disk (named `sql-server-prod-data`) that's attached to your production server for storing your production database.
  * A copy of the [Wide World Importers SQL Server sample database](https://github.com/Microsoft/sql-server-samples/releases/tag/wide-world-importers-v1.0) to simulate the production database that you want to clone.
  * A SQL Server instance on Compute Engine named `sql-server-test` to represent your testing database server. You clone your database onto this server.



The following diagram illustrates this architecture.

![Diagram that shows the setup for cloning a SQL Server database in this tutorial.](https://docs.cloud.google.com/static/architecture/images/cloning-a-microsoft-sql-server-database-on-compute-engine-architecture-1.svg)

### Create the production VM instance

To simulate a production environment, you set up a Compute Engine VM instance running SQL Server on Windows Server.

The VM instance for this tutorial uses two disks: a 50 GB disk for the OS and user accounts, and a 100 GB disk for database storage.

In Compute Engine, using separate disks offers no [performance](https://docs.cloud.google.com/compute/docs/disks#pdspecs) benefits. Disk performance is determined by the total storage capacity of all disks attached to an instance and the total number of vCPUs on your VM instance. Therefore, the database and log file can reside on the same disk.

**Note:** For simplicity in this tutorial, you give the VM instances' default service account full access to all Cloud APIs. In a production environment, it's best to grant access only to required Cloud APIs, or to use a specific service account with limited access.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click **Create**.

  3. In the **Name** field, type `sql-server-prod`.

  4. For **Region** , select **us-east1**.

**Note:** This tutorial uses the `us-east1` region and `us-east1-b` zone for its Google Cloud resources. If you choose a different region and zone, then replace references to `us-east1` and `us-east1-b` with your preferred region and zone.
  5. For **Zone** , select **us-east1-b**.

  6. Under **Machine configuration** , change **Machine type** to **n1-standard-2** (2 vCPU).

  7. Next to the **Boot disk** description, click **Change**.

  8. In the **Boot disk** panel, click the **Public images** tab.

  9. In the **Operating System** drop-down list, select **SQL Server on Windows Server**.

  10. In the **Version** drop-down list, select **SQL Server 2022 Standard on Windows Server 2022 Datacenter**.

  11. Ensure that the following values are set:

     * **Boot disk type** is set to **Standard persistent disk**.
     * **Size (GB)** is set to **50**.
  12. Click **Select**.

  13. Under **Identity and API access** , set **Access scopes** to **Allow full access to all Cloud APIs**.

  14. Expand **Management, security, disks, networking, sole tenancy**.

  15. Click the **Disks** tab.

  16. Click **Add new disk** _add_.

  17. In the **Name** field, type `sql-server-prod-data`.

  18. In the **Size (GB)** field, type `100`.

  19. Click **Done**.

  20. Click **Create**.




###  Cloud Shell 

  1. Open Cloud Shell.

[Open Cloud Shell](https://console.cloud.google.com/welcome?cloudshell=true)

  2. Initialize the following variables:
         
         VPC_NAME=VPC_NAME
         SUBNET_NAME=SUBNET_NAME
         

Where:

     * `VPC_NAME`: name of your VPC
     * `SUBNET_NAME`: name of your subnet
  3. Set your default [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects):
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of your Google Cloud project.

  4. Set your default region:
         
         gcloud config set compute/region REGION
         

Replace `REGION` with the ID of the region you want to deploy in.

  5. Set your default zone:
         
         gcloud config set compute/zone ZONE
         

Replace `ZONE` with the ID of the zone you want to deploy in.

  6. Create a Compute Engine instance by using the app image for SQL Server 2022 Standard on Windows Server 2022 Datacenter:
         
         REGION=$(gcloud config get-value compute/region)
         ZONE=$(gcloud config get-value compute/zone)
         
         gcloud compute instances create sql-server-prod \
             --machine-type=n1-standard-2 \
             --scopes=cloud-platform \
             --image-family=sql-std-2022-win-2022 \
             --image-project=windows-sql-cloud \
             --boot-disk-size=50GB \
             --boot-disk-device-name=sql-server-prod \
             --create-disk="mode=rw,size=100,type=pd-standard,name=sql-server-prod-data,device-name=sql-server-prod-data" \
             --subnet=$SUBNET_NAME 
         

This command grants the instance full access to Google Cloud APIs, creates a 100 GB secondary disk, and attaches the disk to the instance. Ignore the disk performance warning because you don't need high performance for this tutorial.




### Connect to the VM instance

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Wait about 5 minutes for the VM instance to be ready.

To monitor the initialization process of the VM, view its serial port output in Cloud Shell:
         
         gcloud compute instances tail-serial-port-output sql-server-prod
         

When you see the following message, the initialization is complete.
         
         Instance setup finished. sql-server-prod is ready to use.
         

Press `Control+C` to stop monitoring the serial port.

  3. Click the instance name `sql-server-prod` to open the **VM instance details** page.

  4. Under **Remote access** , click **Set Windows password** , and then click **Set** to create your account on the remote machine.

This step generates a password for you. Make a note of the password or copy it to a secure, temporary file.

  5. In the [Compute Engine section](https://console.cloud.google.com/compute/instances) of the Google Cloud console, click the **RDP** dropdown and select the **Download the RDP file** option to download the RDP file for your instance.

Use this file to connect to the instance using an RDP client. For more information, see [Microsoft Remote Desktop clients](https://docs.microsoft.com/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients).

  6. When you're prompted, enter the password you just generated, and then click **OK**.

  7. To accept the server certificate and log into your remote Windows instance, click **Continue**.

  8. When you're prompted whether you want your computer discoverable by other PCs and devices on the network, click **No**.




### Set up the additional disk

The second disk attached to the production instance is for storing your production database. This disk is blank, so you need to partition, format, and mount it.

  1. In an RDP session connected to your `sql-server-prod` instance, click the **Start** button on the Windows taskbar, type `diskpart`, and then click **diskpart** to open DiskPart.
  2. When you're prompted to let the app make changes, click **Yes**.
  3. Display a lists of disks attached to your instance:
         
         list disk
         

The output is the following:
         
         Disk ###  Status         Size     Free     Dyn  Gpt
         --------  -------------  -------  -------  ---  ---
         Disk 0    Online           50 GB      0 B
         Disk 1    Online          100 GB   100 GB
         

Disk 1 (100 GB) is your data disk.

  4. Select the data disk:
         
         select disk 1
         

  5. Initialize the disk:
         
         clean
         

  6. Create a [GUID partition table](https://en.wikipedia.org/wiki/GUID_Partition_Table):
         
         convert gpt
         

  7. Create the data partition by using the entire disk:
         
         create partition primary
         

  8. List the available volumes:
         
         list volume
         

The output is the following:
         
         Volume ###  Ltr  Label        Fs     Type        Size     Status     Info
         ----------  ---  -----------  -----  ----------  -------  ---------  --------
         Volume 0     C                NTFS   Partition     49 GB  Healthy    Boot
         Volume 1                      FAT32  Partition    100 MB  Healthy    System
         Volume 2                      RAW    Partition     99 GB  Healthy
         

Volume 2 (99 GB) is your data disk.

  9. Select the volume:
         
         select volume 2
         

  10. Format the partition with the [NTFS file system](https://wikipedia.org/wiki/NTFS) and label it `data`:
         
         format quick fs=ntfs label=data
         

  11. Mount the disk as drive D:
         
         assign letter=d
         

  12. Exit DiskPart:
         
         exit
         




### Download the sample database

To set up your environment for this cloning exercise, you need to do the following:

  * Create a directory structure on drive D (`data`) to store your database.
  * Download the [Wide World Importers SQL Server sample database](https://github.com/Microsoft/sql-server-samples/releases/tag/wide-world-importers-v1.0) full backup file. This database simulates the production database you want to clone.



To create the directory and download the backup file, follow these steps:

  1. In your RDP session, click the **Start** button on the Windows taskbar, type `PowerShell`, and then select the Windows PowerShell app.

  2. At the PowerShell prompt, create a directory structure for the database storage:
         
         mkdir D:\sql-server-data\wideworldimporters
         

  3. Download the backup file to drive D:
         
         bitsadmin /transfer sampledb /dynamic /download /priority FOREGROUND `
           https://github.com/Microsoft/sql-server-samples/releases/download/wide-world-importers-v1.0/WideWorldImporters-Full.bak `
           D:\sql-server-data\WideWorldImporters-Full.bak
         




### Restore the sample database

You need to restore the sample database to drive D (`data`), either interactively by using the Microsoft [SQL Server Management Studio (SSMS)](https://docs.microsoft.com/en-us/sql/ssms/sql-server-management-studio-ssms?view=sql-server-2017) wizards, or directly by running a Transact-SQL command.

###  SSMS Wizard 

  1. In your RDP session, click the **Start** button on the Windows taskbar, type `ssms`, and then select **Microsoft SQL Server Management Studio (Run as Administrator)**.
  2. After the app starts, click **Connect** to connect to the `sql-server-prod` database engine using Windows Authentication.
  3. In Object Explorer, right-click **Databases** , and then select **Restore Database**.
  4. Under **Source** , select **Device** , and then click the **[...]** button next to the device name.
  5. In the **Select backup devices** dialog, ensure that **File** is selected for **Backup media type** , and then click **Add**.
  6. In the file selector, browse to `D:\sql-server-data`, click the `WideWorldImporters-Full.bak` file, and then click **OK**.
  7. Click **OK** to close the **Select backup devices** dialog.

The **Restore Database** dialog is now populated with data about the Wide World Importers database backup.

  8. Under **Select a page** , click **Files**.

  9. Select the **Relocate all files to folder** checkbox.

  10. In both the **Data file folder** and **Log file folder** fields, enter `D:\sql-server-data\wideworldimporters`.

![Screenshot that shows the Restore Database dialog.](https://docs.cloud.google.com/static/architecture/images/cloning-a-microsoft-sql-server-database-on-compute-engine-restore-database.png)

  11. Click **OK** to start the restore operation.




After a couple of minutes you're notified that the database is restored.

###  Transact-SQL 

  1. In your RDP session, click the **Start** button on the Windows taskbar, type `ssms`, and then select **Microsoft SQL Server Management Studio (Run as Administrator)**.
  2. After the app starts, click **Connect** to connect to the `sql-server-prod` database engine using Windows Authentication.
  3. Select **File** > **New** > **Query with Current Connection** to open a new query window.
  4. Initiate a restore from the backup file you downloaded:
         
         USE [master]
         GO
         
         RESTORE DATABASE [WideWorldImporters]
           FROM  DISK = N'D:\SQL-SERVER-DATA\WideWorldImporters-Full.bak'
           WITH  FILE = 1,
           MOVE N'WWI_Primary' TO
             N'D:\SQL-SERVER-DATA\WideWorldImporters\WideWorldImporters.mdf',
           MOVE N'WWI_UserData' TO
             N'D:\SQL-SERVER-DATA\WideWorldImporters\WideWorldImporters_UserData.ndf',
           MOVE N'WWI_Log' TO
             N'D:\SQL-SERVER-DATA\WideWorldImporters\WideWorldImporters.ldf',
           MOVE N'WWI_InMemory_Data_1' TO
             N'D:\SQL-SERVER-DATA\WideWorldImporters\WideWorldImporters_InMemory_Data_1',
           NOUNLOAD,
           STATS = 5
         GO
         

This command restores the database and log file into the `D:\sql-server-data\wideworldimporters` directory.

  5. Right-click the query code and click **Execute**.

Allow a couple of minutes for the database restore to complete. You can click **Refresh** _refresh_ in Object Explorer to see whether the database is listed in the Databases tree. After the database restore is finished, you can close the query window without saving.




To verify the sample database is functional, you can run a query.

  1. In Microsoft SQL Server Management Studio, select **File** > **New** > **Query with Current Connection** to open a new query window, and then copy the following code:
         
         SELECT top(100)
           i.InvoiceDate, i.InvoiceID, i.CustomerID, c.CustomerName,
           i.ConfirmedDeliveryTime, i.ConfirmedReceivedBy
         FROM
           WideWorldImporters.Sales.Invoices i
           JOIN WideWorldImporters.Sales.Customers c
           ON i.CustomerID=c.CustomerID
         WHERE i.ConfirmedDeliveryTime IS NOT NULL
         ORDER BY i.InvoiceDate desc;
         

This query retrieves summary information from the 100 most recently delivered invoices.

  2. Right-click the query window and click **Execute**.

The **Results** pane displays the summary information.

![Screenshot that shows the Results pane from a query to the sample database.](https://docs.cloud.google.com/static/architecture/images/cloning-a-microsoft-sql-server-database-on-compute-engine-results-pane.png)




### Create the test VM instance

In this section you create a SQL Server instance named `sql-server-test` as the destination for the cloned database. The configuration of this instance is identical to the production instance. However, you don't create a second data disk; instead, you attach the data disk later in this tutorial.

###  Console 

  1. Go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click **Create**.

  3. In the **Name** field, type `sql-server-test`.

  4. For **Region** , select **us-east1**.

**Note:** This tutorial uses the `us-east1` region and `us-east1-b` zone for its Google Cloud resources. If you choose a different region and zone, then replace references to `us-east1` and `us-east1-b` with your preferred region and zone.
  5. For **Zone** , select **us-east1-b**.

  6. Under **Machine configuration** , change **Machine Type** to **n1-standard-2** (**2 vCPU**).

  7. Next to the **Book disk** image, click **Change**.

  8. In the **Boot disk** panel, click the **Public images** tab.

  9. In the **Operating System** drop-down list, select **SQL Server on Windows Server**.

  10. In the **Version** drop-down list, select **SQL Server 2022 Standard on Windows Server 2022 Datacenter**.

  11. Ensure that the following values are set:

     * **Boot disk type** is set to **Standard persistent disk**.
     * **Size (GB)** is set to **50**.
  12. Click **Select**.

  13. Under **Identity and API access** , set **Access scopes** to **Allow full access to all Cloud APIs**.

  14. Click **Create**.




###  Cloud Shell 

  1. Open Cloud Shell.

[Open Cloud Shell](https://console.cloud.google.com/welcome?cloudshell=true)

  2. Create the test SQL Server instance:
         
         gcloud compute instances create sql-server-test \
             --machine-type=n1-standard-2 \
             --scopes=cloud-platform \
             --image-family=sql-std-2022-win-2022 \
             --image-project=windows-sql-cloud \
             --boot-disk-size=50GB \
             --boot-disk-device-name=sql-server-test \
             --subnet=$SUBNET_NAME
         

You can ignore the disk performance warning because you don't need high performance for this tutorial.




### Connect to the VM instance

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Wait about 5 minutes for the VM instance to be ready.

To monitor the initialization process of the VM, view its serial port output in Cloud Shell:
         
         gcloud compute instances tail-serial-port-output sql-server-prod
         

When you see the following message, the initialization is complete.
         
         Instance setup finished. sql-server-test is ready to use.
         

Press `Control+C` to stop monitoring the serial port.

  3. Click the instance name `sql-server-test` to display the **VM instance details** page.

  4. Under **Remote access** , click **Set Windows password** , and then click **Set** to create your account on the remote machine.

This step generates a password for you. Make a note of the password or copy it to a secure, temporary file.

  5. In the [Compute Engine section](https://console.cloud.google.com/compute/instances) of the Google Cloud console, click the **RDP** dropdown and select the **Download the RDP file** option to download the RDP file for your instance.

Use this file to connect to the instance using an RDP client. For more information, see [Microsoft Remote Desktop clients](https://docs.microsoft.com/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients).

  6. When you're prompted, enter the password you just generated, and then click **OK**.

  7. To accept the server certificate and log into your remote Windows instance, click **Continue**.

  8. When you're prompted whether you want your PC discoverable, click **No**.




## Cloning the database using Compute Engine disk snapshots

One way to clone a SQL Server database running on Compute Engine is to store the database on a separate data disk and use persistent disk snapshots to create a clone of that disk.

[Persistent disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) let you get a point-in-time copy of on-disk data. Scheduling disk snapshots is one way to automatically back up your data.

In this section of the tutorial, you do the following:

  * Take a snapshot of the production server's data disk.
  * Create a new disk from the snapshot.
  * Mount the new disk onto the test server.
  * Attach the database on this disk to SQL Server on the test instance.



The following diagram shows how a database is cloned by using disk snapshots.

![Diagram that shows the setup for cloning a SQL Server database using disk snapshots.](https://docs.cloud.google.com/static/architecture/images/cloning-a-microsoft-sql-server-database-on-compute-engine-architecture-2.svg)

**Note:** For simplicity in this tutorial, you create the production and test VM instances in the same project. In a true production environment, it's likely these instances would be in separate projects. Disk snapshots can be shared between projects using the [Google Cloud CLI or API](https://docs.cloud.google.com/compute/docs/images/sharing-images-across-projects).

### Create the disk snapshot

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click the name of the `sql-server-prod` instance.

  3. On the **VM instance details** page, click the disk `sql-server-prod-data`.

  4. Click **Create Snapshot**.

  5. Name the snapshot `sql-server-prod-data-snapshot`.

  6. For **Location** , select **Regional**.

  7. Verify that the region is set to **`us-east1`** (the same as your VM instances).

**Note:** This tutorial uses the `us-east1` region and `us-east1-b` zone for its Google Cloud resources. If you choose a different region and zone, then replace references to `us-east1` and `us-east1-b` with your preferred region and zone.
  8. Select the **Enable VSS** option.

This option uses the [Volume Shadow Copy Service](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot#create-snapshot) in Microsoft Windows to make a consistent snapshot.

  9. Click **Create**.

After a few minutes, your snapshot is created.




###  Cloud Shell 

  1. Open Cloud Shell.

[Open Cloud Shell](https://console.cloud.google.com/welcome?cloudshell=true)

  2. Create a snapshot of your data disk in the same zone as the VM instance:
         
         gcloud compute disks snapshot sql-server-prod-data \
              --snapshot-names=sql-server-prod-data-snapshot \
              --guest-flush \
              --zone="${ZONE}"
         

The `--guest-flush` option uses the [Volume Shadow Copy Service](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot#create-snapshot) in Microsoft Windows to create a consistent snapshot. After a few minutes, your snapshot is created.




### Attach the disk snapshot to the test instance

You need to create a new data disk from the snapshot you created and then attach it to the `sql-server-test` instance.

###  Console 

In the following steps, you create a new persistent disk, use the snapshot of the production disk for its contents, and then attach the disk to the test instance.

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click the instance name `sql-server-test`.

  3. On the **VM instance details** page, click **Edit**.

  4. Click **Add new disk** _add_.

  5. Name the new disk `sql-server-test-data`.

  6. For **Source Type** , select **Snapshot**.

  7. For the `sql-server-prod-data-snapshot` instance you created, select the **Source snapshot**.

  8. Ensure that **Mode** is set to **Read/Write**.

  9. Click **Done**.




###  Cloud Shell 

  1. Open Cloud Shell.

[Open Cloud Shell](https://console.cloud.google.com/welcome?cloudshell=true)

  2. Create a new persistent disk by using the snapshot of the production disk for its contents:
         
         gcloud beta compute disks create sql-server-test-data \
              --size=100GB \
              --source-snapshot=sql-server-prod-data-snapshot \
              --zone="${ZONE}"
         

  3. Attach the new disk to your `sql-server-test` instance with read-write permissions:
         
         gcloud compute instances attach-disk sql-server-test \
             --disk=sql-server-test-data --mode=rw
         




### Mount the new data disk in Windows

The disk you created is attached to the VM instance but is offline, and the volume is set to read-only. To configure the volume as read-write and mountable, perform the following steps:

  1. In the RDP client window that's connected to your `sql-server-test` instance, click the **Start** button on the Windows taskbar, type `diskpart`, and then click **diskpart** to open DiskPart.
  2. When you're prompted to let the app make changes, click **Yes**.
  3. Display a list of the disks attached to your instance:
         
         list disk
         

The output is the following:
         
         Disk ###  Status         Size     Free     Dyn  Gpt
         --------  -------------  -------  -------  ---  ---
         Disk 0    Online           50 GB      0 B
         Disk 1    Offline         100 GB      0 B       *
          

Your data disk (Disk 1, 100 GB) is offline.

  4. Select the data disk:
         
         select disk 1
         

  5. Bring the disk online:
         
         online disk
         

  6. List the available volumes:
         
         list volume
         

The output is the following:
         
         Volume ###  Ltr  Label        Fs     Type        Size     Status     Info
         ----------  ---  -----------  -----  ----------  -------  ---------  --------
         Volume 0     C                NTFS   Partition     49 GB  Healthy    Boot
         Volume 1                      FAT32  Partition    100 MB  Healthy    System
         Volume 2                      RAW    Partition     99 GB  Healthy
         

Volume 2 (99 GB) is your data volume. It's listed as **Hidden** with no drive letter assigned.

  7. Select the volume:
         
         select volume 2
         

  8. Clear the attributes that were set when you created the volume from the snapshot:
         
         attr volume clear readonly hidden nodefaultdriveletter shadowcopy
         

This command makes the volume mountable.

  9. Mount the volume as drive D:
         
         assign letter=d
         

  10. Exit DiskPart:
         
         exit
         




### Reset file ownership and permissions

Because you created the data disk by taking a snapshot on the `sql-server-prod` instance, the user IDs for file ownership and permissions are different than those on the `sql-server-test` instance. You need to change the ownership of the files to a user on the `sql-server-test` instance and update the permissions to make the files readable for your local user and the `MSSQLSERVER` user.

  1. In the RDP client window connected to your `sql-server-test` instance, click the **Start** button on the Windows taskbar, and then type `cmd`.
  2. Open the Command Prompt app as an administrator.
  3. Set the owner of the files in the `sql-server-data` folder to the `MSSQLSERVER` service user:
         
         icacls d:\sql-server-data /setowner "nt service\mssqlserver" /t
         

  4. Reset all permissions on all files in the top-level `sql-server-data` folder:
         
         icacls d:\sql-server-data /reset /t
         

  5. Update the access control lists (ACLs) for the `sql-server-data` folder:
         
         icacls d:\sql-server-data /grant Administrators:(oi)(ci)f "nt service\mssqlserver":(oi)(ci)f "owner rights":(oi)(ci)f  %USERNAME%:(oi)(ci)f
         

  6. Disable the inheritance from the root folder of the drive, so that only the preceding permissions are applied:
         
         icacls d:\sql-server-data /inheritancelevel:r
         

  7. Exit the Command Prompt app:
         
         exit
         




The SQL Server instance and the local user on the `sql-server-test` instance can now access the database files.

### Attach the cloned database

You now attach the cloned database on drive D (`data`) to the test SQL Server instance. You can attach the database either interactively by using the Microsoft SQL Server Management Studio wizards, or directly by running a Transact-SQL command.

###  SSMS Wizard 

  1. In the RDP session connected to your `sql-server-test` instance, click the **Start** button on the Windows taskbar, type `ssms`, and then select **Microsoft SQL Server Management Studio (Run as Administrator)**.
  2. Click **Connect** to connect to the `sql-server-test` database engine using Windows Authentication.
  3. In Object Explorer, right-click **Databases** , and then select **Attach**.
  4. In the **Attach Databases** wizard, click **Add**.
  5. Browse to the directory `D:\sql-server-data\wideworldimporters`, click the `WideWorldImporters.mdf` file, and then click **OK**.
  6. Click **OK** to attach the database.

After a few moments, your cloned database is attached. You can click **Refresh** _refresh_ in Object Explorer to see whether the database is listed in the Databases tree.




###  Transact-SQL 

  1. In an RDP session connected to your `sql-server-test` instance, click the **Start** button on the Windows taskbar, type `ssms`, and then select **Microsoft SQL Server Management Studio (Run as Administrator)**.
  2. Click **Connect** to connect to the `sql-server-prod` database engine using Windows Authentication.
  3. Select **File** > **New** > **Query with Current Connection** to open a new query window.
  4. Attach the data and log files in the `D:\sql-server-data\wideworldimporters` directory:
         
         USE [master]
         GO
         
         CREATE DATABASE [WideWorldImporters] ON
         ( FILENAME = N'D:\sql-server-data\wideworldimporters\WideWorldImporters.mdf' ),
         ( FILENAME = N'D:\sql-server-data\wideworldimporters\WideWorldImporters.ldf' ),
         ( FILENAME = N'D:\sql-server-data\wideworldimporters\WideWorldImporters_UserData.ndf' )
          FOR ATTACH
         GO
         

  5. Right-click the query code and click **Execute**.

After a few moments, your cloned database is attached. You can click **Refresh** _refresh_ in Object Explorer to see whether your database is listed in the Databases tree. After the database is attached, you can close the query window without saving.




To verify that the sample database is functional, you can run a query.

  1. In SQL Server Management Studio, select **File** > **New** > **Query with Current Connection** to open a new query window, and then copy the following code:
         
         SELECT top(100)
           i.InvoiceDate, i.InvoiceID, i.CustomerID, c.CustomerName,
           i.ConfirmedDeliveryTime, i.ConfirmedReceivedBy
         FROM
           WideWorldImporters.Sales.Invoices i
           JOIN WideWorldImporters.Sales.Customers c
           ON i.CustomerID=c.CustomerID
         WHERE i.ConfirmedDeliveryTime IS NOT NULL
         ORDER BY i.InvoiceDate desc;
         

This query retrieves summary information from the 100 most recently delivered invoices.

  2. To run the query, right-click the query window, and then select **Execute**.

The **Results** pane displays the summary information.

![Screenshot that shows the Results pane from a query to the sample database.](https://docs.cloud.google.com/static/architecture/images/cloning-a-microsoft-sql-server-database-on-compute-engine-results-pane.png)




Now that you have seen how to clone a database using persistent disk snapshots, you might want to try cloning a database by using backup and restore. To complete the tutorial for this second approach, you must delete the database that you cloned from the `sql-server-test` instance.

### Delete the cloned database

To delete the cloned database you created by using disk snapshots, perform the following steps.

###  SSMS Wizard 

  1. In the RDP session connected to your `sql-server-test` instance, open Microsoft SQL Server Management Studio, and then connect to the `sql-server-test` database engine.
  2. In Object Explorer, expand **Databases** , right-click the `WorldWideImporters` database, and then select **Delete**.
  3. In the **Delete Object** wizard, ensure that the **Close existing connections** checkbox is selected.
  4. Click **OK**.



###  Transact-SQL 

  1. In the RDP session connected to your `sql-server-test` instance, open Microsoft SQL Server Management Studio, and then connect to the `sql-server-test` database engine.
  2. To close all connections to the `WideWorldImporters` database and delete it, copy the following script into a new query window, right-click the code, and then click **Execute** :
         
         USE [master]
         GO
         ALTER DATABASE [WideWorldImporters] SET SINGLE_USER WITH ROLLBACK IMMEDIATE
         GO
         DROP DATABASE [WideWorldImporters]
         GO
         

After the database is deleted, you can close the query window without saving. You can click **Refresh** _refresh_ in Object Explorer to confirm the database is deleted.




## Cloning using backup and restore

A second method of cloning a SQL Server database running on Compute Engine is to use native SQL Server backup and restore. With this approach, you transfer the backup by using Cloud Storage.

This section of the tutorial uses resources that you created in the Cloning the database using Compute Engine disk snapshots section of this tutorial. If you didn't complete that section, you must do so before continuing.

In this section of the tutorial, you do the following:

  * Create a Cloud Storage bucket.
  * Back up the database on the production server.
  * Copy the backup file from the production server to Cloud Storage.
  * Copy the backup file from Cloud Storage to the test server.
  * Restore the backup on the test instance.



The following diagram shows how a database is cloned by transferring a backup using Cloud Storage.

![Diagram that shows the setup for cloning a SQL Server database using Cloud Storage.](https://docs.cloud.google.com/static/architecture/images/cloning-a-microsoft-sql-server-database-on-compute-engine-architecture-3.svg)

Because systems outside of Google Cloud can be given access to Cloud Storage, you can use this approach to clone databases from external SQL Server instances.

**Note:** This setup requires that the production and test instances have enough free disk space to temporarily store the backup file.

### Create a Cloud Storage bucket

You need to create a Cloud Storage bucket that stores the backup files while you transfer them from the `sql-server-prod` instance to the `sql-server-test` instance.

###  Console 

  1. In the Google Cloud console, go to the Cloud Storage **Browser** page.

[Go to the Cloud Storage Browser page](https://console.cloud.google.com/storage/browser)

  2. Click **Create bucket**.

  3. Name the bucket `project-name`-bucket.

Replace the following:

     * `project-name`: The ID of your Google Cloud project.
  4. Expand **Choose a default storage class** , and then select **Regional**.

  5. For **Location** , select **us-east1**.

**Note:** This tutorial uses the `us-east1` region and `us-east1-b` zone for its Google Cloud resources. If you choose a different region and zone, then replace references to `us-east1` and `us-east1-b` with your preferred region and zone.
  6. Click **Create**.




###  Cloud Shell 

  1. Open Cloud Shell.

[Open Cloud Shell](https://console.cloud.google.com/welcome?cloudshell=true)

  2. Create a Cloud Storage bucket in the same region as your VM instances:
         
         gcloud storage buckets create "gs://$(gcloud config get-value project)-bucket" --location="${REGION}"
         




### Make a full point-in-time backup of the database

In your production environment, you might already make backups. You can use these backups as a base for cloning your database. In this tutorial, you make a [copy-only backup](https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/copy-only-backups-sql-server?view=sql-server-2017) so that it doesn't impact any existing full or incremental backup schedules.

**Note:** The article [Best practices for running SQL Server on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/sql-server/best-practices) recommends using a local SSD (instead of a persistent disk) to temporarily store backup files. Although this tutorial uses another approach, this best practice can help to minimize the CPU and I/O usage associated with writing to persistent disks.

###  SSMS Wizard 

  1. In the RDP session connected to your `sql-server-prod` instance, open Microsoft SQL Server Management Studio, and then connect to the `sql-server-prod` database engine.
  2. In Object Explorer, expand **Databases** , right-click the `WorldWideImporters` database, and then select **Tasks** > **Back Up**.
  3. In the **Back Up Database** wizard, ensure that the following values are set: 
     * **Backup type** is set to **Full**.
     * **Copy-only backup** is selected.
     * **Back up to** is set to **Disk**.
  4. To add a backup file, click **Add**.
  5. In the **Destination** field, enter `D:\sql-server-data\WideWorldImporters-copy.bak`.

![Screenshot that shows the Back Up Database dialog.](https://docs.cloud.google.com/static/architecture/images/cloning-a-microsoft-sql-server-database-on-compute-engine-back-up-database.png)

  6. Select the **Media Options** page, and then select **Overwrite all existing backup sets**.

  7. Select the **Backup Options** page, and then change **Set backup compression** to **Compress backup**.

  8. To create the backup, click **OK**.

The backup takes a few minutes to create.




###  Transact-SQL 

  1. In the RDP session connected to your `sql-server-prod` instance, open Microsoft SQL Server Management Studio, and then connect to the `sql-server-prod` database engine.
  2. To perform a copy-only compressed backup of the `WideWorldImporters`database``to the file `d:\sql-server-data\WideWorldImporters-copy.bak`, copy the following script into a new query window, right-click the code, and then click **Execute**.
         
         BACKUP DATABASE [WideWorldImporters]
            TO  DISK = N'd:\sql-server-data\WideWorldImporters-copy.bak'
            WITH  COPY_ONLY, NOFORMAT, INIT,
            NAME = N'WideWorldImporters-Full Database Backup',
            SKIP, NOREWIND, NOUNLOAD, COMPRESSION,  STATS = 10
         GO
         

Allow a few minutes for the server to create the backup. After the database backup is complete, you can close the query window without saving.




### Copy the backup file to Cloud Storage

  1. In the RDP session connected to your `sql-server-prod` instance, open a Windows PowerShell window.
  2. Copy the backup file into the Cloud Storage bucket you created earlier:
         
         gcloud storage cp d:\sql-server-data\WideWorldImporters-copy.bak "gs://$(gcloud config get-value project)-bucket/" --no-clobber
         

**Note:** The `--no-clobber` flag prevents the gcloud CLI from overwriting existing files with the same name.
  3. Exit PowerShell.
         
         exit
         




### Copy the backup file from Cloud Storage to sql-server-test

  1. In the RDP session connected to your `sql-server-test` instance, open a Windows PowerShell window.
  2. Copy the backup file into the Cloud Storage bucket you created earlier:
         
         gcloud storage cp "gs://$(gcloud config get-value project)-bucket/WideWorldImporters-copy.bak" d:\sql-server-data\
         

  3. Exit PowerShell.
         
         exit
         




Your test instance now has the full-copy backup of your database on its local disk.

### Restore the backup

You can now restore the full-copy backup onto drive D (`data`) of the `sql-server-test` instance.

###  SSMS Wizard 

  1. In the RDP session connected to your `sql-server-test` instance, open Microsoft SQL Server Management Studio, and then connect to the `sql-server-test` database engine.
  2. In Object Explorer, right-click **Databases** , and then select **Restore Database**.
  3. For **Source** , select the **Device** , and then click the **[...]** button next to the device name.
  4. In the **Select backup devices** dialog, select **File** in the **Backup media type** list, and then click **Add**.
  5. In the file selector, browse to `D:\sql-server-data`, click the `WideWorldImporters-copy.bak` file, and then click **OK**.
  6. Click **OK** to close the **Select backup devices** dialog.

The **Restore Database** dialog is now populated with data about the `WideWorldImporters` database backup.

  7. Under **Select a page** , click **Files**.

  8. Select **Relocate all files to folder**.

  9. In the **Data file folder** and **Log file folder** fields, enter `D:\sql-server-data\wideworldimporters`.

![Screenshot that shows the Restore Database dialog.](https://docs.cloud.google.com/static/architecture/images/cloning-a-microsoft-sql-server-database-on-compute-engine-restore-database.png)

  10. To start the restore operation, click **OK**.

When the process is complete, you see the message `Database 'WideWorldImporters' restored successfully`.




###  Transact-SQL 

  1. In the RDP session connected to your `sql-server-test` instance, open Microsoft SQL Server Management Studio, and then connect to the `sql-server-test` database engine.
  2. Select **File** > **New** > **Query with Current Connection** to open a new query window.
  3. Copy the following T-SQL command to initiate a restore from the backup file you copied from Cloud Storage, restoring the database and log file into the `D:\sql-server-data\wideworldimporters`directory:
         
         USE [master]
         GO
         
         RESTORE DATABASE [WideWorldImporters]
           FROM  DISK = N'D:\SQL-SERVER-DATA\WideWorldImporters-copy.bak'
           WITH  FILE = 1,
           MOVE N'WWI_Primary' TO
             N'D:\SQL-SERVER-DATA\WideWorldImporters\WideWorldImporters.mdf',
           MOVE N'WWI_UserData' TO
             N'D:\SQL-SERVER-DATA\WideWorldImporters\WideWorldImporters_UserData.ndf',
           MOVE N'WWI_Log' TO
             N'D:\SQL-SERVER-DATA\WideWorldImporters\WideWorldImporters.ldf',
           MOVE N'WWI_InMemory_Data_1' TO
             N'D:\SQL-SERVER-DATA\WideWorldImporters\WideWorldImporters_InMemory_Data_1',
           NOUNLOAD,
           STATS = 5
         GO
         

  4. Right-click the code and click **Execute**.

After a couple of minutes the database restore completes. You can click **Refresh** _refresh_ in Object Explorer to see whether the database is listed in the Databases tree. After the database restore is complete, you can close the query window without saving.




To demonstrate that the database is functional, you can run a query.

  1. In Microsoft SQL Management Studio, select **File** > **New** > **Query with Current Connection** to open a new query window, and then copy the following code:
         
         SELECT top(100)
           i.InvoiceDate, i.InvoiceID, i.CustomerID, c.CustomerName,
           i.ConfirmedDeliveryTime, i.ConfirmedReceivedBy
         FROM
           WideWorldImporters.Sales.Invoices i
           JOIN WideWorldImporters.Sales.Customers c
           ON i.CustomerID=c.CustomerID
         WHERE i.ConfirmedDeliveryTime IS NOT NULL
         ORDER BY i.InvoiceDate desc;
         

This query retrieves summary information from the 100 most recently delivered invoices.

  2. Right-click on the query window and click **Execute**.

The **Results** pane displays the summary information.

![Screenshot that shows the Results pane from a query to the sample database.](https://docs.cloud.google.com/static/architecture/images/cloning-a-microsoft-sql-server-database-on-compute-engine-results-pane.png)




## Using Cloud SQL as the cloning destination

If your destination database is hosted on Cloud SQL, and the origin database is on Compute Engine, then the only supported mechanism for cloning is by backing up the database to Cloud Storage, and then restoring the database into Cloud SQL.

For this tutorial, you reuse the backup that you created during the previous section.

### Create a Cloud SQL for SQL Server instance

  1. Open Cloud Shell.

[Open Cloud Shell](https://console.cloud.google.com/welcome?cloudshell=true)

  2. Create a Cloud SQL for SQL Server instance running the same database version as your `sql-server-prod` instance:
         
         gcloud sql instances create sqlserver-cloudsql  \
           --database-version=SQLSERVER_2022_STANDARD \
           --cpu=2 \
           --memory=5GB \
           --root-password=sqlserver12@ \
           --region=${REGION}
         

This creates an instance with root user of `sqlserver` with a password of `sqlserver12@`.




### Update object permissions

The correct permissions need to be set on both the Cloud Storage bucket and the backup object so that the Cloud SQL service account is able to read them. These permissions are set automatically when you use the Google Cloud console to import the object, or you can set them using `gcloud` commands.

  1. Open Cloud Shell.

[Open Cloud Shell](https://console.cloud.google.com/welcome?cloudshell=true)

  2. Set an environment variable containing the address of the service account of your Cloud SQL instance:
         
         CLOUDSQL_SA="$(gcloud sql instances describe sqlserver-cloudsql --format='get(serviceAccountEmailAddress)')"
         

  3. Add the service account to the bucket IAM policy as a reader and writer:
         
         gcloud storage buckets add-iam-policy-binding "gs://$(gcloud config get-value project)-bucket/" \
             --member=user:"${CLOUDSQL_SA}" --role=roles/storage.objectUser
         




### Import the exported database

  1. Open Cloud Shell.

[Open Cloud Shell](https://console.cloud.google.com/welcome?cloudshell=true)

  2. Import the exported file into your Cloud SQL instance:
         
         gcloud sql import bak sqlserver-cloudsql \
             "gs://$(gcloud config get-value project)-bucket/WideWorldImporters-copy.bak" \
             --database WideWorldImporters
         

When prompted, enter `y`.

  3. Install the SQL Server tools package:
         
         sudo apt install -y mssql-tools
         

If you accept the licence terms, enter `yes` when prompted.

You use these tools to connect to Cloud SQL from Cloud Shell so that you can run queries on the Cloud SQL instance.

  4. Connect the Cloud SQL proxy to your SQL Server instance:
         
         CONNECTION_NAME=$(gcloud sql instances describe sqlserver-cloudsql --format='value(connectionName)')
         cloud_sql_proxy -instances=${CONNECTION_NAME}=tcp:1433 &
         

  5. To verify that the cloned database is functional, run a query:
         
         /opt/mssql-tools/bin/sqlcmd -U sqlserver -S 127.0.0.1 -Q \
           'SELECT top(100)
             i.InvoiceDate, i.InvoiceID, i.CustomerID, LEFT(c.CustomerName,20) CustomerName,
             i.ConfirmedDeliveryTime, LEFT(i.ConfirmedReceivedBy,20) ConfirmedReceivedBy
           FROM
             WideWorldImporters.Sales.Invoices i
             JOIN WideWorldImporters.Sales.Customers c
             ON i.CustomerID=c.CustomerID
           WHERE i.ConfirmedDeliveryTime IS NOT NULL
           ORDER BY i.InvoiceDate desc;'
         

When prompted, enter the `sqlserver` user's password of the `sqlserver-cloudsql` database server (`sqlserver12@`).

This query retrieves summary information from the 100 most recently delivered invoices.

The output is the following:
         
         InvoiceDate      InvoiceID   CustomerID  CustomerName         ConfirmedDeliveryTime                  ConfirmedReceivedBy
         ---------------- ----------- ----------- -------------------- -------------------------------------- --------------------
               2016-05-30       70349         581 Wingtip Toys (Munich            2016-05-31 07:05:00.0000000 Youssef Eriksson
               2016-05-30       70350         123 Tailspin Toys (Roe P            2016-05-31 07:10:00.0000000 Ella Zvirbule
               2016-05-30       70351         175 Tailspin Toys (San A            2016-05-31 07:15:00.0000000 Julio Correa
               2016-05-30       70352        1029 Veronika Necesana               2016-05-31 07:20:00.0000000 Veronika Necesana
               2016-05-30       70353        1014 Narendra Tickoo                 2016-05-31 07:25:00.0000000 Narendra Tickoo
               2016-05-30       70354         930 Shantanu Huq                    2016-05-31 07:30:00.0000000 Shantanu Huq
               2016-05-30       70355         963 Be Trang                        2016-05-31 07:35:00.0000000 Be Trang
               2016-05-30       70356         567 Wingtip Toys (Jerome            2016-05-31 07:40:00.0000000 Severins Polis
               2016-05-30       70357         510 Wingtip Toys (Grabil            2016-05-31 07:45:00.0000000 Manish Ghosh
         ...
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, you can delete the Google Cloud project that you created for this tutorial.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Learn about the [best practices for running SQL Server instances on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/sql-server/best-practices).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
