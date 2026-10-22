---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-change-document-changelog/
title: Change log for SAP_CHANGE_DOCUMENT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:30.192303+00:00
---

# Change log for SAP_CHANGE_DOCUMENT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-change-document-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SAP_CHANGE_DOCUMENT

Date | Changes  
---|---  
2026-08-19 |  Enhancement:  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `SAP_HOST` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `SAP_SID` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2026-03-17 |  Enhancement:  
\- Added support for JSON format.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Updated new format for timestamp parsing logic for `UDATE`, `UTIME` fields.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `TEXT_CASE`, `CHNGIND`, `TABKEY`, `TABNAME` and `WAS_PLANND` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `CDPOS_DATAAGING`, `CDHDR_DATAAGING`, `VALUE_OLD` , `VALUE_NEW`, `CUKY_NEW`, `CUKY_OLD`, `UNIT_OLD`, `UNIT_NEW`, `FNAME`, `ACT_CHNGNO` and `PLANCHNGNR` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-01-10 |  \- Newly created parser.  
\- Added support for JSON format.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `UDATE`, `UTIME` raw log fields to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `CHANGENR` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `VERSION` raw log field to `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `USERNAME` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `TCODE` raw log field to `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `MANDANT`, `CHANGE_IND`, `LANGU` raw log fields to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `OBJECTCLAS` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `OBJECTID` raw log field to `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `_DATAAGING`, `CDPOS_ITEMS` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
