---
url: https://docs.cloud.google.com/data-studio/remove-or-reconnect-access-to-your-google-account/
title: Remove or reconnect Data Studio's access to your Google Account \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:00:41.836042+00:00
---

# Remove or reconnect Data Studio's access to your Google Account  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/remove-or-reconnect-access-to-your-google-account/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Remove or reconnect Data Studio's access to your Google Account Stay organized with collections  Save and categorize content based on your preferences. 

You can remove or reconnect Data Studio's access to your Google Account, which can help resolve data source authorization errors. You can also control which products Data Studio can access, such as Analytics or Google Ads. Data Studio requires this access to create data sources, which it uses to build reports and dashboards from your data.

[ Take me there now ](https://myaccount.google.com/permissions)

To remove Data Studio access to your Google Account:

  1. Go to [My Account](https://myaccount.google.com/).
  2. On the left, click **Security**.
  3. Scroll down, then under **Your connections to third-party apps with account access** , click **Manage third-party access**.
  4. Click **Data Studio.** You may need to click **See all connections** to find this.
  5. Click **REMOVE ACCESS.**
  6. Click **OK**.

**Warning:** Removing Data Studio from your authorized apps will disable all the data sources you've created using Google product connectors. Data sources based on non-Google data, such as MySQL, won't be affected.

## Reconnect your account to Data Studio

To reconnect Data Studio to your Google Account, create a new data source based on a Google product. You will be asked to grant Data Studio access to your account. During this process, you may also see an OAuth consent popup asking you to authorize the `datastudio.firstparty` scope to use the Data Studio API. Click **Continue** (or **Allow**) to grant consent.

**Note:** Removing and then reconnecting your Google Account to Data Studio can sometimes resolve data source authorization errors. You won't lose any of your reports or data sources when you do this.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
