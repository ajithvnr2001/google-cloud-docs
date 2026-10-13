---
url: https://docs.cloud.google.com/sql/docs/mysql/delete-blue-green-deployment/
title: Delete a blue-green deployment \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:18.783728+00:00
---

# Delete a blue-green deployment  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/delete-blue-green-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Delete a blue-green deployment Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to delete a Cloud SQL blue-green deployment, and details the critical difference in deletion behavior before and after switchover.

## Before you begin

To delete or cancel a blue-green deployment, verify that you have the required roles and permissions.

### Required roles and permissions

To get the permissions that you need to delete a blue-green deployment, ask your administrator to grant you the following IAM role on your project:

  * Cloud SQL Admin (`roles/cloudsql.admin`)



For custom roles, ensure that you have the following permissions:

  * `cloudsql.blueGreenDeployments.delete`
  * `cloudsql.blueGreenDeployments.get`
  * `cloudsql.instances.delete`
  * `cloudsql.operations.get`



For more information about IAM roles and permissions in Cloud SQL, see [Roles and permissions](https://docs.cloud.google.com/sql/docs/mysql/iam-roles).

## Understanding deletion behaviors

The `delete` operation behaves differently depending on whether switchover has occurred:

Deployment stage | Default behavior | Instance impact  
---|---|---  
**Before switchover**  
(Cancel) | Deletes the deployment metadata and automatically deletes the green staging instance. | Your blue production instance remains running and completely unaffected.  
**After switchover**  
(Delete) | Deletes the deployment metadata, but _retains both instances_ as standalone instances by default. | The green instance continues serving production traffic as your active read and write database instance. The blue instance is retained as a standalone read and write instance unless you select the **Delete old source instance** option, pass the optional `--delete-old-source` flag, or set the `deleteOldSource` parameter to `true` to delete it.  
  
## Case 1: Cancel a deployment before switchover

If you detect issues during validation or decide not to proceed with an upgrade, delete the deployment before triggering switchover.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name.
  3. In the **Blue Green Deployment Status** card, click **Details** to open the **Deployment overview** page.
  4. Click **Delete deployment**.
  5. In the **Delete Deployment?** dialog, enter the deployment ID in the **Deployment ID** field to confirm.
  6. Click **Delete**.



### gcloud

To cancel and delete a blue-green deployment using `gcloud`, run the `blue-green-deployments delete` command:
    
    
    gcloud beta sql blue-green-deployments delete DEPLOYMENT_NAME \
      --region=REGION
    

Replace the following:

  * DEPLOYMENT_NAME: the name of your blue-green deployment.
  * REGION: the Google Cloud region where the deployment was created.



### REST v1

To cancel and delete a blue-green deployment using the Cloud SQL Admin API, send a DELETE request to the `blueGreenDeployments.delete` method:
    
    
    DELETE https://sqladmin.googleapis.com/v1/
      projects/PROJECT_ID/locations/REGION/
      blueGreenDeployments/DEPLOYMENT_NAME
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the Google Cloud region where the deployment was created.
  * DEPLOYMENT_NAME: the name of your blue-green deployment.



### REST v1beta4

To cancel and delete a blue-green deployment using the Cloud SQL Admin API, send a DELETE request to the `blueGreenDeployments.delete` method:
    
    
    DELETE https://sqladmin.googleapis.com/sql/v1beta4/
      projects/PROJECT_ID/locations/REGION/
      blueGreenDeployments/DEPLOYMENT_NAME
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the Google Cloud region where the deployment was created.
  * DEPLOYMENT_NAME: the name of your blue-green deployment.



This removes the green staging instance and restores your environment to its original single-instance state without downtime.

## Case 2: Delete post-switchover

After a successful switchover and verification window, you can delete the deployment along with the former blue instance to stop incurring charges on two instances.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name.
  3. In the **Blue Green Deployment Status** card, click **Details** to open the **Deployment overview** page.
  4. Click **Delete deployment**.
  5. In the **Delete Deployment?** dialog, enter the deployment ID in the **Deployment ID** field to confirm.
  6. Choose whether to delete or retain the former blue instance: 
     * **Option A (Delete the deployment and former blue instance):** select the **Delete old source instance** checkbox.
     * **Option B (Delete deployment metadata only):** leave the **Delete old source instance** checkbox cleared to retain the former blue instance as a standalone instance.
  7. Click **Delete**.



### gcloud

To delete a blue-green deployment using `gcloud`, run the `blue-green-deployments delete` command.

**Option A: Delete the deployment and former blue instance**

To delete the deployment metadata and automatically delete the former blue instance, pass the optional `--delete-old-source` flag:
    
    
    gcloud beta sql blue-green-deployments delete DEPLOYMENT_NAME \
      --region=REGION \
      --delete-old-source
    

Replace the following:

  * DEPLOYMENT_NAME: the name of your blue-green deployment.
  * REGION: the Google Cloud region where the deployment was created.



When prompted, confirm that you want to permanently delete the former blue instance.

**Option B: Delete deployment metadata only (retain the former blue instance)**

If you want to keep the former blue instance running as a standalone instance (for example, as a backup or for historical analytical queries), omit the optional `--delete-old-source` flag:
    
    
    gcloud beta sql blue-green-deployments delete DEPLOYMENT_NAME \
      --region=REGION
    

Replace the following:

  * DEPLOYMENT_NAME: the name of your blue-green deployment.
  * REGION: the Google Cloud region where the deployment was created.



This command only deletes the blue-green deployment metadata, leaving both instances as standalone instances until you manually delete the former blue instance. Both instances remain active in your project, and you continue to be billed for both.

### REST v1

To delete a blue-green deployment using the Cloud SQL Admin API, send a DELETE request to the `blueGreenDeployments.delete` method.

**Option A: Delete the deployment and former blue instance**

To delete the deployment metadata and automatically delete the former blue instance, set the `deleteOldSource` query parameter to `true`:
    
    
    DELETE https://sqladmin.googleapis.com/v1/
      projects/PROJECT_ID/locations/REGION/
      blueGreenDeployments/DEPLOYMENT_NAME?deleteOldSource=true
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the Google Cloud region where the deployment was created.
  * DEPLOYMENT_NAME: the name of your blue-green deployment.



**Option B: Delete deployment metadata only (retain the former blue instance)**

If you want to keep the former blue instance running as a standalone instance (for example, as a backup or for historical analytical queries), omit the `deleteOldSource` query parameter:
    
    
    DELETE https://sqladmin.googleapis.com/v1/
      projects/PROJECT_ID/locations/REGION/
      blueGreenDeployments/DEPLOYMENT_NAME
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the Google Cloud region where the deployment was created.
  * DEPLOYMENT_NAME: the name of your blue-green deployment.



This request only deletes the blue-green deployment metadata, leaving both instances as standalone instances until you manually delete the former blue instance. Both instances remain active in your project, and you continue to be billed for both.

### REST v1beta4

To delete a blue-green deployment using the Cloud SQL Admin API, send a DELETE request to the `blueGreenDeployments.delete` method.

**Option A: Delete the deployment and former blue instance**

To delete the deployment metadata and automatically delete the former blue instance, set the `deleteOldSource` query parameter to `true`:
    
    
    DELETE https://sqladmin.googleapis.com/sql/v1beta4/
      projects/PROJECT_ID/locations/REGION/
      blueGreenDeployments/DEPLOYMENT_NAME?deleteOldSource=true
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the Google Cloud region where the deployment was created.
  * DEPLOYMENT_NAME: the name of your blue-green deployment.



**Option B: Delete deployment metadata only (retain the former blue instance)**

If you want to keep the former blue instance running as a standalone instance (for example, as a backup or for historical analytical queries), omit the `deleteOldSource` query parameter:
    
    
    DELETE https://sqladmin.googleapis.com/sql/v1beta4/
      projects/PROJECT_ID/locations/REGION/
      blueGreenDeployments/DEPLOYMENT_NAME
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the Google Cloud region where the deployment was created.
  * DEPLOYMENT_NAME: the name of your blue-green deployment.



This request only deletes the blue-green deployment metadata, leaving both instances as standalone instances until you manually delete the former blue instance. Both instances remain active in your project, and you continue to be billed for both.

## What's next

  * Review [about blue-green deployments](https://docs.cloud.google.com/sql/docs/mysql/about-blue-green-deployments) to understand deployment architecture and lifecycle states.
  * Explore [in-place major version upgrades](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace).
  * Learn about configuring [high availability](https://docs.cloud.google.com/sql/docs/mysql/high-availability).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
