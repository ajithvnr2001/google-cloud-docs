---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-ise-changelog/
title: Change log for CISCO_ISE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:52.456444+00:00
---

# Change log for CISCO_ISE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-ise-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_ISE

Date | Changes  
---|---  
2026-07-31 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: Changed the `event.idm.read_only_udm.metadata.event_type` from `USER_UNCATEGORIZED` to `USER_LOGIN` when `r_cat_name` is `CISE_RADIUS_Accounting` and `Acct-Status-Type` is `Start` and also set `event.idm.read_only_udm.extensions.auth.type` to `AUTHTYPE_UNSPECIFIED`.  
\- `event.idm.read_only_udm.metadata.event_type`: Changed the `event.idm.read_only_udm.metadata.event_type` from `USER_UNCATEGORIZED` to `USER_LOGOUT` when `r_cat_name` is `CISE_RADIUS_Accounting` and `Acct-Status-Type` is `Stop` and also set `event.idm.read_only_udm.extensions.auth.type` to `AUTHTYPE_UNSPECIFIED`.  
\- `event.idm.read_only_udm.metadata.event_type`: Changed the `event.idm.read_only_udm.metadata.event_type` from `USER_UNCATEGORIZED` to `STATUS_UPDATE` when `r_cat_name` is `CISE_Posture_and_Client_Provisioning_Audit`.  
\- `event.idm.read_only_udm.metadata.event_type`: Changed the `event.idm.read_only_udm.metadata.event_type` from `USER_UNCATEGORIZED` to `STATUS_UPDATE` when `r_cat_name` is `CISE_Administrative_and_Operational_Audit` and `event.idm.read_only_udm.metadata.event_type` is `USER_UNCATEGORIZED`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `RequestTime`, `PostureAgentVersion`, `PostureReport`, `PRAEnforcementFlag`, `PRAInterval`, `PRAGraceTime` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-07-10 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `RemoteAddress` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Added grok patterns on `Port` raw log field to extract the numeric port value from string prefixes and mapped with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Port` raw log field with `event.idm.read_only_udm.additional.fields` UDM field when the field contains a non-numeric value.   
2026-07-01 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: When principal machine data and target machine data is present, updated to `USER_LOGIN`.   
2026-06-01 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `time_stamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `session_pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.namespace`: Newly mapped `organization.name` raw log field with `event.idm.read_only_udm.principal.namespace` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `kafkaTopic`, `_time`, `event_details_created`, `cribl_pipe` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `organization_id` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: When `has_principal` is `true` and `has_target` is `true`, updated to `NETWORK_CONNECTION`.  
\- `event.idm.read_only_udm.metadata.event_type`: When `has_target_ip_or_host` is `true` and `has_principal_user` is `true`, updated to `USER_UNCATEGORIZED`.   
2026-05-04 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Port` raw log field with `event.idm.read_only_udm.additional.fields` UDM field when it is not an integer.   
2026-04-09 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: Modified the condition for mapping `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS` when `has_principal_user` is `true` or `has_principal` is `true` or `has_target_user` is `true`.  
\- `event.idm.read_only_udm.metadata.event_type`: Modified the condition for mapping `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` when `has_principal_ip_or_host` is `true` and `has_target_ip_or_host` is `true`.  
\- `event.idm.read_only_udm.metadata.event_type`: Modified the condition for mapping `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` when (`has_target_user` is `true`) or (`has_principal` is `true` and `has_target` is `true`) or (`has_principal` is `true` and `has_target_user` is `true`).  
\- `event.idm.read_only_udm.metadata.event_type`: Modified the condition for mapping `event.idm.read_only_udm.metadata.event_type` to `USER_LOGOUT` when (`has_target_user` is `true`) or (`has_principal` is `true` and `has_target` is `true`) or (`has_principal` is `true` and `has_target_user` is `true`).  
\- `event.idm.read_only_udm.metadata.event_type`: Modified the condition for mapping `event.idm.read_only_udm.metadata.event_type` to `USER_CHANGE_PASSWORD` when (`has_target_user` is `true`) or (`has_principal` is `true` and `has_target` is `true`) or (`has_principal` is `true` and `has_target_user` is `true`).  
\- `event.idm.read_only_udm.metadata.event_type`: Modified the condition for mapping `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` only when `has_principal_ip_or_host` is `true`.   
2026-03-17 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Removed mapping of `Device_IP_Address` and `DeviceIPAddress` from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields as this is an IP of the device the user is trying to connect.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Mapped `Device_IP_Address` and `DeviceIPAddress` raw log fields with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Removed mapping of `DevicePort` from `event.idm.read_only_udm.principal.port` UDM field as this is a port of the device the user is trying to connect.  
\- `event.idm.read_only_udm.target.port`: Mapped `DevicePort` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `NetworkDeviceName` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields as this is a hostname of the device the user is trying to connect.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Mapped `NetworkDeviceName` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Removed mapping of `DestinationIPAddress` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields as this is a server which is authenticating the request of a principal trying to login into a target device.  
\- `event.idm.read_only_udm.intermediary.ip`: Mapped `DestinationIPAddress` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field  
\- `event.idm.read_only_udm.target.port`: Removed mapping of `DestinationPort` from `event.idm.read_only_udm.target.port` UDM field as this is a port of a server which is authenticating the request of a principal trying to login into a target device.  
\- `event.idm.read_only_udm.intermediary.port`: Mapped `DestinationPort` raw log field with `event.idm.read_only_udm.intermediary.port` UDM field.  
\- Modified the conditional check to map `event.idm.read_only_udm.metadata.event_type` to `STATUS_HEARTBEAT` and `STATUS_STARTUP` only when `has_principal` is `true` and `has_target_ip_or_host` is `false`.  
\- Modified the conditional check to map `event.idm.read_only_udm.metadata.event_type` to `STATUS_SHUTDOWN` only when `has_principal` is `false` and `has_target_ip_or_host` is `true`.   
2026-03-06 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: Modified the conditional check for mapping of `event.idm.read_only_udm.metadata.event_type` to `STATUS_SHUTDOWN` when `msg_code` is `12322`, `12930`, `12934`, `12937` and `3001` and `r_cat_name` is `CISE_RADIUS_Accounting` or `CISE_RADIUS_Diagnostics` to map only when `has_target_ip_or_host` is `true` else map to `USER_UNCATEGORIZED`.  
\- `event.idm.read_only_udm.metadata.event_type`: Modified the condition for mapping `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` to map only when `has_principal` is `true` or `has_target_user` is `true` or `has_principal_user` is `true`.  
\- `event.idm.read_only_udm.metadata.event_type`: Changed the conditions for mapping `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` from `has_principal` is `true` to `has_principal` is `true` and `has_principal_user` is `false` and `has_target_user` is `false`.   
2026-02-04 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.ip: Removed mapping of `DeviceIPAddress` from `event.idm.read_only_udm.intermediary.ip` UDM field when `msg_code` is `5400`, `5202`, `5203` and `5201` in-order to introduce a more appropriate UDM mapping.  
\- event.idm.read_only_udm.intermediary.port: Removed mapping of `DevicePort` from `event.idm.read_only_udm.intermediary.port` UDM field when `msg_code` is `5400`, `5202`, `5203` and `5201` in-order to introduce a more appropriate UDM mapping.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `DeviceIPAddress` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field when `msg_code` is `5400`, `5202`, `5203` and `5201`.  
\- event.idm.read_only_udm.principal.port: Newly mapped `DevicePort` raw log field with `event.idm.read_only_udm.principal.port` UDM field when `msg_code` is `5400`, `5202`, `5203` and `5201`.   
2026-01-27 |  Enhancement:  
\- Added a new grok pattern to parse new format of logs.   
2026-01-15 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `nas_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Acct-Multi-Session-Id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `DevicePort` raw log field with `event.idm.read_only_udm.principal.port` UDM field if `msg_code` is `5413`.  
\- Added grok pattern for `Acct-Output-Gigawords` field to correctly extract the integer value.   
2025-12-23 |  Enhancement:  
\- Added new grok pattern to extract `Certificate` and `expiry_date` raw log fields from `msg_attrs` field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Certificate` , `expiry_date` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- The parsing logic for key-value pairs within the `msg_attrs` field has been updated. The raw `msg_attrs` content is now copied to `msg_attrs_1`. Trailing commas and spaces are removed from `msg_attrs_1`. Delimiters within `msg_attrs_1` are transformed by replacing occurrences of , = and ,= with &= before being processed by the kv filter. The kv filter now uses `msg_attrs_1` as the source and & as the field split character.   
2025-10-30 |  Enhancement:  
\- Added a Gsub to replace `AVPair=timezone` to `AVPair=time_zone` to correctly parse the `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.asset.attribute.labels: Newly mapped `Model Name` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.   
2025-10-06 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped Framed-IPv6-Address raw log field(s) with event.idm.read_only_udm.principal.ip UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped Framed-IPv6-Address raw log field(s) with event.idm.read_only_udm.principal.asset.ip UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped dc-profile-name, dc-device-name, Acct-Input-Gigawords, Acct-Output-Gigawords raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.  
\- Added conditional check for `Framed-IPv6-Address` field If the field contains a valid IP address, it is mapped to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields. Otherwise, the original value is mapped to security_result.detection_fields.  
\- Corrected the intermediate field assignment for the raw Framed-IPv6-Address field to FramedIPAddress6.  
\- Added logic to parse cisco-av-pair attributes dc-profile-name and dc-device-name from the raw log message.   
2025-10-04 |  Enhancement:  
\- event.idm.read_only_udm.principal.ip: Newly mapped `FramedIPAddress` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `FramedIPAddress` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `undefined-186`, `undefined-187`, `undefined-188` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added conditional check for `FramedIPAddress` field If the field contains a valid IP address, it is mapped to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields. Otherwise, the original value is mapped to sec_result.detection_fields.   
2025-10-03 |  Enhancement:  
\- Changed the mapping from `event.idm.read_only_udm.security_result` to `sec_result` for `AuthenticationMethod` and `SelectedAuthenticationIdentityStores` raw log field to properly pass the field and prevent duplication.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `Service` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.additional.fields: Newly mapped `Port`, `Type`, `Privilege-Level`, `Authen-Type`, `Authen-Method`, `Service-Argument` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_labels`: Newly mapped `MatchedCommandSet`, `SelectedCommandSet` raw log field with `event.idm.read_only_udm.security_result.rule_labels` UDM field.  
\- Added a conditional check for the `column16` data field to parse the logs in the correct format.   
2025-09-01 |  Enhancement:  
\- Added a grok pattern to extract important fields from the raw logs.  
\- Refactored the logic for the `UniqueSubjectID` additional field to prevent mapping empty values.  
\- Updated event type classification logic to consider the `User-Name` field.  
\- Added fallback to use `User-Name` for `event.idm.read_only_udm.principal.user.userid` when `UserName` is not present.  
\- Adjusted the position of the `NetworkDeviceName` mapping within the configuration.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `ProfilerServer` raw log field to `event.idm.read_only_udm.principal.hostname`.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `ProfilerServer` raw log field to `event.idm.read_only_udm.principal.asset.hostname`.  
\- event.idm.read_only_udm.target.ip: Newly mapped `EndpointNADAddress` raw log field to `event.idm.read_only_udm.target.ip`.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `EndpointNADAddress` raw log field to `event.idm.read_only_udm.target.asset.ip`.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `Calling-Station-ID` raw log field to `event.idm.read_only_udm.principal.mac`.  
\- event.idm.read_only_udm.principal.asset.mac: Newly mapped `Calling-Station-ID` raw log field to `event.idm.read_only_udm.principal.asset.mac`.  
\- event.idm.read_only_udm.principal.user.group_identifiers: Newly mapped `Name` raw log field to `event.idm.read_only_udm.principal.user.group_identifiers`.   
2025-08-25 |  Enhancement:  
\- Added gsub to replace `NetworkDeviceGroups=Location:` to `NetworkDeviceGroups_Location=`.  
\- Added gsub to replace `NetworkDeviceGroups=Device Type:` to `NetworkDeviceGroups_Device_Type=`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `UserName` is not empty and `DestinationIPAddress` is empty, updated to `USER_UNCATEGORIZED`.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `NAS-IP-Address` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ServiceSelectionMatchedRule`, `EapAuthentication`, `ACSVersion`, `NetworkDeviceGroups_Device_Type`, raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.intermediary.location.country_or_region`: Newly mapped `NetworkDeviceGroups_Location` raw log field with `event.idm.read_only_udm.intermediary.location.country_or_region` UDM field.   
2025-08-22 |  Enhancement:  
\- Added a new grok pattern to handle a specific syslog format with a `Response` object.  
\- Refactored `NASPort`, `NASPortType`, and `NASIdentifier` mappings to use intermediate variables (`nas_port`, `nas_port_type`, `nas_identifier`).  
\- Changed the KV field separator for the `kv_data2` field from `; ` to `;`.  
\- Added logic to set `event.idm.read_only_udm.security_result.action` to `BLOCK` and `event.idm.read_only_udm.security_result.action_details` to `FAIL` when the message contains `CISE_Failed_Attempts`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Tunnel-Type` , `Tunnel-Medium-Type`, `Tunnel-Private-Group-ID`, `MS-MPPE-Recv-Key`, `MS-MPPE-Send-Key` raw log fields to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped hardcoded value `CISE_Failed_Attempts` to `event.idm.read_only_udm.additional.fields` for key `login_attempt` when `CISE_Failed_Attempts` is in the message.   
2025-07-18 |  Enhancement:  
\- event.idm.read_only_udm.principal.mac: Newly mapped `EndpointMacAddress` raw log field to `event.idm.read_only_udm.principal.mac`.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `parsed_endpoint_mac` raw log field to `event.idm.read_only_udm.principal.mac`.  
\- event.idm.read_only_udm.target.asset.mac: Newly mapped `PeerAddress` raw log field to `event.idm.read_only_udm.target.asset.mac`.  
\- event.idm.read_only_udm.target.mac: Newly mapped `EndPointMACAddress` raw log field to `event.idm.read_only_udm.target.mac`.  
\- Modified logic to set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` or `NETWORK_CONNECTION` based on the presence of principal or target MAC addresses, using flags like `has_principal` and `has_target`.  
\- Changed condition to validate port value from less than 2147483648 to less than 65535.   
2025-07-11 |  Enhancement:  
\- Modified existing Key names for `event.idm.read_only_udm.additional.fields`, `event.idm.read_only_udm.principal.user.attribute.labels`, `event.idm.read_only_udm.security_result.about.labels` and `event.idm.read_only_udm.security_result.detection_fields` and matched them with raw log field names as follows:  
\- `nas_port` \- `NAS-Port`  
\- `cisco_av_pair_unique` \- `UniqueSubjectID`  
\- `eap_tunnel` \- `EapTunnel`  
\- `nas_identifier_values` \- `NAS-Identifier`  
\- `fremed_mtu` \- `Framed-MTU`  
\- `chargeable_user_identity` \- `Chargeable-User-Identity`  
\- `airspace_wlan_id` \- `Airespace-Wlan-Id`  
\- `authenticationmethod_value` \- `AuthenticationMethod`  
\- `selected_authentication_identity_stores` \- `SelectedAuthenticationIdentityStores`  
\- `UserType_value` \- `UserType`  
\- `Total_Auth_Latency` \- `TotalAuthLatency`  
\- `Client_Latency` \- `ClientLatency`  
\- `Identity_Policy_MatchedRule` \- `IdentityPolicyMatchedRule`  
\- `EndPoint_MatchedProfile` \- `EndPointMatchedProfile`  
\- `Radius_FlowType` \- `RadiusFlowType`  
\- `Is_ThirdParty_DeviceFlow` \- `IsThirdPartyDeviceFlow`  
\- `Selected_Authorization_Profiles` \- `SelectedAuthorizationProfiles`  
\- `ssid_field` \- `SSID`  
\- `Acs SessionID` \- `AcsSessionID`  
\- `Acs_SessionID` \- `AcsSessionID`  
\- `Selected Access Service` \- `SelectedAccessService`  
\- `Selected_Access_Service` \- `SelectedAccessService`  
\- `Endpoint NAD Address` \- `EndpointNADAddress`  
\- `Authentication Identity Store` \- `AuthenticationIdentityStore`  
\- `Authentication_Identity_Store` \- `AuthenticationIdentityStore`  
\- `allow_EasyWired_Session` \- `allowEasyWiredSession`  
\- `Config Version Id` \- `ConfigVersionId`  
\- `Config_Version_Id` \- `ConfigVersionId`  
\- `Request Latency` \- `RequestLatency`  
\- `Request_Latency` \- `RequestLatency`  
\- `Service_Type` \- `Service-Type`  
\- `Class_value` \- `Class`  
\- `Called_Station_ID` \- `Called-Station-ID`  
\- `Calling_Station_ID` \- `Calling-Station-ID`  
\- `Acct_Session_Id` \- `Acct-Session-Id`  
\- `Protocol_value` \- `Protocol`  
\- `Posture_Assessment_Status` \- `PostureAssessmentStatus`  
\- event.idm.read_only_udm.additional.fields: Newly mapped `EnableFlag` and `LicenseTypes` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Modified condition to map `NAS-Port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.   
2025-06-09 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.hostname: Removed mapping of `NetworkDeviceName` from `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.principal.hostname,event.idm.read_only_udm.principal.asset.hostname: Newly mapped `NetworkDeviceName` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.hostname,event.idm.read_only_udm.principal.asset.hostname: Removed mapping of `r_ip_or_host` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname,event.idm.read_only_udm.intermediary.asset.hostname: Mapped `r_ip_or_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.ip,event.idm.read_only_udm.principal.asset.ip: Removed mapping of `r_ip_or_host` from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.ip,event.idm.read_only_udm.intermediary.asset.ip: Mapped `r_ip_or_host` raw log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Removed mapping of `STATUS_UPDATE` from `event.idm.read_only_udm.metadata.event_type` UDM field when `r_ip_or_host` is not null.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` UDM field to `USER_UNCATEGORIZED` if principal user is present.  
\- Added a conditional check whether target is present or not when `event.idm.read_only_udm.metadata.event_type` UDM field is being set as `NETWORK_CONNECTION`.  
\- Added a conditional check whether principal hostname is present or not when `event.idm.read_only_udm.metadata.event_type` UDM field is being set as `STATUS_UPDATE`.  
\- event.idm.read_only_udm.principal.hostname,event.idm.read_only_udm.target.asset.hostname: Removed mapping of `r_ip_or_host` from `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.ip,event.idm.read_only_udm.target.asset.ip: Removed mapping of `r_ip_or_host` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- Added conditional check to map `event.idm.read_only_udm.metadata.event_type` UDM field to `NETWORK_FLOW` and `NETWORK_CONNECTION` if principal and target is present.  
\- Added conditional check to map `event.idm.read_only_udm.metadata.event_type` UDM field to `STATUS_HEARTBEAT` and `STATUS_UNCATEGORIZED` if principal is present.  
\- Added conditional check to map `event.idm.read_only_udm.metadata.event_type` UDM field to `STATUS_UPDATE` if principal hostname is present.  
\- event.idm.read_only_udm.intermediary: Newly mapped `intermediary` raw log field with `event.idm.read_only_udm.intermediary` UDM field.  
\- Removed redundant mapping :  
\- Removed redundant mapping where `event.idm.read_only_udm.metadata.event_type` is being set as `USER_UNCATEGORIZED`, `STATUS_UPDATE` and `NETWORK_CONNECTION`.  
\- Removed redundant mapping of `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- Removed redundant mapping of `event.idm.read_only_udm.metadata.product_name` UDM field.   
2025-05-30 |  Enhancement:  
\- `event.idm.read_only_udm.target.port`: Newly mapped `DestinationPort` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `NAS-Port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `NAS-IP-Address` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.mac`: Nelwy mapped `SSID` raw log field with `event.idm.read_only_udm.intermediary.mac` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `UserName`, `User-Name` raw log fields with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `CPMSessionID` , `TotalAuthenLatency` , `ClientLatency` , `IdentityPolicyMatchedRule` , `EndPointMatchedProfile` , `RadiusFlowType` , `IsThirdPartyDeviceFlow` , `SelectedAuthorizationProfiles` , `SSID` , `AcsSessionID` , `SelectedAccessService` , `AuthenticationIdentityStore` , `allowEasyWiredSession` , `ConfigVersionId` , `RequestLatency` , `Service-Type` , `Class` , `Called-Station-ID` , `Calling-Station-ID` , `Acct-Session-Id` , `Protocol` , `PostureAssessmentStatus` , `r_total_seg` , `r_seg_num`, `EapTunnel`, `cisco-av-pair`, `Framed-MTU` , `Airespace-Wlan-Id`, raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Modified the grok patterns in order to parse the logs with `r_datetime` raw log field with `TIMESTAMP_ISO8601` format.  
\- `event.idm.read_only_udm.principal.labels` : Newly mapped `NAS-Identifier` raw log field with `event.idm.read_only_udm.principal.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels` : Nelwy mapped `Chargeable-User-Identity`, `UserType` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields` : Newly mapped `AuthenticationMethod`, `SelectedAuthenticationIdentityStores` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type` : Newly mapped `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` and `USER_LOGOUT` when `has_principal` and `has_target` and `has_user` are `true`.   
2025-05-14 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `r_ip_or_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.asset.hostname: Newly mapped `r_ip_or_host` raw log field with `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.   
2025-04-24 |  Enhancement:  
\- Added Gsub to replace `@timestamp` with `timestamp` on `message` to parse the logs.  
\- Added a Grok pattern to parse the logs.  
\- event.idm.read_only_udm.observer.ip: Removed mapping of `r_ip_or_host` from `event.idm.read_only_udm.observer.ip` UDM field and mapped `_principal_ip` instead.  
\- Added a Grok pattern to extract `principal_ip_address` from `r_ip_or_host`.  
\- event.idm.read_only_udm.principal.ip,event.idm.read_only_udm.principal.asset.ip: Removed mapping of `r_ip_or_host` from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field and mapped `principal_ip_address` instead.   
2025-04-17 |  Enhancement:  
\- `kv` : Added support for `kv` format.  
\- `event.idm.read_only_udm.principal.nat_ip`: Newly mapped `NAS-IP-Address` raw log field with `event.idm.read_only_udm.principal.nat_ip` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `DestinationIPAddress` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field and set `has_target` to `true`.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `Device_IP_Address` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field and set `has_principal` to `true`.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `UserName` and `User-Name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `NetworkDeviceProfileId` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.mac` : Newly mapped `EndpointMacAddress` raw log field with `event.idm.read_only_udm.principal.asset.mac` UDM field.  
\- `event.idm.read_only_udm.principal.ip` : Newly mapped `ISELocalAddress` raw log field with `event.idm.read_only_udm.principal.ip` UDM field and set `has_principal` to `true`.  
\- `event.idm.read_only_udm.principal.asset.ip` : Newly mapped `ISELocalAddress` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field and set `has_principal` to `true`.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `NetworkDeviceProfileName` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped event.idm.read_only_udm.metadata.event_type UDM field as `NETWORK_CONNECTION` when owner `has_principal` and `has_target` are not null.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped event.idm.read_only_udm.metadata.event_type UDM field as `STATUS_UPDATE` when owner `has_principal` is not null.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped event.idm.read_only_udm.metadata.event_type UDM field as `GENERIC_EVENT` when `has_principal` and `has_target` are null.  
\- Newly added multiple grok patterns in order to parse the logs with syslog+kv format.  
\- Added gsub for `Device Ip Address` raw log field.   
2025-04-11 |  Enhancement:  
\- Added support for the event `CISE_Guest` and relevant corresponding raw log fields.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `UserName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field and set `has_principal_user` to `true`.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `MacAddress` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM fields.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `IpAddress` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields and set `has_principal` to `true`.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `UserType` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `PortalName` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `NADAddress` raw log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields and set `has_intermediary` to `true`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `AuditSessionId` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional_fields: Newly mapped `ResponseTime` raw log field with `event.idm.read_only_udm.additional_fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Removed condition to unnecessarily map `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT` for the event `CISE_RADIUS_Diagnostics` as these logs have important data to map to other `event_types`.   
2025-03-17 |  Enhancement:  
\- Mapped `EndPointMACAddress` to `principal.asset.mac`.  
\- Mapped `ISEPolicySetName to `target.resource.name".  
\- Mapped `CPMSessionID` to `network.session_id`.  
\- Mapped `StepLatency` to `additional.fields`.  
\- Mapped `TotalAuthenLatency` to `sec_result.detection_fields`.  
\- Mapped `ClientLatency` to `sec_result.detection_fields`.  
\- Mapped `HostIdentityGroup` to `additional_fields`.   
2025-03-13 |  Enhancement:  
\- Added a Grok pattern to parse NTP Server value.  
\- Mapped `ntp_server_1`, `ntp_server_2`, and `ntp_server_3` to `target.ip` and `target.asset.ip`.  
\- Added support to parse CSV logs.  
\- Mapped `column11` to `metadata.description`.  
\- Mapped `column14` to `metadata.product_log_id`.  
\- Mapped `column16` to `principal.hostname` and `principal.asset.hostname`.   
2025-03-05 |  Enhancement:  
\- Added a new Grok pattern to support logs with a new format.   
2025-02-19 |  Enhancement:  
\- Added support for a new format of logs.  
\- Mapped `user` to `principal.user.userid`.  
\- Mapped `Source` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `localport` to `principal.port`.   
2025-01-23 |  Enhancement:  
\- Mapped `ntp_server_1`, `ntp_server_2`, and `ntp_server_3` to `target.ip`.   
2024-12-19 |  Enhancement:  
\- Added a Grok pattern to parse a new log pattern.  
\- Mapped `dc-protocol-map` , `audit-session-id` , `vlan-id` , `method` , `cisco-wlan-ssid` , `SelectedAccessService` , and `Network_Device_Profile` to `security_result.detection_fields`.   
2024-11-19 |  Enhancement:  
\- Added a Grok pattern to map `UserName` to `principal.user.userid`.   
2024-11-18 |  Enhancement:  
\- Added Grok pattern to parse a new log pattern.  
\- Added null check to `r_ip_or_host` before mapping it to `observer.hostname`.  
\- Added null check to `r_ip_or_host` before mapping it to `principal.hostname` and `principal.asset.hostname` or merging it with `principal.ip` and `principal.asset.ip`.  
\- Added a new Grok pattern to parse `msg_attrs`.  
\- Mapped `threshold_value` to `additional.fields`.  
\- Mapped `used_space_value` to `additional.fields`.   
2024-10-30 |  Enhancement:  
\- Mapped `Nas-Port-id` to `security_result.detection_fields`.  
\- Mapped `UserName` to `principal.mac`.  
\- Mapped `SSID` to `security_result.detection_fields`.   
2024-10-29 |  Enhancement:  
\- Added a new Grok pattern to parse logs with nested syslog headers.   
2024-09-18 |  Enhancement:  
\- Removed mapping of SYSLOG header `hostname` from `intermediary.hostname`.   
2024-08-06 |  Enhancement:  
\- Mapped `hostname` from SYSLOG header to `intermediary.hostname`.   
2024-07-30 |  Enhancement:  
\- Mapped `RadiusFlowType` to `security_result.detection_fields`.   
2024-05-10 |  Enhancement:  
\- Mapped `ExternalGroups` to `additional.fields`.   
2024-05-09 |  Enhancement:  
\- Added Grok patterns to parse new formats of `CISE_Profiler`.  
\- Mapped some fields for `CISE_Administrative_and_Operational_Audit` and `CISE_Alarm`.   
2024-04-18 |  Enhancement:  
\- Mapped `msg_sev` to `security_result.severity_details`.  
\- Mapped `r_total_seg`, `r_seg_num`, `msg_code`, and `r_msg_id` to `security_result.detection_fields`.  
\- Mapped `r_cat_name` to `security_result.category_details`.  
\- Mapped `msg_text` and `msg_class` to `metadata.description`.  
\- Aligned `target.ip` and `target.asset.ip` mappings.  
\- Aligned `target.hostname` and `target.asset.hostname` mappings.  
\- Aligned `principal.ip` and `principal.asset.ip` mappings.  
\- Aligned `principal.hostname` and `principal.asset.hostname` mappings.  
\- Added a Grok pattern to parse `msg_attrs`.   
2024-04-10 |  Bug-Fix:  
\- Added Grok patterns to parse new formats of `PeerName`.   
2023-11-20 |  Enhancement:  
\- Added new Grok patterns to parse failing Syslogs.  
\- Added `msg_code` `5412` to parse logs having the same `msg_code`.   
2023-09-29 |  Enhancement:  
\- Added support for a new pattern of JSON logs.  
\- Mapped `EndpointSourceEvent`, `NASIdentifier`, `NAS-Port-Type`, `NAS-Port-Id`, `ProfilerServer` to `security_result.detection_fields` for 80002 and 80006 logs.  
\- Changed mapping of `Location` from `principal.location` to `target.location` for 80002 and 80006 logs.  
\- Added on_error check to replace and merge functions.  
\- Modified date mapping to parse date with `MEST` and `MESZ` timezones.   
2023-08-02 |  Enhancement -  
\- Added KV mapping to parse and map `cisco-av-pair=dhcp-option=host-name` to `target.hostname`.  
\- Changed mapping of `security_result.action` from `FAIL` to `BLOCK` when `msg_text` contains `failed|dropped|stop|rejected|down|abandoned|block|blocking|invalid`.   
2023-07-18 |  Enhancement -  
\- Mapped `cisco-av-pair=dhcp-option=host-name` to `target.hostname`.  
\- Changed mapping of `User-Name` from `target.user.userid` to `principal.user.userid`.  
\- Changed mapping of `UserName` from `target.user.userid` to `principal.user.userid`.  
\- Changed mapping of `User` from `target.user.userid` to `principal.user.userid`.  
\- Changed mapping of `PhoneNumber` from `target.user.phone_numbers` to `principal.user.phone_numbers`.  
\- Mapped `FramedIPAddress` to `security_result.detection_fields` for Profiler event types 80002, 80006.  
\- Modified date mapping to parse date with `EASTERN` timezone.  
\- Added Grok pattern to match `PeerAddress`.   
2023-06-07 |  Enhancement-  
\- Added Grok pattern to parse a new log pattern.   
2023-05-26 |  Enhancement-  
\- Modified date mapping to parse date with `BJ` timezone.   
2023-04-18 |  Enhancement-  
\- Added a `json` block to handle JSON logs.  
\- Mapped `logstash.irm_region` to `additional.fields`.  
\- Mapped `logstash.irm_environment` to `additional.fields`.  
\- Mapped `logstash.irm_site` to `additional.fields`.  
\- Mapped `logstash.ingest.timestamp` to `metadata.ingested_timestamp`.  
\- Mapped `logstash.process.timestamp` to `metadata.collected_timestamp`.   
2023-03-01 |  Enhancement-  
\- Whenever `Calling-Station-ID` is an IP address, then map it to `principal.ip`.  
\- Added a regular expression condition to validate MAC address for field `device-mac` before mapping to `principal.mac`.   
2022-12-08 |  Enhancement-  
-Mapped `assetDeviceType` to `principal.resource.name`.  
-Mapped `assetIncidentScore` to `security_result.detection_fields`.  
-Mapped `PostureAssessmentStatus` to `security_result.detection_fields`.  
-Mapped `PolicyVersion` to `security_result.detection_fields`.  
-Mapped `EndPointVersion` to `security_result.detection_fields`.  
-Mapped `EndPointPolicyID` to `security_result.detection_fields`.   
2022-10-13 |  Enhancement- Corrected the date mapping for SYSLOGTIMESTAMP date formats.   
2022-08-12 |  Bug fix -  
-Modified mapping for the field `prinicipal.asset.hostname` to `intermediary.hostname`.  
-Modfied event_type from GENERIC_EVENT to STATUS_UPDATE or NETWORK_CONNECTION.   
2022-08-10 |  Enhancement- Modified mappings for the following fields from `additional.fields` to `security_result.detection_fields`.  
\- `CPMSessionID`, `NASPort`, `AD-Log-Id`, `AD-Srv-Query`, `AD-Srv-Record`, `Tunnel-Client-Endpoint`, `IsThirdPartyDeviceFlow`, `PostureStatus`, `OperationMessageText`, `AcsSessionID`, `SelectedAccessService`, `RadiusPacketType`, `ISELocalAddress`, `ISEModuleName`, `ISEServiceName`, `ConnectionStatus`, `UniqueConnectionIdentifier`, `Audit_session_id`, `EndpointCertainityMetric`, `EndpointNADAddress`, `EndpointOUI`, `EndpointProperty`, `AuthenticationIdentityStore`, `AD-Host-Candidate-Identities`, `PostureExpiry`, `allowEasyWiredSession`, `ConfigVersionId`, `RequestLatency`, `Service-Type`, `Framed-Protocol`, `Class`, `Called-Station-ID`, `Calling-Station-ID`, `Acct-Status-Type`, `Acct-Delay-Time`, `Acct-Input-Octets`, `Acct-Output-Octets`, `Acct-Session-Id`, `Acct-Authentic`, `Acct-Session-Time`, `Acct-Input-Packets`, `Acct-Output-Packets`, `Acct-Terminate-Cause`, `Protocol`.   
2022-07-11 |  Bug-fix - Mapped NetworkDeviceName to `event.idm.read_only_udm.principal.hostname` where Product_event_type is 5440 RADIUS.  
\- Mapped r_ip_or_host to observer.ip or observer.hostname.  
\- Dropped malformed/encoded logs.   
2022-05-02 |  Bug-fix - Corrected mapping for `security_result.action` from `ALLOW` to `FAIL` where the log_type is `CISE_Failed_Attempts`.   
2022-04-21 |  Enhancement-Parsed the logs with log_type=`CISE_Profiler`  
-For log_type=`CISE_TACACS_Accounting changed event_type from `GENERIC_EVENT` to `USER_UNCATEGORIZED'  
-Added proper condition for `NASPort` field and `Port` field.   
2022-04-18 |  -Mapped `foreign_ip` to `intermediary.ip`  
-Parsed the logs with log_type=`CISE_TACACS_Accounting` and `CISE_RADIUS_Accounting`  
-For log_type=`CISE_TACACS_Accounting changed event_type from `GENERIC_EVENT` to `USER_UNCATEGORIZED'  
-Added proper condition for `NASPort` field.   
2022-04-13 |  \- Mapped NAS-Port-Id in event: 5200.  
\- Mapped hostname in events: 60188, 60125, 60116, 60115, 60081, 60080, 51021, 51020, 51003, 51002, 51001, 51000, 52000, 52001, 52002.  
\- Mapped Operation Message text in about.labels in event: 52000.  
\- Mapped Serial Number in additional_fields in event: 5200.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
