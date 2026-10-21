---
url: https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/deploy-oracle/
title: Deploy an Oracle Database workload \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:36.960267+00:00
---

# Deploy an Oracle Database workload  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/deploy-oracle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Deploy an Oracle Database workload Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to deploy an Oracle Database workload on Google Cloud by using the Guided Deployment Automation tool in Workload Manager.

## Create an Oracle Database deployment

To configure and deploy an Oracle Database, perform the following tasks:

  1. In the Google Cloud console, go to the **Workload Manager** page.

[Go to Workload Manager](https://console.cloud.google.com/workload-manager)

  2. In the **Workload Manager** navigation pane, click **Deployments**.

  3. Select the project in which you want to create the deployment.

  4. Click **Create deployment** and choose **Oracle Database**.

  5. If you don't have the required roles and permissions, the Guided Deployment Automation tool indicates the required roles and permissions. Click **Grant and continue**.

  6. In the **Deployment basics** section, enter information about your deployment and workload requirements.

Workload Manager uses this basic information to determine the data to be collected in the subsequent tabs. Workload Manager also provides recommendations for your deployment configuration based on these basic settings.

     1. Enter a name to describe the workload that you are deploying.

This name must be unique in the project in which you're deploying the workload. You can use lowercase alphanumeric characters and hyphens to specify the name, but it must start with a letter and must not end with a hyphen. It can have a minimum of 3 and a maximum of 22 characters.

     2. In the **Deployment description** field, add a description for your workload, which is later displayed on the dashboard that shows your deployments.

     3. In the **Service account** field, select a service account that you want to attach to your Oracle deployment. Workload Manager uses this service account to call other APIs and services for creating resources required for the deployment. You can either select an existing service account or create a new one. For more information, see [User-managed service account](https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites#user-service-account).

**Note:** If the service account is missing any of the required roles for creating a deployment, Workload Manager prompts you to grant these roles. Click **Grant** to grant the missing roles to the attached service account.
     4. In the **Service account for Compute Engine** field, select a service account for the Compute Engine VMs that are created during the deployment process. You can either select an existing service account or create a new service account.

**Note:** If the service account is missing any of the required roles for creating a deployment, Workload Manager prompts you to grant these roles. Click **Grant** to grant the missing roles to the attached service account.
     5. Optional: This step is required only if your organization enforces [VPC Service Controls](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls) compliance. In the **Private pool** field, specify the name of a Cloud Build private pool that is configured for VPC Service Controls in the following format:

**Note:** The private pool must be in the same primary region in which you plan to create your database VM.
            
            projects/PRIVATEPOOL_PROJECT_ID/locations/REGION/workerPools/PRIVATEPOOL_ID
            

Replace the following:

        * PRIVATEPOOL_PROJECT_ID: the ID of the project that contains the private pool.
        * REGION: the region where you created the private pool.
        * PRIVATEPOOL_ID: the ID of the private pool.

For more information, see [Use a Cloud Build private worker pool](https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites#vpc-sc-pool).

     6. Select an Oracle Database **Release** version.

Workload Manager supports Oracle Database Enterprise Edition and release version 19c.

     7. Select a **Release update**.

If you want to use a Developer license, Oracle Database 19c (19.3) is the only version available, in which case select `19.3` update from the **Release update** menu.

**Note:** Oracle Database 19c (19.3) is a 2019 release and has known security vulnerabilities.
     8. Select a deployment model:

        * **Single instance** : In this model, your Oracle Database is deployed on a single VM.
        * **Oracle Data Guard high availability** : Oracle instances are deployed across multiple VMs using maximum availability protection mode for high availability. For more information, see [Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/21/sbydb/oracle-data-guard-protection-modes.html#GUID-16298839-9B8A-4E58-8EC9-27912E57F1CE).
     9. In the **Secret for Database credentials** field, select the name of the secrets that corresponds to the password for your Oracle Database. Guided Deployment Automation tool uses this password throughout the deployment and installation process. This secret must meet the [password complexity requirements](https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/prerequisites-oracle#secrets) and must exist in the same Google Cloud project in which you create the deployment.

**Note:** By default, the Guided Deployment Automation tool selects the latest version of your secret. Make sure that the latest version of your secret meets the password complexity requirements as well.
     10. Enter a **Database name**.

Database name must contain only letters, numbers, and underscores. It can have a maximum of 8 characters.

     11. Enter a **Database domain name**.

Database domain name can either be empty, or have a name that starts with a letter and contains only letters, digits, underscores, hyphens, and periods. It can be between 1 and 128 characters long.

     12. Optional. To enable Oracle Multitenant, select the **Enable multitenant** checkbox.

Oracle Multitenant architecture allows a single container database to host multiple isolated pluggable databases, enabling efficient resource consolidation and simplified management. For more information, see [Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/multi/introduction-to-the-multitenant-architecture.html#GUID-267F7D12-D33F-4AC9-AA45-E9CD671B6F22).

     13. Optional. Enable database monitoring.

Enabling database monitoring configures metric collection to help you monitor the health of your databases. For a list of metrics that are collected, see [Supported metrics](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-oracle#supported-oracle-metrics).

The collected metrics are sent to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) where you can view the metrics using dashboards and set up alerts. For more information, see [View the metrics](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-oracle#view-oracle-metrics).

     14. If you choose to enable database monitoring, select a **secret name for monitoring credentials**. This secret must meet the [password complexity requirements](https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/prerequisites-oracle#secrets) and must exist in the same Google Cloud project in which you create the deployment.

**Note:** By default, the Guided Deployment Automation tool selects the latest version of your secret. Make sure that the latest version of your secret meets the password complexity requirements as well.
  7. Click **Continue** to proceed.

  8. In the **Virtual machine** tab, do the following:

     1. Select the primary region in which you want to create the VM.

**Note:** Your VM and private pool must be in the same primary region.

For more information, see [Supported regions](https://docs.cloud.google.com/workload-manager/docs/deploy/locations).

     2. Select a primary zone from the specified region.

     3. Select a secondary region and a secondary zone.

These options are available only if you selected the **Oracle Data Guard high availability** deployment model in the **Deployment basics** tab.

     4. Select your VPC network.

     5. Select the subnet in the specified VPC network.

     6. Select a secondary subnet. This option is available only if your primary and secondary regions are different.

     7. To set a custom **VM name prefix** , enter a prefix to be applied to the names of all VMs created during the deployment. The prefix must be between 3 and 32 characters.

By default, the **VM name prefix** is set the same as the name of your deployment.

     8. In the **Software installation media** field, select the [Cloud Storage bucket](https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/prerequisites-oracle#storage-bucket) that you created to host your installation files.

Because the bucket is empty and doesn't have any files yet, you see an error that indicates the missing files for the release update you selected in the **Deployment basics** section. Do the following:

        1. Download the missing files to your local machine:

           * Download patches (files starting with 'p') from [My Oracle Support](https://support.oracle.com/).
           * Download base releases from [Oracle Software Delivery Cloud](https://edelivery.oracle.com/) or [Oracle Technology Network](https://www.oracle.com/database/technologies/oracle-database-software-downloads.html).

**Note:** Both **My Oracle Support** and **Oracle Software Delivery Cloud** require Oracle support entitlements. If you want to use a Developer license, Oracle Database 19c (19.3) is the only version available without support entitlement. However, it's a 2019 release and has known security vulnerabilities.
        2. [Upload the files to your bucket](https://docs.cloud.google.com/storage/docs/uploading-objects#uploading-an-object).

        3. Once again, in the **Software installation media** field, select the [Cloud Storage bucket](https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/prerequisites-oracle#storage-bucket). The Guided Deployment Automation tool validates your files, and if there's no error, then you can proceed with the next steps.

     9. Select a machine series for the database VMs.

     10. Select a machine type for the database VMs.

  9. Click **Continue** to proceed.

  10. In the **Storage** tab, enter the information for creating storage disks.

The deployment process creates four storage volumes. Adjust the initial volume sizes based on expected usage.

     1. **Boot disk** : contains the operating system and all the essential files required to start the server. You can provision between 20 GB and 65,536 GB of storage.
     2. **Software binaries disk** : holds Oracle software files and `ORACLE_HOME` directory. You can provision between 30 GB and 65,536 GB of storage.
     3. **Datafiles disk** : stores the database itself, including the Oracle data dictionary and user data. You can provision between 10 GB and 65,536 GB of storage.
     4. **Fast recovery area disk** : stores recovery-related files, such as archived redo logs and local RMAN backups. You can provision between 15 GB and 65,536 GB storage.
  11. To review the deployment configuration, click **Continue**.

In the **Review** tab, Guided Deployment Automation tool validates your deployment configuration against your available quota, and indicates if there's insufficient quota. If that happens, you can either reconfigure your deployment to match your existing quota, or increase the quota by following these steps:

     1. Click **Request quota increase**.
     2. On the **Quota changes** page, update the quota values as per your requirement.
     3. Click **Done**.
     4. Click **Submit request**.
  12. To deploy the Oracle database workload, click **Create**.




## Review the deployment status

After you create the deployment, you can monitor the status of the deployment on the dashboard by hovering the mouse over the **Status** icon.

You receive a notification in the Google Cloud console when Workload Manager completes the deployment process. If the deployment is not successful, you receive a failure notification. You can view additional information about the error on the **Deployment Details** page by clicking the deployment name on the dashboard. See Troubleshoot deployment errors.

**Note:** The entire deployment process can take up to two to three hours to complete. The deployment process continues in the background. You can check the deployment dashboard once you receive the notification.

## Troubleshoot deployment errors

During the deployment process, Terraform creates the Google Cloud resources, such as the VMs and storage disks, and Ansible configures the Oracle software on the VMs. Workload Manager provides logs for both Terraform and Ansible through Cloud Build and Logs Explorer, respectively.

When an error occurs during the deployment process, you receive a notification in the Google Cloud console. You can view additional error details on the **Deployment Details** page, including the root cause, a link to the logs containing additional information, and steps to resolve the error.

If the error occurred during the Terraform process of the deployment:

  * If the underlying issue requires changing the deployment configuration (for example, deployment name was not unique):

    1. [Delete the deployment](https://docs.cloud.google.com/workload-manager/docs/deploy/delete).
    2. Create a new deployment by providing the correct information.
  * If the underlying issue does not require changing the deployment configuration (for example, insufficient quota):

    1. Resolve the issue.
    2. Click **Retry** on the error message to resume the deployment process.

**Note:** The **Retry** option is available only for the errors that occur during the Terraform process and don't require changing the deployment configuration.



If the error occurred during the Ansible process of the deployment:

  * If the underlying issue requires changing the deployment configuration (for example, you specified the wrong Cloud Storage bucket for Oracle Database files):

    1. [Delete the deployment](https://docs.cloud.google.com/workload-manager/docs/deploy/delete).
    2. Create a new deployment by providing the correct configuration.
  * If the underlying issue does not require changing the deployment configuration (for example, OS package failed to download):

    1. Resolve the issue, if applicable.
    2. [Delete the deployment](https://docs.cloud.google.com/workload-manager/docs/deploy/delete).
    3. Create a new deployment by providing the correct configuration.



## What's next

  * [Perform the post-deployment tasks](https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/post-deployment).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
