---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-firewall-changelog/
title: Change log for AZURE_FIREWALL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:45:41.401644+00:00
---

# Change log for AZURE_FIREWALL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-firewall-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AZURE_FIREWALL

Date | Changes  
---|---  
2026-08-13 |  Enhancement:  
\- Added support for parsing new format of JSON logs.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Added support for new format of `event.idm.read_only_udm.metadata.event_timestamp`.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `from_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `target_ip` raw log field with `event.idm.read_only_udm.target.ip`/`event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `from_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `target_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `rule` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `Action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `operationName`, `rule_collection`, raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: When principal and target data is present, setting the value to NETWORK_CONNECTION.   
2026-04-13 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `_TimeReceived` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `TransactionId`, `LineDetails`, `PolicyId`, `PolicyScope`, `PolicyScopeName`, `DetailedData`, `isSuccess`, `message` and `_SubscriptionId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ClientIp` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `Hostname` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.file.names`: Newly mapped `FileDetails` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `RequestUri` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `OperationName` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.intermediary.resource.name`: Newly mapped `InstanceId` raw log field with `event.idm.read_only_udm.intermediary.resource.name` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `errorCode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `Message` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `RuleId` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_set`: Newly mapped `RuleSetType` raw log field with `event.idm.read_only_udm.security_result.rule_set` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_version`: Newly mapped `RuleSetVersion` raw log field with `event.idm.read_only_udm.security_result.rule_version` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: If `Action` is `MATCHED`, updated the value of `event.idm.read_only_udm.security_result.action` to `ALLOW`.  
\- Added a condition to prevent the removal of backslash characters from the `message` field when the `Type` field is `AGWFirewallLogs`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `DetailedMessage`, `_IsBillable` and `_BilledSize` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-02-12 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: If `category` is `AZFWDnsQuery` and `network_dns_questions` is present, then `event.idm.read_only_udm.metadata.event_type` is updated to `NETWORK_DNS`.  
\- `event.idm.read_only_udm.network.application_protocol`: If `category` is `AZFWDnsQuery` and `network_dns_questions` is present, then `event.idm.read_only_udm.network.application_protocol` is set to `DNS`.   
2025-09-29 |  Enhancement:  
\- Added grok pattern to extract `request_duration_seconds` and `request_duration_nanos` from `properties.RequestDurationSecs` raw log field.  
\- event.idm.read_only_udm.network.session_duration.seconds: Newly mapped `properties.RequestDurationSecs` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- event.idm.read_only_udm.network.session_duration.nanos: Newly mapped `properties.RequestDurationSecs` raw log field with `event.idm.read_only_udm.network.session_duration.nanos` UDM field.  
\- Added gsub to remove trailing dot from `properties.QueryName`.  
\- Added grok pattern for `properties.QueryName` raw log field to extract the value without the trailing dot.   
2025-08-14 |  Enhancement:  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `res_name` extracted from `resourceId` raw log field to `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields: Newly mapped `metricName` (key: `Metric Name`), `count` (key: `Count`), `total` (key: `Total`), `minimum` (key: `Minimum`), `maximum` (key: `Maximum`), `average` (key: `Average`), `timeGrain` (key: `Time Grain`) raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `subscription` (key: `Subscription`) and `res_group` (key: `Resource Group`), extracted from `resourceId` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.   
2025-06-23 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.security_result.severity`: Modified mapping of `properties.Severity` raw log field with `event.idm.read_only_udm.metadata.security_result.severity` UDM field.  
\- When `properties.Severity` is `1` then changed mapping of `event.idm.read_only_udm.metadata.security_result.severity` from `INFORMATIONAL` to `CRITICAL`.  
\- When `properties.Severity` is `2` then changed mapping of `event.idm.read_only_udm.metadata.security_result.severity` from `LOW` to `HIGH`.  
\- When `properties.Severity` is `4` then changed mapping of `event.idm.read_only_udm.metadata.security_result.severity` from `HIGH` to `LOW`.  
\- When `properties.Severity` is `5` then changed mapping of `event.idm.read_only_udm.metadata.security_result.severity` from `CRITICAL` to `INFORMATIONAL`.   
2025-06-17 |  Enhancement:  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `properties.ActionReason` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `properties.Flag` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `loggingSourceName`, `properties.IsTlsInspected`, and `properties.IsExplicitProxyRequest` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-05-28 |  Enhancement:  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `properties.Action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.metadata.additional.fields: Newly mapped `properties.SignatureId`, `properties.Fqdn` raw log field with `event.idm.read_only_udm.metadata.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `properties.Description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `properties.Severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `properties.Url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `properties.ThreatDescription` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `properties.Category` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.   
2025-05-13 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_name: Removed mapping of `Azure Firewall Application Rule` from `event.idm.read_only_udm.metadata.product_name` UDM field and mapped `Azure Firewall` instead  
\- event.idm.read_only_udm.metadata1.product_name: Removed mapping of `Azure Firewall Application Rule` from `event.idm.read_only_udm.metadata1.product_name` UDM field and mapped `Azure Firewall` instead   
2025-03-11 |  Enhancement:  
\- Mapped `Policy`, `RuleCollection`, and `RuleCollectionGroup` to `additional.fields`.  
\- Changed mapping for `rulecollection` from `security_result.detection_fields` to `additional.fields`.  
\- Changed mapping for `Properties.RuleCollection` from `security_result.detection_fields` to `additional.fields`.  
\- Changed mapping for `Properties.RuleCollectionGroup` from `security_result.detection_fields` to `additional.fields`.  
\- Changed mapping for `Properties.Policy` from `security_result.detection_fields` to `additional.fields`.   
2025-03-05 |  Enhancement:  
\- Mapped `DestinationIp` to `target.ip` and `target.asset.ip`.   
2025-02-25 |  Enhancement:  
\- Added support to parse the unparsed logs.  
\- Mapped `IpAddress` to `principal.ip`.  
\- Mapped `DNSport` to `principal.port`.  
\- Mapped `DNSMessage` to `security_result.description`.   
2025-02-17 |  Enhancement:  
\- Added support to parse the unparsed logs.  
\- Mapped `SourcePort` to `principal.port`.  
\- Mapped `DestinationPort` to `target.port`.  
\- Mapped `SourceIp` tp `principal.ip`.  
\- Mapped `Fqdn` to `principal.hostname`.  
\- Mapped `ActionReason` to `security_result.summary`.  
\- Mapped `IsTlsInspected` , `Policy` , `RuleCollection` , `Rule` and `IsExplicitProxyRequest` to `additional.fields`.  
\- Mapped `_ItemId` to `metadata.product_log_id`.  
\- Mapped `_ResourceId` to `principal.resource.id`.  
\- Mapped `Type` to `metadata.product_event_type`.  
\- Mapped `TenantId` to `principal.user.product_object_id`.  
\- Mapped `_Internal_WorkspaceResourceId` to `principal.resource.attribute.labels`.  
\- Mapped `TargetUrl` to `target.url`.  
\- Mapped `RuleCollectionGroup` to `observer.group.group_display_name`.   
2024-12-26 |  Bug fix:  
\- When the logs contain the keyword `Alert`, mapped `security_result.action` to `ALLOW`.   
2024-11-13 |  Enhancement:  
\- Mapped `Action` to `security_result.detection_fields`.  
\- Mapped `Signature` to `security_result.detection_fields`.  
\- Mapped `IDS` to `security_result.detection_fields`.  
\- Mapped `Priority` to `security_result.priority_details`.  
\- Mapped `Classification` to `security_result.detection_fields`.   
2024-09-04 |  Enhancement:  
\- Mapped `from_ip` to `dns.questions.name` for DNS events.   
2024-07-02 |  Enhancement:  
\- Added support to handle a new format of timestamp.   
2024-04-29 |  Enhancement  
\- Added support to handle a new format of ingested logs.   
2024-02-07 |  Enhancement  
\- Mapped `ICMP type` to `additional.fields`.  
\- Mapped `Action` and `properties.Action` to `security_result.action_details`.   
2023-06-01 |  Enhancement  
\- Newly ingested JSON logs of category `AZFWDnsQuery` are parsed.  
\- Mapped `properties.msg` in newly ingested JSON logs of category `AzureFirewallNetworkRule`.   
2022-04-29 |  Bug fix - Newly ingested JSON logs are parsed to increase the overall parsing percentage.  
\- operationName mapped to metadata.product_event_type.  
\- resourceId mapped to metadata.product_log_id.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
