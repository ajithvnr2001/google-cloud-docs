---
url: https://docs.cloud.google.com/sql/docs/sqlserver/set-maintenance-window/
title: View and set maintenance windows \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:49.234825+00:00
---

# View and set maintenance windows  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/set-maintenance-window/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  View and set maintenance windows Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/set-maintenance-window "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window "View this page for the PostgreSQL database engine") | SQL Server

This page has procedures for finding and setting maintenance windows for Cloud SQL instances. To learn more about how and why Cloud SQL performs maintenance, see [Maintenance updates on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance).

If you've [opted in to receive maintenance notifications](https://docs.cloud.google.com/sql/docs/sqlserver/set-maintenance-window#opt-in), then Cloud SQL sends you an email notification when a maintenance update is available for your Cloud SQL instance. Cloud SQL sends a notification before the maintenance rollout and then proceeds to apply the update to groups of instances on a weekly schedule. You can control how much advance notification you receive before your instance receives the maintenance update by selecting the maintenance timing for your instance.

You have the following options for scheduling the timing of your maintenance update:

  * If you select `Any` or don't configure this setting, then the maintenance update can happen at any time, but typically happens within the first week of the rollout.
  * If you select `Week 1` (also referred to as `preview` and `canary`), then the maintenance update happens 7 to 14 days after the maintenance notification is sent out.
  * If you select `Week 2` (also referred to as `production` and `stable`), then the maintenance update happens 15 to 21 days after the notification is sent out.
  * If you select `Week 5`, then the maintenance update happens 35 to 42 days after the notification is sent out.



If you make changes to your maintenance window setting while the instance is already undergoing maintenance or is scheduled for maintenance, then the changes don't take effect immediately. These changes are reflected in future maintenance events.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




## Set a maintenance window on an instance

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. In the **Maintenance** section, click **Edit maintenance preferences**.
  4. In the **Configuration options** section, open **Maintenance**.
  5. Configure the following options: 
     * **Maintenance timing**. Select the week to apply the automatic maintenance update. You have the following options: 
       * **Any** : the maintenance update can happen at any time, but typically happens within **Week 1**.
       * **Week 1** : the maintenance happens 7 to 14 days after the maintenance notification is sent out.
       * **Week 2** : the maintenance update happens 15 to 21 days after the notification is sent out.
       * **Week 5** : the maintenance update happens 35 to 42 days after the notification is sent out.
     * **Maintenance window**. Select a preferred day of the week and time window. Options include the following: 
       * **Any window** : the default maintenance window. The maintenance update is not restricted to any specific day of the week or time of day.
       * **_Day of the week_** : select a day for your maintenance window **Saturday** , **Sunday** , **Monday** , **Tuesday** , **Wednesday** , **Thursday** , or **Friday**.
       * **_Time of day_** : if you select a day of the week, then you can also choose a time of day. Select a one hour interval in your local time zone.



### gcloud

To configure a maintenance window and maintenance timing on a Cloud SQL instance, run the following command:
    
    
    gcloud sql instances patch INSTANCE_ID \
      --maintenance-window-day=DAY \
      --maintenance-window-hour=HOUR \
      --maintenance-release-channel=MAINTENANCE_TIMING
        

Replace the following variables:

  * INSTANCE_ID: the instance ID, which can't be a read replica instance.
  * DAY: the day of the week when you want maintenance to occur. Set to `MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, or `SUNDAY`. Specify in the UTC time zone.
  * HOUR: the hour of day, `0` \- `23`, for the maintenance window. Specify in the UTC time zone.
  * MAINTENANCE_TIMING: the week of the maintenance rollout period that you want the maintenance update to be applied. Options include:
    * `preview`: This translates to **Week 1** after the maintenance notification is sent out. The maintenance update is scheduled between 7 to 14 days after the notification.
    * `production`: This translates to **Week 2** after the maintenance notification is sent out. The maintenance update is scheduled between 15 to 21 days after the notification.
    * `week5`: The maintenance update is scheduled 35 to 42 days after the maintenance notification is sent out.



For reference information, see [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch).

### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or project number of the Google Cloud project.
  * INSTANCE_ID: the instance ID, which can't be a read replica instance.
  * HOUR: the hour of day, `0` \- `23`, for the maintenance window. Specify in the UTC time zone. 
  * DAY: the day of the week for the maintenance update to occur. Specify `MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, or `SUNDAY`. Specify in the UTC time zone. 
  * MAINTENANCE_TIMING: the week of the maintenance rollout period that you want the maintenance update to be applied. Options include: 
    * `canary`: This translates to **Week 1** after the maintenance notification is sent out. The maintenance update is scheduled between 7 to 14 days after the notification.
    * `stable`: This translates to **Week 2** after the maintenance notification is sent out. The maintenance update is scheduled between 15 to 21 days after the notification.
    * `week5`: The maintenance update is scheduled 35 to 42 days after the maintenance notification is sent out.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "maintenanceWindow": {
            "hour": "HOUR",
            "day": "DAY",
            "updateTrack": "MAINTENANCE_TIMING"
        }
      }
    }
    
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-04-01T21:30:35.667Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or project number of the Google Cloud project.
  * INSTANCE_ID: the instance ID, which can't be a read replica instance.
  * HOUR: the hour of day, `0` \- `23`, for the maintenance window. Specify in the UTC time zone.
  * DAY: the day of the week when you want the maintenance update to occur. Specify `MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, or `SUNDAY`. Specify in the UTC time zone. 
  * MAINTENANCE_TIMING: the week of the maintenance rollout period that you want the maintenance update to be applied. Options include: 
    * `canary`: This translates to **Week 1** after the maintenance notification is sent out. The maintenance update is scheduled between 7 to 14 days after the notification.
    * `stable`: This translates to **Week 2** after the maintenance notification is sent out. The maintenance update is scheduled between 15 to 21 days after the notification.
    * `week5`: The maintenance update is scheduled 35 to 42 days after the maintenance notification is sent out.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "maintenanceWindow": {
            "hour": "HOUR",
            "day": "DAY",
            "updateTrack": "MAINTENANCE_TIMING"
        }
      }
    }
    
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-04-01T21:30:35.667Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Opt in to maintenance notifications

Before you opt-in to receive maintenance notifications, you must set a maintenance window on an instance

  1. Go to the **Communication** page. [Go to Communication](https://console.cloud.google.com/user-preferences/communication)
  2. In the row for **Cloud SQL** , **Maintenance window** , select the radio button under **Email** to turn it **ON**.



Each user that needs to receive notifications must opt in separately.

## Find maintenance notifications in the Google Cloud console

You can view maintenance notifications in a few places in the Google Cloud console:

  * On the **[Logs explorer](https://console.cloud.google.com/logs)** page in the Google Cloud console. Use the **All logs name** drop-down to search for `maintenance-events`, then click **Apply**. If maintenance is scheduled for an instance, then the log shows the name of the instance and its scheduled maintenance start time.

  * When an instance is scheduled for maintenance, the date for maintenance is listed on the **Instances** page in the **Maintenance** column. The **Maintenance** column is usually hidden, but it displays automatically when maintenance is scheduled. You can also select **Maintenance** from the **Column display options** (![Column display options icon is three lines](https://docs.cloud.google.com/static/sql/images/column_display.png)) if you want the **Maintenance** column to always show up.

  * Alternatively, you can select an instance to go to the **Instance details** page. If the instance is scheduled for maintenance, you will see a message in the **Maintenance** pane.  
[Go to Cloud SQL instances](https://console.cloud.google.com/sql/instances)




## Find scheduled maintenance using the API

### gcloud

To check for upcoming scheduled maintenance, use the following command:
    
    
    gcloud sql instances describe INSTANCE_ID
        

Replace the following variable:

  * INSTANCE_ID: The instance to check for scheduled maintenance.



In the response, look for the `scheduledMaintenance` section.

### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
  * INSTANCE_NAME: the name of the instance that you're configuring for high availability



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#instance",
      "state": "RUNNABLE",
      "databaseVersion": "SQLSERVER_2019_STANDARD"
    }
    

In the response, look for the `scheduledMaintenance` section.

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
  * INSTANCE_NAME: the name of the instance that you're configuring for high availability



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#instance",
      "state": "RUNNABLE",
      "databaseVersion": "SQLSERVER_2019_STANDARD"
    }
    

In the response, look for the `scheduledMaintenance` section.

## Reschedule planned maintenance

You can reschedule maintenance by using the Google Cloud console, the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or the Cloud SQL Admin API.

If you set the maintenance timing of your instance to Week 1 or Week 2, then you can reschedule maintenance by up to 28 days.

If you set the maintenance timing of your instance to Week 5, then you can reschedule maintenance by up to 7 days. You must reschedule maintenance within this time period to ensure that the instance receives the maintenance update before the next quarterly maintenance rollout begins.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Filter for the term **Maintenance** to list all instances scheduled for maintenance.
  3. In the **Maintenance** column, click **Reschedule**.
  4. In the **Reschedule** dialog, choose whether to apply maintenance immediately, reschedule it to happen at a specific time within the allowed deferral period as defined in rescheduled planned maintenance, or defer to the next available maintenance window.



### gcloud

To reschedule maintenance on a Cloud SQL instance, run the following command:
    
    
    gcloud sql reschedule-maintenance INSTANCE_ID \
      --reschedule-type=RESCHEDULE_TYPE \
      [--schedule-time=RESCHEDULE_TIME]
      

Replace the following variables:

  * INSTANCE_ID: The instance to reschedule.
  * RESCHEDULE_TYPE: Use one of **IMMEDIATE** , **NEXT_AVAILABLE_WINDOW** , or **SPECIFIC_TIME**. 

If you choose **NEXT_AVAILABLE_WINDOW** , maintenance is rescheduled to the next available maintenance window following the current scheduled time. 

  * RESCHEDULE_TIME: If you specify **SPECIFIC_TIME** for RESCHEDULE_TYPE, then you also need to set the `--schedule-time` flag to specify the new day and time for maintenance to occur. Uses ISO 8601 format. For example, 2020-01-16T16:56:00.000Z



For reference information, see [`gcloud sql reschedule-maintenance`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/reschedule-maintenance).

If you want to reschedule maintenance for up to 28 days, then check the version number of `gcloud`. If the version number is below `390.0.0_RC00`, then reinstall `gcloud`. 

### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The project ID
  * INSTANCE_ID: The instance ID
  * RESCHEDULE_TYPE: Use one of **IMMEDIATE** , **NEXT_AVAILABLE_WINDOW** , or **SPECIFIC_TIME**. 

If you choose **NEXT_AVAILABLE_WINDOW** , then maintenance is rescheduled to the next available maintenance window. 




HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/rescheduleMaintenance

Request JSON body: 
    
    
    {
      "reschedule": {
        "reschedule_type": "RESCHEDULE_TYPE"
      }
    }
    
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/rescheduleMaintenance"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/rescheduleMaintenance" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "startTime": "08:00",
      "endTime": "08:01",
      "operationType": RESCHEDULE_MAINTENANCE,
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The project ID
  * INSTANCE_ID: The instance ID
  * RESCHEDULE_TYPE: Use one of **IMMEDIATE** , **NEXT_AVAILABLE_WINDOW** , or **SPECIFIC_TIME**. 

If you choose **NEXT_AVAILABLE_WINDOW** , then maintenance is rescheduled to the next available maintenance window. 




HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/rescheduleMaintenance

Request JSON body: 
    
    
    {
      "reschedule": {
        "reschedule_type": "RESCHEDULE_TYPE"
      }
    }
    
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/rescheduleMaintenance"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/rescheduleMaintenance" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "startTime": "08:00",
      "endTime": "08:01",
      "operationType": RESCHEDULE_MAINTENANCE,
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

To see how the [underlying REST API request](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/patch) is constructed for this task, see the [APIs Explorer on the instances:post page](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/patch).

**Note** : If you reschedule maintenance for an instance at the same time as an existing deny maintenance period, then the deny maintenance period takes precedence and the maintenance event is skipped.

## Configure a deny maintenance period

You can configure a maximum of one deny maintenance period on a Cloud SQL instance at any given time. The deny maintenance period takes precedence over any scheduled maintenance window. If there's a conflict between the timing of a maintenance window and the deny maintenance period, the deny maintenance period overrides the maintenance window.

**Caution:** Starting on August 15, 2025, you can't set a deny maintenance period for an instance if its maintenance version is older than 12 months. Any instance that uses a maintenance version older than 12 months must receive an update. To update the instance, [perform self-service maintenance](https://docs.cloud.google.com/sql/docs/sqlserver/self-service-maintenance) or wait for the automatic update during the [next maintenance window](https://docs.cloud.google.com/sql/docs/sqlserver/set-maintenance-window#find-maintenance-api). After you update the instance, then you can set a deny maintenance period.

You can manually remove a deny maintenance period, whether it has already occurred or not.

To configure a deny maintenance period, set its start date, end date, and the time of day the interval begins and ends. A deny maintenance period can span from one to 90 days.

For start date and end date, there are two formats:

  * `yyyy-mm-dd`: indicates a specific date
  * `mm-dd`: indicates a date recurring every year



The start date and end date are UTC. To set the timezone, use the time field to adjust the start time. For example, the start date = 2020-10-10 and the time = 07:00:00 indicate the start time 2020-10-10 07:00:00 UTC (2020-10-10 00:00:00 PST)

For time, the format is: `HH:mm:SS`.

  * Hours are between 0 and 23 (inclusive).
  * Minutes and seconds are between 0 and 59 (inclusive).



### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. In the **Maintenance** section, click **Edit maintenance preferences**.
  4. In the **Deny maintenance period** section, set the start and end dates.
  5. In the **Advanced options** section, optionally select **Repeat every year**.
  6. Click **Save**.



### gcloud

To configure a deny maintenance period on a Cloud SQL instance, run the following command:
    
    
    gcloud sql instances patch INSTANCE_ID\
       --deny-maintenance-period-start-date=START_DATE \
       --deny-maintenance-period-end-date=END_DATE \
       --deny-maintenance-period-time=TIME

Replace the following variables:

  * INSTANCE_ID: Cloud SQL instance ID
  * START_DATE: date when the interval begins. For example, 2021-11-29
  * END_DATE: date when the interval ends. For example, 2021-12-02
  * TIME: time of day for interval to start and end. For example, 00:00:00



### REST v1

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID
  * start-date: The start date (yyyy-mm-dd) or (mm-dd) for annual recurrence
  * end-date: The end date (yyyy-mm-dd) or (mm-dd) for annual recurrence
  * time: The start and end time (HH:mm:SS)



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings":
      {
        "denyMaintenancePeriods": [{
          "start_date": "start-date",
          "end_date": "end-date"
          "time": "time"
        }]
      }
    }
    
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "startTime": "08:00",
      "endTime": "08:01",
      "operationType": MAINTENANCE_DENY_PERIOD,
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID
  * start-date: The start date (yyyy-mm-dd) or (mm-dd) for annual recurrence
  * end-date: The end date (yyyy-mm-dd) or (mm-dd) for annual recurrence
  * time: The start and end time (HH:mm:SS)



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings":
      {
        "denyMaintenancePeriods": [{
          "start_date": "start-date",
          "end_date": "end-date"
          "time": "time"
        }]
      }
    }
    
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "startTime": "08:00",
      "endTime": "08:01",
      "operationType": MAINTENANCE_DENY_PERIOD,
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

## Remove a deny maintenance period

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. In the **Maintenance** section, click **Edit maintenance preferences**.
  4. In the **Deny maintenance period** section, click **Clear**.
  5. Click **Save**.



### gcloud

To remove a deny maintenance period from a Cloud SQL instance, run the following command:
    
    
    gcloud sql instances patch INSTANCE_ID \
    --remove-deny-maintenance-period

Replace the following variables:

  * INSTANCE_ID: Cloud SQL instance ID



### REST v1

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings":
      {
        "denyMaintenancePeriods": []
      }
    }
    
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "startTime": "08:00",
      "endTime": "08:01",
      "operationType": MAINTENANCE_DENY_PERIOD,
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings":
      {
        "denyMaintenancePeriods": []
      }
    }
    
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "startTime": "08:00",
      "endTime": "08:01",
      "operationType": MAINTENANCE_DENY_PERIOD,
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

## Deny maintenance period notifications

Maintenance window notifications aren't sent when the planned maintenance time falls within the deny maintenance period and are forbidden by maintenance deny period settings.

If you change the deny maintenance period settings to prevent maintenance at a previously scheduled time, then the Cloud SQL instance skips maintenance and sends a notification about canceling the maintenance. Cloud SQL sends this cancellation notice whenever the instance is scheduled for an update.

Notifications of planned maintenance are sent during the deny maintenance period, as long as such maintenance is scheduled to occur outside of that period.

## What's next

  * [Start, stop, and restart instances](https://docs.cloud.google.com/sql/docs/sqlserver/start-stop-restart-instance)
  * [Learn more about deny maintenance periods](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance#deny)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
