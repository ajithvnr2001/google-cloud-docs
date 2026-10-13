---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/environment-groups/
title: Manage environment groups \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:43.082293+00:00
---

# Manage environment groups  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/environment-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage environment groups

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to create and manage environment groups in Google Security Operations. Environment groups let you organize multiple environments into logical categories, making it easier to manage large organizations or multiple customers as a Managed Security Service Provider (MSSP). 

## Environment group use cases

MSSPs, government entities, and enterprises with multiple sub-organizations can all benefit from using environment groups. Common use cases include:

  * **MSSP service-level tiers** : Differentiating services based on customer tiers (for example, Gold, Silver).
  * **Government sectors** : Customize security solutions for specific industries (for example, communication, transportation).
  * **Enterprise sub-organizations** : Manage security for individual sub-organizations within a larger entity (for example, Sub Org 1, Sub Org 2).



## Understand supported modules for environment groups

The following modules support environment groups:

  * [ **Settings**](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/work-with-environments): Speeds up onboarding of new users and simplifies adding new environments to existing groups.
  * [ **Playbooks or blocks**](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/whats-on-the-playbooks-screen): Streamlines playbook creation. You can adjust the scope of your playbooks by grouping environments together. Playbooks automatically update the scope when you modify the environment groups.
  * [ **Case filters**](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/apply-and-save-filters): Enables targeted issue and efficient issue resolution by filtering cases by environment group. 



### Limitations

The following modules don't support environment groups as a filter: 

  * **SOAR Search** : When searching for cases, you can't filter by environment groups. You must manually select individual environments.
  * **SOAR Reports** : When creating reports, environment groups aren't available as a filter. You must select individual environments to define the report scope.



## Create an environment group

To create an environment group: 

  1. Go to **SOAR Settings** > **Organization** > **Environments**.
  2. Click the **Groups** tab.
  3. Click add**Add**.
  4. Enter the environment group name and description.
  5. Add as many environments to the group as needed.



You can modify environment groups at any time. To do so, select **Manage Groups** and edit existing groups as needed.

## Delete environment groups

When you delete an environment group, the action doesn't delete its associated environments. However, if the deleted environment group is the only one associated with a playbook, the system also deletes the playbook. 

To delete an environment group: 

  1. Go to **SOAR Settings** > **Organization** > **Environments**.
  2. Click the **Groups** tab.
  3. Click **Manage Groups**.
  4. Click delete**Delete**.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
