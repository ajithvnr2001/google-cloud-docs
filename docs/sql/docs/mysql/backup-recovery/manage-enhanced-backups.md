---
url: https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/manage-enhanced-backups/
title: Manage enhanced backups \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:26.929305+00:00
---

# Manage enhanced backups  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/manage-enhanced-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Manage enhanced backups Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/manage-enhanced-backups "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/manage-enhanced-backups "View this page for the SQL Server database engine")

Enhanced backups allow you to use Backup and DR Service with your Cloud SQL instances to manage your backups. You can enable enhanced backups for any instance by associating it with a [Backup and DR backup plan](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backup-options#enhanced-backups). You can also manage enhanced backups for your instance by doing the following:

  * Change your instance's associated backup plan
  * Perform an on-demand backup
  * List all backups in the backup vault for your instance



For more information about how enhanced backups work and their integration with Backup and DR, see [Enhanced backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backup-options#enhanced-backups). For more information on how backups work in Cloud SQL, see [Cloud SQL overview](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups).

## Before you begin

Before you can manage enhanced backups for your Cloud SQL instances, you must do the following:

  * Enable the Backup and DR API
  * Confirm you have the required permissions



### Enable the Backup and DR API

To use enhanced backups with your Cloud SQL instances, you must first enable the Backup and DR API:

[Enable the Backup and DR API ](https://console.cloud.google.com/backupdr?project=_)

### Required permissions

The following permissions are required to configure enhanced backups for your Cloud SQL instances:

  * `backupdr.backupPlans.list`
  * `backupdr.backupPlanAssociations.createForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.fetchForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.list`
  * `backupdr.backupPlanAssociations.getForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.triggerBackupForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.deleteForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.updateForCloudSqlInstance`
  * `backupdr.backupPlans.useForCloudSqlInstance`
  * `backupdr.bvdataSources.get`
  * `backupdr.bvdataSources.list`



For more information about these permissions, see [Backup and DR roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr).

## Enable enhanced backups

To enable enhanced backups for your instance, do the following:

  1. Identify the backup vault and backup plan you want to use.
  2. Associate your Cloud SQL instance to the backup plan.



For more information about enhanced backups, see [About Cloud SQL backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups).

### Identify the backup plan you want to use

To associate your Cloud SQL instance with a backup plan, you need first to create or identify the [backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan) that you want to use. The plan you choose defines your instance's backup schedule and log retention settings.

To create a backup plan, first use the [Backup and DR service](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr) to [create up a vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create) in which your backups will be stored, and then [create the plan itself](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create) in the [Backup and DR console](https://console.cloud.google.com/backupdr/backup-plans/list).

**Important:** The backup plan you want to use must be in the same region as your Cloud SQL instance.

Once you've identified the backup plan you want to associate, use its name to associate it with your Cloud SQL instance.

### Associate a backup plan to a Cloud SQL instance

**Warning:** When you attach a backup plan to a Cloud SQL instance, the existing backup and restore settings are overwritten by the backup plan.

To associate a backup plan with a Cloud SQL instance, you'll need the name for the backup plan you want to use. For more information on how to find the backup plan name, see [Create and manage a backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create).

###  Console 

To associate a backup plan with your Cloud SQL instance, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find the instance you want to associate the backup plan with. To open the **Overview** page of the instance, click the instance name.

  3. Click **Edit**.

  4. In the **Data Protection** section, under **Backup tier** , select **Enhanced backup tier**.

  5. In the **Backup plan** section, click **Select**.

  6. In the **Select a backup plan** window, do the following:

     1. Under **Project** , click **Browse** , then search for and select the Backup and DR project that contains the backup plan.

     2. Once you select the project, you'll see a list of all available backup plans. Find the backup plan you want to use, then click **Select**.

  7. Click **Save**.

Your instance is enabled for enhanced backups and using the associated backup plan's backup and retention settings.

**Caution:** This might cause your instance to restart.



###  gcloud 

To associate a backup plan with your Cloud SQL instance, run the following command:
    
    
    gcloud backup-dr backup-plan-associations create BACKUP_PLAN_ASSOCIATION_NAME
    --project=PROJECT_ID
    --resource=INSTANCE_ID
    --backup-plan=BACKUP_PLAN_NAME
    --resource-type=sqladmin.googleapis.com/Instance
    --location=REGION_ID
    

Replace the following:

  * BACKUP_PLAN_ASSOCIATION_NAME: the name of the backup plan association.
  * PROJECT_ID: your instance's project ID.
  * INSTANCE_ID: the ID of the instance you want to associate the backup plan to.
  * BACKUP_PLAN_NAME: the name of the backup plan you want to use. For more information, see identify the backup plan you want to use.
  * REGION_ID: the instance's region.



###  REST v1 

To create a backup plan association, use the [`backupPlanAssociations`](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.backupPlanAssociations) method in the [Backup and DR API](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest).

Before using any of the request data, make the following replacements: 

  * backup-plan-association-id: the backup plan association ID
  * resource-name: the full name of the Cloud SQL instance, in `projects/project-id/locations/location/instances/instance-name`format
  * backup-plan-name: the name of the backup plan, in `projects/project-id/backupPlans/backup-plan-name` format



HTTP method and URL: 
    
    
    POST https://backupdr.googleapis.com/v1/projects/project-id/locations/location/backupPlanAssociations

Request JSON body: 
    
    
    {
      "name": "backup-plan-association-id",
      "resourceType": "sql.googleapis.com/Instance",
      "resource": "resource-name",
      "backupPlan": "backup-plan-name"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://backupdr.googleapis.com/v1/projects/project-id/locations/location/backupPlanAssociations"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://backupdr.googleapis.com/v1/projects/project-id/locations/location/backupPlanAssociations" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "operation",
      "state": "CREATING",
      "user": "user@example.com",
      "updateTime": "2020-01-21T22:43:37.981Z",
      "operationType": "backupPlanAssociations.create",
      "name": "operation-id",
      "dataSource": "projects/project-id/locations/location/backupVaults/backup-vault-name/dataSources/data-source-name"
    }
    

**Note:** When you change to a backup plan that has a longer log retention than your current plan, it will take time before you have as many days of logs available as the new plan specifies. For example, if your current plan has a log retention period of 7 days and your new plan has a log retention period of 10 days, you won't be able to restore to a point in time 10 days earlier until at least 3 days after you make the change.

## Manage enhanced backups

After your instance is enabled for enhanced backups and a backup plan is associated with the instance, you can perform an on-demand backup, view all the backups in the backup vault, or change the associated backup plan.

To manage a backup plan, see [Create and manage a backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create). To manage a backup vault, see [Create and manage a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create).

### Change your instance's associated backup plan

You can change the backup plan to use with your Cloud SQL instance. To change the backup plan associated with your Cloud SQL instance, the new plan must be in the same backup vault as your current backup plan, and be in the same region as your Cloud SQL instance.

To change to a new backup plan, do the following:

###  Console 

To associate the new backup plan with your instance, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find the instance you want to change the backup plan for. To open the **Overview** page of the instance, click the instance name.

  3. Click **Edit**.

  4. In the **Data Protection** section, under **Backup tier** , select **Enhanced backup tier**.

  5. Click the **Change** button.

  6. In the **Select a backup plan** window, choose the new plan.

  7. Click **Save**.

Your instance is enabled for enhanced backups and is using the new backup plan that you selected.

**Note:** This will cause your instance to restart.



###  gcloud 

To associate the new backup plan with your instance, do the following:
    
    
    gcloud backup-dr backup-plan-associations create BACKUP_PLAN_ASSOCIATION_NAME
    --project=PROJECT_ID
    --resource=INSTANCE_ID
    --backup-plan=BACKUP_PLAN_NAME
    --resource-type=sqladmin.googleapis.com/Instance
    --location=REGION_ID
    

Replace the following:

  * BACKUP_PLAN_ASSOCIATION_NAME: the name of the backup plan association.
  * PROJECT_ID: the instance's project ID.
  * INSTANCE_ID: the instance's ID.
  * BACKUP_PLAN_NAME: the name of the backup plan. For more information, see identify the backup plan you want to use.
  * REGION_ID: the instance's region.



###  REST v1 

After you delete the existing backup plan association, associate the new backup plan using the [`backupPlanAssociations`](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.backupPlanAssociations) method in the [Backup and DR API](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest).

Before using any of the request data, make the following replacements: 

  * backup-plan-association-id: the backup plan association ID
  * resource-name: the full name of the Cloud SQL instance, in `projects/project-id/locations/location/instances/instance-name`format
  * backup-plan-name: the name of the backup plan, in `projects/project-id/backupPlans/backup-plan-name` format



HTTP method and URL: 
    
    
    POST https://backupdr.googleapis.com/v1/projects/project-id/locations/location/backupPlanAssociations

Request JSON body: 
    
    
    {
      "name": "backup-plan-association-id",
      "resourceType": "sql.googleapis.com/Instance",
      "resource": "resource-name",
      "backupPlan": "backup-plan-name"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://backupdr.googleapis.com/v1/projects/project-id/locations/location/backupPlanAssociations"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://backupdr.googleapis.com/v1/projects/project-id/locations/location/backupPlanAssociations" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "operation",
      "state": "CREATING",
      "user": "user@example.com",
      "updateTime": "2020-01-21T22:43:37.981Z",
      "operationType": "backupPlanAssociations.create",
      "name": "operation-id",
      "dataSource": "projects/project-id/locations/location/backupVaults/backup-vault-name/dataSources/data-source-name"
    }
    

### Perform an on-demand backup

You can perform an on-demand backup for a Cloud SQL instance with and associated backup plan using Google Cloud console, [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or the Cloud SQL API.

###  Console 

To perform an on-demand backup for an instance with enhanced backups enabled, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Backups** page.

[Go to Cloud SQL Backups](https://console.cloud.google.com/sql/backups)

  2. Click **Create backup**.

  3. In the **Create an on-demand backup** window, do one of the following:

     * Under **Choose a backup rule** , select the type of on-demand backup you want to take. The backup rule defines the retention period of the on-demand backup.
     * Select the **Based on custom retention period** option to specify a custom retention period for the backup. When using a custom retention period, consider the following rules:
     * **Retention Range Logic** : The allowed retention range is determined by the intersection of the backup vault's minimum enforced retention and the backup plan's maximum custom retention setting.
     * **Implicit Defaults** : If `max_custom_on_demand_retention_days` is not explicitly set in the backup plan, the service uses a default upper limit of the backup vault's minimum enforced retention plus 30 days.
     * **Upper Limit** : Regardless of configuration, the maximum allowed retention for any custom on-demand backup is 10 years (3,653 days).
  4. Click **Create**.

Your on-demand backup is created.




###  gcloud 

To perform an on-demand backup for an instance with enhanced backups enabled, run the following command:
    
    
    gcloud backup-dr backup-plan-associations trigger-backup BACKUP_PLAN_ASSOCIATION_NAME
    --backup-rule-id=BACKUP_RULE_ID
    --project=PROJECT_ID
    --location=BACKUP_VAULT_LOCATION
    --custom-retention-days=CUSTOM_RETENTION
    [--no-async]
    

Replace the following:

  * BACKUP_PLAN_ASSOCIATION_NAME: the name of the backup plan association of your Cloud SQL instance. To find a list of all backup plans associated with a Cloud SQL instance, see List all backup plan associations.
  * BACKUP_RULE_ID: the backup rule name for the type of on-demand backup you want to take (e.g. `rule-daily`).
  * PROJECT_ID: the instance's project ID.
  * BACKUP_VAULT_LOCATION: the location of the backup vault associated with your backup plan.



###  REST v1 

To trigger an on-demand backup for your Cloud SQL instance, use the [`backupPlanAssociations`](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.backupPlanAssociations) method in the [Backup and DR API](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest).

Before using any of the request data, make the following replacements: 

  * backup-rule-id: the backup rule ID for which a backup needs to be triggered



HTTP method and URL: 
    
    
    GET https://backupdr.googleapis.com/v1/projects/project-id/locations/location/backupPlanAssociations/backup-plan-association-id:triggerBackup

Request JSON body: 
    
    
    {
      "ruleId": "backup-rule-id"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://backupdr.googleapis.com/v1/projects/project-id/locations/location/backupPlanAssociations/backup-plan-association-id:triggerBackup"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://backupdr.googleapis.com/v1/projects/project-id/locations/location/backupPlanAssociations/backup-plan-association-id:triggerBackup" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "operation",
      "done": "true",
      "user": "user@example.com",
      "updateTime": "2020-01-21T22:43:37.981Z",
      "operationType": "backupPlanAssociations:triggerBackup",
      "name": "operation-id"
    }
    

### List all the backups in a backup vault for your instance

You can list all backups for in the backup vault for your Cloud SQL instance using Google Cloud console, [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or the Cloud SQL API.

###  Console 

  1. In the Google Cloud console, go to the **Cloud SQL Backups** page.

[Go to Cloud SQL Backups](https://console.cloud.google.com/sql/backups)

  2. In the **Backup tier** drop-down, select **Enhanced tier** , then from the **Backup vault** list, select the backup vault that contains the backup you want to use.

All backups available in the backup vault for your selected instance are displayed.




###  gcloud 

To list all available backups for your Cloud SQL instance in the backup vault, you need to first find the `data-source` for your Cloud SQL instance, then run the `gcloud backup-dr backups list` command.

To find your instance's `data-source`, run the following command:
    
    
    gcloud backup-dr data-source-references
    fetch-for-resource-type sqladmin.googleapis.com/Instance
    --location=REGION_ID | grep INSTANCE_NAME
    

Replace the following:

  * REGION_ID: the region ID for your Cloud SQL instance.
  * INSTANCE_NAME: the name of your Cloud SQL instance.



To list all the backups in a backup vault for your instance, run the following command:
    
    
    gcloud backup-dr backups list
    --data-source=DATA_SOURCE
    --location=REGION_ID
    --backup-vault=BACKUP_VAULT_NAME
    

Replace the following:

  * DATA_SOURCE: the `data-source` for your Cloud SQL instance.
  * REGION_ID: the region ID for the backup vault.
  * BACKUP_VAULT_NAME: the name of the backup vault associated with your backup plan.



###  REST v1 

To list all available backups for your Cloud SQL instance in the backup vault, you need to first find the data source for your Cloud SQL instance, then get all the backups using the data source name.

**Find the instance's data source**

To find your instance's data source, use the [`dataSource.References`](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.dataSourceReferences) method in the [Backup and DR API](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest).

HTTP method and URL: 
    
    
    GET https://backupdr.googleapis.com/v1/projects/project-id/locations/location/dataSourceReferences:fetchForResourceType?filter=dataSourceGcpResourceInfo.gcp_resourcename="projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "resourceType": "sqladmin.googleapis.com/Instance"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://backupdr.googleapis.com/v1/projects/project-id/locations/location/dataSourceReferences:fetchForResourceType?filter=dataSourceGcpResourceInfo.gcp_resourcename="projects/project-id/instances/instance-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://backupdr.googleapis.com/v1/projects/project-id/locations/location/dataSourceReferences:fetchForResourceType?filter=dataSourceGcpResourceInfo.gcp_resourcename="projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/project-id/locations/location/dataSourceReferences/dataSourceId"
      "dataSourceBackupConfigState": "ACTIVE",
      "dataSourceBackupCount": "1",
      "dataSourceBackupConfigInfo": {
        "lastBackupState: "SUCCEEDED",
        "lastSuccessfulBackupConsistencyTime": "2024-09-19T18:00:00Z"
      },
      "dataSourceGcpResourceInfo": {
        "gcpResourceName": "projects/project-id/instances/instance-id",
        "type": "sqladmin.googleapis.com/Instance",
        "location": "location"
        "cloudSqlInstanceProperties": {
          "name": "projects/project-id/instances/instance-id"
        }
      }
    }
    

**List the instance's backups**

To list your the backups for your instance using the data source ID, use the [`backupVaults.dataSources.backups`](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.backupVaults.dataSources.backups) method in the [Backup and DR API](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest).

HTTP method and URL: 
    
    
    GET https://backupdr.googleapis.com/v1/projects/project-id/locations/location/backupVaults/backup-vault-id/dataSources/data-source-id/backups

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://backupdr.googleapis.com/v1/projects/project-id/locations/location/backupVaults/backup-vault-id/dataSources/data-source-id/backups"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://backupdr.googleapis.com/v1/projects/project-id/locations/location/backupVaults/backup-vault-id/dataSources/data-source-id/backups" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "backups": [
        {
          "name": "backup-name",
          "state": "ACTIVE",
          "backupType": "ON_DEMAND",
          "createTime": "",
          "expireTime": "",
          "CloudSqlInstanceBackupProperties": {
            "databaseInstalledVersion": "database-installed-version",
            "finalBackup": "TRUE",
            "sourceInstance": "instance-name",
            "instanceTier": "db-custom-1-3840"
          }
        },
        {
          ...
        }
      ]
    }
    
    

## Disable enhanced backups

You can disable enhanced backups by switching your Cloud SQL instance back to the standard backups option. This deletes the association between the backup plan and your instance.

### Change your instance to standard backups

**Warning:** Changing your instance to standard backups causes your instance to restart.

###  Console 

To disable enhanced backups and switch your instance back to the standard backups option, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find the instance you want to change the backup option for. To open the **Overview** page of the instance, click the instance name.

  3. Click **Edit**.

  4. In the **Data Protection** section, under **Backup tier** , select the **Standard backup tier**. Update the Standard backups settings for your instance as necessary.

  5. Click **Save**.

Your instance's associated backup plan is deleted and your instance is now managed under the Standard backups option, managed by Cloud SQL.




###  gcloud 

To disable enhanced backups and switch your instance back to the standard backups option, run the following command:
    
    
    gcloud backup-dr backup-plan-associations delete BACKUP_PLAN_ASSOCIATION_NAME
    --location=BACKUP_VAULT_LOCATION
    

Replace the following:

  * BACKUP_PLAN_ASSOCIATION_NAME: the name of the backup plan association you want to delete.
  * BACKUP_VAULT_LOCATION: the location of the backup vault.



###  REST v1 

To disable enhanced backups, you need to remove the backup plan association using the [`backupPlanAssociations`](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.backupPlanAssociations) method in the [Backup and DR API](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest).

Before using any of the request data, make the following replacements: 

  * backup-plan-association-id: the backup plan association ID, in `projects/project-id/locations/location/backupPlanAssociations/backup-plan-association-id` format



HTTP method and URL: 
    
    
    POST https://backupdr.googleapis.com/v1/projects/project-id/locations/location/backupPlanAssociations/delete

Request JSON body: 
    
    
    {
      "name": "backup-plan-association-id",
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://backupdr.googleapis.com/v1/projects/project-id/locations/location/backupPlanAssociations/delete"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://backupdr.googleapis.com/v1/projects/project-id/locations/location/backupPlanAssociations/delete" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "operation",
      "done": "true",
      "user": "user@example.com",
      "updateTime": "2020-01-21T22:43:37.981Z",
      "operationType": "backupPlanAssociations.delete",
      "name": "operation-id"
    }
    

## What's next

  * [Restore an instance](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restoring#restore-backup-vault)
  * [About Cloud SQL backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
