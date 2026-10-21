---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/how-do-i-add-a-new-user-to-the-platform/
title: Manage SOAR standalone users \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:15:09.678496+00:00
---

# Manage SOAR standalone users  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/how-do-i-add-a-new-user-to-the-platform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage SOAR standalone users

Supported in:

[ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This document applies only to the standalone Google SecOps SOAR platform. 

**Note:** This section only applies if you have not yet completed Stage 1 of [SOAR Migration to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp). After the completion of Stage 1, refer to [Access Google Secops instance](https://docs.cloud.google.com/chronicle/docs/onboard/log-in-to-new-instance).

This document is intended for users of the Google Security Operations SOAR platform who want to add new users. 

## User types

The Google Security Operations SOAR user types include:

  * **Standard users** : can be given various permissions and have edit rights to the platform as you defined them.
  * **View-only users** : can only view certain parts of the platform based on their assigned permissions. They require a special license. For details, see [Create a view-only user](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/create-a-view-only-user).
  * **Collaborator users** : can have edit or view permissions for specific platform modules. For more information on this user type, see [Benefits of adding a collaborator user](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/benefits-of-adding-a-collaborator-user). 
  * **Managed users:** Have full case management permissions, letting them participate in a hybrid SOC model alongside a Managed Security Service Provider (MSSP). **Note:** Managed users have no access to edit playbooks. For more information on managed users, see [Create a Managed or Managed-plus user](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/create-a-managedmanagedplus-user).
  * **Managed-plus users** : Have the same case management permissions as managed users, with the additional ability to build and edit playbooks within their own environment. For more information on Managed-plus users, see [Create a Managed or Managed-plus user](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/create-a-managedmanagedplus-user).



## Add a new user

To add a new user to the Google Security Operations SOAR platform, follow these steps:

  1. Go to **Settings > Organization > User Management**.
  2. Click add**Add**.
  3. Fill out the required information in the fields. You can edit this information after the user is created. The **Login ID** field must contain an email address for internal users. If you edit the **Login ID** field, the user's status changes to **Pending** until the next sign-in.
**Note:** For SAML authentication, select the required SAML provider in the **User Type** field. The **Login ID** field must conform to your SAML specifications, and the **Email** field is intended for notification purposes only. 
  4. Click **Add**. The new user appears in the user list, and an email invitation is automatically sent.



## Set environment access

If you select a permission group with edit permissions for **All Environments** , the user is granted access to all environments by default. To change this at the permission group level, follow these steps:

  1. On the **Permissions** page, select **None** for **All Environments**.
  2. Select one or more specific environments for the user to have access to.
  3. Click **Add**. The new user appears in the list of users, and an email invitation is automatically sent.
  4. For internal users, the status remains **Pending** until they accept the invitation and create a password.

The invitation link is valid for 3 days. The administrator can resend the invitation on the **User Management** page.

For SAML users, the status remains **Pending** until the initial login. They can sign in directly to the platform without the need to use the invitation email.




You can also [map users with multiple control access parameters](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-with-multiple-control-access-parameters).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
