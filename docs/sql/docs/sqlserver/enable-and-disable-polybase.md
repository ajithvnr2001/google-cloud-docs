---
url: https://docs.cloud.google.com/sql/docs/sqlserver/enable-and-disable-polybase/
title: Enable and disable PolyBase \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:00.421923+00:00
---

# Enable and disable PolyBase  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/enable-and-disable-polybase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Enable and disable PolyBase Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page shows you how to enable and disable PolyBase for your Cloud SQL for SQL Server instances.

For overview information about PolyBase, see [Cloud SQL for SQL Server support for PolyBase](https://docs.cloud.google.com/sql/docs/sqlserver/about-polybase).

For information about how to set up configuration, see [Configure external data sources for use with PolyBase](https://docs.cloud.google.com/sql/docs/sqlserver/configure-external-data-sources).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Cloud SQL, Cloud SQL Admin, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=sql-component.googleapis.com,sqladmin.googleapis.com,compute.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Cloud SQL, Cloud SQL Admin, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=sql-component.googleapis.com,sqladmin.googleapis.com,compute.googleapis.com)

  10. Configure your network to allow traffic between Cloud SQL for SQL Server and your external data source. 
     * If SQL Server can't establish a successful connection, then the T-SQL command to set up or query the external data source fails.
     * Whether using a public or private IP address, make sure your Cloud SQL instance, and any supporting Google Cloud resources, have access to your external data source within the firewall of the data source.

If you are using the public IP address of the Cloud SQL instance, then you also need to obtain access to the underlying [Compute Engine](https://docs.cloud.google.com/compute/docs/overview) VM and must obtain its IP address. Since this underlying VM is not externalized to users, you must contact [Google Cloud Support](https://docs.cloud.google.com/sql/docs/sqlserver/getting-support) to retrieve its IP address. This IP address might change if the instance is recreated.

  11. To enable or disable PolyBase, you need the following permissions: 
     * `cloudsql.instances.get`
     * `cloudsql.instances.update`
Either of the following roles provide the previous permissions: 
     * `roles/cloudsql.editor`
     * `roles/cloudsql.admin`

We recommend using the [principle of least privilege](https://docs.cloud.google.com/sql/docs/sqlserver/roles-and-permissions#best_practices) when granting access.

Alternatively, you can also assign these permissions to a [custom role](https://docs.cloud.google.com/sql/docs/sqlserver/iam-roles#custom-roles).

  12. Review your instance's existing warehouse database names.

When PolyBase is enabled, three new PolyBase data warehouse databases are created:

     * DWConfiguration
     * DWQueue
     * DWDiagnostics

If you enable PolyBase on an instance that already contains user databases with these restricted DW names, then SQL Server deletes and recreates them.

Before enablement, use a tool like [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/ssms/install/install) to verify whether any databases with these names already exist. If so, contact [Google Cloud support](https://docs.cloud.google.com/sql/docs/sqlserver/getting-support) for help before you continue.

Certain restrictions apply to these system databases:

     * You can't use the Google Cloud console, Cloud SQL Admin API, and gcloud CLI to perform certain operations on DW databases: 
       * Create
       * Delete
       * List
       * Import
You can, however, use the export command to take a backup of these databases.
     * You can't access DW databases using SQL Server Management Studio (SSMS).
     * If the instance is replicated, DW databases are not copied to the new resource.
     * If the instance is restored using [PITR](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/configure-pitr), DW databases are not copied to the new resource.
     * DW databases are retained even after PolyBase is disabled.

For more information, see the following resources:

     * [Install PolyBase on Linux](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-linux-setup?view=sql-server-ver16&tabs=rhel)
     * [PolyBase feature summary](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-versioned-feature-summary?view=sql-server-ver16#known-limitations)



## PolyBase enablement using database flags

You can enable PolyBase with your Cloud SQL for SQL Server instance using [database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags). The required flags vary based on the type of external data source you want to use:

  * The [`polybase`](https://docs.cloud.google.com/sdk/gcloud/reference/sql) database flag is required for all external data sources.
  * If using Cloud Storage, you also need to apply the Microsoft SQL Server trace flag, [`13702`](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-traceon-trace-flags-transact-sql?view=sql-server-ver17#tf13702). Enabling this flag also enables other trace flags required for PolyBase support.



The following sections show you how to enable PolyBase on new and existing instances.

### Create a new instance with PolyBase enabled

To create a new instance with PolyBase enabled, run the following [`gcloud`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create#--database-flags) command:

###  Oracle 
    
    
    gcloud sql instances create INSTANCE_NAME \
      --database-version=VERSION --region=LOCATION \
      --root-password=PASSWORD --edition=EDITION \
      --cpu=NUMBER_OF_CPUs --memory=MEMORY_SIZE \
      --database-flags="DATABASE_FLAG"
    

Replace the following:

  * INSTANCE_NAME: the name of the Cloud SQL instance.
  * VERSION: the database version you want to use.
  * LOCATION: the location of the Cloud SQL instance.
  * PASSWORD: the password of the Cloud SQL instance.
  * EDITION: the database edition you want to use.
  * NUMBER_OF_CPUs: the number of CPUs you want to use.
  * MEMORY_SIZE: the amount of memory you want to use.
  * DATABASE_FLAG: the database flag value required to enable PolyBase, regardless of the type of external data source.

You must enter, `cloud sql enable polybase=on`.

For more information, see [Database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags).




###  Cloud Storage 
    
    
    gcloud sql instances create INSTANCE_NAME \
      --database-version=VERSION --region=LOCATION \
      --root-password=PASSWORD --edition=EDITION \
      --cpu=NUMBER_OF_CPUs --memory=MEMORY_SIZE \
      --database-flags="DATABASE_FLAG_CLOUD_STORAGE"
    

Replace the following:

  * INSTANCE_NAME: the name of the Cloud SQL instance.
  * VERSION: the database version you want to use.
  * LOCATION: the location of the Cloud SQL instance.
  * PASSWORD: the password of the Cloud SQL instance.
  * EDITION: the database edition you want to use.
  * NUMBER_OF_CPUs: the number of CPUs you want to use.
  * MEMORY_SIZE: the amount of memory you want to use.
  * DATABASE_FLAG_CLOUD_STORAGE: the database flag values required to enable PolyBase. If your external data source is Cloud Storage, then you must enter, `cloud sql enable polybase=on,13702=on`.

For more information, see [Database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags).




### Enable PolyBase on an existing instance

To enable PolyBase on an existing instance, run the following [`gcloud`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--database-flags) command:

###  Oracle 
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --database-flags="DATABASE_FLAG"
    

Replace the following:

  * INSTANCE_NAME: the name of the Cloud SQL instance.
  * DATABASE_FLAG: the database flag value required to enable PolyBase, regardless of the type of external data source.



You must enter, `cloud sql enable polybase=on`.

This example is for illustrative purposes only. Running a `patch` operation with a specific database flag setting replaces any existing database flags. Make sure to include any existing database flags you want to keep. If you omit a previously set database flag, then the omitted flag is reverted to its default value.

For more information, see [Database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags).

###  Cloud Storage 
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --database-flags="DATABASE_FLAG_CLOUD_STORAGE"
    

Replace the following:

  * INSTANCE_NAME: the name of the Cloud SQL instance.
  * DATABASE_FLAG_CLOUD_STORAGE: the database flag value required to enable PolyBase, regardless of the type of external data source.



You must enter, `cloud sql enable polybase=on,13702=on`.

This example is for illustrative purposes only. Running a `patch` operation with a specific database flag setting replaces any existing database flags. Make sure to include any existing database flags you want to keep. If you omit a previously set database flag, then the omitted flag is reverted to its default value.

For more information, see [Database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags).

## Check instance configuration

To check whether PolyBase is enabled on an existing instance, run the following [`gcloud`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create#--database-flags) command:

###  gcloud 
    
    
    gcloud sql instances describe INSTANCE_NAME \
      --format="value(settings.databaseFlags)"
    

Replace the following:

  * INSTANCE_NAME: the name of the Cloud SQL instance.



## Disable PolyBase

To disable PolyBase on an instance, run the following [`gcloud`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create#--database-flags) command:

###  gcloud 
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --database-flags="cloud sql enable polybase=off"
    

Replace the following:

  * INSTANCE_NAME: the name of the Cloud SQL instance.



When PolyBase is disabled, the following PolyBase resources aren't deleted:

  * DW system databases
  * Database master key (DMK)
  * Data sources
  * Data scoped credentials
  * External tables



These resources are kept in the event you want to re-enable the feature in the future.

## What's next

  * [Cloud SQL for SQL Server support for PolyBase](https://docs.cloud.google.com/sql/docs/sqlserver/about-polybase)
  * [Configure external data sources for use with PolyBase](https://docs.cloud.google.com/sql/docs/sqlserver/configure-external-data-sources)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
