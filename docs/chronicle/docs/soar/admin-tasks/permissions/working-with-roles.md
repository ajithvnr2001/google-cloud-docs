---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-roles/
title: Manage SOC roles \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:16.525752+00:00
---

# Manage SOC roles  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage SOC roles 

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** SOAR SOC roles will continue to exist after [migrating SOAR to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp). They are independent of IAM roles. 

Roles in Google Security Operations let administrators streamline workflows by creating custom access levels and automating task assignments. This document explains how to create SOAR SOC roles to control permissions and manage SOC team workloads effectively.

## Role permissions and customization

You can customize roles to fit the needs of your SOC. This lets you control permissions, manage team workloads, and route tasks more effectively, with these details in mind:

  * An administrator can add up to 20 customized roles.
  * Predefined SOC roles (such as `Tier 1` or `Collaborator`) can also be modified.
  * New roles can be created for various purposes, such as to:
    * Route tasks to specific SOC teams
    * Manage SOC teams' daily workloads
    * Control view permissions
    * Manage cases access permissions



## Create a new role

To create a new role, follow these steps:

  1. Go to **Settings** > **Organization** > **Roles**.
  2. On the **Roles** page, click add**Add**.
  3. In the **Add Role** dialog, enter a name for the new role, and select which additional roles it should have access to. Doing this affects which cases users can see in the Google SecOps platform.  

  4. Click **Add**. The role is added to the table.

**Note:** Click **Edit** to set a role as the default. All new cases are automatically assigned to the default role, and it can't be deleted while it's a default role. 

For more information on roles, see [Learn how to control access to the platform](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/control-access-to-platform).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
