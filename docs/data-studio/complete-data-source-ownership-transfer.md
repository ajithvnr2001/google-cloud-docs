---
url: https://docs.cloud.google.com/data-studio/complete-data-source-ownership-transfer/
title: Complete data source ownership transfer \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:14:55.628333+00:00
---

# Complete data source ownership transfer  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/complete-data-source-ownership-transfer/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Complete data source ownership transfer Stay organized with collections  Save and categorize content based on your preferences. 

When a data source changes ownership, you must claim it in Data Studio to keep your reports working without interruption. Claiming the transferred data source reconnects your credentials so viewers can continue visualizing data seamlessly. If you aren't the new owner, contact them and share this document to complete the transfer.

To complete data source ownership transfer, perform the following steps:

  1. In the message bar at the top of the page, click **need to be fixed**. This will open the **Resource > Manage added data sources** page.
  2. For each data source in the report shown as "Ownership changed," click **FIX IT**.
  3. If you have access to the [data set](https://docs.cloud.google.com/data-studio/dataset), you'll see the data source configuration page.
  4. In the top left, click **EDIT CONNECTION**.
  5. Make any changes to the data source connection, then in the upper right, click **RECONNECT**.



If you don't have access to the original data set, you'll need to edit the connection and select a new data set.

**Important:** Complete the ownership transfer as soon as possible. See the following section for more information.

## Additional information

  * Transferring ownership is a 3 step process: 
    1. The original owner must first share the data source with the new owner.
    2. The original owner can then [transfer ownership of the data source](https://docs.cloud.google.com/data-studio/transfer-ownership) to a new owner.
    3. The new owner "claims" (transfers their credentials to) the data source by reconnecting it.
  * As a temporary condition, any reports with unclaimed data sources will continue to work, but will show editors a message at the top of the report. In the near future, **these reports may stop working until the data sources are claimed.**
  * You can see which data sources need to be claimed by editing the report and going to the **Resource > Manage added data sources** page.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
