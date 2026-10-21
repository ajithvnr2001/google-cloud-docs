---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-ser-changelog/
title: Change log for PROOFPOINT_SER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:37:45.626866+00:00
---

# Change log for PROOFPOINT_SER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-ser-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PROOFPOINT_SER

Date | Changes  
---|---  
2025-01-02 |  Enhancement:  
\- Converted `acceptedMessages`,`deliveredMessages`,`rejectedMessages`,`sentMessages`, and `totalMessage` from `string_value` to `number_value`.   
2024-11-20 |  Enhancement:  
\- Mapped `data.throughput` and `data.totalThroughput` to `additional.fields`.  
\- Mapped `metadata.totalThroughput` to `additional.fields`.  
\- Mapped `principal_host` to `principal.hostname`.  
\- Mapped `principal_port` to `principal.port`.  
\- Mapped `desc` to metadata.description".  
\- Added support for new pattern of JSON logs.   
2024-10-03 |  Enhancement:  
\- Mapped `data.name` to `metadata.description`.  
\- Mapped `data.relayUserId` to `principal.user.product_object_id`.  
\- Mapped `data.throughputLimit`, `data.averageDailyThroughput`, `data.throughputForecast`, `data.remainingThroughput`, `data.acceptedThroughput`, `data.licenseStartDate`, `data.licenseEndDate`, `data.average7DayThroughput`, `data.average30DayThroughput`, `data.requestedMessages`, `data.acceptedMessages`, `data.sentMessages`, `data.deliveredMessages`, `data.avgAcceptedMessageSize`, `data.blockedMessages`, `data.quarantinedMessages`, `data.rejectedMessages`, `data.requestedThroughput`, `data.totalMessages`, and `data.undeliveredMessages` to `additional.fields`.   
2023-08-29 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
