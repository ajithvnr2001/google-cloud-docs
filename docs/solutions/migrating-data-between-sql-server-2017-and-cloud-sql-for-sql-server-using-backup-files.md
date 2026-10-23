---
url: https://docs.cloud.google.com/solutions/migrating-data-between-sql-server-2017-and-cloud-sql-for-sql-server-using-backup-files/
title: Migrating data between SQL Server 2017 and Cloud SQL for SQL Server using backup files \u00a0|\u00a0 Solutions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:42:57.991167+00:00
---

# Migrating data between SQL Server 2017 and Cloud SQL for SQL Server using backup files  |  Solutions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/solutions/migrating-data-between-sql-server-2017-and-cloud-sql-for-sql-server-using-backup-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Solutions ](https://docs.cloud.google.com/solutions)



Send feedback 

#  Migrating data between SQL Server 2017 and Cloud SQL for SQL Server using backup files Stay organized with collections  Save and categorize content based on your preferences. 

In this tutorial, you migrate data from SQL Server 2017 Enterprise running on Compute Engine to Cloud SQL for SQL Server 2017 Enterprise. The tutorial shows you how to export the data from SQL Server 2017, import the data to Cloud SQL for SQL Server 2017, and validate that the data was successfully imported.

If you want to migrate data from SQL Server 2008, see [Migrating data between SQL Server 2008 and Cloud SQL for SQL Server using backup files](https://docs.cloud.google.com/solutions/migrating-data-between-sql-server-2008-and-cloud-sql-for-sql-server-using-backup-files).

This tutorial is useful if you are a sysadmin, developer, engineer, database admin, or DevOps engineer who wants to migrate data from SQL Server 2017 to Cloud SQL for SQL Server.

The tutorial assumes that you're familiar with the following:

  * Microsoft SQL Server
  * Microsoft PowerShell
  * [Compute Engine](https://docs.cloud.google.com/compute)
  * [Cloud Storage](https://docs.cloud.google.com/storage)
  * [Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver)



## Objectives

  * Create a SQL Server virtual machine (VM) instance on Compute Engine to host the sample database.
  * Create a Cloud SQL for SQL Server instance.
  * Create a Cloud Storage bucket.
  * Back up the sample database.
  * Import the database into Cloud SQL for SQL Server.
  * Validate the imported data.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://docs.cloud.google.com/compute/all-pricing)
  * [Cloud SQL](https://docs.cloud.google.com/sql/pricing)
  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)
  * [SQL Server](https://docs.cloud.google.com/compute/all-pricing#sql_server_pricing) (premium with Compute Engine)



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

  4. Enable the Cloud Storage, Cloud SQL Admin, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute,sqladmin,storage_component)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Storage, Cloud SQL Admin, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute,sqladmin,storage_component)

  8. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 




## Creating a script for a sample database

In this section, you create a script to populate a pre-loaded sample database. Then you create a SQL Server 2017 instance on Compute Engine that uses this database.

  1. In Cloud Shell, create a PowerShell script to deploy as a startup script:
         
         cat << 'EOF' > startup.ps1
         [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
         $dataseturl = "https://opendata.maryland.gov/api/views/ryxx-aeaf/rows.csv?accessType=DOWNLOAD"
         Invoke-WebRequest -Uri $dataseturl -OutFile c:\dataset.csv
         Invoke-Sqlcmd -Query "CREATE DATABASE testdb;"
         Invoke-Sqlcmd -Query "CREATE TABLE testdb.dbo.MarylandZipCodes ( zipcode int NOT NULL PRIMARY KEY,  city varchar(255), county varchar(255))"
         Invoke-Sqlcmd -Query "BULK INSERT testdb.dbo.MarylandZipCodes FROM 'c:\dataset.csv' WITH (DATAFILETYPE='char',FIELDTERMINATOR=',' ,ROWTERMINATOR = '0x0a',  FIRSTROW=2);"
         EOF
         

This startup script creates a local database named `testdb` with a table called `MarylandZipCodes`. Then the script downloads the [Maryland public zip code registry](https://opendata.maryland.gov/) and imports the registry into the table.

  2. Create a SQL Server 2017 Enterprise instance for Windows Server 2016:
         
         gcloud compute instances create sql-server --machine-type n1-highmem-4 \
             --boot-disk-size 50GB \
           --image-project windows-sql-cloud --image-family sql-ent-2017-win-2016 \
           --zone us-central1-f  \
           --scopes=https://www.googleapis.com/auth/cloud-platform \
           --metadata-from-file windows-startup-script-ps1=startup.ps1
         

For this tutorial, you create the instance in the `us-central1-f` zone with a boot disk size of 50 GB. For more information about zones, see [Cloud locations](https://docs.cloud.google.com/about/locations). The `--metadata-from-file` flag sets the PowerShell script to be the startup script for the instance.




## Creating the Cloud SQL instance and Cloud Storage bucket

  1. In Cloud Shell, create the Cloud SQL for SQL Server 2017 Enterprise instance that you later migrate the database to:
         
         gcloud beta sql instances create target  \
             --database-version=SQLSERVER_2017_ENTERPRISE \
             --cpu=2 \
             --memory=5GB \
             --root-password=sqlserver12@ \
             --zone=us-central1-f
         

It can take a few minutes to create the instance. The default root username is `sqlserver` with a default password of `sqlserver12@`. For this tutorial, you create the instance in the `us-central1-f` zone. For more information about zones, see [Cloud locations](https://docs.cloud.google.com/about/locations).

  2. Create a Cloud Storage bucket to store the backup file before the data is imported into Cloud SQL:
         
         gcloud storage buckets create "gs://${DEVSHELL_PROJECT_ID}-sql-backups" --location=US
         




## Backing up the sample database

In this section, you connect to the SQL Server virtual machine (VM), create a backup of the database, and upload the backup database to Cloud Storage.

  1. In Cloud Shell, reset the password for the SQL Server VM instance:
         
         gcloud compute reset-windows-password sql-server --zone=us-central1-f
         

Make a note of the new password for the user.

  2. Install a Remote Desktop Protocol (RDP) client. For more information, see [Microsoft Remote Desktop clients](https://docs.microsoft.com/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients).

  3. In the Google Cloud console, go to the **VM instances** page.

[GO TO THE VM INSTANCES PAGE](https://console.cloud.google.com/compute/instances)

  4. In the [Compute Engine section](https://console.cloud.google.com/compute/instances) of the Google Cloud console, click the **RDP** dropdown and select the **Download the RDP file** option to download the RDP file for your SQL Server VM instance.

Use this file to connect to the instance using an RDP client. For more information, see [Microsoft Remote Desktop clients](https://docs.microsoft.com/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients).

  5. In the browser, minimize all windows, and then launch the PowerShell command-line tool.

  6. Create a backup folder:
         
         mkdir c:\backup
         

  7. In the browser, create a backup of the database in the backup folder:
         
         osql -E -Q "BACKUP DATABASE testdb TO DISK='c:\backup\testdb.bak'"
         

  8. In the shell in the instance, copy the backup file to the Cloud Storage bucket:
         
         $PROJECT_ID=(gcloud config get-value core/project)
         
         gcloud storage cp c:\backup\testdb.bak gs://$PROJECT_ID-sql-backups --no-clobber
         




## Importing the backup file into Cloud SQL

  1. In Cloud Shell, retrieve the service account that's associated with the Cloud SQL instance and save it in a variable:
         
         SVC_EMAIL_ADDRESS=$(gcloud sql instances describe target \
             --format='value(serviceAccountEmailAddress)')
         echo $SVC_EMAIL_ADDRESS
         

Google Cloud creates a service account when you created the Cloud SQL instance. You use the service account to give the Cloud SQL instance permission to access the resources it needs.

  2. Give the service account permission to write to the Cloud Storage bucket:
         
         gcloud storage buckets add-iam-policy-binding gs://${DEVSHELL_PROJECT_ID}-sql-backups \
             --member=serviceAccount:${SVC_EMAIL_ADDRESS} \
             --role=roles/storage.legacyBucketWriter
         

  3. Give the service account permission to read files in the Cloud Storage bucket:
         
         gcloud storage buckets add-iam-policy-binding gs://${DEVSHELL_PROJECT_ID}-sql-backups/testdb.bak \
             --member=serviceAccount:${SVC_EMAIL_ADDRESS} \
             --role=roles/storage.legacyObjectReader
         

  4. Import the backup file to the Cloud SQL database:
         
         gcloud beta sql import bak target \
             gs://${DEVSHELL_PROJECT_ID}-sql-backups/testdb.bak --database testdb
         




## Validating the data import

In this section, you check that the sample data was successfully imported.

  1. In Cloud Shell, install the [SQL Server toolkit](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools?view=sql-server-ver15):
         
         sudo apt-get install -y mssql-tools
         

If you accept the license terms, enter `yes` when you're prompted.

  2. To securely access your Cloud SQL instance, download the [Cloud SQL proxy](https://cloud.google.com/sql/docs/mysql/sql-proxy):
         
         wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
         

  3. Start the Cloud SQL proxy:
         
         CONNECTION_NAME=$(gcloud sql instances describe target --format='value(connectionName)')
         ./cloud_sql_proxy -instances=${CONNECTION_NAME}=tcp:1433 &
         

  4. Read the number of rows in the Cloud SQL table:
         
         /opt/mssql-tools/bin/sqlcmd -U sqlserver -S 127.0.0.1 -Q "select count(*)
         from testdb.dbo.MarylandZipCodes"
         

When you're prompted, enter the `sqlserver12@` password. In the output, make sure that the result is `619`.




## Clean up

The easiest way to eliminate billing is to delete the Google Cloud project you created for the tutorial. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Read about [customer-managed encryption keys (CMEK) for Cloud SQL for SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/configure-cmek).
  * Read about [configuring private IP connectivity for Cloud SQL for SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
