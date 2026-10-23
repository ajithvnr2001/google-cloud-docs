---
url: https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/migrate-cloud-sql-to-alloydb/
title: Migrate from Cloud SQL for PostgreSQL to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:30.279423+00:00
---

# Migrate from Cloud SQL for PostgreSQL to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/migrate-cloud-sql-to-alloydb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)



Send feedback 

#  Migrate from Cloud SQL for PostgreSQL to AlloyDB for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

Standard Free trial

To evaluate AlloyDB for PostgreSQL or migrate an existing workload without setting up continuous replication, you can copy a Cloud SQL for PostgreSQL backup directly into an AlloyDB cluster.

This page assumes familiarity with Cloud SQL. If you're new to AlloyDB, see the [AlloyDB overview](https://docs.cloud.google.com/alloydb/docs/overview). 

To learn how to migrate your data from Cloud SQL to AlloyDB using [continuous data replication](https://docs.cloud.google.com/database-migration/docs/overview#continuous-migration), see [Database Migration Service for PostgreSQL to AlloyDB](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest). 

The following aren't supported:

  * Cross-project and cross-region restores
  * Instances with Customer Managed Encryption Keys (CMEK)
  * Instances with Identity and Access Management (IAM) group authentication



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

  6. Enable the AlloyDB, Compute Engine, and Service Networking APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=alloydb.googleapis.com,compute.googleapis.com,servicenetworking.googleapis.com)

  7. Make sure that you have the following: 
     * The necessary [Identity and Access Management (IAM) permissions](https://docs.cloud.google.com/alloydb/docs/migrate-cloud-sql-to-alloydb#required-roles)
     * A Cloud SQL backup with a size that's less than 15TB
     * [A version of PostgreSQL supported by AlloyDB](https://docs.cloud.google.com/alloydb/docs/db-version-policies)



### Required roles

To get the permissions that you need to copy a Cloud SQL for PostgreSQL backup into an AlloyDB cluster, grant yourself the following IAM roles on your project:

  * [Cloud SQL Viewer](https://docs.cloud.google.com/sql/docs/postgres/iam-roles) (`roles/cloudsql.viewer`) or any custom role that includes the `cloudsql.backupRuns.export` permission.
  * [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)



## Copy a Cloud SQL backup into an AlloyDB cluster

Copying a Cloud SQL backup into an AlloyDB standard cluster restores the backup to the same version of PostgreSQL on AlloyDB, for example, a PostgreSQL 14 Cloud SQL backup restores to a PostgreSQL 14 standard cluster. Keep in mind that extension versions and PostgreSQL minor versions might be different.

Copying a backup from Cloud SQL only supports the configuration of those items supported in the AlloyDB standard cluster.

**Note:** You can't copy a backup if it's greater than 15TB.

To copy a Cloud SQL backup into an AlloyDB standard cluster, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Clusters** page.  


[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click **Migrate data** and then select **Copy from Cloud SQL Backup**.
  3. In the **Copy from Cloud SQL backup** page, enable the required APIs. If you already enabled the APIs, you don't need to re-enable the APIs.
  4. On the **Select the cluster type** page, select **Provisioned cluster**.
  5. Click **Select Cluster Type**.
  6. Select the Cloud SQL instance that you want to copy a backup from and then click **Select instance**. You can filter Cloud SQL instances.  
Only compatible database versions are displayed. Replicas don't have backups and aren't displayed in the list of available instances.
  7. Select the backup you want to import from and then click **Select backup**. This page displays the most recent 1,000 backups.
  8. In the **Create your provisioned cluster** page, enter your networking information. The cluster ID is populated by default, but you can also customize your provisioned cluster.
  9. Click **Create Cluster**.



After the operation completes, a primary instance is automatically created. You see a new AlloyDB cluster with the data that is copied from the Cloud SQL for PostgreSQL backup that you selected.

When you copy a Cloud SQL for PostgreSQL backup into an AlloyDB cluster, database flags are migrated if the database flags are in Cloud SQL for PostgreSQL and in AlloyDB. Resource level permissions aren't automatically migrated. After the copy is complete, you must manually set up permissions and those database flags that weren't migrated due to a mismatch.

You can check which database flags in Cloud SQL for PostgreSQL are supported in AlloyDB in the **Create your provisioned cluster** page.

### gcloud

To use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install) the gcloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

  1. Run the `[gcloud alloydb clusters migrate-cloud-sql](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/migrate-cloud-sql)` command:  

         
         gcloud alloydb clusters migrate-cloud-sql CLUSTER_ID \
                 --cloud-sql-backup-id=CLOUD_SQL_BACKUP_ID \
                 --cloud-sql-instance-id=CLOUD_SQL_INSTANCE_ID \
                 --cloud-sql-project-id=CLOUD_SQL_PROJECT_ID \
                 --password=PASSWORD \
                 --region=REGION \
                 --database-version=DATABASE_VERSION \
                 --subscription-type=STANDARD
               

Replace the following:

     * `CLUSTER_ID`: Cloud SQL for PostgreSQL cluster ID.
     * `CLOUD_SQL_BACKUP_ID`: Cloud SQL backup ID to migrate from. This must be the backup ID.
     * `CLOUD_SQL_INSTANCE_ID`: Cloud SQL instance ID to migrate from. This must be the instance ID.
     * `CLOUD_SQL_PROJECT_ID`: Cloud SQL project ID to migrate from. This must be the project ID.
     * `PASSWORD`: Initial PostgreSQL user password to set up during cluster creation.
     * `REGION`: Location, for example, `asia-east1` or `us-east1`. See the full list of regions at [Locations](https://docs.cloud.google.com/alloydb/docs/locations).
     * `DATABASE_VERSION`: Database version of the cluster. This must be one of: `POSTGRES_14`, `POSTGRES_15`, `POSTGRES_16`, `POSTGRES_17`, or `POSTGRES_18`. The database version must be the same as the version of the Cloud SQL backup.
  2. Run the `gcloud alloydb operations describe` command to confirm the status of the backup operation:  

         
         gcloud alloydb operations describe OPERATION_ID \
                 --region=REGION_ID \
                 --project=PROJECT_ID
               

Replace the following:

     * `OPERATION_ID`: the name of the Cloud SQL for PostgreSQL operation.
     * `REGION_ID`: the region in which the Cloud SQL for PostgreSQL cluster is deployed.
     * `PROJECT_ID`: the project ID.
  3. Use the `[gcloud alloydb instances create](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/create)` command to [create a primary instance](https://docs.cloud.google.com/alloydb/docs/instance-primary-create#gcloud).



### REST API

  1. To get a list of backups for the instance from which you want to restore your backup, call the [`backupRuns.list`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/backupRuns/list) method:  

         
         GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/backupRuns
               

Replace the following:

     * `PROJECT_ID`: the project ID.
     * `INSTANCE_ID`: the instance ID.

To send your request, use one of these options:

#### **curl (Linux, macOS, or Cloud Shell)**

The following command assumes that you signed into the `[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)` with your user account by running `[gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init)` or `[gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login)`, or by using `[Cloud Shell](https://docs.cloud.google.com/shell/docs)`, which automatically signs you into the `gcloud CLI`.

You can check the active account by running `[gcloud auth list](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list)`.

Execute the following command:
    
    curl -X GET \
                   -H "Authorization: Bearer $(gcloud auth print-access-token)" \
                   -H "Content-Type: application/json; charset=utf-8" \
                   "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/backupRuns"
            

#### **PowerShell (Windows)**

The following command assumes that you signed into the `gcloud CLI` with your user account by running `**[gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init)**` or `**[gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login)**`, or by using `[Cloud Shell](https://docs.cloud.google.com/shell/docs)`, which automatically signs you into the `gcloud CLI`.

You can check the active account by running `**[gcloud auth list](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list)**`.

Execute the following command:
    
    $cred = gcloud auth print-access-token
             $headers = @{ "Authorization" = "Bearer $cred" }
             Invoke-WebRequest \
              -Method GET \
              -Headers $headers \
              -ContentType: "application/json; charset=utf-8" \
              -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/backupRuns" | Select-Object -Expand Content
          

You receive a JSON response similar to the following:

#### Response

If successful, the response body contains a list of `[BackupRun](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/backupRuns#BackupRun)` objects:
    
    {
            "kind": string,
            "items": [
              {
                object (BackupRun)
              }
            ],
            "nextPageToken": string
          }
          

The API response returns a list of backups for the instance as an array list, including `"id": string`.

  2. Call the [`clusters.restoreFromCloudSQL`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/restoreFromCloudSQL) method: 
         
         POST https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters:restoreFromCloudSQL
               

Replace the following:

     * `PROJECT_ID`: the project ID.
     * `REGION`: the region in which the AlloyDB cluster is deployed.

#### Request JSON body:
    
    {
            "clusterId": string,
            "cluster": {
              "databaseVersion": "POSTGRES_14/POSTGRES_15/POSTGRES_16/POSTGRES_17/POSTGRES_18",
              ["subscriptionType"](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#SubscriptionType): "STANDARD"
            },
            // Union field source can be only one of the following:
            "cloudsqlBackupRunSource": {
              object (CloudSQLBackupRunSource)
            }
            // End of list of possible types for union field source.
          }
          

To send your request, use one of these options:

#### **curl (Linux, macOS, or Cloud Shell)**

The following command assumes that you signed into the `gcloud CLI` with your user account by running `[gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init)` or `[gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login)`, or by using `[Cloud Shell](https://docs.cloud.google.com/shell/docs)`, which automatically signs you into the `gcloud CLI`.

You can check the active account by running `[gcloud auth list](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list)`.

Save the request body in a file named `request.json` and execute the following command:
    
    curl -X POST \
                   -H "Authorization: Bearer $(gcloud auth print-access-token)" \
                   -H "Content-Type: application/json; charset=utf-8" \
                   -d @request.json \
                   "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters:restoreFromCloudSQL"
          

#### **PowerShell (Windows)**

The following command assumes that you signed into the `gcloud CLI` with your user account by running `[gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init)` or `[gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login)`, or by using `[Cloud Shell](https://docs.cloud.google.com/shell/docs)`, which automatically signs you into the `gcloud CLI`.

You can check the active account by running `[gcloud auth list](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list)`.

Save the request body in a file named `request.json` and execute the following command:
    
    $cred = gcloud auth print-access-token
            $headers = @{ "Authorization" = "Bearer $cred" }
            Invoke-WebRequest \
              -Method POST \
              -Headers $headers \
              -ContentType: "application/json; charset=utf-8" \
              -InFile request.json \
              -Uri "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters:restoreFromCloudSQL"|Select-Object -Expand Content
          

You receive a JSON response similar to the following:

#### Response

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/alloydb/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

AlloyDB creates a new cluster in the specified project and location, and restores its volume from the backup specified in the [CloudSQLBackupRunSource](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#CloudSQLBackupRunSource) message.

  3. When the cluster is in a `READY` state, create the primary instance by calling the `[projects.locations.clusters.instances.create](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances/create)` method:  

         
         POST https://alloydb.googleapis.com/v1/{parent=projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID}/instances
               

Replace the following:

     * `PROJECT_ID`: the project ID.
     * `REGION`: the region in which the AlloyDB cluster is deployed.
     * `CLUSTER_ID`: the cluster ID.

#### Request JSON body:
    
    {
              "instanceId": "string",
              "instance": {
                "object": "Instance"
              }
            }
          

The request body contains an instance of `[Instance](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#Instance)`.

To send your request, use one of these options:

#### **curl (Linux, macOS, or Cloud Shell)**

The following command assumes that you signed into the `gcloud CLI` with your user account by running `[gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init)` or `[gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login)`, or by using `[Cloud Shell](https://docs.cloud.google.com/shell/docs)`, which automatically signs you into the `gcloud CLI`.

You can check the active account by running `[gcloud auth list](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list)`.

Save the request body in a file named `request.json` and execute the following command:
    
    curl -X POST \
                 -H "Authorization: Bearer $(gcloud auth print-access-token)" \
                 -H "Content-Type: application/json; charset=utf-8" \
                 -d @request.json \
                 "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID/instances"
          

#### **PowerShell (Windows)**

The following command assumes that you signed into the `gcloud CLI` with your user account by running `[gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init)` or `[gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login)`, or by using `[Cloud Shell](https://docs.cloud.google.com/shell/docs)`, which automatically signs you into the `gcloud CLI`.

You can check the active account by running `[gcloud auth list](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list)`.

Save the request body in a file named `request.json` and execute the following command:
    
    $cred = gcloud auth print-access-token
             $headers = @{ "Authorization" = "Bearer $cred" }
             Invoke-WebRequest \
               -Method POST \
               -Headers $headers \
               -ContentType: "application/json; charset=utf-8" \
               -InFile request.json \
               -Uri "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID/instances"|Select-Object -Expand Content
          

You receive a JSON response similar to the following:

#### Response

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/alloydb/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

  4. After the instance is updated to the `READY` state, connect to the instance and access the restored data from the Cloud SQL snapshot.



## What's next

  * [Connect to AlloyDB using public IP](https://docs.cloud.google.com/alloydb/docs/connect-public-ip).
  * [Create and connect to a database](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
