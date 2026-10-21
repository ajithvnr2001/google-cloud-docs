---
url: https://docs.cloud.google.com/workload-manager/docs/deploy/sap/deploy-sap/
title: Deploy an SAP S/4HANA application \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:20.566887+00:00
---

# Deploy an SAP S/4HANA application  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/deploy/sap/deploy-sap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Deploy an SAP S/4HANA application Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to deploy an SAP S/4HANA application on Google Cloud by using the Guided Deployment Automation tool in Workload Manager.

## Deploy an SAP S/4HANA application

To configure and deploy an SAP S/4HANA workload, perform the following tasks:

  1. In the Google Cloud console, go the **Workload Manager** page.

[Go to Workload Manager](https://console.cloud.google.com/workload-manager)

  2. In the **Workload Manager** navigation pane, click **Deployments**.

  3. Select the project in which you want to create the deployment.

  4. Click **Create deployment** and choose **SAP**.

  5. In the **Deployment basics** section, enter information about your deployment and workload requirements. Workload Manager uses this basic information to determine the data to be collected in the subsequent tabs. Workload Manager also provides recommendations for your deployment configuration based on these basic settings.

**Field** | **Description**  
---|---  
**Name** | Enter a name to describe the workload you are deploying.  
  
Example: "S4-Prod-EP1"  
  
This name must be unique in the current project and is involved in naming some resources that are deployed. A maximum of 25 characters is allowed.  
**Description** | Optional: An additional field that describes your workload. This description is displayed on the dashboard for your deployment.  
  6. In the **Service account** field, select a service account that you want to attach to the deployment. Workload Manager uses this service account to call other APIs and services for creating resources required for the deployment. You can either select an existing service account or create a new service account.

     1. Click **New service account** to create a new service account for your deployment. The **Create service account** page opens. Enter the details of the service account and grant the required roles for deployment.

For more information about the required roles, see [Service accounts](https://docs.cloud.google.com/workload-manager/docs/deploy/sap/prerequisites-sap#service-accounts).

     2. Click **Refresh list** to populate the new service account in the list of service accounts.

**Note:** If the service account is missing any of the required roles for creating a deployment, Workload Manager prompts you to grant these roles. Click **Grant** to grant the missing roles to the attached service account.
  7. In the **Ansible Runner service account** section, select a service account for the temporary Ansible Runner VM created during the deployment process. You can either create a service account or choose an existing service account with the required IAM permissions. For more information, see [Service accounts and permissions](https://docs.cloud.google.com/workload-manager/docs/deploy/sap/prerequisites-sap#service-accounts).

  8. Optional: This step is required only if your organization enforces VPC Service Controls compliance. In the **Private pool** field, specify the name of a Cloud Build private pool that is configured for VPC Service Controls in the following format:
         
         projects/PRIVATEPOOL_PROJECT_ID/locations/REGION/workerPools/PRIVATEPOOL_ID
         

Replace the following:

     * PRIVATEPOOL_PROJECT_ID: the ID of the project that contains the private pool
     * REGION: the region where you created the private pool
     * PRIVATEPOOL_ID: the ID of the private pool

For more information, see [Use a Cloud Build private worker pool](https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites#vpc-sc-pool).

  9. In the **Product information** section, enter the details of your SAP system and the deployment model. See [Supported SAP workloads](https://docs.cloud.google.com/workload-manager/docs/deploy/about-wlm-deployment#supported-system). 

**Field** | **Description**  
---|---  
**SAP application** | Select the SAP product to install.  
**SAP version** | Select the version of the specified SAP application.  
**Environment type** | Select whether the workload is intended for production use or non-production use.  
**Deployment model** | Select a deployment model:  

     * **Distributed with high availability** : recommended for production systems and other critical workloads to achieve the highest availability.
     * **Distributed** : suitable for non-production workloads where availability is not critical to achieve lower cost.  
**HANA scaling method** | Select the scaling method for the database.  
  10. In the **VM name prefix** field, enter a prefix that is applied to the names of all VMs created during the deployment. A maximum of seven characters are allowed for the prefix.

  11. In the **Software installation media bucket** field, select the Cloud Storage bucket that holds the SAP installation media you uploaded. The bucket must exist within the project in which you're creating the deployment.

For more information, see [Prepare SAP installation files for deployment](https://docs.cloud.google.com/workload-manager/docs/deploy/sap-install-files).

  12. Click **Continue** to proceed.

  13. In the **Location & networking** tab, enter the following.

**Field** | **Description**  
---|---  
**Project name** | Select the Google Cloud project in which you want to deploy the workload.  
**Region** | Select the Google Cloud region in which you want to deploy the workload.  
**Primary zone** | Select a zone from the specified region.  
**Secondary zone** | Select a zone from the specified region for deploying the secondary system.  
This field is visible only if you've specified high availability (HA) as the deployment model in the basics section.   
**Network** | Select the Virtual Private Cloud (VPC) network into which you're deploying the workload  
**Subnet** | Select the subnet in the specified VPC network where you want to deploy the workload.  
**Internet access** | Select a method for providing external internet access to the VMs. For more information, see [Prerequisites](https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites#network).  

     * **Cloud NAT:** If you want to provide external internet access using a Cloud NAT gateway that you've already created for the specified network.
     * **Allow External IP:** If you want to provide external internet access by reserving a static external IP address on each VM.  
**Skip automatic firewall setup** | To disable automatic firewall rule creation, select this checkbox. If you skip the firewall rule creation, verify that your network's firewall rules enable communication between the VMs in the deployment. For more information, see [Firewall rules](https://docs.cloud.google.com/workload-manager/docs/deploy/sap/prerequisites-sap#firewall).  
**Network tags** | Specify the network tags that help you apply firewall rules to VMs in the deployment. For more information, see [Add network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags).  
**DNS zone** | 
  14. **Create a new DNS zone** : Select this option if you want Workload Manager to create a private Cloud DNS zone for the deployment.
  15. **Skip DNS configuration** : Select this option to manually set up a DNS zone on your own and to use that in the deployment.
For more information, see [DNS zones](https://docs.cloud.google.com/workload-manager/docs/deploy/sap/sap-hana-overview#dns).  
  16. Click **Continue**.

  17. In the **Database** tab, enter the following information:

**Field** | **Description**  
---|---  
**HANA SID** | Specify the SAP system ID (SID) for the database layer. The SID must consist of three alphanumeric characters and begin with a letter. All letters must be in uppercase.   
**Operating system** | Select a supported OS image. For more information, see [Supported operating systems](https://docs.cloud.google.com/workload-manager/docs/deploy/about-wlm-deployment#supported_operating_systems).  
  
All database VMs created during the deployment process use this operating system.  
**Secret name for database credentials** | Select the name of the secret that corresponds to the password for SAP HANA database. Workload Manager uses this password throughout the deployment and installation process. This secret must exist in the Google Cloud project in which you create the deployment.  
**Machine family** | Select a machine family for the database VMs.  
**Series** | Select a machine series for the database VMs.  
**Machine type** | Select a machine type for the database VMs.  
**Block storage option** | Select the type of block storage for the HANA database VM.*  
  
*If you select Balanced Persistent Disk or SSD Persistent Disk during the deployment process, all disks in the deployment will be the selected disk type. If you select Hyperdisk Extreme, only the `/data` and `/log` volumes use Hyperdisk Extreme, and the other disk volumes use SSD Persistent Disk. Disk sizes for each volume is automatically calculated in accordance with the best practices for the selected machine type and block storage type.

  18. Click **Continue**.

  19. In the **Application** tab, configure the SAP Central services and application servers for your S/4HANA workload.

**General**

**Field** | **Description**  
---|---  
**NetWeaver SID** | Specify the SAP system ID (SID) for the application layer. The SID must consist of three alphanumeric characters and begin with a letter. All letters must be in uppercase.   
**Operating system** | Select a supported OS image. For more information, see [Supported operating systems](https://docs.cloud.google.com/workload-manager/docs/deploy/about-wlm-deployment#supported_operating_systems).  
  
All application VMs created during the deployment process use this operating system.  
**Secret for application credentials** | Select the name of the secret that corresponds to the password for your SAP application. Workload Manager uses this password throughout the deployment and installation process. This secret must exist in the Google Cloud project in which you create the deployment.  
**Shared storage** | Workload Manager creates an NFS shared file storage for the deployment. For more information, see [Filestore Enterprise](https://docs.cloud.google.com/filestore/docs/overview#service_tiers).  
Alternatively, to use an existing shared storage, specify the mount location of the shared storage in the following format: 
         
         IP_ADDRESS/STORAGE_NAME

Replace the following:
     * IP_ADDRESS: the IP address of the NFS shared file storage
     * STORAGE_NAME: the name of the shared storage   
  
**Central services**

**Field** | **Description**  
---|---  
**Central services service account** | Select a service account for the ABAP SAP Central Services (ASCS) instances. You can either create a service account or choose an existing service account with the required IAM permissions. For more information, see [Service accounts and permissions](https://docs.cloud.google.com/workload-manager/docs/deploy/sap/prerequisites-sap#service-accounts).  
**Central services OS image** | Select a supported OS image. For more information, see [Supported operating systems](https://docs.cloud.google.com/workload-manager/docs/deploy/about-wlm-deployment#supported_operating_systems).  
All ASCS VMs created during the deployment process use this OS image.  
**Central services machine family** | Select a machine family for the ASCS VMs.  
**Central services machine series** | Select the machine series for the ASCS VMs.  
**Central services machine type** | Select a machine type for the ASCS VMs.  
  
**Application servers**

  
**Field** |   
**Description**  
---|---  
**Number of application servers per zone** |  Specify the required number of application servers in each zone.  
For example, a value of `2` creates two application VMs in a non-HA deployment model or a total of four application VMs in a HA deployment model, where the four VMs are divided evenly across both zones.  
**App instance number** | Specify the instance number for application servers.  
**VM names** | Specify names for the application servers that are created during the deployment.  
For high availability configurations, Workload Manager assigns the names to VMs in the primary and secondary zones in alternating order. If you leave this field empty, Workload Manager automatically assigns names based on the **VM name prefix** that you specified in the **Deployment basics** section.   
**Application server service account** | Select a service account for the application servers. You can either create a service account or choose an existing service account with the required IAM permissions. For more information, see [Service accounts and permissions](https://docs.cloud.google.com/workload-manager/docs/deploy/sap/prerequisites-sap#service-accounts).  
**Application server OS image** | Select a supported OS image. For more information, see [Supported operating systems](https://docs.cloud.google.com/workload-manager/docs/deploy/about-wlm-deployment#supported_operating_systems).  
Application servers created during the deployment process use this OS image.  
**Application server machine family** | Select a machine family for the application servers.  
**Application server machine series** | Select a machine series for the application servers.  
**Application server machine type** | Select a machine type for the application servers.  
  20. To see the **Preview** page, click **Continue**.

The **Preview** page summarizes the deployment details you entered in the previous tabs of the wizard. In addition, you can view errors from the previous steps in the Deployment dashboard.

  21. To deploy the SAP workload, click **Create**.




## Review the deployment status

After you create the deployment, you can monitor the status of the deployment on the dashboard by hovering the mouse over the **Status** icon.

You receive a notification in the Google Cloud console when Workload Manager completes the deployment process. If the deployment is not successful, you receive a failure notification. You can view additional information about the error on the Deployment Details page by clicking the deployment name on the dashboard. See Troubleshoot deployment errors.

**Note:** The entire deployment process can take up to two or three hours to complete. The deployment process continues in the background. You can check the deployment dashboard once you receive the notification.

## Troubleshoot deployment errors

When an error occurs during the deployment process, you receive a notification on the Google Cloud console. You can view additional error details on the **Deployment Details** page. If possible, steps to resolve the error or root cause are also provided. Otherwise, the error message contains a link to logs containing additional information.

If the error occurred during the configuration or provisioning of resources:

  * If the underlying issue requires changing the deployment configuration (for example, deployment name was not unique):

    1. Delete the deployment.
    2. Create a new deployment by providing the correct information.
  * If the underlying issue does not require changing the deployment configuration (for example, insufficient quota):

    1. Resolve the issue.
    2. Click **Retry** on the error message to resume the deployment process.



If the error occurred during the Ansible process of the deployment:

  * If the underlying issue requires changing the deployment configuration (for example, you specified the wrong Cloud Storage bucket for SAP files):

    1. Delete the deployment.
    2. Create a new deployment by providing the correct configuration.
  * If the underlying issue does not require changing the deployment configuration (for example, OS package failed to download):

    1. Resolve the issue, if applicable.
    2. Delete the deployment
    3. Create a new deployment by providing the correct configuration.



## What's next

  * [Perform the post-deployment tasks](https://docs.cloud.google.com/workload-manager/docs/deploy/post-deployment).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
