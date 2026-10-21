---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberark-pam-changelog/
title: Change log for CYBERARK_PAM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:12:11.827014+00:00
---

# Change log for CYBERARK_PAM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberark-pam-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CYBERARK_PAM

Date | Changes  
---|---  
2026-09-16 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `cs1` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field when `cs1Label` is `Affected User Name` and `duser` is empty.   
2026-08-31 |  Enhancement:  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `source` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `customData.target` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `isDr` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-04-29 |  Enhancement:  
\- Added a grok pattern to parse SYSLOG+JSON logs.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `Command` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `User` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `syslog.audit_record.TargetUser` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field if `User` raw log field is empty.  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `syslog.audit_record.TargetUser` raw log field with `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `SrcHost` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `DstHost` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.process.file.names`: Newly mapped `ProcessName` raw log field with `event.idm.read_only_udm.target.process.file.names` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `SessionID` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `Protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `syslog.audit_record.Issuer` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `syslog.audit_record.SourceUser` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `syslog.audit_record.SourceUser` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `syslog.audit_record.Action` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `syslog.audit_record.Version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `syslog.audit_record.Severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `syslog.audit_record.Severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `syslog.audit_record.Location` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `syslog.audit_record.Message` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog.audit_record.CAProperties.CAProperty`, `format`, `syslog.audit_record.Rfc5424`, `syslog.audit_record.Timestamp`, `syslog.audit_record.IsoTimestamp`, `syslog.audit_record.Hostname`, `syslog.audit_record.Vendor`, `syslog.audit_record.Product`, `syslog.audit_record.RequestId`, `version`, `PSMID` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-04-27 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.name`: Mapped `cs2` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field when `cs2Label` is `Safe Name`.  
\- `event.idm.read_only_udm.metadata.description`: Mapped from `act` raw log field when `name` indicates a file search failure and a file name is not present.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- Set to FILE_CREATION when the name indicates file creation, and principal machine data and target file data are present.  
\- Set to FILE_READ when the name indicates file read or file retrieve, and principal machine data and target file data are present.  
\- Set to USER_LOGOUT when the name indicates user logoff or session end, and user data and target machine data are present.  
\- Set to USER_CHANGE_PASSWORD when the name indicates password management, and principal and target machine data are present.  
\- Set to FILE_UNCATEGORIZED when the name indicates file category update, and principal machine data and target file data are present.  
\- Set to SYSTEM_AUDIT_LOG_UNCATEGORIZED when the name indicates keystroke logging, and principal machine and principal user data are present.  
\- Set to USER_RESOURCE_ACCESS when the name indicates file or metadata access, and principal machine data and target resource data are present.  
\- Set to USER_LOGIN when the name or EventMessage indicates user authentication, and user, principal, and target machine data are present.  
\- `event.idm.read_only_udm.extensions.auth.mechanism`:  
\- Set to `REMOTE` when `name` indicates a file creation or upload AND `app` is `RDP`.  
\- Set to `USERNAME_PASSWORD` when `name` indicates a file creation or upload AND `app` is not `RDP`.  
\- Set to `REMOTE` when `name` or `EventMessage` indicates a user authentication event AND `app` is `RDP`.  
\- Set to `USERNAME_PASSWORD` when `name` or `EventMessage` indicates a user authentication AND `app` is not `RDP`.  
\- Set to `REMOTE` when `name` indicates a user logoff or disconnect AND `app` is `RDP`.  
\- Set to `USERNAME_PASSWORD` when `name` indicates a user logoff or disconnect AND `app` is not `RDP`.   
2026-04-10 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `event_data.created` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `host` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.metadata.event_type`: Set the value of `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS` when the `name` is `Backup Metadata` and target resource information is present.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly Set the value of `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` when the `EventMessage` is `User Authentication` and both principal and target information is present.  
\- `event.idm.read_only_udm.extensions.auth.mechanism`: Newly set the value `USERNAME_PASSWORD` to the `event.idm.read_only_udm.extensions.auth.mechanism` UDM field when the `EventMessage` is `User Authentication` and both principal and target information is present.   
2026-03-27 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.asset.ip`: Newly mapped `dvc` raw log field with `event.idm.read_only_udm.intermediary.asset.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `dvc` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM fields if `dvc` is not an IP address.  
\- Added grok patterns on `dvc`, `shost` and `dhost` to validate ip addresses instead of using regex pattern.  
\- Added gsub to replace the string `event` to `event_data` in raw log to avoid conflict with reserved UDM keyword `event`.  
\- Added support for a log format where the primary log data is within the `event_data.original` field of a JSON object.  
\- As we added support for `event_data`, the following UDM fields are now being mapped correctly:  
\- `event.idm.read_only_udm.additional.fields`  
\- `event.idm.read_only_udm.extensions.auth.mechanism`  
\- `event.idm.read_only_udm.intermediary.ip`  
\- `event.idm.read_only_udm.metadata.description`  
\- `event.idm.read_only_udm.metadata.event_timestamp`  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.product_log_id`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.product_version`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`  
\- `event.idm.read_only_udm.principal.resource.name`  
\- `event.idm.read_only_udm.principal.user.user_display_name`  
\- `event.idm.read_only_udm.principal.user.userid`  
\- `event.idm.read_only_udm.security_result.action_details`  
\- `event.idm.read_only_udm.security_result.description`  
\- `event.idm.read_only_udm.security_result.severity`  
\- `event.idm.read_only_udm.target.application`  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`  
\- `event.idm.read_only_udm.target.file.full_path`  
\- `event.idm.read_only_udm.target.resource.name`  
\- `event.idm.read_only_udm.target.user.user_display_name`  
\- `event.idm.read_only_udm.target.user.userid`  
2026-02-05 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `CPMStatus`, `CreationMethod`, `LastSuccessChange`, `LastSuccessVerification`, `LastTask`, `RequestId`, `RetriesCount`, `SequenceID` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `GatewayStation` raw log field(s) with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `GatewayStation` raw log field(s) with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `Desc` raw log field(s) with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `Action` raw log field(s) with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `MessageID` raw log field(s) with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `Version` raw log field(s) with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `Address`, `Station` raw log field(s) with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `Address`, `Station` raw log field(s) with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `Address`, `Station` raw log field(s) with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `Address`, `Station` raw log field(s) with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `UserName` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `PolicyID` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.src.user.userid`: Newly mapped `Issuer` raw log field(s) with `event.idm.read_only_udm.src.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `DeviceType` raw log field(s) with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- If `Severity` is `Info`, `event.idm.read_only_udm.security_result.severity` is set to `LOW`.   
2026-01-16 |  Enhancement:  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `PSMID` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `PSMID` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `GatewayStation` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `GatewayStation` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.process.file.full_path: Newly mapped `reason` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ApplicationType`, `RDPOffset`, `VIDOffset`, `ConnectionComponentId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added support to parse event_timestamp correctly for the new format of logs.  
\- event.idm.read_only_udm.target.process.pid: Newly mapped `ProcessId` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.   
2025-12-12 |  Enhancement:  
\- Added a new grok pattern to parse LEEF formatted logs.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `leef_version`,`leef_event_id` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `inter_host` raw log field(s) with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `EventMessage` raw log field(s) with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src` raw log field(s) with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `usrName` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `Reason` raw log field(s) with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `Category` raw log field(s) with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `sev` raw log field(s) with `event.idm.read_only_udm.security_result.severity` and `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `address` raw log field(s) with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `Safe` raw log field(s) with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `username` raw log field(s) with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `Action` raw log field to `event.idm.read_only_udm.metadata.product_event_type` UDM field if `message` contains `LEEF`.  
\- Renamed from `_intermediary` to `intermediary`.  
\- Added conditional logic before mapping `Action` and `username` fields based on whether the log message contains `LEEF`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `EventMessage` in [`CPM Change Password`, `Failure: CPM Change Password Failed`, `Set Password`, or `Store password`] updated to `USER_CHANGE_PASSWORD`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `EventMessage` in [`Failure: Find Files`, `Open File (Write Only)`, `Retrieve File`, `Retrieve password`, or `Update File Category`] and `has_target` is true, updated to `FILE_READ`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `EventMessage` in [`Failure: Find Files`, `Open File (Write Only)`, `Retrieve File`, `Retrieve password`, or `Update File Category`] and `has_target` is false, updated to `USER_RESOURCE_ACCESS`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `event_type` is `GENERIC_EVENT` and `has_principal` is `true` , updated to `STATUS_UPDATE`.  
\- The mapping logic for `event.idm.read_only_udm.src.hostname` from the `header_host` field was updated to write directly to the UDM field, removing an intermediate step.   
2025-12-02 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Validate_ticket_number`, `User`, `Account`, `cs6` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-11-28 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: If name is one of [`Failure: Find Files`, `Open File (Write Only)`, `Retrieve File`, `Retrieve password`], has_principal is true, and has_target is false, the event type is now set to USER_RESOURCE_ACCESS.  
\- `event.idm.read_only_udm.metadata.event_type`: The condition to set the event type to FILE_READ has been updated to require has_target to be true.   
2025-10-22 |  Enhancement:  
\- event.idm.read_only_udm.principal.administrative_domain: Newly mapped `logondomain` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- event.idm.read_only_udm.principal.resource.resource_subtype: Newly mapped `devicetype` raw log field with `event.idm.read_only_udm.principal.resource.resource_subtype` UDM field.  
\- event.idm.read_only_udm.src.hostname: Newly mapped `header_host` raw log field with `event.idm.read_only_udm.src.hostname` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Ticket_ID` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Ticketing_System` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Ticketing_Audit_Safe` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Action` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `msg` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.principal.resource.name: Newly mapped `name` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `policyid` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-05-08 |  Enhancement:  
\- `JSON`: Added support for `JSON` format.  
\- Added gsub function to replace `message` with `msg` from `message" field.  
\- Added conditional check before dropping logs.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `msg` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `actionType`, `action`, `auditType`, `customData.app_id`, `customData.end_time`, `customData.is_internal_application`, `customData.scopes`, `customData.start_time`, `customData.token_type`, `customData.user_guid`, `identityType`, `tenantId`, `component`, `serviceName`, `customData.DPA.ephemeral_user`, `customData.DPA.access_method`, `customData.DPA.assigned_domain_groups`, `customData.DPA.assigned_groups`, `customData.DPA.authentication_methods`, `customData.DPA.connection_string`, `customData.DPA.maximum_session_duration`, `customData.deny_by_user`, `customData.mfa_reason`, `customData.factors`, `customData.auth_method`, `customData.entity_type`, `customData.mfa_initiator`, `safe`, `cloudAssets`, `cloudIdentities` and `cloudResources` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `applicationCode` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `auditCode` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `userId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `username` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.cloud.environment: Newly mapped `cloudProvider` raw log field with `event.idm.read_only_udm.principal.cloud.environment` UDM field.  
\- if `cloudProvider` similar to `aws` then mapped `AMAZON_WEB_SERVICES`.  
\- if `cloudProvider` similar to `azure` then mapped `MICROSOFT_AZURE`.  
\- if `cloudProvider` similar to `gcp` then mapped `GOOGLE_CLOUD_PLATFORM`.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `customData.client` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `uuid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `source` raw log field with `event.idm.read_only_udm.principal.ip` UDM field (if it is an IP).  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `source` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field (if it is an IP).  
\- event.idm.read_only_udm.extensions.auth.auth_details: Newly mapped `accessMethod` raw log field with `event.idm.read_only_udm.extensions.auth.auth_details` UDM field.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped `accountId` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `sessionId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `target` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `target` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.labels: Newly mapped `targetPlatform` raw log field with `event.idm.read_only_udm.target.labels` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `customData.DPA.source_hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `customData.DPA.source_hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.user.attributes.labels: Newly mapped `customData.DPA.source_user` raw log field with `event.idm.read_only_udm.principal.user.attributes.labels` UDM field.  
\- event.idm.read_only_udm.target.labels: Newly mapped `customData.DPA.target_machine` raw log field with `event.idm.read_only_udm.target.labels` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `customData.entity_name` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `customData.entity_name` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.location.region_latitude: Newly mapped `customData.geoip_latitude` raw log field with `event.idm.read_only_udm.principal.location.region_latitude` UDM field.  
\- event.idm.read_only_udm.principal.location.region_longitude: Newly mapped `customData.geoip_longitude` raw log field with `event.idm.read_only_udm.principal.location.region_longitude` UDM field.  
\- event.idm.read_only_udm.principal.location.city: Newly mapped `customData.geoip_city_name` raw log field with `event.idm.read_only_udm.principal.location.city` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `customData.mfa_result` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `customData.geoip_country_name` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.principal.asset.platform_software.platform: Newly mapped `customData.request_device_os` raw log field with `event.idm.read_only_udm.principal.asset.platform_software.platform` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `customData.request_broswer_name` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `customData.geoip_country_code` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `accountName` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `targetAccount` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.target.user.attribute.labels: Newly mapped `customData.PAM.new_target` raw log field with `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `customData.PAM.target` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `customData.directory_service_id` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `customData.user_id` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `customData.user_name` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.extensions.auth.type: Newly mapped `customData.mfa_initiator` raw log field with `event.idm.read_only_udm.extensions.auth.type` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If the log has `event.idm.read_only_udm.principal.user.userid`, then the `event.idm.read_only_udm.metadata.event_type` is mapped to `USER_LOGIN`.   
2025-02-06 |  Enhancement:  
\- Mapped `signature_id` to `metadata.product_event_type`.  
\- If `severity` is 0, 1, 2, or 3, then `security_result.severity` is mapped to `LOW`. Otherwise, if `severity` is 4, 5, or 6, then `security_result.severity` is mapped to `MEDIUM`. Otherwise, if `severity` is 7 or 8, then `security_result.severity` is mapped to `HIGH`. Otherwise, if `severity` is 9 or 10, then `security_result.severity' is mapped to `CRITICAL".   
2024-11-28 |  Enhancement:  
\- Added a Grok pattern to parse `metadata.version`.   
2024-11-21 |  Enhancement:  
\- Mapped `act` to `metadata.product_event_type`.  
\- Mapped `app` to `target.application`.   
2024-10-29 |  \- Added support for new log patterns.   
2024-05-05 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
