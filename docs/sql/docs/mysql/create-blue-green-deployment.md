---
url: https://docs.cloud.google.com/sql/docs/mysql/create-blue-green-deployment/
title: Create and stage a blue-green deployment \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:49.386619+00:00
---

# Create and stage a blue-green deployment  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/create-blue-green-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Create and stage a blue-green deployment Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to create and stage a Cloud SQL blue-green deployment to perform major version upgrades or configuration changes.

## Before you begin

To create and stage a blue-green deployment, verify that you have the required roles and that your source instance meets the deployment prerequisites.

### Required roles and permissions

To get the permissions that you need to create and stage a blue-green deployment, ask your administrator to grant you the following IAM roles on your project:

  * Cloud SQL Editor (`roles/cloudsql.editor`)
  * Cloud SQL Admin (`roles/cloudsql.admin`)



For custom roles, ensure that you have the following permissions:

  * `cloudsql.blueGreenDeployments.create`
  * `cloudsql.blueGreenDeployments.get`
  * `cloudsql.instances.get`
  * `cloudsql.instances.create`
  * `cloudsql.operations.get`



For more information about IAM roles and permissions in Cloud SQL, see [Roles and permissions](https://docs.cloud.google.com/sql/docs/mysql/iam-roles).

### Instance prerequisites

Before creating a blue-green deployment, verify that your production (blue) instance meets the following requirements:

  1. **Database engine and version:** your instance must run Cloud SQL for MySQL version 5.7, 8.0, or 8.4. Version 8.0.18 isn't supported. For major version upgrades, you can upgrade from version 8.0 to 8.4.
  2. **Binary logging and automated backups:** you must enable binary logging and automated backups on the blue instance to establish continuous logical replication to the green environment.
  3. **Instance status:** the blue instance must be in a `RUNNING` state with no ongoing operations or conflicting maintenance windows.
  4. **Unsupported features:** verify that your instance doesn't use any features that aren't supported in blue-green deployments, which include the following:

     * [Outbound connectivity with Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#enable-psc-outbound)
     * [Read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication#read-replicas)
     * [IAM group authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication#iam-group-auth)
  5. **Latest maintenance version:** your instance must run the latest maintenance version before you create a blue-green deployment. For more information, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance).

  6. **Network architecture:** your instance must use the [new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture). Instances that use the old network architecture aren't supported.




When you trigger deployment creation, Cloud SQL automatically runs a series of automated prechecks to validate replication compatibility and flags. For major version upgrades, Cloud SQL also runs the major version upgrade pre-check API on the source instance to validate upgrade readiness before proceeding with the workflow. If prechecks fail, deployment creation stops and returns an error in the operation status.

## Create a blue-green deployment

You can create a blue-green deployment _with intent_ to perform a major version upgrade, or _without intent_ to stage hardware or flag updates.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name.
  3. In the **Configuration** section, click **Create blue green deployment**.
  4. On the **Create Blue Green Deployment** page, in the **Deployment information** section, enter a unique name for the deployment in the **Deployment name** field.
  5. In the **Deployment use case** list, select one of the following options: 
     * **Option A (Major version upgrade):** to stage and test a major version upgrade on the green instance before switchover, select **Major version upgrade**. In the **Target database version** list, select the target database version (for example, **MySQL 8.4**). 

When you create a deployment with intent, Cloud SQL automatically runs the major version upgrade precheck as part of the operation before creating the green instance. Alternatively, we recommend that you run the [major version upgrade precheck](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace#precheck) before creating the deployment to identify any upgrade blockers.

     * **Option B (Default):** to create a green staging environment at the same database version as the source instance to test configuration or hardware changes, select **Default**.
  6. Click **Create**.



### gcloud

To create a blue-green deployment using `gcloud`, run the `blue-green-deployments create` command.

**Option A: Create with intent (major version upgrade)**

When you create a deployment with intent, Cloud SQL automatically runs the major version upgrade precheck as part of the operation before creating the green instance. Alternatively, you can run the [major version upgrade precheck](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace#precheck) on your blue instance before creating the deployment to identify any upgrade blockers.
    
    
    gcloud beta sql blue-green-deployments create DEPLOYMENT_NAME \
      --source-instance=SOURCE_INSTANCE_ID \
      --target-database-version=TARGET_DATABASE_VERSION \
      --region=REGION \
      --async
    

Replace the following:

  * DEPLOYMENT_NAME: a unique name for your deployment.
  * SOURCE_INSTANCE_ID: the name of your blue source instance.
  * TARGET_DATABASE_VERSION: the target version (for example, `MYSQL_8_4`).
  * REGION: the Google Cloud region of your blue instance.



**Option B: Create without intent (hardware or configuration)**

Omit the `--target-database-version` flag to provision a green environment at the same database version as the blue instance:
    
    
    gcloud beta sql blue-green-deployments create DEPLOYMENT_NAME \
      --source-instance=SOURCE_INSTANCE_ID \
      --region=REGION \
      --async
    

Creating a blue-green deployment takes several minutes to complete, especially when performing a major version upgrade. You might see a message indicating that the operation is taking longer than expected. You can either ignore this message or run the [`gcloud sql operations wait`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/wait) command to dismiss the message and wait for the operation to complete:
    
    
    gcloud sql operations wait OPERATION_ID
    

Replace OPERATION_ID with the operation ID returned by the command or displayed in the message.

### REST v1

To create a blue-green deployment using the Cloud SQL Admin API, send a POST request to the `blueGreenDeployments.create` method.

**Option A: Create with intent (major version upgrade)**

When you create a deployment with intent, Cloud SQL automatically runs the major version upgrade precheck as part of the operation before creating the green instance. Alternatively, you can run the [major version upgrade precheck](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace#precheck) on your blue instance before creating the deployment to identify any upgrade blockers.
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/
      locations/REGION/
      blueGreenDeployments?blueGreenDeploymentId=DEPLOYMENT_NAME
    {
      "sourceInstance": "SOURCE_INSTANCE_ID",
      "requestedConfig": {
        "databaseVersion": "TARGET_DATABASE_VERSION"
      }
    }
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the Google Cloud region of your blue instance.
  * DEPLOYMENT_NAME: a unique name for your deployment.
  * SOURCE_INSTANCE_ID: the name of your blue source instance.
  * TARGET_DATABASE_VERSION: the target database version (for example, `MYSQL_8_4`).



**Option B: Create without intent (hardware or configuration)**

Omit the `requestedConfig` field to provision a green environment at the same database version as the blue instance:
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/
      locations/REGION/
      blueGreenDeployments?blueGreenDeploymentId=DEPLOYMENT_NAME
    {
      "sourceInstance": "SOURCE_INSTANCE_ID"
    }
    

### REST v1beta4

To create a blue-green deployment using the Cloud SQL Admin API, send a POST request to the `blueGreenDeployments.create` method.

**Option A: Create with intent (major version upgrade)**

When you create a deployment with intent, Cloud SQL automatically runs the major version upgrade precheck as part of the operation before creating the green instance. Alternatively, you can run the [major version upgrade precheck](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace#precheck) on your blue instance before creating the deployment to identify any upgrade blockers.
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/
      locations/REGION/
      blueGreenDeployments?blueGreenDeploymentId=DEPLOYMENT_NAME
    {
      "sourceInstance": "SOURCE_INSTANCE_ID",
      "requestedConfig": {
        "databaseVersion": "TARGET_DATABASE_VERSION"
      }
    }
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the Google Cloud region of your blue instance.
  * DEPLOYMENT_NAME: a unique name for your deployment.
  * SOURCE_INSTANCE_ID: the name of your blue source instance.
  * TARGET_DATABASE_VERSION: the target database version (for example, `MYSQL_8_4`).



**Option B: Create without intent (hardware or configuration)**

Omit the `requestedConfig` field to provision a green environment at the same database version as the blue instance:
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/
      locations/REGION/
      blueGreenDeployments?blueGreenDeploymentId=DEPLOYMENT_NAME
    {
      "sourceInstance": "SOURCE_INSTANCE_ID"
    }
    

## Monitor deployment status

Creation is a long-running operation (LRO). During staging, Cloud SQL provisions the green instance, upgrades it (if a major version upgrade was requested), and starts continuous logical replication.

Check the progress and status of your blue-green deployment:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name.
  3. Locate the **Blue Green Deployment Status** card to view the status of the deployment.
  4. To view detailed provisioning tasks and progress, click **Details** to open the **Deployment overview** page.



### gcloud

To check the progress and status of your blue-green deployment using `gcloud`, run the `blue-green-deployments describe` command:
    
    
    gcloud beta sql blue-green-deployments describe DEPLOYMENT_NAME \
      --region=REGION
    

Replace the following:

  * DEPLOYMENT_NAME: the name of your blue-green deployment.
  * REGION: the Google Cloud region where the deployment was created.



To wait for the creation operation to complete, run the [`gcloud sql operations wait`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/wait) command:
    
    
    gcloud sql operations wait OPERATION_ID
    

Replace OPERATION_ID with the ID of the creation operation.

### REST v1

To check the progress and status of your blue-green deployment using the Cloud SQL Admin API, send a GET request to the `blueGreenDeployments.get` method:
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/
      locations/REGION/
      blueGreenDeployments/DEPLOYMENT_NAME
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the Google Cloud region where the deployment was created.
  * DEPLOYMENT_NAME: the name of your blue-green deployment.



### REST v1beta4

To check the progress and status of your blue-green deployment using the Cloud SQL Admin API, send a GET request to the `blueGreenDeployments.get` method:
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/
      locations/REGION/
      blueGreenDeployments/DEPLOYMENT_NAME
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the Google Cloud region where the deployment was created.
  * DEPLOYMENT_NAME: the name of your blue-green deployment.



In the command output or the Google Cloud console, monitor the `state` field to track the deployment lifecycle:

  * **`PROVISIONING`:** the green instance is being created, upgraded (if requested), and connected to continuous logical replication.
  * **`SWITCHOVER_READY`:** initial replication has completed and continuous logical replication is active. The deployment is ready for validation, testing, and switchover.
  * **`SWITCHOVER_NOT_READY`:** the deployment is provisioned, but switchover can't be initiated (for example, if replication is broken or an issue is reported in `errorDetail`).



For more information about all deployment lifecycle phases, see [Deployment lifecycle and states](https://docs.cloud.google.com/sql/docs/mysql/about-blue-green-deployments#lifecycle-states).

Wait until the deployment state changes to `SWITCHOVER_READY` before you proceed to describe the deployment, validate your application workloads, or start a switchover.

## What's next

  * [Describe and list blue-green deployments](https://docs.cloud.google.com/sql/docs/mysql/describe-blue-green-deployment) to inspect deployment status and retrieve connection details.
  * [Switchover a blue-green deployment](https://docs.cloud.google.com/sql/docs/mysql/switchover-blue-green-deployment) to convert the green instance to the active production read and write instance.
  * [Delete a blue-green deployment](https://docs.cloud.google.com/sql/docs/mysql/delete-blue-green-deployment) to cancel staging and remove the green environment.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
