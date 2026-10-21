---
url: https://docs.cloud.google.com/workload-manager/docs/deploy/about-wlm-deployment/
title: About Guided Deployment Automation \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:09:40.143491+00:00
---

# About Guided Deployment Automation  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/deploy/about-wlm-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  About Guided Deployment Automation Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the Guided Deployment Automation tool in Workload Manager that lets you quickly customize and deploy your workloads on Google Cloud.

## Guided Deployment Automation

The Guided Deployment Automation tool in Workload Manager lets you configure and deploy enterprise applications on Google Cloud. You can also use Guided Deployment Automation to configure a deployment for your workload, and then generate Terraform and Ansible infrastructure as code (IaC) that you can export for further customization or use in an existing deployment pipeline.

## Benefits

Guided Deployment Automation provides you with the following features and key benefits:

  * Provides end-to-end deployment automation built on Terraform and Ansible, leveraging existing Google Cloud products and services.
  * Reduces the deployment time by collecting your intent for the system and then guiding you through the configuration process to meet your requirements.
  * Built-in recommendations and safeguarding helps you ensure that you follow the deployment best practices and avoid errors during the configuration and deployment process.



## Supported workloads

You can use the Guided Deployment Automation to deploy the following workloads:

  * [SAP S/4HANA](https://docs.cloud.google.com/workload-manager/docs/deploy/sap/sap-hana-overview)
  * [SQL Server](https://docs.cloud.google.com/workload-manager/docs/deploy/sql-server/sql-deploy-overview)
  * [Oracle Database](https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/oracle-deploy-overview)



## Limitations

The following limitations apply for the Guided Deployment Automation tool:

  * Does not support post-deployment modifications directly from the Google Cloud console. If post-deployment modifications are expected, we recommend that you [export and download the IaC](https://docs.cloud.google.com/workload-manager/docs/deploy/export-sap-iac) and make subsequent changes using Terraform and Ansible.



## How Guided Deployment Automation works

Workload Manager performs the following tasks when you deploy your application using the Guided Deployment Automation tool:

  1. Lets you select a supported application to deploy.
  2. Helps you select the configurations specific to your application and completes the deployment configuration on the Google Cloud console.
  3. Generates the equivalent infrastructure as code (IaC) based on the configuration.
  4. After configuring the deployment, you can either deploy it directly from the Google Cloud console or download the generated IaC and deploy manually.



## Pricing

Guided Deployment Automation is available at no cost. You will be charged for any resources that are consumed during the deployment process, such as VMs and persistent disks, in addition to the charges that might result from the necessary APIs or other services.

Guided Deployment Automation does not include an option to estimate the cost for your deployment. Contact your Google account team for price information, including any relevant discounts or credits.

## What's next

  * Read the [prerequisites for using the Guided Deployment Automation tool](https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites).
  * Learn how to [deploy an SAP S/4HANA workload](https://docs.cloud.google.com/workload-manager/docs/deploy/sap/deploy-sap).
  * Learn how to [deploy a SQL Server workload](https://docs.cloud.google.com/workload-manager/docs/deploy/sql-server/deploy-sql).
  * Learn how to [deploy an Oracle Database workload](https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/oracle-deploy-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
