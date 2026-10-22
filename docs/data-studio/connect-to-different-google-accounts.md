---
url: https://docs.cloud.google.com/data-studio/connect-to-different-google-accounts/
title: Connect Data Studio to different Google Accounts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:33.666996+00:00
---

# Connect Data Studio to different Google Accounts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-different-google-accounts/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect Data Studio to different Google Accounts Stay organized with collections  Save and categorize content based on your preferences. 

Access to Google data is based on the account with which you sign into Data Studio. This means that a data source can only directly connect to a single Google Account. To connect Data Studio to different accounts, you have the following options:

## Share the data with yourself

Suppose you want to create a report with data from Google Sheets belonging to 2 different Google Accounts? One solution is to share the Sheet with each account. Then either account can create data sources using those Sheets.

Another solution is to create data sources in one account, then share those data sources with the other account. For example, suppose you have data in accounts A and B, and you want to create Data Studio reports using account A. To include data from account B, you could do the following:

  1. Sign into Data Studio using the account B.
  2. Create the data source.
  3. Make sure the data source uses Owner's Credentials.
  4. Share the data source with account A, with edit permission.



You can then return to account A and use the shared data source in your reports.

Note that only the data source owner can refresh or reconnect a data source, so you'll need to make any schema changes to the shared data source as account B.

## Use the data control

The [data control](https://docs.cloud.google.com/data-studio/data-control) allows a report viewer to switch the report to any account to which they have access. The data control is available for a subset of the available connectors.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
