---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/winevtlog-changelog/
title: Change log for WINEVTLOG \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:51.916851+00:00
---

# Change log for WINEVTLOG  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/winevtlog-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WINEVTLOG

Date | Changes  
---|---  
2026-09-29 |  \- Handled edge case scenarios for `SYSLOG + JSON` format logs.   
2026-09-25 |  \- Handled edge case scenarios for logs with EventID 5136.   
2026-09-18 |  \- Handled edge case scenarios for the `Task` raw log field.   
2026-09-11 |  \- Added Xpath for `RuleSddl` and `RuleName` raw log fields for XML format.  
\- `target.file.sha256`: Newly mapped `FileHash` raw log field with `target.file.sha256` UDM field for XML log format of windows event 8002.   
2026-07-16 |  \- `principal.labels[SubjectLogonId]`: Updated the key name for `principal.labels` UDM field for events 6416, 5137, and 5141 to make it consistent.  
\- `additional.fields[Subject Logon Id]`: Removed mapping of `SubjectLogonId` from `additional.fields` UDM field for event 6416 to remove duplicate field mapping.  
\- `additional.fields[SubjectLogonId]`: Updated the key name of `additional.fields` udm field for field `SubjectLogonId` for events 5137, and 5141 to make it consistent.   
2026-07-08 |  \- Updated the field mapping for Windows Event ID 2889 and the Microsoft-Windows-ActiveDirectory_DomainService provider.  
\- `principal.administrative_domain`: Removed mapping of `Data_1`(Extracted the domain from the Data_1 raw field value) from `principal.administrative_domain` UDM field  
\- `target.administrative_domain`: Mapped `Data_1`(Extracted the domain from the Data_1 raw field value) raw log field with `target_udm_field` UDM field  
\- `principal.user.userid`: Removed mapping of `Data_1`(Extracted the user details from the Data_1 raw field value) from `principal.user.userid` UDM field   
\- `target.user.userid`: Mapped `Data_1`(Extracted the user details from the Data_1 raw field value) raw log field with `target_udm_field` UDM field  
\- `metadata.event_type`: Updated the `metadata.event_type` value from `SYSTEM_AUDIT_LOG_UNCATEGORIZED` to `USER_LOGIN`  
2026-06-16 |  \- additional.fields[MessageNumber] : Newly mapped `/Event/EventData/Data[@Name=`MessageNumber`]` raw log field with `additional.fields[MessageNumber]` UDM field for XML log format of windows event 4104 and provider `Microsoft-Windows-PowerShell`.  
\- additional.fields[MessageTotal] : Newly mapped `/Event/EventData/Data[@Name=`MessageTotal`]` raw log field with `additional.fields[MessageTotal]` UDM field for XML log format of windows event 4104 and provider `Microsoft-Windows-PowerShell`.   
2026-06-12 |  \- `target.resource.attribute.labels`: Newly mapped `UserAccountControl` raw log field with `target.resource.attribute.labels` UDM field for winlogbeat format.   
2026-05-19 |  \- `principal.ip`: Newly mapped `host.ip` raw log field with `principal.ip` UDM field for winlogbeat format of windows event ID `4625`.   
2026-05-05 |  \- `additional.fields[winlog_computer_name]`: Newly mapped `winlog.computer_name` raw log field with `additional.fields[winlog_computer_name]` UDM field for winlogbeat format logs.   
2026-04-06 |  \- `additional.fields[ServiceStartType]`: Newly mapped `ServiceStartType` raw log field with `additional.fields[ServiceStartType]` UDM field for XML log format of windows event 4697.   
2026-04-03 |  \- Handled edge case scenarios for the `SourceAddress` raw log field.   
2026-04-01 |  Updated the field mapping for windows Event ID 8015, 8018, 8019, 8020, 8027, 8033, 8010, 8017.  
\- `intermediary.ip`: Removed mapping of `DnsServerList` from `intermediary.ip` UDM field.  
\- `target.ip`: Mapped `DnsServerList` raw log field with `target.ip` UDM field.  
\- `target.asset.ip`: Mapped `DnsServerList` raw log field with `target.asset.ip` UDM field.  
\- `target.ip`: Removed mapping of `Ipaddress` from `target.ip` UDM field.  
\- `target.asset.ip`: Removed mapping of `Ipaddress` from `target.asset.ip` UDM field.  
\- `principal.ip`: Mapped `Ipaddress` raw log field with `principal.ip` UDM field.  
\- `principal.asset.ip`: Mapped `Ipaddress` raw log field with `principal.asset.ip` UDM field.   
2026-03-09 |  \- `target.process.pid`: Newly mapped `NewProcessId` raw log field with `target.process.pid` UDM field for XML log format of windows event 4688.   
2026-02-13 |  \- `target.resource.attribute.labels`: Newly mapped `UserAccountControl` raw log field with `target.resource.attribute.labels` UDM field for Windows Event 4738, 4720, 4741, and 4742. The values are converted to their corresponding descriptions.   
2026-01-16 |  Updated the Winevtlog parser to handle edge cases in the `SidList` raw field for events 4908 and 4964.   
2025-12-30 |  \- Handle edge case for `security_result.category` UDM field.   
2025-12-08 |  \- Updated mapping for the XML fields within raw log field `TargetServerName` for Windows event 4648 to introduce more accurate mappings.  
\- Avoids overwriting `TargetServerName` with `TargetUserName` in the `target.hostname` and `target.asset.hostname` field.   
2025-11-28 |  \- `XML`: Added support for `XML` log format for Windows event `2889`.   
2025-11-25 |  \- Added mapping for the following XML fields from `TaskContent` for Windows events 4699, 4700, and 4701, and from `TaskContentNew` for Windows event 4702:  
\- `target.resource.attribute.labels`: Newly mapped `/Task/@version` and `/Task/@xmlns` raw log fields with `target.resource.attribute.labels` UDM field.  
\- `target.user.attribute.labels`: Newly mapped `/Task/Principals/Principal/@id` raw log field with `target.user.attribute.labels` UDM field.  
\- `target.resource.attribute.labels`: Newly mapped `/Task/Actions/@Context` raw log field with `target.resource.attribute.labels` UDM field.   
2025-11-11 |  \- `additional.fields`: Mapped `insertId` raw log field with `additional.fields` UDM field.  
\- `additional.fields`: Mapped `TimeGenerated` raw log field with `additional.fields` UDM field.  
\- `additional.fields`: Mapped `TimeWritten` raw log field with `additional.fields` UDM field.  
\- `additional.fields`: Mapped `EventType` raw log field with `additional.fields` UDM field.  
\- `additional.fields`: Mapped `EventCategory` raw log field with `additional.fields` UDM field.  
\- `additional.fields`: Mapped `qualifiers` raw log field with `additional.fields` UDM field.  
\- `additional.fields`: Mapped `logName` raw log field with `additional.fields` UDM field.  
\- `additional.fields`: Mapped `new_process_exe` raw log field with `additional.fields` UDM field.   
2025-10-28 |  \- intermediary.ip: Newly mapped `HostIP` raw log field with `intermediary.ip` UDM field.   
2025-08-19 |  -  
\- src.hostname: Newly mapped `CallerComputerName` raw log field with `src.hostname` UDM field for eventid 4740.   
2025-08-14 |  -  
\- principal.process.pid: Newly mapped `/Event/EventData/Data[@Name=`ProcessID`]` raw log field with `principal.process.pid` UDM field for EventIDs: 5156,5157.   
2025-07-29 |  -  
\- Additionally handled the parsing logic for the `SamAccountName` raw log field for Windows event 5830.  
\- target.hostname: Mapped `SamAccountName` raw log field with `target.hostname` UDM field.  
\- target.asset.hostname: Mapped `SamAccountName` raw log field with `target.asset.hostname` UDM field.   
2025-07-24 |  \- Updated the parsing logic and UDM field mapping for the `Workstation` and `WorkstationName` raw log field to handle various formats as mentioned below, to introduce more accurate mappings:  
\- IP values: Now mapped to `principal.ip` and maps the full value `principal.hostname`.  
\- Hostname or \\\\\Hostname values: Now mapped to `principal.hostname` by extracting hostname value.  
\- FQDN values: Extracts the portion before the first dot as `principal.hostname` and the remaining domain as `principal.administrative_domain` (or `principal.asset.network_domain` if SubjectDomainName is present).  
\- Domain\Hostname values: Extracts `principal.hostname` and maps the domain to `principal.administrative_domain` (or `principal.asset.network_domain` if SubjectDomainName is present).  
\- IP:Port values: Extracts IP to `principal.ip`, port to `principal.port`, and maps the full value to `principal.hostname`.  
\- principal.asset.asset_id: Removed mapping of `Workstation` and `WorkstationName` from `principal.asset.asset_id` UDM field.  
\- principal.asset.attribute.labels: Removed mapping of `Workstation` and `WorkstationName` from `principal.asset.attribute.labels` UDM field.  
\- principal.asset_id: Removed mapping of `Workstation` and `WorkstationName` from `principal.asset_id` UDM field.  
\- principal.asset.hostname: Removed mapping of `Workstation` and `WorkstationName` from `principal.asset.hostname` UDM field for inaccurate field value `-`.  
\- principal.hostname: Removed mapping of `Workstation` and `WorkstationName` from `principal.hostname` UDM field for inaccurate field value `-`.  
\- intermediary.hostname: Newly mapped `Computer` raw log field with `intermediary.hostname` UDM field.  
\- Mapping for windows event ID 5140 is updated as below to introduce more accurate mappings:  
\- principal.hostname: Removed mapping of `Computer` from `principal.hostname` UDM field.  
\- principal.asset.hostname: Removed mapping of `Computer` from `principal.asset.hostname` UDM field.  
\- target.hostname: Mapped `raw_field` raw log field with `target.hostname` UDM field.  
\- target.asset.hostname: Mapped `raw_field` raw log field with `target.asset.hostname` UDM field.  
\- Update key label from `Channel` to `EventData_Channel` for `additional.fields` UDM field for windows event ID 19 to resolve the flaky behavior.   
2025-07-17 |  \- `32850, 32867, 32868, 24577, 8193, 8194, 8197`: Added support for the events `32850, 32867, 32868, 24577, 8193, 8194, 8197` for provider `Microsoft-Windows-Powershell` and relevant corresponding raw log fields.  
\- `8001, 8003`: Added support for the events `8001, 8003` for provider `Microsoft-Windows-WLAN-AutoConfig` and relevant corresponding raw log fields.  
\- `2004`: Added support for the event `2004` for provider `Microsoft-Windows-DriverFrameworks-UserMode` and relevant corresponding raw log fields.  
\- For windows event IDs `4802, 4803` for provider `Microsoft-Windows-Security-Auditing`, the following mappings are changed in order to introduce more accurate mappings  
\- target.user.windows_sid: Removed mapping of `TargetUserSid` from `target.user.windows_sid` UDM field.  
\- principal.user.windows_sid: Mapped `TargetUserSid` raw log field with `principal.user.windows_sid` UDM field  
\- target.user.attribute.labels: Removed mapping of `TargetUserSid` from `target.user.attribute.labels` UDM field.  
\- principal.user.attribute.labels: Mapped `TargetUserSid` raw log field with `principal.user.attribute.labels` UDM field  
\- target.administrative_domain: Removed mapping of `TargetDomainName` from `target.administrative_domain` UDM field.  
\- principal.administrative_domain: Mapped `TargetDomainName` raw log field with `principal.administrative_domain` UDM field  
\- For windows event ID `4624, 4625,4648 , 4768, 4770, 4771` for provider `Microsoft-Windows-Security-Auditing`, the following mappings were changed in order to introduce more accurate mappings:  
\- src.ip: Removed mapping of `IpAddress` from `src.ip` UDM field.  
\- src.asset.ip: Removed mapping of `IpAddress` from `src.asset.ip` UDM field.  
\- principal.ip: Mapped `IpAddress` raw log field with `principal.ip` UDM field  
\- src.port: Removed mapping of `IpPort` from `src.port` UDM field.  
\- principal.port: Mapped `IpPort` raw log field with `principal.port` UDM field  
\- For windows event ID `4624, 4625, 4768, 4769, 4770, 4771` for provider `Microsoft-Windows-Security-Auditing`, the following mappings were removed as the raw log field is already mapped to a different UDM field (removing duplications):  
\- principal.hostname: Removed mapping of `Computer` from `principal.hostname` UDM field.  
\- principal.asset.hostname: Removed mapping of `Computer` from `principal.hostname` UDM field.  
\- For windows event ID `4624, 4625, 4794, 4776` for provider `Microsoft-Windows-Security-Auditing`, the following mappings were changed in order to introduce more accurate mappings:  
\- principal.asset_id: Removed mapping of `Workstation` from `principal.asset_id` UDM field.  
\- principal.asset.asset_id: Removed mapping of `Workstation` from `principal.asset.asset_id` UDM field.  
\- principal.hostname: Mapped `Workstation` raw log field with `principal.hostname` UDM field  
\- principal.asset.hostname: Mapped `Workstation` raw log field with `principal.asset.hostname` UDM field  
\- security_result.action: Newly set `security_result.action` UDM field for providers below:  
\- Microsoft-Windows-Security-Auditing  
\- Microsoft-Windows-TerminalServices-RemoteConnectionManager  
\- Microsoft-Windows-Kerberos-Key-Distribution-Center  
\- Microsoft-Windows-Security-Kerberos  
\- Microsoft-Windows-AppLocker  
\- Microsoft-Windows-Windows Defender  
\- Microsoft-Windows-TerminalServices-LocalSessionManager  
\- Security  
\- AD FS Auditing  
\- Added support for new events for providers `Microsoft-Windows-Bits-Client`  
\- `3008`: Added support for the events `3008` for provider `Microsoft-Windows-DNS-Client` and relevant corresponding raw log fields.  
\- `1125`: Added support for the event `1125` for provider `Microsoft-Windows-GroupPolicy` and relevant corresponding raw log fields.   
2025-06-30 |  Handled edge case for raw log field `UserName` for EventID: 5860.   
2025-06-09 |  \- `additional.fields.key/value.string_value`: Newly mapped `/Event/EventData/Data[@Name=`PreAuthEncryptionType`]` raw log field with `additional.fields.key/value.string_value` UDM field for EventID: 4768.  
\- `additional.fields.key/value.string_value`: Newly mapped `/Event/EventData/Data[@Name=`ClientAdvertizedEncryptionTypes`]` raw log field with `additional.fields.key/value.string_value` UDM field for EventID: 4768.  
\- `additional.fields.key/value.string_value`: Newly mapped `/Event/EventData/Data[@Name=`RequestTicketHash`]` raw log field with `additional.fields.key/value.string_value` UDM field for EventID: 4769.  
\- `additional.fields.key/value.string_value`: Newly mapped `/Event/EventData/Data[@Name=`ResponseTicketHash`]` raw log field with `additional.fields.key/value.string_value` UDM field for EventID: 4769.  
\- `additional.fields.key/value.string_value`: Newly mapped `/Event/EventData/Data[@Name=`AccountSupportedEncryptionTypes`]` raw log field with `additional.fields.key/value.string_value` UDM field for EventID: 4768 and 4769.  
\- `additional.fields.key/value.string_value`: Newly mapped `/Event/EventData/Data[@Name=`AccountAvailableKeys`]` raw log field with `additional.fields.key/value.string_value` UDM field for EventID: 4768 and 4769.  
\- `additional.fields.key/value.string_value`: Newly mapped `/Event/EventData/Data[@Name=`ServiceSupportedEncryptionTypes`]` raw log field with `additional.fields.key/value.string_value` UDM field for EventID: 4768 and 4769.  
\- `additional.fields.key/value.string_value`: Newly mapped `/Event/EventData/Data[@Name=`ServiceAvailableKeys`]` raw log field with `additional.fields.key/value.string_value` UDM field for EventID: 4768 and 4769.  
\- `additional.fields.key/value.string_value`: Newly mapped `/Event/EventData/Data[@Name=`DCSupportedEncryptionTypes`]` raw log field with `additional.fields.key/value.string_value` UDM field for EventID: 4768 and 4769.  
\- `additional.fields.key/value.string_value`: Newly mapped `/Event/EventData/Data[@Name=`DCAvailableKeys`]` raw log field with `additional.fields.key/value.string_value` UDM field for EventID: 4768 and 4769.  
\- `additional.fields.key/value.string_value`: Newly mapped `/Event/EventData/Data[@Name=`SessionKeyEncryptionType`]` raw log field with `additional.fields.key/value.string_value` UDM field for EventID: 4768 and 4769.   
2025-04-23 |  \- `additional.fields.key/value.list_value`: Newly mapped `/Event/RenderingInfo/Keywords/Keyword` raw log field with `additional.fields.key/value.list_value` UDM field.   
2025-04-15 |  Added support for multiple new fields across various Windows Event IDs as part of the WINEVTLOG parser update.   
2025-04-09 |  \- `security_result.detection_fields[statement]` -> (Changed UDM Field Value) ->Previously, the `\n` character was removed from the `statement` raw log field value for Windows event 33205 with source `MSSQL`. -> The gsub for the `statement` field has now been updated to retain the `\n` character in the value.   
2025-04-01 |  \- `metadata.description` (New UDM field mapping) → No UDM mapping to mapping of the `Message` field from the raw log of Windows event 15457 and source MSSQL.   
2025-03-07 |  \- `security_result.detection_fields[statement]` \--> (Changed UDM Field Mapping) -> Earlier, the `statement` raw log field was truncated for the Windows event 33205 and source `MSSQL` -> The grok pattern for the `statement` raw log field has been updated to map the entire value.   
2025-02-28 |  \- Added support for the following fields for event IDs 403, 404, 410, 510, 1102, and 1203 in the `AD FS Auditing` provider.  
\- Event ID - 403  
\- `msg1` => `additional.fields`  
\- `instance_id` => `target.resource.product_object_id`  
\- `activity_id` => `additional.fields`  
\- `request_detail` => `additional.fields`  
\- `year-month-day:time` => `metadata.event_timestamp`  
\- `http_method` => `target.network.http.method`  
\- `url_absolute_path` => `target.url`  
\- `query_string` => `additional.fields`  
\- `content_length` => `additional.fields`  
\- `caller_identity` => `additional.fields`  
\- `certificate_identity` => `additional.fields`  
\- `target_relying_party` => `additional.fields`  
\- `through_proxy` => `additional.fields`  
\- `proxy_dns_name` => `additional.fields`  
\- Event ID - 404  
\- `msg1` => `additional.fields`  
\- `instance_id` => `target.resource.product_object_id`  
\- `activity_id` => `additional.fields`  
\- `response_detail` => `additional.fields`  
\- `year-moth-day:time` => `metadata.event_timestamp`  
\- Event ID - 410  
\- `msg1` => `additional.fields`  
\- `activity_id` => `additional.fields`  
\- `x_ms_client_application` => `additional.fields`  
\- `x_ms_client_user_agent` => `additional.fields`  
\- `client_request_id` => `additional.fields`  
\- `x_ms_forwarded_client_ip` => `additional.fields`  
\- `x_ms_proxy` => `additional.fields`  
\- `x_ms_adfs_proxy_client_ip` => `additional.fields`  
\- Event ID - 510  
\- `msg1` => `additional.fields`  
\- `instance_id` => `target.resource.product_object_id`  
\- `Connection` => `additional.fields`  
\- `Content-Type` => `additional.fields`  
\- `Host` => `additional.fields`  
\- `charset` => `additional.fields`  
\- `X-MS-Endpoint-Absolute-Path` => `additional.fields`  
\- `Cache-Control` => `additional.fields`  
\- Event ID - 1102  
\- `msg1` => `additional.fields`  
\- `activity_id` => `additional.fields`  
\- `request_detail` => `additional.fields`  
\- `client_ip` => `target.ip`  
\- `requested_url` => `target.url`  
\- `client_certificate_serial` => `network.tls.client.certificate.serial`  
\- `client_certificate_subject` => `network.tls.client.certificate.subject`  
\- Event ID - 1203  
\- `EventData/Data1` => `additional.fields`  
\- `EventData/Data2/AuditBase/AuditType` => `additional.fields`  
\- `EventData/Data2/AuditBase/AuditResult` => `additional.fields`  
\- `EventData/Data2/AuditBase/FailureType` => `additional.fields`  
\- `EventData/Data2/AuditBase/ErrorCode` => `additional.fields`  
\- `EventData/Data2/AuditBase/ContextComponents/Component/RelyingParty - xsi:type=`ResourceAuditComponent\` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/ClaimsProvider - xsi:type=`ResourceAuditComponent\` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/UserId - xsi:type=`ResourceAuditComponent\` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/PrimaryAuth - xsi:type=`AuthNAuditComponent"` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/DeviceAuth - xsi:type=`AuthNAuditComponent"` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/DeviceId - xsi:type=`AuthNAuditComponent"` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/MfaPerformed - xsi:type=`AuthNAuditComponent"` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/MfaMethod - xsi:type=`AuthNAuditComponent"` => `additional.fields"  
\- `EventData/Data2/EventData/Data2/AuditBase/ContextComponents/Component/TokenBindingProvidedId - xsi:type=`AuthNAuditComponent"` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/TokenBindingReferredId - xsi:type=`AuthNAuditComponent"` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/SsoBindingValidationLevel - xsi:type=`AuthNAuditComponent"` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/OAuthClientId - xsi:type=`ProtocolAuditComponent"` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/OAuthGrant - xsi:type=`ProtocolAuditComponent"` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/Server - xsi:type=`RequestAuditComponent"` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/AuthProtocol - xsi:type=`RequestAuditComponent"` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/NetworkLocation - xsi:type=`RequestAuditComponent"` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/IpAddress - xsi:type=`RequestAuditComponent"` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/ForwardedIpAddress - xsi:type=`RequestAuditComponent"` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/ProxyIpAddress - xsi:type=`RequestAuditComponent"` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/NetworkIpAddress - xsi:type=`RequestAuditComponent"` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/ProxyServer - xsi:type=`RequestAuditComponent"` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/UserAgentString - xsi:type=`RequestAuditComponent"` => `additional.fields"  
\- `EventData/Data2/AuditBase/ContextComponents/Component/Endpoint - xsi:type=`RequestAuditComponent"` => `additional.fields"   
2025-02-24 |  \- Removed duplicated mapping of `intermediary.hostname` for Windows event 4768.   
2025-02-19 |  \- Mapped `ClientAdvertizedEncryptionTypes` field with `additional.fields` UDM field for EventID: 4769 of the JSON format.   
2025-02-17 |  \- Added support for the raw log field `Message` to `additional.fields[Message]`.   
2025-02-14 |  \- Added support for event 33205 with source name starting with MYSQL for the XML format.   
2025-02-13 |  \- Added UDM validation for USER_CREATION, SCHEDULED_TASK_CREATION, USER_CHANGE_PERMISSIONS, and USER_RESOURCE_UPDATE_PERMISSIONS.  
\- Additional field mappings when `INSTALL_DATE` or `UF_TYPE` is present in the log:  
\- Mapped the EventType, ignoreOlderThan, and evt_resolve_ad_obj raw log fields to additional.fields.  
\- Added support for TaskCategory to additional.fields for EventID 4719.  
\- Added support for Message to metadata.description for EventID 4781.  
\- Added support for TargetLogonGuid to additional.fields for EventID 4624.  
\- Added support for Group_Membership to target.user.group_identifiers for EventID 4627.  
\- Added support for AccessList to target.resource.attribute.permissions for EventID 4662.  
\- Added support for AccessList and Properties to target.resource.attribute.permissions and security_result.detection_fields for EventID 4662.  
\- Added support for AppendData_or_AddSubdirectory_or_CreatePipeInstance, CONTROL, DAC, DELETE, ReadAttributes, WriteAttributes, WriteData_or_AddFile, and WriteEA to security_result.detection_fields for EventIDs 5145 and 5140.  
\- Added support for Result_Code to target.resource.attribute.labels for EventIDs 4720, 4738, 4741, or 4742.  
\- Added support for ObjectType and subjectlogonid to target.resource.resource_subtype and additional.fields for EventID 5145.  
\- Added support for SubjectLogonId and Access_Mask to additional.fields for EventID 5140.  
\- Added support for Message and Access_Mask to metadata.description for EventIDs 5805, 1643, 1644, and 1713.  
\- Added support for clientip and clientport to src.ip and src.port for EventID 1643.  
\- Added support for clientip to src.ip for EventID 1643.  
\- Added support for Query to metadata.description for EventIDs 5861, 5857, 5858, 5859, and 5860.  
\- Added support for Message to additional.fields for EventID 5860.  
\- Added support for the following fields to additional.fields: xmlns, OperationType, Attribute_selection, Attribute, Attributes_Preventing_Optimization, BackupType, Clean_pages_modified, Dirty_pages_modified, Expensive_search_operations, Inefficient_search_operations, NetworkInformation, Number_of_search_operations, Pages_preread_from_disk, Pages_read_from_disk, Pages_referenced, Perm_Consumer, Returned_entries, Search_scope, Search_time_ms, Starting_node, Time_interval_hours, Used_indexes, and Visited_entries.   
2025-02-07 |  \- Handled the parsing error in the `principal.port` UDM field.  
\- Added support for the following log fields to the UDM field, for Windows Event 1000:  
\- FaultingApplicationPath => additional.fields  
\- FaultingModulePath => additional.fields   
2025-02-04 |  Enhancement:  
\- Added Grok patterns to parse `Security ID`, `User Name`, `Domain`, `Logon ID` and `Client Address` fields for Windows Event 4825 of the cloud ops format.  
\- Added support for the field `SubjectLogonId` to `additional.fields[SubjectLogonId]` for Windows Event 4825.   
2025-01-28 |  \- Added support for the following log fields to the UDM field, for Windows Event 4688 in the Winlogbeat format, as outlined below:  
\- process.parent.executable => principal.process.file.full_path  
\- process.parent.name => principal.process.file.names  
\- process.name => target.process.file.names   
2025-01-22 |  \- Added support for the field `CertIssuerName`, `CertSerialNumber`, `CertThumbprint` and `ResponseTicket` for EventID: 4768 of the JSON format.  
\- Added support for source names MSSQL$EVAULT_P1, MSSQL$AVID_MAIN_P1, and MSSQL$ABC_M1   
2025-01-08 |  \- Updated event validation logic for `PROCESS_LAUNCH`, `SYSTEM_AUDIT_LOG_UNCATEGORIZED`, `PROCESS_UNCATEGORIZED`, `PROCESS_OPEN`, `PROCESS_TERMINATION`, `SERVICE_UNSPECIFIED`, `SERVICE_STOP`, `SERVICE_MODIFICATION`, `SERVICE_CREATION`, `STATUS_STARTUP`, `STATUS_SHUTDOWN`, `STATUS_UPDATE` UDM events.   
2025-01-02 |  \- Mapped `Path` field with `target.file.full_path` for EventID: 4104.   
2024-12-26 |  \- Fixed flaky behavior.   
2024-12-07 |  \- Adding a Grok pattern to remove leading and trailing spaces from the `LogonProcessName` field.   
2024-12-06 |  \- Added support for the field `KeyLength` for xml format.   
2024-12-02 |  \- Added support for raw log field `UserName` and `FullName` for windows event 10025.   
2024-11-28 |  \- Updated grok for event 33205.   
2024-11-27 |  \- Mapped `SubjectLogonId` field to `additional.fields` UDM field for windows event 4756.   
2024-11-26 |  \- Added support for `LmPackageName` field for EventID: 4624 of the XML format.   
2024-11-25 |  \- Mapped `ObjectServer` raw log field to `target.resource_ancestors.name` UDM field.   
2024-11-15 |  \- Added support for `DN` field for windows event 5136.   
2024-11-13 |  \- Added support to parse the Splunk UF `classic` JSON format of the windows event logs.   
2024-10-18 |  \- Added support for well known sid names for windows event 4627.   
2024-10-04 |  \- Added support for field `Keywords` log field.   
2024-09-27 |  \- Handled the newline characters (`\n`) by replacing them with commas (`,`) in the `PrivilegeList` log field for the logs forwarded using the Bind Plane agent.  
\- Updated event validation for windows event 4104.  
\- Added support for the field `HandleId` in event 4662.   
2024-09-20 |  \- Added support for field `ServiceType` and `StartType` in event 7045.   
2024-09-18 |  \- Added support for field `EventData.ErroCode` in event 5035 and 5037.  
\- Updated the mapping of the fields `Client Address` and `Client Port` for Windows event IDs 4768, 4770, and 4771.  
\- Updated event validation for `USER_LOGIN` UDM event.  
\- Added support for `PreAuthType` log field for XML format logs.   
2024-09-17 |  \- Updated mapping of `Workstation` log field to `principal.hostname` for windows event 4776.  
\- Added support of `TdoType`, `TdoDirection`, `TdoAttributes`, `SidFilteringEnabled` log fields for EventID: 4706, 4716  
\- Added support of `DomainSid` log field for EventID: 4706, 4707, 4716, 4865, 4867, 4866.  
\- Added support of `ForestRoot`, `ForestRootSid`, `OperationId`, `EntryType`, `Flags`, `TopLevelName`, `DnsName`, `NetbiosName`, `SubjectLogonId` log fields for EventID: 4865, 4866, 4867.   
2024-09-13 |  \- Added support for the raw log field `Param1`, `Param2` and `Param3` for the EventID: 1149 and `User` and `Address` for the EventID: 21.   
2024-08-30 |  \- Added support for raw log field `ProcessId` and `ProcessName` for windows event 4689.  
\- Udpdate logic for `MemberName` field and Updated mapping for `MemberSid` and `TargetDomainName` field for events 4728, 4729, 4732, 4733, 4756, 4757.   
2024-08-16 |  \- Added support of field `TargetSid` for windows event 4704.   
2024-08-09 |  \- Added support for the raw log field `ObjectDN` for the event 5137, 5141.  
\- Added support for Windows Powershell events 400.  
\- Update the mapping of HostApplication and HostName for Windows Powershell events 403.  
\- Added support for `message` fields and update the mapping of HostApplication for Windows Powershell events 800.  
\- Added support for `message` fields and update the mapping of HostApplication for Windows Powershell events 4103.  
\- Added support for `message` fields and update the mapping of ScriptBlockText for Windows Powershell events 4104.   
2024-07-11 |  \- Extracted the UserId from the Task Content raw log field and mapped with the additional.fields of the UDM model.  
\- Added support for the raw log field `winlog.event_data.AccessMask` for the event 5145.  
\- Added support for the fields under the raw log field `winlog.user_data`.  
\- Added support for the raw log field `host.ip` for the event 4625.  
\- Added support for the raw log field `MemberName` for the event 4728, 4729, 4732, 4733, 4756, 4757.  
\- Added support for the raw log field `EventData.PreviousTim` and `EventData.NewTime` for the event 4616.  
\- Added support for the raw log field `TargetSid` for the event 4704.  
\- Added support for the event id 33205 with source name MSSQL$SSDB01$AUDIT.   
2024-06-14 |  \- Added support for unparsed logs for event 1102.   
2024-06-12 |  \- Added support for Windows event 1116 for sourcename `Microsoft-Windows-Windows Defender`.  
\- Added support for new Grok for event 4698.  
\- Added support for raw log field `winlog.user.name`, `winlog.user.domain`, and `message`.   
2024-06-05 |  \- Added support for `RunLevel` and `GroupId` field for windows event ID 4698.  
\- Added mapping for `Messasge` raw log field for the event 15457.   
2024-05-08 |  \- Added support of elements inside of `winlog.event_data.param1` field.   
2024-05-01 |  \- Added support for `Data/ScriptBlockText` field.  
\- Added support for `ObjectClass` field for event id `5139`.   
2024-04-24 |  \- Handled the `metadata.event_type` UDM mapping for EventIDs 530, 531, 532, 533, 534, 535, 536, 537, and 539, similar to EventID 4625.  
\- Updated the mapping for `workstation` raw log field.  
\- Added the mapping for the EventID 1149.  
\- Added support of string and integer value types for `LogonType` field.   
2024-03-27 |  \- Extracted the username, port, and IP address from the Message raw log field for EventID: 2889.  
\- Mapped `PasswordLastSet` raw log field with `target.user.last_password_change_time` UDM field for EventID: 4738.  
\- Changed mapping of `RuleName` and `RuleId` raw log field for Event ID: 4945, 4947 and 4948.   
2024-03-13 |  \- Added additional mappings for `noun.labels` deprecated fields.  
\- Update mapping for EventID 4769.  
\- Add support for `event_data` object fields.  
\- Add mapping of `target.application` UDM field for 11707 event.   
2024-02-29 |  \- Added support for additional JSON format logs.   
2024-02-28 |  \- Added mapping of field `winlog.event_data.payload` for EventID: 4103.  
\- Added mapping of fields `TemplateVersion`, `TemplateSchemaVersion`, `TemplateOID`, `TemplateDSObjectFQDN`, `DCDNSName`, `TemplateContent`, and `SecurityDescriptor` for EventID: 4898.  
\- Added mapping of field `RelativeTargetName` for EventID: 5145.   
2024-02-14 |  \- Added mapping of field `TargetLogonId`.  
\- Added mapping of field `PeerName`, `ProtocolSequence` and `SecurityError` for EventID: 4816.   
2024-01-31 |  \- Added mapping of field `NewObjectDN` for EventID: 5139.   
2024-01-17 |  \- Bug fix   
2024-01-16 |  Enhancement:  
\- When `EventID` is 4732 then a Grok pattern is added to extract `name` from `MemberName` and is mapped to `principal.user.user_display_name` .   
2024-01-04 |  \- Added support for the additional fields for `EventID`: 4886, 4887.   
2023-11-29 |  \- Added a Grok pattern to extract data from `Message` log field for EventID: 1535.  
\- Aligned `principal/target.hostname` and `principal/target.asset.hostname` mapping.   
2023-11-01 |  \- For EventID: 4778, changed the following mappings:  
`Hostname` raw log field to `target.hostname`.  
`Clientname` raw log field to `principal.hostname`.  
`ClientAddress` raw log field to `principal.ip`.   
2023-10-18 |  \- Added mapping of fields `Version`, `Level`, `Task`, `Opcode`, `Keywords`, `ThreadID`, and `PackageName` for EventID: 4776.  
\- Parsed unsupported Event IDs to set `metadata.event_type` to either `GENERIC_EVENT` or `STATUS_UPDATE`.   
2023-10-04 |  \- Mapped `Workstation` field to the `principal.asset_id` UDM field.  
\- Removed mapping sheet link from WINEVTLOG parser code.   
2023-09-20 |  \- Added about.labels with key as `creator_process_exe` and `new_process_exe` for EventID: 4688   
2023-09-06 |  \- Parsed `OU`, `CN`, `DC` fields from the message field for `EventID 4728`.  
\- Copied value of `principal.hostname` to `principal.asset.hostname` if the `principal.asset.hostname` is remaining empty in the parser.  
\- Added support for new EventID: 40962, 53504, 40961 of SourceName `Microsoft-Windows-PowerShell`.   
2023-08-23 |  \- Added mapping of fields `AccessMask` and `ObjectType` for EventID: 4656.  
\- Added support for new EventID: 852, 17137, 49930 of SourceName `MSSQLSERVER`.   
2023-08-09 |  \- Added support for new EventID: 2006, 2001, 216, 2003, 2005, 637, 327 of SourceName `ESENT`.  
\- Added support for new EventID: 202, 103, 119, 141, 106, 108, 110, 118, 142 of SourceName `Microsoft-Windows-TaskScheduler`.  
\- Added `convert` filter to handle the parsing for EventID: 4690 of SourceName `Microsoft-Windows-Security-Auditing`  
\- Added support for new EventID: 17063 of SourceName `MSSQLSERVER`.   
2023-07-26 |  \- Added support for new EventID: 105 of SourceName `ESENT`.  
\- Added support for new EventID: 4440 of SourceName `Microsoft-Windows-Complus`.  
\- Added support for new EventID: 8200, 1004, 1014, 8197, 20482, 1033, 1013, 1067, 12304, 1036, 20489, 20481, 1025, 12305, 12311, 20488 of SourceName `Microsoft-Windows-Security-SPP`.  
\- Added support for new EventID: 1281 of SourceName `Microsoft-Windows-TPM-WMI`.  
\- Added support for new EventID: 63 of SourceName `Microsoft-Windows-WMI`.  
\- Added support for new EventID: 1025, 11724, 1005, 1038, 1029 of SourceName `MsiInstaller`.  
\- Added support for new EventID: 7030 of SourceName `Service Control Manager`.   
2023-07-12 |  Resolved validation error for event `SYSTEM_AUDIT_LOG_WIPE`.   
2023-06-28 |  \- Added support for new EventID: 4105 of SourceName `Microsoft-Windows-PowerShell`.  
\- Added support for new EventID: 403 of SourceName `PowerShell`.   
2023-06-14 |  Updated the parser to include `parse_network_http_user_agent` to use `Parsed User Agent` and `User Agent`.   
2023-05-31 |  \- Added mapping of field `URI` and `Command` for EventID: 4698.  
\- Added mapping of `AccessMask` for EventID: 4663.  
\- Added mapping of `Message` and `ScriptBlockText` log fields for Event Id: 4104.  
\- Mapped `Opcode` with `about.labels`.  
\- Changed mapping for `WorkstationName` log field.  
\- Added support for new EventID: 5447 of SourceName `Microsoft Corporation`.  
\- Added a Grok pattern to extract data from `Message` log field for EventID: 4776, 4624, 4672, 4697, 7045.   
2023-05-02 |  1\. Added support for new EventID: 8 of SourceName `WSH`.  
2\. Added mapping of field `param2` for EventID: 7036.  
3\. Added support for new ADFS Event IDs: 1200,1201,1202,1203,1204,1205,1206,1207.   
2023-04-12 |  1\. Added support for new EventIDs 3005 and 3006 of SourceName LogRhythm Agent.  
2\. Changed mapping of fields `Hostname`, `WorkstationName`, `ClientName` and `Workstation`.   
2023-03-29 |  1\. For `Event ID 7036`, when value is `stopped` in field `param2`, changed `security_result.action` from `BLOCK` to `ALLOW`.  
2\. Handled mapping of invalid hostname. Mapped it to `principal.labels` if validation fails.   
2023-03-01 |  Added support for new format of cloud storage logs.   
2023-02-15 |  1\. Added support for new EventID: 325 of SourceName Microsoft-Windows-TaskScheduler.  
2\. Added Support for new EventID: 0 (SourceName: edgeupdate).  
3\. Added support for new EventID: 8 (SourceName: CylanceSvc).  
4\. Added mapping for TokenElevationType, MandatoryLabel for EventID: 4688.   
2023-02-01 |  1\. Added support for IT (Italian) and DE (German) language for parsing EventID 1102   
2022-11-23 |  1\. Handled properties field coming in message field for EventID: 4662.   
2022-11-09 |  1\. Changed EventType Mapping for EventId: 4776 of Microsoft-Windows-Security-Auditing.   
2022-08-26 |  1\. Changed EventType Mapping for EventId: 7036 of Service Control Manager.   
2022-08-12 |  1\. Added support for new EventID: 8010, 8017 of SourceName Microsoft-Windows-DNS-Client.  
2\. Added support for new EventID: 5857, 5858, 5859, 5860 of SourceName Microsoft-Windows-WMI-Activity.  
3\. For field PossibleCause, added on_error tag for handling replace failure error.  
4\. If target.hostname is empty then we have mapped DnsHostName with target.hostname UDM field otherwise we have mapped DnsHostName with target.asset.attribute.labels.key/value.   
2022-08-01 |  1) Added support for new EventID:8021, 8022, 8025 of SourceName Microsoft-Windows-AppLocker.  
2) Added mapping for FilePath,FileHash,Fqbn for EventID 8003, 8004, 8006, 8007.  
3) Added mapping of Message field for EventID 1100.  
4) Removed target_user_id due to dupliucation issue with target_group_display_name for EventID 4728,4732.  
5) Added support for new EventID: 105, 6, 7 of SourceName WudfUsbccidDriver  
6) Added support for new EventID: 12 of SourceName Microsoft-Windows-EnhancedStorage-EhStorTcgDrv  
7) Added support for new EventID: 11 of SourceName Microsoft-Windows-Wininit  
8) Added support for new EventID: 1068 of SourceName Microsoft-Windows-GroupPolicy   
2022-07-11 |  1) Added support of new EventID:195, 196 of SourceName Microsoft-Windows-USB-USBHUB3.  
2) Added support of new EventID:10001, 10002, 10100 of SourceName Microsoft-Windows-DriverFrameworks-UserMode.  
3) Added support of new EventID:1014, 8015, 8018, 8019, 8020, 8027, 8033 of SourceName Microsoft-Windows-DNS-Client.  
4) Removed user.role_name and user.role_description, Replaced with user.attribute.roles.name and user.attribute.roles.description  
5) Added support for new EventID:2,19 of SourceName Microsoft-Windows-WHEA-Logger.  
6) Added support for new EventID:20 of SourceName Microsoft-Windows-Kernel-General.  
7) Added support for new EventID:22 of SourceName Microsoft-Windows-UserModePowerService.  
8) Added support for new EventID:1000,1001 of SourceName Microsoft-Windows-LoadPerf.  
9) Added support for new EventID:132, 142 of SourceName Microsoft-Windows-WinRM.  
10) Added support for new EventID:4100 of SourceName Microsoft-Windows-PowerShell.  
11) Added support for new EventID:24, 130 of SourceName Microsoft-Windows-Time-Service.  
12) Added support for new EventID:10317 of SourceName Microsoft-Windows-NDIS.  
13) Added support for new EventID:14205 of SourceName Microsoft-Windows-WMPNSS-Service  
14) Added support for new EventID:16963, 16966 of SourceName Microsoft-Windows-Directory-Services-SAM.  
11) Added support for new EventID:14, 15, 24 of SourceName TPM.  
12) Added support for new EventID:4, 59, 61, 16385, 16392 of SourceName Microsoft-Windows-Bits-Client.  
13) Removed Generic_Event usage from WINEVTLOG parser  
14) Added mapping of Message field for EventID 104.   
2022-07-04 |  1) Added FR language support for EventID 1102.   
2022-06-17 |  1) Added support of new EventID:145 of SourceName Microsoft-Windows-WinRM.  
2) Added mapping of Category GUIDs for EventID 4719.  
3) Mapped AccountName and Domain by splitting Data_1 field for EventID 8222.   
2022-06-07 |  1) Added support of new eventID:77 of Provider name: Microsoft-Windows-CertificationAuthority.  
2) Added gsub and modified the grok pattern to avoid incorrect mapping of key `MemberName` mapped to UDM field `target.user.user_display_name`.   
2022-05-24 |  1) Action set to ALLOW for error code equal to 0x0 for EventID 4776.  
2) Added mapping for AuthenticationPackageName for EventID 4624, 4625.  
3) Added support for EventID 400 for provider name PowerShell .  
4) Added mapping for ScriptBlockID in EventID 4104.  
5) Updated mapping of DeviceName for EventID 98, 140 from principal.hostname to target.resource_name.  
6) Added support for EventID 3, 60, 100, 187, 1096, 1127, 8000, 8003, 8004, 8006, 8007, 8021, 8024, 10000, 10004, 10111, 14204.  
7) Added security_result.severity for EventID 10110.  
8) Added ServiceFileName mapping for EventID 7045.  
9) Mapped Computer field with intermediary.hostname.  
10) Mappedd UserAccountControl for EventID 4738.  
11) Added mapping for TargetOutboundUserName in EventID 4624.   
2022-05-10 |  1) Enhanced WINEVTLOG parser by adding support of WINDOWS 11 and WINDOWS SERVER 2022 events.  
2) Added support of new events: 1202, 102, 11, 10, 18, 1000, 1027, 1025, 10110, 1026, 1282, 1130, 10118, 1, 4000, 4101, 4001, 400.  
3) For 5137 & 5141, mapped SubjectLogonId with principal.labels.key/value.  
4) Mapped Computer field with intermediary.hostname.  
5) For 4719, mapped the value of AuditPolicyChanges with about.labels.key/value.  
6) For 5141, mapped ObjectClass field with target.labels.key/value.  
7) Action set to ALLOW for error codes equal to 0x0.  
8) Added mapping of TargetOutboundUserName in EventID 4624.  
9) Added raw value of AccessList in target.resource.attribute.permissions.name.  
10) For 4698, 4699 and 4702, mapped task_command with principal.process.file.full_path and task_arguments with principal.process.command_line.   
2022-04-27 |  Promoted parser from test to new global default.   
2022-04-22 |  1) Added EventID 1202 (Provider name: SceCli) and Event ID 102 (Provider Name: Microsoft-Windows-TaskScheduler).   
2022-04-21 |  1) For every event mapped Message field for Microsoft-Windows-Security-Auditing.  
2) For EventID 5137 mapped ObjectClass, ObjectDN.  
3) For EventID 5136 mapped AttributeValue.  
4) For EventID 4769 mapped TicketOptions, TicketEncryptionType.  
5) For EventID 4662 mapped ObjectType  
6) For EventID 4625 mapped FailureReason  
7) For EventID 4742 mapped SubjectLogonId  
8) Mapped Computer as intermediary.hostname.   
2022-03-30 |  1) Added mapping of `Channel` field for all the Event IDs.  
2) For EventID `5861` and SourceName `Microsoft-Windows-WMI-Activity`, changed mapping of `Channel` field from `security_result.summary` to `about.labels.key/value`.  
3) Added mapping of Task field for Event ID 4702.  
4) Extracted Event Description from Message field for Event ID 4767.  
5) Added gsub to handle `·` present in Message field for Event ID 4719.  
6) Added mapping of DSName and DSType field for Event ID 5137 & 5141.  
7) Added mapping of ObjectClass field for Event ID 5141.  
8) Added mapping of OriginalVolume(Data_9), ShadowDeviceName(Data_8) and ProcessName(Data_3) field for Event ID 8222.  
9) Added mapping of OriginalVolume(Data_8) and ShadowDeviceName(Data_7) field for Event ID 8223.   
2022-03-29 |  1) Added mapping of TargetLogonId field for Event ID 4624.  
2) Added mapping of ServiceSid field for Event ID 4769.  
3) Added mapping of NewObjectDN and OldObjectDN fields for Event ID 5139.  
4) Added mapping of DnsHostName field for Event ID 4741.  
5) Added mapping for SubjectLogonId field.  
6 )Mapped actual hostname from FQDN name in Event ID 4768.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
