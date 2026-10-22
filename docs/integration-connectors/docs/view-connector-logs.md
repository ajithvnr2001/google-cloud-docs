---
url: https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs/
title: View Integration Connectors logs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:03.186600+00:00
---

# View Integration Connectors logs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View Integration Connectors logs

This page describes the logging data available for a connector and how you can access this data using Cloud Logging. 

Cloud Logging is a fully managed service that allows you to store, search, analyze, monitor, and alert on logging data and events from Google Cloud. For more information about Cloud Logging, see [Cloud Logging documentation](https://docs.cloud.google.com/logging/docs). 

You can configure a connector to log at any of the following levels:

  * **Error:** Logs error messages that occur during failures such as connection failures, and authentication failures.   
Warning logs for non-critical messages also get logged. For example, if you are accessing an unsupported entity, a warning message is logged. 
  * **Info:** Logs information about operations and executions, including the requests and responses the connector makes to your backend system. 
  * **Debug:** Logs detailed tracing information which would be useful for debugging any issues in connection or execution. This log will have all the information that is logged at the **Info** and **Error** levels, and additional details such as SSL information, network calls, and other tracing information. 

**Note:** Logging is disabled by default for a connector as enabling logging might impact performance. You can enable logging when configuring a new connector or if you already have a connector, you can enable logging by editing the connector. To understand how to edit a connector, see [Edit connection](https://docs.cloud.google.com/integration-connectors/docs/manage-connections).

## View logs

If logging is enabled for a connector, you can view the logs in the Logs Explorer. To view the logs in the Google Cloud console, do the following steps:

  1. Go to the Logs Explorer in the Google Cloud console: 

[Go to Logs Explorer](https://console.cloud.google.com/logs)

To get a better understanding of the Logs Explorer, see [Logs Explorer interface](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface). 

  2. In the **Query** tab, enter: 
         
         resource.type="connectors.googleapis.com/Connection"
         

This sample query shows logs for all the connections across all the regions. You can further filter the logs based on region and a connection name. For example, the following query shows logs for the `cloud-storage-con-1` connection, that is configured in the `us-central1` location. 
         
         resource.type="connectors.googleapis.com/Connection"
         resource.labels.location="us-central1"
         resource.labels.connection="cloud-storage-con-1"
         

  3. You can filter the search results further by time, severity, and log name.
  4. Click **Run query**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
