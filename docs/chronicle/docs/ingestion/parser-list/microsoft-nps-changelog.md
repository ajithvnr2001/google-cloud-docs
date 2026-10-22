---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-nps-changelog/
title: Change log for MICROSOFT_NPS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:43.134959+00:00
---

# Change log for MICROSOFT_NPS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-nps-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MICROSOFT_NPS

Date | Changes  
---|---  
2025-12-31 |  Enhancement:  
\- Added support for JSON+CSV format logs.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `column1` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `column2` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `column3`, `column4` raw log fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.labels.packet_type`: Newly mapped `column5` raw log field with `event.idm.read_only_udm.principal.labels.packet_type` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `column6` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.labels.client_vendor`: Newly mapped `column15` raw log field with `event.idm.read_only_udm.principal.labels.client_vendor` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `column16` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `column16` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `column17` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.labels.nas_port_type`: Newly mapped `column20` raw log field with `event.idm.read_only_udm.principal.labels.nas_port_type` UDM field.  
\- `event.idm.read_only_udm.principal.labels.reason_code`: Newly mapped `column26` raw log field with `event.idm.read_only_udm.principal.labels.reason_code` UDM field.  
\- `event.idm.read_only_udm.principal.labels.acct_status_type`: Newly mapped `column32` raw log field with `event.idm.read_only_udm.principal.labels.acct_status_type` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `column36` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.labels.acct_authentic`: Newly mapped `column37` raw log field with `event.idm.read_only_udm.principal.labels.acct_authentic` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `column61` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `column63` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `column63` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `column64` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `column64` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary`: Merged `intermediary` internal field to `event.idm.read_only_udm.intermediary` UDM field.  
\- `TimeCreated`: Combined `column3` and `column4` into `TimeCreated`.  
\- `TimeCreated`: Converted type to `date` with error handling for `date_match_failed`.  
\- Initialized new internal fields: `is_csv`, `csv_parse_failure`, `intermediary`, `RecordDate`, `RecordTime`, and `column1` through `column66`.  
\- Added `csv` filter to parse `_raw` field using comma as a separator.  
\- Expanded `date` filter for `TimeCreated` to include `MM/dd/yyyy HH:mm:ss` format.  
\- Updated XML parsing conditional logic to check for `Event` in `_raw` instead of `_raw` being non-empty.   
2025-12-01 |  Enhancement:  
\- Added support for JSON+XML format logs.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `Computer` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `Computer` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `ProviderName` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.windows_sid`: Newly mapped `UserName` raw log field with `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `UserName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `NAS_Port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `Acct_Session_Id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `NAS_IP_Address` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `NAS_IP_Address` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `Client_IP_Address` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `Client_IP_Address` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `Client_Friendly_Name` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `Client_Friendly_Name` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `Proxy_Policy_Name` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.principal.labels`: Newly mapped `NAS-Port-Type`, `Acct-Status-Type`, `Acct-Authentic`, `Client-Vendor`, `Packet-Type`, `Reason-Code` raw log fields with `event.idm.read_only_udm.principal.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `source`, `cribl_pipe` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2024-07-24 |  Resolved flaky behavior.   
2024-03-12 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
