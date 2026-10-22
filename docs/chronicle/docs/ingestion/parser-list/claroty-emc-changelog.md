---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/claroty-emc-changelog/
title: Change log for CLAROTY_EMC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:44:41.636621+00:00
---

# Change log for CLAROTY_EMC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/claroty-emc-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CLAROTY_EMC

Date | Changes  
---|---  
2026-02-17 |  Enhancements:  
\- Added grok patterns to support for new syslog events.  
\- event.idm.read_only_udm.principal.administrative_domain: Newly mapped `user_type` raw log field to event.idm.read_only_udm.principal.administrative_domain.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user_email` raw log field to event.idm.read_only_udm.principal.user.userid.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `server_name` raw log field to event.idm.read_only_udm.target.asset.hostname.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `ip_address` raw log field to event.idm.read_only_udm.target.asset.ip.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `server_name` raw log field to event.idm.read_only_udm.target.hostname.  
\- event.idm.read_only_udm.target.ip: Newly mapped `ip_address` raw log field to event.idm.read_only_udm.target.ip.  
\- event.idm.read_only_udm.metadata.event_type: If msg contains `connected to the server` or `opened the session` or event_desc is `Login to SRA succeeded` and has_target is true, updated to USER_LOGIN.  
\- event.idm.read_only_udm.metadata.event_type: If msg contains `disconnected the server` and has_target is true, updated to USER_LOGOUT.  
\- event.idm.read_only_udm.extensions.auth.type: Newly mapped to AUTHTYPE_UNSPECIFIED for USER_LOGIN and USER_LOGOUT events.   
2026-02-02 |  Enhancements:  
\- Added grok patterns to support for new syslog events.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `event_desc` raw log field to `event.idm.read_only_udm.metadata.description`.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `cn1` raw log field to `event.idm.read_only_udm.metadata.product_log_id` (when `cn1Label` is `message_id`).  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped from combined `year`, `month`, `date`, `time` raw log fields to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `cs2` raw log field to `event.idm.read_only_udm.principal.user.email_addresses` (when `cs2Label` is `user`).  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `target_hostname` raw log field (extracted from `msg`) to `event.idm.read_only_udm.target.hostname`.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `target_hostname` raw log field (extracted from `msg`) to `event.idm.read_only_udm.target.asset.hostname`.  
\- `event.idm.read_only_udm.target.location.name`: Newly mapped `target_location_name` raw log field (extracted from `msg`) to `event.idm.read_only_udm.target.location.name`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `site_id` raw log field (extracted from `msg`) to a key named `site_id` within `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `cn3` raw log field to `event.idm.read_only_udm.security_result.category_details` (when `cn3Label` is `category`).  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `msg` raw log field to `event.idm.read_only_udm.security_result.description`.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` raw log field (extracted from `msg`) to `event.idm.read_only_udm.network.session_id`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cs1`, `cs2`, and `cn1` raw log field to `event.idm.read_only_udm.additional.fields` as else condition.  
\- Modified grok patterns to handle an additional Syslog format.  
\- Added logic to parse fields (session_id, target_hostname, target_location_name, site_id) from the `msg` raw log field.   
2024-04-30 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
