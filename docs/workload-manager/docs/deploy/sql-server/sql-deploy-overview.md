---
url: https://docs.cloud.google.com/workload-manager/docs/deploy/sql-server/sql-deploy-overview/
title: Overview of SQL Server deployment \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:09:37.862060+00:00
---

# Overview of SQL Server deployment  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/deploy/sql-server/sql-deploy-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Overview of SQL Server deployment Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of the SQL Server systems that you can deploy on Google Cloud using the Guided Deployment Automation tool in Workload Manager.

When you configure your SQL Server deployment, Workload Manager collects the necessary information about your workload, recommends values for your deployment settings, and helps you ensure that your deployment follows the best practices for running SQL Server on Google Cloud. 

## SQL Server deployment process

Workload Manager completes the following tasks when you deploy a SQL Server workload:

  * Enable the required APIs, if not enabled in the project.
  * Configure and provision the required infrastructure for deployment.
  * Configure the operating system on VMs.
  * Install the selected SQL Server edition.
  * Configure distributed network name (DNN).
  * Join the VMs to a Microsoft Active Directory domain.
  * Install Google Cloud's Agent for Compute Workloads on the VMs.



The output of a successful deployment is an empty ("greenfield") SQL Server database.

## High-level architecture of SQL Server deployment

This section provides an overview of the SQL Server high availability deployments that Workload Manager supports. Note that the exact architecture might vary depending on the configuration and settings that you specified. The figures don't include all deployed resources.

### SQL Server Always On availability groups

The following figure illustrates a highly available SQL Server deployment using Always On availability groups. For more information, see [Configure SQL Server Always On availability groups](https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability-dnn).

![High availability Architecture](https://docs.cloud.google.com/static/compute/images/sqlserver-ag-architecture-dnn.svg)

### SQL Server failover cluster instance that uses Storage Spaces Direct

The following figure illustrates a highly available SQL Server deployment using Windows Server failover cluster using Storage Spaces Direct (S2D). For more information, see [Configuring a SQL Server failover cluster instance using storage spaces direct](https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-failover-cluster-instance).

![S2D architecture](https://docs.cloud.google.com/static/compute/images/sqlserver-fci-s2d-architecture.svg)

## Configuration process

When you configure your SQL Server deployment, the Guided Deployment Automation tool collects the required information and specifications for your workload, and then recommends values for some of the settings. You can modify these default values as needed.

The Guided Deployment Automation tool automatically converts your configuration settings to Terraform and PowerShell Desired State Configuration (DSC) files. You can choose to deploy the generated files directly from the Google Cloud console or export the files and deploy on your own.

### Deploy using the Google Cloud console

If you choose to deploy the system automatically, Workload Manager deploys the workload and runs the Terraform and PowerShell DSC files. You have access to all underlying files used during the deployment process.

[Cloud Build](https://docs.cloud.google.com/build/docs/overview) is used to initiate Terraform and it stores the Terraform files and the Terraform state file in a Cloud Storage bucket, which users with project-wide roles for Cloud Storage can access. All the required resources, such as VMs and disks, are configured and provisioned using Terraform.

In addition to Compute Engine resources required for your SQL Server workload, Terraform also configures PowerShell DSC using the `sysprep-specialize-script-ps1` [startup script](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows#metadata-keys). PowerShell DSC is responsible for further configuration of the deployed infrastructure, including OS configuration, high availability (HA) cluster configuration, and orchestration of SQL Server installation and configuration.

### Export and deploy

After you configure the deployment, you can download the Terraform folder that contains all the files required for the deployment, in addition to a variable file which is pre-configured based on your inputs in the configuration process.

You can customize the Terraform files or deploy them as they are. For more information about managing and deploying Terraform on your own, see the [Terraform on Google Cloud documentation](https://docs.cloud.google.com/docs/terraform).

We recommend that you customize the deployment only if you are an advanced user, because such changes can disrupt the deployment process or deviate from best practices.

Workload Manager doesn't register or list workloads deployed on your own using Terraform. You can refer to the troubleshooting and post-deployment steps, but they cannot be applied to workloads deployed outside of Workload Manager. For these reasons, we recommend that only advanced users use the export option.

## Security considerations

The following sections describe how Workload Manager secures your deployments.

### Service Accounts

Workload Manager uses the service account attached to your deployment to call other APIs and services for creating resources required for the deployment.

When you configure the deployment, you can either attach an existing service account or create a service account. Depending on your application and configuration, Workload Manager might prompt you to grant any missing roles to your service account.

### SQL Server credentials

Workload Manager uses [Secret Manager](https://docs.cloud.google.com/secret-manager) to store credentials for your SQL Server systems. To securely provide the password, you must [create secrets](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) for the Active Directory and database, and then specify that secret during the deployment process.

## Google Cloud APIs

A SQL Server workload on Google Cloud uses various products and services. The deployment process requires the following APIs that are enabled automatically if needed. The usage of these APIs is subject to the terms of service of each API and may incur additional associated charges.

  * Service Usage API
  * Cloud Config Manager API
  * Cloud DNS API
  * Compute Engine API
  * Cloud Storage API
  * Cloud Resource Manager API
  * Identity and Access Management API
  * IAM Service Account Credentials API
  * Cloud Logging API
  * Cloud Build API
  * Workload Manager API
  * Secret Manager API



## Pricing

Guided Deployment Automation is available at no cost. You might incur a charge for any resources used during the deployment process, such as VMs, persistent disks, and licenses. You might also be charged for the necessary APIs or other services.

Workload Manager does not provide a cost estimate for the chosen deployment. Contact your Google account team for pricing information, including any relevant discounts or credits.

## What's next

  * Read the [prerequisites for deploying using Workload Manager](https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites).
  * Learn how to [deploy a SQL Server workload](https://docs.cloud.google.com/workload-manager/docs/deploy/sql-server/deploy-sql).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
