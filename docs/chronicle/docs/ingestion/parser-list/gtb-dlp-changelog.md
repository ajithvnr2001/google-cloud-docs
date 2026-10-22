---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gtb-dlp-changelog/
title: Change log for GTB_DLP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:58.805510+00:00
---

# Change log for GTB_DLP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gtb-dlp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GTB_DLP

Date | Changes  
---|---  
2026-05-07 |  Enhancement:  
\- Added a grok pattern to parse the new format of logs.  
\- Added a grok pattern on `kvData` to extract `Subject` as we have two `cs5` fields within kvData.  
\- Modified the parsing of the `dhost` field to remove spaces before mapping to `event.idm.read_only_udm.network.email.to`.  
\- `event.idm.read_only_udm.additional.fields`: Removed the mapping of `cs5` from `event.idm.read_only_udm.additional.fields` UDM field when `cs5Label` is `Subject` to map to more appropriate UDM field.  
\- `event.idm.read_only_udm.network.email.subject`: Mapped `Subject` raw log field with `event.idm.read_only_udm.network.email.subject` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `cs7` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field when `cs7Label` is `IP Address`.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `cs8` raw log field with `event.idm.read_only_udm.target.application` UDM field when `cs8Label` is `Application`.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `cs5` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field when `cs5Label` is `Login name`.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `cs14` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field when `cs14Label` is `Destination IP`.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `cs15` raw log field with `event.idm.read_only_udm.target.url` UDM field when `cs15Label` is `URL`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cs14` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field when `cs14Label` is not `Destination IP`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cs15` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field when `cs15Label` is not `URL`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cs13` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field when `cs13` is not a valid ip address.   
2025-10-28 |  \- Newly created parser  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped `proto` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- event.idm.read_only_udm.network.email.to: Newly mapped `dhost` raw log field with `event.idm.read_only_udm.network.email.to` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `suser`, `cs6` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.network.email.from: Newly mapped `shost` raw log field with `event.idm.read_only_udm.network.email.from` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `suser` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `src`, `cs13` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `src`, `cs13` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `spt`, `port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `dpt` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.target.user.email_addresses: Newly mapped `duser` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `dvc` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `rt` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `act`, `cs1`, `cs3`, `cs4`, `cs8`, `cs10`, `cs11`, `cs12`, `cs2`, `cs5`, `cs6`, `cs18`, `cs19`, `cert`, `deviceExternalId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.vendor_name: Newly mapped `vendor` raw log field with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped `product` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `rulename` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `peventtype` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `externalId`, `error.innerError.client-request-id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `message_data` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `cs4` raw log field with `event.idm.read_only_udm.metadata.description` UDM field if it matches the grok pattern.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `http_method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `http_response` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `target_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.target.file.size: Newly mapped `cs7` raw log field with `event.idm.read_only_udm.target.file.size` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `cs9` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `cs16`, `cs17`, `error.code`, `error.innerError.date` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.file.sha256: Newly mapped `sha256` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `error.message` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `error.innerError.request-id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If has_principal is `true` and has_target is `true`, updated to `NETWORK_CONNECTION`.  
\- event.idm.read_only_udm.metadata.event_type: If has_user is `true` and message contains `login`, updated to `USER_LOGIN`.  
\- event.idm.read_only_udm.metadata.event_type: If has_user is `true` and message contains `logout`, updated to `USER_LOGOUT`.  
\- event.idm.read_only_udm.metadata.event_type: If has_user is `true` and has_principal_email is `true` and has_target_email is `true`, updated to `EMAIL_TRANSACTION`.  
\- event.idm.read_only_udm.metadata.event_type: If has_principal is `true`, updated to `STATUS_UPDATE`.  
\- event.idm.read_only_udm.metadata.event_type: If has_user is `true`, updated to `USER_UNCATEGORIZED`.  
\- event.idm.read_only_udm.metadata.event_type: Otherwise, updated to `GENERIC_EVENT`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
