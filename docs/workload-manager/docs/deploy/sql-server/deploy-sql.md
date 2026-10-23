---
url: https://docs.cloud.google.com/workload-manager/docs/deploy/sql-server/deploy-sql/
title: Deploy a SQL Server workload \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:44.842284+00:00
---

# Deploy a SQL Server workload  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/deploy/sql-server/deploy-sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Deploy a SQL Server workload Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to deploy a SQL Server workload on Google Cloud by using the Guided Deployment Automation tool in Workload Manager.

## Configure SQL Server deployment

To configure and deploy a SQL Server workload, perform the following tasks:

  1. In the Google Cloud console, go to the **Workload Manager** page.

[Go to Workload Manager](https://console.cloud.google.com/workload-manager)

  2. In the **Workload Manager** navigation pane, click **Deployments**.

  3. Select the project in which you want to create the deployment.

  4. Click **Create Deployment** and choose **SQL Server**.

  5. In the **Deployment basics** section, enter the following information about your deployment and workload requirements.

Workload Manager uses this basic information to determine the data to be collected in the subsequent tabs. Workload Manager also provides recommendations for your deployment configuration based on the basic settings:

     1. Enter a name to describe the workload you are deploying. For example, `sqlserver-prod-1`. This name must be unique in the project where you're deploying the workload.

You can use lowercase alphanumeric characters and hyphens to specify the name, but it must start with a letter and must not end with a hyphen. It can have minimum of 3 and maximum of 22 characters.

     2. In the **Deployment description** field, add a description for your workload, which is later displayed on the dashboard that shows your deployments.

     3. In the **Service account** field, select a service account that you want to attach to the deployment. Workload Manager uses this service account to call other APIs and services for creating resources required for the deployment. You can either select an existing service account or create a new service account.

**Note:** If the service account is missing any of the required roles for creating a deployment, Workload Manager prompts you to grant these roles. Click **Grant** to grant the missing roles to the attached service account.
     4. Select whether the workload is intended for production use or non-production use. Note: Certain default values are used in the tool based on the environment selection.

     5. Select the operating system. Workload Manager supports deploying SQL Server only on VMs that run Windows operating system.

     6. Select the licensing type for Windows from the following options:

        * Bring your own license (BYOL)
        * Pay as you go (PAYG)
     7. Select the licensing type for SQL Server from the following options:

        * Bring your own license (BYOL)
        * Pay as you go (PAYG)
     8. Select the OS image from public or custom images.

     9. Select the deployment strategy:

        * Single node: each SQL Server instance is deployed on its own VM
        * High availability: highly available SQL Server cluster is deployed across multiple zones
     10. Select the availability mode:

        * Availability group (AG)
        * Failover cluster instance (FCI)
  6. In the **VM name prefix** field, enter a prefix that is applied to the names of all VMs created during the deployment. A maximum of seven characters are allowed for the prefix.

  7. In the **Software installation media bucket** field, select the Cloud Storage bucket that holds the SQL Server installation media you uploaded. The bucket must exist within the project in which you're creating the deployment.

For more information, see [Prepare SQL Server installation files for deployment](https://docs.cloud.google.com/workload-manager/docs/deploy/sql-server/prerequisites-sql#install-files).

  8. Click **Continue** to proceed.

  9. In the **Location & networking** tab, enter the following.

     1. Select the Google Cloud project in which you want to deploy the workload.
     2. Select the Google Cloud region in which you want to deploy the workload.
     3. Select a zone from the specified region.
     4. Select a zone from the specified region for deploying the secondary system. This field is visible only if you have specified HA as the deployment model in the basics section.
     5. Select the Virtual Private Cloud (VPC) network into which you're deploying the workload.
     6. Select the subnet in the specified VPC network where you want to deploy the workload.
     7. Select a method for providing external internet access to the VMs. For more information, see [Prerequisites](https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites#network%22%3EPrerequisites). 
        * Cloud NAT: If you want to provide external internet access using a Cloud NAT gateway that you have already created for the specified network.
        * Allow External IP: If you want to provide external internet access by reserving a static external IP address on each VM.
     8. Select **Create a new DNS zone**. Workload Manager automatically creates a DNS to allow communication between VMs in the deployment.
  10. Click **Continue**.

  11. In the **Active Directory** tab, enter the following.

     1. Select the [Secret Manager name](https://docs.cloud.google.com/secret-manager) that corresponds to the password for the username specified in the **Domain username** field to connect to Active Directory. Workload Manager uses this password throughout the deployment and installation process. This secret must exist in the Google Cloud project in which you create the deployment.
     2. Specify the name of the Active Directory user account used to join the VMs to the Active Directory domain.
     3. Specify the IP address of the Active Directory node.
     4. Specify the Active Directory domain DNS name.
  12. Click **Continue**.

  13. In the **Database** tab, enter the following information:

     1. Select the [Secret Manager name](https://docs.cloud.google.com/secret-manager) that corresponds to the password used for the database.
     2. Select the tenancy model from the following options: 
        * Shared
        * Sole tenant Note: The shared tenancy option is not available for Windows BYOL licenses.
     3. Select a machine family for the database VMs.
     4. Select a machine type for the database VMs.
     5. Select the type of block storage for the VM.
     6. Select the **SMT off** option to turn on or turn off simultaneous multithreading, which is also called as hyper-threading.
     7. Select the **TempDB on local SSD** option to use a local SSD to store TempDB.
  14. To review the deployment configuration, click **Continue**.

  15. To deploy the SQL Server workload, click **Create**.




## Review the deployment status

After you click **Create** , you see the Deployment dashboard, where you can monitor the status of your deployment. You can monitor the status of the deployment by hovering over the **Status** icon.

You receive a notification in the Google Cloud console when Workload Manager completes the deployment process. If the deployment is not successful, you receive a failure notification. You can view additional information about the error on the Deployment Details page by clicking the deployment name on the dashboard. See Troubleshoot deployment errors.

**Note:** The entire deployment process might take up to two or three hours to complete. The deployment process continues in the background. After you receive the notification, you can check the deployment dashboard.

## Troubleshoot deployment errors

If the error occurred during the Terraform file creation, then follow these steps:

  * If the underlying issue requires changing the configuration, for example, if deployment name or VM prefix was not unique, then do the following: 
    1. Delete the deployment.
    2. Make a new deployment using the correct configuration.
  * If the underlying issue does not require changing the configuration, for example, quota issues: 
    1. Fix the issue.
    2. Click **Retry** on the error message to resume the deployment process.



If the error occurred during the PowerShell Desired State Configuration (DSC) file creation:

  * If the underlying issue requires changing the configuration, for example, the wrong software bucket was chosen: 
    1. Delete the deployment.
    2. Create a new deployment using the correct configuration.
  * If the underlying issue does not require changing the configuration, for example, the OS package failed to download: 
    1. Resolve the underlying problem, if applicable.
    2. Stop and start the Ansible Runner VM named VM_PREFIX-ansible-runner from the Compute Engine dashboard. VM_PREFIX is the prefix you specified for all VMs in your deployment. This process restarts the Ansible creation for the deployment.



## What's next

  * [Perform the post-deployment tasks](https://docs.cloud.google.com/workload-manager/docs/deploy/post-deployment).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
