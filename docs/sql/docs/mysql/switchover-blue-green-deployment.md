---
url: https://docs.cloud.google.com/sql/docs/mysql/switchover-blue-green-deployment/
title: Perform a blue-green deployment switchover \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:23.517680+00:00
---

# Perform a blue-green deployment switchover  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/switchover-blue-green-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Perform a blue-green deployment switchover Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

After you test and validate your green environment, you start a _switchover_ to convert the green environment to become your new production read and write environment.

## Before you begin

Before you initiate a switchover, ensure that you have the required permissions and that your deployment is ready for cutover.

### Required roles and permissions

To get the permissions that you need to execute a switchover, ask your administrator to grant you the following IAM role on your project:

  * Cloud SQL Admin (`roles/cloudsql.admin`)



For custom roles, ensure that you have the following permissions:

  * `cloudsql.blueGreenDeployments.switchover`
  * `cloudsql.blueGreenDeployments.get`
  * `cloudsql.instances.switchover`
  * `cloudsql.operations.get`



For more information about IAM roles and permissions in Cloud SQL, see [Roles and permissions](https://docs.cloud.google.com/sql/docs/mysql/iam-roles).

### Pre-switchover verification

Before initiating a switchover, verify the following conditions:

  1. **Deployment state:** the deployment must be in the `SWITCHOVER_READY` state.
  2. **Workload validation:** complete all testing and validation on the green staging instance.
  3. **Low replication lag:** ensure that replication lag between blue and green is minimal to reduce cutover time.



## How switchover works

When you start a switchover, Cloud SQL performs the following automated sequence:

  1. **Pre-switchover validation:** before the switchover operation, Cloud SQL validates that replication is not broken and performs a series of configuration checks to ensure that the deployment is ready.
  2. **Switchover workflow execution:** during workflow execution, Cloud SQL prepares the instances for cutover. If replication lag is too high or if an active transaction blocks cutover, the switchover operation fails and your production blue environment remains online.
  3. **Traffic redirection:** Cloud SQL swaps the connection endpoints between the blue and green instances.
  4. **Role conversion:** the green instance becomes the active production read and write instance, and the blue instance becomes a standalone read and write instance.



During switchover, application connections experience a brief disruption (typically in seconds) before reconnecting automatically to the upgraded production instance. Switchover downtime varies based on the Cloud SQL edition:

  * **Cloud SQL Enterprise Plus edition:** switchover downtime is typically sub-second.
  * **Cloud SQL Enterprise edition:** switchover downtime is typically less than 60 seconds, depending on workload and replication lag. No application configuration or connection string changes are required.

**Note:** Blue-green deployment switchover is strictly a planned operation that requires a healthy, `RUNNING` blue source instance. Unlike a disaster recovery (DR) replica or high availability standby, the green instance cannot be used as a failover target during an unplanned outage of your source instance.

### Switchover lifecycle states

Before, during, and after a switchover, the deployment transitions through the following states in the `state` response field:

  * **`SWITCHOVER_READY`:** logical replication from blue to green is healthy and the deployment is ready for switchover. The `SWITCHOVER_READY` status is contingent only on replication being healthy. Cloud SQL doesn't evaluate replication lag when setting this status.
  * **`SWITCHOVER_NOT_READY`:** the deployment is provisioned, but switchover can't be initiated. This occurs if logical replication is broken, paused, or stopped, or if an underlying node error occurred. Cloud SQL doesn't evaluate replication lag when setting this status. Inspect `errorDetail` and resolve the error before attempting switchover.
  * **`SWITCHOVER_IN_PROGRESS`:** the switchover command is actively executing. Cloud SQL is swapping connection endpoints and converting green to the production read and write instance.
  * **`SWITCHOVER_COMPLETED`:** the switchover finished successfully. Green is now your active production database instance serving read and write traffic, and the blue instance is retained as a standalone read and write instance until you delete the deployment.



## Best practices before switchover

  * **Schedule during low-traffic windows:** although downtime is minimal (typically in seconds), start the switchover during periods of low write activity (for example, off-peak hours or maintenance windows when write queries per second [QPS] are at their lowest). This minimizes replication lag and reduces the risk of canceled transactions.
  * **Verify replication lag:** make sure that replication lag is minimal before you start the switchover. Describing a blue-green deployment doesn't show replication lag, and Cloud SQL doesn't check replication lag before the switchover operation. However, during workflow execution, switchover fails if replication lag is too high. To monitor replication lag, check Cloud Monitoring metrics (such as `replica_lag`) or inspect replication status directly on the green instance. For more information, see [Replication lag](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-lag).
  * **Check active transactions:** make sure that long-running DDL operations or batch writes are completed before you start the switchover.



## Start a switchover

Start the switchover operation by using the Google Cloud console, the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or the Cloud SQL Admin API:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name.
  3. In the **Blue Green Deployment Status** card, click **Details** to open the **Deployment overview** page.
  4. Click **Switchover deployment**.
  5. In the **Instance Setting Differences** dialog, review the setting differences between the **Source** and **Target** instances, and then click **Continue** to start the switchover.



### gcloud

Run the `blue-green-deployments switchover` command:
    
    
    gcloud beta sql blue-green-deployments switchover DEPLOYMENT_NAME \
      --region=REGION \
      --async
    

Switchover operations can take several minutes to complete. You might see a message indicating that the operation is taking longer than expected. You can either ignore this message or run the [`gcloud sql operations wait`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/wait) command to dismiss the message and wait for the operation to complete:
    
    
    gcloud sql operations wait OPERATION_ID
    

To check the status of the switchover operation, run the [`gcloud sql operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/describe) command:
    
    
    gcloud sql operations describe OPERATION_ID
    

Replace the following:

  * DEPLOYMENT_NAME: the name of your blue-green deployment.
  * REGION: the Google Cloud region where the deployment was created.
  * OPERATION_ID: the ID of the switchover operation.



### REST v1

Send a POST request to the `blueGreenDeployments.switchover` method:
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/
      locations/REGION/
      blueGreenDeployments/DEPLOYMENT_NAME:switchover
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the Google Cloud region where the deployment was created.
  * DEPLOYMENT_NAME: the name of your blue-green deployment.



### REST v1beta4

Send a POST request to the `blueGreenDeployments.switchover` method:
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/
      locations/REGION/
      blueGreenDeployments/DEPLOYMENT_NAME:switchover
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the Google Cloud region where the deployment was created.
  * DEPLOYMENT_NAME: the name of your blue-green deployment.



## Post-switchover monitoring

After the switchover completes:

  1. Verify that your application reconnects successfully and production database operations resume.
  2. Monitor query throughput, error logs, and replication status on the new production instance.
  3. Keep the blue standalone instance intact during your initial post-upgrade verification window. After you confirm stability, delete the deployment. For more information, see [Delete a blue-green deployment](https://docs.cloud.google.com/sql/docs/mysql/delete-blue-green-deployment).

**Note:** If an error occurs during the creation of the blue instance after switchover, your new production instance is unaffected and continues serving production traffic. You can restore the blue instance by using the final backup taken of the source instance. Depending on whether the database version changed during the switchover, the backup description is one of the following: 

  * If the major or minor database version changed: `Last backup taken on engine version DATABASE_VERSION (blue-green deployment).`, where DATABASE_VERSION includes the minor version of the source instance.
  * If the database version didn't change: `Last backup taken on source instance (blue-green deployment).`



For more information, see [Restore an instance](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restoring).

## What's next

  * [Delete a blue-green deployment](https://docs.cloud.google.com/sql/docs/mysql/delete-blue-green-deployment) to remove deployment metadata and delete the former blue instance.
  * Learn how to [monitor instances](https://docs.cloud.google.com/sql/docs/mysql/monitoring).
  * Learn about [backup and recovery](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
