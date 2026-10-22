---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-ase-changelog/
title: Change log for SAP_ASE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:30.396412+00:00
---

# Change log for SAP_ASE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-ase-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SAP_ASE

Date | Changes  
---|---  
2026-01-22 |  Enhancement:  
\- Modified the grok pattern to parse the new pattern of logs.   
2025-12-26 |  Enhancement:  
\- Updated `Last Updated` date.   
2025-12-08 |  Enhancement:  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `column19` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `column23` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `column21`, `column22`, `column25` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `event_value` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- A new grok pattern has been introduced to parse the `SAP_ASE_AUDIT` log format.  
\- The `csv` filter is utilized to parse the `csv_data` field, which populates `column1` through `column27`. These columns are then used to map various raw log fields such as `nodeid`, `event_value`, `spid`, `loginname`, `extrainfo`, and `src_ip`.  
\- `event.idm.read_only_udm.metadata.product_log_id` is now populated from the `log_type` field.   
2025-11-28 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped src_hostname raw log field with event.idm.read_only_udm.principal.hostname UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped src_hostname raw log field with event.idm.read_only_udm.principal.asset.hostname UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped src_ip raw log field with event.idm.read_only_udm.principal.ip UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped src_ip raw log field with event.idm.read_only_udm.principal.asset.ip UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped loginname raw log field with event.idm.read_only_udm.target.user.userid UDM field.  
\- `event.idm.read_only_udm.security_result`: Newly mapped security_result raw log field with event.idm.read_only_udm.security_result UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped spid, objid raw log fields with event.idm.read_only_udm.additional.fields UDM field.  
\- `event.idm.read_only_udm.extensions.auth.type`: Set to SSO for USER_LOGIN and USER_LOGOUT event types based on event_value.  
\- `event.idm.read_only_udm.security_result.description`: Set to `User Login Successful`, `User Login Failed`, or `User Logout Successful` based on event_value and eventmod.   
2024-12-04 |  Enhancement:  
\- Mapped `hostname` to `principal.hostname` and `principal.asset.hostname`.   
2024-11-13 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
