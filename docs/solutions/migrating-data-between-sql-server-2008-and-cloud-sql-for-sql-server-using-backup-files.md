---
url: https://docs.cloud.google.com/solutions/migrating-data-between-sql-server-2008-and-cloud-sql-for-sql-server-using-backup-files/
title: Migrating data between SQL Server 2008 and Cloud SQL for SQL Server using backup files \u00a0|\u00a0 Solutions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:42:57.811128+00:00
---

# Migrating data between SQL Server 2008 and Cloud SQL for SQL Server using backup files  |  Solutions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/solutions/migrating-data-between-sql-server-2008-and-cloud-sql-for-sql-server-using-backup-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Solutions ](https://docs.cloud.google.com/solutions)



Send feedback 

#  Migrating data between SQL Server 2008 and Cloud SQL for SQL Server using backup files Stay organized with collections  Save and categorize content based on your preferences. 

In this tutorial, you migrate data from SQL Server 2008 to Cloud SQL for SQL Server 2017 Enterprise. The tutorial shows you how to export the data from SQL Server 2008, import the data to Cloud SQL for SQL Server 2017, and validate that the data was successfully imported. 

If you want to migrate data from SQL Server 2017, see [Migrating data between SQL Server 2017 and Cloud SQL for SQL Server using backup files](https://docs.cloud.google.com/solutions/migrating-data-between-sql-server-2017-and-cloud-sql-for-sql-server-using-backup-files).

This tutorial is useful if you are a sysadmin, developer, engineer, database admin, or DevOps engineer who wants to migrate data from SQL Server 2008 to Cloud SQL for SQL Server 2017 or who wants to upgrade from SQL Server 2008 to SQL Server 2017.

The tutorial assumes that you have a license for SQL Server 2008 and that you're familiar with the following:

  * Microsoft SQL Server 2008
  * Microsoft SQL Server 2017
  * Microsoft PowerShell
  * [Cloud Storage](https://docs.cloud.google.com/storage)
  * [Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver)



## Objectives

  * Create a Cloud SQL for SQL Server instance.
  * Create a Cloud Storage bucket.
  * Back up your database.
  * Import the database into Cloud SQL for SQL Server.
  * Validate the imported data.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud SQL](https://docs.cloud.google.com/sql/pricing)
  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Note:** If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[GO TO THE PROJECT SELECTOR PAGE](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Make sure that billing is enabled for your Google Cloud project. [Learn how to confirm billing is enabled for your project](https://docs.cloud.google.com/billing/docs/how-to/modify-project).

  3. Enable the Cloud Storage and Cloud SQL APIs.

[ENABLE THE APIS](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin,storage_component)

  4. [Install and initialize the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) on the server that's running SQL Server 2008.

  5. In the Google Cloud console, go to Cloud Shell.

[GO TO Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/features) session opens and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed, and with values already set for your current project. It can take a few seconds for the session to initialize.




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
         
         gcloud storage buckets create "gs://bucket-name" --location=US
         

Replace `bucket-name` with a unique name for the Cloud Storage bucket.




## Backing up your database

In this section, you connect to your Windows server running SQL Server 2008, create a backup of your database, and upload the backup database to Cloud Storage.

  1. Connect to your Windows server running SQL Server 2008 by using RDP. It can be the primary or a replica server.

  2. Launch the PowerShell command-line tool.

  3. In the terminal where you [installed the gcloud CLI](https://docs.cloud.google.com/sdk/docs), create a backup folder:
         
         mkdir c:\backup
         

  4. Create a backup of the database in the backup folder:
         
         osql -E -Q "BACKUP DATABASE db-name TO DISK='c:\backup\db-name.bak'"
         

Replace `db-name` with the name of the database that you want to migrate to Cloud SQL.

  5. Copy the backup file to the Cloud Storage bucket:
         
         $PROJECT_ID = (gcloud sql instances describe target --format='value(project)' )
         gcloud storage cp c:\backup\db-name.bak gs://bucket-name --no-clobber
         




## Importing the backup file to Cloud SQL

  1. In Cloud Shell, retrieve the service account that's associated with the Cloud SQL instance and save it in a variable:
         
         SVC_EMAIL_ADDRESS=$(gcloud sql instances describe target \
             --format='value(serviceAccountEmailAddress)')
         echo $SVC_EMAIL_ADDRESS
         

Google Cloud creates a service account when you created the Cloud SQL instance. You use the service account to give the Cloud SQL instance permission to access the resources it needs.

  2. Give the service account permission to write to the Cloud Storage bucket:
         
         gcloud storage buckets add-iam-policy-binding gs://bucket-name \
             --member=serviceAccount:${SVC_EMAIL_ADDRESS} \
             --role=roles/storage.legacyBucketWriter
         

  3. Give the service account permission to read files in the Cloud Storage bucket:
         
         gcloud storage buckets add-iam-policy-binding gs://bucket-name \
             --member=serviceAccount:${SVC_EMAIL_ADDRESS} \
             --role=roles/storage.legacyObjectReader
         

  4. Import the backup file to the Cloud SQL database:
         
         gcloud beta sql import bak target \
             gs://bucket-namedb-name.bak \
             --database db-name
         




## Validating the data import

In this section, you check that the data was successfully imported.

  1. In Cloud Shell, install the [SQL Server toolkit](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools?view=sql-server-ver15):
         
         sudo apt-get install -y mssql-tools
         

If you accept the license terms, enter `yes` when you're prompted.

  2. To securely access your Cloud SQL instance, download the [Cloud SQL proxy](https://cloud.google.com/sql/docs/mysql/sql-proxy):
         
         wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
         

  3. Start the Cloud SQL proxy:
         
         CONNECTION_NAME=$(gcloud sql instances describe target --format='value(connectionName)')
         ./cloud_sql_proxy -instances=${CONNECTION_NAME}=tcp:1433 &
         

  4. Run a query to validate the data in one or more of the tables:
         
         /opt/mssql-tools/bin/sqlcmd -U sqlserver -S 127.0.0.1 -Q "query-string"
         

Replace `query-string` with the SQL query that you want to run.

When you're prompted, enter the `sqlserver12@` password.




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
