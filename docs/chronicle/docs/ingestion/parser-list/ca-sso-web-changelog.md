---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ca-sso-web-changelog/
title: Change log for CA_SSO_WEB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:28.414476+00:00
---

# Change log for CA_SSO_WEB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ca-sso-web-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CA_SSO_WEB

Date | Changes  
---|---  
2026-04-17 |  Enhancement:  
\- Added a grok pattern to parse new format of syslogs.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `prod_log_id` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.priority_details`: Newly mapped `syslog_priority` raw log field to `event.idm.read_only_udm.security_result.priority_details` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Newly mapped `syslog_host` to `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` when `syslog_host` is an IP address.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `syslog_host` to `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` when `syslog_host` is not an IP address.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `target_app` raw log field to `event.idm.read_only_udm.target.application` UDM field.   
2024-06-25 |  Enhancement:  
\- Added a Grok pattern to parse newly ingested syslog format.   
2022-08-08 |  Enhancement -  
\- Added the header.  
\- Added conditional check and grok pattern for the field `ClientIp` mapped to `principal.ip`.  
\- Added conditional checks for the fields :  
\- `Action` mapped to `network.http.method`.  
\- `AgentName` mapped to `target.hostname`.  
\- `sm_user` mapped to `target.user.email_addresses`  
\- `sm_group` mapped to `target.user.group_identifiers`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
