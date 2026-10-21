---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-dra-changelog/
title: Change log for IMPERVA_DRA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:39:30.583102+00:00
---

# Change log for IMPERVA_DRA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-dra-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IMPERVA_DRA

Date | Changes  
---|---  
2026-04-30 |  \- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `client_ip`, `source_ip` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `action_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `client_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `destination_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `destination_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `distinguished_name_device_id` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `distinguished_name`, `distinguished_name_ou` raw log fields with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `distinguished_name_user` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `rule_name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `packet_size` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: If `action` is `allow`, updated the value of `event.idm.read_only_udm.security_result.action` to ALLOW.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `collective_id`, `collective_name`, `connection_type`, `entitlement_token_id`, `json_wrapper.appname`, `json_wrapper.facility`, `start`, `json_wrapper.priority` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `rule_subnet` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-01-16 |  \- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `srcUser` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `srcApp` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `msg` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cat` raw log field with `event.idm.read_only_udm.additional.fields.value.string_value` UDM field (where `event.idm.read_only_udm.additional.fields.key` is set to `Category`).  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `server.dbName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `server.dbUser` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `server.dbType` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Removed mapping of `suser` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field to introduce a more accurate mapping.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `suser` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field as `principal.user.userid` is more suitable field for mapping of `suser` raw log field.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Newly mapped `IMPERVA` value with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `Data_Risk_Analytics` value with `event.idm.read_only_udm.metadata.product_name` UDM field.   
2025-10-24 |  \- event.idm.read_only_udm.src.ip: Newly mapped `srcHosts` raw log field with `event.idm.read_only_udm.src.ip` UDM fields.  
\- event.idm.read_only_udm.src.asset.ip: Newly mapped `srcHosts` raw log field with `event.idm.read_only_udm.src.asset.ip` UDM fields.  
\- event.idm.read_only_udm.src.hostname: Newly mapped `srcHosts` raw log field with `event.idm.read_only_udm.src.hostname` UDM fields.  
\- event.idm.read_only_udm.src.asset.hostname: Newly mapped `srcHosts` raw log field with `event.idm.read_only_udm.src.asset.hostname` UDM fields.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `dstHosts` raw log field with `event.idm.read_only_udm.target.hostname` these UDM fields.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `dstHosts` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- The date filter for `event_timestamp` was updated to rebase the timestamp.  
\- Parser logic was updated to iterate over array-based raw log fields (srcIps, sourceApps, dstIps, destinationAccount, destination, destinationType) and map individual elements to their corresponding UDM fields.  
\- Added conditional check for srcHosts to map to either IP or hostname UDM fields based on its format.  
\- Added conditional check for dstIps. If a value is not a valid IP, it is mapped to event.idm.read_only_udm.additional.fields.   
2025-10-02 |  \- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `srcUsers` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `srcIps` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `srcIps` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `srcHosts` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `srcHosts` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `sourceApps` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `dstIps` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `dstIps` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `dstHosts` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `dstHosts` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `destinationAccount` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `destination` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.resource.resource_subtype: Newly mapped `destinationType` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- event.idm.read_only_udm.target.resource.type: Newly mapped `accessedTables` raw log field with `event.idm.read_only_udm.target.resource.type` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `securityEventTimestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `actionType` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `severity`, `numOfAccessedObjects`, `userAction`, `clusterNames` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly added dynamic mapping of `severity` raw log field to key `severity` within `event.idm.read_only_udm.additional.fields` if severity matches (?i)test-severity.  
\- event.idm.read_only_udm.security_result.severity: Changed mapping for event.idm.read_only_udm.security_result.severity from a direct mapping of severity to a conditional mapping based on the value of the severity raw field.   
2024-09-26 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
