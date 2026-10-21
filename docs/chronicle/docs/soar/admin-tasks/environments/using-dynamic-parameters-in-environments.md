---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/using-dynamic-parameters-in-environments/
title: Configure custom environment groups \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:43.570100+00:00
---

# Configure custom environment groups  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/using-dynamic-parameters-in-environments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure custom environment groups

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to use dynamic parameters to create custom categories or groups for your environments in Google Security Operations. Dynamic parameters are especially useful for playbooks, letting you define custom triggers, actions, or conditions based on these parameters. This enhanced customization benefits both enterprises and Managed Security Service Providers (MSSPs) who manage multiple tenants. 

## Add a dynamic parameter

To add a dynamic parameter, follow these steps: 

  1. Go to **Settings** > **Organization** > **Environments**.
  2. On the **Environments** page, click format_list_bulleted **List** and select **Add Dynamic Parameters**.  

  3. In the **Dynamic Parameters** dialog, click add **Add** to add a new parameter.
  4. Enter a name for the parameter (for example,`Service Package`).
  5. Choose one of the following ways to set the parameter value:
     * Enter a string and a default value. The system applies the default value to all existing environments.
     * Select **List** , enter your values in the **List Content** field, and press **Enter** after each value. Then, select a default value from the list.
  6. Click **Save** > **Done**. The system applies the dynamic parameter and its selected default value to all existing environments and displays it on the main page.



## Edit parameter values in bulk

To update multiple parameter values at once, export them to a spreadsheet, make changes, and re-import them.

To edit parameters in bulk using export or import, follow these steps:

  1. Click format_list_bulleted **List** and select **Export Dynamic Parameters**.
  2. In the spreadsheet, edit the values as needed. You can't change the **Parameter** names or **Environment** names.
  3. When finished, click format_list_bulleted **List** and select **Import Dynamic Parameters**.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
