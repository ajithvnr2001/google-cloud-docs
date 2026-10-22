---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/logging/
title: Cloud logging \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:54.327093+00:00
---

# Cloud logging  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/logging/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Cloud logging Stay organized with collections  Save and categorize content based on your preferences. 

Dialogflow API requests and responses can optionally be logged to [Cloud logging](https://docs.cloud.google.com/logging/docs) for your agent. You can also control the [region](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region) in which these logs are stored.

## Enable Cloud logging

To enable or disable Cloud logging for your agent, see the logging options in the [agent's general settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#settings-general). 

## Viewing Cloud logs

Once you enable Cloud logging for an agent, you can browse these logs using the [Cloud Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

## Log format

For detailed information on the log format, see [Log entry structure](https://docs.cloud.google.com/logging/docs/api/platform-logs#structure).

The following is a partial list of log entry titles used by Dialogflow:

  * Dialogflow Request
  * Dialogflow Response 
  * Dialogflow webhook request
  * Dialogflow webhook response
  * Dialogflow webhook error 

Request and response log entries have a `jsonPayload` field in the JSON format. The content of this payload resembles the structure of like-named Dialogflow API REST requests and responses as defined in [Dialogflow reference documentation](https://docs.cloud.google.com/dialogflow/cx/docs/reference). 

## Regionalization

By default, Dialogflow Cloud log entries are routed to the [_Default logs bucket](https://docs.cloud.google.com/logging/docs/buckets), which is global. If you have data residency requirements for your project, you can route your logs to a region-specific logs bucket. For instructions, see [regionalizing your project's logs using logs buckets](https://docs.cloud.google.com/logging/docs/regionalized-logs).

**Note:** When redirecting log sinks, you can use  
`LOG_ID("dialogflow-runtime.googleapis.com/requests")` for filtering Dialogflow Cloud logs.

## Limitations

If Dialogflow response exceeds the Cloud logging log entry size [limit](https://docs.cloud.google.com/logging/quotas), the `QueryResult.diagnosticInfo` field is not included in the logs.

At most 500 turns will be logged for each conversation.

[ Previous arrow_back  Conversation history  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-history)

[ Next Interaction logging export to BigQuery  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/export-bq)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
