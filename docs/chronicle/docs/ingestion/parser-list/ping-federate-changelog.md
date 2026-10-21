---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ping-federate-changelog/
title: Change log for PING_FEDERATE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:34:52.978616+00:00
---

# Change log for PING_FEDERATE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ping-federate-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PING_FEDERATE

Date | Changes  
---|---  
2026-08-13 |  Enhancement:  
\- `event.idm.read_only_udm.target.url`: Newly mapped `column5` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.principal.url`: Newly mapped `column6` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column3`, `column9`, `Issuer`, `AssertionConsumerServiceURL`, `Destination`, `IssueInstant`, `ProtocolBinding`, `ProviderName`, `AllowCreate`, `Format`, `Comparison`, `AuthnContextClassRef` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `ID` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `Version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `column7` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `column7` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- Mapped `event.idm.read_only_udm.security_result.action` to `ALLOW`/`BLOCK` and `event.idm.read_only_udm.security_result.action_details` to `success`/`failure` based on SAML status success pattern in `column7`.   
2025-10-15 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `xff` raw log field to `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.asset.ip: Newly mapped `xff` raw log field to `event.idm.read_only_udm.intermediary.asset.ip` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `logType` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-06-25 |  Enhancement:  
\- Added support for new pattern of JSON logs by adding a Grok pattern followed by a JSON filter.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `transactionId` and `policyName` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Replaced values of newer raw log field names to their corresponding old raw log field names to map data to UDM fields using existing mappings as follows:  
\-- `pfhost` -> `host`  
\-- `trackingid` -> `trackingId`  
\-- `connectionid` -> `connectionId`  
\-- `adapterid` -> `adapterId`  
\-- `APP` -> `app`  
\-- `COMP` -> `comp`  
\-- `responsetime` -> `responseTimeMs`  
2025-06-09 |  Enhancement:  
\- event.idm.read_only_udm.target.hostname and event.idm.read_only_udm.target.asset.hostname: Removed mapping of `pfhost` from `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field as `pfhost` is the system that is acting as an intermediary and it's more relevant to map it to intermediary.  
\- event.idm.read_only_udm.intermediary.hostname and event.idm.read_only_udm.intermediary.asset.hostname: Mapped `pfhost` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM field  
\- event.idm.read_only_udm.principal.user.userid: Removed mapping of `subject` from `event.idm.read_only_udm.principal.user.userid` UDM field as this is the target of the authentication process.  
\- event.idm.read_only_udm.target.user.userid: Mapped `subject` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped 'event.idm.read_only_udm.security_result.action` as `ALLOW` when `status` raw log field value is `success|inprogress` and `BLOCK` when `status` raw log field value is `failure`.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `status` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Removed prefix `TID:` from `trackingid` raw log field from `event.idm.read_only_udm.target.resource.product_object_id` UDM field because the raw log itself has the prefix in it.   
2025-05-07 |  Enhancement:  
\- target_resource_sudo_value: Newly mapped `event.idm.read_only_udm.target.resource.product_object_id` to `target_resource_sudo_value` raw log field .  
\- Added a conditional check before mapping `event_type` to `USER_RESOURCE_ACCESS`.   
2025-04-11 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `product` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `startupID` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `threadID` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `conn` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `op` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `msgID` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `requesterDN` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `base` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `scope` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `filter` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `sizeLimit` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `timeLimit` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `deref` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `typesOnly` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `attrs` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `clientConnectionPolicy` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `reason` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `requesterIP` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `requesterIP` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `prin_host` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `prin_host` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `from` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `from` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `fromPort` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `toPort` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `to` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `to` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.resource.name : Newly mapped `instanceName` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- Added a conditional check before mapping `column3` to `event.idm.read_only_udm.metadata.description`.  
\- `NETWORK_CONNECTION`: Added support for the event `NETWORK_CONNECTION` if, `has_principal` and `has_target` are true.  
\- `STATUS_UPDATE` : Added support for the event `STATUS_UPDATE` if, `has_principal` is true.  
\- Added a Grok pattern to parse the unparsed logs.  
\- Added a conditional check before mapping `column3` to `event.idm.read_only_udm.metadata.description`.   
2025-03-12 |  Enhancement:  
\- Removed mapping for `ip` from `target.ip`.  
\- Removed mapping for `subject` from `target.user.userid`.  
\- Removed mapping for `connectionid` from `target.url`.  
\- Removed mapping for `protocol` from `target.application`.  
\- Mapped `ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `subject` to `principal.user.userid`.  
\- Mapped `connectionid` to `target.application`.  
\- Mapped `protocol` to `additional.fields`.   
2024-11-21 |  Enhancement:  
\- Added support to parse unparsed logs.   
2024-10-24 |  Enhancement:  
\- Added a Grok pattern to extract `client_id` and mapped it to `additional.fields`.   
2024-10-10 |  Enhancement:  
\- Added support to parse unparsed logs.  
\- mapped `suser` and `duid` to `target.user.userid`.  
\- mapped `src` to `principal.ip`.  
\- mapped `cs3` to `target.application`.  
\- mapped `dvchost` to `principal.hostname`.  
\- mapped `cs4` , `requestClientApplication` , `msg` , `cs2` ,and `cs4` to `additional.fields`.   
2024-10-07 |  Enhancement:  
\- Changed mapping of `subject` field from `additional.fields` to `target.user.userid`.  
\- Changed mapping of `connectionid` field from `additional.fields` to `target.url`.   
2024-08-20 |  Enhancement:  
\- Added support to handle unparsed syslog and KV logs.   
2023-04-24 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
