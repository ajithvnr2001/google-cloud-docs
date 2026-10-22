---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/create-a-managedmanagedplus-user/
title: Create a managed user \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:43.112416+00:00
---

# Create a managed user  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/create-a-managedmanagedplus-user/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a managed user

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This page only applies to customers who haven't migrated to Google Cloud. After completing Stage 1 of the migration, see [Feature RBAC using Cloud IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access#overview-perm-role) to manage roles and permissions for Google SecOps including SOAR.

The **Managed** and **Managed-plus** user types are hybrid roles—combining aspects of the Collaborator and Full User roles—designed specifically for end-customers of a Managed Security Service Provider (MSSP). These roles enable flexible, scoped access to the platform. .

  * **Managed user** :
    * useful for an MSSP who wants to run a hybrid SOC together with their end customers.
    * has full case management capabilities on their own environment (similar to the MSSP analyst).
  * **Managed-plus user** :
    * Has the same permissions as a managed user, but with the added ability to build and edit playbooks in their own environment.
    * Can view playbooks running in their environment such as **All environments** playbooks, but won't be able to edit playbooks if they don't have permissions to all the environments that the playbook is associated with. For example, a user with permissions to the environment "North England" only will be able to view but not edit a playbook that is running on "North England", "South England" and "East England" environments. This user won't see that this playbook is running on "South England" and "East England" environments.



The MSSP is responsible for managing the Content Hub, configuring the integrations and agents and customizing actions in the Integrated Development Environment (IDE) for the Managed-plus user.

The high-level steps to add a new managed or managed-plus user are the same as that of adding other types of users:

  1. Purchase the license for the required number of users with your Account Manager.
  2. Select the predefined **managed user** or **managed-plus user** permission groups, or create a new one.
  3. Create a new user.



## Purchase managed user or managed-plus user license

To purchase a license for a managed user or managed-plus user, follow these steps:

  1. Arrange a license for the required number of managed users or managed-plus users.
  2. Go to **Settings > Organizations > License Management** to view the details.



## Set up a permission group

To set up a permission group for a managed user or managed-plus user, follow these steps:

  1. Go to **Settings > Organization > Permissions**.
  2. In the **License Types** list, select **Managed User** or **Managed-Plus User** , or create a new one.
  3. Select the categories that you want to be accessible. Note that the playbooks module isn't available for the managed User.
  4. Select the type of **Landing Page** from the list.
  5. Click **Save**.



## Create a Managed or Managed-plus user (SOAR standalone customers only)

To create a managed or managed-plus user, follow these steps:

  1. Go to **Settings > Organization > User Management.**
  2. In the **User Management** page, click add **Add** ; the **Add User** dialog appears.
  3. In the **License Type** field, select **Managed User** or **Managed-Plus User**.
  4. In the **Permission Group** list, select the **Managed User** or **Managed-Plus User** Group or any new group that you created.
  5. Select the **Read/Write** permissions as required.
  6. Click **Add**. An email invitation is sent automatically to the user. The invitation status remains **Pending** until they accept the invitation to join Google SecOps SOAR and create a password. 



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
