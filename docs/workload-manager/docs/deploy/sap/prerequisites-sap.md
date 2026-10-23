---
url: https://docs.cloud.google.com/workload-manager/docs/deploy/sap/prerequisites-sap/
title: Prerequisites for deploying an SAP S/4HANA application \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:27.418745+00:00
---

# Prerequisites for deploying an SAP S/4HANA application  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/deploy/sap/prerequisites-sap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Prerequisites for deploying an SAP S/4HANA application Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the prerequisites for deploying an SAP S/4HANA application on Google Cloud using Workload Manager.

You must first meet the [prerequisites for using the Guided Deployment Automation](https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites) tool before deploying an SAP S/4HANA application.

Prerequisite | Description  
---|---  
**Google Cloud network resources** | Create or select a VPC network and subnetwork for your SAP deployment. You must also configure outbound internet access for your machines to download the required packages. For more information, see Network.  
**OS Login and SSH keys** | You must temporarily disable OS Login in your project metadata until the deployment is complete. For more information, see OS login and SSH keys.  
**Secrets for SAP workload** | To securely provide the passwords for your workload, you must use a secret created using Secret Manager. For more information, see Secrets for SAP workload.  
**IAM roles and permissions** | Users who deploy a SAP workload using the Guided Deployment Automation tool must have or be granted the required roles and permissions to configure the deployment. For more information, see IAM roles and permissions.  
**Service accounts** | Attach a service account to the deployment and make sure that the service account has all the roles required for deploying your workload. For more information, see Service accounts.  
**Quotas** | Make sure that you have sufficient resource quota in your project to deploy the SAP application. For more information, see Quotas.  
**SAP installation media** | Create a Cloud Storage bucket in the project in which you deploy the SAP application and upload all the SAP files required for deployment. For more information, see [Prepare SAP installation files for deployment](https://docs.cloud.google.com/workload-manager/docs/deploy/sap/sap-install-files).  
  
### Network

This section describes the Google Cloud networking resources that you need to configure before deploying the SAP application.

#### VPC network and subnetwork

If your project has a default VPC network, don't use it for creating a deployment. Instead, we recommend that you create your own VPC network so that the only firewall rules in effect are those that you create explicitly for the network. [Create a VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) and subnet or contact your Google Cloud organization's networking team.

#### Configure external internet access

During the deployment process, the VMs in your project need outbound internet access to download packages and to register for licensing.

Google recommends that you create a Cloud NAT gateway to provide external internet access for your VMs without creating external IP addresses. You can [create a Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation#configure-nat) in each subnet and region in which your VMs are located. If you create a Cloud NAT gateway, we recommended that you allocate at least 256 _Minimum ports per VM instance_.

If you don't want to use a Cloud NAT gateway, during the deployment process you can specify external IP addresses to provide the required internet access for your VMs.

### Firewall rules

During the deployment process, Workload Manager automatically creates the necessary firewall rules for the deployment.

Note that the existing _deny_ rules in your project might take a higher priority and deny the necessary access.  
Depending on your existing firewall rules in the project, create firewall rules to _allow_ access for:

  * The default ports used by SAP, as documented in [TCP/IP Ports of All SAP Products](https://help.sap.com/docs/Security/575a9f0e56f34c6e8138439eefc32b16/616a3c0b1cc748238de9c0341b15c63c.html)
  * Connections from your computer or your corporate network environment to your Compute Engine VM instances. If you are unsure of what IP address to use, contact your organization's network administrator.
  * Outgoing connectivity to Google Cloud services, using Google Private Access as appropriate.
  * Communication between machines in the same subnetwork: 
    * SSH access between VMs in the same subnet to configure deployed systems and for access by a system administrator.
    * Access to HANA application ports for communication between the application servers and the HANA database.
    * Access to SAP message servers, replication enqueue, gateway services between SAP application servers and central services instances.



For more information, see [Create VPC firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules).

#### Configure a DNS zone

When you create a deployment, you can choose Workload Manager to create a Cloud DNS zone. You can also skip the DNS zone creation during deployment and manually set it up later.

If you manually set up a DNS zone, ensure that the VPC network you're using for the deployment is added to the Cloud DNS zone and it is visible for querying records. For more information, see [Configure a DNS zone](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory-zone).

### OS Login and SSH keys

If [OS login](https://docs.cloud.google.com/compute/docs/instances/access-overview#oslogin) is enabled in your project metadata, you need to disable OS login temporarily until your deployment is complete. The deployment process configures SSH keys in the instance metadata. When OS Login is enabled, metadata-based SSH key configurations are disabled, and the deployment fails. After the deployment is complete, you can enable OS Login.

To disable OS Login, set the `enable-oslogin` metadata value to `false`. See [how to set project-wide metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-projectwide).

### Service accounts

Workload Manager uses the service account attached to your deployment to call other APIs and services for creating resources required for the deployment.

You can either attach an existing service account or create a service account when you configure the deployment. Depending on your application and configuration, Workload Manager prompts you to grant any of the missing roles to your service account.

For more information about the roles required for deploying SAP S/4HANA, see [Service accounts and permissions](https://docs.cloud.google.com/workload-manager/docs/deploy/sap/sap-hana-overview#service-accounts).

### IAM roles and permissions for deploying SAP S/4HANA

The Workload Manager Deployment Admin role contains all the permissions required for configuring and deploying SAP S/4HANA on Google Cloud.

For more information about the required IAM roles and permissions to deploy a workload using the Guided Deployment Automation tool, see [IAM roles and permissions](https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites#iam-roles).

For more information about IAM permissions for running SAP on Google Cloud, see [Identity and Access Management for SAP Programs on Google Cloud](https://docs.cloud.google.com/sap/docs/security-for-sap/iam-for-sap-programs).

### Quotas

Google Cloud uses quotas to protect and control the number of resources that a particular account or organization can use. SAP workloads often consume a large portion of resources. Given the size of the databases and applications, you might experience quota issues during the deployment process.

To avoid quota issues, do the following:

  1. [View your quota values and usage](https://docs.cloud.google.com/docs/quotas/view-manage).
  2. If needed, [request a higher quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) or contact your project administrator.



### Secrets for SAP workload

The Guided Deployment Automation tool uses Secret Manager to store passwords needed during the deployment and installation process, such as the passwords for administrator and SYSTEM user accounts. Plain text passwords are prohibited in accordance with our [Terraform best practices](https://docs.cloud.google.com/docs/terraform/best-practices-for-terraform#secrets).

Before using the Guided Deployment Automation tool, you must [create at least one Secret](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart). If you want to use different secrets for the database and application layers, create separate secrets for each layer.

To ensure that the secrets meet the password requirements from SAP, follow the [SAP guidance for creating passwords](https://help.sap.com/docs/SLTOOLSET/39c32e9783f6439e871410848f61544c/fe3f4554f82b1d5de10000000a44538d.html?version=CURRENT_VERSION_SWPM20&q=password).

You must create secrets in the project in which you deploy the SAP workload.

## What's next

  * Learn how to [prepare SAP installation files for deployment](https://docs.cloud.google.com/workload-manager/docs/deploy/sap-install-files).
  * Learn how to [deploy a SAP S/4HANA workload](https://docs.cloud.google.com/workload-manager/docs/deploy/deploy-sap).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
