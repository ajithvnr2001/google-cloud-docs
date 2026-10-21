---
url: https://docs.cloud.google.com/data-studio/set-a-default-google-cloud-project-for-pro/
title: Set a default Google Cloud project for Data Studio Pro \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:15.799954+00:00
---

# Set a default Google Cloud project for Data Studio Pro  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/set-a-default-google-cloud-project-for-pro/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Set a default Google Cloud project for Data Studio Pro Stay organized with collections  Save and categorize content based on your preferences. 

> _This article is intended for organization administrators._

As an organization administrator, you can set a default project for content that is created by Data Studio Pro subscribers. When you set a default project, Pro subscribers can create content only in their Pro Sandbox or a team workspace. Their existing content will be moved to their personal **Sandbox** location under the default project, and Pro subscribers will no longer have **Owned by me** as an available location in which to create Data Studio content.

Content won't be moved if it belongs to users in your organization who either are not Data Studio Pro subscribers or are Pro subscribers who are associated with a different Google Cloud project. These users can still create content in their **Owned by me** location.

## Before you begin

You must be assigned the [Services Admin](https://support.google.com/a/answer/2405986#services_admin) role in Google Workspace to perform the steps that are described in the next section.

## Set a default project for Pro content

**Important:** Users in your organization must be Data Studio Pro subscribers in the project that you select.

To set a default Pro project, follow these steps:

  1. Sign in to the [Google Admin console](https://admin.google.com/) with the account that has the required role.
  2. In the Admin console, go to **Menu** > **Apps** > **Additional Google Services** > **Looker Studio**.
  3. Select the Google Group or organizational unit that you want this setting to apply to.
  4. Expand the **Looker Studio Pro** settings panel.
  5. Edit the **Default Pro project** settings.
  6. Enter the ID of the Google Cloud project that you want to use as the default location for Data Studio Pro content.
  7. Click **SAVE**.



## Effects of setting a default Pro project

Setting a default project for Data Studio Pro content has the following effects:

  * All Data Studio Pro users in the selected group or organizational unit who belong to the default Pro project no longer have **Owned by me** as an available location in the Data Studio Pro navigation.
  * Any content that was previously owned by these users moves to their personal **Sandbox** location under the default project.
  * New users who are added to the Data Studio Pro subscription that is associated with the default project have their content moved to their personal **Sandbox** location under the default project.

**Note:** Moving existing content from a user's **Owned by me** location to the default Pro project can take up to 48 hours.

## Change the default Pro project

You can change the default Pro project at any time. However, existing content in the previous default Pro project won't be moved to the new default project. Users may manually move their content to the new project if they are members of that project's Pro subscription.

## Related resources

  * [Subscribe to Data Studio Pro](https://docs.cloud.google.com/data-studio/pro-subscription-overview)
  * [Add or remove Data Studio Pro users](https://docs.cloud.google.com/data-studio/edit-a-pro-subscription)
  * [Add or removeData Studio Pro licenses](https://docs.cloud.google.com/data-studio/edit-a-pro-subscription)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
