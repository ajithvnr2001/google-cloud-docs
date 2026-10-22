---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bitdefender-changelog/
title: Change log for BITDEFENDER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:31.978091+00:00
---

# Change log for BITDEFENDER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bitdefender-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for BITDEFENDER

Date | Changes  
---|---  
2026-09-02 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed the mapping of `BitdefenderGZMalwareHash` raw log field from `event.idm.read_only_udm.security_result.detection_fields` UDM field as `BitdefenderGZMalwareHash` raw log field has sha256 hash value.  
\- `event.idm.read_only_udm.principal.process.file.sha256`: Mapped `BitdefenderGZMalwareHash` raw log field with `event.idm.read_only_udm.principal.process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.target.user.company_name`: Newly mapped `BitdefenderGZCompanyName` raw log field with `event.idm.read_only_udm.target.user.company_name` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `syslog_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `start` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `BitdefenderGZTaskScanType`, `BitdefenderGZCleanedMalwareCnt`, `BitdefenderGZDeletedMalwareCnt`, `BitdefenderGZQuarantinedMalwareCnt`, `BitdefenderGZIgnoredMalwareCnt`, `BitdefenderGZPresentMalwareCnt`, `BitdefenderGZLicenseSlotsUsed`, `BitdefenderGZLicenseSlotsTotal`, `BitdefenderGZLicenseLimitReachedForCompany`, `BitdefenderGZLicenseLimitReachedForPartnerCompany`, `device_event_class_id`, `BitdefenderGZMalwareHash`, `cef_name` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `BitdefenderGZLicenseKey` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `appname` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- Added a grok pattern on `message` to extract `syslog_host`, `appname`.  
\- Modified a grok pattern to parse the raw log fields.  
\- Added a conditional check before the already existing mapping of `BitdefenderGZMalwareHash` to `event.idm.read_only_udm.principal.process.file.sha256`.   
2026-06-22 |  Enhancement:  
\- Added a grok pattern to parse SYSLOG+JSON format logs.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `name` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `created` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.user.company_name`: Newly mapped `company_name` raw log field with `event.idm.read_only_udm.target.user.company_name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `license_key`, `product_id`, `servers_used`, `servers_total` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `recv_for_his_company` and `recv_for_partner_company`, `endpointId` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If event is user related, then updated the value of `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `detection_username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.first_discovered_time`: Newly mapped `detection_time` raw log field with `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `driverPath` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `detection_technique` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `detection_pid` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.process.parent_process.pid`: Newly mapped `detection_parentPid` raw log field with `event.idm.read_only_udm.target.process.parent_process.pid` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `detection_path` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.parent_process.file.full_path`: Newly mapped `detection_parentPath` raw log field with `event.idm.read_only_udm.target.process.parent_process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `detection_commandLine` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `detection_action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.principal.user.windows_sid`: Newly mapped `detection_userSid` raw log field with `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Set `event.idm.read_only_udm.security_result.action` UDM field to `BLOCK` if `main_action` is `deny`.   
2025-10-30 |  Enhancement:  
\- Added support for JSON log format.  
\- event.idm.read_only_udm.principal.application: Newly mapped `appname` raw log field to `event.idm.read_only_udm.principal.application`.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `hostname` raw log field to `event.idm.read_only_udm.intermediary.hostname`.  
\- event.idm.read_only_udm.intermediary.asset.hostname: Newly mapped `hostname` raw log field to `event.idm.read_only_udm.intermediary.asset.hostname`.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `message` raw log field to `event.idm.read_only_udm.metadata.description`.  
\- event.idm.read_only_udm.metadata.event_type: Newly mapped `meta_event_type` raw log field to `event.idm.read_only_udm.metadata.event_type` for the newly added JSON format logs.  
\- Added validation to ensure fields (`hash`, `BitdefenderGZMalwareHash`, `file_hash_sha256`) are valid SHA256 hashes before mapping them to `event.idm.read_only_udm.principal.process.file.sha256` or `event.idm.read_only_udm.target.process.file.sha256`.   
2025-10-14 |  Enhancement:  
\- Added a grok pattern to parse the new log formats.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `machine_name` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `os_family`, `os_version`, `os_platform`, `container_id`, `user_sid`, `integrity`, `integrity_sz`, `elevation`, `elevation_sz`, `parent_integrity`, `parent_integrity_sz`, `parent_elevation`, `parent_elevation_sz`, `ring`, `event_version`, `company_id`, `ctc_version` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `hardware_id` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `parent_pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `parent_cmdline` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `parent_user_name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `cmdline` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `user_name` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.process.file.sha256`: Newly mapped `process_sha` raw log field with `event.idm.read_only_udm.target.process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.target.process.file.md5`: Newly mapped `process_md5` raw log field with `event.idm.read_only_udm.target.process.file.md5` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `mitre_ids` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added a gsub mutation to remove the ￻ character from the msg field.  
\- For file_read and file_modify events, `event.idm.read_only_udm.target.file.full_path` is now populated from the `process_path` raw log field if `target_file_full_path` is not available.  
\- For file_move events, logic was updated to populate `event.idm.read_only_udm.source.file.full_path` from the `old_path` raw log field and `event.idm.read_only_udm.target.file.full_path` from the `new_path` raw log field.   
2025-07-03 |  Enhancement:  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Removed mapping of `dvc` from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields when `BitdefenderGZModule` is `avc` in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip: Newly mapped `dvc` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields when `BitdefenderGZModule` is `avc`.  
\- Added null conditions for `security_result.action` UDM field.  
if `BitdefenderGZModule` is `new-incident`:  
\- event.idm.read_only_udm.target.file.md5: Newly mapped `fileHash` raw log field with `event.idm.read_only_udm.target.file.md5` UDM field.  
\- event.idm.read_only_udm.target.file.sha256: Newly mapped `BitdefenderGZFileHashSha256` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- event.idm.read_only_udm.target.file.names: Newly mapped `fname` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `BitdefenderGZAttackTypes`, `BitdefenderGZOldHwid`, and `BitdefenderGZNewHwid` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `BitdefenderGZIncidentId` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.security_result.first_discovered_time: Newly mapped `start` raw log field with `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.  
if `BitdefenderGZModule` is `hd`:  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `BitdefenderGZAttackType`, `BitdefenderGZDetectionLevel`, and `BitdefenderGZFilelessAttack` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
if `BitdefenderGZModule` is `fw`:  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `BitdefenderGZEventSourceIP` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped `BitdefenderGZFwProtocolId` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `cnt` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
if `BitdefenderGZModule` is `av`:  
\- event.idm.read_only_udm.security_result.action: When `act` is `deleted` set `event.idm.read_only_udm.security_result.action` UDM field as `BLOCK`.  
\- event.idm.read_only_udm.target.file.sha256: Newly mapped `BitdefenderGZMalwareHash` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- event.idm.read_only_udm.security_result.threat_name: Newly mapped `BitdefenderGZMalwareType` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `BitdefenderGZMalwareName` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
if `BitdefenderGZModule` is `avc`:  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `BitdefenderGZIncidentId` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.target.file.sha256: Newly mapped `BitdefenderGZFileHashSha256` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- event.idm.read_only_udm.target.process.parent_process.pid: Newly mapped `BitdefenderGZParentPid` raw log field with `event.idm.read_only_udm.target.process.parent_process.pid` UDM field.  
\- event.idm.read_only_udm.target.process.parent_process.file.full_path: Newly mapped `BitdefenderGZParentPath` raw log field with `event.idm.read_only_udm.target.process.parent_process.file.full_path` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `suser` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.windows_sid: Newly mapped `suid` raw log field with `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- event.idm.read_only_udm.security_result.action:  
\- When `act` is `blocked` set `event.idm.read_only_udm.security_result.action` UDM field as `BLOCK`.  
\- When `act` is `Disinfected` set `event.idm.read_only_udm.security_result.action` UDM field as `ALLOW_WITH_MODIFICATION`.  
\- event.idm.read_only_udm.security_result.threat_name: Newly mapped `BitdefenderGZDetectionName` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- event.idm.read_only_udm.target.process.command_line: Newly mapped `BitdefenderGZProcessCommandLine` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
if `BitdefenderGZModule` is `network-monitor`:  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `BitdefenderGZDetectionAttackTechnique` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `BitdefenderGZDetectionAttackerIp` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip: Newly mapped `BitdefenderGZDetectionVictimIp` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- event.idm.read_only_udm.target.port: Newly mapped `BitdefenderGZDetectionLocalPort` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
if `BitdefenderGZModule` is `exchange-malware`:  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `BitdefenderGZEmailSender` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `duser` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.network.email.subject: Newly mapped `BitdefenderGZEmailSubject` raw log field with `event.idm.read_only_udm.network.email.subject` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
if `BitdefenderGZModule` is `aph`:  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `BitdefenderGZEventType` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
if `module` is `antitampering`:  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `BitdefenderGZDetectionTechnique` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `BitdefenderGZDriverPath` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.process.parent_process.pid: Newly mapped `BitdefenderGZParentProcess` raw log field with `event.idm.read_only_udm.target.process.parent_process.pid` UDM field.  
\- event.idm.read_only_udm.target.process.parent_process.file.full_path: Newly mapped `BitdefenderGZParentProcessPath` raw log field with `event.idm.read_only_udm.target.process.parent_process.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.process.command_line: Newly mapped `BitdefenderGZDetectionCommandLine` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Setting `BitdefenderGZDetectionTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field when `BitdefenderGZModule` is in `av`, `avc`, `hd` else `BitdefenderGZDetectionTime` raw log field with `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.   
2025-05-21 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.first_seen_timestamp`: Newly mapped `BitdefenderGZDetectionTime` raw log field with `event.idm.read_only_udm.security_result.first_seen_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `BitdefenderGZSignaturesNumber` , `BitdefenderGZTaskScanType` , `BitdefenderGZScanEngineType` , `BitdefenderGZCleanedMalwareCnt` , `BitdefenderGZBlockedMalwareCnt` , `BitdefenderGZDeletedMalwareCnt` , `BitdefenderGZQuarantinedMalwareCnt` , `BitdefenderGZIgnoredMalwareCnt` and `BitdefenderGZPresentMalwareCnt` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added a `has_principal` check condition to set `event.idm.read_only_udm.metadata.event_type` UDM field as `STATUS_UNCATEGORIZED` when `has_principal` is `true`, else `GENERIC_EVENT`.   
2025-05-09 |  Enhancement:  
\- Declared `BitdefenderGZDetectionName` raw log field as null.   
2025-05-02 |  Enhancement:  
\- Added support for a new pattern of JSON logs.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `BitdefenderGZModule` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.target.user.company_name: Newly mapped `BitdefenderGZCompanyId` raw log field with `event.idm.read_only_udm.target.user.company_name` UDM field.  
\- event.idm.read_only_udm.about.hostname: Newly mapped `dvchost` raw log field with `event.idm.read_only_udm.about.hostname` UDM field.  
\- event.idm.read_only_udm.security_result.threat_name: Newly mapped `BitdefenderGZMalwareName` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field if `BitdefenderGZMalwareName` is not null , else Newly mapped if `BitdefenderGZDetectionName` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- event.idm.read_only_udm.principal.asset.network_domain: Newly mapped `BitdefenderGZComputerFQDN` raw log field with `event.idm.read_only_udm.principal.asset.network_domain` UDM field.  
\- event.idm.read_only_udm.principal.process.file.sha256: Newly mapped `BitdefenderGZMalwareHash` raw log field with `event.idm.read_only_udm.principal.process.file.sha256` UDM field, when the hash matches the regex format.  
\- event.idm.read_only_udm.target.resource.id: Newly mapped `BitdefenderGZHwId` raw log field with `event.idm.read_only_udm.target.resource.id` UDM field.  
\- event.idm.read_only_udm.security_result.category: Newly mapped `event_name` raw log field with `event.idm.read_only_udm.security_result.category` UDM field when `event_name` is `Antiphishing` set as `PHISHING else if `event_name` is `AntiMalware` set as `SOFTWARE_MALICIOUS".  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `reason` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `dvc` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.about.ip: Newly mapped `dvc` raw log field with `event.idm.read_only_udm.about.ip` UDM field.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.about.asset.asset_id: Newly mapped `deviceExternalId` raw log field with `event.idm.read_only_udm.about.asset.asset_id` UDM field, including `device_vendor` and `device_product` raw log fields.  
\- event.idm.read_only_udm.target.url: Newly mapped `request` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `BitdefenderGZSeverityScore` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `BitdefenderGZMalwareType` , `BitdefenderGZAttCkId` and `BitdefenderGZEndpointId` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.process.command_line: Newly mapped `sproc` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `suid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `BitdefenderGZMainAction` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `BitdefenderGZMainAction` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `BitdefenderGZMainAction` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `actionTaken` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `actionTaken` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `actionTaken` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `final_status` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `final_status` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `final_status` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `status` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `status` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `status` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.target.hostname and event.idm.read_only_udm.target.asset.hostname: Newly mapped `dhost` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `suser` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `act` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `msg` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `start` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.about.file.full_path: Newly mapped `filePath` raw log field with `event.idm.read_only_udm.about.file.full_path` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `device_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Setting `event.idm.read_only_udm.metadata.event_type` UDM field as `STATUS_UNCATEGORIZED` when `BitdefenderGZModule` is `new-incident` and `has_principal` is `true`, else `USER_UNCATEGORIZED` when `BitdefenderGZModule` is `task-status` and `has_principal_user` is not empty,else `STATUS_UPDATE` when `has_principal` is `true` and `BitdefenderGZModule` is not `new-incident` and `has_principal_user` is not empty, `GENERIC_EVENT` for any other case.  
\- event.idm.read_only_udm.metadata.vendor_name: Set `event.idm.read_only_udm.metadata.vendor_name` UDM field as `BitDefender`.  
\- event.idm.read_only_udm.metadata.product_name: Set `event.idm.read_only_udm.metadata.product_name` UDM field as `BitDefender EDR`.   
2023-05-02 |  Enhancement:  
\- Parsed logs ingested in CEF format.   
2022-09-28 |  Enhancement:  
\- Mapped `security_result.action` to `BLOCK` when `status` is `portscan_blocked` or `uc_site_blocked`.  
\- Mapped `security_result.action` to `BLOCK` when `main_action` is `blocked`.  
\- Mapped `security_result.action` to `BLOCK` when `actionTaken` is `block`.  
\- Mapped `security_result.action` to `BLOCK` when `final_status` is `blocked` or `deleted`.  
\- Mapped `security_result.action` to `ALLOW` when `final_status` is `ignored` or `still present`.  
\- Mapped `security_result.action` to `ALLOW` when `main_action` is `no action`.  
\- Mapped `security_result.action` to `QUARANTINE` when `final_status` is `quarantined`.  
\- Mapped `security_result.action` to `ALLOW_WITH_MODIFICATION` when `final_status` is `disinfected` or `restored`.   
2022-08-17 |  Enhancement  
\- Modified mapping for `source_ip` from `principal.ip` to `srcc.ip`.  
\- Set `event_type` to `SCAN_NETWORK` when `module` is equal to `network-monitor` or `fw`.  
\- Mapped `user.userSid` to `principal.user.windows_sid`.  
\- Mapped `user.userName` to `target.user.user_display_name`.  
\- Mapped `protocol_id` to `network.ip_protocol`.  
\- Set `security_result.action` to `BLOCK` when `status` is equal to `portscan_blocked` or `uc_site_blocked`.  
\- Mapped `local_port` to `principal.port`.  
\- Mapped `actionTaken` to `security_result.action`.  
\- Mapped `detection_attackTechnique` to `security_result.detection_fields`.   
2022-08-13 |  Bug-fix - Modified mapping for the field `computer_name` from `principal.asset.hostname` to `event.idm.read_only_udm.principal.resource.attribute.labels`.   
2022-08-11 |  Bug fix-  
\- Modified conditional checks for the field `main_action` mapped to `security_result.action`.  
\- Mapped `STATUS_UPDATE` to `metadata.event_type` for the logs having `task-status` module.   
2022-04-14 |  Enhancement-Added mappings for computer_name, computer_id, uc_type, block_type,status,product_installed.   
2022-03-30 |  Bug fix-Corrected the timestamp error and mapped the fields user.id, user.name, companyId, computer_name, computer_fqdn, computer_ip, computer_id, url and categories.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
