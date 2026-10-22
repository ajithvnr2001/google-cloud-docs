---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/create-a-view-only-user/
title: Create a view-only user \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:53.704474+00:00
---

# Create a view-only user  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/create-a-view-only-user/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a view-only user

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This page only applies to customers who haven't migrated to Google Cloud. After completing Stage 1 of the migration, see [Feature RBAC using Cloud IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access#overview-perm-role) to manage roles and permissions for Google SecOps including SOAR.

The administrator can add view only users to the Google Security Operations platform. This can be useful when you want somebody in your organization or an MSSP customer to be aware of information pertaining to specific places in the platform but without having the ability to change them.

The procedure to add these users is the same as that of adding regular users:

  1. Purchase the license for the required number of users with your Account Manager.
  2. Create a new view only user group or use the predefined view only group.
  3. Create a new user.



## Purchase a view only license

  1. Arrange a license for the required number of view only users.
  2. Go to **Settings > Organizations > License Management** to view the details. 



## Set up a permission group

  1. Go to **Settings > Organization > Permissions**.
  2. Click the predefined permissions group called **View Only** or create a new one.
  3. Select the **landing page** from the list. 
  4. Click **Save**.



## Create a view only user - for SOAR standalone users only

  1. Go to **Settings > Organization > User Management**.
  2. Click add **Add** to open the **Add User** dialog.
  3. In the **License Type** field, select the **View Only** type.
  4. In the **Permission Group** list, select the **View Only** group (or any new group) that you created for **View Only** users. 
  5. Fill out the rest of the fields as required.
  6. Click **Add**. An email invitation is sent automatically to the user. Their status remains **Pending** until they accept the invitation to join Google Security Operations SOAR and create a password.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
