---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sep-changelog/
title: Change log for SEP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:00.189437+00:00
---

# Change log for SEP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sep-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SEP

Date | Changes  
---|---  
2026-05-29 |  Enhancement:  
\- Added new grok patterns to parse the new format of syslog logs.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `vrCat` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `intermediary_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.   
2026-04-29 |  Enhancement:  
\- Added a new grok pattern to parse new format of syslog logs.  
\- Removed `has_target` as true when `event.idm.read_only_udm.target.asset_id` and `event.idm.read_only_udm.target.asset.asset_id` is not null as these fields don't come under the target machine details criteria.  
\- Removed `has_principal` as true when `event.idm.read_only_udm.principal.asset_id` and `event.idm.read_only_udm.principal.asset.asset_id` is not null as these fields don't come under the principal machine details criteria.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `COMMAND_ID`, `ATP_DEVICE_ID`, `DEVICE_INFO`, `pattern_idx`, `vrType`, `translation`, `locale` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.group.attribute.labels`: Newly mapped `group_type` raw log field with `event.idm.read_only_udm.target.group.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.group.group_display_name`: Newly mapped `group_name` raw log field with `event.idm.read_only_udm.target.group.group_display_name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `deleted`, `discovered`, `virusname_idx`, `stealth`, `vID`, `removal`, `performance`, `privacy`, `dependency`, `detection_type`, `dynacat`, `catDes` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `virusname` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `RemotePort` raw log field with `event.idm.read_only_udm.target.port` UDM field.   
2026-02-05 |  Enhancement:  
\- Added support to parse `security_result.action` as `BLOCK` when `security_result_action` is `TERMINATED`.   
2025-11-27 |  Enhancement:  
\- event.idm.read_only_udm.security_result.about.labels: Removed mapping of `custom_politica_infringida` raw log field from `event.idm.read_only_udm.security_result.about.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `custom_politica_infringida` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.about.labels: Removed mapping of `custom_incidente` raw log field from `event.idm.read_only_udm.security_result.about.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `custom_incidente` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.about.labels: Removed mapping of `connection.ether_type` raw log field from `event.idm.read_only_udm.security_result.about.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `connection.ether_type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.about.labels: Removed mapping of `feature_name` raw log field from `event.idm.read_only_udm.security_result.about.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `feature_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-10-29 |  Enhancement:  
\- event.idm.read_only_udm.target.hostname and event.idm.read_only_udm.target.asset.hostname: Removed mapping of `ServerName` from `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field when `logType` is similar to `Virus found` inorder to remove duplicate values.   
2025-08-21 |  Enhancement:  
\- Parser overhaul version to make it more efficient and increase fields coverage. You can see the full list of changes in the parser documentation page https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sep .   
2025-08-14 |  Enhancement:  
Added support to parse new format of json logs.  
Added Grok pattern to map the fields.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped facility, cids_signature_id1, cids_signature_subid, url_category, url_risk, intensive_protection_level raw log fields with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped local_host_ip raw log field with event.idm.read_only_udm.principal.ip UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped local_host_ip raw log field with event.idm.read_only_udm.principal.asset.ip UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped remote_host_name raw log field with event.idm.read_only_udm.target.hostname UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped remote_host_name raw log field with event.idm.read_only_udm.target.asset.hostname UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped event_description raw log field with event.idm.read_only_udm.metadata.description UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped user_name raw log field with event.idm.read_only_udm.principal.user.userid UDM field.  
\- event.idm.read_only_udm.principal.administrative_domain: Newly mapped domain_name raw log field with event.idm.read_only_udm.principal.administrative_domain UDM field.  
\- event.idm.read_only_udm.principal.location.city: Newly mapped location raw log field with event.idm.read_only_udm.principal.location.city UDM field.  
\- event.idm.read_only_udm.extensions.vulns.vulnerabilities: Newly mapped vuln raw log field with event.idm.read_only_udm.extensions.vulns.vulnerabilities UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped hostname raw log field with event.idm.read_only_udm.principal.hostname UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped hostname raw log field with event.idm.read_only_udm.principal.asset.hostname UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped remote_host_ip raw log field with event.idm.read_only_udm.target.ip UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped remote_host_ip raw log field with event.idm.read_only_udm.target.asset.ip UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped local_port raw log field with event.idm.read_only_udm.principal.port UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped remote_port raw log field with event.idm.read_only_udm.target.port UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped occurrences1 raw log field with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.target.mac: Newly mapped remote_host_mac raw log field with event.idm.read_only_udm.target.mac UDM field.  
\- event.idm.read_only_udm.target.asset.mac: Newly mapped remote_host_mac raw log field with event.idm.read_only_udm.target.asset.mac UDM field.  
\- event.idm.read_only_udm.principal.mac: Newly mapped local_host_mac raw log field with event.idm.read_only_udm.principal.mac UDM field.  
\- event.idm.read_only_udm.principal.asset.mac: Newly mapped local_host_mac raw log field with event.idm.read_only_udm.principal.asset.mac UDM field.  
\- event.idm.read_only_udm.target.file.sha256: Newly mapped sha256 raw log field with event.idm.read_only_udm.target.file.sha256 UDM field.  
\- event.idm.read_only_udm.target.process.file.md5: Newly mapped md5 raw log field with event.idm.read_only_udm.target.process.file.md5 UDM field.  
\- event.idm.read_only_udm.security_result: Newly mapped security_result raw log field with event.idm.read_only_udm.security_result UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped application_path raw log field with event.idm.read_only_udm.target.file.full_path UDM field.  
\- event.idm.read_only_udm.principal.file.full_path: Newly mapped application_path_2 raw log field with event.idm.read_only_udm.principal.file.full_path UDM field.  
\- Added a conditional null check for `domain_name` raw log field in the include file to remove null value for `event.idm.read_only_udm.intermediary.administrative_domain` UDM field.  
\- event.idm.read_only_udm.metadata.vendor_name: Newly mapped `Symantec` with event.idm.read_only_udm.metadata.vendor_name UDM field.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped `SEP` with event.idm.read_only_udm.metadata.product_name UDM field.   
2025-03-20 |  Enhancement:  
\- If `syslogServer` is not empty, then mapped `syslogServer` to `intermediary.hostname` else mapped `computer` to `intermediary.hostname`.   
2025-02-26 |  Enhancement:  
\- If `log_type` value is `REP`, and `syslogServer` value is not empty, then map `syslogServer` to `intermediary.hostname` else map `computer` to `intermediary.hostname`.   
2025-01-09 |  Enhancement:  
\- If `Actual action` value is `Left alone`, then changed mapping of `security_result.action` from `BLOCK` to `UNKNOWN_ACTION`.  
\- Changed mapping of `computer` from `intermediary.hostname` to `principal.hostname` and `principal.asset.hostname`.  
\- Changed mapping of `syslogServer` from `principal.hostname` to `intermediary.hostname`.   
2024-12-12 |  Enhancement:  
\- Added a Grok pattern to parse new format of syslog logs.  
\- Mapped `anvpap-srv1` to `intermediary.hostname`.  
\- Mapped `SymantecServer` to `principal.hostname`.  
\- Mapped `Remote Host Name` to `target.hostname`.  
\- Mapped `Remote Port` to `target.port`.  
\- Mapped `Remote Host IP` to `target.ip`.  
\- Mapped `Local Port` to `principal.port`.  
\- Mapped `Remote Host MAC` to `principal.mac`.  
\- Mapped `ICMP` to `network.ip_protocol`.  
\- Mapped `Inbound` to `network.direction`.  
\- Mapped `Application` to `principal.process.file.full_path`.  
\- Mapped `Rule` to `security_result.rule_name`.  
\- Mapped `Action` to `security_result.action`.  
\- Mapped `SHA-256` to `principal.process.file.sha256`.   
2024-11-21 |  Enhancement:  
\- Added `gsub` to parse new pattern of logs.  
\- Added a Grok pattern to `event_description` to parse the fields.  
\- Mapped `File` to `principal.process.file.full_path`.  
\- Mapped `Size` to `principal.process.file.size`.   
2024-11-07 |  Enhancement:  
\- Mapped `SITE_NAME` and `SOURCE` to `additional.fields`.  
\- Mapped `SOURCE` to `security_result.description`.   
2024-10-25 |  Enhancement:  
\- Mapped `SCAN_ID`, `CATEGORY_DESC`, `CLIENT_TYPE`, `DETECTION_TYPE`, `HELP_VIRUS_IDX`, `HPP_APP_TYPE`, `IDX`, `LAST_LOG_SESSION_GUID`, `SITE_TYPE`, `UUID`, `VBIN_ID`, and `VIRUS_TYPE` to `additional.fields`.  
\- Mapped `USER_DOMAIN_NAME` to `target.administrative_domain`.  
\- Mapped `COMPUTER_DOMAIN_NAME` to `principal.administrative_domain`.  
\- Mapped `IP_ADDR1` to `src.ip`.  
\- Mapped `SOURCE_COMPUTER_NAME` to `src.asset.hostname` and `src.hostname`.  
\- Mapped `COMPUTER_NAME` to `principal.asset.hostname` and `principal.hostname`.  
\- Mapped `OPERATION_SYSTEM` to `principal.asset.platform_software.platform`.  
\- Mapped `SERVICE_PACK` to `principal.asset.platform_software.platform_version`.  
\- Mapped `SOURCE_COMPUTER_IP` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `ALERT` to `metadata.product_event_type`.  
\- Mapped `USER_NAME` to `principal.user.userid`.  
\- Mapped `BIOS_SERIALNUMBER` to `principal.asset.hardware.serial_number`.  
\- Mapped `ACTUALACTION` to `security_result.action_details`.  
\- Mapped `VIRUSNAME` to `security_result.threat_name`.  
\- Mapped `NOOFVIRUSES` to `security_result.verdict_info.malicious_count`.  
\- Mapped `SOURCE`, `DESCRIPTION`, `REQUESTEDACTION` to `security_result.detection_fields`.  
\- Mapped `CLIENT_GROUP` to `principal.group.group_display_name`.  
\- Mapped `downloader` to `principal.process.file.full_path`.   
2024-10-24 |  Enhancement:  
\- Added support to parse logs with `logType` as `IPS`, `Network Intrusion Protection System`, `REP`, `Memory Exploit Mitigation System`, and `NTR`.   
2024-10-08 |  Enhancement:  
\- Added support for new format of syslog logs.   
2024-09-23 |  Enhancement:  
\- Changed mapping of `rule_name` from `principal.resource.name` to `security_result.rule_name`.  
\- Removed mapping of `principal.resource.resource_type` as `FIREWALL_RULE`.  
\- Changed mapping of `security_result.category` from `ACL_VIOLATION` to `UNKNOWN_CATEGORY`.   
2024-09-11 |  Enhancement:  
\- Added support for array-type logs.   
2024-08-08 |  \- Mapped `REQUESTEDACTION` to `security_result.action_details`.  
\- Mapped `SECONDARYACTION`, `ACTUALACTION`, `VIRUSNAME`, and `NOOFVIRUSES` to `security_result.detection_fields`.  
\- Mapped `SOURCE` to `additional.fields`.  
\- Mapped `HPP_APP_HASH` to `target.file.sha256`.  
\- Mapped `HPP_APP_NAME` to `target.file.names`.  
\- Mapped `FILEPATH` to `target.file.full_path`.  
\- Mapped `CLIENT_GROUP` to `target.user.group_identifiers`.   
2024-06-07 |  \- Added Support for KV format logs.   
2024-05-27 |  Enhancement:  
\- Mapped `target_file_name` from `target.file.full_path` to `target.file.names`.   
2023-11-28 |  Bug-Fix:  
\- When `event_time` present, mapped the same to `datetime`.   
2023-11-08 |  Bug-Fix:  
\- Removed mapping of `ServerName` to `target.asset.hostname` and mapped it to `intermediary.hostname`.  
\- When `Actualaction` is `Cleaned`, then mapped `security_result.action` to `BLOCK` and `is_significant` to `false`.  
\- Added Grok pattern to parse the unparsed logs with varying patterns.  
\- Mapped `type`, `utility-sub-type`, `lang`, `service-sandbox-type`, `mojo-platform-channel-handle`, `field-trial-handle`, `disable-features` to `security_result.detection_fields`.  
\- Mapped `target_arguments` to `read_only_udm.additional.fields`.  
\- Mapped `user-data-dir` to `sec_result.about.file.full_path`.  
\- Mapped `security-realm` to `security_result.summary`.  
\- Mapped `startup-url` to `principal.url`.  
\- Mapped `source_ip` to `target.ip`.  
\- Mapped `action_word` to `security_result.action_details`.   
2023-10-12 |  Bug-Fix:  
\- Added Grok pattern to parse the unparsed logs with varying patterns.   
2023-04-21 |  Bug-Fix:  
\- Changed intermediate variable names in the include files.  
\- Mapped `security_result.rule_name` for `File` related events.   
2023-04-10 |  Enhancement:  
\- Handled the dropped logs with the logType `File Read`, `File Write`, `File Delete`, or `Registry Write`.  
\- Mapped `payload.domain_name` to `principal.administrative_domain`.  
\- Added null check for `payload.device_id` and `event_description`.   
2023-01-21 |  Enhancement:  
\- Added conditional check for `targetComputerName`,`event_description1`.  
\- Added on_error check for `file_full_path`,`GroupName`,`ServerName`.  
\- Mapped `Applicationtype` to `principal.resource.attribute.labels`.  
\- Mapped `mail` to `target.user.email_addresses`.  
\- Mapped `server_name_1` to `principal.hostname`.  
\- For logtype `SEC`:  
\- Mapped `computer` to `principal.hostname`.  
\- Mapped `syslogServer` to `intermediary.hostname`.  
\- Mapped `event_description` to `metadata.description`.  
\- Added `for loop` for the logtype `SONAR`,`CVE`,`SEC`.   
2022-11-24 |  Enhancement:  
\- Added grok pattern to parse logs containaing `SONAR detection now allowed`.   
2022-11-15 |  Enhancement:  
\- Added grok pattern to parse failed logs of type `Virus Found` and `SONAR Scan`.  
\- Added conditional check for `Categorytype`.   
2022-10-25 |  Enhancement:  
\- Mapped `EventDescription` to `metadata.description`.  
\- Mapped `LocalHostIP`,`IPAddress`,`source_ip` to `principal.ip`.  
\- Mapped `LocalHostMAC` to `principal.mac`.  
\- Mapped `computer` to `principal.hostname`  
\- Mapped `guid` to `principal.asset.asset_id`.  
\- Mapped `DeviceID` to `principal.resource.product_object_id`.  
\- Mapped `Filesize` to `target.file.size`.  
\- Mapped `SHA256` to `target.file.sha256`.  
\- Mapped `User1` to `principal.user.userid`.  
\- Mapped `file_path` to `target.file.full_path`.  
\- Mapped `GroupName` to `principal.group.group_display_name`.  
\- Mapped `action_word` to `security_result.action_details`.  
\- Mapped `Begin` to `vulnerabilities.scan_start_time`.  
\- Mapped `EndTime` to `vulnerabilities.scan_end_time`.  
\- Mapped `ScanID` to `principal.process.product_specific_process_id`.  
\- Mapped `inter_host` to `intermediary.hostname`.  
\- Mapped `inter_ip` to `intermediary.ip`.  
\- Mapped `ActionType` to `additional.fields`.  
\- Mapped `Rule` to `security_result.rule_name`.   
2022-10-10 |  \- Mapped `category` to `security_result.category_details`.  
\- Mapped `CIDS Signature ID` to `target.resource.attribute.labels`.  
\- Mapped `CIDS Signature SubID` to `target.resource.attribute.labels`.  
\- Mapped `CIDS Signature string` to `target.resource.attribute.labels`.  
\- Mapped `Intrusion URL` to `principal.url`.  
\- Mapped `User Name` to `principal.user.userid`.  
\- Mapped `Actual action` to `security_result.action_details`.  
\- Mapped `Application hash` to `target.file.sha256`.  
\- Mapped `Application name` to `target.application`.  
\- Mapped `Application type` to `target.resource.attribute.labels`.  
\- Mapped `Certificate issuer` to `network.tls.server.certificate.issuer`.  
\- Mapped `Certificate serial number` to `network.tls.server.certificate.serial`.  
\- Mapped `Certificate signer` to `network.tls.server.certificate.subject`.  
\- Mapped `Certificate thumbprint` to `network.tls.server.certificate.sha256`.  
\- Mapped `Secondary action` to `target.resource.attribute.labels`.  
\- Mapped `First Seen` to `security_result.detection_fields`.  
\- Mapped `Risk Name` to `security_result.detection_fields`.  
\- Mapped `Risk Type` to `security_result.detection_fields`.  
\- Mapped `Permitted application reason` to `security_result.detection_fields`.  
\- Mapped `Company name` to `target.user.company_name`.  
\- Mapped `Computer name` to `principal.hostname`.  
\- Mapped `Server Name` to `principal.asset.network_domain`.  
\- Mapped `Confidence` to `security_result.description`.  
\- Mapped `Detection Type` to `security_result.summary`.  
\- Mapped `Group Name` to `principal.group.group_display_name`.  
\- Mapped `Risk Level` to `security_result.severity_details`.  
\- Mapped `File size (bytes)` to `target.file.size`.   
2022-09-21 |  Enhancement - Migrated custom parsers to default parser.   
2022-08-12 |  Enhancement - Modified grok pattern to parse the logs.  
Handled the dropped logs and mapped them to valid event_types.  
\- Dropped logs had following logType, which are now handled:  
`REP`, `SubmissionsMan`, `SYLINK`, `IPS`, `SONAR`, `SEC`, `CVE`, `LiveUpdate Manager; Messages related to definition updates`,  
`Antivirus detection submission`.  
\- New conditions `msg1` containing `Create Process|GUP|RebootManager|Smc|WSS|Network Intrusion|Mitigation System` are handled.  
\- event_description containing `client-server activity logs|Got a valid certificate.|Replication .*from remote site|The database|received the client log successfully`.  
\- Added new code block to handle the logType REP,SONAR,CVE,GUP,Smc,WSS made them parse.  
\- Changed event type from `GENERIC_EVENT` to `STATUS_UPDATE`, `USER_UNCATEGORIZED`, `NETWORK_CONNECTION`, `STATUS_UNCATEGORIZED` wherever possible.  
\- Mapped `eventDescription` to `metadata.description`.  
\- Mapped `hostName` to `principal.hostname`.  
\- Mapped `machineDomainName` to `principal.administrative_domain`.  
\- Mapped `domainName` to `target.administrative_domain`.  
\- Mapped `serverName` to `intermediary.hostname`.  
\- Mapped `userName` to `principal.user.userid`.  
\- Mapped `siteName` to `read_only_udm.additional.fields`.   
2022-07-26 |  for the logs that has messageTmp as Site mapped the following fields:  
\- Mapped `eventDescription` to `metadata.description`.  
\- Mapped `hostName` to `target.hostname`.  
\- Mapped `machineDomainName` to `target.administrative_domain`.  
\- Mapped `domainName` to `principal.administrative_domain`.  
\- Mapped `serverName` to `principal.hostname`.  
\- Mapped `userName` to `principal.user.userid`.  
\- Mapped `siteName` to `read_only_udm.additional.fields`.   
2022-05-11 |  Parsed Event Timestamp log entries with the format `yyyy-MM-dd HH:mm:ss`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
