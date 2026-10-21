---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/stream-processing-operations/
title: Streaming processing operations \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:43.340689+00:00
---

# Streaming processing operations  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/stream-processing-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Streaming processing operations

From release v1.4.0 onwards, you can start and stop the stream processing using the API and the web interface. This is a convenient feature that lets you stop the ingestion in case of a configuration error. This is convenient, because having an erroneous configurations might result in the messages being rejected and sent to the dead-letter queue (which might take more manual effort to replay them back), or erroneously parsed messaged persisted in tables (which will need manual seek and removal).

The API provides the following functionalities:

  * Start the ingestion.
  * Stop the ingestion.
  * Getting the status of the ingestion.

**Note:** Stopping or starting the ingestion impacts all of the services involved in all the processing pipelines. All of the processing metrics in the monitoring dashboard will indicate that they are stopped, and the internal queues depth won't change.

![Web interface to enable the stream processing](https://docs.cloud.google.com/static/manufacturing-data-engine/images/processing-enabled.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
