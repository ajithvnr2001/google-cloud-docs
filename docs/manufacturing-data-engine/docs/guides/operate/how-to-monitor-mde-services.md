---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/how-to-monitor-mde-services/
title: Monitor services \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:49.610398+00:00
---

# Monitor services  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/how-to-monitor-mde-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor services

This guide describes how to use the underlying Google Cloud services and Manufacturing Data Engine (MDE) metrics to proactively identify processing pipeline issues, diagnose configuration or system problems, and monitor system scaling in response to current load.

## Metrics published by MDE

MDE publishes custom metrics for its different services, all of them offer a p50, p95, and max percentiles.

Metric | Definition  
---|---  
custom/mde/configuration/error/count | Errors encountered processing messages in configuration manager service .  
custom/mde/configuration/messages/count | Number of messages processed by the configuration manager service.  
custom/mde/configuration/processing/time | Message processing time in the configuration manager service.  
custom/mde/configuration/tags/cached/count | Total count of the cached tag requested from the configuration manager service.  
custom/mde/configuration/tags/created/count | Total count of the created tags requested from the configuration manager service.  
custom/mde/configuration/messages/pubsub/shift/publishing | Time difference between publishing the message to PubSub and the event timestamp in the configuration manager.  
custom/mde/configuration/messages/pubsub/shift/receiving | Time difference between receiving the message from PubSub and the event timestamp in the configuration manager.  
custom/mde/metadata/error/count | Errors encountered processing messages in metadata service.  
custom/mde/metadata/messages/count | Number of messages processed by the metadata service.  
custom/mde/metadata/processing/time | Message processing time in the metadata service.  
custom/mde/metadata/instance/cached | Total count of the cached metadata instances as they are received by the metadata service.  
custom/mde/metadata/instance/created | Total count of the created metadata instances as they are received by the metadata service.  
custom/mde/metadata/messages/pubsub/shift/publishing | Time difference between publishing the message to PubSub and the event timestamp in the metadata service.  
custom/mde/metadata/messages/pubsub/shift/receiving | Time difference between receiving the message from PubSub and the event timestamp in the metadata service.  
custom/mde/mapper/error/count | Errors encountered processing messages in mapper service.  
custom/mde/mapper/messages/count | Number of messages processed by the mapper service.  
custom/mde/mapper/processing/time | Message processing time in the mapper service.  
custom/mde/mapper/messages/pubsub/shift/publishing | Time difference between publishing the message to PubSub and the event timestamp in the mapper service.  
custom/mde/mapper/messages/pubsub/shift/receiving | Time difference between receiving the message from PubSub and the event timestamp in the mapper service.  
custom/mde/federation/request/processing/bq | Request processing time in the MDE federation service for BigQuery requests.  
custom/mde/federation/request/processing/bt | Request processing time in the MDE federation service for Big table requests.  
custom/mde/federation/request/processing/cfg | Request processing time in the MDE federation service for Config requests.  
|   
  
## MDE monitoring dashboard

In order to monitor the Google Cloud services and metrics you can use the built-in Monitoring Dashboard named `MDE Monitoring`. The following are examples of the MDE monitoring dashboard interface.

![monitoring-dashboard-01](https://docs.cloud.google.com/static/manufacturing-data-engine/images/mde-monitoring-dashboard-01.png)

![monitoring-dashboard-02](https://docs.cloud.google.com/static/manufacturing-data-engine/images/mde-monitoring-dashboard-02.png)

![monitoring-dashboard-03](https://docs.cloud.google.com/static/manufacturing-data-engine/images/mde-monitoring-dashboard-03.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
