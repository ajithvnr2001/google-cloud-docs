---
url: https://docs.cloud.google.com/workload-manager/docs/release-notes/
title: Workload Manager release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:39:33.830652+00:00
---

# Workload Manager release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Resources ](https://docs.cloud.google.com/workload-manager/docs/release-notes)



Send feedback 

#  Workload Manager release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Workload Manager. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

## September 11, 2026

Feature

**Preview** : Workload Manager supports viewing rule findings for workloads that you evaluate across Google Cloud projects in your resource hierarchy. These rule findings help you identify configuration risks for your resources against the best practices for reliability and security. You can also view the rule findings directly on the Compute Engine **Overview** page in the Google Cloud console.

For more information, see the following:

  * [About Workload Manager rule findings](https://docs.cloud.google.com/workload-manager/docs/about-rule-findings)
  * [View Workload Manager rule findings](https://docs.cloud.google.com/workload-manager/docs/evaluate/view-rule-findings)
  * [View Workload Manager rule findings on the Compute Engine Overview page](https://docs.cloud.google.com/compute/docs/view-wlm-findings)
  * [Share evaluation findings](https://docs.cloud.google.com/workload-manager/docs/evaluate/create-evaluation#share-findings)



## March 27, 2026

Feature

**Generally available** : Workload Manager supports deploying Oracle Database workloads on Google Cloud using the Guided Deployment Automation. For more information, see [Overview of Oracle Database workload deployment](https://docs.cloud.google.com/workload-manager/docs/deploy/oracle/oracle-deploy-overview).

## March 10, 2026

Announcement

**Generally available** : The Workload Manager observability service for SAP workloads is now generally available and introduces the following enhancements:

  * The main observability dashboard displays the **Observability Pre-reqs** field, which indicates the overall status of the observability prerequisites for your SAP workloads.

For more information, see [View system dashboard](https://docs.cloud.google.com/workload-manager/docs/observe/sap/view-dashboards#dashboard-overview).

  * Instead of waiting 48 hours, you can immediately remove your SAP workload from the Workload Manager **Observability** page of the Google Cloud console by using the `projects.locations.insights.delete` API method.

For more information, see [Remove workloads from the observability dashboard](https://docs.cloud.google.com/workload-manager/docs/observe/sap/view-dashboards#remove-dashboards).




For more information about the observability service, see [SAP observability overview](https://docs.cloud.google.com/workload-manager/docs/observe/sap/overview).

## February 23, 2026

Feature

**Preview** : To configure Google Cloud's Agent for SAP for setting up observability for your SAP workload, you can use VM Extension Manager.

For more information, see [Configure Agent for SAP to set up observability](https://docs.cloud.google.com/workload-manager/docs/observe/sap/configure-agent).

## November 04, 2025

Feature

**Preview** : The Workload Manager observability dashboard has been updated to display information about the status and configuration of Google Cloud's Agent for SAP that you're using.

You can view this information in the following fields of the **Applications** and **Databases** tabs:

  * **Agent version**
  * **Process metrics**
  * **System discovery**
  * **HANA monitoring**.



To view this information, you need to use version 3.10 or later of the agent.

For more information, see [Applications and Databases tabs](https://docs.cloud.google.com/workload-manager/docs/observe/sap/view-dashboards#applications_and_databases_tabs).

## September 18, 2025

Feature

**Generally available** : You can evaluate MySQL and Redis workloads running on Compute Engine instances by using Workload Manager. For these evaluations, you need to install version 1.2 of Agent for Compute Workloads.

For information about how to set up the agent, see:

  * [Set up the agent for MySQL workloads](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-mysql)
  * [Set up the agent for Redis workloads](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-redis)



For information about the evaluations supported for MySQL and Redis workloads, see:

  * [Workload Manager best practices for MySQL](https://docs.cloud.google.com/workload-manager/docs/reference/best-practices-mysql)
  * [Workload Manager best practices for Redis](https://docs.cloud.google.com/workload-manager/docs/reference/best-practices-redis)



## July 21, 2025

Feature

You can set up the Agent for Compute Workloads to collect metrics of your Oracle workloads running on Google Compute Engine instances. For more information, see [Set up the agent for Oracle](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-oracle).

## March 17, 2025

Announcement

**Generally available** : Workload Manager supports deploying Microsoft SQL Server workloads on Google Cloud. You can configure and deploy a SQL Server system using the Guided Deployment Automation tool in Workload Manager. For more information, see [Overview of SQL Server deployment](https://docs.cloud.google.com/workload-manager/docs/deploy/sql-server/sql-deploy-overview).

Feature

Workload Manager supports the following features when you deploy SAP S/4HANA workloads on Google Cloud:

  * Deploy SAP S/4HANA workloads on X4 instances.
  * Customize the names of application server VMs.
  * Specify network tags for the deployed instances.
  * Skip the creation of automatic firewall rules.
  * Skip the DNS configuration.
  * Choose an existing NFS shared storage.
  * Specify a service account to be attached to instances for each layer of the deployment.



For more information, see [Deploy an SAP S/4HANA application](https://docs.cloud.google.com/workload-manager/docs/deploy/sap/deploy-sap)

## January 21, 2025

Feature

**Generally available** : You can define organizational best practices for your workloads using _custom rules_ written in the Rego policy language. Workload Manager evaluates your workloads against these rules and creates reports for any violation and helps you prioritize remediation. This helps you continuously improve the quality, reliability, and performance of your workloads. For more information, see [Implementing best practices using custom rules](https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/about-custom-rules).

## October 07, 2024

Feature

**Preview** : Workload Manager now supports deploying Microsoft SQL Server workloads on Google Cloud. You can configure and deploy a SQL Server system using the Guided Deployment Automation tool in Workload Manager. For more information, see [Overview of SQL Server deployment](https://docs.cloud.google.com/workload-manager/docs/deploy/sql-server/sql-deploy-overview).

## August 15, 2024

Feature

**Preview** : The observability service for SAP in Workload Manager is now available for public preview. The preconfigured observability dashboards provide a unified view of the infrastructure monitoring metrics and your SAP application metrics. This helps you correlate events and understand the health status of your SAP system across all layers of the environment.

For more information about this service, see [SAP observability overview](https://docs.cloud.google.com/workload-manager/docs/observe/sap/overview).

## May 20, 2024

Feature

**Preview** : You can now define organizational best practices for your workloads using _custom rules_ written in the Rego policy language. Workload Manager evaluates your workloads against these rules and creates reports for any violation and helps you prioritize remediation. This helps you continuously improve the quality, reliability, and performance of your workloads. For more information, see [Implementing best practices using custom rules](https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/about-custom-rules).

## March 06, 2024

Announcement

**Generally Available** : Workload Manager now supports deploying SAP workloads on Google Cloud. You can configure and deploy a SAP S/4HANA system using the Guided Deployment Automation tool in Workload Manager. For more information, see [About Guided Deployment Automation](https://docs.cloud.google.com/workload-manager/docs/deploy/about-wlm-deployment).

## January 31, 2024

Announcement

**Generally available** : Workload Manager is now generally available (GA) for evaluating SQL Server workloads. For more information, see [About Workload Manager Evaluation](https://docs.cloud.google.com/workload-manager/docs/about-evaluations)

## September 05, 2023

Feature

**Preview:** Workload Manager is now available for SQL Server workloads. For more information, see the [Product overview](https://docs.cloud.google.com/workload-manager/docs/overview).

## August 17, 2023

Feature

**Generally available** : Workload Manager introduces new rules for SAP workloads that help you evaluate the workload against the security best practices from SAP and Google Cloud. For more information, see [Best practices for SAP](https://docs.cloud.google.com/workload-manager/docs/reference/best-practices).

For information about setting up Google Cloud's Agent for SAP to collect security validation metrics, see [Enable Workload Manager validation metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-workload-manager-evaluation#enable_wlm_evaluation_metrics_collection).

## July 11, 2023

Feature

**Preview** : Workload Manager now supports deploying SAP workloads on Google Cloud. You can configure and deploy a SAP S/4HANA system using the Guided Deployment Automation tool in Workload Manager. For more information, see [About Guided Deployment Automation](https://docs.cloud.google.com/workload-manager/docs/deploy/about-wlm-deployment).

## April 11, 2023

Announcement

**Generally available** : Workload Manager is now generally available (GA) for evaluating SAP workloads. It is a rule-based, cross-project validation service for evaluating workloads running on Google Cloud. 

You can use Workload Manager to evaluate your SAP HANA and SAP NetWeaver workloads, and detect deviations from key best practices that SAP, OS vendors, and Google Cloud prescribe. This helps you improve the quality, reliability, and performance of your SAP workloads.

The set of rules provided will continue to evolve to cover new machine types and storage options as they become available, and extend SAP HANA and SAP NetWeaver best practices as relevant for your SAP workloads.

For more information, see the [Product overview](https://docs.cloud.google.com/workload-manager/docs/overview).

## February 06, 2023

Feature

**Preview** : While [creating a new evaluation](https://docs.cloud.google.com/workload-manager/docs/create-evaluation#create-a-workload-evaluation), you can now choose how frequently you want to run the evaluation.

## October 11, 2022

Feature

**Preview:** Workload Manager is now available for SAP workloads. For more information, see the [Product overview](https://docs.cloud.google.com/workload-manager/docs/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
