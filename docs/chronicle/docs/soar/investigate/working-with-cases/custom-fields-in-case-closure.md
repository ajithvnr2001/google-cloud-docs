---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/custom-fields-in-case-closure/
title: Manage custom case closure fields \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:56.971743+00:00
---

# Manage custom case closure fields  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/custom-fields-in-case-closure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage custom case closure fields

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to use custom fields to collect and manage information during the case closure process.

## Create a custom field

You must create a custom field with a specific scope before it can be used in the **Close Case** dialog. The **Scope** , **Type** , and **Name** of a custom field are mandatory and can't be modified after it's saved.

To create a custom field for the **Close Case** dialog, follow these steps:

  1. Go to **SOAR Settings > Case Data > Custom Fields**.
  2. Click  Add **Add Custom Fields**.
  3. Set the **Scope** to either **Case** or **All**. Custom fields with an **Alert** scope can't be used in the **Close Case** dialog.
  4. Enter a custom field **Name**.
  5. Select a custom field **Type** from the list: 
     * **Free Text** : Enter any text, up to 1,024 characters.
     * **Radio Button** : Provides two customizable options for selection.
     * **Single Select** : List with a single option to select. This type supports a maximum of 1,024 characters, with each option name limited to 255 characters.
     * **Multi Select** : List with multiple options to select. This type supports a maximum of 1,024 characters, with each option name limited to 255 characters.
     * **Calendar** : A date and time field. The default format is `DD/MM/YYYY HH:MM:SS`.
  6. Click **Save**.



## Add a custom field to the Close Case dialog

After you create a custom field with the correct scope, you can add it to the **Close Case** dialog.

  1. Go to **SOAR Settings > Case Data > Close Case**.
  2. In the **Custom Fields** section, click  settings  **Settings**.
  3. In the **Case Closure Fields** side drawer, click **Manage Custom Fields**.
  4. Select the custom fields you want to display in the **Close Case** dialog. You can select up to 1,000 custom fields.
  5. Click **Save**.



## Close a single case

When you close a case individually, you can enter additional information for the custom fields you added to the **Close Case** dialog.

  1. Go to the case you want to close, then click ![closecaseicon](https://docs.cloud.google.com/static/chronicle/images/soar/closecaseicon.png)**Close Case**.
  2. In the **Close Case** dialog, the standard **Reason** and **Root Cause** fields appear alongside any custom fields that have been added. Select the appropriate options for your case and enter any additional comments. These comments will be posted on the **Case Wall**.
  3. Click **Close**.

**Note:** The **Close Case** dialog for bulk operations doesn't include custom fields. Custom field values can differ between cases. To update or use custom fields, you must close each case individually. 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
