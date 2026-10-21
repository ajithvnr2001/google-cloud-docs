---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-securesphere-changelog/
title: Change log for IMPERVA_SECURESPHERE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:10:16.172154+00:00
---

# Change log for IMPERVA_SECURESPHERE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-securesphere-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IMPERVA_SECURESPHERE

Date | Changes  
---|---  
2026-09-15 |  Enhancement:  
\- Added support for new format of SYSLOG log.  
\- Added a Grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `observer_host` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.observer.application`: Newly mapped `observer_app` raw log field with `event.idm.read_only_udm.observer.application` UDM field.  
\- `event.idm.read_only_udm.observer.process.pid`: Newly mapped `observer_pid` raw log field with `event.idm.read_only_udm.observer.process.pid` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `session_start` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `client_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `client_host` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `client_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `db_user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `src_program` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `server_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `server_host` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `server_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `service_name` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `db_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_type`: Newly set the value of `event.idm.read_only_udm.target.resource.resource_type` to `DATABASE` when `db_name` is not empty.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `server_type` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `sql_query` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `net_protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `db_protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol_version`: Newly mapped `db_protocol_version` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `auth_code`, `syslog_priority` and `sql_status` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `rule_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `rule_name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `guard_severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `guard_severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `request_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.   
2026-07-19 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.hostname`: Removed mapping of `inter_host` from `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_header_domain`, `Authorization`, `X-Office-Major-Version`, `X-FeatureVersion`, `Accept-Auth`, `X-MS-CookieUri-Requested`, `X-IDCRL_ACCEPTED` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-07-08 |  Enhancement:  
\- Added a grok pattern to support the new format of Syslog+KV(CEF) logs.  
\- Modified the KV filters to parse the `kv_data4` and `kv_data2` fields.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `dvc` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.   
2026-06-25 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `cs3` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields when `cs3Label` is `ServiceName` as this is a duplicate mapping.  
\- `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent`: Removed mapping of `cs6` from `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` UDM fields as the `cs6` field does not contain user agent data.  
\- Added a KV filter to parse the `cs6` raw log field.  
\- `event.idm.read_only_udm.security_result.summary`: Removed mapping of `msg` from `event.idm.read_only_udm.security_result.summary` UDM field in order to introduce more accurate mapping.  
\- `event.idm.read_only_udm.security_result.threat_name`: Mapped `msg` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Removed mapping of `requestMethod` and `http.request.method` from `event.idm.read_only_udm.network.http.method` UDM field when invalid http method is present.  
\- `event.idm.read_only_udm.target.application`: Mapped `cs3` raw log field with `event.idm.read_only_udm.target.application` UDM field when `cs3Label` is `GeneralApplicationName`.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `User-Agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `User-Agent` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `Referer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.principal.asset.platform_software.platform`: Newly mapped `sec-ch-ua-platform` raw log field with `event.idm.read_only_udm.principal.asset.platform_software.platform` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `Host` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields when `Host` field contains a hostname.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `Host` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields when `Host` field contains an IP address.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Accept`, `Accept-Encoding`, `Accept-Language`, `Connection`, `DNT`, `Sec-Fetch-Dest`, `Sec-Fetch-Mode`, `Sec-Fetch-Site`, `Sec-Fetch-User`, `Upgrade-Insecure-Requests`, `sec-ch-ua`, `sec-ch-ua-mobile` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type` and `event.idm.read_only_udm.network.application_protocol`: Setting the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_HTTP` and `event.idm.read_only_udm.network.application_protocol` to `HTTP` when principal machine details are present and target machine details are present and http details are present.   
2026-06-21 |  Enhancement:  
\- Added a grok pattern to parse the new format of logs.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `dvc` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cs6`, `cs7` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-05-21 |  Enhancement:  
\- Added a new grok pattern to parse the new `SYSLOG_KV` format logs.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `externalId`, `deviceCustomDate1`, `flexString1`, `flexString2`, `flexString2Label`, `requestContext`, `flexNumber1`, `cn2` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `cn1` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field when `cn1Label` is `EventId`.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `ad.host` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `requestMethod` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `request` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `msg` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `flexNumber2` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field when `flexNumber2Label` is `ResponseSize`.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `flexString2` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field when `flexString2Label` is `ResponseCode`.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `cs6` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field when `cs6Label` is `UserAgent`.   
2026-05-13 |  Enhancement:  
\- Added a new grok pattern to parse the new format logs.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `name` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cs2`, `cs3`, `cs4` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `suser` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `login_user` raw log fields with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `princ_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.security_result.action`:  
\- If `act` contains `none`, set the value of `event.idm.read_only_udm.security_result.action` to `ALLOW`.  
\- If `act` contains `block`, set the value of `event.idm.read_only_udm.security_result.action` to `BLOCK`.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `cs1` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field when `cs1Label` is `Policy`.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `cs5` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Newly mapped `device_vendor` raw log field with `event.idm.read_only_udm.metadata.vendor_name` UDM field when both `device_vendor` and `device_product` raw log fields are not empty.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `device_product` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field when both `device_vendor` and `device_product` raw log fields are not empty.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly set the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` when both principal and target information are present.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly set the value of `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when principal user related information is present.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the value of `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS` when the current `event.idm.read_only_udm.metadata.event_type` is not set and principal information is present.   
2026-04-16 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `descrip` log field with event.idm.read_only_udm.additional.fields UDM field.  
\- The gsub pattern for `kv_data2` was updated to ensure correct key-value pair parsing.  
\- Added gsub on `message` to remove field newline characters.   
2026-03-22 |  Enhancement:  
\- Modified a grok pattern to correctly parse logs where the product_type field contains spaces. Added a new test case to validate the change. Due to this change, the following UDM fields are now being mapped correctly:  
\- `event.idm.read_only_udm.metadata.description`  
\- `event.idm.read_only_udm.metadata.event_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.product_version`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.network.ip_protocol`  
\- `event.idm.read_only_udm.principal.asset.hostname`  
\- `event.idm.read_only_udm.principal.hostname`  
\- `event.idm.read_only_udm.principal.asset.ip`  
\- `event.idm.read_only_udm.principal.ip`  
\- `event.idm.read_only_udm.principal.group.group_display_name`  
\- `event.idm.read_only_udm.principal.port`  
\- `event.idm.read_only_udm.security_result.action_details`  
\- `event.idm.read_only_udm.security_result.category_details`  
\- `event.idm.read_only_udm.security_result.rule_name`  
\- `event.idm.read_only_udm.security_result.severity`  
\- `event.idm.read_only_udm.security_result.severity_details`  
\- `event.idm.read_only_udm.target.application`  
\- `event.idm.read_only_udm.target.asset.ip`  
\- `event.idm.read_only_udm.target.ip`  
\- `event.idm.read_only_udm.target.port`  
\- `event.idm.read_only_udm.target.resource.attribute.labels.key`  
\- `event.idm.read_only_udm.target.resource.attribute.labels.value`  
\- `event.idm.read_only_udm.target.user.userid`  
2025-11-05 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cs9`, `cs9Label` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added on_error for rt.  
\- Modified the date filter to add support for the ISO8601 date format for the rt raw log field.  
\- Modified conditional logic to process cs9 and cs9Label fields independently of the cs8 and cs8Label fields.   
2025-10-31 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `cs5` raw log field to `event.idm.read_only_udm.metadata.product_log_id` when `cs5Label` is `EventId`.  
\- event.idm.read_only_udm.principal.application: Newly mapped `cs10` raw log field to `event.idm.read_only_udm.principal.application` when `cs10Label` is `SourceApplication`.  
\- event.idm.read_only_udm.principal.application: Newly mapped `app` raw log field to `event.idm.read_only_udm.principal.application`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `cs11` raw log field to `event.idm.read_only_udm.principal.user.userid` when `cs11Label` is `OSUser`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `osUser` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `cs12` raw log field to `event.idm.read_only_udm.principal.hostname` when `cs12Label` is `HostName`.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `cs12` raw log field to `event.idm.read_only_udm.principal.asset.hostname` when `cs12Label` is `HostName`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `cs3` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` with `key` `ServiceName` when `cs3Label` is `ServiceName`.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `suser` raw log field to `event.idm.read_only_udm.principal.user.user_display_name`.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `cs13` raw log field to `event.idm.read_only_udm.target.resource.name` when `cs13Label` is `Database`.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `dbName` raw log field to `event.idm.read_only_udm.target.resource.name`.  
\- event.idm.read_only_udm.target.resource.resource_type: Newly mapped `cs13` raw log field to `event.idm.read_only_udm.target.resource.resource_type` (set to `DATABASE`) when `cs13Label` is `Database`.  
\- event.idm.read_only_udm.target.resource.resource_type: Newly mapped `dbName` raw log field to `event.idm.read_only_udm.target.resource.resource_type` (set to `DATABASE`).  
\- event.idm.read_only_udm.additional.fields: Newly mapped `cs18` (with key from `cs18Label`), `cs19` (with key from `cs19Label`), `cs20` (with key from `cs20Label`), `cs21` (with key from `cs21Label`) raw log fields to `event.idm.read_only_udm.additional.fields`. Also mapped `cs5` raw log field to `event.idm.read_only_udm.additional.fields` with key `RawDBQuery` when `cs5Label` is `RawDBQuery`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `shost` raw log field to `event.idm.read_only_udm.principal.ip`.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `shost` raw log field to `event.idm.read_only_udm.principal.asset.ip`.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `bytesOut` raw log field to `event.idm.read_only_udm.network.sent_bytes`.  
\- event.idm.read_only_udm.target.process.command_line: Newly mapped `cs4` raw log field to `event.idm.read_only_udm.target.process.command_line` when `cs4Label` is `DBQuery`.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `isAuthenticated` raw log field to `event.idm.read_only_udm.security_result.action` (set to `ALLOW`) when `isAuthenticated` is `True`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `dbSchema` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` with key `dbSchema`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `dbBindVariables` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` with key `dbBindVariables`.  
\- Updated `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` for logs where `descrip` contains `SQL protocol` and `message` contains `login`.   
2025-10-17 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `ruleid` raw log field to `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cs3`, `deviceCustomDate1`, `cs8`, `cs9`, `cs10`, `cs11`, `cs13`, `cs4` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `src` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `cs5` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `cs6` raw log field to `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `dst` raw log field to `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dst` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `cs7` raw log field to `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `cs12` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `cn1` raw log field to `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `cn2` raw log field to `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `cn3` raw log field to `event.idm.read_only_udm.target.port` UDM field.  
\- Added logic to set `metadata.event_type` to `NETWORK_CONNECTION`, `USER_UNCATEGORIZED`, `STATUS_UPDATE`, or `GENERIC_EVENT` based on the presence of principal, target, and user information for the new log format.  
\- Added grok patterns to parse new pattern of syslog logs.   
2025-07-18 |  Enhancement:  
\- Added mappings for `cs7` and `cs11` raw log fields globally.  
\- Modified the condition to map `cs12` raw log field to `security_result.description` UDM field when `cs12Label` is not `OSUser`.  
\- Modified the condition to map `cs17` raw log field to `event.idm.read_only_udm.target.resource.resource_subtype` UDM field when `cs17Label` is not `Error`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `cs17` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field when cs17Label is `Error`.   
2025-07-03 |  Enhancement:  
\- Added Grok patterns to support new pattern of syslog logs.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cs2`, `cs2Label`, and `additional_json_data` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field when cs2Label is `ServerGroup`.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `cs5` raw log field with `event.idm.read_only_udm.target.application` UDM field when cs5Label is `ApplicationName`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `cs4` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field when cs4Label is `ServiceName`.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `cs6` raw log field with `event.idm.read_only_udm.principal.application` UDM field when cs11Label is `SrcApp`.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `cs7` raw log field with `event.idm.read_only_udm.security_result.description` UDM field when cs7Label is `AlertDesc`.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `cs11` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field when cs11Label is `DatabaseName`.  
\- `event.idm.read_only_udm.target.resource.resource_type`: Newly mapped `DATABASE` with `event.idm.read_only_udm.target.resource.resource_type` UDM field when cs11Label is `DatabaseName`.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `cs10` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field when cs10Label is `EventID`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `cs15` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field when cs15Label is not `ViolatedItem`.  
\- `event.idm.read_only_udm.security_result.threat_id`: Newly mapped `cs9` raw log field with `event.idm.read_only_udm.security_result.threat_id` UDM field when cs9Label is `AlertID`.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `cs12` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field when cs12Label is `OSUser`  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `inter_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `cs13` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field when cs13Label is `HostName`.  
\- Modified condition such that `cs2` raw log field is mapped to `event.idm.read_only_udm.principal.group.group_display_name` when `cs2Label` is `ServerGroup`.  
\- Modified condition such that `cs4` raw log field is mapped to `event.idm.read_only_udm.target.application` UDM field when `cs4Label` is `ApplicationName`.  
\- Modified condition such that `cs5` raw log field is mapped to `event.idm.read_only_udm.metadata.description` UDM field when `cs5Label` is `Description`.  
\- Modified condition such that `cs15` raw log field is mapped to `security_result.summary` UDM field when `cs15Label` is `ViolatedItem`.  
\- Modified condition such that `cs9` raw log field is mapped to `event.idm.read_only_udm.principal.user.userid` UDM field when `cs9Label` is `osUser`.  
\- Modified condition such that `cs8` raw log field is mapped to `event.idm.read_only_udm.target.resource.name` UDM field when `cs8Label` is `DatabaseName` or `ApplicationName`.   
2024-04-01 |  Enhancement -  
\- Added support for JSON logs.   
2023-04-26 |  Enhancement -  
\- Mapped `cs1` to `security_result.rule_name`.  
\- Mapped `cs2` to `principal.group.group_display_name`.  
\- Mapped `cs3` to `principal.hostname`.  
\- Mapped `cs6` to `target.resource_ancestors.name`.  
\- Mapped `cs7` to `target.resource_ancestors.resource_subtype`.  
\- Mapped `cs5` to `metadata.description`.  
\- Mapped `cs12` to `security_result.description`.  
\- Mapped `cs14` to `target.resource.attribute.labels`.  
\- Mapped `cs15` to `security_result.summary`.  
\- Mapped `cs16` to `principal.process.command_line`.  
\- Mapped `cs17` to `target.resource.resource_subtype`.  
\- Parsed `severity` field.  
\- Mapped `act` to `security_result.action_details`.  
\- Mapped `cs13` to `metadata.product_log_id`.   
2022-07-24 |  Enhancement -  
\- Mapped `proto` to `network.ip_protocol`.  
\- Mapped `severity` to `security_result.severity_details`.  
\- Mapped `cs1Label` to `security_result.detection_fields`.  
\- Mapped `cs2Label` to `security_result.detection_fields`.  
\- Mapped `cs3Label` to `security_result.detection_fields`.  
\- Mapped `cs4` to `target.application`.  
\- Mapped `cs5Label` to `security_result.detection_fields`.  
\- Mapped `cs8` to `target.resource.name`.  
\- Mapped `cs9` to `principal.user.userid`.  
\- Mapped `cs10Label` to `additional.fields`.  
\- Mapped `cs11` to `principal.application`.  
\- Mapped `cs12Label` to `additional.fields`.  
\- Mapped `cs13Label` to `additional.fields`.  
\- Mapped `cs14Label` to `additional.fields`.  
\- Mapped `cs16Label` to `additional.fields`.  
\- Mapped `cs17Label` to `additional.fields`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
