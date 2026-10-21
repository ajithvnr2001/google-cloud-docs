---
url: https://docs.cloud.google.com/data-studio/enable-and-disable-gemini-in-data-studio/
title: Enable and disable Gemini in Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:17.746394+00:00
---

# Enable and disable Gemini in Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/enable-and-disable-gemini-in-data-studio/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Enable and disable Gemini in Data Studio Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** While in preview, Gemini in Data Studio features are available at no additional cost. At the end of this Preview period, usage of Gemini in Data Studio features may require an additional fee.

This documentation page describes the settings that are available to manage Gemini in Data Studio as part of a Data Studio Pro subscription. It covers the following topics:

  * The enablement options that are available for Data Studio
  * How to enable and disable Gemini in Data Studio
  * The permissions that are required to use Gemini in Data Studio features



## What is Gemini in Data Studio?

Gemini in Data Studio represents a series of features in the [Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview) portfolio that provides generative AI-powered assistance to help you analyze and gain valuable insights from your data.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

For more information about the types of tasks that Gemini in Data Studio can assist with, see the [Gemini in Data Studio overview](https://docs.cloud.google.com/data-studio/gemini-overview) documentation page.

## Before you begin

Before Gemini in Data Studio features can be enabled, the following requirements must be met:

  * Your organization must have a Data Studio Pro subscription

  * To view and modify Gemini in Data Studio settings in Data Studio:

    * For a standard self-service subscription, you must be assigned a role that contains the `lookerstudio.pro.manage` IAM permission for the Google Cloud project that you use for your Data Studio Pro subscription. The `lookerstudio.pro.manage` permission is included in the [Data Studio Pro Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.proManager) (`roles/lookerstudio.proManager`) and [Owner](https://docs.cloud.google.com/iam/docs/understanding-roles#owner) (`roles/owner`) IAM roles. You may also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).
    * For a "whole organization, monthly active user (MAU)" subscription, you must be assigned a role that contains the `Manage Data Studio Settings` Workspace privilege, which is included in the [Services Admin](https://support.google.com/a/answer/2405986#services_admin) and [Super Admin](https://support.google.com/a/answer/2405986#super_admin) roles in Google Workspace. You may also be able to get this privilege with a [custom admin role](https://support.google.com/a/answer/2406043). Additionally, your subscription must be [linked to a Google Cloud project](https://docs.cloud.google.com/data-studio/set-a-default-google-cloud-project-for-pro).



For more information about Data Studio Pro subscription types, see the [Data Studio Pro subscription overview](https://docs.cloud.google.com/data-studio/pro-subscription-overview).

## Gemini in Data Studio settings management

You can manage Gemini in Data Studio settings on the **Gemini in Data Studio** page in the Data Studio user settings. Although you're managing these settings for a Google Cloud project, the settings that you configure here will actually apply to the users under the Data Studio Pro subscription that is associated with the project.

To access the **Gemini in Data Studio** page, click settings **User settings** and select the **Gemini settings** tab.

From the **Gemini in Data Studio** page, you can view and manage the following settings:

  * **Enabled** : When this setting is enabled, Gemini in Data Studio features are available for the users of the Data Studio Pro subscription that is associated with the Google Cloud project that you are managing.
  * **Trusted Tester features** : When this setting is enabled, users of the selected Data Studio Pro subscription can access the Trusted Tester capabilities of Gemini in Data Studio. **This setting must be enabled to allow users to access the Gemini features that are in Preview.**
  * **Enable Trusted Tester Data Use** : When this setting is enabled, you consent to your data being used by Google as described in the [Gemini for Google Cloud Trusted Tester Program terms](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview). This setting is optional.
  * **Code Interpreter** : When this setting is enabled, Data Studio Pro users can use the [Code Interpreter](https://docs.cloud.google.com/data-studio/conversational-analytics-code-interpreter) in [Conversational Analytics](https://docs.cloud.google.com/data-studio/conversational-analytics-overview). This setting can be enabled only when the **Enabled** setting is on for Gemini in Data Studio. This setting is disabled by default when the **Trusted Tester features** setting is disabled. This setting is enabled by default when both Gemini in Data Studio is enabled and the **Trusted Tester features** setting is enabled.



## Enable and disable Gemini in Data Studio

**Note:** The following conditions affect the default enablement for Gemini in Data Studio for Data Studio Pro subscriptions: 

  * Gemini in Data Studio is disabled by default for Google Cloud projects that are associated with a canceled Data Studio Pro subscription.
  * Gemini in Data Studio is enabled by default for all Data Studio Pro subscriptions that are created on or after June 3, 2025.



To enable Gemini in Data Studio for users under a Data Studio Pro subscription, follow these steps for the Google Cloud project that is associated with that subscription:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. Click settings **User settings** , and select the **Gemini settings** tab to open the **Gemini in Data Studio** page.
  3. On the **Gemini in Data Studio** page, turn on the **Enabled** setting for a selected project. When this setting is enabled, you can also choose to enable the **Trusted Tester features** setting, which enables the **Trusted Tester data use** and the **Code Interpreter** settings automatically. You can disable the **Trusted Tester data use** and the **Code Interpreter** settings manually if needed.



To disable Gemini in Data Studio and revoke access to Gemini in Data Studio features for all users under a Data Studio Pro subscription, follow these steps for the Google Cloud project that is associated with that subscription:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. Click the settings **User settings** icon and select the **Gemini settings** tab.
  3. On the **Gemini in Data Studio** page, turn off the **Enabled** setting for a selected project. If you turn off the **Enabled** setting, then the **Trusted Tester features** , **Trusted Tester data use** , and **Code Interpreter** settings, if enabled, are disabled automatically.



## Permissions to use Gemini in Data Studio features

To use Gemini in Data Studio features, users must be granted the following roles or privileges:

  * To create calculated fields, users must be assigned an [Editor](https://docs.cloud.google.com/data-studio/roles-and-permissions#basic_roles) role.
  * To add Data Studio content to your Slides presentation, users must be assigned a Viewer or Editor role in Data Studio and have the [Editor or Owner](https://support.google.com/docs/answer/2494822#zippy=%2Cunderstand-share-permissions) permission level for the Slides presentation.



## Provide feedback

You can provide feedback about each Gemini in Data Studio feature. Instructions for how to submit feedback are included in the documentation for each feature.

## Related resources

  * [Gemini in Data Studio overview](https://docs.cloud.google.com/data-studio/gemini-overview)
  * [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
