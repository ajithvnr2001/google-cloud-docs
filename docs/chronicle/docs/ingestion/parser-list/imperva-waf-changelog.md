---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-waf-changelog/
title: Change log for IMPERVA_WAF \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:43.308911+00:00
---

# Change log for IMPERVA_WAF  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-waf-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IMPERVA_WAF

Date | Changes  
---|---  
2026-08-12 |  Enhancement:  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `kv.ref` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `log.account_id` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `log.account_name` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `log.zone_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `log.zone_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `log.ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `log.destination_addr` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.network.dns.questions.name`: Newly mapped `log.query_hostname` raw log field with `event.idm.read_only_udm.network.dns.questions.name` UDM field.  
\- `event.idm.read_only_udm.network.dns.questions.type`: Newly mapped `log.type` raw log field with `event.idm.read_only_udm.network.dns.questions.type` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `log.is_dnssec_query`, `log.is_replied_from_cache`, `log.is_forwarded` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `log.is_blocked` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.network.dns.response_code`: Newly mapped `log.response_code` raw log field with `event.idm.read_only_udm.network.dns.response_code` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region` and `event.idm.read_only_udm.principal.asset.location.country_or_region`: Newly mapped `log.country_iso_code` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` and `event.idm.read_only_udm.principal.asset.location.country_or_region` UDM fields.  
\- `event.idm.read_only_udm.intermediary.location.city`: Newly mapped `log.pop_name` raw log field with `event.idm.read_only_udm.intermediary.location.city` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: If `log.is_udp_connection` is true, updated the value of `event.idm.read_only_udm.network.ip_protocol` to UDP.  
\- `event.idm.read_only_udm.metadata.event_type`, `event.idm.read_only_udm.network.application_protocol`: If principal data or target data is present and `log.query_hostname`, `log.type` raw log fields are not empty, updated the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_DNS` and `event.idm.read_only_udm.network.application_protocol` to `DNS`.   
2026-08-07 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.id`: Removed mapping of `log.resource_id` from `event.idm.read_only_udm.target.resource.id` UDM field since the UDM field is deprecated.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Mapped `log.resource_id`, `log.imperva.audit_trail.resource_id` raw log fields with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `log.type_description`, `log.assumed_by_user`, `log.code`, `log.imperva.audit_trail.assumed_by`, `log.imperva.audit_trail.resource_type_description` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `log.id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `log.message` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `log.event.dataset` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `log.imperva.audit_trail.resource_type` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Set the value of `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`, When the log has user related data.   
2026-05-13 |  Enhancement:  
\- Added support for new format of CEF logs.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `log_type` log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `end` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `end` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.network.organization_name`: Mapped `organization` log field with `event.idm.read_only_udm.network.organization_name` UDM field if `Customer` is not present.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `organization` log field with `event.idm.read_only_udm.metadata.description` UDM field if `Customer` is present.   
2026-01-08 |  Enhancement:  
\- event.idm.read_only_udm.target.port: Removed mapping of `kv.spt` field from `event.idm.read_only_udm.target.port` UDM field as it was incorrectly mapped.  
\- event.idm.read_only_udm.principal.port: Mapped `kv.spt` raw log field to `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.principal.port: Removed mapping of `kv.cpt` from event.idm.read_only_udm.principal.port UDM field as it was incorrectly mapped.  
\- event.idm.read_only_udm.target.port: Mapped `kv.cpt` raw log field to `event.idm.read_only_udm.target.port` UDM field.  
\- Added null conditional check for `kv.dpt` before mapping to `event.idm.read_only_udm.target.port` UDM field.   
2025-09-09 |  Enhancement:  
\- Added conditional check as block for kv.act to map `event.idm.read_only_udm.security_result.action` as BLOCK  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `kv.cs12` and `kv.cs10` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `kv.cat` raw log fields with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields.value: updated `kv.cs97Label` to `kv.cs97` and `kv.cs9Label` to `kv.cs9`. Reason (Incorrect mapping)  
\- event.idm.read_only_udm.security_result.detection_fields.key: updated `cs97Label` to `kv.cs97Label` and `cs9Label` to `kv.cs9Label`. Reason (Incorrect mapping)   
2025-08-22 |  Enhancement:  
\- Removed duplicate mapping of `kv.spt` raw log field.  
\- Modified parser logic within the block where `principal_present` and `target_present` are true. Added a default behavior if `kv.app` is empty or not present, event.idm.read_only_udm.metadata.event_type will now be set to `NETWORK_HTTP`.  
\- event.idm.read_only_udm.target.ip: Newly mapped `kv.sip` raw log field to event.idm.read_only_udm.target.ip.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `kv.sip` raw log field to event.idm.read_only_udm.target.asset.ip.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `kv.in` raw log field to event.idm.read_only_udm.network.received_bytes.  
\- event.idm.read_only_udm.security_detection_fields: Newly mapped `kv.siteTag` raw log field to event.idm.read_only_udm.security_result.detection_fields with the key sitereferenceid.  
\- event.idm.read_only_udm.security_detection_fields: Changed the detection field key name for `kv.filePermission` from filePermission to attackid.  
\- event.idm.read_only_udm.principal.port: Removed mapping of `port` from event.idm.read_only_udm.principal.port, as the field is more appropriately mapped to the target entity.  
\- event.idm.read_only_udm.target.port: Mapped `port` raw log field to event.idm.read_only_udm.target.port.  
\- event.idm.read_only_udm.target.user.user_display_name: Removed mapping of `kv.cicode` from event.idm.read_only_udm.target.user.user_display_name, as kv.cicode represents a location code, not a username.  
\- event.idm.read_only_udm.principal.location.city: Mapped `kv.cicode` raw log field to event.idm.read_only_udm.principal.location.city.  
\- event.idm.read_only_udm.principal.application: Removed mapping of `kv.requestClientApplication` from event.idm.read_only_udm.principal.application, as this field better fits the User-Agent definition.  
\- event.idm.read_only_udm.network.http.user_agent: Mapped `kv.requestClientApplication` raw log field to event.idm.read_only_udm.network.http.user_agent.  
\- event.idm.read_only_udm.target.port: Removed mapping of `kv.cpt` from event.idm.read_only_udm.target.port, as kv.cpt semantically represents the principal`s port, not the target`s.  
\- event.idm.read_only_udm.principal.port: Mapped `kv.cpt` raw log field to event.idm.read_only_udm.principal.port.  
\- event.idm.read_only_udm.security_result.category_details: Removed mapping of `kv.dproc` from event.idm.read_only_udm.security_result.category_details, as the field is more specific and fits better within detection fields.  
\- event.idm.read_only_udm.security_result.detection_fields: Mapped `kv.dproc` raw log field to event.idm.read_only_udm.security_result.detection_fields with the key browsertype.   
2025-07-14 |  Enhancement:  
\- `event.idm.read_only_udm.network.organization_name`: Newly mapped `Customer` raw log field with `event.idm.read_only_udm.network.organization_name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `siteid`, `deviceExternalId` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `spt` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `cpt` raw log field with `event.idm.read_only_udm.target.port` UDM field.   
2025-05-29 |  Enhancement:  
\- `event.idm.read_only_udm.security_result,severity`: Newly mapped `severity` with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- Added `Block` as a value in a condition to map `event.idm.read_only_udm.security_result.action` to `BLOCK`.  
\- Added a grok pattern to parse `csv_message`.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `product_version` with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details` Newly mapped `cat` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `cs9Label` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_longitude`: Newly mapped `cs8Label` raw log field with `event.idm.read_only_udm.principal.location.region_longitude` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `kv.cat` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `kv.cs8` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-01-16 |  Enhancement:  
\- Mapped `log.imperva.audit_trail.resource_name` to `target.resource.name`.   
2024-11-14 |  Enhancement:  
\- Added support to handle new log format.   
2024-10-10 |  Enhancement:  
\- Mapped `metadata.vendor_name` to `Imperva Cloud WAF`.   
2024-10-03 |  Enhancement:  
\- Mapped `cn1` to `network.http.response_code`.   
2024-09-05 |  Enhancement:  
\- Added support to handle new log format.   
2024-08-27 |  Enhancement:  
\- Changed mapping of `log.imperva.ids.account_name` from `metadata.product_event_type` to `target.user.user_display_name`.   
2024-06-25 |  Enhancement:  
\- Added support to handle JSON logs.   
2024-04-02 |  Enhancement:  
\- Mapped `log.imperva.request_user` to `security_result.detection_fields`.  
\- Mapped `log.imperva.classified_client` to `security_result.detection_fields`.   
2024-02-26 |  Enhancement:  
\- Mapped `log.imperva.request_session_id` to `network.session_id`.  
\- Mapped "`log.imperva.successful_logins_last_24h`,`log.imperva.path` and `log.imperva.failed_logins_last_24h` to `security_result.detection_fields`.  
\- Mapped `log.imperva.risk_reason` to `security_result.severity_details` and `security_result.severity`.  
\- Mapped `additional_factor`,`log.imperva.device_reputation` and `log.imperva.credentials_leaked` to `additional.fields`.  
\- Mapped `log.imperva.fingerprint` to `security_result.description`.  
\- Mapped `log.imperva.referrer` to `network.http.referral_url`.  
\- Mapped `log.imperva.classified_client` to `principal.process.file.full_path`  
2024-02-06 |  Enhancement:  
\- Initialized `accept_encoding_label`, `site_name_label`, `random_id_label`, `request_type_label`, `accept_language_label`, `headers_connection_label`, `zuid_labels`, `site_id_label`, `policy_id`, `policy_name`, `selector_derived_id`, `hsig`, `selector`, `detection_fields_event_action`, `detection_fields_event_context`, `detection_fields_significant_domain_name`, and `detection_fields_domain_risk` to null inside the `for loop` for json_array.   
2024-01-27 |  Enhancement:  
\- Mapped `description` to `security_result.threat_name`.  
\- Mapped `severity` to `security_result.threat_id`.  
\- Mapped `kv.src`, `src` and `log.client.ip` to `principal.asset.ip`.  
\- Mapped `kv.dst` and `dst` to `target.asset.ip`.  
\- Mapped `kv.dvc` to `about.asset.ip`.  
\- Mapped `kv.cs9` and `cs9` to `security_result.rule_name`.  
\- Mapped `kv.fileType` and `fileType` to `security_result.rule_type`.  
\- Mapped `dst` to `target.asset.ip`.  
\- Mapped `xff` and `forwardedIp` to `intermediary.asset.ip`.  
\- Mapped `log.client.domain` to `principal.asset.hostname`.  
\- Mapped `log.server.domain` to `target.asset.hostname`.   
2023-10-16 |  Bug-Fix:  
\- Initialized `security_result` and `security_action` to null inside the `for loop` for json_array.  
\- Added a null check before merging `security_action` to `security_result.action`.  
\- When `log.imperva.abp.monitor_action` is `block`, then mapped `security_action` to `BLOCK`.   
2023-09-26 |  Enhancement:  
\- Mapped `significant_domain_name`, `domain_risk`, `violated_directives` to `security_result.detection_fields` in CSP logs.   
2023-08-07 |  Bug-fix -  
\- Added support to parse array of JSON logs.  
\- Added Grok pattern to check for hostname before mapping `xff` to `intermediary.hostname`.   
2023-06-16 |  Bug-fix -  
\- Mapped `imperva.audit_trail.event_action` to `security_result.detection_fields`.  
\- Mapped `imperva.audit_trail.event_action_description` to `security_result.detection_fields`.  
\- Mapped `imperva.audit_trail.event_context` to `security_result.detection_fields`.  
\- Mapped `imperva.audit_trail.event_context_description` to `security_result.detection_fields`.  
\- Fixed Timestamp parsing issues.  
\- Dropped malformed logs.  
\- Resolved presubmit issue due to single on_error for two fields.   
2023-06-08 |  Enhancement -  
\- Mapped `imperva.abp.apollo_rule_versions` to `security_result.detection_fields`.  
\- Mapped `imperva.abp.bot_violations` to `security_result.detection_fields`.  
\- Mapped `imperva.abp.bot_behaviors` to `security_result.detection_fields`.  
\- Mapped `imperva.abp.bot_deciding_condition_ids` to `security_result.detection_fields`.  
\- Mapped `imperva.abp.bot_deciding_condition_names ` to `security_result.detection_fields`.  
\- Mapped `imperva.abp.bot_triggered_condition_ids` to `security_result.detection_fields`.  
\- Mapped `imperva.abp.bot_triggered_condition_names` to `security_result.detection_fields`.   
2023-04-26 |  Enhancement -  
\- Defined the field `kv.src` in the statedata.  
\- Mapped `kvdata.ver` to `network.tls.version` and network.tls.cipher.  
\- Mapped `kvdata.sip` to `principal.ip`.  
\- Mapped `kvdata.spt` to `principal.port`.  
\- Mapped `kvdata.act` to `security_result.action_details`.  
\- Mapped `kvdata.app` to `network.application_protocol`.  
\- Mapped `kvdata.requestMethod` to `network.http.method`.   
2023-02-04 |  Enhancement -  
\- For field `deviceReceiptTime` added rebase = true in `event.timestamp`.   
2023-01-19 |  Enhancement -  
\- Added support to parser logs by adding following mappings.  
\- Mapped `event.provider` to `principal.user.userid`.  
\- Mapped `client.ip` to `principal.ip`.  
\- Mapped `client.domain` to `principal.hostname`.  
\- Mapped `imperva.abp.request_type` to `principal.labels`.  
\- Mapped `imperva.abp.pid` to `principal.process.pid`.  
\- Mapped `client.geo.country_iso_code` to `principal.location.country_or_region`.  
\- Mapped `server.domain` to `target.hostname`.  
\- Mapped `server.geo.name` to `target.location.name`.  
\- Mapped `url.path` to `target.process.file.full_path`.  
\- Mapped `imperva.abp.customer_request_id` to `target.resource.id`.  
\- Mapped `imperva.abp.token_id` to `target.resource.product_object_id`.  
\- Mapped `imperva.abp.random_id` to `additional.fields`.  
\- Mapped `http.request.method` to `network.http.method`.  
\- Mapped `user_agent.original` to `network.http.parsed_user_agent`.  
\- Mapped `imperva.abp.headers_referer` to `network.http.referral_url`.  
\- Mapped `imperva.abp.zuid` to `additional.fields`.  
\- Mapped `imperva.ids.site_name` to `additional.fields`.  
\- Mapped `imperva.ids.site_id` to `additional.fields`.  
\- Mapped `imperva.ids.account_name` to `metadata.product_event_type`.  
\- Mapped `imperva.ids.account_id` to `metadata.product_log_id`.  
\- Mapped `imperva.abp.headers_accept_encoding` to `security_result.detection_fields`.  
\- Mapped `imperva.abp.headers_accept_language` to `security_result.detection_fields`.  
\- Mapped `imperva.abp.headers_connection` to `security_result.detection_fields`  
\- Mapped `imperva.abp.policy_id` to `security_result.detection_fields`.  
\- Mapped `imperva.abp.policy_name` to `security_result.detection_fields`.  
\- Mapped `imperva.abp.selector_derived_id` to `security_result.detection_fields`.  
\- Mapped `imperva.abp.monitor_action` to `security_result.action`.   
2022-06-28 |  Enhancement -  
Mapped vendor.name = Imperva and product.name = Web Application Firewall for all logs  
Changed `metadata.event_type` where the `src` is `Distributed` from `GENERIC_EVENT` to `USER_UNCATEGORIZED`  
Changed `metadata.event_type` to `USER_UNCATEGORIZED` to `USER_STATS`  
2022-06-20 |  Modified grok pattern for field `rt`.  
Bug-fix - Improvements to security_result.action.  
\- REQ_PASSED: If the request was routed to the site`s web server (security_result.action = `ALLOW').  
\- REQ_CACHED_X: If a response was returned from the data center`s cache (security_result.action = `ALLOW').  
\- REQ_BAD_X: If a protocol or network error occurred (security_result.action = `FAIL`).  
\- REQ_CHALLENGE_X: If a challenge was returned to the client (security_result.action = `BLOCK`).  
\- REQ_BLOCKED_X: If the request was blocked (security_result.action = `BLOCK`).   
2022-06-14 |  Bug-fix - Added gsub and modified the kv filter to avoid incorrect mapping of fields `cs1Label`, `cs2Label`, `cs3Label` mapped to UDM field `security_result.detection_fields`.   
2022-05-26 |  Bug-fix - Removed key name and colon character from the value of the detection fields.   
2022-05-10 |  Enhancement - Mapped the following fields:  
\- `cs1`, `cs2`, `cs3`, `cs4`, `cs5`, `fileType`, `filePermission` to `security_result.detection_fields`.  
\- `cs7` to `principal.location.region_latitude`.  
\- `cs8` to `principal.location.region_longitude`.  
\- `cn1`, `cn2` to `security_result.detection_fields` for CEF format logs.  
\- `act` to `security_result.action` and `security_result.action_details` for CEF format logs.  
\- `app` to `network.application_protocol` for CEF format logs.  
\- `requestClientApplication` to `network.http.user_agent` for CEF format logs.  
\- `dvc` to `about.ip` for CEF format logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
