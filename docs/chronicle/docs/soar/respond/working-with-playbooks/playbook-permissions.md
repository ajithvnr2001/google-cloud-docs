---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/playbook-permissions/
title: Manage playbook permissions \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:23.276954+00:00
---

# Manage playbook permissions  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/playbook-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage playbook permissions

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

The playbook creator can define, view, and edit permissions for users per playbook. This means you can restrict access for specific users or SOC roles to edit certain playbooks. 

Examples of Managed Security Service Providers (MSSPs) use cases for playbook permissions include: 

  * Grant end customers (Managed-plus users) permission to build playbooks in their own environment while collaborating with MSSP engineers. 
  * Grant MSSPs permission to create playbooks without giving edit permissions to their end customers (Managed-plus users). 



Examples of Enterprise use cases for playbook permissions include: 

  * Restrict edit access of certain engineers to sensitive playbooks. 
  * Prevent engineers from overriding your work while building a playbook. 



## Grant permission to users

To grant permission to users, follow these steps:

  1. On the **Playbooks** page, click  passkey **Permissions** to show the **Playbook access permissions** dialog.
  2. The **Playbook access permissions** dialog has two main sections:
     * **Default Permissions** : This section focuses on all the users who have access to all the environments that the playbook can run on. In this dialog can choose to let users view this playbook or grant them permission to make changes. You have to have access to all the environments the playbook runs on in order to have editing rights. However, you only need access to one environment in order to have viewing rights. 
     * **Specific permissions** : This section facilitates more granular flexibility in drilling down to specific users or SOC roles within specific groups to grant them either edit or view access. Permissions selected here override the default permissions that were previously set. 



### Grant specific permissions

You can configure specific permissions for individual users or for SOC roles. SOC roles can be assigned to both users and API keys.

For example, you could tag Tier 3 as **view only** and select Alex Smith (who is in Tier 3) as having edit permissions. 

  


**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
