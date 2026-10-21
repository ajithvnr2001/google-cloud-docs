---
url: https://docs.cloud.google.com/workload-manager/docs/deploy/sql-server/prerequisites-sql/
title: Prerequisites for deploying a SQL Server workload \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:33.606302+00:00
---

# Prerequisites for deploying a SQL Server workload  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/deploy/sql-server/prerequisites-sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Prerequisites for deploying a SQL Server workload Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the prerequisites for deploying a SQL Server workload on Google Cloud using Workload Manager.

You must first meet the [prerequisites for using the Guided Deployment Automation](https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites) tool before deploying a SQL Server workload.

Prerequisite | Description  
---|---  
**Google Cloud network resources** | Create or select a VPC network and subnetwork for your SQL Server deployment. You must also configure outbound internet access for your machines to download the required packages. For more information, see Network.  
**IAM roles and permissions** | Users who deploy a SQL Server workload using the Guided Deployment Automation tool must have or be granted the required roles and permissions to configure the deployment. For more information, see IAM roles and permissions.  
**Secrets for SQL Server workload** | To securely provide the passwords for your workload, you must use a secret created using Secret Manager. For more information, see Secrets for SQL Server workload.  
**Quotas** | Make sure that you have sufficient resource quota in your project to deploy the SQL Server application. For more information, see Quotas.  
**SQL Server installation media** | Create a Cloud Storage bucket in the project in which you deploy the SQL Server application and upload all the SQL Server files required for deployment. For more information, see Prepare SQL Server installation files for deployment.  
**Active Directory** | Create an Active Directory domain by using the Managed Microsoft Active Directory or by deploying a custom Active Directory on VMs. For more information, see Create an Active Directory domain.  
  
### Configure networking resources

This section describes the Google Cloud networking resources that you need to configure before deploying the SQL Server workload.

### VPC Network And Subnetwork

Although your project has a default VPC and subnetwork (subnet), we recommend that you create a new network so that the only firewall rules in effect are those that you create explicitly. [Create a VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) and subnet or contact your Google Cloud organization's networking team.

### Create a Cloud NAT gateway

During the deployment process, VMs need outbound internet access to download packages and register for licensing. Google recommends that you create a Cloud NAT gateway to provide external internet access for your VMs without creating external IP addresses. You can [create a Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation#configure-nat) in each subnet and region in which your VMs are located.

If you don't want to use a Cloud NAT gateway, during the deployment process you can specify external IP addresses to provide the required internet access for your VMs.

## IAM permissions and roles

The following permission is required to enable the Workload Manager API in the project where you're deploying the workload. This permission only needs to be granted once in each project. An administrator or another user with this permission can enable the API and other users will be able to access Workload Manager in the project.

**Action(s)** | **Permission Required(s)** | **Example Role(s)**  
---|---|---  
Enabling Workload Manager API | serviceusage.services.enable | roles/editor  
roles/service.Usage.Admin  
  
Workload Manager also has roles to control who can access the deployment options and determine who can deploy, manage, and view deployments. Each role has the necessary permissions to perform the stated tasks. A complete list of the permissions assigned to each role can be found in the references section of the documentation.

**Role** | **Deployment Actions in WLM**  
---|---  
Workload Manager Deployment Admin | Create / Modify / Deploy  
View  
Workload Manager Deployment Viewer | View  
  
You must also have the following permission to create the service accounts that are used throughout the deployment process.

**Action(s)** | **Permission Required(s)** | **Example Role(s)**  
---|---|---  
Creating service accounts used in deployment | resourcemanager.projects.setIamPolicy | role/resourcemanager.projectIamAdmin  
  
## Secrets for SQL Server workload

The Guided Deployment Automation tool uses Secret Manager to store passwords needed during the deployment process. Plain text passwords are prohibited in accordance with our [Terraform best practices](https://docs.cloud.google.com/docs/terraform/best-practices-for-terraform#secrets).

Before using the Guided Deployment Automation tool, you must [create at least one Secret](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart) using Secret Manager.

Make sure to follow the [password complexity requirements](https://learn.microsoft.com/en-us/sql/relational-databases/security/password-policy?view=sql-server-ver16#password-complexity) for SQL Server accounts. To ensure that the secrets meet the password requirements from SQL Server, follow the [SQL Server guidance for creating passwords](https://help..com/docs/SLTOOLSET/39c32e9783f6439e871410848f61544c/fe3f4554f82b1d5de10000000a44538d.html?version=CURRENT_VERSION_SWPM20&q=password).

You must create secrets in the project in which you deploy the SQL Server workload.

## Quotas

Google Cloud uses quotas to protect and control the number of resources that a particular account or organization can use. SQL Server workloads often consume a large portion of resources. Given the size of the databases and applications, you might experience quota issues during the deployment process.

To avoid quota issues, do the following:

  1. [View your quota values and usage](https://docs.cloud.google.com/docs/quotas/view-manage).
  2. If needed, [request a higher quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) or contact your project administrator.



## Licensing

Customers have a range of options for on-demand SQL Server and Windows Server licenses directly from Google Cloud, and also the option to bring their own existing licenses if those licenses meet the eligibility requirements. For more information, see the [Microsoft licensing documentation](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing).

## Prepare the SQL Server installation files

For SQL Server high availability (HA) configuration using bring your own license (BYOL), you must create a Cloud Storage bucket in the project to hold the required installation media (ISO) file used during installation of SQL Server. Use the Google Cloud console to [create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/discover-object-storage-console) for storing the SQL Server installation files.

After creating the bucket, upload the SQL Server installation ISO file to the bucket by following your chosen method to [upload objects to a bucket](https://docs.cloud.google.com/storage/docs/uploading-objects#uploading-an-object).

## Create an Active Directory domain

Before using the Guided Deployment Automation tool to deploy a SQL Server workload, you need to set up the following:

  * An Active Directory domain with at least one domain controller.

You can create an Active Directory domain by using [Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain). Alternatively, you can [deploy a custom AD environment on Compute Engine](https://docs.cloud.google.com/architecture/deploy-an-active-directory-forest-on-compute-engine) and [set up a private DNS forwarding zone](https://docs.cloud.google.com/compute/docs/instances/windows/best-practices#use_cloud_dns_private_forwarding_zones) that forwards DNS queries to your domain controllers.

  * An Active Directory user who has permissions to join VMs to the domain and who can sign in by using RDP. If you're using Managed Microsoft AD, you can use the `setupadmin` user.

  * A Google Cloud project with a VPC network with connectivity to your AD domain controllers.




## What's next

  * Learn how to [deploy a SQL Server workload](https://docs.cloud.google.com/workload-manager/docs/deploy/sql-server/deploy-sql).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
