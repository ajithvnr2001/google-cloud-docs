---
url: https://docs.cloud.google.com/apigee/docs/api-platform/debug/offline-trace/
title: Using Offline Debug \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:54.927481+00:00
---

# Using Offline Debug  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/debug/offline-trace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Using Offline Debug Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The Offline Debug tool lets you view and analyze "offline" debug sessions that were [ previously downloaded](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace#downloading-a-debug-session) in the **Debug** view in the Proxy Editor. A saved debug session is essentially a "recording" of a debug session, and can be useful for cases where troubleshooting and further analysis is required. The UI for the Offline Debug tool is similar to the **Debug** view in the Proxy Editor.

To learn about the Debug Tool UI and on downloading debug sessions, see [ Using Debug](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace).

To view downloaded debug data using Offline Debug:

  1. In the Google Cloud console, go to the **Apigee > Proxy development > Offline Debug** page. 

[Go to Offline Debug](https://console.cloud.google.com/apigee/offline-debug)

  2. The **Offline Debug** view displays:

![Click to view larger image](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/offline-debug-view-v2.png)![](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/offline-debug-view-v2.png)
  3. To load data into the **Offline Debug** view, click **Open Debug Session** , select a [ previously downloaded](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace#download) offline debug session file in JSON format, and then click **Open**.

**Note:** When you download a debug session in the Proxy Editor **Debug** view, the name of the download file has the form `debug-{session ID}.json`, where `{session id}` is the ID of the debug session; however, you can rename the file if you wish.

The Apigee UI loads the debug file's data and displays all of the transactions in the list in the **Transactions** panel.

![Click to view larger image](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/session-loaded-in-offline-debug-v2.png)![Offline
          Offline Debug view with debug file loaded](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/session-loaded-in-offline-debug-v2.png)
  4. Click the row for the transaction in the **Transactions** panel to display the transaction in the **Transaction Map**. ![Click to view larger image](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/session-downloaded-transaction-map.png)![Downloaded transaction map](https://docs.cloud.google.com/static/apigee/docs/api-platform/debug/images/session-downloaded-transaction-map.png)



From here, you can explore the debug session just as you would for a newly-created debug session. See [ Creating a debug session](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace#creating-a-debug-session) for more information. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
