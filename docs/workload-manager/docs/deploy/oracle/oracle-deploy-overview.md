---
url: https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/oracle-deploy-overview/
title: Overview of Oracle Database workload deployment \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:09:39.735657+00:00
---

# Overview of Oracle Database workload deployment  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/oracle-deploy-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Overview of Oracle Database workload deployment Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of the Oracle Database workloads that you can deploy on Google Cloud using the Guided Deployment Automation tool in Workload Manager.

When you configure your Oracle Database deployment, Workload Manager collects your workload requirements, recommends values for your deployment settings, and helps you ensure that your deployment follows the best practices for running Oracle Database workloads on Compute Engine.

## Oracle Database deployment process

Workload Manager completes the following tasks when you deploy an Oracle Database:

  * Enable the required APIs (if not enabled in the project) and grant the required roles and permissions.
  * Configure and provision the required infrastructure for deployment.
  * Create VMs for Oracle database.
  * Create [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) repositories.
  * Create the necessary firewall rules required for the VMs to communicate with each other.
  * Create storage disks.
  * Configure and install Oracle software.
  * Install [Agent for Compute Workloads](https://docs.cloud.google.com/compute/docs/instances/agent-for-compute-workloads) on the VMs.



The output of a successful deployment is an empty ("greenfield") Oracle database running on the Compute Engine.

## High-level architecture of Oracle Database deployment

For a high-level architecture of Oracle Database deployment, see [Enterprise application with Oracle Database on Compute Engine](https://docs.cloud.google.com/architecture/enterprise-app-oracle-database-compute-engine). Oracle Database deployment using the Guided Deployment Automation tool creates a Compute Engine VM hosting an Oracle database which is a small building block of the high-level architecture.

### Deploy using the Google Cloud console

When you choose to deploy your workload using the Google Cloud console, Workload Manager automatically handles the end-to-end deployment, including provisioning the Oracle database, VMs, and storage. You also have access to all underlying files used during the deployment process.

Workload Manager uses [Infrastructure Manager](https://docs.cloud.google.com/infrastructure-manager/docs/overview) to automate the deployment process. Infra Manager uses Cloud Build to initialize Terraform and to run other Terraform commands. Cloud Build then stores Terraform files and the Terraform State File in a Cloud Storage bucket in your Google Cloud project. Ansible orchestrates the installation of the Oracle software on the VMs.

## Security considerations

The following sections describe how Workload Manager helps protect your deployments.

### Service Accounts and IAM permissions

Workload Manager uses the following three service accounts to grant required IAM roles and permissions for your Oracle deployment:

  * Workload Manager service account
  * User-managed service account
  * Compute Engine service account



For more information about these service accounts, see [Service accounts for Oracle deployments](https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/prerequisites-oracle#service-accounts-oracle).

### Oracle Database credentials

Workload Manager uses [Secret Manager](https://cloud.google.com/secret-manager) to store the access credentials for your Oracle database. For passwords of your database, you must [create secrets](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets), and then specify the secrets during the deployment process.

For more information, see [Prerequisites](https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/prerequisites-oracle).

## Google Cloud APIs

An Oracle Database workload on Google Cloud uses various products and services. The deployment process requires the following APIs that are enabled automatically if needed. The usage of these APIs is subject to the terms of service of each API and may incur additional associated charges.

  * Artifact Registry API
  * Cloud Build API
  * Cloud Logging API
  * Cloud Resource Manager API
  * Cloud Storage API
  * Compute Engine API
  * IAM Service Account Credentials API
  * Identity and Access Management API
  * Infrastructure Manager API
  * Secret Manager API
  * Service Usage API
  * Workload Manager API



## Licensing

Workload Manager uses a bring-your-own-license (BYOL) model for Oracle Database workload deployments, which means you're responsible for licensing of all of your Oracle software.

## Pricing

Although the Guided Deployment Automation is available at no cost, you incur charges for any other resources used during the deployment process, such as VMs and persistent disks. You might also be charged for the necessary APIs or other services.

Workload Manager doesn't provide a cost estimate for the chosen deployment. Contact your Google account team for pricing information, including any relevant discounts or credits.

## Getting Support

If you're facing an issue with your deployment or need assistance, contact [Cloud Customer Care](https://cloud.google.com/support-hub).

## What's next

  * Read the [prerequisites for deploying using Workload Manager](https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites).
  * Learn how to [deploy an Oracle Database workload](https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/deploy-oracle).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
