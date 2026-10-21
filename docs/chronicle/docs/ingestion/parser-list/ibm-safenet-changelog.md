---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-safenet-changelog/
title: Change log for IBM_SAFENET \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:42:32.967848+00:00
---

# Change log for IBM_SAFENET  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-safenet-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IBM_SAFENET

Date | Changes  
---|---  
2026-03-05 |  Enhancement:  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `cmd_data` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- Added a grok pattern on description to extract `cmd_data`, `process_id`, `status`, and `application` fields.  
\- Added support for new pattern of SYSLOG logs, this is allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.metadata.event_timestamp.seconds`.  
\- `event.idm.read_only_udm.metadata.event_type`.  
\- `event.idm.read_only_udm.metadata.log_type`.  
\- `event.idm.read_only_udm.metadata.product_name`.  
\- `event.idm.read_only_udm.metadata.vendor_name`.  
\- `event.idm.read_only_udm.principal.application`.  
\- `event.idm.read_only_udm.principal.asset.hostname`.  
\- `event.idm.read_only_udm.principal.hostname`.  
\- `event.idm.read_only_udm.principal.process.command_line`.  
\- `event.idm.read_only_udm.principal.process.pid`.  
\- `event.idm.read_only_udm.security_result.description`.  
\- `event.idm.read_only_udm.security_result.summary`.   
2023-05-24 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
