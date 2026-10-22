---
url: https://docs.cloud.google.com/chronicle/docs/administration/migrate-legacy-siem-infra/
title: SIEM migration overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:29.987555+00:00
---

# SIEM migration overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/administration/migrate-legacy-siem-infra/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SIEM migration overview

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** For a comprehensive, end-to-end demo on the Migration process, see the [Google SecOps SIEM Legacy Infra Migration video ](https://youtu.be/Bg8VZftcrlg?si=3mvcaSucWS-KfZkd).

This document describes how to perform a self-service migration to modernize your Google Security Operations SIEM from legacy infrastructure to Google Cloud. The migration ensures you are well positioned to benefit from the latest innovations in Google SecOps by unlocking Agentic Security Operations, greater reliability, privacy, top tier compliance posture, and newer capabilities like Emerging Threats, Dashboards, Data Access Controls, Security Validation, and Federation.

## Which SIEM instance should be migrated?

_Migrate your SIEM instance_ if it is _any_ of the following types: 

  * Not deployed in your Google Cloud project 
  * _OR_ Not using Google Cloud Authentication (Workforce Identity Federation / Cloud Identity)
  * _OR_ Not using Google Cloud Identity and Access Management (IAM) for Role-Based Access Control (RBAC)



_You don't need to migrate_ if your instance meets _all_ of the following conditions:

  1. Deployed in a Google Cloud project
  2. _AND_ Uses Workforce Identity Federation or Cloud Identity for authentication
  3. _AND_ Uses Google Cloud IAM to manage granular access permissions



## Why migrate now?

Migrating to the new infrastructure unlocks several critical benefits for your organization:

  * **Enhanced reliability and security:** Leverages Google Cloud infrastructure to provide higher platform reliability, stronger privacy controls, and enhanced security controls with VPC Service Controls.
  * **Granular access controls:** Transition from homegrown RBAC to Google Cloud IAM, enabling very precise feature and data access permissions.
  * **Agentic SOC capabilities:** Unlocks new agentic capabilities and AI-driven security operations.
  * **Comprehensive auditing:** Integration with Cloud Audit Logs for enhanced visibility into product actions.
  * **Compliance:** Meet growing compliance requirements including CMEK, VPC Service Controls, FedRAMP, and regional data residency requirements.



## Scope of migration

**Infra** | **Legacy stack** | **Modern stack**  
---|---|---  
Project hosting  | Google owned project  | Customer-owned Google Cloud project   
Authentication  | Legacy SIEM Authentication  | Google Cloud Auth: Workforce Identity Federation (WIF) or Cloud Identity   
Authorization  | Legacy SIEM RBAC  | Feature RBAC: Google Cloud IAM   
Audit Logging  | Limited internal logging  | Cloud Audit Logs: Comprehensive Google Cloud logging   
  
## Before you begin

Prepare your Google Cloud environment before you start the migration:

  * **Identify or create a Google Cloud[organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization)** and a **Google Cloud[project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project)**. Contact your Google Cloud administrator if you don't have the permissions to do so.
  * **Link the project to the correct billing account** , consistent with your Google SecOps contract.



## Perform the Self-service Migration

Perform the following migration steps in order. These steps are designed to ensure no adverse impact to customers, including no data loss and no product downtime.

  1. [Migrate from your Google owned project to your Google Cloud project](https://docs.cloud.google.com/chronicle/docs/administration/migrate-to-gcp-project).
  2. [Migrate from legacy authentication to Google Cloud authentication](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-auth-to-gcp-auth).
  3. [Migrate from legacy RBAC to feature RBAC](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-rbac-to-feature-rbac).
  4. [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api).



## After migration

After migration, you gain the following enhanced Google SecOps capabilities:

  * **Authentication** : Your authentication service is upgraded to [Cloud Identity](https://docs.cloud.google.com/identity/docs/overview) or [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).
  * **Authorization** : You have granular authorization, based on [Cloud IAM](https://docs.cloud.google.com/iam/docs/overview) roles and permissions.
  * **Audit logs** : You have comprehensive logs that you can view in [Cloud Audit Logs](https://docs.cloud.google.com/chronicle/docs/administration/audit-logging).



## We're here to help

We understand that these changes might require some planning, and we are here to support you throughout this transition. If you have any questions or require assistance, contact [Google SecOps Support](https://console.cloud.google.com/support).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
