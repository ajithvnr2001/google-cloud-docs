---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ping-changelog/
title: Change log for PING \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:49.212895+00:00
---

# Change log for PING  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ping-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PING

Date | Changes  
---|---  
2026-07-16 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.name`: Removed mapping of `resource.name` raw log field from `event.idm.read_only_udm.target.resource.name` UDM field when `resource.name` is an email address.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Mapped `resource.name` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Removed mapping of `actors.client.name` from `event.idm.read_only_udm.principal.user.user_display_name` UDM field when `actors.client.name` is an application.  
\- `event.idm.read_only_udm.principal.application`: Mapped `actors.client.name` raw log field with `event.idm.read_only_udm.principal.application` UDM field.   
2026-06-16 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped key-value pairs from `record._embedded.riskEvaluation.event1.customAttributes` raw log field with `event.idm.read_only_udm.additional.fields` UDM field, where each key from the raw log is prefixed with `riskEvaluation.event.customAttributes.` in the UDM.   
2026-05-28 |  Enhancement:  
\- Updated the date filter for `event.idm.read_only_udm.metadata.event_timestamp` to use the `recorded` field and support `yyyy-dd-MMTHH:mm:ss.SSS` and `yyyy-MM-ddTHH:mm:ss.SSS` as input formats.   
2026-04-22 |  Enhancement:  
\- event.idm.read_only_udm.principal.ip: Newly mapped `client.ipAddress` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `client.ipAddress` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `source` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Added support for date format `yyyy-MM-ddTHH:mm:ss.SSS` in `recorded` field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `result.message` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `event_data.client.id` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `actor.name` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Removed mapping of `actor.name` from `event.idm.read_only_udm.principal.user.user_display_name` UDM field as it contains email address.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `actor.name` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.target.resource.id: Removed mapping of `resource.id` from `event.idm.read_only_udm.target.resource.id` UDM field as `resource.id` is deprecated.  
\- event.idm.read_only_udm.target.resource.product_object_id: If `index` = `0`, mapped `resource.id` raw log field to `event.idm.read_only_udm.target.resource.product_object_id` UDM field else it is mapped to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.type: Removed mapping of `resource.type` from `event.idm.read_only_udm.target.resource.type` UDM field as `resource.type` is deprecated.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `resource.type` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.name: If `index` = `0`, mapped `resource.name` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field else it is mapped to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.about.resource.attribute.labels: Newly mapped `resource.idpEntityId` raw log field with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.   
2025-12-01 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `record._embedded.notificationPolicy.id` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `remoteMtpIp` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `remoteMtpIp` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ntype`, `nsmtpResponse`, `nprocessingTimeMillis`, `nreportingMTA` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Updated the `event.idm.read_only_udm.metadata.event_type` UDM field to `USER_LOGIN` when has_principal_user is true else if to `NETWORK_CONNECTION` when has_principal and has_target is true.   
2025-11-06 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `record._embedded.modifiedAttributes`,`record._embedded.externalId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `record.source.ipAddress` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `record.source.ipAddress` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `record.source.userAgent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `correlationId` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Changed mapping for event.idm.read_only_udm.security_result.detection_fields from record.CorrelationId to record.correlationId UDM field.   
2025-10-31 |  Enhancement:  
\- Added handling for a nested JSON structure within the `message` field when an `event` key is present.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `resource.ipaddress`, `Previous Authentication IP` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `resource.ipaddress`, `Previous Authentication IP` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `resource.token`, `event_data.result.status`, `Geovelocity Whitelist Met`, `Risk Level`, `Policy Met`, `Rule Met` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `resource.websession` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.target.resource.id: Newly mapped `Requested Application ID` raw log field with `event.idm.read_only_udm.target.resource.id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Accessing Device Browser`,`Previous Country`, `IP Reputation Whitelist Met`, `Previous Authentication Time`, `Ground Speed`, `Current VPN/Proxy login`, `New Device`, `Password Reset`, `Self Service Device Management`, `Time since last Authentication`, `Device Model`, `Device Lock Enabled`, `Device Rooted or Jailbroken`, `Device enrolled in MDM`, `Device biometrics supported` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `event_data.recorded` field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- Updated mapping of `network` field to `event.idm.read_only_udm.network` UDM field.   
2025-06-13 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `recordedAt` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field   
2025-05-16 |  Enhancement:  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `cluster_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `kubernetes` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `column7` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `column7` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `column23` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `column23` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `column22`, `column24` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `column25` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-03-03 |  Enhancement:  
\- Mapped `actors.user.id` to `target.user.userid`.  
\- Mapped `actors.user.name` to `target.user.user_display_name`.  
\- Mapped `actors.user.type` to `target.user.attribute.roles`.  
\- Mapped `actors.user.environment.id` to `target.resource.attribute.labels`.  
\- Mapped `actors.user.href` to `target.url`.  
\- Mapped `actors.user.population.id` to `target.resource.attribute.labels`.  
\- Mapped `internalCorrelation.sessionId` to `network.session_id`.  
\- Mapped all fields with `_embedded` to `additional.fields`.   
2024-11-27 |  Enhancement:  
\- Mapped `details.device.id` to `principal.asset.asset_id`  
\- Mapped `externalId`,`estimatedDistance`,`lastSeen`,`externalLastSeen` and `os_name_label` to `additional.fields`  
2024-11-07 |  Enhancement:  
\- Added mappings for the following fields: `riskEvent`, `riskDetails`, `riskResult`, and `riskEvaluation`.   
2024-07-29 |  Enhancement:  
\- Added support for a new pattern of JSON logs.   
2024-06-17 |  Enhancement:  
\- Added support to handle unparsed SYSLOG + KV logs.   
2023-12-07 |  Bugfix:  
\- Mapped `actors.client.type` to `principal.user.attribute.roles`.  
\- Mapped `actors.client.name` to `principal.user.user_display_name`.  
\- Mapped `actors.client.id` to `principal.user.userid`.  
\- Mapped `actors.client.href` to `principal.url`.  
\- Mapped `source.userAgent` to `network.http.user_agent`.  
\- Mapped `source.ipAddress` to `principal.ip`.  
\- Mapped `resources.href` to `target.url`.   
2023-04-06 |  Enhancement:  
\- Parsed logs ingested in JSON format.  
\- Added new Grok pattern to handle failing SYSLOG+JSON logs because of change in date format.  
\- Mapped `result.message.Country` to `principal.location.country_or_region`.  
\- Modified mapping for `resource.status` from `security_result.about.labels` to `security_result.about.resource.attribute.labels`.   
2022-08-04 |  Enhancement:  
\- Mapped user_id to principal.user.userid.  
\- wrote grok to extract user_id.   
2022-07-21 |  Enhancement:  
\- Added a new grok pattren for logs with product_event_type DEBUG.  
\- Mapped description to metadata.description.  
\- Mapped product_event_type to metadata.product_event_type.  
\- Mapped src_host to principal.hostname.  
\- Mapped src_port to principal.port.  
\- Mapped userid to principal.user.userid.  
\- Mapped sr_description to security_result.description.  
\- Mapped sr_summary to security_result.summary.  
\- Mapped event_type to USER_UNCATEGORIZED where userid not null.   
2022-07-08 |  Enhancement:  
\- Modified mapping for `actor.type` from `principal.user.role_name` to `principal.user.attribute.roles`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
