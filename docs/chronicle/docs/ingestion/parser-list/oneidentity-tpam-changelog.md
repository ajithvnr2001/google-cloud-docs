---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oneidentity-tpam-changelog/
title: Change log for ONEIDENTITY_TPAM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:39:14.451962+00:00
---

# Change log for ONEIDENTITY_TPAM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oneidentity-tpam-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ONEIDENTITY_TPAM

Date | Changes  
---|---  
2025-12-23 |  Enhancement:  
\- Added a new grok pattern to parse new format of logs.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `cn2`, `cn3` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.intermediary.ip and event.idm.read_only_udm.intermediary.hostname: Setting `event.idm.read_only_udm.intermediary.ip` UDM field if `intermediary_data` raw log field is `IP` else setting `intermediary_data` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field.   
2025-04-10 |  \- event.idm.read_only_udm.metadata.product_event_type: Mapped `eventid` along with `logmsg` raw log fields with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- Added gsubs in order to handle `event.idm.read_only_udm.additional.fields` for new format of kv logs.   
2025-03-11 |  \- Mapped `logtype` to `metadata.vendor_name`  
\- Mapped `logmessage` to `metadata.product_name`  
\- Mapped `version` to `metadata.product_version`  
\- Mapped `logmsg` to `metadata.product_event_type`  
\- Mapped `hostname` to `principal.hostname` and `principal.asset.hostname`  
\- Mapped `groupName` to `principal.group.group_display_name`  
\- Mapped `duid` to `target.user.userid`  
\- Mapped `duser` to `target.user.user_display_name`  
\- Mapped `msg` to `metadata.description`  
\- Mapped `destinationDnsDomain` to `target.domain.name`  
\- Mapped `requestUrl` to `target.url`  
\- Mapped `reason` to `security_result.summary`  
\- Mapped `cn1` to `target.resource.product_object_id`  
\- Mapped `cs1` to `principal.user.attribute.roles`  
\- Mapped `cs2`, `cs3`, `cs4`, `cs5`, `cs6` to `additional.fields`  
\- Mapped `deviceCustomDate1` to `security_result.detection_fields`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
