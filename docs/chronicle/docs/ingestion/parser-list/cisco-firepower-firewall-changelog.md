---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-firepower-firewall-changelog/
title: Change log for CISCO_FIREPOWER_FIREWALL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:45:30.257582+00:00
---

# Change log for CISCO_FIREPOWER_FIREWALL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-firepower-firewall-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_FIREPOWER_FIREWALL

Date | Changes  
---|---  
2026-09-16 |  Enhancement:  
\- Added a new Grok pattern to parse hostname correctly.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Original_Address`, `internal_ts`, `after` and `before` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-08-07 |  Enhancement:  
\- `event.idm.read_only_udm.src.ip` and `event.idm.read_only_udm.src.asset.ip`: Newly mapped `originalClientSrcIP` raw log field with `event.idm.read_only_udm.src.ip` and `event.idm.read_only_udm.src.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Mapped `ReferencedHost` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields if it is a hostname.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `SSLVersion` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- `event.idm.read_only_udm.network.tls.cipher`: Newly mapped `SSLCipherSuite` raw log field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- `event.idm.read_only_udm.network.tls.client.server_name`: Newly mapped `SSLServerName` raw log field with `event.idm.read_only_udm.network.tls.client.server_name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `InspectedPacketCount` and `InspectionMicroseconds` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-07-08 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.ingestion_labels`: Removed mapping of `action` raw log field with key `event_action` from `event.idm.read_only_udm.metadata.ingestion_labels` UDM field as it is a duplicate mapping.  
\- `event.idm.read_only_udm.metadata.ingestion_labels`: Removed mapping of `action` raw log field with key `connection_type` from `event.idm.read_only_udm.metadata.ingestion_labels` UDM field when `action` is `ALLOW` or `BLOCK`as it is dupliacted with `event.idm.read_only_udm.security_result.action` UDM field.   
2026-06-17 |  Enhancement:  
\- Added a new grok pattern to parse new format of logs with eventIds `746012`, `746013`, `815004`, `111009`, `720041`, `720042`.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Newly mapped `target_uid` field with `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `principal_uid` field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Setting `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` when message contains `Add` and `user_deatils` else if message contains `Delete` and `user_details` then setting `event.idm.read_only_udm.metadata.event_type` to `USER_LOGOUT`.  
\- `event.idm.read_only_udm.extensions.auth.type`: Setting `event.idm.read_only_udm.extensions.auth.type` to `VPN` when message contains `VPN` else setting it to `AUTHTYPE_UNSPECIFIED`.   
2026-05-29 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: If `eventId` is `430005` or `430004` and `ApplicationProtocol` is `SMTP`, then set the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_SMTP`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ArchiveFileStatus` and `ApplicationProtocol` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-02-19 |  Enhancement:  
\- Added new grok patterns to parse `event.idm.read_only_udm.intermediary.hostname` UDM field correctly.  
\- Added new grok patterns to parse `event.idm.read_only_udm.principal.userid` and `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields correctly.  
\- event.idm.read_only_udm.target.userid: Newly mapped `target_user` raw log field with `event.idm.read_only_udm.target.userid` UDM field.   
2026-02-12 |  Enhancement:  
\- Added support to parse logs with no `ApplicationProtocol` UDM field. This is allowing the following UDM fields to be mapped correctly:  
\- event.idm.read_only_udm.intermediary.asset.hostname.  
\- event.idm.read_only_udm.intermediary.hostname.  
\- event.idm.read_only_udm.metadata.event_timestamp.seconds.  
\- event.idm.read_only_udm.metadata.ingestion_labels.key.  
\- event.idm.read_only_udm.metadata.ingestion_labels.value.  
\- event.idm.read_only_udm.metadata.log_type.  
\- event.idm.read_only_udm.metadata.product_name.  
\- event.idm.read_only_udm.metadata.vendor_name.  
\- event.idm.read_only_udm.network.http.parsed_user_agent.device.  
\- event.idm.read_only_udm.network.http.parsed_user_agent.family.  
\- event.idm.read_only_udm.network.http.user_agent.  
\- event.idm.read_only_udm.network.ip_protocol.  
\- event.idm.read_only_udm.network.received_bytes.  
\- event.idm.read_only_udm.network.received_packets.  
\- event.idm.read_only_udm.network.sent_bytes.  
\- event.idm.read_only_udm.network.sent_packets.  
\- event.idm.read_only_udm.principal.asset.attribute.labels.key.  
\- event.idm.read_only_udm.principal.asset.attribute.labels.value.  
\- event.idm.read_only_udm.principal.asset.ip.  
\- event.idm.read_only_udm.principal.ip.  
\- event.idm.read_only_udm.principal.port.  
\- event.idm.read_only_udm.security_result.category_details.  
\- event.idm.read_only_udm.security_result.confidence_details.  
\- event.idm.read_only_udm.security_result.detection_fields.  
\- event.idm.read_only_udm.security_result.rule_labels.  
\- event.idm.read_only_udm.security_result.rule_name.  
\- event.idm.read_only_udm.target.asset.ip.  
\- event.idm.read_only_udm.target.ip.  
\- event.idm.read_only_udm.target.port.  
\- event.idm.read_only_udm.target.url.   
2026-01-22 |  Enhancement:  
\- Modified a Grok pattern to parse the new format of logs.   
2025-12-23 |  Enhancement:  
\- Added a new Grok pattern to parse the new format of logs.   
2025-11-27 |  Enhancement:  
\- event.idm.read_only_udm.target.file.mime_type: Newly mapped `FileType` raw log field to `event.idm.read_only_udm.target.file.mime_type` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `SHA_Disposition`, `ThreatScore`, `SperoDisposition`, `ArchiveSHA256`, `ArchiveFileName`, `ArchiveDepth` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-11-19 |  Enhancement:  
\- Corrected the key name for `Revision` raw log field from `Singnature_Version` to `Signature_Version`.  
\- Added a new grok pattern to parse `intermediary.hostname` correctly.   
2025-10-27 |  Enhancement:  
\- Parser overhaul version to make it more efficient and increase fields coverage. You can see the full list of changes in the parser documentation page https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-firepower-firewall.   
2025-10-23 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `access_group` and `access_group_id` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `prin_location` raw log field to `event.idm.read_only_udm.principal.location.name`.  
\- `event.idm.read_only_udm.target.location.name`: Newly mapped `dst_location` raw log field to `event.idm.read_only_udm.target.location.name`.  
\- event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `syslog_priority` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.   
2025-10-17 |  Enhancement:  
\- Added a new Grok pattern to parse new log format.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `device_ids` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `src_ip` raw log field with event.idm.read_only_udm.principal.ip UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `src_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `tar_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `tar_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- The date filter was updated to support an additional timestamp format (yyyy-MM-ddTHH:mm:ssZZ).   
2025-10-06 |  Enhancement:  
\- Modified grok patterns in the message and message2 fields to support new log formats, extracting fields such as timestamp, action_type, scope, category1, category2, id, name, policyOwner, prin_user, and command_line.  
\- Conditionally mapped `srcuser` to `event.idm.read_only_udm.principal.user.userid` only if `prin_user` is absent.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp` raw log field to event.idm.read_only_udm.metadata.event_timestamp.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `action_type` raw log field to event.idm.read_only_udm.security_result.action_details.  
\- event.idm.read_only_udm.principal.resource.id: Newly mapped `id` raw log field to event.idm.read_only_udm.principal.resource.id.  
\- event.idm.read_only_udm.principal.resource.name: Newly mapped `name` raw log field to event.idm.read_only_udm.principal.resource.name.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `srcuser` raw log field to event.idm.read_only_udm.principal.user.user_display_name.  
\- event.idm.read_only_udm.principal.process.command_line: Newly mapped `command_line` raw log field to event.idm.read_only_udm.principal.process.command_line.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `path` raw log field to event.idm.read_only_udm.principal.process.file.full_path.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `ip` raw log field to event.idm.read_only_udm.principal.ip.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `scope` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `category1`, `category2` raw log field to event.idm.read_only_udm.security_result.category_details.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `policyOwner` raw log field to event.idm.read_only_udm.principal.resource.attribute.labels.   
2025-09-30 |  Enhancement:  
\- event.idm.read_only_udm.principal.nat_ip: Newly mapped `src_nat_ip` raw log field with `event.idm.read_only_udm.principal.nat_ip` UDM field.  
\- event.idm.read_only_udm.principal.nat_port: Newly mapped `src_nat_port` raw log field with `event.idm.read_only_udm.principal.nat_port` UDM field.  
\- event.idm.read_only_udm.target.nat_ip: Newly mapped `dst_nat_ip` raw log field with `event.idm.read_only_udm.target.nat_ip` UDM field.  
\- event.idm.read_only_udm.target.nat_port: Newly mapped `dst_nat_port` raw log field with `event.idm.read_only_udm.target.nat_port` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `interface`,`dest_interface` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added a new Grok pattern to parse `session_id` and `protocol` raw log fields.  
\- event.idm.read_only_udm.network.session_id: Mapped `session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.network.ip_protocol: Mapped `protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.   
2025-09-26 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `eventID` raw log field with event.idm.read_only_udm.metadata.product_event_type UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `src_pid` raw log field with event.idm.read_only_udm.principal.process.pid UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `src_component` raw log field with event.idm.read_only_udm.principal.resource.attribute.labels UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `target_application` raw log field with event.idm.read_only_udm.target.application UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `target_ip` raw log field with event.idm.read_only_udm.target.ip UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `target_ip` raw log field with event.idm.read_only_udm.target.asset.ip UDM field.  
\- `event.idm.read_only_udm.intermediary.application`: Newly mapped `inter_application` raw log field with event.idm.read_only_udm.intermediary.application UDM field.  
\- `event.idm.read_only_udm.intermediary.process.pid`: Newly mapped `inter_pid` raw log field with event.idm.read_only_udm.intermediary.process.pid UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `StatsSec`, `EventsRead`, `EventsSent`, `JSONEventsDropped`, `BundlesSent`, `PerSec`, `AckWaitSec`, `SysCPUSec`, `UserCPUSec`, `Count`, `Number_of_rows`, `Find_failures`, `status` and `Find_success` raw log fields with event.idm.read_only_udm.additional.fields UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `msg_description` raw log field with event.idm.read_only_udm.metadata.description UDM field.   
2025-09-25 |  Enhancement:  
\- Added a new Grok pattern to parse `message1` raw log field properly.  
\- event.idm.read_only_udm.intermediary.ip: Removed mapping of `int_IP1`, `int_IP2` and `int_IP3` raw log fields from `event.idm.read_only_udm.intermediary.ip` UDM field when `eventId` is `713041` and `713050` in order to introduce a more accurate mapping for the raw log fields.  
\- event.idm.read_only_udm.target.ip: Newly mapped `int_IP1` raw log field with `event.idm.read_only_udm.target.ip` UDM field when `eventId` is `713041`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `int_IP2` raw log field with `event.idm.read_only_udm.principal.ip` UDM field when `eventId` is `713041`.  
\- event.idm.read_only_udm.target.nat_ip: Newly mapped `int_IP3` raw log field with `event.idm.read_only_udm.target.nat_ip` UDM field when `eventId` is `713041`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `crypto_map`, `interface` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field when `eventId` is `713041`.  
\- event.idm.read_only_udm.target.nat_ip: Newly mapped `int_IP1` raw log field with `event.idm.read_only_udm.target.nat_ip` UDM field when `eventId` is `713050`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `int_IP2` raw log field with `event.idm.read_only_udm.principal.ip` UDM field when `eventId` is `713050`.  
\- event.idm.read_only_udm.target.ip: Newly mapped `int_IP3` raw log field with `event.idm.read_only_udm.target.ip` UDM field when `eventId` is `713050`.   
2025-09-21 |  Enhancement:  
\- Converted `priority` raw log field type to string.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `appname` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `facility`, `proc_id` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `message` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.priority_details: Newly mapped `priority` raw log field with `event.idm.read_only_udm.security_result.priority_details` UDM field.  
\- event.idm.read_only_udm.principal.process.file.names: Newly mapped `process_name` raw log field with `event.idm.read_only_udm.principal.process.file.names` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `process_id` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.   
2025-09-17 |  Enhancement:  
\- Added a Grok pattern to parse new syslog format.  
\- event.idm.read_only_udm.security_result.action: Newly mapped auth_status raw log field(s) with event.idm.read_only_udm.security_result.action UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped session_type raw log field(s) with event.idm.read_only_udm.target.application UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If message contains Authentication: successful and username_Id is not empty, updated to USER_LOGIN.  
\- event.idm.read_only_udm.security_result.action_details: Populated with a static string `Authentication successful` or `Authentication failed` based on the value of the auth_status field.  
\- event.idm.read_only_udm.extensions.auth.type: Set to a static value `VPN` if the message field contains `Authentication: successful` and the username_Id field is present.   
2025-08-18 |  Enhancement:  
\- Added a grok pattern to parse `principal.ip`.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `AccessControlRuleReason` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `Client` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `IPSCount`, `ConnectionDuration` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ReferencedHost` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.   
2025-08-11 |  Enhancement:  
\- event.idm.read_only_udm.security_result.severity: Newly mapped CRITICAL raw log field with event.idm.read_only_udm.security_result.severity UDM field when severity is 0.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped INFORMATIONAL raw log field with event.idm.read_only_udm.security_result.severity UDM field when severity is 7.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped Emergency: System is unusable raw log field with event.idm.read_only_udm.security_result.severity_details UDM field when severity is 0.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped Debugging: Debugging messages raw log field with event.idm.read_only_udm.security_result.severity_details UDM field when severity is 7.  
\- event.idm.read_only_udm.security_result.severity: Removed mapping of `INFORMATIONAL` from `event.idm.read_only_udm.security_result.severity` UDM field and mapped `HIGH` instead when severity is 1.  
\- event.idm.read_only_udm.security_result.severity: Removed mapping of `INFORMATIONAL` from `event.idm.read_only_udm.security_result.severity` UDM field and mapped `LOW` instead when severity is 4.  
\- event.idm.read_only_udm.security_result.severity_details: Removed mapping of `Immediate action needed` from `event.idm.read_only_udm.security_result.severity_details` UDM field and mapped `Alert: Immediate action needed` instead when severity is 1.  
\- event.idm.read_only_udm.security_result.severity_details: Removed mapping of `Critical condition` from `event.idm.read_only_udm.security_result.severity_details` UDM field and mapped `Critical: Critical conditions` instead when severity is 2.  
\- event.idm.read_only_udm.security_result.severity_details: Removed mapping of `Error condition` from `event.idm.read_only_udm.security_result.severity_details` UDM field and mapped `Error: Error conditions` instead when severity is 3.  
\- event.idm.read_only_udm.security_result.severity_details: Removed mapping of `Warning condition` from `event.idm.read_only_udm.security_result.severity_details` UDM field and mapped `Warning: Warning conditions` instead when severity is 4.  
\- event.idm.read_only_udm.security_result.severity_details: Removed mapping of `Normal but significant condition` from `event.idm.read_only_udm.security_result.severity_details` UDM field and mapped `Notice: Normal but significant condition` instead when severity is 5.  
\- event.idm.read_only_udm.security_result.severity_details: Removed mapping of `Informational message only` from `event.idm.read_only_udm.security_result.severity_details` UDM field and mapped `Informational: Informational messages only` instead when severity is 6.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped EventPriority, PrefilterPolicy, ClientAppDetector raw log field(s) with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.network.sent_packets: Mapped InitiatorPackets raw log field to event.idm.read_only_udm.network.sent_packets UDM field.  
\- event.idm.read_only_udm.network.received_packets: Mapped ResponderPackets raw log field to event.idm.read_only_udm.network.received_packets UDM field.  
\- event.idm.read_only_udm.principal.nat_port: Mapped NAT_InitiatorPort raw log field to event.idm.read_only_udm.principal.nat_port UDM field.  
\- event.idm.read_only_udm.target.nat_port: Mapped NAT_ResponderPort raw log field to event.idm.read_only_udm.target.nat_port UDM field.  
\- event.idm.read_only_udm.principal.nat_ip: Mapped NAT_InitiatorIP raw log field to event.idm.read_only_udm.principal.nat_ip UDM field.  
\- event.idm.read_only_udm.target.nat_ip: Mapped NAT_ResponderIP raw log field to event.idm.read_only_udm.target.nat_ip UDM field.  
\- event.idm.read_only_udm.principal.asset.attribute.labels: Mapped InstanceID, IngressVRF, EgressVRF raw log fields to event.idm.read_only_udm.principal.asset.attribute.labels UDM field.   
2025-08-05 |  Enhancement:  
\- Added support for syslogs with eventId `199018` by adding a new Grok pattern.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `src_user1` log field to `event.idm.read_only_udm.principal.user.userid` and set `has_user` to `true`.  
\- Added a condition to set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when `has_user` is `true`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `srcip` log field to `event.idm.read_only_udm.principal.ip`.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `srcip` log field to `event.idm.read_only_udm.principal.asset.ip`.  
\- Concatenated `month`, `day` and `year` and `time` log fields to map with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-07-18 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Removed the mapping of `event.idm.read_only_udm.principal.user.userid` by adding new grok pattern to avoid parsing dns data as user data.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Removed the mapping of `event.idm.read_only_udm.principal.user.user_display_name` by adding new grok pattern to avoid parsing dns data as user data.  
\- `event.idm.read_only_udm.network.dns.questions.name`: Newly mapped `dns_question` raw log field to `event.idm.read_only_udm.network.dns.questions.name`.   
2025-07-16 |  Enhancement:  
\- Added support for SYSLOG format with `kernel` messages by adding a new Grok pattern.  
\- Enhanced date filter to separately handle formats having `year` data.  
\- Added grok pattern to parse `product`, `severity`, and `eventID` from src_app.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `eventID` log field to `event.idm.read_only_udm.metadata.product_event_type`.  
\- Added grok pattern to parse `Reg` and `Value` from `sec_desc` field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `kernel_value` log field to event.idm.read_only_udm.additional.fields.  
event.idm.read_only_udm.additional.fields: Newly mapped `Reg` log field to event.idm.read_only_udm.additional.fields.  
event.idm.read_only_udm.additional.fields: Newly mapped `Value` log field to event.idm.read_only_udm.additional.fields.   
2025-07-01 |  Enhancement:  
\- Added Grok pattern to correctly extract the value of `intermediary_ip` or `syslog` fields from the raw log.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `ConnectionID` raw log field to `event.idm.read_only_udm.network.session_id`.  
\- Added a null check conditional for `sysloghost` field in `cisco_firepower_firewall_normalization.include` file.   
2025-04-03 |  Enhancement:  
\- `event.idm.read_only_udm.network.http.user_agent`: Mapped `UserAgent` to `event.idm.read_only_udm.network.http.user_agent`.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Mapped `UserAgent` to `event.idm.read_only_udm.network.http.parsed_user_agent`.  
\- Modified the `message1` field by replacing all occurrences of `Prefilter Policy` with `Prefilter_Policy`.   
2025-03-19 |  Enhancement:  
\- Modified the Grok pattern to parse data to their respective mappings.   
2025-02-25 |  Enhancement:  
\- Removed `is_alert` functionality from UDM mapping to avoid the discrepancy in the number of `ingested` events vs `normalized` events.   
2025-02-14 |  Enhancement:  
\- Added `on_error` to fix the parsing errors.   
2025-02-07 |  Enhancement:  
\- Changed mapping for `hostname` from `principal.hostname` and `principal.asset.hostname` to `intermediary.hostname` and `intermediary.asset.hostname`.  
\- Modified mapping from `intermediary.ip` to `target.ip`.   
2025-01-30 |  Enhancement:  
\- Added a new Grok pattern to parse the unparsed logs   
2025-01-23 |  Enhancement:  
\- Mapped `event_id` to `additional.fields`.   
2025-01-22 |  Enhancement:  
\- Added support for new pattern of syslog logs.   
2025-01-16 |  Enhancement:  
\- Added `gsub` to support the new JSON log formats.   
2025-01-03 |  Enhancement:  
\- Added support for the parsing of `ASA` logs, which were previously not being parsed.  
\- Added a new Grok pattern to parse new log types.   
2024-12-06 |  Enhancement:  
\- Added support for a new pattern of syslog logs.  
\- Mapped `path` to `principal.process.file.full_path`.  
\- Mapped `event_name` to `metadata.product_event_type`.  
\- Mapped `description` to `metadata.description`.  
\- Mapped `host` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `srcuser` to `principal.user.userid` and `user_display_name` , and set `metadata.event_type` to `USER_UNCATEGORIZED`  
\- Mapped `src_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `src_port` to `principal.port`.   
2024-12-05 |  Enhancement:  
\- Added support for a new pattern of JSON logs.   
2024-11-28 |  Enhancement:  
\- Added support for a new pattern of syslog logs.  
\- Mapped `username2` to `target.user.userid`.  
\- Mapped `pwd` to `target.file.full_path`.  
\- Mapped `command` to `target.process.command_line`.   
2024-11-13 |  Enhancement:  
\- Added support for new pattern of syslog logs.  
\- Mapped `username` to `principal.user.userid`.  
\- Mapped `action` to `metadata.ingestion_labels`.  
\- Mapped `bytes_transferred` to `network.sent_bytes`.   
2024-11-06 |  Enhancement:  
\- Added support for new pattern of syslog logs.   
2024-11-05 |  Enhancement:  
\- Added support to parse a new format of syslog logs.   
2024-08-13 |  Enhancement:  
\- Added support to parse a new format of unparsed KV logs.   
2024-08-08 |  Enhancement:  
\- Added support to parse a new format of unparsed logs.   
2024-07-15 |  Enhancement:  
\- Added support to parse the unparsed logs with `eventId` as `106016`, `302021`, and `302020`.   
2024-07-08 |  Enhancement:  
\- Added validation before setting the `metadata.event_type` to `FILE_CREATION` and `FILE_UNCATEGORIZED`.  
\- When `SrcIP` and `DstIP` are not null, set `metadata.event_type` to `NETWORK_CONNECTION`.   
2024-06-28 |  Enhancement:  
\- Changed mapping for `InitiatorBytes` from `network.received_bytes` to `network.sent_bytes`.  
\- Changed mapping for `ResponderBytes` from `network.sent_bytes` to `network.received_bytes`.   
2024-06-11 |  Enhancement:  
\- Modified a Grok pattern to parse the intermediary hostname.   
2024-04-12 |  Enhancement:  
\- Mapped `HTTP_Hostname` to `target.resource.attribute.labels`.  
\- Mapped `HTTP_URI` to `target.resource.attribute.labels`.  
\- When `InlineResult` is nearly equal to `Alert`, then set `security_result.action` to `ALLOW`.  
\- When `InlineResult` is nearly equal to `Dropped`, then set `security_result.action` to `BLOCK`.  
\- Mapped `InlineResult` to `security_result.action_details`.   
2024-04-06 |  Enhancement -  
\- Added a Grok pattern to parse the unparsed logs with `eventId` as `302022`.  
\- Changed mapping of `metadata.product_event_type` from `eventId` to `action`.  
\- Changed mapping of `InitiatorBytes` from `network.received_bytes` to `network.sent_bytes`.   
2024-01-04 |  Enhancement:  
\- Added support for SFAUDIT syslog logs.  
\- Mapped `user_id_field` to `principal.user.userid`.  
\- Mapped `http_method` to `network.http.method`.  
\- Mapped `HTTPReferer` to `network.http.referral_url`.  
\- Mapped `HTTPResponse` to `network.http.response_code`.  
\- Mapped `event_name` to `metadata.product_event_type`.  
\- Mapped `event_description` to `metadata.description`.  
\- Mapped `event_summary` to `security_result.summary`.  
\- Added Grok patterns to parse `intermediary.hostname` properly for new pattern of syslog logs.  
\- When `sysloghost` is a valid IP, then mapped it to `intermediary.ip`.  
\- Added support for JSON logs.  
\- Mapped `userId` to `principal.user.userid`.  
\- Mapped `sourceIpAddress` to `principal.ip`.  
\- Mapped `sourcePortOrIcmpType` to `principal.port`.  
\- Mapped `@computed.sensor` to `principal.hostname`.  
\- Mapped `@computed.user` to `principal.user.user_display_name`.  
\- Mapped `@computed.clientApplication` to `principal.application`.  
\- Mapped `@computed.ingressInterface` to `principal.asset.attribute.labels`.  
\- Mapped `@computed.sourceIpCountry` to `principal.location.country_or_region`.  
\- Mapped `destinationIpAddress` to `target.ip`.  
\- Mapped `destinationPortOrIcmpType` to `target.port`.  
\- Mapped `@computed.destinationIpCountry` to `target.location.country_or_region`.  
\- Mapped `ipProtocolId` to `network.ip_protocol`.  
\- Mapped `httpResponse` to `network.http.response_code`.  
\- Mapped `@computed.applicationProtocol` to `network.application_protocol`.  
\- Mapped `ruleId` to `security_result.rule_id`.  
\- Mapped `priorityId` to `security_result.priority_details`.  
\- Mapped `@computed.priority` to `security_result.priority`.  
\- Mapped `@computed.firewallPolicy` to `security_result.rule_name`.  
\- Mapped `@computed.message` to `security_result.threat_name`.  
\- Mapped `iocNumber` to `security_result.detection_fields`.  
\- Mapped `recordLength` to `security_result.detection_fields`.  
\- Mapped `@computed.classificationDescription` `security_result.description`.  
\- Mapped `@computed.recordTypeDescription` to `metadata.description`.  
\- Mapped `@computed.recordTypeCategory` to `metadata.product_event_type`.   
2023-12-26 |  Enhancement -  
\- Added a Grok pattern to parse the unparsed logs of type `%FTD-6-302303`.  
\- Added an on_error for a kv block.   
2023-09-12 |  Enhancement -  
\- Mapped `user_name` to `principal.user.email_addresses` and `client_ip` to `principal.ip` for `metadata.product_event_type` = `716001`.  
\- Added a Grok pattern to parse the unparsed logs where `product` = `Intrusion`.   
2023-08-08 |  Bug-Fix -  
\- Added a Grok pattern to map the complete value present in the raw log to `intermediary.hostname`.   
2023-06-15 |  Enhancement -  
\- Added support for JSON format logs.   
2023-06-07 |  Enhancement -  
\- Added new Grok pattern and mapped fields accordingly to parse unparsed logs.   
2023-05-03 |  Enhancement -  
\- Modified Grok pattern to parse the failing logs.  
\- Corrected the logic to correctly map `network.direction` to the values `INBOUND` and `OUTBOUND`.   
2023-04-19 |  Enhancement -  
\- Modified g=Grok pattern to get valid hostname.   
2023-04-06 |  Enhancement -  
\- Added a Grok pattern and mappings for EventId 106006.   
2023-03-09 |  Enhancement -  
\- Mapped hostname form Syslog header to `intermediary.hostname`.  
\- Removed mapping of src_ip/src_host to `observer.ip`/`observer.hostname`.  
\- Added new grok patterns and mappings for EventIds 106001, 302015, 302016, 713219, 302013, 305012, 305011.  
\- Mapped severity to `security_result.severity` and `security_result.severity_details`.  
\- Modified `metadata.event_type` to `NETWORK_CONNECTION` where `eventId` is 305011,305012,607001,302303.  
\- Mapped `network.direction` to INBOUND/OUTBOUND based on `src_interface_name`, `dst_interface_name`.  
\- Mapped `src_interface_name`,`dst_interface_name` to `metadata.ingestion_labels`.  
\- Added check to `ApplicationProtocol` prior mapping to UDM.   
2023-02-27 |  Enhancement  
\- Added Grok patterns and mappings for EventIds 302016,302014.   
2023-01-27 |  Enhancement  
\- Mapped `observer.hostname`,`observer.ip` for thees product_event_type 430002,430003,430004,430005.  
\- Modified grok patterns for these EventIds 721018, 722055, 722023, 113009, 722037 to parse data correctly.   
2022-11-25 |  Enhancement  
\- Added grok pattern for product_event_type [199017].  
\- Mapped `AUTH_VIOLATION` to security_result.category for product_event_type [199017].  
\- Mapped `USER_LOGIN` and `STATUS_UPDATE` event_type for product_event_type [199017].  
\- Mapped `target.user.userid` for product_event_type [199017].  
\- Mapped `extensions.auth.auth_details` for product_event_type [199017].  
\- Added grok pattern and `on_error` for product_event_type [713902].  
\- Modified `event_description` mapping for product_event_type [713902].  
\- Added `on_error` in grok for product_event_type [713903].   
2022-07-07 |  Enhancement  
\- Removed is_alert where product_event_type is [430002,430003,313005,419002].  
\- Added is_alert where product_event_type is 430005.   
2022-06-27 |  Mapped the following unparsed events:  
[1:1000171:1] (Nmap), [122:1:1] (Portscan), [122:2:1] (Portscan), [122:8:1] (Portscan), [122:19:1] (Portsweep), [122:21:1] (Portscan), [122:22:1] (Portscan), [122:23:1], (Portsweep), [122:24:1] (Portscan), [122:7:1] (Portsweep),LOGSTASH[-].  
Mapped `category` to `security_result.threat_name` where eventId is `http_inspect`.  
Mapped `category` to `security_result.threat_name` where eventId is `0` and product is `SFIMS`.  
Mapped `Classification` to `security_result.threat_name` where eventId is `430001`.  
Mapped `DeviceUUID` to `principal.resource.id` where eventId is `430001`.   
2022-06-09 |  Bug-  
Added new field mapping. ACPolicy mapped to `security_result.rule_labels`.  
Removed field name from `security_result.confidence_details` value.  
Removed field name from `security_result.rule_name` value.   
2022-05-20 |  Bug-Fixed an error where SFIMS product logs were not being parsed.   
2022-05-05 |  Enhancement-Moved customer specific to default and fixed incorrectly parsed metadata.event_timestamp.   
2022-04-22 |  Enhancement-Fixed incorrectly parsed metadata.event_timestamp.   
2022-04-13 |  Enhancement- mapped metadata.event_timestamp correctly for some unparsed logs   
2022-04-04 |  Enhancement- Zones, interfaces, policy, user, bytes, Urlcategory and urlreputation fields are mapped.   
2022-03-22 |  Enhancement-IngressZone,EgressZone,Priority,GID,SID,Revision,IntrusionPolicy fields are mapped.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
