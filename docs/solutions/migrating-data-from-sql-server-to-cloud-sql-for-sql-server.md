---
url: https://docs.cloud.google.com/solutions/migrating-data-from-sql-server-to-cloud-sql-for-sql-server/
title: Migrating data from SQL Server 2017 to Cloud SQL for SQL Server using snapshot replication \u00a0|\u00a0 Solutions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:42:57.667260+00:00
---

# Migrating data from SQL Server 2017 to Cloud SQL for SQL Server using snapshot replication  |  Solutions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/solutions/migrating-data-from-sql-server-to-cloud-sql-for-sql-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Solutions ](https://docs.cloud.google.com/solutions)



Send feedback 

#  Migrating data from SQL Server 2017 to Cloud SQL for SQL Server using snapshot replication Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to migrate data from Microsoft SQL Server 2017 Enterprise running on Compute Engine to Cloud SQL for SQL Server 2017 Enterprise. This tutorial is useful if you are a sysadmin, developer, engineer, database admin, or DevOps engineer. The tutorial shows you how to set up [SQL Server Distributor](https://docs.microsoft.com/en-us/sql/relational-databases/replication/distributor?view=sql-server-ver15), use the [SQL Server Agent](https://docs.microsoft.com/en-us/sql/ssms/agent/sql-server-agent?view=sql-server-ver15) for snapshot replication into Cloud SQL for SQL Server 2017, and validate that the data was successfully imported.

In this tutorial, you use [snapshot replication](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-replication-tutorial-tsql?view=sqlallproducts-allversions#detailed-steps) to keep the source and target in sync. Snapshot replication sends subscribers a full copy of each article—that is, published database object. Cloud SQL also supports transactional replication, which sends only incremental data. A limitation of transactional replication is that tables must have primary keys. For more information about SQL Server replication types, see the [SQL Server documentation](https://docs.microsoft.com/en-us/sql/relational-databases/replication/types-of-replication?view=sql-server-ver15).

For simplicity, the tutorial uses the source SQL Server to host a Distributor. In a production scenario, if data is being replicated from outside Google Cloud, you might prefer to host distribution on the Google Cloud side on a Compute Engine instance.

**Note:** Cloud SQL for SQL Server doesn't support log shipping, database mirroring, or [these features](https://docs.cloud.google.com/sql/docs/features#sqlserver-unavailable). Microsoft SQL Server [doesn't support](https://docs.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2017?view=sql-server-ver15) replication from Developer, Web, or Express editions.

The tutorial assumes that you're familiar with the following:

  * SQL Server
  * Microsoft PowerShell
  * [Compute Engine](https://docs.cloud.google.com/compute)
  * [Cloud SQL for SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver)



## Objectives

  * Create a SQL Server virtual machine (VM) instance on Compute Engine to host the sample database.
  * Populate a sample database.
  * Create a Cloud SQL for SQL Server instance.
  * Create a Distributor.
  * Set up publication and subscription.
  * Initiate replication from SQL Server to Cloud SQL.
  * Validate the imported data.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://docs.cloud.google.com/compute/all-pricing)
  * [Cloud SQL](https://docs.cloud.google.com/sql/pricing)
  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)
  * [SQL Server](https://docs.cloud.google.com/compute/all-pricing#sql_server_pricing) (premium with Compute Engine)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud SQL Admin and Compute Engine API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute,sqladmin&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud SQL Admin and Compute Engine API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute,sqladmin&redirect=https%3A//console.cloud.google.com)

  8. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  9. Install any Remote Desktop Protocol (RDP) client of your choice. For more information, see [Microsoft Remote Desktop clients](https://docs.microsoft.com/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients). If you already have an RDP client installed, you can skip this task. 



When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Creating a SQL Server VM

The first step is to create a SQL Server 2017 instance on a Windows 2016 VM on Compute Engine and connect to it by using RDP.

  1. In Cloud Shell, create a SQL Server 2017 Standard instance on Windows Server 2016. The source database must be a SQL Server Standard or Enterprise database because lower tiers don't have the database publisher capability.
         
         gcloud compute instances create sqlserver --machine-type=n1-standard-4 \
             --boot-disk-size=100GB \
             --image-project=windows-sql-cloud \
             --image-family=sql-std-2017-win-2016 \
             --zone=us-central1-f  \
             --scopes=https://www.googleapis.com/auth/cloud-platform
         

For this tutorial, you create the instance in the `us-central1-f` zone with a boot disk size of 100 GB. For more information, see [Cloud locations](https://docs.cloud.google.com/about/locations).

  2. Generate a Windows password:
         
         gcloud compute reset-windows-password sqlserver --zone=us-central1-f
         

  3. In the Google Cloud console, go to the **VM instances** page.

[Go to VM Instances ](https://console.cloud.google.com/compute/instances)

  4. In the [Compute Engine section](https://console.cloud.google.com/compute/instances) of the Google Cloud console, click the **RDP** dropdown and select the **Download the RDP file** option to download the RDP file for your instance.

Use this file to connect to the instance using an RDP client. For more information, see [Microsoft Remote Desktop clients](https://docs.microsoft.com/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients).

  5. In the **username** and **password** fields, enter the username and password that you created for the SQL Server VM instance. Leave the **Domain** field blank, and then click **OK** to connect to the SQL Server VM.

![Screenshot of the dialog where you enter the username and password.](https://docs.cloud.google.com/static/solutions/images/migrating-data-from-sql-server-to-cloud-sql-username-password.png)

When prompted, accept the certificate.

  6. If you accept the terms, click **Continue**.

  7. In the instance, minimize all windows, click **Start** on the Windows taskbar, type `PowerShell`, and then right-click the Windows PowerShell app and select **Run as administrator**.

  8. At the PowerShell prompt, create a directory structure for the database storage:
         
         mkdir c:\sql-server-data\adventureworks
         




## Creating and populating a sample database

You now download Microsoft [AdventureWorks database](https://github.com/microsoft/sql-server-samples/tree/master/samples/databases/adventure-works) backup file and restore it into your SQL Server instance. This database simulates the production database that you want to migrate.

  1. From the PowerShell command line, download the `AdventureWorksLT2017.bak` backup file to drive C:
         
         bitsadmin /transfer sampledb /dynamic /download /priority FOREGROUND "https://github.com/Microsoft/sql-server-samples/releases/download/adventureworks/AdventureWorksLT2017.bak " C:\sql-server-data\AdventureWorksLT2017.bak
         

  2. Restore the database:
         
         osql -E -Q "USE [master]
         RESTORE DATABASE [AdventureWorksLT2017]
         FROM  DISK = N'C:\sql-server-data\AdventureWorksLT2017.bak' WITH  FILE = 1,
         MOVE N'AdventureWorksLT2012_Data' TO N'C:\sql-server-data\adventureworks\AdventureWorksLT2012.mdf',
         MOVE N'AdventureWorksLT2012_Log' TO N'C:\sql-server-data\adventureworks\AdventureWorksLT2012_log.ldf',
         NOUNLOAD,  STATS = 5"
         

  3. Validate the newly restored database by querying the number of rows in the `Customer` table. The output is 847 rows.
         
         osql -E -Q "select count(*) from AdventureWorksLT2017.SalesLT.Customer"
         




## Preparing the Cloud SQL instance

  1. In Cloud Shell, create the Cloud SQL for SQL Server 2017 Enterprise instance:
         
         gcloud sql instances create target-sqlserver  \
             --database-version=SQLSERVER_2017_STANDARD \
             --cpu=4 \
             --memory=15 \
             --storage-size=100 \
             --root-password=sqlserver12@ \
             --zone=us-central1-f
         

The root user is `sqlserver` with a password of `sqlserver12@`. Also make note of the SQL Server IP address.

  2. Store the IP address of the source SQL Server VM in an environment variable:
         
         sql_source_ip=$(gcloud compute instances describe sqlserver \
             --zone=us-central1-f | grep natIP | awk '{print $2}')
         echo $sql_source_ip
         

  3. Add the SQL Server VM IP address with the Cloud SQL instance to the allowlist (whitelist):
         
         gcloud sql instances patch target-sqlserver --authorized-networks=$sql_source_ip
         

  4. Create a destination database:
         
         gcloud sql databases create AdventureWorksTarget --instance=target-sqlserver
         

  5. In the PowerShell command line that you launched as an administrator, check connectivity to Cloud SQL for SQL Server:
         
         $cloud_sql_server_ip=gcloud sql instances describe target-sqlserver --format='value(ipAddresses.ipAddress)'
         osql -S $cloud_sql_server_ip -U sqlserver -P sqlserver12@ -Q "select 'test'"
         

The command prints `'test'`.




## Initiating replication from the VM to Cloud SQL

Using SQL Server snapshot replication, you create a job to replicate database snapshots into Cloud SQL.

### Set up the Distributor

You now configure the SQL Server VM to be a SQL Server Distributor. In practice, a Distributor can run on a separate machine, but in this tutorial, you run it on the same VM.

  1. From the PowerShell command line that you launched as administrator, update the SQL Server local instance name to match the VM host name:
         
         $servername=hostname
         osql -E -Q "sp_dropserver 'INST-INSTALL-SQ';"
         osql -E -Q "sp_addserver '$servername', local;"
         Restart-Service -F MSSQLServer
         mkdir c:\sql-server-data\repldata
         

If you receive the error `Cannot open MSSQLServer service on computer '.'.`, you likely didn't run the PowerShell command line as an administrator.

  2. Verify that the instance name is now `"sqlserver"`:
         
         osql -E -Q "select @@servername;"
         

  3. Specify the distribution database:
         
         $servername=hostname
         osql -E -Q "use master; exec sp_adddistributor @distributor = N'$servername', @password = N'';"
         osql -E -Q "exec sp_adddistributiondb @database = N'distribution', @data_folder = N'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\Data', @log_folder = N'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\Data', @log_file_size = 2, @min_distretention = 0, @max_distretention = 72, @history_retention = 48, @deletebatchsize_xact = 5000, @deletebatchsize_cmd = 2000, @security_mode = 1"
         

  4. Configure the distribution database:
         
         osql -E -Q "
         use [distribution]
         if (not exists (select * from sysobjects where name = 'UIProperties' and type = 'U '))
             create table UIProperties(id int)
         if (exists (select * from ::fn_listextendedproperty('SnapshotFolder', 'user', 'dbo', 'table', 'UIProperties', null, null)))
             exec sp_updateextendedproperty N'SnapshotFolder', N'c:\sql-server-data\repldata', 'user', dbo, 'table', 'UIProperties'
         else
             exec sp_addextendedproperty N'SnapshotFolder', N'c:\sql-server-data\repldata', 'user', dbo, 'table', 'UIProperties'
         "
         

  5. Register the SQL Server VM name with the Distributor as a publisher:
         
         osql -E -Q "exec sp_adddistpublisher @publisher = N'$servername',
         @distribution_db = N'distribution', @security_mode = 1, @working_directory
         = N'c:\sql-server-data\repldata', @trusted = N'false', @thirdparty_flag =
         0, @publisher_type = N'MSSQLSERVER'"
         




### Set up publishing

Now that distribution is set up, you configure which tables are published.

  1. From the PowerShell command line, enable and start the SQL Server Agent:
         
         Set-Service -Name SQLServerAgent -StartupType Automatic
         Start-Service -Name SQLServerAgent
         

  2. Create a publication for the `AdventureWorksLT2017` database:
         
         $servername=hostname
         osql -E -Q "
         use [AdventureWorksLT2017]
         exec sp_replicationdboption @dbname = N'AdventureWorksLT2017', @optname = N'publish', @value = N'true'"
         
         osql -E -Q "use [AdventureWorksLT2017]
         exec sp_addpublication @publication = N'advn-pub3', @description = N'Snapshot publication of database ''AdventureWorksLT2017'' from Publisher ''$servername''.', @sync_method = N'native', @retention = 0, @allow_push = N'true', @allow_pull = N'true', @allow_anonymous = N'true', @enabled_for_internet = N'false', @snapshot_in_defaultfolder = N'true', @compress_snapshot = N'false', @ftp_port = 21, @ftp_login = N'anonymous', @allow_subscription_copy = N'false', @add_to_active_directory = N'false', @repl_freq = N'snapshot', @status = N'active', @independent_agent = N'true', @immediate_sync = N'true', @allow_sync_tran = N'false', @autogen_sync_procs = N'false', @allow_queued_tran = N'false', @allow_dts = N'false', @replicate_ddl = 1"
         

  3. Configure the publication to send a snapshot of the source to Cloud SQL once every hour:
         
         osql -E -Q "
         use [AdventureWorksLT2017]
         exec sp_addpublication_snapshot @publication = N'advn-pub3', @frequency_type = 4, @frequency_interval = 1, @frequency_relative_interval = 1, @frequency_recurrence_factor = 0, @frequency_subday = 8, @frequency_subday_interval = 1, @active_start_time_of_day = 0, @active_end_time_of_day = 235959, @active_start_date = 0, @active_end_date = 0, @job_login = null, @job_password = null, @publisher_security_mode = 1"
         

  4. Add articles (tables) to publication. Although the `AdventureWorksLT2017` database contains many tables, for the sake of simplicity in this tutorial, you replicate three tables: `Address`, `Customer`, and `CustomerAddress`.
         
         osql -E -Q "
         use [AdventureWorksLT2017]
         exec sp_addarticle @publication = N'advn-pub3', @article = N'Address', @source_owner = N'SalesLT', @source_object = N'Address', @type = N'logbased', @description = null, @creation_script = null, @pre_creation_cmd = N'drop', @schema_option = 0x000000000803509D, @identityrangemanagementoption = N'manual', @destination_table = N'Address', @destination_owner = N'SalesLT', @vertical_partition = N'false'
         "
         
         osql -E -Q "
         use [AdventureWorksLT2017]
         exec sp_addarticle @publication = N'advn-pub3', @article = N'Customer', @source_owner = N'SalesLT', @source_object = N'Customer', @type = N'logbased', @description = null, @creation_script = null, @pre_creation_cmd = N'drop', @schema_option = 0x000000000803509D, @identityrangemanagementoption = N'manual', @destination_table = N'Customer', @destination_owner = N'SalesLT', @vertical_partition = N'false'
         "
         
         osql -E -Q "
         use [AdventureWorksLT2017]
         exec sp_addarticle @publication = N'advn-pub3', @article = N'CustomerAddress', @source_owner = N'SalesLT', @source_object = N'CustomerAddress', @type = N'logbased', @description = null, @creation_script = null, @pre_creation_cmd = N'drop', @schema_option = 0x000000000803509D, @identityrangemanagementoption = N'manual', @destination_table = N'CustomerAddress', @destination_owner = N'SalesLT', @vertical_partition = N'false'
         "
         

  5. Manually create a snapshot of the articles. If you don't do so, it can take up to an hour before the scheduler creates the initial snapshot.
         
         osql -E -Q "use [AdventureWorksLT2017]
         exec sp_startpublication_snapshot @publication = N'advn-pub3'"
         




### Set up a subscription

You now create a subscription that sends the published data to Cloud SQL.

  1. From the PowerShell command line, create a subscription to send the publication snapshot to Cloud SQL:
         
         $cloud_sql_server_ip=gcloud sql instances describe target-sqlserver --format='value(ipAddresses.ipAddress)'
         $cloud_sql_user="sqlserver"
         $cloud_sql_password="sqlserver12@"
         $target_db_name="AdventureWorksTarget"
         osql -E -Q " use [AdventureWorksLT2017] exec sp_addsubscription @publication = N'advn-pub3', @subscriber = N'$cloud_sql_server_ip', @destination_db = N'$target_db_name', @subscription_type = N'Push', @sync_type = N'automatic', @article = N'all', @update_mode = N'read only', @subscriber_type = 0
         
         exec sp_addpushsubscription_agent @publication = N'advn-pub3', @subscriber = N'$cloud_sql_server_ip', @subscriber_db = N'$target_db_name', @job_login = null, @job_password = null, @subscriber_security_mode = 0, @subscriber_login = N'$cloud_sql_user', @subscriber_password = N'$cloud_sql_password', @frequency_type = 64, @frequency_interval = 0, @frequency_relative_interval = 0, @frequency_recurrence_factor = 0, @frequency_subday = 0, @frequency_subday_interval = 0, @active_start_time_of_day = 0, @active_end_time_of_day = 235959, @active_start_date = 20200408, @active_end_date = 99991231, @enabled_for_syncmgr = N'False', @dts_package_location = N'Distributor' "
         



  1. Validate that the data is available in the Cloud SQL instance:
         
         osql -S $cloud_sql_server_ip -U $cloud_sql_user -P $cloud_sql_password -Q "select count(*) from [AdventureWorksTarget].[SalesLT].[CustomerAddress] UNION
         select count(*) from [AdventureWorksTarget].[SalesLT].[Customer]
         UNION
         Select count(*) from [AdventureWorksTarget].[SalesLT].[Address]"
         

The command prints `417`, `450`, `847`




## Clean up

After you finish the tutorial, you can clean up the resources that you created so that they stop using quota and incurring charges. The following sections describe how to delete or turn off these resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Learn how to [migrate data from SQL Server 2017 to Cloud SQL for SQL Server using backup files](https://docs.cloud.google.com/solutions/migrating-data-between-sql-server-2017-and-cloud-sql-for-sql-server-using-backup-files).
  * Learn how to [migrate data from SQL Server 2008 to Cloud SQL for SQL Server using backup files.](https://docs.cloud.google.com/solutions/migrating-data-between-sql-server-2008-and-cloud-sql-for-sql-server-using-backup-files)
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
