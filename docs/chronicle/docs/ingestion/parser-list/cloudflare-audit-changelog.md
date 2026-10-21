---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudflare-audit-changelog/
title: Change log for CLOUDFLARE_AUDIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:34:57.106809+00:00
---

# Change log for CLOUDFLARE_AUDIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudflare-audit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CLOUDFLARE_AUDIT

Date | Changes  
---|---  
2026-08-24 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ActorIPAddress` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `ActionTimestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `AuditLogID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `AccountID` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ActorContext`, `ActorTokenDetails.name`, `ActorTokenDetails.id`, `AccountName`, `ResourceScope`, `ResourceProduct` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `ResourceResponse.name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `Raw.uri` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `Raw.method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `Raw.status_code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `ActionDescription` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Mapped `ActionResult` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `ResourceRequest.append`, `ResourceResponse.description`, `ResourceResponse.id`, `ResourceResponse.type`, `Raw.cf_ray_id` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `Raw.user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.   
2026-08-06 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.id`: Removed mapping of `ResourceID` from `event.idm.read_only_udm.target.resource.id` UDM field as it is deprecated UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `action.info` raw log field with `event.idm.read_only_udm.security_result.description` UDM field  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `action.type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `newValueJson.session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `newValueJson`, `oldValueJson`, `newValue`, `oldValue` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `actor.ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `resource.type` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `resource.id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Newly mapped `owner.id` raw log field with `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `interface` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `actor.email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `actor.id` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.   
2026-01-01 |  Enhancement:  
\- Modified the condition to set the event type as USER_RESOURCE_UPDATE_CONTENT only when principal user id or principal email is present.  
\- Modified the condition to set the event type as USER_RESOURCE_ACCESS only when principal user id and principal machine data is present.  
\- event.idm.read_only_udm.metadata.event_type: Newly mapped to STATUS_UPDATE when principal machine data is present.   
2023-11-27 |  Enhancement:  
\- Added a Grok pattern to match new log format.  
\- Mapped `ResourceID` to `target.resource.product_object_id`.  
\- Mapped `metainfo_zone_name` to `principal.hostname`.  
\- Mapped `metainfo_user_id` to `principal.user.userid`.  
\- Mapped `metainfo_user_email` to `principal.user.email`.  
\- Mapped `metainfo_user_tag` to `principal.user.product_object_id`.  
\- Mapped `metainfo` fields to `security_result.detection_fields`.  
\- Mapped `newvalue_session_id` to `network.session_id`.  
\- Mapped `NewValue` to `security_result.detection_fields`.  
\- Mapped `OldValue` to `security_result.detection_fields`.  
\- If `ActorID` is present, set `metadata.event_type` to `USER_RESOURCE_ACCESS`.   
2023-07-09 |  New parser created.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
