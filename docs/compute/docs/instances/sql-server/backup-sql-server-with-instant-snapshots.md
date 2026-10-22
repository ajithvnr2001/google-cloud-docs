---
url: https://docs.cloud.google.com/compute/docs/instances/sql-server/backup-sql-server-with-instant-snapshots/
title: Backup SQL Server using instant snapshots \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:21:48.131024+00:00
---

# Backup SQL Server using instant snapshots  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/sql-server/backup-sql-server-with-instant-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Backup SQL Server using instant snapshots Stay organized with collections  Save and categorize content based on your preferences. 

If your SQL Server database files are spread across multiple disks, you can back up all the disks simultaneously, maintaining application and data consistency. You achieve this exact point-in-time backup with Compute Engine consistency groups of instant snapshots, which let you [back up data across a group of disks](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots#back_up_data_across_a_group_of_disks).

This tutorial describes how to back up SQL Server databases with Compute Engine snapshots and the Transact-SQL (T-SQL) snapshot feature that's available in SQL Server 2022 and later. This solution supports both Windows and Linux deployments and minimizes the performance impact on your live workloads.

## How it works

The workflow consists of these main steps, which are managed by a script running on a compute instance:

  1. **Freeze the database** : the script sends a T-SQL command to SQL Server to suspend all write operations for the target database(s). This ensures the database files are in a consistent state for the backup.
  2. **Take instant snapshots** : while the database is frozen, create a group of instant snapshots of the disks where the database's data and log files reside. This is the Google Cloud equivalent of using a hardware or service-level snapshot mechanism.
  3. **Record and thaw** : the script sends another T-SQL command to SQL Server to record the backup metadata. This command creates a small backup file that points to the consistency group of instant snapshots and is recorded in the `msdb` backup history. Upon completion, SQL Server automatically thaws the database and resumes normal operations.



This entire process is typically completed in under a second, minimizing the duration of the write freeze on your database. While the freeze is in place, data can be read but not written. You can manually cancel the freeze state by setting `SUSPEND_FOR_SNAPSHOT_BACKUP=OFF` for the database.

## Objectives

In this tutorial, you'll learn how to complete the following tasks: 

  * Create a SQL Server instance with two data disks.
  * Create new database with the data and log files on separate disks.
  * Create a consistency group of all the disks of the VM running SQL Server.
  * Create instant snapshots of the group of disks.
  * Create new disks from the instant snapshots.



## Costs

In this document, you use the following billable components of Google Cloud: 

To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. For this tutorial, you need a Google Cloud project. You can create a new one, or select an existing project:

     1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

        * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
        * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

     2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

     3. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Ensure that Microsoft SQL Server 2022 or later is installed and running.




### Required permissions

In addition to standard read access, ensure your SQL Server administrator grants you the `ALTER DATABASE` permission for the target database.

To get the permissions that you need to create instance and create snapshots, ask your administrator to grant you the following IAM roles on the project: 

  * Manage instance: `compute.instanceAdmin.v1`
  * Create snapshots: `compute.storageAdmin`



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Compute Engine SQL instance

Create a SQL Server instance.

  1. In the Google Cloud console, open [Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell) by clicking the **Activate Cloud Shell** ![Activate Cloud Shell.](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg) button.

[Go to the Google Cloud console](https://console.cloud.google.com/)

  2. Create a SQL Server instance. Paste the following command:



    
    
      REGION=REGION
      ZONE=$REGION-a
      VM_NAME=VM_NAME
      gcloud compute instances create $VM_NAME \
        --boot-disk-auto-delete \
        --boot-disk-size 100 \
        --boot-disk-type hyperdisk-balanced \
        --image-family sql-std-2022-win-2025 \
        --image-project windows-sql-cloud \
        --machine-type c4-highmem-4 \
        --zone $ZONE \
        --network-interface subnet=default \
        --tags sql-server-instant-snapshot \
        --scopes=cloud-platform,service-control,service-management,monitoring-write,logging-write,storage-rw \
        --create-disk=device-name=$VM_NAME-data-disk1,mode=rw,name=$VM_NAME-data-disk1,size=100,type=hyperdisk-balanced \
        --create-disk=device-name=$VM_NAME-data-disk2,mode=rw,name=$VM_NAME-data-disk2,size=100,type=hyperdisk-balanced
    

Replace the following:

  * **Region** : The region where your new instance will be deployed.
  * **VM_NAME** : The name of your new SQL Server instance.

**Note:** Variables persist only for the current terminal session and will need to be reset when session is disconnected.

## Create a consistency group of disks

  1. Create a consistency group.
         
         gcloud compute resource-policies create disk-consistency-group $VM_NAME-snap-grp \
             --region=$REGION
         

  2. Add the VM's disks to the consistency group.
         
         gcloud compute disks add-resource-policies $VM_NAME \
             --zone=$ZONE \
             --resource-policies=$VM_NAME-snap-grp
         
         gcloud compute disks add-resource-policies $VM_NAME-data-disk1 \
             --zone=$ZONE \
             --resource-policies=$VM_NAME-snap-grp
         
         gcloud compute disks add-resource-policies $VM_NAME-data-disk2 \
             --zone=$ZONE \
             --resource-policies=$VM_NAME-snap-grp
         




## Create a new database

  1. [Create a username and password](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances) for the VM instance.
  2. [Connect to the VM by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and sign in using the username and password created in the previous step.
  3. Right-click the **Start** button (or press **Win+X**) and click **Terminal (Admin)**.
  4. Confirm the elevation prompt by clicking **Yes**.
  5. Run the following PowerShell script in opened Terminal window. This script initializes the data disk, formats the disk with a 64 KB block size, and assigns a drive letter.
         
         $availableDisks = Get-PhysicalDisk -CanPool $True
         $diskLetters = [char[]] (68..72) | Where-Object { !(Get-PSDrive $_ -ErrorAction SilentlyContinue) }
         $diskCount = 0
         foreach ($disk in $availableDisks) {
             $diskLetter = $diskLetters[$diskCount]
             $diskLabel = "$diskLetter-DataDisk"
             Initialize-Disk -Number $disk.DeviceId -PartitionStyle MBR -PassThru
         
             New-Partition -DiskNumber $disk.DeviceId -UseMaximumSize `
             -DriveLetter $diskLetter | Format-Volume -FileSystem NTFS `
             -NewFileSystemLabel $diskLabel -AllocationUnitSize 65536 -Confirm:$false
         
             New-Item -ItemType Directory -Path "$($diskLetter):\MSSQL"
             $diskCount = $diskCount +1
         }
         

  6. Open the SQL Server Management Studio (SSMS). Run it as Administrator.

  7. In the Connect to server dialog, verify the server name is set to `localhost`, and select **Connect**.

  8. In the file menu, select **File > New > Query** with the current connection.

  9. Copy following code to the newly opened query window.
         
         USE Master;
         GO
         CREATE DATABASE SnapBackupDB
         ON PRIMARY
         (
             NAME = 'SnapBackupDB_Data',
             FILENAME = 'D:\MSSQL\SnapBackupDB.mdf',
             SIZE = 500MB,
             MAXSIZE = UNLIMITED,
             FILEGROWTH = 64MB
         )
         LOG ON
         (
             NAME = 'SnapBackupDB_Log',
             FILENAME = 'E:\MSSQL\SnapBackupDB_log.ldf',
             SIZE = 250MB,
             MAXSIZE = 2GB,
             FILEGROWTH = 64MB
         );
         




## Deploy snapshot script

This script automates the complete process required to take application-consistent snapshots of the disks attached to the VM running SQL Server.

  1. Using the same Remote Desktop session, open Notepad.
  2. Copy the contents of the following script and paste into the opened Notepad window.
  3. Save the file as `take-snapshot.ps1` in `c:\scripts`
         
         # Import Modules
         Import-Module -Name SQLPS
         
         # Set variables
         $formattedTimestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
         $backupLocation = 'D:\MSSQL\Backup'
         $dbName = 'SnapBackupDB'
         $bkmFile = Join-Path -Path $backupLocation  -ChildPath ("${dbName}_${formattedTimestamp}.bkm")
         $sqlServer = 'localhost'
         
         # SQL Commands
         $suspendDbCmd = "ALTER DATABASE [$dbName] SET SUSPEND_FOR_SNAPSHOT_BACKUP=ON WITH NO_WAIT;"
         $backupMetadataCmd = "BACKUP DATABASE [$dbName] TO DISK='$bkmFile' WITH METADATA_ONLY, FORMAT;"
         $unsuspendDbCmd = "ALTER DATABASE [$dbName] SET SUSPEND_FOR_SNAPSHOT_BACKUP=OFF;"
         
         # --- Helper Function for SQL Execution ---
         function Invoke-MySqlCommand {
             param(
                 [Parameter(Mandatory=$true)]
                 [string]$CommandText,
                 [Parameter(Mandatory=$true)]
                 [System.Data.SqlClient.SqlConnection]$SqlConnection
             )
             Write-Host "Executing SQL Command: $($CommandText)"
             try {
                 $Command = New-Object System.Data.SqlClient.SqlCommand($CommandText, $SqlConnection)
                 $Result = $Command.ExecuteNonQuery()
                 return $true
             }
             catch {
                 Write-Host "Error executing SQL Command: $($CommandText)`n$($_.Exception.Message)" -ForegroundColor Red
                 return $false
             }
         }
         
         $sqlConn = New-Object System.Data.SqlClient.SqlConnection
         $sqlConn.ConnectionString = "server='$sqlServer';database='$dbName';Integrated Security=True;"
         $databaseSuspended = $false
         
         if (-not(Test-Path $backupLocation)) {
             New-Item -Path $backupLocation -ItemType directory -Force
         }
         
         try {
             $instanceName = (Invoke-RestMethod -Headers @{"Metadata-Flavor"="Google"} -Uri "http://metadata.google.internal/computeMetadata/v1/instance/name")
             $vmConfigString = (gcloud compute instances list --filter="name=('$instanceName')" --format=json --quiet)
             if ($LASTEXITCODE -ne 0) {
                 Write-Host "Error querying gcloud for VM instances (exit code: $LASTEXITCODE). Exiting." -ForegroundColor Red
                 exit 1
             }
             $vmConfig = $vmConfigString | ConvertFrom-Json
         
             # Open SQL Server connection
             $sqlConn.Open()
         
             # Suspend Database
             Write-Host "Suspending database '$dbName' for snapshot..."
             if (-not (Invoke-MySqlCommand -CommandText $suspendDbCmd -SqlConnection $sqlConn)) {
                 Write-Host "Failed to suspend database. Exiting." -ForegroundColor Red
                 exit 1
             }
             $databaseSuspended = $true
         
             # Take a disk snapshot
             try {
                 $consistencyGroupListStr = (gcloud compute resource-policies list --filter='name:*-snap-grp' --format=json --quiet)
                 if ($LASTEXITCODE -ne 0) { throw "gcloud resource-policies list failed (exit code: $LASTEXITCODE)." }
                 $consistencyGroupList = $consistencyGroupListStr | ConvertFrom-Json
         
                 if (@($consistencyGroupList).Count -eq 0) { throw "No consistency group found matching '*-snap-grp'." }
                 if (@($consistencyGroupList).Count -gt 1) { Write-Warning "More than one consistency group found, using the first one." }
         
                 $consistencyGroupSelfLink = $consistencyGroupList[0].selfLink
                 $zoneName = Split-Path $vmConfig[0].zone -Leaf
                 $snapshotName = "$($vmConfig.Name)-${formattedTimestamp}"
         
                 $snapshotCmd = "gcloud compute instant-snapshot-groups create $snapshotName --source-consistency-group=$consistencyGroupSelfLink --zone=$zoneName --quiet"
                 Invoke-Expression $snapshotCmd
                 if ($LASTEXITCODE -ne 0) { throw "gcloud compute instant-snapshot-groups create failed (exit code: $LASTEXITCODE)." }
                 Write-Host "Instant snapshot group created successfully."
             }
             catch {
                 Write-Host "Error during snapshot creation: $($_.Exception.Message)" -ForegroundColor Red
                 exit 1 # Exit after handling in finally
             }
         
             # Backup database metadata
             if (-not (Invoke-MySqlCommand -CommandText $backupMetadataCmd -SqlConnection $sqlConn)) {
                 Write-Host "Failed to backup database metadata." -ForegroundColor Red
                 exit 1
             }
         
             # Unsuspend Database
             Write-Host "Unsuspending database '$dbName'..."
             if (-not (Invoke-MySqlCommand -CommandText $unsuspendDbCmd -SqlConnection $sqlConn)) {
                 Write-Host "Failed to unsuspend database after successful snapshot and metadata backup. Manual intervention may be required." -ForegroundColor Red
                 exit 1
             }
             $databaseSuspended = $false # Successfully unsuspended
         
         }
         catch {
             Write-Host "An unhandled error occurred: $($_.Exception.Message)" -ForegroundColor Red
             exit 1
         }
         finally {
             if ($databaseSuspended -and ($sqlConn.State -eq [System.Data.ConnectionState]::Open)) {
                 if (-not (Invoke-MySqlCommand -CommandText $unsuspendDbCmd -SqlConnection $sqlConn)) {
                     Write-Host "Failed to unsuspend database in finally block. Manual intervention may be required." -ForegroundColor Red
                 }
             }
         
             # Ensure SQL connection is closed
             if ($sqlConn.State -eq [System.Data.ConnectionState]::Open) {
                 $sqlConn.Close()
             }
         }
         
         

  4. Right-click the **Start** button (or press **Win+X**) and click **Terminal (Admin)**.

  5. Confirm the elevation prompt by clicking **Yes**.

  6. Execute the script by running following command.
         
         C:\scripts\take-snapshot.ps1
         




## Verify the instant snapshots were created

Run the following commands in the Cloud Shell

  1. Verify the script created the snapshots.
         
         gcloud compute instant-snapshots list --filter="name:$VM_NAME*"
         

  2. List the instant snapshot groups.
         
         gcloud compute instant-snapshot-groups list --zones $ZONE
         

  3. View details of the instant snapshot group.
         
         gcloud compute instant-snapshot-groups describe  \
             INSTANT_SNAPSHOT_NAME --zone=$ZONE
         

  4. Copy the `selfLink` value to use in the next section.




## Restore the instant snapshots to new disks

Run the following commands in the Google Cloud console window.

  1. Create disks from the consistency group of instant snapshots.
         
         gcloud compute disks bulk create --source-instant-snapshot-group \
             INSTANT_SNAPSHOT_NAME_URL \
             --source-instant-snapshot-group-region $REGION --zone=$ZONE
         

  2. Confirm your snapshots were restored by listing the disks in the zone.
         
         gcloud compute disks list --zones=$ZONE --filter="name:$VM_NAME-*"
         

  3. Create a new VM from the newly created disks.
         
         REGION=REGION
         ZONE=$REGION-a
         VM_NAME=VM_NAME
         gcloud compute instances create $VM_NAME \
             --machine-type c4-highmem-4 \
             --zone $ZONE \
             --network-interface subnet=default \
             --tags sql-server-instant-snapshot \
             --disk=name=BOOT_DISK_NAME,boot=yes,auto-delete=no \
             --disk=name=DATA_DISK_1_NAME,mode=rw,auto-delete=no \
             --disk=name=DATA_DISK_2_NAME,mode=rw,auto-delete=no
         




Replace the following:

  * **Region** : The region where your new instance will be deployed.
  * **VM_NAME** : The name of your new SQL instance.
  * **BOOT_DISK_NAME** : The name of the boot disk created in the previous step.
  * **DATA_DISK_1_NAME** : The name of the first data disk created in previous step.
  * **DATA_DISK_2_NAME** : The name of the second data disk created in previous step.



You can now [attach](https://docs.cloud.google.com/compute/docs/disks/attach-disks) the disks to a new or existing VM. 

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, delete the project.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
