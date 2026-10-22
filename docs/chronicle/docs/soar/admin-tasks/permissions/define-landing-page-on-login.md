---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/define-landing-page-on-login/
title: Define a landing page \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:12.594438+00:00
---

# Define a landing page  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/define-landing-page-on-login/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Define a landing page

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

Administrators can define a specific page for Google Security Operations users to see after they sign in to the platform. Users are directed to their assigned landing page based on their permission group. Permission groups are determined by the user's Identity Provider (IdP) or email group, depending on their authentication method. This makes sure that users are directed to the most relevant section of the platform. Users can return to their landing page at any time by clicking  home **Home**.

The default landing pages for each permission group include:

User Role | Permissions  
---|---  
Admins | **Cases > Case overview**  
Readers | **Cases > Case overview**  
View-only | **Dashboards**  
Collaborators | **Your Workdesk > Pending Actions**  
Basic | **Cases > Case overview**  
  
There are two other options for landing pages for Google SecOps users:

  * [ SIEM Search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
  * [ Legacy SIEM Search:](https://docs.cloud.google.com/chronicle/docs/review-security-alert) This page can't be accessed through the Google SecOps navigation menu. 



## Define a landing page

**Note:** After migrating to Google Cloud, you can control the landing page for each user. To do so, select the **User Preferences** option from your avatar. For more information, see [Migrate to Google Cloud](/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp).

To define a landing page for a permission group, follow these steps:

  1. Go to **SOAR Settings > Organization > Permissions**.
  2. Select the required permission group or click  add **Add Permission Group** to create a new group.
  3. Select the **Landing Page** from the list.
  4. Click **Save**. 



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
