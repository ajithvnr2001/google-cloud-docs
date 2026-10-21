---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/adfs-changelog/
title: Change log for ADFS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:21:46.321979+00:00
---

# Change log for ADFS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/adfs-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ADFS

Date | Changes  
---|---  
2026-01-20 |  Enhancement:  
\- event.idm.read_only_udm.principal.administrative_domain: Newly mapped the domain portion of the User_Id raw log field to the event.idm.read_only_udm.principal.administrative_domain UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Changed mapping for event.idm.read_only_udm.principal.user.userid from the full User_Id to only the username portion of the User_Id raw log field.  
\- event.idm.read_only_udm.additional.fields: Removed mapping of activity_id from event.idm.read_only_udm.additional.fields UDM field. As it is more appropriate mapping for event.idm.read_only_udm.security_result.detection_fields  
\- event.idm.read_only_udm.security_result.detection_fields: Mapped activity_id raw log field to event.idm.read_only_udm.security_result.detection_fields UDM field when EventID is `403`.  
\- event.idm.read_only_udm.principal.hostname: Removed mapping of Hostname from event.idm.read_only_udm.principal.hostname UDM field for EventID `1202`.As it is more appropriate mapping.  
\- event.idm.read_only_udm.intermediary.hostname: Mapped Hostname or System.Computer raw log field to event.idm.read_only_udm.intermediary.hostname UDM field when EventID is `1202`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped SystemTime raw log field to the event.idm.read_only_udm.additional.fields UDM field.   
2025-12-16 |  Enhancement:  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `Level` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- Added EventID `1202` in conditional check.  
\- Added split function to split the `Ip_Address` raw log field with comma and map each IP to the `principal.ip` and `principal.asset.ip` UDM fields.  
\- Added conditional check for `Proxy_Server` field to prevent mapping `N/A` values.   
2025-06-19 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: The mappings for `User_Id`, `Ip_Address`, and `Proxy_Server` have been removed from the `event.idm.read_only_udm.additional.fields` UDM field. These fields are now mapped to specific UDM fields based on their data type and relevance. `Ip_Address` represents a valid IP and should no longer be mapped to the additional field. Similarly, `Proxy_Server` contains server-related data and has been reassigned appropriately. Additionally, `User_Id`, which pertains to user-related data, should not be mapped to the additional field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `Ip_Address` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `Ip_Address` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `Proxy_Server` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `Proxy_Server` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `User_Id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.   
2025-05-13 |  Enhancement:  
\- Initialized the `LogonType` field with empty strings.  
\- event.idm.read_only_udm.extensions.auth.auth_details: Added a condition that assigns the value of `LogonType` field to `event.idm.read_only_udm.extensions.auth.auth_details` only if the LogonType field is not empty. This prevents overwriting the field with an empty value.  
\- event.idm.read_only_udm.extensions.auth.auth_details: Modified the condition to assign the value of `SubjectLogonId` field to `event.idm.read_only_udm.extensions.auth.auth_details` only when the `LogonType` field is empty and `SubjectLogonId` has a value.  
\- Added a `gsub` filter to replace `Additional Context` with `AdditionalContext` in the `message` field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `security.user_id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Activity_ID` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `Client_IP` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `Instance_ID` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `Local_IP` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `Local_Port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `User_Agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.   
2025-04-22 |  Enhancement:  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Removed the use of convert and rename for the `User Agent` field from `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field and replaced it with replace and convert with on_error. This change ensures that the value is assigned directly and the conversion is performed only if needed, avoiding errors when the field is already a string.  
\- Initialized the `TargetDomainName` and `KeyName` fields with empty strings.  
\- Added a condition to prevent mapping `empty` or `-` values to the `event.idm.read_only_udm.network.http.method`.  
\- Added a condition to prevent mapping `empty` or `--` values to the `event.idm.read_only_udm.network.http.referral_url`.   
2025-03-21 |  Enhancement:  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `EventType` fields from the raw log.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `gmi_sourcetype` fields from the raw log.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `SeverityValue` fields from the raw log.  
\- `security_result.detection_fields` (New UDM field mapping) -> No UDM mapping to mapping of `Task` fields from the raw log.  
\- `security_result.detection_fields` (New UDM field mapping) -> No UDM mapping to mapping of `Opcode` fields from the raw log.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `Relying party` fields from the Message field, for EventID 299.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `content_length` fields from the Message field, for EventID 403.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `caller_identity` fields from the Message field, for EventID 403.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `certificate_identity` fields from the Message field, for EventID 403.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `Targeted relying party` fields from the Message field, for EventID 403.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `through_proxy` fields from the Message field, for EventID 403.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `proxy_dns_name` fields from the Message field, for EventID 403.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `port` fields from the Message field, for EventID 410.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `x_ms_client_application` fields from the Message field, for EventID 410.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `x_ms_client_user_agent` fields from the Message field, for EventID 410.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `client_request_id` fields from the Message field, for EventID 410.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `x_ms_endpoint_absolute_path` fields from the Message field, for EventID 410.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `x_ms_forwarded_client_ip` fields from the Message field, for EventID 410.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `x_ms_proxy` fields from the Message field, for EventID 410.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `x_ms_adfs_proxy_client_ip` fields from the Message field, for EventID 410.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `port` fields from the Message field, for EventID 500.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `port` fields from the Message field, for EventID 501.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `chronicle_tag` fields from the Message field, for EventID 500.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `chronicle_tag` fields from the Message field, for EventID 501.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `Upgrade-Insecure-Requests` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `Origin` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `Sec-Fetch-Site` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `Sec-Fetch-Mode` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `Sec-Fetch-User` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `Sec-Fetch-Dest` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `X-MS-Forwarded-Client-IP` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `client-request-id` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `X-MS-Proxy` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `X-MS-Endpoint-Absolute-Path` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `Cache-Control` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `Content-Length` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `Content-Type` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `Accept` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `Accept-Encoding` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `Accept-Language` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `Cookie` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `Expect` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `Host` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `Referer` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `Connection` fields from the Message field, for EventID 510.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `charset` fields from the Message field, for EventID 510.  
\- Added support for new EventID 1102, 1203 and 1210.   
2025-03-20 |  Enhancement:  
\- Mapped `data` to `security_result.detection_fields` when Index is `1` with the key as `Activity ID`.  
\- Mapped `data` to `security_result.detection_fields` when Index is `2` with the key as `Request ID`.  
\- Mapped `data` to `principal.ip` and `principal.asset.ip` when Index is `4`.  
\- Mapped `data` to `network.http.method` when Index is `5`.  
\- Mapped `data` to `network.http.referral_url` when Index is `7`.  
\- Mapped `data` to `network.http.response_code` when Index is `8`.  
\- Mapped `data` to `target.ip` and `target.asset.ip` when Index is `9`.  
\- Mapped `data` to `network.http.user_agent` and `network.http.parsed_user_agent` when Index is `10`.  
\- If `metadata.event_type` is `GENERIC_EVENT`, `STATUS_UPDATE`, or `USER_UNCATEGORIZED`, and if `has_principal` is `true`, `has_target` is `true`, and `has_user` is `true`, then the `metadata.event_type` will be set to `USER_LOGIN` and `extensions.auth.type` will be set to `AUTHTYPE_UNSPECIFIED`.  
\- If `metadata.event_type` is `GENERIC_EVENT`, `STATUS_UPDATE`, or `USER_UNCATEGORIZED`, and if `has_principal` is `true`, `has_target` is `true`, and `is_http` is `true`, then the `metadata.event_type` will be set to `NETWORK_HTTP`.  
\- If `metadata.event_type` is `GENERIC_EVENT`, `STATUS_UPDATE`, or `USER_UNCATEGORIZED`, and if `has_principal` is `true` and `has_target` is `true`, then the `metadata.event_type` will be set to `NETWORK_CONNECTION`.   
2025-03-10 |  Enhancement:  
\- Changed user_id mapping to principal.user.userid to target.user.user_id.   
2025-02-20 |  Enhancement:  
\- Mapped `principal_user` to `principal.user.userid`.  
\- Added `gsub` to parse fields correctly.   
2024-11-21 |  Enhancement:  
\- Added support for a new format of JSON logs.  
\- Changed `metadata.event_type` from `STATUS_UNCATEGORIZED` to `STATUS_UPDATE` where `has_principal` is true.  
\- Changed `metadata.event_type` from `SYSTEM_AUDIT_LOG_UNCATEGORIZED` to `STATUS_UPDATE` where `has_principal` is true.   
2024-09-09 |  Enhancement:  
\- Mapped `_raw.Event.System.Computer` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `_raw.Event.System.EventRecordID` to `metadata.product_log_id`.  
\- Mapped `_raw.Event.System.Channel`, `_raw.Event.System.Keywords`, `_raw.Event.System.Task`, `_raw.Event.System.Level`, `_raw.Event.System.EventID._value`, `_raw.Event.System.EventID.Qualifiers`, `source`, `index`, `sourcetype`, `host`, and `cribl` to `additional.fields`.   
2024-08-28 |  Enhancement:  
\- Added support for the XML logs with `AuditBase` fields.   
2024-07-31 |  Enhancement:  
\- Added support for a new format of JSON logs.   
2024-07-30 |  Enhancement:  
\- Added support for the XML logs.   
2024-05-27 |  Enhancement  
\- Added a Grok pattern to extract `Instance ID` from `Message` and map it to `target.resource.product_object_id`.   
2023-08-18 |  Enhancement  
\- Added a Grok pattern to extract `email` from `Message` and map it to `principal.user.email_addresses`.   
2023-07-31 |  Enhancement  
\- Mapped the field `user_email` to `principal.user.email_addresses`.  
\- Mapped the field `X-Forwarded-For` to `additional.fields`.   
2023-06-26 |  Enhancement  
\- Added kv block to extract the values from the field `Message` where `EventID` is `404`, `403`, `342`, `364`.  
\- Mapped the field `Protocol Name` to `additional.fields`.  
\- Mapped the field `Relying Party` to `additional.fields`.  
\- Mapped the field `Exception details` to `additional.fields`.  
\- Mapped the field `Token Type` to `additional.fields`.  
\- Mapped the field `Error message` to `additional.fields`.  
\- Mapped the field `Client IP` to `principal.ip`.  
\- Mapped the field `Local IP` to `target.ip`.  
\- Mapped the field `Local Port` to `target.port`.  
\- Mapped the field `Url Absolute Path`, `Query string` to `target.url`.  
\- Mapped the field `Instance ID` to `target.resource.product_object_id`.  
\- Mapped the field `Activity ID` to `security_result.detection_fields`.  
\- Mapped the field `Status Code` to `network.http.response_code`.  
\- Mapped the field `HTTP Method` to `network.http.method`.  
\- Mapped the field `User Agent` to `network.http.user_agent` and `network.http.parsed_user_agent`.   
2023-06-08 |  Enhancement  
\- Added `on_error` condition for `EventID` and `RecordNumber` conversion.  
\- Added validation check for the event_type `SYSTEM_AUDIT_LOG_UNCATEGORIZED`.  
\- Changed `metadata.event_type` from `GENERIC_EVENT` to `STATUS_UPDATE` where `principal.hostname` is not null.   
2023-02-02 |  Enhancement  
\- Added `UNIX`,`UNIX_MS`,`ISO8601` in date block to parse logs for which `EventTime`,`EventReceivedTime` might be in this format.   
2022-08-09 |  Bug fix  
\- Mapped AdapterSuffixName field to intermediary.hostname.   
2022-07-08 |  Enhancement:  
\- Modified mapping for the field `AdapterSuffixName` from `target.asset.hostname` to `intermediary.hostname`.   
2022-05-18 |  Newly Created Parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
