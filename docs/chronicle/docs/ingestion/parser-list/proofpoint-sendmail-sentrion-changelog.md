---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-sendmail-sentrion-changelog/
title: Change log for PROOFPOINT_SENDMAIL_SENTRION \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:40.217162+00:00
---

# Change log for PROOFPOINT_SENDMAIL_SENTRION  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-sendmail-sentrion-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PROOFPOINT_SENDMAIL_SENTRION

Date | Changes  
---|---  
2026-07-17 |  Enhancement:  
\- Proofpoint Sendmail Sentrion product was announced End Of Life, and therefore the prebuilt parser won't be updated. We recommend using the GitHub community version of this parser instead (https://github.com/chronicle/content-hub/tree/main/content/parsers/third_party/community/PROOFPOINT_SENDMAIL_SENTRION).   
2024-06-05 |  Enhancement:  
\- Mapped `subject` to `network.email.subject`.   
2024-05-22 |  \- Added a Grok pattern over `message` to parse a new log type.  
\- Added a Grok over `kv_data` to extract the field `subject`.  
\- Mapped `subject` to `security_result.detection_fields`.   
2024-03-07 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
