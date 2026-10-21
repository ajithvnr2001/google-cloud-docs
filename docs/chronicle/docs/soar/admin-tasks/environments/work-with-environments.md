---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/work-with-environments/
title: Environments overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:42.931625+00:00
---

# Environments overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/work-with-environments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Environments overview

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

Environments represent distinct networks, customers, or business units managed by your SOC or Managed Security Service Provider (MSSP). They help segment data, actions, and visibility across different operational contexts. This document explains how to work with your environments to make it easier to manage security operations for multiple tenants or organizational divisions from a single platform. 

## Add a new environment

When you add a new environment, it lets your SOC or MSSP manage and monitor distinct networks, customers, or business units within the platform. This setup helps isolate data and workflows across different environments while maintaining centralized visibility and control. **Note:** To prevent data loss, the platform ingests alerts into environments that don't exist. The connector (or webhook or API) creates these by setting the environment manually. You must create the environment to access the case in the platform. 

The platform provides a predefined environment named **Default Environment** by default. 

Use the following steps to configure and register a new environment in Google Security Operations

  1. Go to **Settings** > **Organization** > **Environments**. 
  2. Click  add  **Add**. 
  3. In the **Add Environment** dialog, enter the required information. 
  4. Optional: Select the **Append to all Users and API Keys** checkbox to automatically assign the new environment to all existing users and API keys. You can also add an alias if a third-party integration uses a different tenant name. 
  5. If the **Allow Data Retention Period per Environment** checkbox is not selected in **Settings** > **Advanced** > **General** , specify the time period for deleting information related to closed cases in this environment. 
  6. Click **Create**. The new environment appears in the list of environments. 

**Note:** You can't rename environments once they're created. 

## Allow access to other environments

Google Security Operations offers you a way to create a customized Cross Environment Policy that works for your organization's needs. Use the **Cross Environment Policy** settings to choose the required permissions for assigning users to cases and moving cases between environments.

### Assign cases in environments

With the **Assign Case** option, you can let users have access to a specific cases in environments where they don't have default permissions. This option is useful when you need to investigate or collaborate on cases outside your assigned environment. With this permission enabled, you can also assign manual actions, create case tasks, and add mentions in the case wall or chat. As a best practice, we recommend keeping the **Assign Case** setting at **Prevent** (default).

**Note:** You can assign a case in another environment to an individual user, but not to a SOC role.

### Move cases between environments

Under **Move Case** option, you can control whether users are granted permission to move cases between environments. This is helpful when you investigate alerts in the context of a different environment within the organization.

### Assign cases across environments

To assign a case, follow these steps:

  1. Go to **Settings** > **Advanced** > **General**.
  2. In the **Cross Environment Policy** dialog, under **Assign Case** , select **Allow users to assign cases to users from other environments**.  

  3. Click **Save**.



### Move cases to a different environment

To move cases to a different environment, follow these steps:

  1. Click **Settings** > **Advanced** > **General**.
  2. In the **Cross Environment Policy** dialog, under **Move Case** , select **Allow users to move cases between environments**.  

  3. Click **Save**.  




## Delete an environment

To delete an environment, follow these steps: 

  1. Go to **Settings** > **Organization** > **Environments**.
  2. Select the required environment, and then click edit**Edit**. 
  3. In the **Edit Environment** dialog, click delete**Delete**. The **Delete** page lists all configurations and utilities associated with this environment. Once you delete this environment, you can't undo this action. 
  4. Click **Confirm**. 



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
