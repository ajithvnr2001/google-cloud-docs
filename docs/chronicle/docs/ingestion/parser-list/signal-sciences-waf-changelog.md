---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/signal-sciences-waf-changelog/
title: Change log for SIGNAL_SCIENCES_WAF \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:58.450875+00:00
---

# Change log for SIGNAL_SCIENCES_WAF  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/signal-sciences-waf-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SIGNAL_SCIENCES_WAF

Date | Changes  
---|---  
2024-05-13 |  Enhancement:  
\- Added support to handle array of JSON logs.   
2023-11-22 |  Enhancement:  
\- Added a Grok pattern to validate `remoteIP`.  
\- Added on_error function for fields `tag.detector`, `tag.link`, `tag.location`, `tag.redaction`, `tag.type`, and `tag.value1`.   
2023-09-16 |  Bug-Fix:  
\- Added a condition check to avoid mapping negative values to `network.received_bytes` and `network.http.response_code`.   
2023-02-21 |  Bug-Fix  
\- Added gsub to fix the issue of userid and username not displayed in the udm mapping of `target.user.user_display_name` and `target.user.userid`, respectively.   
2022-11-25 |  Enhancement  
\- Enhanced the parser to support new log format.   
2022-11-03 |  Enhancement  
\- Mapped `created` to `metadata.timestamp`.  
\- Checked for not null conditions for following:  
`remoteIP`, `responseSize`, `uri`, `remoteHostname`,`serverName`,`userAgent`,`method`,`remoteCountryCode`,`id` prior mapping to udm.  
\- Mapped `eventType` to `metadata.product_event_type`.  
\- Mapped `message_data` to `metadata.description`.  
\- Mapped `username` to `target.user.user_display_name`.  
\- Mapped `userid` to `target.user.userid`.  
\- Mapped `attachments.Fields.Title` , `attachments.Fields.Value` to `metadata.ingestion_labels` key and value.  
\- Mapped `msgData.detailLink` to `network.http.referral_url`.  
\- Mapped `msgData.name` to `target.resource.name`.  
\- Mapped `msgData.changes` to `target.resource.attribute.labels`.  
\- Mapped `msgData.reason` to `security_result.summary`.  
\- Mapped `msgData.conditions` to `security_result.description`.  
\- Mapped `msgData.sites` to `network.http.user_agent`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
