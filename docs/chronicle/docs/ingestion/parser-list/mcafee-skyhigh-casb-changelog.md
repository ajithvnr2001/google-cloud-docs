---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-skyhigh-casb-changelog/
title: Change log for MCAFEE_SKYHIGH_CASB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:05:18.833266+00:00
---

# Change log for MCAFEE_SKYHIGH_CASB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-skyhigh-casb-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MCAFEE_SKYHIGH_CASB

Date | Changes  
---|---  
2026-03-13 |  \- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `column2` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `intermediary_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `column3` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `column8` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `column9` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `column10` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `column10` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `http_method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `tar_host` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `tar_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `application_protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `tar_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `http_version`, `column1` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.intermediary.application`: Newly mapped `intermediary_application` raw log field with `event.idm.read_only_udm.intermediary.application` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `column5` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `column6`, `column12` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.file.mime_type`: Newly mapped `column7` raw log field with `event.idm.read_only_udm.target.file.mime_type` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped to `NETWORK_HTTP` if event contains both principal and target and application protocol information.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped to `NETWORK_CONNECTION` if event contains both principal and target information.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped to `STATUS_UPDATE` if event contains principal information.  
\- Added a Grok pattern for `message` field to parse the raw log fields.  
\- Added a Grok pattern on `column4` to extract `http_method`, `tar_host`, `tar_port`, `application_protocol`, `http_version`, `tar_url`.  
\- Modified the condition to drop events. Events are now dropped if they fail both KV and Grok parsing.  
\- Added support for new pattern of CSV logs, this is allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.annotation`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.browser`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.browser_engine_version`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.browser_version`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.device`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.device_version`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.family`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.locale`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.os`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.os_variant`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.platform`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.sub_family`  
\- `event.idm.read_only_udm.metadata.event_timestamp.seconds`  
2023-06-17 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
