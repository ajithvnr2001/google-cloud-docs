---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/winevtlog-xml-changelog/
title: Change log for WINEVTLOG_XML \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:10:53.285662+00:00
---

# Change log for WINEVTLOG_XML  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/winevtlog-xml-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WINEVTLOG_XML

Date | Changes  
---|---  
2026-09-04 |  Enhancement:  
\- Added a grok pattern to parse the new pattern of XML raw logs.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `ObjectName` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `Computer` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `ProcessID` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Level`, `Opcode`, `EventIDCode` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `TaskSource`, `TaskAuthor` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2026-08-12 |  Enhancement:  
\- Updated mapping of `TimeGenerated` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field globally.  
\- Added a conditional check before already existing mapping of `OriginatingComputer` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `Opcode` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field when EventID is 5379.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Level` raw log field with `event.idm.read_only_udm.additional.fields` UDM field when EventID is 5379.   
2026-08-11 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `event_data_message` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `HostApplication` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `_TimeReceived` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `details_part`, `xmlns_url`, `type`, `NewEngineState`, `PreviousEngineState`, `SeqNum`, `ClientIpScopeId`, `ParameterXml`, `EventLevel`, `EventLog`, `MG`, `_IsBillable`, `_BilledSize`, `_Internal_WorkspaceResourceId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `EventID` is `403`, and user data is present updated to `USER_RESOURCE_ACCESS`, else `GENERIC_EVENT`.   
2026-07-01 |  Enhancement:  
\- Added a grok pattern to parse `message` raw log field to extract `sys_pri`, `time_stamp` and `host_name` raw log fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `sys_pri` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `time_stamp` raw log field to `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `host_name` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated `event.idm.read_only_udm.metadata.event_type` from `GENERIC_EVENT` to `STATUS_UPDATE` when principal device data is present.   
2026-06-09 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `User` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `Host Name` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `Host ID` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `Severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `HostVersion`, `EngineVersion`, `RunspaceID`, `PipelineID`, `CommandType`, `ShellID`, `UserData`, `CommandPath`, `ConnectedUser`, `command`, `type_definition_code`, `language`, `ignore_warnings`, raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added and modified the extraction of `ContextInfo` from XML path `/Event/EventData/Data[@Name=`ContextInfo`]`.  
\- Added extraction of `Payload` from XML path `/Event/EventData/Data[@Name=`Payload`]`.  
\- Added extraction of `UserData` from XML path `/Event/EventData/Data[@Name=`UserData`]`.  
\- Added a grok pattern on Payload to extract `command`, `type_definition_code`, `language`, `ignore_warnings`.   
2026-06-05 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `LogonGuid`, `KeyLength`, `ProcessId`, `VirtualAccount`, `TargetLinkedLogonId`, `ElevatedToken`, `ImpersonationLevel`, `Correlation`, `Task`, `Level`, raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `TargetOutboundUserName`, `TargetOutboundDomainName`, `TransmittedServices` raw log field with `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels`: Newly mapped `Provider` raw log field with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.about.resource.attribute.labels`: Newly mapped `RestrictedAdminMode` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels` UDM field.   
2026-04-23 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `AuthenticationPackageName`, `Status`, `agent_eventid` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `column4` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `Logon Account` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `prod_event_type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: If `Severity` is `Success Audit`, updated the value of `event.idm.read_only_udm.security_result.severity` to `INFORMATIONAL`.  
\- Added a Grok pattern on the `message` field to correctly parse the raw log fields.   
2026-03-18 |  Enhancement:  
\- Added a grok pattern on client_ip1 to extract the IP address.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `EventSourceName`, `EventIDQualifiers`, `ipv6_zone_index` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-03-11 |  Enhancement:  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `FQDN` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `FQDN` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.auth_details`: Newly mapped `ServiceSid` raw log field with `event.idm.read_only_udm.extensions.auth.auth_details` UDM field.  
\- `event.idm.read_only_udm.target.resource.id`: Newly mapped `details.Object.Handle ID` raw log field with `event.idm.read_only_udm.target.resource.id` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `details.New Logon.Logon ID` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `details.Account Information.Account Domain` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `details.Operation.Accesses` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `ElevatedToken`, `elevated_token` raw log fields with `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `ReadOperation`, `details_Subject_Read_Operation` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `TargetName`, `AccessList`, `ClientProcessStartKey`, `RpcCallClientLocality`, `ServiceName`, `CountOfCredentialsReturned`, `PrivilegeList`, `TargetLinkedLogonId`, `TaskName`,`TaskContentNew`, `details_Logon_Process_Name`, `details_Object_Object_Type`, `details_Object_Object_Server`, `details_Access_Mask`, `details_Object_Object_Name`, `details_Service_Information_Available_Keys`, details_Service_Information_MSDS_SupportedEncryptionTypes raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ProcessCreationTime`, `AdditionalInfo2`, `ObjectName`, `details_Additional_Information_Parameter_2`, `VirtualAccount`, `Type`, `ReturnCode`, `ImpersonationLevel`, `TargetLogonId`, `TicketOptions`, `TicketEncryptionType`, `SessionKeyEncryptionType`, `Status`, `RequestTicketHash`, `ResponseTicketHash`, `ServiceSupportedEncryptionTypes`, `ServiceAvailableKeys`, `DCSupportedEncryptionTypes`, `DCAvailableKeys`, `ClientAdvertizedEncryptionTypes`, `details.Privileges`, `details_New_Logon_Security_ID`, `details_Additional_Information_Parameter_1`, `details_New_Logon_Account_Name`, `details_New_Logon_Linked_Logon_ID`, `impersonation_level`, `correlation_activity_id`, `details_Account_Information_Account_Name`, `details_Account_Information_Logon_GUID`, `details_Operation_Operation_Type`, `details_additional_information_failure_code`, `details_Additional_Information_Ticket_Options`, `details_Additional_Information_Ticket_Encryption_Type`, `details_Additional_Information_Session_Encryption_Type`, `details_Domain_Controller_Information_Available_Keys`, `details_Domain_Controller_Information_MSDS_SupportedEncryptionTypes`, `details_Service_Information_Service_ID`, `network_information_client_port`, `details.Network_Information.Advertized_Etypes`, `response_ticket_hash` `request_ticket_hash`, `details_Subject_Logon_ID` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.administrative_domain`: Added a conditional check before already existing mapping of `details.Subject.Account Domain` raw log field with event.idm.read_only_udm.target.administrative_domain UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Added a conditional check before already existing mapping of `details.Subject.Account Name` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.windows_sid`: Added a conditional check before already existing mapping of `details.Subject.Security ID` raw log field with `event.idm.read_only_udm.target.user.windows_sid` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Added a conditional check before mapping `TaskName`, `CallerProcessName`, `details_Process_Information_Creator_Process_Name` and `details_Process_Information_Process_Name` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `network_information_client_address` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `network_information_client_address` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `ClientProcessId` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `ParentProcessId` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `details_Service_Information_Service_Name` raw log field with `event.idm.read_only_udm.target.application` UDM field.   
2026-03-03 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_name`: Updated the mapping for `event.idm.read_only_udm.metadata.product_name` to be conditionally set from various raw fields, overriding the previous static value of `Windows`, to dynamically and more accurately populate the product name based on available data in the logs.  
\- `event.idm.read_only_udm.metadata.product_name`: Mapped `SourceName` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Mapped `Source` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field if `SourceName` is empty.  
\- `event.idm.read_only_udm.metadata.product_name`: Mapped `provider.name` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field if `SourceName` and `Source` are empty.  
\- `event.idm.read_only_udm.metadata.product_name`: Mapped `prod_name` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field if `SourceName`, `Source`, and `provider.name` are empty.  
\- `event.idm.read_only_udm.metadata.product_name`: Mapped `EventSourceName` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field if `SourceName`, `Source`, `provider.name`, and `prod_name` are empty.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `NewProcessId` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.   
2026-02-26 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `details.Network Information.Source Network Address` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `details.Network Information.Source Network Address` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Newly mapped `details.Account For Which Logon Failed.Security ID` raw log field with `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `details.Detailed Authentication Information.Logon Process` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `details.Failure Information.Failure Reason` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `event_id.qualifiers`, `TargetUserSid`, `WorkstationName`, `LogonType`, `AuthenticationPackageName`, `KeyLength`, `LogonProcessName`, `details.Network Information.Source Port`, `details.Account For Which Logon Failed.Account Name` and `Msg_1` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `details.Account For Which Logon Failed.Account Domain` raw log field with `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `version`, `details.Detailed Authentication Information.Key Length`, `keywords`, `details.Detailed Authentication Information.Authentication Package`, `details.Failure Information.Status`, `details.Failure Information.Sub Status`, `details.Process Information.Caller Process ID`, `details.Subject.Security ID` and `details.Network Information.Workstation Name` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` and `has_user` is true, set to USER_LOGIN.  
\- `event.idm.read_only_udm.extensions.auth.type`: Newly mapped to `AUTHTYPE_UNSPECIFIED` for USER_LOGIN event type.  
\- Added conditional check to prevent mapping null value and `-` , this is allowing the following UDM fields to be mapped properly:  
\- `event.idm.read_only_udm.principal.administrative_domain`  
\- `event.idm.read_only_udm.principal.user.userid`  
\- `event.idm.read_only_udm.target.process.file.full_path`  
2026-02-23 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `SamAccountName`, `UserPrincipalName`, `HomeDirectory`, `HomePath`, `ScriptPath`, `ProfilePath`, `UserWorkstations`, `PasswordLastSet`, `AccountExpires`, `PrimaryGroupId`, `AllowedToDelegateTo`, `OldUacValue`, `NewUacValue`, `UserAccountControl`, `UserParameters`, `LogonHours`, `ServicePrincipalNames` raw log field(s) with `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `DisplayName` raw log field(s) with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `UserPrincipalName` raw log field(s) with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `DnsHostName` raw log field(s) with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `DnsHostName` raw log field(s) with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `EventReceivedTime` raw log field(s) with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `SourceModuleName` raw log field(s) with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `Opcode`,`ComputerAccountChange` raw log field(s) with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `ProcessID` raw log field(s) with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ThreadID`,`SeverityValue`,`Category` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `PrivilegeList` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `SourceName` raw log field with `event.idm.read_only_udm.principal.application` UDM field.   
2026-02-12 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `Hostname` log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field for EventID 4627.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `EventIdx` and `EventCountTotal` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-02-04 |  Enhancement:  
\- Added grok patterns to parse `ProcessName` value correctly.  
\- Added grok pattern to parse `SourceIPAddress` value correctly.  
\- event.idm.read_only_udm.metadata.event_type: Setting `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` when `has_target_details` is `true`.  
\- Created a new include file `winevtlog_xml.include`.   
2026-01-30 |  Enhancement:  
\- Added support for JSON array format where each object in the `logEvents` array contains the Event XML message.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `record.owner` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.security_result.about.resource.name: Newly mapped `record.logGroup` raw log field with `event.idm.read_only_udm.security_result.about.resource.name` UDM field.  
\- event.idm.read_only_udm.security_result.about.resource.attribute.labels: Newly mapped `record.logStream`, `Provider` raw log fields with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `record.messageType` (as key `Message_type`), `OldSd` (as key `Original Security Descriptor`), and `NewSd` (as key `New Security Descriptor`) raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `logEvent.id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Address` (as key `Address`), `AddressLength` (as key `Address Length`), `Keyword` (as key `Keyword`), `BinaryId` (as key `BinaryId`), `EventIDQualifiers` (as key `Event ID Qualifiers`), `Opcode` (as key `event_system_opcode`), `param1` (as key `param1`), and `param2` (as key `param2`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.resource.resource_subtype: Newly mapped `PrivilegeList` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `Version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Channel_type` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-01-01 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `TimeGenerated` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `SystemProcessId` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `EventRecordId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped `SourceComputerId` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- event.idm.read_only_udm.principal.group.group_display_name: Newly mapped `ManagementGroupName` raw log field with `event.idm.read_only_udm.principal.group.group_display_name` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `SystemThreadId` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Type`, `EventLevelName`, `TenantId`, `LogonTypeName`, `Activity`, `MG`, `_SubscriptionId`, `_ItemId`, `_IsBillable`, `_BilledSize`, `_Internal_WorkspaceResourceId` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `TimeCollected` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `SystemUserId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.resource.product_object_id: Newly mapped `_ResourceId` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `EventSourceName` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.target.process.product_specific_process_id: Newly mapped `EventOriginId` raw log field with `event.idm.read_only_udm.target.process.product_specific_process_id` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `SourceSystem` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-12-19 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `OldTargetUserName`, `NewTargetUserName` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `NewTargetUserName` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `EventSourceName` raw log field for EventID 4781 with `event.idm.read_only_udm.target.application` UDM field.  
\- Added a new condition for setting `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when `has_resource` == `false` and `has_target_user` == `true`.  
\- Modified the condition for setting `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_UPDATE_CONTENT`.  
\- Removed initialization of `NewTargetUserName` field from `libs/winevtlog.include`.   
2025-12-01 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `SAM Account Name`, `Display Name`, `User Workstations`, `Account Expires`, `Primary Group ID`, `DNS Host Name` raw log field(s) with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `User Principal Name`, `Service Principal Names` raw log field(s) with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Home Directory`, `Home Drive`, `Script Path`, `Profile Path`, `AllowedToDelegateTo`, `Old UAC Value`, `New UAC Value`, `User Account Control`, `User Parameters`, `SID History`, `Logon Hours`, `additional_information`, `Description_data` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added grok pattern to support new format of log.   
2025-11-29 |  Enhancement:  
\- `event1.idm.read_only_udm.metadata.product_version`: Newly mapped `Version` raw log field with `event1.idm.read_only_udm.metadata.product_version` UDM field.  
\- Added a conversion for `LogonType` to string to avoid parsing issues.   
2025-11-28 |  Enhancement:  
\- event1.idm.read_only_udm.metadata.event_timestamp: Newly mapped `event_Time` field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- Modified the grok pattern to parse `time` field correctly.  
\- event1.idm.read_only_udm.principal.user.userid: Newly mapped `UserName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field when EventID is 7040.  
\- event1.idm.read_only_udm.target.application: Newly mapped `param1` raw log field with `event.idm.read_only_udm.target.application` UDM field when EventID is 7040.  
\- event1.idm.read_only_udm.additional.fields: Newly mapped `param2`, `param3` and `param4` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field when EventID is 7040.  
\- event1.idm.read_only_udm.additional.fields: Newly mapped `Type`, `sourceHealthServiceId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-10-28 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: If EventID is 4799, updated to `GROUP_UNCATEGORIZED`.  
\- `event.idm.read_only_udm.metadata.event_type`: If EventID is 4780, updated to `USER_CHANGE_PERMISSIONS`.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `/Event[%{index}]/TaskName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.   
2025-10-07 |  Enhancement:  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `computer` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `computer` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Removed mapping of `computer` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.principal.user.windows_sid: Newly mapped `SubjectUserSid` raw log field with `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `IpAddress` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `IpAddress` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `IpPort` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.principal.resource.product_object_id: Newly mapped `LogonGuid` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.process.pid: Newly mapped `ProcessId` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- event.idm.read_only_udm.target.process.file.full_path: Newly mapped `ProcessName` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.principal.administrative_domain: Newly mapped `SubjectDomainName` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `SubjectUserName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.labels: Newly mapped `SubjectLogonId` raw log field with `event.idm.read_only_udm.principal.labels` UDM field.  
\- event.idm.read_only_udm.target.administrative_domain: Newly mapped `TargetDomainName` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `TargetUserName` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `TargetServerName` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `TargetLogonGuid` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.labels: Newly mapped `TargetInfo` raw log field with `event.idm.read_only_udm.target.labels` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `execution.process_id` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `provider.guid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `system_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `execution.thread_id`, `provider.name`, `record_id`, `task`, `opcode` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Setting `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` if `has_principal` is true.   
2025-09-04 |  Enhancement:  
\- Modified grok patterns to handle tab characters in the `Message` field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `Version` raw log field to event.idm.read_only_udm.metadata.product_version.  
\- event.idm.read_only_udm.target.process.pid: Newly mapped `Engine_PID` raw log field to event.idm.read_only_udm.target.process.pid.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Level` and `Result_Code` raw log fields to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Op_code` and `Channel_type` raw log fields to event.idm.read_only_udm.security_result.detection_fields.   
2025-08-11 |  Enhancement:  
\- Removed the grok pattern in order to parse `Message` field into summary for the EventIds `3040`,`3041`,`3039`,`2889`.   
2025-08-05 |  Enhancement:  
\- event1.idm.read_only_udm.target.file.full_path: Newly mapped `ServiceFileName` raw log field with `event1.idm.read_only_udm.target.file.full_path` UDM field.  
\- event1.idm.read_only_udm.principal.hostname and event1.idm.read_only_udm.principal.asset.hostname: Newly mapped `Computer` raw log field with `event1.idm.read_only_udm.principal.hostname` and `event1.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event1.idm.read_only_udm.principal.ip and event1.idm.read_only_udm.principal.asset.ip: Newly mapped `OriginatingComputer` raw log field with `event1.idm.read_only_udm.principal.ip` and `event1.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event1.idm.read_only_udm.principal.user.userid: Newly mapped `AccountName` raw log field with `event1.idm.read_only_udm.principal.user.userid` UDM field.  
\- event1.idm.read_only_udm.additional.fields: Newly mapped `ServiceAccount` raw log field with `event1.idm.read_only_udm.additional.fields` UDM field.  
\- event1.idm.read_only_udm.metadata.event_type:  
\- Setting `USER_UNCATEGORIZED` to `event1.idm.read_only_udm.metadata.event_type` UDM field if `has_principal_user` is true.  
\- Setting `STATUS_UPDATE` to `event1.idm.read_only_udm.metadata.event_type` UDM field if `has_principal` is true.  
\- Removed event_type as GENERIC_EVENT when EventID is 4697 and 601.   
2025-08-01 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `client_ip1` raw log field to `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `client_port` raw log field to `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `identity` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `binding_type` raw log field to `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `rendering_task` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Modified grok pattern for the Message field to correctly parse multiline event messages for specific EventIDs.  
\- Refactored the mapping of various raw fields (e.g., username, TargetUserName, ClientUserName) to the event.idm.read_only_udm.target.user.userid UDM field from a rename operation to a replace operation.  
\- Refactored mapping of the OpCorrelationID raw log field to the event.idm.read_only_udm.network.session_id UDM field to be generic across all event IDs.   
2025-07-28 |  Enhancement:  
\- event1.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped Task raw log field to event1.idm.read_only_udm.principal.resource.attribute.labels.  
\- Consolidated all mapping for event1.idm.read_only_udm.additional.fields, event1.idm.read_only_udm.security_result.detection_fields, and event1.idm.read_only_udm.principal.resource.attribute.labels, event1.idm.read_only_udm.target.resource.attribute.labels, event1.idm.read_only_udm.security_result.about.labels into a for loop.  
\- Removed redundant mapping for `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`, `event1.idm.read_only_udm.network.http.response_code`, `event1.idm.read_only_udm.metadata.product_log_id`, `event1.idm.read_only_udm.observer.application`, `event1.idm.read_only_udm.target.administrative_domain`, `event1.idm.read_only_udm.principal.administrative_domain`, `event1.idm.read_only_udm.target.process.pid`, `event1.idm.read_only_udm.principal.process.pid`, `event1.idm.read_only_udm.principal.process.file.full_path`.  
\- Replaced deprecated udm mapping `about.labels` with `about.resource.attribute.labels`.   
2025-07-10 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `BinaryId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ProviderName` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `loggingSourceName` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `Pid` raw log fields with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `Description` raw log fields with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `EventTickCount` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `ProductVersion` raw log fields with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ActivityID` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-07-01 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `ModuleVersion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `AppPath` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.user.windows_sid`: Newly mapped `SubjectUserSid` raw log field with `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- `event1.idm.read_only_udm.principal.resource.name`: Newly mapped `SourceModuleName` raw log field with `event1.idm.read_only_udm.principal.resource.name UDM field`.  
\- `event1.idm.read_only_udm.observer.application`: Newly mapped `SourceModuleType` raw log field with `event1.idm.read_only_udm.observer.application UDM field`.  
\- `event1.idm.read_only_udm.principal.asset_id`: Newly mapped `ProviderGuid` raw log field with `event1.idm.read_only_udm.principal.asset_id UDM field`.  
\- Removed `SourceName` mapping of `event1.idm.read_only_udm.principal.application` UDM field.  
\- If `EventID` is equal to `16962` then mapped `Hostname` to `event1.idm.read_only_udm.principal.hostname` and `event1.idm.read_only_udm.principal.asset.hostname`.  
\- Added Gsub to update `Installation choice` to `Installation_choice`, `Default SD String:` to `Default_SD_String:`, `Host OS Major version` to `Host_OS_Major_version`, `Host OS Minor version` to `Host_OS_Minor_version`, `Host OS Build number` to `Host_OS_Build_number`, `Host OS Service pack major number` to `Host_OS_Service_pack_major_number`, `Host OS Service pack minor number` to `Host_OS_Service_pack_minor_number`.  
\- Added conditional checck for field `Channel`.  
\- Removed redundant code for field `SourceName` from `event1.idm.read_only_udm.principal.application`.   
2025-06-27 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `QXID`, `GUID`, `Flags`, `CacheScope`, `RecursionScope`, `RD`, `Port` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `Source` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip` : Newly mapped `Source` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Removed mapping of `InterfaceIP` raw log field with `event.idm.read_only_udm.principal.ip` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Removed mapping of `InterfaceIP` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.intermediary.ip`: Mapped `InterfaceIP` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- Modified the condition to map `event.idm.read_only_udm.metadata.event_type` UDM field with `NETWORK_DNS` only when `has_principal` is true.   
2025-06-18 |  Enhancement:  
\- Added Grok patterns to parse the unparsed logs.  
\- Added a null check condition before using the csv filter.  
\- Added a null check condition before mapping `SubjectUserName`. If `SubjectUserName` is not empty then map it to `event1.idm.read_only_udm.principal.user.userid` else map `usrName` to `event1.idm.read_only_udm.principal.user.userid`.  
\- Added a null check condition before mapping `SubjectDomainName`.  
\- event1.idm.read_only_udm.additional.fields: Newly mapped `cat` , `SecurityId` , `AccountName` , `LogonId` , `HandleId` , `OperationType` , `NewValueType` , `OldValueType` and `OldValue` raw log field with `event1.idm.read_only_udm.additional.fields` UDM field  
\- event1.idm.read_only_udm.principal.application: Newly mapped `application` raw log field with `event1.idm.read_only_udm.principal.application` UDM field  
\- event1.idm.read_only_udm.metadata.description: Newly mapped `message` raw log field with `event1.idm.read_only_udm.metadata.description` UDM field  
\- event1.idm.read_only_udm.principal.administrative_domain: Newly mapped `AccountDomain` raw log field with `event1.idm.read_only_udm.principal.administrative_domain` UDM field  
\- event1.idm.read_only_udm.principal.process.file.full_path: Newly mapped `ProcessName` raw log field with `event1.idm.read_only_udm.principal.process.file.full_path` UDM field   
2025-06-13 |  Enhancement:  
\- Added a conversion function to convert `OpCode` to string before mapping it to avoid parsing issues.  
\- If `eventId` is `1001` and `loggingSourceName` is present then map `event_type` to `USER_UNCATEGORIZED`.  
\- event1.idm.read_only_udm.principal.process.command_line : Newly mapped raw log field if [i] == `16` when event=1001 with `event1.idm.read_only_udm.principal.process.command_line`.  
\- event1.idm.read_only_udm.principal.file.full_path: Newly mapped raw log field if [i] == `17` when event=1001 with `event1.idm.read_only_udm.principal.file.full_path`.  
\- event1.idm.read_only_udm.principal.user.product_object_id : Newly mapped raw log field if [i] == `20` when event=1001 with `event1.idm.read_only_udm.principal.user.product_object_id`.  
\- event1.idm.read_only_udm.principal.url: Newly mapped `xmlns` raw log field with `event1.idm.read_only_udm.principal.url` UDM field.  
\- event1.idm.read_only_udm.principal.user.userid : Newly mapped `loggingSourceName` raw log field with `event1.idm.read_only_udm.principal.user.userid`.  
\- event1.idm.read_only_udm.principal.application: Newly mapped `SourceName` raw log field with `event1.idm.read_only_udm.principal.application` UDM field.  
\- event1.idm.read_only_udm.principal.asset_id: Newly mapped `ProviderGuid` raw log field with `event1.idm.read_only_udm.principal.asset_id` UDM field.   
2025-06-04 |  Enhancement:  
\- Newly added `CSV` filter to parse logs with CSV data.  
\- Added gsub to parse the required data in the logs.  
\- Added new grok pattern to `powershell_command`, and `Address` raw log fields to parse `scriptblock_id`, `target_path`, and `Address_ip` raw log fields in `winevtlog.include`.  
\- `event.idm.read_only_udm.security_result.about.process.command_line` : Newly mapped `powershell_command` raw log field with `event.idm.read_only_udm.security_result.about.process.command_line` UDM field in `winevtlog.include`.  
\- `event.idm.read_only_udm.security_result.detection_fields` : Newly mapped `scriptblock_id` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field in `winevtlog.include`.  
\- `event1.idm.read_only_udm.principal.ip` : Newly mapped `Address_ip` raw log filed with `event1.idm.read_only_udm.principal.ip` UDM field in `winevtlog.include`.  
\- `event1.idm.read_only_udm.principal.asset.ip` : Newly mapped `Address_ip` raw log filed with `event1.idm.read_only_udm.principal.asset.ip` UDM field in `winevtlog.include`.   
2025-05-27 |  Enhancement:  
\- Modified the condition to parse new type of logs.  
\- Added null check condition for `TargetUserName` raw log field.   
2025-05-21 |  Enhancement:  
\- event.idm.read_only_udm.target.ip: Newly mapped `Destination` raw log field with `event1.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `Destination` raw log field with `event1.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.network.dns.questions.name: Newly mapped `qname` raw log field with `event1.idm.read_only_udm.network.dns.questions.name` UDM field.  
\- event.idm.read_only_udm.network.dns.questions.type: Newly mapped `qtype` raw log field with `event1.idm.read_only_udm.network.dns.questions.type` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `InterfaceIP` raw log field with `event1.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `InterfaceIP` raw log field with `event1.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Flags`,`zone`,`xid`,`dnssec`,`PacketData`,`BufferSize`,`rcode`,`AA`,`TCP`,`ElapsedTime`,`AD` and `AdditionalInfo` raw log fields with `event1.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `port` raw log field with `event1.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.network.dns.response_code: Newly mapped `rcode` raw log field with `event1.idm.read_only_udm.network.dns.response_code` UDM field.  
\- Added support for new format of XML logs.   
2025-04-27 |  Enhancement:  
\- `event.idm.read_only_udm.principal.asset_id`: Removed mapping of `memSid` from `event.idm.read_only_udm.principal.asset_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `memSid` raw field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added a Gsub to remove ` & ` from the XML log.   
2025-04-18 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Keyword` raw log field with `event.idm.read_only_udm.additional.fields` UDM field with key as `Keyword`.   
2025-04-16 |  Enhancement:  
\- Added new grok pattern to parse `event1.idm.read_only_udm.metadata.description` UDM field from `Message` raw log field.   
2025-04-11 |  Enhancement:  
\- Added a new grok pattern to parse the SYSLOG + JSON logs.  
\- Newly mapped `ACCOUNT_NAME`raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Newly mapped `SECURITY_ID` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-03-25 |  Enhancement:  
\- Added a gsub to parse the UDM fields correctly.   
2025-03-19 |  Enhancement:  
\- Mapped `ingestion_source` to `metadata.ingestion_labels`.  
\- Mapped `details.Creator Subject.Account Domain` to `principal.administrative_domain`.  
\- Mapped `details.Creator Subject.Logon ID` to `additional.fields`.  
\- Mapped `details.Creator Subject.Account Name` to `principal.user.userid`.  
\- Mapped `details.Creator Subject.Security ID` to `principal.user.windows_sid`.  
\- Mapped `details.Process Information.Creator Process ID` to `principal.process.pid`.  
\- Mapped `details.Process Information.Creator Process Name` to `principal.process.file.full_path`.  
\- Mapped `details.Process Information.Mandatory Label` to `target.labels`.  
\- Mapped `details.Process Information.New Process ID` to `target.process.pid`.  
\- Mapped `details.Process Information.New Process Name` to `target.process.file.full_path`.  
\- Mapped `details.Process Information.Process Command Line` to `target.process.command_line`.  
\- Mapped `details.Process Information.Token Elevation Type` to `security_result.detection_fields`.  
\- Mapped `details.Target Subject.Account Domain` to `target.administrative_domain`.  
\- Mapped `details.Target Subject.Account Name` to `target.user.userid`.  
\- Mapped `details.Target Subject.Logon ID` to `target.user.windows_sid`.  
\- Mapped `details.Target Subject.Security ID` to `target.user.windows_sid`.  
\- Mapped `details.Process Information.Process ID` to `principal.process.pid`.  
\- Mapped `details.Process Information.Process Name` to `principal.process.file.full_path`.  
\- Mapped `details.Subject.Account Domain` to `principal.administrative_domain`.  
\- Mapped `details.Subject.Account Name` to `principal.user.userid`.  
\- Mapped `details.Subject.Logon ID` to `additional.fields`.  
\- Mapped `details.Subject.Security ID` to `principal.user.windows_sid`.  
\- Mapped `details.Transaction Information.New State` to `sec_result.detection_fields`.  
\- Mapped `details.Transaction Information.RM Transaction ID` to `network.session_id`.  
\- Mapped `details.Transaction Information.Resource Manager` to `target.resource.name`.  
\- Mapped `details.Additional_Context` to `security_result.detection_fields`.  
\- Modified the drop condition to include a check for `task1` being empty.  
\- Added a conditional check before the drop condition.  
\- Mapped `event_id.id` to `security_result.rule_name`.  
\- Mapped `computer` to `intermediary.hostname`.  
\- Mapped `channel` to `security_result.summary`.   
2025-03-06 |  Enhancement:  
\- Added a Grok pattern to map `AccountName` to `principal.user.userid` and `TargetUserName` to `target.user.userid`.  
\- Added a support to parse the unparsed logs.   
2025-03-03 |  Enhancement:  
\- Mapped `Library` to `target.file.full_path`.   
2025-02-27 |  Enhancement:  
\- Added support for new pattern of KV and syslog logs.   
2025-02-20 |  Enhancement:  
\- Added a Grok pattern to parse unpasred logs.  
\- For Event ID 4724, the `prin_user` is parsed to `principal.user.userid` and the `tar_user` to `target.user.userid`.  
\- For Event ID 4740, changed the mapping of `principal.user.userid` to `target.user.userid.`  
\- For Event ID 4634, changed the mapping for principal.user.userid from `logonid` to `account name`.   
2025-02-07 |  Enhancement:  
\- Modified conditional check for `memSid`.   
2025-02-03 |  Enhancement:  
\- Added support for the new pattern of `5136` logs.  
\- Mapped `ServiceName` to `target.application`.  
\- Mapped `ServiceFileName` to `target.process.file.full_path`.  
\- Mapped `ServiceType`, `ServiceStartType` to `security_result.detection_fields`.  
\- Mapped `ServiceAccount` to `target.user.userid`.  
\- Mapped Task to `principal.resource.attribute.labels`.   
2025-01-16 |  Enhancement:  
\- Added `gsub` for `ParentProcessName` and `CreatorProcessName` to restore `C~` to `C:`.   
2025-01-15 |  Enhancement:  
\- Mapped `IpAddress1` to `principal.ip` and `principal.asset.ip`.   
2024-12-30 |  Enhancement:  
\- Replaced backslashes (`\\`) with forward slashes (`/`) using the `gsub` function.   
2024-11-27 |  Enhancement:  
\- Added support to parse unparsed logs.   
2024-11-04 |  Enhancement:  
\- Added a new Grok pattern to parse the data that was not parsed earlier.  
\- Added support to parse failed logs.  
\- Mapped `hostname_prin` to `principal.hostname`.  
\- Mapped `ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `Account Name` to `target.yser.userid` and `principal.user.userid`.   
2024-10-27 |  Enhancement:  
\- Added support for new pattern of SYSLOG logs.   
2024-10-18 |  Enhancement:  
\- Mapped `AttributeSyntaxOID` and `OperationType` to `additional.fields`.  
\- Modified the XML pattern to parse `OpCorrelationID` and `ObjectGUID`.   
2024-10-10 |  Enhancement:  
\- Added support for a new pattern of syslog logs.  
\- Changed EventId mapping from `column4` to `column6`.   
2024-10-04 |  Enhancement:  
\- Added support for new pattern of SYSLOG logs.   
2024-10-01 |  Enhancement:  
\- Modified the XML pattern to parse `LogonProcessName`.   
2024-09-24 |  Enhancement:  
\- Added new Grok patterns to parse `task_command` and `task_arguments` fields.   
2024-09-03 |  Enhancement:  
\- Mapped `DomainPolicyChanged` to `security_result.detection_fields`.   
2024-08-30 |  Enhancement:  
\- Added support to handle unparsed SYSLOG + KV logs.  
\- Modified mappong for `AttributeLDAPDisplayName` from `target.resource.type` to `target.resource.resource_subtype`.  
\- Handled logs having `EventId` as 4826.  
\- Mapped `MemberSid` to `principal.resource.attribute.labels`.   
2024-08-27 |  Enhancement:  
\- Modified FILE/USER/NETWORK/STATUS uncategorized events to appropriate event types.   
2024-08-21 |  Enhancement:  
\- Added support to parse syslog and CSV logs.   
2024-08-16 |  Enhancement:  
\- Mapped `source` to `about.process.command_line`.   
2024-08-13 |  Enhancement:  
\- Added support for new format of syslog and JSON logs.   
2024-08-08 |  Enhancement:  
\- Mapped `task_command` to `principal.process.file.full_path` and `task_arguments` to `principal.process.command_line` for EventIDs `4698`, `4699`, `4700`, `4701`, and `4702`.   
2024-08-06 |  Enhancement:  
\- Added support to parse logs with EventIDs 1149, 21, and 4611.  
\- Added support to map `CallerProcessName` to `target.file.full_path` for logs with EventId 4799.  
\- Mapped `Param1` to `target.user.userid`.  
\- Mapped `Param2` to `principal.administrative_domain`.  
\- Mapped `Param3` to `principal.ip`.  
\- Added a grok pattern to parse UserData from field `Message`.   
2024-07-26 |  Enhancement:  
\- Added support to parse dropped logs.  
\- Mapped `SubjectUserName` and `SubjectUserSid` to `additional.fields`.   
2024-07-08 |  Enhancement:  
\- Mapped `Hostname` to `additional.fields` with `src` as the key.  
\- Added support to parse logs for EventID 5157.  
\- Mapped `UserRight`, and `AuditSourceName` to `security_result.detection_fields`.  
\- Added support for McAfee logs.   
2024-06-24 |  Enhancement:  
\- Added support to parse dropped logs.  
\- Mapped `PackageName` to `security_result.detection_fields`.   
2024-06-10 |  Bug-Fix, Enhancement:  
\- Added `gsub` for `NewProcessName` to restore `C~` to `C:`.  
\- Added `gsub` for `Task Name` and `Auditing Settings` to parse them properly.  
\- Added a Grok pattern for `Logon Type` for EventID 4634.  
\- Mapped `AgentLogFile` to `additional.fields`.   
2024-05-20 |  Enhancement, Bug-Fix:  
\- Added support to parse logs for EventIDs 5807, 5723, 5721, 5840, 5802.  
\- Changed mapping of `TargetUserName` from `additional.fields` to `target.user.userid`.  
\- Mapped `SubjectAccountName` to `principal.user.userid` and `TargetAccountName` to `target.user.userid` for EventIDs 4648, 4624, and 4720.  
\- Mapped `ProcessName` to `target.process.file.full_path` for EventID 1.  
\- Mapped `TargetServerName` to `additional.fields`.  
\- Added `gsub` for `Source Workstation` and `Error Code` fields to avoid `Error` getting mapped to `principal.hostname`.   
2024-05-14 |  Enhancement:  
\- Added support to parse logs for EventID 4739.   
2024-05-06 |  Enhancement:  
\- Mapped `Privileges` to `security_result.detection_fields`.   
2024-04-23 |  Enhancement:  
\- Added support to map `Logon Type` for logs with EventIds 4624.  
\- Mapped `Logon Type` to `additional.fields`.   
2024-04-16 |  Enhancement:  
\- Mapped `IpAddress1` to `principal.ip` when `EventID` is 4625.  
\- Mapped `AccessRight` to `additional.fields` as per its corresponding values.   
2024-03-25 |  Enhancement:  
\- Added additional mapping of fields for logs with EventIds 4648, 4771.   
2024-03-15 |  Enhancement:  
\- Changed mapping of `principal.user.user_display_name` to `target.user.user_display_name` for `EventIDs` 4732,4733,4728,4729,4756,4757,4746,4747,4751,4752,4761,4762 logs.  
\- When `EventID` is 5140, then mapped `ShareName` to `target.file.names`.  
\- When `EventID` is 4624, then mapped `LmPackageName` to `target.labels`.   
2024-02-20 |  Enhancement:  
\- Added support for new pattern of XML logs embedded in JSON fields.  
\- Added support for `EventIDs` 4947 and 8222.  
\- When `EventID` is 4985, then mapped `SubjectDomainName` to `principal.administrative_domain`.   
2024-02-13 |  Enhancement:  
\- Added a block for `EventId` `1309` to parse unparsed logs.  
\- Replaced redundant code with common code.  
\- Mapped `Hostname` to `principal.asset.hostname`.  
\- Mapped `WorkstationName`, `TargetAccountDomain`, `SourceAddress`, `DSName`, `database_name`, and `target_hostname` to `target.asset.hostname`.   
2024-01-25 |  Enhancement:  
\- Mapped `Properties` to `target.resource.attribute.labels`.   
2024-01-05 |  Enhancement:  
\- Mapped `TargetLogonId`, `AccessMask`, `CertIssuerName`, `TicketOptions`, `TargetUserName`, `AttributeLDAPDisplayName`, `AttributeValues`, `ObjectDN` to `additional.fields`.   
2023-12-29 |  Enhancement:  
\- Added support for `EventIDs` 0, 208, 219, 233, 1000, 1026, 1315, 10000, 10001, 10002, 10003, 10114, 16969, 17573, 18453, 18454, 36867, 49930 logs.  
\- Added a null check for `registry_key` before setting the `metadata.event_type` to `REGISTRY_MODIFICATION` for `EventID` 13.  
\- Added a null check for `registry_key` before setting the `metadata.event_type` to `REGISTRY_CREATION` for `EventID` 12.  
\- When `target.registry` is empty and `Hostname` is present, then set `metadata.event_type` to `STATUS_UPDATE` for `EventIDs` 12, 13.  
\- Added a regular expression pattern as conditional check for `UserID` to match `windows_sid` pattern for `EventIDs` 7040, 7045.  
\- When `UserID` does not match `windows_sid`, then mapped `UserID` to `principal.user.userid` for `EventID` 4070.  
\- When `UserID` does not match `windows_sid`, then mapped `UserID` to `target.user.userid` for `EventID` 4075\.   
2023-11-20 |  Enhancement:  
\- Added a regular expression pattern as conditional check for `TargetUserSid` to match `windows_sid` pattern.  
\- Added a regular expression pattern as conditional check for `TargetSid` to match `windows_sid` pattern.  
\- Added a regular expression pattern as conditional check for `SubjectUserSid` to match `windows_sid` pattern.  
\- Set `event1.idm.read_only_udm.metadata.event_type` from `STATUS_UPDATE` to `USER_RESOURCE_ACCESS` when `Event.System.EventID` value is `4797`.  
\- Mapped `Event.System.Provider@Name` to `event1.principal.application` when `Event.System.EventID` value is `4797`.  
\- Mapped `Event.System.Correlation@ActivityID` to `event1.security_result.detection_fields` when `Event.System.EventID` value is `4797`.  
\- Mapped `Event.System.Execution@ProcessID` to `event1.principal.process.pid` when `Event.System.EventID` value is `4797`.  
\- Mapped `Event.EventData.Data@SubjectUserName` to `event1.idm.read_only_udm.principal.user.userid` when `Event.System.EventID` value is `4797`.  
\- Mapped `Event.EventData.Data@SubjectDomainName` to `event1.idm.read_only_udm.principal.administrative_domain` when `Event.System.EventID` value is `4797`.  
\- Mapped `Event.EventData.Data@Workstation` to `event1.idm.read_only_udm.target.hostname` when `Event.System.EventID` value is `4797`.  
\- Mapped `Event.EventData.Data@TargetUserName` to `event1.idm.read_only_udm.target.user.userid` when `Event.System.EventID` value is `4797`.  
\- Mapped `Event.EventData.Data@TargetDomainName` to `event1.idm.read_only_udm.target.administrative_domain` when `Event.System.EventID` value is `4797`.   
2023-11-10 |  Enhancement:  
\- Added support for EventIDs 4098, 14554 logs.  
\- Mapped `Keywords` to `additional.fields`.  
\- Mapped `AttributeLDAPDisplayName` to `target.resource.attribute.labels` for EventId 5136.   
2023-11-02 |  Enhancement:  
\- For logs with EventId 4624:  
\- Added a new Grok pattern to parse log with EventId 4624.  
\- Mapped `PrincipalDomain` to `principal.administrative_domain`.  
\- Mapped `PrincipalAccountName` to `principal.user.userid`.  
\- Mapped `TargetAccountName` to `target.user.userid`.  
\- Mapped `TargetDomain` to `target.administrative_domain`.  
\- Mapped `Logon GUID` to `principal.resource.id`.  
\- Mapped `ProcessID` to `target.process.pid`.  
\- Mapped `SourceAddress` to `principal.ip`.  
\- Mapped `Security_ID`, `VirtualAccount`, `EventCategory`, `ImpersonationLevel`, `LinkedLogonID`, `NetworkAccountName`, `NetworkAccountDomain`,and `RestrictedAdminMode` to `security_result.detection_fields`.  
\- Mapped `LogonID` and `TargetLogonID` to `about.labels`.  
\- Mapped `AgentDevice` to `additional.fields`.  
\- Mapped `EventType` to `target.registry.registry_key`.  
\- Mapped `SourcePort` to `principal.port`.  
\- For logs with EventId 4794:  
\- Mapped `Workstation` to `principal.hostname`.  
\- Mapped `ProcessId` to `principal.process.pid`.  
\- Mapped `SourceName` to `target.application`.  
\- Mapped `ProviderGuid` to `target.resource.product_object_id`.   
2023-10-10 |  Enhancement:  
\- Added support for EventIDs 403,404,410,510,1001,1502,1100,4105,4703,4793,4797,4954,5158,5379,5827,6417,10016,10028,18452,36871,1073748860,1073747010,  
2147483684 logs.  
\- Added support for logs that contain Task =~ `SE_ADT`.  
\- Added null check for `AccountName` for EventID=1704,4624,4625,5861.   
2023-09-12 |  Bug-Fix:  
\- Removed mapping of `ProcessName` from `principal.user.userid`.  
\- Added support for new pattern of 4781 event logs.  
\- Checked and added `on_error` for `ProviderGuid`,`LogonID`,`SourceName`,`Task`,`SourceModuleName`,`SourceModuleType` for EventID=4825.  
\- Added null check for `UserID` for EventID=517.  
\- Added support for new pattern of 4731 event logs.   
2023-08-25 |  \- Resolved issue caused due to mapping of `security_result.about.resource.type`.   
2023-08-21 |  Bug-Fix:  
\- Mapped `Account Name` to `principal.user.userid` for EventID 4625 logs.  
\- Mapped `Account Domain` to `principal.administrative_domain` for EventID 4625 logs.  
\- Mapped `Workstation Name` to `principal.hostname` for EventID 4625 logs.  
\- Mapped `Caller Process Id` to `principal.process.pid` for EventID 4625 logs.  
\- Mapped `Source Network Address` to `principal.ip` for EventID 4625 logs.  
\- Mapped `Source Port` to `principal.port` for EventID 4625 logs.  
\- Mapped `Logon Process` to `additional.fields` for EventID 4625 logs.  
\- Mapped `Opcode` to `about.labels`.  
\- Mapped `SubjectLogonId` to `principal.labels`.  
\- Mapped `SubjectUserSid` to `principal.user.windows_sid`.  
\- Mapped `ServiceName` to `target.application`.  
\- Mapped `ImpersonationLevel` to `about.labels`.  
\- Mapped `TargetHandleId` to `about.labels`.  
\- Mapped `RestrictedAdminMode` to `about.labels`.  
\- Mapped `TargetOutboundDomainName` to `target.user.attribute.labels`.  
\- Mapped `KeyLength` to `target.labels`.  
\- Mapped `LmPackageName` to `target.labels`.  
\- Mapped `TargetLogonId` to `target.labels`.  
\- Mapped `TransmittedServices` to `target.labels`.  
\- Mapped `TargetLinkedLogonId` to `target.labels`.  
\- Mapped `VirtualAccount` to `target.labels`.  
\- Mapped `OldSd` to `target.resource.attribute.labels`.  
\- Mapped `NewSd` to `target.resource.attribute.labels`.   
2023-07-24 |  Enhancement:  
\- Added support for EventID 16384 and 16394.  
\- Handled nested XML EventID logs.   
2023-03-17 |  Enhancement:  
\- Supported key-value format logs.  
\- Mapped `Channel`, `SubjectLogonId`, and `ThreadId` to `additional.labels`.  
Enhancement: Parsed the logs with EventID's 4674, 4932, and 4933.  
\- When `EventID` is 4731, 4732, 4733, 4734, 4735, 4737, 4798, or 4799, mapped the following:  
\- Mapped `TargetDomainName` to `target.administrative_domain`.  
\- Mapped `TargetSid` to `target.user.windows_sid`.   
2023-01-15 |  Enhancement:  
\- For `EventId`: 8004.  
\- Mapped `Task` to `target.resource.type`.  
\- Mapped `DomainName` to `principal.administrative_domain`.  
\- Mapped `Keywords`,`Channel`,`Level`,`SChannelName`,`SChannelType`,`Opcode` to "".  
\- Mapped `ThreadID` to `target.resource.attribute.labels`.   
2023-01-13 |  Enhancement:  
\- Handled unparsed logs having `EventId`: 5001, 5007.  
\- Mapped `ProcessID` to `target.process.pid`.  
\- Mapped `ProviderGuid` to `target.resource.product_object_id`.  
\- Mapped `UserID` to `target.user.windows_sid`.  
\- Mapped `ProductName` and `ProductVersion` to `metadata.product_version`.  
\- Mapped `metadata.event_type` to `STATUS_UPDATE`.   
2022-12-06 |  Enhancement:  
\- Handled unparsed logs having `EventId`: 8004.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
