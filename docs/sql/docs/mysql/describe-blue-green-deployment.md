---
url: https://docs.cloud.google.com/sql/docs/mysql/describe-blue-green-deployment/
title: Describe and list blue-green deployments \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:38.891783+00:00
---

# Describe and list blue-green deployments  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/describe-blue-green-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Describe and list blue-green deployments Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to list and describe Cloud SQL blue-green deployments, inspect connection details and configuration differences, and connect to the green staging environment to test and validate your workloads.

## Before you begin

To list or describe a blue-green deployment and connect to the green staging instance, verify that you have the required roles and database credentials.

### Required roles and permissions

To get the permissions that you need to list and describe blue-green deployments, ask your administrator to grant you the following IAM roles on your project:

  * Cloud SQL Viewer (`roles/cloudsql.viewer`)
  * Cloud SQL Editor (`roles/cloudsql.editor`)
  * Cloud SQL Admin (`roles/cloudsql.admin`)



For custom roles, ensure that you have the following permissions:

  * `cloudsql.blueGreenDeployments.get`
  * `cloudsql.blueGreenDeployments.list`



To connect to the green staging instance and run test queries, you also need database user credentials configured on the source instance.

For more information about IAM roles and permissions in Cloud SQL, see [Roles and permissions](https://docs.cloud.google.com/sql/docs/mysql/iam-roles).

## Overview

The describe command lets you monitor and track the status of a Cloud SQL blue-green deployment at all times throughout its lifecycle—from initial provisioning and staging through switchover completion.

Describing a blue-green deployment provides visibility into:

  * **Deployment lifecycle state:** monitor the real-time status of your deployment as it transitions through states such as `PROVISIONING`, `SWITCHOVER_READY`, `SWITCHOVER_NOT_READY`, `SWITCHOVER_IN_PROGRESS`, and `SWITCHOVER_COMPLETED`.
  * **Target instance connection details:** retrieve the unique connection name and network endpoints for the green staging instance. This lets database administrators (DBAs) and QA engineers connect applications, run test queries, and validate performance on the green instance without affecting live blue production traffic.
  * **Replication health and switchover readiness:** verify that continuous logical replication from blue to green is healthy and inspect diagnostic error details if issues arise. Note that describing a deployment doesn't show replication lag.
  * **Configuration differences:** when requested with the detailed view, inspect a side-by-side comparison (`diffs`) of database versions, machine tiers, storage settings, and high availability configurations between the blue and green instances.



## List blue-green deployments

To list blue-green deployments in a project:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. In the instances list, view the **Blue green deployment ID** column to see the blue-green deployments associated with your instances. Instances that are part of a blue-green deployment also display a role tag (**Blue** , **Green** , **Old-blue** , or **New-blue**) next to the instance name.



### gcloud

To list blue-green deployments using `gcloud`, run the `blue-green-deployments list` command:
    
    
    gcloud beta sql blue-green-deployments list \
      --region=REGION
    

To list deployments across all regions in your project, omit the `--region` flag.

### REST v1

To list deployments using the Cloud SQL Admin API, send a GET request to the `blueGreenDeployments.list` method:
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/
      locations/REGION/blueGreenDeployments
    

### REST v1beta4

To list deployments using the Cloud SQL Admin API, send a GET request to the `blueGreenDeployments.list` method:
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/
      locations/REGION/blueGreenDeployments
    

## Describe the blue-green deployment

To inspect the deployment status and obtain the green instance connection details, describe the deployment:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Deployment overview** page, do one of the following: 
     * In the **Blue green deployment ID** column, click the deployment ID.
     * Click the instance name to open the **Overview** page, and then in the **Blue Green Deployment Status** card, click **Details**.
  3. On the **Deployment overview** page, review the **Deployment details** card to inspect the deployment **Status** , **Source instance** , **Target instance** , **Target instance endpoint** , and **Target version** , and review the **Deployment progress** card to inspect task statuses.



### gcloud

To describe a deployment using `gcloud`, run the `blue-green-deployments describe` command:
    
    
    gcloud beta sql blue-green-deployments describe DEPLOYMENT_NAME \
      --region=REGION
    

Replace the following:

  * DEPLOYMENT_NAME: the name of your blue-green deployment.
  * REGION: the Google Cloud region where the deployment was created.



### REST v1

To describe a deployment using the Cloud SQL Admin API, send a GET request to the `blueGreenDeployments.get` method:
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/
      locations/REGION/
      blueGreenDeployments/DEPLOYMENT_NAME
    

### REST v1beta4

To describe a deployment using the Cloud SQL Admin API, send a GET request to the `blueGreenDeployments.get` method:
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/
      locations/REGION/
      blueGreenDeployments/DEPLOYMENT_NAME
    

### Inspect status and connection details

In the command output, verify the deployment state and locate the connection information for the target green instance:
    
    
    name: projects/my-project/locations/us-central1/
      blueGreenDeployments/my-deployment
    createTime: '2026-08-13T10:00:00.000Z'
    state: SWITCHOVER_READY
    sourceInstance: my-source-instance
    switchoverTargetInstance: my-target-instance
    requestedConfig:
      databaseVersion: MYSQL_8_4
    deploymentMappings:
    - source:
        connection: my-project:us-central1:my-source-instance
        dns: my-source-instance.123456789012.us-central1.sql.goog.
        instance: projects/my-project/instances/my-source-instance
        ipAddresses:
        - ipAddress: 10.0.0.1
          type: PRIMARY
      state: PROVISIONED
      target:
        connection: my-project:us-central1:my-target-instance
        dns: my-target-instance.123456789012.us-central1.sql.goog.
        instance: projects/my-project/instances/my-target-instance
        ipAddresses:
        - ipAddress: 10.0.0.2
          type: PRIMARY
      tasks:
      - type: PROVISION
        state: SUCCEEDED
        startTime: '2026-08-13T10:00:00.000Z'
        endTime: '2026-08-13T10:15:00.000Z'
    deploymentTasks:
    - type: PROVISION
      state: SUCCEEDED
      startTime: '2026-08-13T10:00:00.000Z'
      endTime: '2026-08-13T10:15:00.000Z'

Review the following fields in the response:

  * **`name`:** the fully qualified resource path of the deployment in the format `projects/PROJECT_ID/locations/REGION/blueGreenDeployments/DEPLOYMENT_NAME`.
  * **`createTime`:** the timestamp when the deployment was created.
  * **`state`:** the overall lifecycle status of the deployment: 
    * `PROVISIONING`: the deployment is provisioning the green environment and setting up replication.
    * `SWITCHOVER_READY`: staging is complete, logical replication is healthy, and the deployment is ready for switchover. Confirm this state before running tests.
    * `SWITCHOVER_NOT_READY`: the deployment is not ready for switchover. Check `errorDetail` for troubleshooting.
    * `SWITCHOVER_IN_PROGRESS`: a switchover operation is actively executing.
    * `SWITCHOVER_COMPLETED`: switchover finished successfully, and the green instance is now serving production traffic as the active read and write instance.
    * `DELETING`: the deployment resource is being deleted.
  * **`sourceInstance`:** the instance identifier of your original blue production instance.
  * **`switchoverTargetInstance`:** the instance identifier of the green staging instance that becomes the production read and write instance during switchover.
  * **`requestedConfig`:** the configuration intended for the target instance at creation time, such as `databaseVersion` for major version upgrades.
  * **`errorDetail`:** diagnostic error details explaining why switchover is not ready or why a provisioning or switchover task failed.
  * **`deploymentMappings`:** the list of source and target instance pairings in the deployment. For each pair, review: 
    * **`source`:** connection and network details for the blue instance, including the instance resource path (`instance`), connection name (`connection`), DNS hostname (`dns`), and IP addresses (`ipAddresses`).
    * **`target`:** connection and network details for the green instance. Use the target `connection` name or `ipAddresses` to connect staging applications and test suites to the green environment.
    * **`diffs`:** differences in configuration between the blue and green instances when using the detailed view. During Preview, database flag changes aren't shown.
    * **`state`:** the operational status of the paired node (such as `PROVISIONING`, `PROVISIONED`, `UPGRADING`, `UPGRADED`, `UPGRADE_FAILED`, `SWITCHOVER_IN_PROGRESS`, `SWITCHOVER_FAILED`, `SWITCHOVER_SUCCEEDED`, or `DELETING`).
    * **`tasks`:** the execution status, start time, end time, and error details for deployment tasks performed on this node.
  * **`deploymentTasks`:** a consolidated list of all deployment tasks across all nodes, including task `type` (`PROVISION`, `UPGRADE`, `SWITCHOVER`, `DELETE`, or `POST_SWITCHOVER_OPERATIONS`), `state` (`PENDING`, `RUNNING`, `SUCCEEDED`, or `FAILED`), `startTime`, `endTime`, and `errorMessage`.



## View configuration differences

By default, describing a deployment returns the basic view with core metadata. To review configuration differences between the blue and green instances, view the setting differences in the Google Cloud console or request the detailed view using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the Cloud SQL Admin API:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name.
  3. In the **Blue Green Deployment Status** card, click **Details** to open the **Deployment overview** page.
  4. In the **Deployment details** card, click **View setting differences**.
  5. In the **Instance Setting Differences** dialog, review the comparison between the **Source** and **Target** instances, and then click **Close**.



### gcloud

Run the `blue-green-deployments describe` command with the `--show-config-diff` flag:
    
    
    gcloud beta sql blue-green-deployments describe DEPLOYMENT_NAME \
      --region=REGION \
      --show-config-diff
    

### REST v1

Send a GET request to the `blueGreenDeployments.get` method with the `view=DETAILED` query parameter:
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/
      locations/REGION/
      blueGreenDeployments/DEPLOYMENT_NAME?view=DETAILED
    

### REST v1beta4

Send a GET request to the `blueGreenDeployments.get` method with the `view=DETAILED` query parameter:
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/
      locations/REGION/
      blueGreenDeployments/DEPLOYMENT_NAME?view=DETAILED
    

### Review configuration differences

When you specify the detailed view, the response includes a `diffs` section within each paired node under `deploymentMappings`:
    
    
    deploymentMappings:
    - diffs:
      - field: database_version
        sourceValue: MYSQL_8_0
        targetValue: MYSQL_8_4
      - field: settings/tier
        sourceValue: db-custom-2-7680
        targetValue: db-custom-4-15360
      source:
        instance: projects/PROJECT_ID/instances/my-source-instance
      target:
        connection: PROJECT_ID:REGION:my-target-instance
        instance: projects/PROJECT_ID/instances/my-target-instance

The `diffs` section highlights differences between the source and target instances for attributes such as:

  * **`database_version`:** the database engine version on the blue versus green instances.
  * **`settings/tier`:** machine type (vCPU and memory) allocated to the instance.
  * **`edition`:** the Cloud SQL edition (Cloud SQL Enterprise edition or Cloud SQL Enterprise Plus edition).
  * **`availability_type`:** high availability (HA) configuration (`ZONAL` or `REGIONAL`).
  * **`settings/data_disk_size_gb`:** storage capacity in gigabytes.
  * **`settings/data_disk_type`:** storage type (`PD_SSD`).

**Note:** During Preview, configuration differences between the source and target instances don't show database flag changes. 

Confirm that all listed changes match your planned deployment specifications before you begin functional workload testing.

## Connect and validate application workloads

Connect your application or client tools to the green instance using its unique connection string:
    
    
    gcloud sql connect TARGET_INSTANCE_NAME --user=DB_USER
    

Replace the following:

  * TARGET_INSTANCE_NAME: the name of your target green instance.
  * DB_USER: the database username.



Perform the following validation steps:

  * **Run integration tests:** verify that application queries and stored procedures run without error on the green instance.
  * **Inspect error logs:** check Cloud Logging and Cloud SQL database error logs for deprecated syntax warnings or unexpected engine errors.
  * **Review performance stats:** monitor CPU, memory, and I/O metrics on the green instance to ensure performance meets operational SLOs.



## What's next

  * If validation is successful and the green instance meets all functional and performance criteria, proceed to [Switchover a blue-green deployment](https://docs.cloud.google.com/sql/docs/mysql/switchover-blue-green-deployment).
  * If you detect issues during validation, you can safely [delete the blue-green deployment](https://docs.cloud.google.com/sql/docs/mysql/delete-blue-green-deployment) without affecting your live blue environment.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
