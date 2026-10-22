---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/iboss-webproxy-changelog/
title: Change log for IBOSS_WEBPROXY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:21.949549+00:00
---

# Change log for IBOSS_WEBPROXY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/iboss-webproxy-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IBOSS_WEBPROXY

Date | Changes  
---|---  
2023-08-22 |  Enhancement:  
\- Added a `kv` function to retrieve key-value data.  
\- Added conditional check for `src_port`, `mac_address`, `file_name`, `targetPort`, `computer_Mac_Address`, `filtering_Group_Name`, `uri_path`, `down_stream`, `user_Agent`, `up_stream`, `ref_url`, `response_Code`, `desc`, `description`, `category_Name`, `url`, `ts`.   
2023-03-28 |  Modified the following Mappings-  
\- Modified mapping of `host` from `principal.hostname` to `target.hostname`.  
\- Modified mapping of `url` from `principal.url` to `target.url`.  
\- Modified mapping of `uriPath` from `principal.process.file.full_path` to `target.process.file.full_path`.  
\- Modified mapping of `iboss` from `target.hostname` to `intermediary.hostname`.  
\- Modified mapping of `upstreamByteUsage` from `network.sent_bytes` to `network.received_bytes`.  
\- Modified mapping of `downstreamByteUsage` from `network.received_bytes` to `network.sent_bytes`.  
\- Mapped `computerName` to `principal.hostname` as well as it was already mapped to `principal.asset.hostname`.   
2023-02-21 |  Newly Created Parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
