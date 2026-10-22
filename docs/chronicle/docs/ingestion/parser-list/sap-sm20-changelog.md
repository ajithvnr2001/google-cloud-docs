---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-sm20-changelog/
title: Change log for SAP_SM20 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:29.767902+00:00
---

# Change log for SAP_SM20  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-sm20-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SAP_SM20

Date | Changes  
---|---  
2025-07-07 |  \- Added support for new pattern of SYSLOG logs.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `application` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `resource_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `date` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2024-04-16 |  \- Mapped `ALGSYSTEM` to `principal.hostname` and `principal.asset.hostname`.   
2024-01-29 |  \- Added support for newly ingested logs.  
\- Mapped `WP_PID` to `target.process.pid`.  
\- Mapped `WP_SERVER` to `intermediary.hostname`.  
\- Mapped `WP_STATUS` to `security_result.summary`.  
\- Mapped `INSTANCE_NAME` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `TXSEVERITY` to `security_result.severity`.  
\- Mapped `TXSUBCLSID` to `security_result.description`.  
\- Mapped `ALGSYSTEM` to `principal.hostname` and `principal.asset.hostname`.  
\- If `ALGLTERM` is an IP address, then mapped it to `target.ip` and `target.asset.ip`, else mapped it to `target.hostname` and `target.asset.hostname`.  
\- Mapped `ALGCLIENT` and `ALGINST` to `target.resource.attribute.labels`.  
\- Mapped `ALGUSER` to `target.user.userid`.  
\- Mapped `ALGTEXT` to `metadata.description`.  
\- If `ALGTEXT` is nearly equals to `logon successful` and `has_principal` and `has_target` is equals to `true` then `metadata.event_type` is set to `USER_LOGIN`.  
\- Mapped `WP_TYP`, `ALGREPNA`, `ALGAREA`, `ALGFILENO`, `ALGFILEPOS`, `ALGSUBID`, `UTCDIFF`, `ALGTASKNO`, `ALGTASKTYPE`, `ALGTCODE` to `additional.fields`.   
2023-12-07 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
