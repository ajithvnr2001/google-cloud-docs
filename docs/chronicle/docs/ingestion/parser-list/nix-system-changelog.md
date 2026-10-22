---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nix-system-changelog/
title: Change log for NIX_SYSTEM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:37.340372+00:00
---

# Change log for NIX_SYSTEM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nix-system-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for NIX_SYSTEM

Date | Changes  
---|---  
2026-09-21 |  \- `additional.fields`: Newly mapped `audit_id` raw log field from `msg=audit(timestamp:audit_id)` with `additional.fields` UDM field.  
\- `target.process.pid`: Newly mapped `pid` from `event[pid]` with `target.process.pid` UDM field for groupadd, groupmod, and groupdel events.   
2026-09-01 |  \- Updated grok pattern to support new structure of kernel logs.   
2026-08-28 |  \- `metadata.event_type`: Mapped the value `SERVICE_STOP` with `metadata.event_type` UDM field for JSON format logs having `Closed` in `message` raw log field for `systemd` process.  
\- `principal.hostname`: Newly mapped `labels.compute.googleapis.com/resource_name` with `principal.hostname` UDM field for `systemd` process for JSON format logs.  
\- `principal.asset.attribute.cloud.project.id`: Newly mapped `resource.labels.project_id` with `principal.asset.attribute.cloud.project.id` UDM field for `systemd` process for JSON format logs.  
\- `principal.process.pid`: Newly mapped `jsonPayload.pid` with `principal.process.pid` UDM field for `systemd` process for JSON format logs.  
\- `principal.asset.asset_id`: Newly mapped `labels.compute.googleapis.com/resource_id` with `principal.asset.asset_id` UDM field for `systemd` process for JSON format logs.  
\- `principal.asset.attribute.cloud.availability_zone`: Newly mapped `labels.compute.googleapis.com/zone` with `principal.asset.attribute.cloud.availability_zone` UDM field for `systemd` process for JSON format logs.  
\- `metadata.product_log_id`: Newly mapped `insertId` raw log field with `metadata.product_log_id` UDM field for `systemd` process for JSON format logs.  
\- `principal.resource.resource_subtype`: Newly mapped `resource.type` with `principal.resource.resource_subtype` UDM field for `systemd` process for JSON format logs.  
\- `metadata.description`: Newly mapped `jsonPayload.message` with `metadata.description` UDM field for `systemd` process for JSON format logs.  
\- `target.application`: Newly mapped `jsonPayload.ident` with `target.application` UDM field for `systemd` process for JSON format logs.   
2026-08-14 |  \- `security_result.description`: Newly mapped `op` raw log field with `security_result.description` UDM field unconditionally when `op` is present in audit logs.  
\- `metadata.event_type`: Mapped the value `GROUP_MODIFICATION` with `metadata.event_type` UDM field if the raw log field `eventType` has value `USER_MGMT` and if the raw log field `op` has value `add-user-to-group`, `add-user-to-shadow-group`, `delete-user-from-group`, `delete-user-from-shadow-group`, `deleting-user-from-group`, or `deleting-user-from-shadow-group`.  
\- `metadata.event_type`: Mapped the value `USER_CHANGE_PASSWORD` with `metadata.event_type` UDM field if the raw log field `eventType` has value `USER_CHAUTHTOK` and if the raw log field `op` has value `PAM:chauthtok`, `attempted-to-change-password`, `updating-password`, `changing`, or `updating`.  
\- `metadata.event_type`: Mapped the value `USER_UNCATEGORIZED` with `metadata.event_type` UDM field if the raw log field `eventType` has value `USER_CHAUTHTOK` and if the raw log field `op` has value `password status displayed for user`.  
\- `security_result.description`: Mapped the hardcoded value ``password status displayed for user`` with `security_result.description` UDM field if the raw log field `eventType` has value `USER_CHAUTHTOK` and if the raw log field `sub_audit_message` contains `op=password status displayed for user`.  
\- `target.group.product_object_id`: Newly mapped `id` raw log field with `target.group.product_object_id` UDM field if the raw log field `eventType` has value `DEL_GROUP`.  
\- `target.user.userid`: Newly mapped `acct` raw log field with `target.user.userid` UDM field if the raw log field `eventType` has value `DEL_GROUP`, `ADD_USER` or `ADD_GROUP`.  
\- `target.user.userid`: Newly mapped user id value parsed from the `msg1` raw log field with `target.user.userid` UDM field if the raw log field `process` has value `usermod` or `useradd`.  
\- `target.group.group_display_name`: Newly mapped group name value parsed from the `msg1` raw log field with `target.group.group_display_name` UDM field if the raw log field `process` has value `usermod` or `useradd`.  
\- `target.application`: Newly mapped `process` raw log field with `target.application` UDM field if the raw log field `process` has value `usermod` or `useradd`.  
\- `metadata.event_type`: Mapped the value `USER_UNCATEGORIZED` with `metadata.event_type` UDM field if the raw log field `process` has value `usermod` or `useradd` and if the raw log field `msg1` contains the group addition pattern.  
\- `metadata.event_type`: Mapped the value `USER_CHANGE_PASSWORD` with `metadata.event_type` UDM field if the raw log field `process` has value `usermod` and if the raw log field `msg1` contains the password change pattern.  
\- `target.hostname`: Removed mapping of hostname raw log field from `target.hostname` UDM field when `eventType` has value `DEL_GROUP`.  
\- `principal.hostname`: Mapped hostname raw log field with `principal.hostname` UDM field when `eventType` has value `DEL_GROUP`.  
\- `target.ip`: Removed mapping of ip address raw log field from `target.ip` UDM field when `eventType` has value `DEL_GROUP`.  
\- `principal.ip`: Mapped ip address raw log field with `principal.ip` UDM field when `eventType` has value `DEL_GROUP`.  
\- `target.user.userid`: Removed mapping of `uid`, `ouid`, `auid`, `suid`, `euid`, `oauid` or `fsuid` raw log fields from `target.user.userid` UDM field when `eventType` has value `DEL_GROUP`.  
\- `principal.user.userid`: Mapped `uid`, `ouid`, `auid`, `suid`, `euid`, `oauid` or `fsuid` raw log fields with `principal.user.userid` UDM field when `eventType` has value `DEL_GROUP`.  
\- `target.user.attribute.labels`: Removed mapping of `ouid`, `auid`, `suid`, `euid`, `oauid` and `fsuid` raw log fields from `target.user.attribute.labels` UDM field when `eventType` has value `DEL_GROUP`.  
\- `principal.user.attribute.labels`: Mapped `ouid`, `auid`, `suid`, `euid`, `oauid` and `fsuid` raw log fields with `principal.user.attribute.labels` UDM field when `eventType` has value `DEL_GROUP`.  
\- `metadata.event_type`: Mapped the value `GROUP_DELETION` with `metadata.event_type` UDM field if the raw log field `eventType` has value `DEL_GROUP`.  
\- `metadata.event_type`: Mapped the value `GROUP_CREATION` with `metadata.event_type` UDM field if the raw log field `eventType` has value `ADD_GROUP`.   
2026-07-21 |  \- Added grok pattern to parse the dropped logs in the legacy backward compatibility code.   
2026-06-01 |  \- `principal.ip`: Enhanced the grok pattern for `laddr` to correctly extract IPv6 addresses with interface suffixes for the logs parsed through the legacy backward compatibility code.   
2026-05-08 |  \- `intermediary.hostname`: Newly mapped `hostname` raw log field with `intermediary.hostname` UDM field for logs parsed through the legacy backward compatibility code having `resolve_first: Unable to lookup` log description.   
2026-04-28 |  \- Enhaced the facility and severity mapping logic to enhance performance and readability.  
\- security_result.severity: Updated the logic to map the value of `security_result.severity` based on the value of the `` prefix in the log header.  
\- security_result.severity_details: Updated the logic to map the value of `security_result.severity_details` based on the value of the `` prefix in the log header.   
2026-04-21 |  \- `metadata.event_timestamp`: Enhanced timestamp extraction, remove rebase, and added support for the new date format to ensure accurate parsing into `metadata.event_timestamp` for the logs of source path `/var/log/apache2/error.log`.  
\- Enhanced GROK pattern to support new pattern of logs and support mapping of below UDM fields for source path `/var/log/apache2/error.log`.  
\- `metadata.collected_timestamp`: Newly mapped `collected_ts` raw log field with `metadata.collected_timestamp` UDM field.  
\- `principal.hostname`: Newly mapped `principal_hostname` raw log field with `principal.hostname` UDM field.  
\- `principal.application`: Newly mapped `principal_application` raw log field with `principal.application` UDM field.   
2026-04-16 |  \- `security_result.severity`: Updated the logic to map the value of `security_result.severity` based on the value of the `` prefix in the log header.  
\- `security_result.severity_details`: Updated the logic to map the value of `security_result.severity_details` based on the value of the `` prefix in the log header.  
\- `metadata.product_log_id`: Updated the logic to map the value of `metadata.product_log_id` based on the value of the `` prefix in the log header.  
\- `metadata.product_log_id`: Removed mapping of `ID` from `metadata.product_log_id` UDM field if the `` prefix is present in the same log entry for logs in the `syslog` source path.  
\- additional.fields[ID]`: Newly mapped `ID` raw log field with `additional.fields[ID]` UDM field if the `` prefix is present in the same log entry for logs in the `syslog` source path.   
2026-03-24 |  \- `metadata.event_type`: Updated mapping of `metadata.event_type` from `USER_LOGIN` to `USER_LOGOUT` for logs parsed through the legacy backward compatibility code having `session closed` log description.   
2026-02-19 |  -`security_result.severity_details`: Newly mapped `severity` raw log field with `security_result.severity_details` UDM field for logs parsed through the legacy backward compatibility code.  
\- `security_result.severity`: Newly mapped `severity` raw log field with `security_result.severity` UDM field for logs parsed through the legacy backward compatibility code.  
\- `metadata.product_log_id`: Newly mapped `facility` raw log field with `metadata.product_log_id` UDM field for logs parsed through the legacy backward compatibility code.   
2026-01-30 |  \- Removed condition to filter out log drop for the log action `getting password` and the `pam_get_item` in the legacy backward compatibility code to parse logs.  
\- Added grok pattern for the `rsyslogd` process to accurately parse below UDM fields in the legacy backward compatibility code:  
\- `metadata.event_timestamp`  
\- `metadata.product_event_type`  
\- `target.application`  
\- `principal.hostname`  
\- `intermediary.hostname`  
2026-01-27 |  Updated grok pattern to support new fields of logs in the legacy backward compatibility code.  
\- `security_result.severity_details`: Newly mapped `severity` raw log field with `security_result.severity_details` UDM field for specific log pattern logs.  
\- `security_result.severity`: Newly mapped `severity` raw log field with `security_result.severity` UDM field for specific log pattern logs.  
\- `metadata.product_log_id`: Newly mapped `facility` raw log field with `metadata.product_log_id` UDM field for specific log pattern logs.   
2026-01-23 |  \- `principal.ip`: Removed mapping of invalid IP address value from `principal.ip` UDM field for `tufin-server` log.  
\- `principal.asset.ip`: Removed mapping of invalid IP address value from `principal.asset.ip` UDM field for `tufin-server` log.  
\- `target.user.userid`: Newly mapped `User ID` raw log field with `target.user.userid` UDM field for `tufin-server` log.  
\- `target.user.user_display_name`: Newly mapped `User name` raw log field with `target.user.user_display_name` UDM field for `tufin-server` log.   
2026-01-08 |  \- Added a grok pattern to support new pattern of logs in the `syslog` source path to map fields more accurately from earlier legacy support which will update the mapping as below:  
\- `target.hostname`: Removed mapping of `hostname` raw log field from `target.hostname` UDM field for NetworkManager process logs.  
\- `target.asset.hostname`: Removed mapping of `hostname` raw log field from `target.asset.hostname` UDM field for NetworkManager process logs.  
\- `intermediary.hostname`: Removed mapping of `hostname` raw log field from `intermediary.hostname` UDM field for NetworkManager process logs.  
\- `principal.hostname`: Mapped `hostname` raw log field with `principal.hostname` UDM field for NetworkManager process logs.  
\- `target.application`: Removed mapping of `process` raw log field from `target.application` UDM field for NetworkManager process logs.  
\- `target.platform`: Removed mapping of `LINUX` for `target.platform` UDM field for NetworkManager process logs.  
\- `principal.platform`: Set `principal.platform` UDM field `LINUX` for NetworkManager process logs.  
\- `principal.process.command_line`: Mapped `process` raw log field with `principal.process.command_line` UDM field for NetworkManager process logs.  
\- `security_result.description`: Newly mapped `description` raw log field with `security_result.description` UDM field for NetworkManager process logs.  
\- `security_result.severity`: Newly mapped `severity` raw log field with `security_result.severity` UDM field for NetworkManager process logs.   
2025-12-16 |  \- Support was added for log format that contain the `SyslogMessage` as a separate field in JSON format.   
2025-12-12 |  Enhanced GROK pattern to support new pattern of logs.   
2025-12-01 |  Updated grok pattern to support new structure of logs in the legacy backward compatibility code.  
\- principal.ip: Newly mapped `rhost` raw log field with `principal.ip` UDM field if the raw log field `process` has value `sshd` and if the raw log field `action` has value `authentication success`.  
\- principal.asset.ip: Newly mapped `rhost` raw log field with `principal.asset.ip` UDM field if the raw log field `process` has value `sshd` and if the raw log field `action` has value `authentication success`.  
\- principal.user.userid: Newly mapped `ruser` raw log field with `principal.user.userid` UDM field if the raw log field `process` has value `sshd` and if the raw log field `action` has value `authentication success`.  
\- security_result.description: Newly mapped `description` raw log field with `security_result.description` UDM field if the raw log field `process` has value `sshd` and if the raw log field `action` has value `authentication success`.  
\- metadata.event_type: Newly mapped the value `USER_LOGIN` with `metadata.event_type` UDM field if the raw log field `process` has value `sshd` and if the raw log field `action` has value `authentication success`.  
\- extensions.auth.mechanism: Newly mapped the value `USERNAME_PASSWORD` with `extensions.auth.mechanism` UDM field if the raw log field `process` has value `sshd` and if the raw log field `action` has value `authentication success`.  
\- security_result.action: Newly mapped the value `ALLOW` with `security_result.action` UDM field if the raw log field `process` has value `sshd` and if the raw log field `action` has value `authentication success`.  
\- network.application_protocol: Newly mapped the value `SSH` with `network.application_protocol` UDM field if the raw log field `process` has value `sshd` and if the raw log field `action` has value `authentication success` and if the raw log field `proto` has value `ssh`.   
2025-11-25 |  Added condition to exclude logs containing `NetworkManager` from being processed through the log source paths `/var/log/apache2/access.log` and `/var/log/nginx/access.log`. This change prevents potential parsing issues by ensuring only logs with the expected structure from these specific paths are processed through them.  
\- Added grok pattern to adjust the UDM mapping for the following field:  
\- metadata.product_event_type`: Removed mapping of the value `Simon` of raw log field `process` from `metadata.product_event_type` UDM field and mapped the value `pbs_oucheck` instead for the logs having `Simon` as a process.   
2025-11-17 |  \- Enhanced grok pattern to map the NetworkManager, CROND, and vsftpd processes to `metadata.product_event_type` UDM field.   
2025-11-14 |  Added grok pattern to support new structure of logs from the `syslog` source path.   
2025-11-06 |  Added GROK pattern to support new structure of logs.   
2025-10-31 |  Updated grok pattern to support new structure of logs in the legacy backward compatibility code.   
2025-10-30 |  Enhanced GROK pattern to support new pattern of logs.   
2025-10-13 |  Added grok pattern to map the following fields in the legacy backward compatibility code.  
\- target.ip: Newly mapped `DstIP` raw log field with `target.ip` UDM field.  
\- target.port: Newly mapped `DstPort` raw log field with `target.port` UDM field.  
\- principal.ip: Newly mapped `SrcIP` raw log field with `principal.ip` UDM field.  
\- principal.port: Newly mapped `SrcIP` raw log field with `principal.port` UDM field.   
2025-10-10 |  \- Added a grok pattern to parse logs from the `syslog` source path in JSON format.   
2025-09-09 |  \- target.user.userid: Added grok pattern to remove mapping of the partial value of `username` from the `target.user.userid` UDM field and mapped the complete value of `username` instead.   
2025-09-08 |  Added a grok pattern to support new structure of logs.  
\- metadata.product_event_type: Newly mapped `process` raw log field with `metadata.product_event_type` UDM field.  
\- principal.process.pid: Newly mapped `process_id` raw log field with `principal.process.pid` UDM field.   
2025-08-26 |  \- Added a grok pattern to parse logs from the `syslog` source path in JSON format.   
2025-06-30 |  Updated grok pattern to support new structure of `syslog` logs.   
2025-04-28 |  intermediary.hostname: Newly mapped `hostname` raw log field with `intermediary.hostname` UDM field.   
2025-03-11 |  Added grok pattern to support new schema structure of `kernel` logs.   
2025-02-11 |  Updated grok pattern to support new structure of `syslog` logs.   
2025-01-22 |  Added grok pattern to support new structure of `kernel` log.   
2025-01-17 |  Added support for dropped logs of the `Could not load host key` and `Set` actions logs in sshd.   
2024-12-26 |  Updated grok pattern to support new structure of `mail` log.   
2024-11-26 |  Added support for dropped logs of the `reprocess` action logs in sshd.   
2024-10-25 |  Promoted the parser to default.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
