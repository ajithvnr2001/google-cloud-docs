---
url: https://docs.cloud.google.com/integration-connectors/docs/suspend-resume-connection/
title: Suspend and resume a connection \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:33.561399+00:00
---

# Suspend and resume a connection  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/suspend-resume-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Suspend and resume a connection

This page describes how to suspend and resume a connection. If you suspend a connection, the connection will not accept any incoming or outgoing traffic, and you are not billed for a connection that is in a suspended state.

## Suspend a connection

To suspend a connection, perform the following steps:

  1. In the [Cloud console](https://console.cloud.google.com/), go to the **Integration Connectors > Connections** page, and then select your Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

This page lists all the available connections.

  2. Click on the connection that you want to suspend. 

This opens the edit connection page.

  3. Click **Suspend** , and then click **Confirm** in the confirmation dialog. 

After you suspend the connection, its status is shown as **Inactive** in the [Connections page](https://console.cloud.google.com/connectors/connections).


**Note:** Suspending a connection frees up the nodes used by the connection, and hence you aren't billed for connections in the suspended state.

## Resume a suspended connection

To resume a suspended connection, perform the following steps:

  1. In the [Cloud console](https://console.cloud.google.com/), go to the **Integration Connectors > Connections** page, and then select your Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

This page lists all the available connections.

  2. Click on the connection that you want to resume. 

This opens the edit connection page.

  3. Click **Resume** , and then click **Confirm** in the confirmation dialog. 

After you resume the connection, its status is shown as **Active** in the [Connections page](https://console.cloud.google.com/connectors/connections).


**Note:** After you resume a connection from a suspended state, the connection becomes billable. For more information, see [Integration Connectors pricing](https://docs.cloud.google.com/application-integration/pricing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
