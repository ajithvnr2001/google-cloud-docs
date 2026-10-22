---
url: https://docs.cloud.google.com/dialogflow/es/docs/logging/
title: Cloud logging \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:45.487754+00:00
---

# Cloud logging  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Cloud logging Stay organized with collections  Save and categorize content based on your preferences. 

Dialogflow API requests and responses can optionally be logged to [Cloud logging](https://docs.cloud.google.com/logging/docs) for your agent. You can also control the [region](https://docs.cloud.google.com/dialogflow/es/docs/how/region) in which these logs are stored.

## Enable Cloud logging

To enable or disable Cloud logging for your agent, see the logging options in the [agent's general settings](https://docs.cloud.google.com/dialogflow/es/docs/agents-settings#general). 

## Viewing Cloud logs

Once you enable Cloud logging for an agent, you can browse these logs using the [Cloud Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

You can also access all of the logs for an agent by clicking the **Open logs** link in the [agent's general settings](https://docs.cloud.google.com/dialogflow/es/docs/agents-settings#general). 

## Log format

For detailed information on the log format, see [Log entry structure](https://docs.cloud.google.com/logging/docs/api/platform-logs#structure).

The following is a partial list of log entry titles used by Dialogflow:

  * Dialogflow Request
  * Dialogflow Response 
  * Dialogflow fulfillment request
  * Dialogflow fulfillment response
  * Dialogflow fulfillment error 

Request and response log entries have a `textPayload` field in the [HOCON](https://en.wikipedia.org/wiki/HOCON) or Human-Optimized Config Object Notation format. The content of this payload resembles the structure of like-named Dialogflow API REST requests and responses as defined in [Dialogflow reference documentation](https://docs.cloud.google.com/dialogflow/es/docs/reference). You can use a HOCON parser for log conversion to JSON. 

## Regionalization

By default, Dialogflow Cloud log entries are routed to the [_Default logs bucket](https://docs.cloud.google.com/logging/docs/buckets), which is global. If you have data residency requirements for your project, you can route your logs to a region-specific logs bucket. For instructions, see [regionalizing your project's logs using logs buckets](https://docs.cloud.google.com/logging/docs/regionalized-logs).

**Note:** When redirecting log sinks, you can use  
`LOG_ID("dialogflow-runtime.googleapis.com/requests")` for filtering Dialogflow Cloud logs.

## Log analysis tools

Looker provides a tool that can help with analyzing log data:

  * [Dialogflow Parser by Looker](https://marketplace.looker.com/marketplace/detail/dialogflow-parser) (overview of the tool)
  * [stacklogs-looker](https://github.com/GoogleCloudPlatform/dialogflow-integrations/tree/master/stacklogs-looker) (instructions for the tool)



[ Previous arrow_back  Voice agent design best practices  ](https://docs.cloud.google.com/dialogflow/es/docs/voice-agent-design)

[ Next Interaction logging  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/interaction-logging)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
