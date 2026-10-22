---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-meraki-changelog/
title: Change log for CISCO_MERAKI \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:50.155615+00:00
---

# Change log for CISCO_MERAKI  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-meraki-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_MERAKI

Date | Changes  
---|---  
2026-08-26 |  Enhancement:  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `bssid`, `src_mac` raw log fields with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM field.  
\- `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac`: Newly mapped `wired_mac`, `dst_mac` raw log fields with `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `vlan_id`, `channel`, `rssi`, `fc_type`, `fc_subtype` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-06-25 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `decision` raw log field with `event.idm.read_only_udm.security_result.action` UDM field, sets the value to `ALLOW` when `decision` is `allow`.   
2026-06-08 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `decision` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `shost` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped the `direction` raw log field to the `event.idm.read_only_udm.network.direction` UDM field, sets the value to `OUTBOUND` when `direction` is `egress` and `INBOUND` when `direction` is `ingress`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-04-16 |  Enhancement:  
\- `event.idm.read_only_udm.target.mac`: Removed mapping of `mac` from `event.idm.read_only_udm.target.mac` UDM field for `dhcp no offers` events to map it to more appropriate UDM field.  
\- `event.idm.read_only_udm.principal.mac`: Mapped `mac` raw log field with `event.idm.read_only_udm.principal.mac` UDM field for `dhcp no offers` events.  
\- `event.idm.read_only_udm.network.dhcp.chaddr`: Newly mapped `mac` raw log field with `event.idm.read_only_udm.network.dhcp.chaddr` UDM field for `dhcp no offers` events.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `eventSummary` raw log field with `event.idm.read_only_udm.metadata.description` UDM field for `dhcp no offers` events.  
\- `event.idm.read_only_udm.network.dhcp.chaddr`: Newly mapped `clientMac` raw log field with `event.idm.read_only_udm.network.dhcp.chaddr` UDM field for `dhcp release` events.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_DHCP` for all dhcp events when has valid dhcp data.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the value of `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT` for all dhcp events when has no valid dhcp data.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `uplink` (key: `uplink`), `old_AutoVPN_port` (key: `old_AutoVPN_port`), `new_AutoVPN_port` (key: `new_AutoVPN_port`), `vpn_type` (key: `vpn_type`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-03-03 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `srcIp` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `srcport` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `destIp` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `destport` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `event.idm.read_only_udm.security_result.action` UDM field as `BLOCK` or `ALLOW` based on the value of `blocked` raw log field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `ruleId` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `module` (key: `module`), `classification` (key: `classification`), `version` (key: `version`), `sentAt` (key: `sentAt`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `data_message` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Setting `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` when `has_principal` is true and `has_target` is true.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Added support for `ts` raw log field to parse `event.idm.read_only_udm.metadata.event_timestamp` UDM field correctly.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `eventType` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.priority`: Updated the mapping logic for the `priority` raw log field to ensure it parse globally.  
\- `event.idm.read_only_udm.additional.fields`: Updated the mapping logic for the `signature` raw log field to ensure it parse globally.   
2025-12-22 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` : Removed `prinIP` raw log field mapping from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields. These are identified as additional IP as originating from the firewall rule not `src` for which the IP value is already mapped under `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_priority` and `syslog_version` raw log field to `event.idm.read_only_udm.additional.fields`.   
2025-12-11 |  Enhancement:  
\- Refactored the parsing of `event.idm.read_only_udm.network.ip_protocol` and `event.idm.read_only_udm.network.application_protocol` to use centralized include files (parse_ip_protocol.include, parse_app_protocol.include), which replaces extensive, hardcoded if/else logic.   
2025-11-11 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `organizationID`, `productType`, `category`, `ssidNumber`, `eventData.channel`, `eventData.rssi` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `deviceName` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `deviceName` raw log field to `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.   
2025-07-09 |  Enhancement:  
\- Added a grok patterns on `message` and on `msg1` to parse the fields.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `inter_ip` field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.principal.mac`, `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `mac_address` field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM field  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `port1` field with `event.idm.read_only_udm.principal.port` UDM field  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `description1`,`vlan1` field with `event.idm.read_only_udm.security_result.description` UDM field.   
2025-04-24 |  Enhancement:  
\- Added Grok patterns to parse the fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `sport` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dport` raw log field with `event.idm.read_only_udm.principal.port` UDM field  
\- `event.idm.read_only_udm.target.nat_port`: Newly mapped `dst_translated_port` raw log field with `event.idm.read_only_udm.target.nat_port` UDM field  
\- Added an if condition to check if `natDstIp` is not equal to `dstIp` then mapped:  
`event.idm.read_only_udm.target.nat_ip`: Newly mapped `natDstIp` raw log field with `event.idm.read_only_udm.target.nat_ip` UDM field.  
`event.idm.read_only_udm.target.ip`: Newly mapped `dstIp` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
`event.idm.read_only_udm.target.asset.ip`: Newly mapped `dstIp` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- Added a gsub function on `agent` raw log field to replace `@` with ''.  
\- Added a gsub function on `agent` raw log field to replace `\\*` with ''.  
\- `event.idm.read_only_udm.principal.mac`: Newly mapped `peer` raw log field with `event.idm.read_only_udm.principal.mac` UDM field.  
\- `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `peer` raw log field with `event.idm.read_only_udm.principal.asset.mac` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `packet`, `subnetMask`, `dnsServer1`, `dnsServer2`, `peer_type`, `connection_status` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `anchor` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `anchor` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `clientHostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `clientHostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `act` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `STATUS_UPDATE`: Added support for the event `STATUS_UPDATE` when `peer` raw log field is present.  
\- `STATUS_UPDATE`: Added support for the event `STATUS_UPDATE` when `anchor` raw log field is present.  
\- `STATUS_UPDATE`: Added support for the event `STATUS_UPDATE` when `has_principal` is true for logs with `eventSummary` as `dhcp release`.  
\- `STATUS_UPDATE`: Added support for the event `STATUS_UPDATE` when `has_principal` is true for logs with `eventSummary` as `Block` or `denied`.   
2024-12-05 |  Enhancement:  
\- When `protocol` is equal to `88` then set `network.ip_protocol` to `EIGRP`.  
\- When `protocol` is equal to `50` then set `network.ip_protocol` to `ESP`.  
\- When `protocol` is equal to `97` then set `network.ip_protocol` to `ETHERIP`.  
\- When `protocol` is equal to `47` then set `network.ip_protocol` to `GRE`.  
\- When `protocol` is equal to `1` then set `network.ip_protocol` to `ICMP`.  
\- When `protocol` is equal to `58` then set `network.ip_protocol` to `ICMP6`.  
\- When `protocol` is equal to `2` then set `network.ip_protocol` to `IGMP`.  
\- When `protocol` is equal to `41` then set `network.ip_protocol` to `IP6IN4`.  
\- When `protocol` is equal to `103` then set `network.ip_protocol` to `PIM`.  
\- When `protocol` is equal to `132` then set `network.ip_protocol` to `SCTP`.  
\- When `protocol` is equal to `6` then set `network.ip_protocol` to `TCP`.  
\- When `protocol` is equal to `17` then set `network.ip_protocol` to `UDP`.  
\- When `protocol` is equal to `112` then set `network.ip_protocol` to `VRRP`.  
\- When `protocol` is equal to `0` then set `network.ip_protocol` to `UNKNOWN_IP_PROTOCOL`.   
2024-10-04 |  Enhancement:  
\- Added the Grok pattern and conditional checks to parse unparsed `ip`, `userid`, `mac`, `bytes`, and `vlan`.  
\- Mapped `ip` to `principal.ip`.  
\- Mapped `userid` to `principal.userid`.  
\- Mapped `mac` to `principal.mac`.  
\- Mapped `bytes` to `network.sent_bytes`.  
\- Mapped `vlan` to `security_result.detection_fields`.   
2024-09-26 |  Enhancement:  
\- Added a Grok pattern to parse unparsed IP and mapped it to `target.ip`.   
2024-09-19 |  Enhancement:  
\- Mapped `networkName` to `principal.hostname`.  
\- Mapped `organizationName` to `principal.resource.name`.  
\- Mapped `organizationUrl` to `principal.resource.attribute.labels`.  
\- Mapped `networkTags`, `alertType`, `alertTypeId` , and `alertData.num` to `additional.fields`.  
\- Mapped "`networkId` to `network.session_id`.  
\- Mapped `networkUrl` to `network.http.referral_url`.  
\- Mapped `deviceMac` to `target.mac`.  
\- Mapped `deviceUrl` to `target.url`.  
\- Mapped `deviceModel` to `target.hardware.model`  
\- Mapped `alertLevel` to `security_result.severity`.   
2024-08-29 |  Enhancement:  
\- Added Grok pattern with a conditional check to parse the unparsed SYSLOG logs.   
2024-07-31 |  Enhancement:  
\- Removed the drop tag and added Grok pattern with a conditional check to parse unparsed logs.   
2024-06-19 |  Enhancement:  
\- Added a Grok pattern to parse unparsed logs.   
2024-03-19 |  Enhancement:  
\- Added a Grok pattern to map the sending device IP address to `intermediary.ip`.   
2024-02-06 |  Enhancement:  
\- Parsed logs where `eventSummary` is `cli_set_rad_parms` or `cli_set_rad_pmksa_parms`.  
\- Mapped `group` and `attr` to `additional.fields`.   
2023-12-26 |  Enhancement:  
\- Parsed logs containing `eventSummary` as `status changed` and `changed STP role`.   
2023-10-09 |  Enhancement:  
\- Set `sec_res.action` to `BLOCK` when `pattern` is in `1 all`, `deny all`, or `Group Policy Deny`.  
\- Set `sec_res.action` to `ALLOW` when `pattern` is in `0 all`, `allow all`, or `Group Policy Allow`.   
2023-07-19 |  Bug-Fix -  
Parsed unparsed syslog logs of type `firewall`.   
2023-07-14 |  Enhancement -  
\- for type `splash_auth` mapped `event_type` to `USER_LOGIN`.  
\- for type `device_packet_flood`, `packet_flood` mapped `event_type` to `GENERIC_EVENT`.  
\- for type `vpn_connectivity_change`, `wpa_deauth`, `wpa_auth` mapped `event_type` to `STATUS_UPDATE`.  
\- Mapped `agent` to `network.http.parsed_user_agent`.  
\- If `protocol` == `47` then mapped `network.ip_protocol` to `GRE`.  
\- If `protocol` == `103` then mapped `network.ip_protocol` to `PIM`.   
2023-07-04 |  Enhancement -  
\- Used key-value filters, instead of a Grok pattern, to parse the logs of type `urls`, `firewall`, `vpn_firewall`.   
2023-06-16 |  Enhancement -  
\- Mapped `src` to `principal.ip`  
\- Mapped `dst` to `target.ip`  
\- Mapped `protocol` to `network.ip_protocol`  
\- Mapped `sport` to `principal.port`  
\- Mapped `dport` to `target.port`  
\- Mapped `mac` to `principal.mac`.  
\- Mapped `pattern` to `security_result.description`.   
2023-06-09 |  Enhancement -  
\- Mapped `metadata.event_type` to `USER_LOGOUT` when `type` = `8021x_deauth`.  
\- Mapped `radio`,`vap`,`reason`,`is_8021x`,`instigator`,`band` to `additional.fields` for `type` = `disassociation`.   
2023-05-26 |  Enhancement -  
\- For type `security_filtering_file_scanned` modified `metadata.event_type` from `STATUS_UPDATE` to `SCAN_FILE`.  
\- Added Grok pattern to parse syslog logs.  
\- Mapped `ip` to `principal.ip`  
\- Mapped `mac` to `principal.mac`.   
2023-03-03 |  Enhancement -  
\- Added Grok pattern to parse logs which have the field `ip_flow_end`.  
\- Mapped `natsrcIp` mapped `principal.nat_ip`.  
\- Mapped `natsrcport` mapped `principal.nat_port`.   
2022-11-25 |  Enhancement -  
\- Added support for unparsed JSON logs, network_dns query logs and failing syslog+kv_data logs.  
\- Mapped `metadata.eventType` to RESOURCE_CREATION, FILE_UNCATEGORIZED, SETTING_MODIFICATION, NETWORK_UNCATEGORIZED,  
GROUP_UNCATEGORIZED, PROCESS_LAUNCH, PROCESS_TERMINATION, STATUS_UNCATEGORIZED, SYSTEM_AUDIT_LOG_UNCATEGORIZED,  
USER_LOGOUT, USER_LOGIN, RESOURCE_PERMISSIONS_CHANGE, USER_RESOURCE_ACCESS based on `EventID` for json logs.  
\- Mapped `DisabledPrivilegeList`, `EnabledPrivilegeList` to `target.user.attribute.permissions`.  
\- Mapped `GroupMembership` to `target.user.group_identifiers`.  
\- Mapped `AccessList` to `target.resource.attribute`.  
\- Mapped `auth_mechanism` to `extensions.auth.mechanism`.  
\- Mapped `question` to `network.dns.questions`.  
\- Set `security_result.priority` based on `priority` value.  
\- Mapped `RecordNumber` to `metadata.product_log_id`.   
2022-10-06 |  Enhancement -  
\- Mapped `dvc` to `intermediary.hostname`.  
\- Mapped `eventType` to `metadata.product_event_type`.  
\- Mapped `pattren` to `security_result.action_details`.  
\- Mapped `principalMac` to `principal.mac`.  
\- Mapped `principalIp` to `principal.ip`.  
\- Added null check for `dstIp` prior mapping to udm.   
2022-07-04 |  Enhancement -  
\- When `protocol` is equal to `47` then set `protocol` to `GRE`.  
\- When `protocol` is equal to `50` then set `protocol` to `ESP`.  
\- Added kv block when `eventType` is equal to `events`.  
\- Mapped `identity` to `target.user.userid`.  
\- Mapped `last_known_client_ip` to `principal.ip`.  
\- When `eventSummary` is equal to `association`.  
\- Mapped `client_ip` to `principal.ip`;  
\- Mapped `client_mac` to `principal.mac`.  
\- Mapped `rssi` to `intermediary.asset.product_object_id`.  
\- Mapped `channel` to `security_result.detection_fields`.  
\- Mapped `aid` to `network.session_id`.   
2022-06-15 |  Enhancement -  
\- Mapped `lastSeen`, `firstSeen`, `wiredLastSeen` to `security_result.detection_fields`.  
\- Mapped `wiredMacs` to `intermediary.mac`.  
\- Mapped `type` to `security_result.summary`.  
\- Mapped `description` to `security_result.description`.  
\- Mapped `deviceSerial` to `_target_hardware.serial_number`.  
\- Mapped `deviceName` to `target.hostname`.  
\- Mapped `ssidName`, `clientId`, `clientDescription` to `additional.fields`.  
\- Mapped `eventData.client_mac` to `principal.mac`.  
\- Mapped `eventData.identity` to `principal.hostname`.  
\- Mapped `eventData.aid` to `principal.asset_id`.  
\- Mapped `organizationId` to `principal.resource.id`.  
\- Mapped `eventData.group` to `principal.group.group_display_name`.  
\- Mapped `eventData.client_ip` to `principal.ip`.  
\- Mapped `occurredAt` to `metadata.event_timestamp`.   
2022-05-04 |  Enhancement - Added mapping for hostname.   
2022-04-13 |  Enhancement - Added parsing of logs of JSON type.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
