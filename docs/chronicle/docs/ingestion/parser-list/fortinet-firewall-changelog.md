---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-firewall-changelog/
title: Change log for FORTINET_FIREWALL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:33.756537+00:00
---

# Change log for FORTINET_FIREWALL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-firewall-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FORTINET_FIREWALL

Date | Changes  
---|---  
2026-07-24 |  \- **`network.session_duration.seconds`**: Limited to maximum allowed value (315576000000 seconds) to prevent invalid duration errors. Any value equal to or above this will be mapped to 315576000000 as a limit.   
2026-07-22 |  \- **`metadata.product_event_type`**: Append the raw log field `eventtype` into `metadata.product_event_type` when the `type`, `subtype` and `eventtype` are present in the log.  
\- **`additional.fields`**: Mapped `type` raw log field with `additional.fields` UDM field.  
\- **`additional.fields`**: Mapped `subtype` raw log field with `additional.fields` UDM field.  
\- **`additional.fields`**: Mapped `eventtype` raw log field with `additional.fields` UDM field.   
2026-07-15 |  \- **`target.user.userid`**: Newly mapped `user` raw log field with `target.user.userid` UDM field for `event` type and `wireless` subtype for specific logid values (43573, 43629, 43630, 43636, 43637, 43638, 43675, 43677, 43678, 43712, 43713, 43714, 43575).  
\- **`target.user.attribute.labels`**: Newly mapped `user` raw log field with `target.user.attribute.labels` UDM field for `event` type and `wireless` subtype when specific logid values (43573, 43629, 43630, 43636, 43637, 43638, 43675, 43677, 43678, 43712, 43713, 43714, 43575) are not matched.  
\- **`principal.mac`**: Newly mapped `stamac` raw log field with `principal.mac` UDM field for `event` type and `wireless` subtype.  
\- **`metadata.event_type`**: Introduced specific event type mappings (`NETWORK_DHCP`, `NETWORK_DNS`, `USER_LOGIN`, and `USER_LOGOUT`) for `event` logs with `wireless` subtype based on `logid` values, and added a fallback to `NETWORK_UNCATEGORIZED` for remaining `wireless` subtype events.   
2026-07-07 |  \- **`extensions.auth.auth_type`**: Newly mapped `method` raw log field with `extensions.auth.auth_type` UDM field as ENUM `SSO` when `method` is `sso`.  
\- **`extensions.auth.auth_details`**: Newly mapped `method` raw log field with `extensions.auth.auth_details` UDM field when `method` is not `sso`.  
\- **`metadata.event_type`**: Modified the parser logic to prevent overriding `metadata.event_type` to `SCAN_UNCATEGORIZED` for system subtype logs.   
2026-06-19 |  \- **`metadata.event_type`**: Optimized the conditions for setting `metadata.event_type` to `USER_LOGIN`.   
2026-06-04 |  \- **`metadata.event_type`**: Mapped `metadata.event_type` to `USER_LOGIN` for successful logons when `action` is `NTLM-auth` and `status` is `success`.  
\- **`metadata.event_type`**: Mapped `metadata.event_type` to `NETWORK_CONNECTION` when `type` is `event` and `subtype` is either `ha` or `security-rating` as these are related to network events for fortinet firewall product.   
2026-05-25 |  \- **`intermediary.hostname`**: Mapped `devname` raw log field with `intermediary.hostname` UDM field. Retaining the duplicate mapping of `devname` to `intermediary.hostname` when `type=event` and `subtype=system`.  
\- **`principal.resource.attribute.labels`**: Removed mapping of `unauthuser` from `principal.resource.attribute.labels` UDM field.  
\- **`principal.user.attribute.labels`**: Mapped `unauthuser` raw log field with `principal.user.attribute.labels` UDM field if it is not already mapped to `principal.user.userid`. As `principal.user.attribute.labels` is a more specific field for user information.  
\- **`security_result.rule_labels`**: Removed direct mapping of `poluuid` from `security_result.rule_labels` UDM field to make sure `policyid` takes precedence.  
\- **`security_result.rule_labels`**: Mapped `poluuid` raw log field with `security_result.rule_labels` UDM field when `policyid` is not equal to `0` to serve as a secondary supporting attribute.  
\- **`security_result.detection_fields`**: Mapped `severity` raw log field with `security_result.detection_fields` UDM field to retain the severity value.  
\- **`extensions.auth.auth_type`**: Removed mapping of `domainctrlauthtype` from `extensions.auth.auth_type` UDM field.  
\- **`extensions.auth.auth_details`**: Mapped `domainctrlauthtype` raw log field with `extensions.auth.auth_details` UDM field.  
\- **`network.application_protocol`**: Added support for `LDAP` as a valid `service` value in `network.application_protocol` UDM field.  
\- **`principal.artifact.last_https_certificate`**: Removed mapping of `clientcert` from `principal.artifact.last_https_certificate` UDM field.  
\- **`principal.asset.attribute.labels`**: Mapped `clientcert` raw log field with `principal.asset.attribute.labels` UDM field.   
2026-05-08 |  \- event.idm.read_only_udm.metadata.event_type: Mapped `metadata.event_type` to `USER_LOGIN` for successful, attempted, failed, unknown and timed-out logons based on the following conditions: if `action` is `NEGO-auth` and `status` is `success` or if `action` is `unknown` or if `status` is `failure` or `timed_out`.   
2026-04-16 |  \- Updated the field mapping for the FORTINET_FIREWALL parser.  
\- Please refer to the parser documentation page for information regarding the updated UDM mappings - https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-firewall#udm_refresher_mapping_delta   
2026-02-01 |  \- security_result.severity: Hardcoded `severity` mappings based on logid are no longer used in the fortinet_firewall_mapping.include file. This change allows the main parser logic to dynamically determine `severity`.  
\- security_result.severity: The parser prioritizes the `severity` field from the raw log to set the UDM `security_result.severity` field. If the `severity` field is not present, the parser checks the following fields in the following precedence: crlevel, deviceSeverity, fsaverdict, and infectedfilelevel. As a final fallback, the level field is used to determine security_result.severity.   
2026-01-19 |  \- Support new SYSLOG + KV format in FORTINET_FIREWALL parser.  
\- intermediary.hostname: Added a new grok pattern to handle logs with an ISO8601 timestamp and a different structure. Enhanced the handling of the `fortihost` field to map it to `intermediary_temp.hostname` if it's not an IP address.   
2025-12-18 |  \- Updated the precedence of conditions written on `logid` raw log field.   
2025-12-10 |  Enhancement:  
\- event.idm.read_only_udm.principal.ip: Newly mapped `remip` raw log field to `event.idm.read_only_udm.principal.ip`.  
\- event.idm.read_only_udm.metadata.event_type: The conditions for setting `NETWORK_CONNECTION` or `NETWORK_UNCATEGORIZED` for logs where type is `event` and subtype is `vpn` have been modified. The logic now includes a check if `has_principal` is `true` as part of determining if principal information is present.   
2025-12-09 |  \- principal.hostname: Removed mapping of `authserver` from `principal.hostname` UDM field.  
\- principal.asset.hostname: Removed mapping of `authserver` from `principal.asset.hostname` UDM field.  
about.hostname: Mapped `authserver` raw log field with `about.hostname` UDM field   
2025-11-28 |  \- intermediary.ip: Removed mapping of `gateway` from `intermediary.ip` UDM field.  
target.ip: Mapped `gateway` raw log field with `target.ip` UDM field   
2025-11-14 |  \- Updating the mapping of `remip` and `locip` to ensure the fields correctly reflect the roles of Initiator (or Principal) and Responder (or Target) based on the Direction (dir) of the VPN connection.  
1) Update Field Mapping - change the UDM field  
\- The mappings for `remip` (remote client IP) and `locip` (FortiGate public IP) have been updated to be conditional based on the `dir` field:  
\- `locip`:  
\- Removed mapping from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.  
\- If `dir` is `outbound`:  
\- `locip` maps to `event.idm.read_only_udm.principal.ip`  
\- `locip` maps to `event.idm.read_only_udm.principal.asset.ip`  
\- If `dir` is not present or have any other value:  
\- `locip` maps to `event.idm.read_only_udm.target.ip`  
\- `locip` maps to `event.idm.read_only_udm.target.asset.ip`  
\- `remip`:  
\- Removed mapping from `event.idm.read_only_udm.src.ip` and `event.idm.read_only_udm.src.asset.ip`.  
\- If `dir` is `outbound`:  
\- `remip` maps to `event.idm.read_only_udm.target.ip`  
\- `remip` maps to `event.idm.read_only_udm.target.asset.ip`  
\- If `dir` is not present or have any other value:  
\- `remip` maps to `event.idm.read_only_udm.principal.ip`  
\- `remip` maps to `event.idm.read_only_udm.principal.asset.ip`  
\- The mapping for `event.idm.read_only_udm.metadata.event_type` when `type` is `event` and `subtype` is `vpn` has been updated:  
\- Mapped to `NETWORK_CONNECTION` if the `action` field is `tunnel-up` or `tunnel-down`.  
\- Mapped to `NETWORK_UNCATEGORIZED` if the `action` field has any other value.  
2) Delete Field Mapping  
\- Removed the previous static mapping of `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` when `type` is `event` and `subtype` is `vpn`.  
3) Other Updates  
\- The parser logic now incorporates the `dir` field to more accurately represent the roles of IP addresses (principal vs. target) based on the traffic direction (inbound/outbound) relative to the FortiGate device.   
2025-11-04 |  \- Added support for JSON logs parsing where the log content resides in the `attributes.message` field.   
2025-10-31 |  \- intermediary.ip: Removed mapping of `forwardedfor` raw log field from `intermediary.ip` UDM field as it now correctly populates `principal.ip` to represent the true client source and avoid duplicate assets.  
\- principal.ip: Added mapping of `forwardedfor` raw log field with `principal.ip` UDM field and in the presence of `forwardedfor` raw log field, `srcip` raw log fields mapped with `principal.nat_ip` from `principal.ip`  
\- Added a condition to ensure the network.ip_protocol UDM field is not overwritten by values from other protocol-related fields.  
\- target.resource.attribute.labels: Removed Mapping of `dsthwvendor` raw log field from `target.resource.attribute.labels` UDM field and mapped it to the UDM field `target.asset.hardware.manufacturer` as it is a more specific field to identify the hardware manufacturer of the destination device.  
\- target.asset.hadware.manufacturer: Mapped `dsthwvendor` raw log field with `target.asset.hadware.manufacturer` UDM field.  
\- additional.fields: Removed Mapping of `srcserver` raw log field from `additional.fields` UDM field which is now mapped to `principal.asset.attribute.labels` for better association with the source asset.  
\- principal.asset.attribute.labels: Mapped `srcserver` raw log field with `principal.asset.attribute.labels` UDM field.  
\- security_result.detection_fields: Removed Mapping of `policyid` and `poluuid` raw log field from `security_result.detection_fields` UDM field which are now mapped to the UDM field `security_result.rule_labels` which is a more appropriate field for associating events with the policy rules that generated them.  
\- security_result.rule_labels: Mapped `policyid` and `poluuid` raw log field with `security_result.rule_labels` UDM field.   
2025-10-29 |  \- Updated the grok pattern to extract the `device name`.   
2025-10-21 |  \- security_result.severity: Mapped the `security_result.severity` UDM field to `LOW` for Severity `Notice`  
\- security_result.severity: Mapped the `security_result.severity` UDM field to `INFORMATIONAL` for Severity `information` or `info` or `Debug`  
\- security_result.severity: Mapped the `security_result.severity` UDM field to `ERROR` for Severity `Error`  
2025-09-30 |  \- This is a new Premium version for the FORTINET_FIREWALL (FortiGate) parser.  
\- For the configuration details along with the list mapping which were changed in comparison to the existing default parser, please check the parser documentation page https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/default-parser-configuration#premium-parsers   
2025-09-09 |  Enhancement:  
event.idm.read_only_udm.additional.fields: Newly mapped total, used, interface raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.   
2025-08-21 |  Enhancement:  
\- If date, time, and tz fields are all present and not empty, they are combined to form a logtime string. This logtime string is then parsed to include the timezone offset, using the format yyyy-MM-dd HH:mm:ss Z.  
\- Added date filter to handle the timezones properly.  
\- event.idm.read_only_udm.security_result.summary: Removed mapping of the raw msg field from the event.idm.read_only_udm.security_result.summary UDM field, as this was causing redundant mapping.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `changes` raw log field with the event.idm.read_only_udm.security_result.description UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `action`,`lograte`,`msgrate`,`logratelimit`,`logratepeak`,`disk2usage`,`memusage`,`diskusage`,`userfrom`,`cpuusage` raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.   
2025-08-18 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped msg raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.  
\- The logic to map the raw msg field to event.idm.read_only_udm.additional.fields was moved to a more general section of the configuration. This will cause it to be applied to a broader range of event types.   
2025-08-12 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped sn, ap, vap, ssid, radioid, signal, snr, channel, security, encryption, snprev, remotewtptime raw log fields with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.principal.mac: Newly mapped stamac raw log field with event.idm.read_only_udm.principal.mac UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped reason raw log field with event.idm.read_only_udm.security_result.description UDM field.   
2025-07-31 |  Enhancement:  
\- Added a Grok pattern to parse the `msg` raw log field to extract `ip`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `tz`, `psrcport`, `pdstport`, `service`, `addr`, `audittime`, `auditscore`, `sync_type`, `Eventsubtype` and `sync_status` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-07-24 |  Enhancement:  
\- Added a GROK pattern to parse the `msg` raw log field correctly.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `principalip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `principal_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `msg` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-07-09 |  Enhancement:  
\- event.idm.read_only_udm.security_result.action: Removed mapping of `action` from `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.security_result.action: Mapped `utmaction` raw log field with `event.idm.read_only_udm.security_result.action` UDM field  
\- event.idm.read_only_udm.additional.fields: Newly mapped `countips`, `countapp` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.platform: Newly mapped `dstosname` raw log field with `event.idm.read_only_udm.target.platform` UDM field.   
2025-06-05 |  Enhancement:  
\- Added support for a new pattern of (SYSLOG + KV) logs by adding a gsub block.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `vwlid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-05-29 |  Enhancement:  
\- Modified Grok pattern's to parse the required data.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `device_id` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field  
\- event.idm.read_only_udm.metadata.description: Newly mapped `desc` raw log field with `event.idm.read_only_udm.metadata.description` UDM field  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `remote_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `remote_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field  
\- event.idm.read_only_udm.security_result.rule_version: Newly mapped `srchwversion` and `dsthwversion` raw log field with `event.idm.read_only_udm.security_result.rule_version` UDM field  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `pri` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field. If `pri` is equal to `alert` then map `event.idm.read_only_udm.security_result.severity` to `CRITICAL`  
\- event.idm.read_only_udm.additional.fields: Newly mapped `shapingpolicyid` , `shaperdropsentbyte` , `shapersentname` , `shapingpolicyname` , `shaperdroprcvdbyte` and `shaperrcvdname` raw log field with `event.idm.read_only_udm.additional.fields` UDM field  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `srcfamily` and `srchwvendor` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field   
2025-05-21 |  Enhancement:  
\- event.idm.read_only_udm.target.ip: Removed mapping of `remip` from `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Removed mapping of `remip` from `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.src.ip: Mapped `remip` raw log field with `event.idm.read_only_udm.src.ip` UDM field.  
\- event.idm.read_only_udm.extensions.auth.type: Mapped `VPN` with `event.idm.read_only_udm.extensions.auth.type` UDM field when `subtype` is `vpn`.   
2025-05-19 |  Enhancement:  
\- Moved mutate block which was converting `rcvdpkt` to an integer above the if block.  
\- Added else block to handle the case where `rcvdpkt` is greater than 0.   
2025-05-15 |  Enhancement:  
\- Moved mapping of `eventtime`, `timestamp`, `syslogtime`, `start` and `logtime` outside the else block to make it accessible for both if and else cases.   
2025-04-30 |  Enhancement:  
\- event.idm.read_only_udm.security_result.action: Extended value mapping for raw field action to treat `client-rst` and `server-rst` as ALLOW actions.  
\- event.idm.read_only_udm.security_result_2.description: Newly mapped action raw log field with event.idm.read_only_udm.security_result_2.description UDM field.  
\- event.idm.read_only_udm.security_result_2.action_details: Newly mapped action raw log field with event.idm.read_only_udm.security_result_2.action_details UDM field.  
\- security_result_2_action: Newly mapped from raw utmaction and action values when utmaction matches block and action matches accept or close.  
\- When type is `traffic` and subtype is `forward` and action matches timeout (case-insensitive), security_result_action is set to ALLOW.  
\- When type is `traffic`, subtype is `local`, action matches timeout (case-insensitive), and rcvdpkt is greater than or equal to 0, security_result_action is also set to ALLOW.  
\- Added a mutate block to convert rcvdpkt to an integer with error tagging (rcvdpkt_not_integer) if conversion fails.  
\- Added `block` to the list of values mapped as BLOCK actions.  
\- Separated timeout actions into a distinct conditional block to ensure consistent BLOCK mapping where applicable.  
\- Implemented conditional logic for utmaction + action scenarios to build a secondary security result (security_result_2):  
\- Populates security_result_2_action as ALLOW.  
\- Populates security_result_2.action_details and description from action.  
\- Merges security_result_2 into event.idm.read_only_udm.security_result.  
\- Updates the main security_result_action to BLOCK, and sets security_result.description and action_details using utmaction   
2025-04-25 |  Enhancement:  
\- event.idm.read_only_udm.principal.asset.hardware.serial_number: Removed mapping of `devid` from `event.idm.read_only_udm.principal.asset.hardware.serial_number` UDM field where `type` is not equal to `event` and `subtype` is not equal to `system`.  
\- event.idm.read_only_udm.intermediary.asset.hardware.serial_number: Newly mapped `devid` raw log field with `event.idm.read_only_udm.intermediary.asset.hardware.serial_number` UDM field.   
2025-04-24 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `status` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-04-22 |  Enhancement:  
\- When `level` is `notice`, then removed `security_result.severity` from `MEDIUM`.  
\- When `level` is `notice`, then set `security_result.severity` to `LOW`.   
2025-03-21 |  Enhancement:  
\- Added a check to fix the parsing issue for KV logs.   
2025-03-18 |  Enhancement:  
\- Mapped `sproc` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `metadata.event_type` to `DEVICE_CONFIG_UPDATE` when `logdesc` is `Configuration changed` or `Object attribute configured` and `message` has `Edit firewall.policy` or `Add firewall.policy`.  
\- Mapped `metadata.event_type` to `USER_UNCATEGORIZED` when `logdesc` is `User changed`.  
\- Mapped `metadata.event_type` to `USER_CREATION` when `logdesc` is `Local user added`.  
\- Mapped `metadata.event_type` to `USER_CHANGE_PASSWORD` when `logdesc` is `Object attribute configured` and `message` has `password`.   
2025-02-28 |  Enhancement:  
\- Added support to separate fields in `cfgattr` and mapped to `additional.fields`.   
2025-02-27 |  Enhancement:  
\- Mapped `deviceExternalId` to `about.asset.asset_id` for new pattern of logs.   
2025-02-24 |  Enhancement:  
\- Mapped `dstname` to `target.hostname`.  
\- Mapped `saddr` to `principal.ip`.   
2025-02-18 |  Enhancement:  
\- When `action` is `clear_session`, then mapped `security_result.action` to `BLOCK`.   
2025-01-31 |  Enhancement:  
\- Changed mapping for `remip` from `principal.ip` to `target.ip`.   
2025-01-24 |  Enhancement:  
\- If srcip is associated with a user interface (UI) or SSH traffic, then mapped srcip to `principal.ip`.   
2025-01-20 |  Enhancement:  
\- Mapped `ui`, `cfgpath`, `cfgobj`, `cfgattr`, and `msg` to `additional.fields`.   
2025-01-08 |  Enhancement:  
\- When type=`event` and subtype=`vpn`, then mapped `metadata.event_type` to `STATUS_UPDATE`.  
\- When type=`event` subtype=`vpn`, and action= `tunnel-stats`, then mapped `metadata.event_type` to `NETWORK_UNCATEGORIZED`.   
2025-01-01 |  Enhancement:  
\- Replaced `devid` in `target.user.userid` with `principal.asset.hardware.serial_number`.   
2024-12-20 |  Enhancement:  
\- Rearranged the GROK pattern.  
\- Added GROK pattern to parse new type of logs.   
2024-12-04 |  Enhancement:  
\- Mapped `ipaddr` to `network.dns.answers`.  
\- Mapped `fortihost` to `intermidiary.ip`.   
2024-11-28 |  Enhancement:  
\- Mapped `metadata.event_type` to `USER_CREATION` when `action` is `Add`.  
\- Mapped `metadata.event_type` to `USER_DELETION` when `action` is `Delete`.  
\- Mapped `metadata.event_type` to `DEVICE_CONFIG_UPDATE` when `action` is `Edit`.  
\- Changed mapping for `devid` from `security_result.detection_fields` to `target.user.userid`.   
2024-11-27 |  Enhancement:  
\- If `utmaction` is present, mapped `action` to `security_result_1.action_details`.   
2024-11-21 |  Enhancement:  
\- Changed mapping for `msg` from `metadata.description` to `security_result.summary`.  
\- Mapped `logdesc` to `metadata.description`.   
2024-11-08 |  Enhancement:  
\- Mapped `ui` to `principal.ip` and `principal.asset.ip`.   
2024-10-15 |  Enhancement:  
\- Mapped `type`, `subtype`, and `level` to `additional.fields`.   
2024-09-20 |  Enhancement:  
\- When `dstosname` is equal to `DEBIAN`, set `target.platform` to `LINUX`.   
2024-09-19 |  Enhancement:  
\- When `service` is `kernel`, removed the drop tag.  
\- Mapped `mac` to `principal.mac`.   
2024-09-13 |  Enhancement:  
\- Added a conditional check for `ssl-login-fail` and `auth-logon` before mapping the `security_result.action` UDM field value.   
2024-08-29 |  Enhancement:  
\- If `action` is `negotiate`, then set `security_result.action` to `BLOCK`.  
\- If `action` is `tunnel-down`, `tunnel-stats`, `tunnel-up`, and `ssl-new-con`, then set `security_result.action` to `ALLOW`.  
\- If `action` is nearly equal to `tunnel` or `action` is `negotiate`, then set `metadata.event_type` to `NETWORK_CONNECTION`.   
2024-08-16 |  Enhancement:  
\- Changed the mapping of `security_result.action` from `FAIL` to `BLOCK` when `action` is `timeout`.   
2024-08-13 |  Enhancement:  
\- Mapped `logid` to `metadata.product_log_id`.  
\- Mapped `vd` to `principal.administrative_domain`.  
\- Mapped `srcintfrole` to `security_result.detection_fields`.  
\- Mapped `dstintfrole` to `security_result.detection_fields`.  
\- Mapped `sentpkt`, `rcvdpkt`, `vpntype`, `authserver`, `crlevel`, `trandisp`, `policyid`, and `appcat` to `additional.fields`.  
\- Mapped `policytype` to `security_result.rule_type`.  
\- Mapped `craction` to `security_result.about.labels`.  
\- Mapped `crscore` to `security_result.severity_details`.  
\- Mapped `group` to `principal.user.group_identifiers`.   
2024-08-06 |  Enhancement:  
\- Mapped `auditid`, `auditscore`, `auditid`, `criticalcount`, `highcount` , `mediumcount`, `lowcount`, `passedcount`, `criticalcount`, `srccountry`, `direction`, `dstcountry`, `dstintf`, `dstintfrole`, `xid`, `qtype`, `qtypeval`, `qclass`, `cat`, `rcode` and `license_limit` to `security_result.detection_fields`.  
\- Mapped `cpu`, `mem`, `disk`, `bandwidth`, `disklograte`, `fazlograte`, `freediskstorage`, `sysuptime`, `waninfo`, `trandisp`, `used_for_type`, `connection_type`, `count` and `fctuid` to `additional.fields`.  
\- Mapped `totalsession` to `network.session_duration.seconds`.  
\- Mapped `incidentserialno` to `network.tls.client.certificate.serial`.  
\- Mapped `scertcname` to `network.tls.client.certificate.subject`.  
\- Mapped `scertissuer` to `network.tls.client.certificate.issuer`.  
\- Mapped `authserver` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `dstserver` and `dst_host` to `target.hostname` and `target.asset.hostname`.  
\- Mapped `dsthwvendor` to `target.resource.attribute.labels`.  
\- Mapped `eventtime` to `metadata.event_timestamp`.  
\- Mapped `reqtype`, `rcvdbyte`, `ratemethod`, `outintf`, `cookies`, `useralt`, `xauthuser`, `xauthgroup`,  
`assignip`, `vpntunnel`, `init`, `stage`, `role`, `advpnsc`, `tunneltype`, `tunnelid` and `nextstat` to `principal.resource.attribute.labels`.  
\- Mapped `policyid` to `security_result.rule_id`.  
\- Mapped `policytype` to `security_result.rule_type`.  
\- Mapped `date`,`time` and `tz` to `metadata.ingested_timestamp`.  
\- Mapped `profile` to `target.resource.name` and `target.resource.resource_type`.  
\- If `user` is a valid ip, then mapped `user` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `group` to `principal.user.group_identifiers`.  
\- Mapped `mode` to `security_result.summary`.  
\- Mapped `result` to `security_result.description`.   
2024-07-29 |  Enhancement:  
\- Added a conditional check for the `success` field before mapping `security_result.action` UDM field.   
2024-07-17 |  Enhancement:  
\- Added `gsub` to parse unparsed syslog logs.   
2024-07-02 |  Enhancement:  
\- Mapped `FTNTFGTappcat` to `additional.fields`.  
\- Mapped `FTNTFGTduration` to `network.session_duration.seconds`.  
\- Mapped `FTNTFGTsentpkt` to `additional.fields` and `network.sent_packets`.  
\- Mapped `FTNTFGTrcvdpkt` to `additional.fields` and `network.received_packets`.  
\- Mapped `FTNTFGTdstintfrole` to `security_result.detection_fields`.  
\- Mapped `FTNTFGTsrcintfrole` to `security_result.detection_fields`.  
\- Mapped `FTNTFGTpoluuid` to `security_result.rule_id`.  
\- Mapped `FTNTFGTvd` to `principal.administrative_domain`.   
2024-05-21 |  Enhancement:  
\- Added `gsub` to parse JSON logs.   
2024-04-19 |  Enhancement:  
\- `Mapped correct `shost` value to `principal.hostname` by adding gsub function for `fw_version` field.`  
Bug-fix:  
\- Added support for logs that don't have `jsonPayload.message` field.   
2024-03-07 |  Enhancement:  
\- Mapped `httpmethod` to `network.http.method`.  
\- Mapped `agent` to `network.http.user_agent` and `network.http.parsed_user_agent`.  
\- Aligned mappings for `principal.ip` and `principal.asset.ip`.  
\- Aligned mappings for `principal.hostname` and `principal.asset.hostname`.  
\- Aligned mappings for `target.ip` and `target.asset.ip`.  
\- Aligned mappings for `target.hostname` and `target.asset.hostname`.   
2023-11-21 |  Bug-Fix:  
\- Mapped `dstuser` to `event.idm.read_only_udm.target.user.userid`.  
\- Mapped `dstauthserver` to `event.idm.read_only_udm.target.hostname`.  
\- Mapped `poluuid` to `event.idm.read_only_udm.additional.fields`.  
\- Mapped `srcuuid` to `event.idm.read_only_udm.principal.resource.product_object_id`.  
\- Mapped `dstuuid` to `event.idm.read_only_udm.target.resource.product_object_id`.  
\- Mapped `attack` to `event.idm.read_only_udm.security_result.category_details`.  
\- If `type` value is `utm` and `subtype` value is `waf`, changed `event.idm.read_only_udm.metadata.event_type` from `NETWORK_UNCATEGORIZED` to `NETWORK_CONNECTION`.  
\- If `direction` value is `request`, set `event.idm.read_only_udm.network.direction` to `OUTBOUND`.  
\- If `direction` value is `response`,set `event.idm.read_only_udm.network.direction` to `INBOUND`.   
2023-11-20 |  Bug-fix:  
\- Mapped `transip` to `principal.nat_ip`.  
\- Mapped `transport` to `principal.nat_port`.  
\- Mapped `tranport` to `target.nat_port`.   
2023-07-10 |  Enhancement -  
\- Parsed raw logs of type `Added FTP Server`.   
2023-06-01 |  Enhancement - Mapped `log_id` to `metadata.product_log_id`.  
\- Mapped `operation` to `security_result.action_details` and `security_result.action` to `ALLOW`.  
\- Mapped `performed_on` to `security_result.about.application`.  
\- Mapped `path` to `security_result.description`.  
\- Mapped `pri` to `security_result.severity_details`.  
\- Mapped `mode` to `security_result.summary`.  
\- Mapped `desc` to `metadata.description`.  
\- Mapped `userfrom` to `principal.ip`.   
2023-05-24 |  Enhancement -  
\- Mapped `severity` to `security_result.detection_fields`.   
2023-04-19 |  Enhancement - Mapped `srcinetsvc` and `dstinetsvc` to `security_result.detection_fields`.   
2023-03-06 |  Enhancement - when `type` = `event` and `subtype` = `vpn` mapped -  
\- `event_type` to `USER_LOGIN`.  
\- `extensions.auth.type` to `VPN`.  
\- `devname` to `target.hostname`.  
\- Mapped `action` to `security_result.action` if present else mapped `utmaction`. Initially it was done vice versa.   
2023-02-22 |  \- Mapped `metadata.event_type` as `USER_UNCATEGORIZED` instead of `GENERIC_EVENT` when `user` field is present.  
\- Mapped `msg` to `security_result.summary`.  
\- Mapped `nas` to `principal.nat_ip`.  
\- Modified grok to parse data for `target.user.userid` when `logdesc` contains `GUI_ENTRY_DELETION`.   
2023-01-13 |  \- Mapped `shost` to `principal.hostname`.   
2022-11-24 |  Enhancement - Mapped `tranip` to `target.nat_ip`.  
\- Modified the mapping of `msg` from `security_result.description` to `security_result.summary`.   
2022-10-21 |  Enhancement:  
\- Mapped `suser` to `principal.user.user_display_name`.  
\- Mapped `duser` to `target.user.user_display_name`.  
\- Mapped `suid` to `principal.user.userid`.  
\- Mapped `duid` to `target.user.userid`.   
2022-10-20 |  Bug:  
\- `security_result.action` mapping changed from `BLOCK` to `ALLOW` when `action=close`.   
2022-10-13 |  Enhancement:  
\- Changed Mapping for `metadata.event_type` from `GENERIC_EVENT` to `USER_DELETION` when `logdesc` is `GUI_ENTRY_DELETION`  
\- Mapped `msg` to `security_result.description`  
\- Mapped `devname` to `principal.hostname`  
\- Mapped `user_name` to `target.user.userid`  
\- Mapped `level` to `security_result.severity_details`  
2022-10-06 |  Bug-Fix:  
\- Added conditional check for the field `utmaction` and `action`.  
\- Mapped the field `utmaction` to security_result.action if present, else mapped the field `action`.   
2022-09-21 |  Enhancement:  
\- Mapped the field `protocol` to `network.ip_protocol` if protocol contains tcp and udp else mapped it to `network.application_protocol`.  
\- Added gsubs and enhanced the parser to parse the logs of CEF format having different field names.   
2022-09-09 |  Enhancement:  
\- Migrated customer specific parsers to default parser.  
\- Added support for logs with CEF format.  
\- Mapped the field `cs6` to `principal.user.group_identifiers`.  
\- Mapped the field `start` to `metadata.event_timestamp`.  
\- Mapped the field `dvchost` to `intermediary.hostname`.  
\- Mapped the field `dhost` to `target.hostname`.  
\- Mapped the field `src` to `principal.ip`.  
\- Mapped the field `spt` to `principal.port`.  
\- Mapped the field `sourceTranslatedAddress` to `principal.nat_ip`.  
\- Mapped the field `sourceTranslatedPort` to `principal.nat_port`.  
\- Mapped the field `dst` to `target.ip`.  
\- Mapped the field `dpt` to `target.port`.  
\- Mapped the field `out` to `network.sent_bytes`.  
\- Mapped the field `in` to 'network.received_bytes.  
\- Mapped the field `deviceSeverity` to `security_result.severity`.  
\- Mapped the field `act` to `security_result.action` and `security_result.action_details`.  
\- Mapped the field `sentpkt` to `additional.fields`.  
\- Mapped the field `rcvdpkt` to `additional.fields`.  
\- Added conditional null checks for fieldsout `metadata.product_name`, `metadata.vendor_name`, `sentbyte`, `rcvdbyte`, `intermediary`.  
\- Modified the field `metadata.event_type` for the following cases:  
\- `GENERIC_EVENT` to `NETWORK_UNCATEGORIZED` where principal.ip and target.ip is not null.  
\- `GENERIC_EVENT` to `STATUS_UNCATEGORIZED` where principal.ip is not null.   
2022-08-22 |  Enhancement:  
\- Added support for logs with CEF format.  
\- Mapped the field `vd` to `principal.administrative_domain`.  
\- Mapped the field `status` to `security_result.summary`.  
\- Mapped the field `msg` to `security_result1.description`.  
\- Mapped the field `ip_address` to `principal.ip` where the field `msg` is present.  
\- Removed mapping for the field `devname` mapped to `principal.hostname`.   
2022-08-11 |  Enhancement:  
\- The field `app` is mapped to `additional.fields[n]`.  
\- Added null condition check for the field `remip`.   
2022-07-21 |  Enhancement:  
\- Modified mapping for `group` from `principal.user.groupid` to `principal.user.group_identifiers`.   
2022-07-13 |  Enhancement: Added mappings for new fields.  
Mapped `appcat` to event.idm.read_only_udm.additional.fields".  
Mapped `apprisk` to event.idm.read_only_udm.additional.fields".  
Mapped `applist` to event.idm.read_only_udm.additional.fields".  
Mapped `appact` to event.idm.read_only_udm.additional.fields".  
Mapped `devid` to event.idm.read_only_udm.additional.fields".   
2022-06-20 |  Enhancement- Mapped `security_result.action` as `ALLOW` when the value of field `action` or `utmaction` is `detected`.   
2022-05-20 |  Enhancement: Added mappings for new fields;  
Mapped `action` and `utmaction` to `security_result.action_details`.  
Added validation checks for `principal.ip` and `target.ip`.   
2022-04-29 |  Enhancement-Added support for action = timeout/close to UDM.  
Mapped devname to principal.hostname when principal field is empty.   
2022-04-12 |  Enhancement-Added mappings for new fields.  
attackid mapped to security_result.rule_id  
crlevel mapped to security_result.severity  
incidentserialno mapped to metadata.product_log_id  
craction mapped to metadata.product_deployment_id  
dstintf mapped to additional.fields  
dstintfrole mapped to additional.fields   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
