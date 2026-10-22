---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/auditd-changelog/
title: Change log for AUDITD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:37.629888+00:00
---

# Change log for AUDITD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/auditd-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AUDITD

Date | Changes  
---|---  
2026-09-30 |  Enhancement:  
\- Added New Grok pattern to support new format of syslog logs.  
\- Modified the grok patterns to support new format of syslog logs.   
2026-09-22 |  Enhancement:  
\- Added support for new format of syslog.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `eventType`, `process_pid`, `msg2` raw log fields with `event.idm.read_only_udm.metadata.description` UDM field.   
2026-09-18 |  \- Handled edge case scenarios for the `Task` raw log field.   
2026-09-01 |  Enhancement:  
\- Added a Grok pattern to support new format of syslog logs.  
\- `event.idm.read_only_udm.principal.process.pid`: Removed mapping of `process_pid` from `event.idm.read_only_udm.principal.process.pid` UDM field since it is a duplicate Mapping and Added a conditional check to map `process_pid` to `event.idm.read_only_udm.principal.process.pid` UDM field when `tar_pid` is null.   
2026-07-30 |  Enhancement:  
\- Modified grok pattern to support new format of syslog logs.   
2026-07-03 |  Enhancement:  
\- Added a Grok pattern to support new format of syslog logs.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `service` field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `uid` field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.first_name`: Newly mapped `first_name` field with `event.idm.read_only_udm.principal.user.first_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.last_name`: Newly mapped `last_name` field with `event.idm.read_only_udm.principal.user.last_name` UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `domain` field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.   
2026-05-07 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `home`, `shell` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `name` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field when the log is having `new user` related data.  
\- `event.idm.read_only_udm.target.group.group_display_name`: Newly mapped `name` raw log field with `event.idm.read_only_udm.target.group.group_display_name` UDM field when the log is having `new group` related data.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Newly mapped `UID` raw log field with `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.user.group_identifiers`: Newly mapped `GID` raw log field with `event.idm.read_only_udm.target.user.group_identifiers` UDM field when the log is having `new user` related data.  
\- `event.idm.read_only_udm.target.group.product_object_id`: Newly mapped `GID` raw log field with `event.idm.read_only_udm.target.group.product_object_id` UDM field when the log is having `new group` related data.  
\- Added a Grok pattern on the `msg2` data field to parse the raw log fields.   
2026-04-13 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_priority` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `file_path` log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- Added a Grok pattern on `message` to parse the raw log fields.  
\- Added a grok pattern on `msg2` to extract `apname`, `outcome`, `file_path`, and `description`.   
2026-03-31 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `USER_LOGIN` to `event.idm.read_only_udm.metadata.event_type` to when `message` is `Accepted publickey` and target user data.   
2026-02-26 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `key_type`, `hash`, raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `key_fingerprint` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added a new grok pattern for the raw log field `message` to extract `service_name`, `desc_1`, `target_user_id`, `uid`, `srcip`, `srcport`.  
\- Added a new grok pattern for the `message` field this is allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.principal.ip`  
\- `event.idm.read_only_udm.principal.asset.ip`  
\- `event.idm.read_only_udm.principal.port`  
\- `event.idm.read_only_udm.target.user.product_object_id`  
\- `event.idm.read_only_udm.target.user.userid`  
2026-02-25 |  Enhancement:  
\- If `type` is `VIRT_CONTROL` and `principal_hostname` is empty, set `event.idm.read_only_udm.principal.hostname` to `UNKNOWN`.   
2026-02-12 |  Enhancement:  
\- Added gsub to replace \\\` with `.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `user` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- If the above grok match is successful, added conditional check to map `user` to `event.idm.read_only_udm.target.user.userid`.  
\- If the above grok match is not successful, added conditional check to map `desc_1` to `event.idm.read_only_udm.security_result.description`.   
2026-02-09 |  Enhancement:  
\- Added grok pattern to properly support a format of syslog logs and prevent duplicate mapping of same hostname in `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.intermediary.hostname`.  
\- Modified the gsub logic to ensure the strings `network` and `target` are not incorrectly transformed into `network1` and `target1` within the raw logs.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `error_detail1` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.   
2026-02-06 |  Enhancement:  
\- Added support for Azure JSON Syslog format.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `_SubscriptionId` and `_Internal_WorkspaceResourceId` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- event.idm.read_only_udm.principal.process.file.names: Newly mapped `ProcessName` raw log field to `event.idm.read_only_udm.principal.process.file.names`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `MG`, `TimeGenerated`, `Type`, `_BilledSize`, `_IsBillable`, `_TimeReceived` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `EventTime` raw log field to `event.idm.read_only_udm.metadata.event_timestamp`.   
2026-01-22 |  Enhancement:  
\- Modified the logic for populating `event.idm.read_only_udm.principal.hostname`. The `node` field will now only be used to populate `event.idm.read_only_udm.principal.hostname` if the `labels.host.name` field is empty. This gives precedence to labels.host.name when available.   
2026-01-13 |  Enhancement:  
\- Added a GROK pattern to support an additional AUDITD log format.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `service_name`, `ssh_disconnect_code` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `srcip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `srcip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `srcport` raw log field to `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `desc_1` raw log field to `event.idm.read_only_udm.security_result.description` UDM field.   
2026-01-02 |  Enhancement:  
\- Added a mutate filter that performs a global substitution on the message field, replacing `network1` with `network`.  
\- Removed the `,timestamp:` substring from the type_props.AUID field, which is used to populate the event.idm.read_only_udm.about.user.user_display_name UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `labels.bp_csoc`, `labels.bp_env_id`, `labels.log.file.name`, `resource.labels.node_id` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `labels.host.name` raw log field to `event.idm.read_only_udm.principal.hostname` UDM field.   
2025-12-24 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped facility, kind, priority raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped message raw log field(s) with event.idm.read_only_udm.metadata.description UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped msg_type raw log field(s) with event.idm.read_only_udm.metadata.product_event_type UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped hostname raw log field(s) with event.idm.read_only_udm.principal.asset.ip UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped hostname raw log field(s) with event.idm.read_only_udm.principal.hostname UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped hostname raw log field(s) with event.idm.read_only_udm.principal.ip UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped proc_id raw log field(s) with event.idm.read_only_udm.principal.process.pid UDM field.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped actor_uid, uid raw log field(s) with event.idm.read_only_udm.principal.user.product_object_id UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped op raw log field(s) with event.idm.read_only_udm.security_result.action UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped addr, auid, fp, ses, subj raw log field(s) with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped res raw log field(s) with event.idm.read_only_udm.security_result.summary UDM field.  
\- event.idm.read_only_udm.target.file.sha256: Newly mapped fp raw log field(s) with event.idm.read_only_udm.target.file.sha256 UDM field.  
\- event.idm.read_only_udm.target.process.file.full_path: Newly mapped exe raw log field(s) with event.idm.read_only_udm.target.process.file.full_path UDM field.  
\- event.idm.read_only_udm.target.process.pid: Newly mapped spid, target_pid raw log field(s) with event.idm.read_only_udm.target.process.pid UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped appname raw log field(s) with event.idm.read_only_udm.target.resource.name UDM field.  
\- event.idm.read_only_udm.target.user.product_object_id: Newly mapped suid, uid raw log field(s) with event.idm.read_only_udm.target.user.product_object_id UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped target_user_id raw log field(s) with event.idm.read_only_udm.target.user.userid UDM field.  
\- event.idm.read_only_udm.security_result.action: Set to ALLOW if the parsed op field from the log message is destroy.   
2025-12-11 |  Enhancement:  
\- Added a GROK pattern to support an additional AUDITD log format. This allows the parser to extract fields from logs where the `intermediary_host` value is not prefixed with an asterisk (*), making the parsing more flexible.   
2025-11-19 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `intermediary_host` raw log field(s) with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- Two new grok patterns were added to extract intermediary_host and other fields from different auditd_system log formats.   
2025-08-05 |  Enhancement:  
\- Parser overhaul version to make it more efficient and increase fields coverage. You can see the full list of changes in the parser documentation page https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/auditd.   
2025-07-29 |  Enhancement:  
\- Added grok pattern to parse new pattern of syslog logs.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `PWD` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `log_details` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added regex expression to map srcIP to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.   
2025-07-15 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `indicator.SUID`, `indicator.UID`, and `indicator.AUID` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped the `type_crypto_props.msg` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-06-12 |  Enhancement:  
\- Made changes in the `auditd.include` file.  
\- Added grok pattern for new SYSLOG logs.  
\- Added a condition check to set event type as `PROCESS_LAUNCH`  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `usr` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `pi` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field  
\- event.idm.read_only_udm.target.process.command_line: Newly mapped `cmnd` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field   
2025-05-31 |  Enhancement:  
\- When `auth` contains `sshd` and `audit_message` contains `error resolving or error getting information or authentication fails` then set `security_result.detection_fields.key` as `authentication_protocol` and `security_result.detection_fields.value` as `Kerberos`.  
\- When `auth` contains `sshd` and `audit_message` contains `Invalid user or invalid user or error resolving or error retrieving or error getting information or authentication fails or check pass` then set `security_result.action_details` as `FAILURE`.  
\- When `auth` contains `sshd` and `audit_message` contains `check pass` then set `security_result.detection_fields.key` as `authentication_mechanism` and `security_result.detection_fields.value` as `PAM_UNIX`.  
\- When `auth` contains `sshd` and `audit_message` contains `error retrieving` then set `security_result.detection_fields.key` as `authentication_mechanism` and `security_result.detection_fields.value` as `PAM`.  
\- When `auth` contains `sshd` and `audit_message` contains `error getting information or authentication fails` then set `security_result.detection_fields.key` as `authentication_mechanism` and `security_result.detection_fields.value` as `PAM_KRB5`.  
\- When `auth` contains `sshd` and `audit_message` contains `Bye Bye` then set `security_result.detection_fields.key` as `connection_state` and `security_result.detection_fields.value` as `DISCONNECTED`.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `proctitle_value` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.names`: Newly mapped `filename` raw log field with `event.idm.read_only_udm.principal.process.file.names` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `filepath` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- When audit_message contains `PROCTITLE`, and principal_hostname is not empty, and tar_host is not empty, then set `event.idm.read_only_udm.metadata.event_type` to `PROCESS_LAUNCH`.  
\- When `has_principal` is `true`, and has_file is `true`, and message contains `file-open`, then set `event.idm.read_only_udm.metadata.event_type` to `FILE_OPEN`.  
\- When the `event_type` field is equal to the string `USER_UNCATEGORIZED` or is equal to the string `GENERIC_EVENT`, and the `principal_user_present` field is equal to `true` or the `has_principal` field is equal to `true`, and the `target_user_present` field is equal to `true` or the `has_target` field is equal to `true`, and the message field contains any of the following strings: `error resolving, error retrieving, error getting information, invalid user, authentication fails, or check pass` then:  
\- Set the `event.idm.read_only_udm.extensions.auth.type` to `AUTHTYPE_UNSPECIFIED.  
\- Set the `event.idm.read_only_udm.metadata.event_type` to `USER_LOGOUT`.   
2025-05-21 |  Enhancement:  
\- Added grok patterns to parse new pattern of syslog logs.  
\- Added gsub function to remove ` msg=`.+?`` from the `type_syscall` field.  
\- Added KV filter for `type_syscall` field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `uid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `acct` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.target.process.file.full_path: Newly mapped `exe` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.about.user.userid: Newly mapped `auid` raw log field with `event.idm.read_only_udm.about.user.userid` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `ses` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Added GROK pattern to match then mapped `addr` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- Added grok pattern to extract `msg_value` and `grantors_value` from `acct_msg_value` field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `subj` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `res` and `op` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `msg_value` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `grantors_value` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field if `grantors_value` is not empty and `?`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `indicator.msg` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field if `indicator_msg` is starting with `op=` or `msg_Value` is starting with `PAM` and not empty.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `indicator.grantors` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field if `grantors_value` is empty and `grantors_label.value` is not empty and `?`.  
\- event.idm.read_only_udm.principal.application: Newly mapped `terminal` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.security_result: Newly mapped `sec_result` raw log field with `event.idm.read_only_udm.security_result` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field if `hostname` is not empty and `?`.  
\- Added grok pattern to parse new pattern of syslog logs in the `.include` file.   
2025-05-19 |  Enhancement:  
\- `event.idm.read_only_udm.src.user.attribute.permissions`: Newly mapped `indicator.mode` raw log field with `event.idm.read_only_udm.src.user.attribute.permissions` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `indicator.nametype` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields` : Newly mapped `indicator.cap_frootid` , `indicator.cap_fver` , `indicator.cap_fi` , `indicator.cap_fp` and `indicator.cap_fe` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid` : Newly mapped `OUID` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.group.group_display_name` : Newly mapped `OGID` raw log field with `event.idm.read_only_udm.principal.group.group_display_name` UDM field.   
2025-04-17 |  Enhancement:  
\- Added grok patterns to parse new pattern of syslog logs.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly Mapped `action_data` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field when `action_data` is `Accepted password`.  
\- `event.idm.read_only_udm.security_result.action`: Newly Mapped `ALLOW` with `event.idm.read_only_udm.security_result.action` UDM field when `action_data` is `Accepted password`.   
2025-04-16 |  Enhancement:  
\- Added Grok patterns to parse new type of logs.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `sessionid` raw log field with event.idm.read_only_udm.network.session_id UDM field.  
\- event.idm.read_only_udm.network.email.mail_id: Newly mapped `mailid` raw log field with event.idm.read_only_udm.network.email.mail_id UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `email` raw log field with event.idm.read_only_udm.principal.user.email_addresses UDM field, if it matches a valid email pattern.  
\- event.idm.read_only_udm.principal.process.command_line: Newly mapped `auth` raw log field with event.idm.read_only_udm.principal.process.command_line UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `process_pid` raw log field with event.idm.read_only_udm.principal.process.pid UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `error_message` raw log field with event.idm.read_only_udm.metadata.description UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user_name` raw log field with event.idm.read_only_udm.principal.user.userid UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `auth_realm` raw log field with event.idm.read_only_udm.additional.fields UDM field.  
\- If audit_message contains `pam_krb5.*authentication fails for`, set metadata.product_event_type to PAM_KRB5_AUTH_ERROR.  
\- If audit_message contains `Received disconnect`, set metadata.product_event_type to DISCONNECT.  
\- If audit_message contains `Invalid user`, set metadata.product_event_type to INVALID_USER.  
\- If audit_message contains `pam_succeed_if.*error retrieving information about`, set metadata.product_event_type to PAM_AUTH_ERROR.  
\- If audit_message contains `error getting information about` and applica is pam_krb5, set metadata.product_event_type to PAM_KRB5_AUTH_ERROR.  
\- If audit_message contains `pam_unix.*check pass`, set metadata.product_event_type to PAM_UNIX_AUTH_ERROR.   
2025-04-07 |  Enhancement:  
\- Added a grok pattern to map the unparsed fields.  
\- Additional Fields Mapping:  
\- `event.idm.ready_only_udm.target.user.email_addresses`: Newly mapped `target_email` raw log field with `event.idm.ready_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.ready_only_udm.principal.ip` and `event.idm.ready_only_udm.principal.asset.ip`: Newly mapped `princi_ip` raw log field with `event.idm.ready_only_udm.principal.ip` and `event.idm.ready_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.ready_only_udm.target.port`: Newly mapped `target_port` raw log field with `event.idm.ready_only_udm.target.port` UDM field.  
\- `event.idm.ready_only_udm.security_result.action_details`: Newly mapped `status` raw log field with `event.idm.ready_only_udm.security_result.action_details` UDM field.  
\- `event.idm.ready_only_udm.network.email.to`: Newly mapped `to_email` raw log field with `event.idm.ready_only_udm.network.email.to` UDM field.  
\- `event.idm.ready_only_udm.target.hostname`: Newly mapped `target_hostname` raw log field with `event.idm.ready_only_udm.target.hostname` UDM field.  
\- `event.idm.ready_only_udm.additional.fields`: Newly mapped `relay_data` , `delays_data` , `delay_data` , and `dns_data` raw log field with `event.idm.ready_only_udm.additional.fields` UDM field.  
\- `event.idm.ready_only_udm.network.sent_bytes`: Newly mapped `bytes_sent` raw log field with `event.idm.ready_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.ready_only_udm.network.received_bytes`: Newly mapped `bytes_received` raw log field with `event.idm.ready_only_udm.network.received_bytes` UDM field.  
\- `event.idm.ready_only_udm.network.http.response_code`: Newly mapped `response_code` raw log field with `event.idm.ready_only_udm.network.http.response_code` UDM field.   
2025-03-26 |  Enhancement:  
\- Modified Grok pattern to parse `principal.user.userid`.   
2025-03-11 |  Enhancement:  
\- Added Grok patterns to parse new type of logs.  
\- Mapped `principal_user_name` to `principal.user.userid`.   
2025-03-06 |  Enhancement:  
\- Added Grok patterns to parse username for the new format of syslog logs.   
2025-02-13 |  Enhancement:  
\- Added support for SYSLOG logs.   
2025-02-12 |  Enhancement:  
\- Added support for the new format of JSON logs.   
2025-01-17 |  Enhancement:  
\- Added support for a new JSON log format.   
2025-01-15 |  Enhancement:  
\- Removed the index value from the `security_result.detection_fields` value.   
2025-01-10 |  Enhancement:  
\- Mapped `remote` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `method` to `network.http.method`.  
\- Mapped `path` to `principal.file.full_path`.  
\- Mapped `code` to `additional.fields`.  
\- Mapped `size` to `principal.file.size`.  
\- Mapped `agent` to `network.http.user_agent`.  
\- Mapped `az` to `principal.location.name`.  
\- Mapped `ec2_instance_id` to `principal.asset.product_object_id`.  
\- Mapped `private_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `ProviderName` to `additional.fields`.  
\- Mapped `Version` to `additional.fields`.  
\- Mapped `Task` to `additional.fields`.  
\- Mapped `EventRecordID` to `additional.fields`.  
\- Mapped `ThreadID` to `additional.fields`.  
\- Mapped `messageType` to `target.resource.attribute.labels`.  
\- Mapped `owner` to `principal.user.userid`.  
\- Mapped `logevent.id` to `metadata.product_log_id`.  
\- Mapped `logGroup` to `secu_result.about.resource.name`.  
\- Mapped `logStream` to `secu_result.about.resource.attribute.labels`.  
\- Added Grok patterns to parse `logevent.message` and `logevent.extractedFields.message`.  
\- Mapped `ip_addr` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `gd` to `secu_result.description`.  
\- Mapped `process` to `target.application`.  
\- Mapped `pid` to `target.process.pid`.  
\- Mapped `status_code` to `network.http.response_code`.  
\- Mapped `url` to `network.http.referral_url`.  
\- Mapped `useragent` to `network.http.user_agent`.  
\- Mapped `request` to `additional.fields`.  
\- Mapped `method` to `network.http.method`.  
\- Mapped `tls_version` to `network.tls.version`.  
\- Mapped `hostname_is` to `principal.hostname`.  
\- Mapped `referrer` to `network.http.referral_url`.   
2024-12-26 |  Enhancement:  
\- Added support for `security_os_linux_visible`, `security_wifi_arubacontroller`, and `security_os_linux_soe` logs.   
2024-12-18 |  Enhancement:  
\- Changed `indicator.res` mapping from `security_result.detection_fields` to `security_result.description`.   
2024-12-12 |  Enhancement:  
\- Added a new Grok pattern to support new format of syslog logs.   
2024-12-05 |  Enhancement:  
\- when `eventType` is `sshd`, then mapped the following fields:  
\- `target_host` to `target.hostname`  
\- `source_ip` to `src.ip`  
\- `source_port` to `src.port`  
\- `tar_app` to `target.application`  
\- `tar_pid` to `target.process.pid`  
2024-11-21 |  Enhancement:  
\- Changed mapping of `username` from `principal.user.userid` to `target.user.userid`.  
\- When `username` is not null, then mapped `metadata.event_type` to `USER_LOGIN`.  
\- When `audit_message` is `PROCTITLE`, then mapped `metadata.event_type` to `PROCESS_UNCATEGORIZED`.   
2024-11-19 |  Enhancement:  
\- Mapped `srcIP` to `principal.ip` and `srcPort` to `principal.port`.   
2024-11-15 |  Enhancement:  
\- Added Grok patterns to parse `username` field.  
\- Mapped `username` to `principal.user.user_display_name`.   
2024-11-06 |  Enhancement:  
\- Mapped `type_syscall_props.msg` to `additional.fields`.   
2024-10-31 |  Enhancement:  
\- Added support for the new pattern of SYSLOG logs.   
2024-10-28 |  Enhancement:  
\- Added support for timestamps that include timezone offsets.   
2024-10-15 |  Enhancement:  
\- Mapped `sw`, `sw_type`, and `subj` to `security_result.detection_fields`.   
2024-10-14 |  Enhancement:  
\- Added a conditional check and mapped `metadata.event_type` to `USER_LOGIN` from `USER_UNCATEGORIZED`.   
2024-10-10 |  Enhancement:  
\- Added `gsub` to map `type` to `metadata.product_event_type`.  
\- Mapped `indicator.SYSCALL` to `security_result.detection_fields`.   
2024-10-09 |  \- Mapped `exe` to `principal.process.file.full_path`.   
2024-09-24 |  Enhancement:  
\- Swapped mapping from `target.port` to `principal.port`.  
\- Added support to handle Syslog logs.   
2024-09-16 |  Enhancement:  
\- Modified a Grok pattern to parse new patterns of logs.   
2024-08-13 |  Enhancement:  
\- Converted `a2` from hexadecimal value to ASCII.   
2024-07-18 |  \- Added `gsub` to replace `\\r\\n` with ` ` from the message.  
\- Added a grok pattern for `msg2`.  
\- Mapped `target.user.userid` to `principal.user.userid`.   
2024-07-09 |  Enhancement:  
\- Added `gsubs` to handle invalid JSON logs.  
\- When `type` is `SYSCALL` and `has_principal` is true and `exe` is not empty, then set `metadata.event_type` to `PROCESS_LAUNCH`.   
2024-06-18 |  Enhancement:  
\- Added new Grok patterns to handle authentication syslog logs.  
\- Mapped `target_user_name` to `target.user.userid`.  
\- Handled the new patterns of `_timestamp`.   
2024-05-08 |  Enhancement:  
\- When the value is not `?`, then mapped `field` to `field33` to `security_result.detection_fields`.  
\- When `type_name` is `CRYPTO_KEY_USER`, then mapped `exe` to `principal.process.file.full_path`.  
\- When `type_name` is `CRYPTO_KEY_USER`, then mapped `fp` to `network.tls.client.certificate.sha256`.  
\- When `type_name` is `CRYPTO_KEY_USER`, then mapped `pid` to `principal.process.pid`.  
\- Added Grok patterns to parse new pattern of logs.  
\- Mapped `syslog-tag` to `security_result.detection_fields`.  
\- Mapped `inter_ip` to `intermediary.ip`.  
\- Mapped `inter_hostname` to `intermediary.hostname`.   
2024-05-02 |  Enhancement:  
\- When `type_name` is `USER_MGMT`, then mapped `grp` to `target.group.group_display_name`.  
\- When `type_name` is `USER_MGMT`, then changed mapping of `uid` from `principal.user.userid` to `target.user.userid`.  
\- When `type_name` is `USER_MGMT` and `op` is equal to `deleting-user-from-group`, then set `metadata.event_type` to `GROUP_MODIFICATION`.  
\- When `type_name` is `USER_MGMT`, then changed mapping of `exe` from `target.process.file.full_path` to `principal.process.file.full_path`.  
\- When `type_name` is `USER_MGMT`, then mapped `id` to `about.user.userid`.   
2024-04-08 |  Enhancement:  
\- When `type_name` is `ADD_USER`, principal_user_present is `true`, target_user_present is `true`, and has_principal is `true`, then set `metadata.event_type` to `USER_CREATION`.  
\- When `type_name` is `USER_AUTH`, then mapped `acct` to `target.user.user_display_name`.  
\- When `type_name` is `USER_AUTH`, then mapped `uid` to `principal.user.userid`.  
\- When `type_name` is not in `ADD_USER`,`USER_AUTH`,`CRED_ACQ`, and `USER_MGMT`, then mapped `auid` to `about.user.userid`.  
\- When `type_name` is `ADD_USER`, then mapped `auid` to `target.user.userid`.  
\- When `type_name` is `ADD_USER` or `USER_AUTH` then mapped `exe` to `principal.process.file.full_path`.  
\- When `type_name` is `ADD_USER`, then mapped `op` and `id` to `security_result.summary`.  
\- When `type_name` is `USER_AUTH`, then mapped `op` and `acct` to `security_result.summary`.   
2024-03-22 |  Enhancement:  
\- Added support for new pattern of JSON logs.  
\- Mapped `labels.compute.googleapis.com/resource_name`,`jsonPayload._HOSTNAME` , `CollectorHostName`, `HOSTNAME`, and `Computer` to `principal.hostname`.  
\- Mapped `HostIP` to `principal.ip`.  
\- Mapped `ProcessID` and `jsonPayload._PID` to `principal.process.pid`.  
\- Mapped `SyslogMessage` to `metadata.description`.  
\- Mapped `TenantId`, `_ItemId`, `_Internal_WorkspaceResourceId`, `_ResourceId`, and `Facility` to `additional.fields`.  
\- Mapped `SeverityLevel` to `security_result.severity`.  
\- Mapped `SourceSystem` to `principal.platform`.  
\- Mapped `jsonPayload._COMM` to `principal.application`.  
\- Mapped `jsonPayload._EXE` to `target.process.file.full_path`.  
\- Mapped `jsonPayload._AUDIT_FIELD_FILE` to `target.file.full_path`.  
\- Mapped `jsonPayload._AUDIT_FIELD_HASH` to `target.file.hash`.  
\- Mapped `jsonPayload._AUDIT_SESSION` to `network.session_id`.  
\- Mapped `jsonPayload._PPID` to `principal.process.parent_process.pid`.  
\- Mapped `jsonPayload._AUDIT_FIELD_A0`, `jsonPayload._AUDIT_FIELD_A1`, `jsonPayload._AUDIT_FIELD_A2`, `jsonPayload._AUDIT_FIELD_A3`, `jsonPayload._BOOT_ID`, and `jsonPayload._AUDIT_FIELD_EXIT` to `security_result.detection_fields`.   
2023-11-27 |  Enhancement:  
\- Added validation check to ensure either `principal_user_present`, `target_user_present` or `has_principal` is true before setting `metadata.event_type` to `USER_LOGIN`.  
\- Added validation check to ensure either `principal_user_present`, `target_user_present` or `has_principal` is true before setting `metadata.event_type` to `USER_LOGOUT`.  
\- Added validation check to ensure either `principal_user_present`, `target_user_present` or `has_principal` is true before setting `metadata.event_type` to `USER_CREATION`.  
\- Added validation check to ensure either `principal_user_present`, `target_user_present` or `has_principal` is true before setting `metadata.event_type` to `USER_DELETION`.  
\- Added validation check to ensure either `principal_user_present`, `target_user_present` or `has_principal` is true before setting `metadata.event_type` to `USER_UNCATEGORIZED`.  
\- Added validation check to ensure either `principal_user_present`, `target_user_present` or `has_principal` is true before setting `metadata.event_type` to `USER_RESOURCE_ACCESS`.  
\- Added validation check to ensure either `principal_user_present`, `target_user_present` or `has_principal` is true before setting `metadata.event_type` to `USER_CHANGE_PERMISSIONS`.  
\- When user details are present and principal machine details are not present then changed mapping of `metadata.event_type` from `USER_CREATION` to `USER_UNCATEGORIZED`.  
\- When user details are present and principal machine details are not present then changed mapping of `metadata.event_type` from `USER_DELETION` to `USER_UNCATEGORIZED`.   
2023-09-06 |  Enhancement:  
\- Added mapping of `CMD` to `target.process.command_line` for `cron daemon(CROND)`.   
2023-06-20 |  Enhancement - Added or modified the following mappings when type=`ADD_USER` and `DEL_USER`-  
\- Modified the mapping of `uid` from `target.user.userid` to `principal.user.userid`.  
\- Mapped `id` to `target.user.userid`.  
\- Mapped `ID` to `target.user.user_display_name`.  
\- Modified the mapping of `UID` from `principal.user.userid` to `principal.user.user_display_name`.  
\- Modified the mapping of `acct` from `principal.user.user_display_name` to `target.user.user_display_name` and `target.user.userid`.   
2023-06-09 |  Enhancement - Modified `event_type` from `USER_LOGIN` to `USER_CREATION` when `type=ADD_USER`.   
2023-04-17 |  Enhancement  
\- Added gsub function to replace `GS - Group separator` character which is breaking the JSON construction.   
2023-04-10 |  Enhancement  
\- Added `gid`,`euid`,`egid`,`suid`,`fsuid`,`sgid`,`fsgid`,`tty`,`items` fields to security_result.detection_fields.  
\- Additionally mapped `gid` to `principal.user.group_identifiers`.  
\- Mapped `euid` to `target.user.userid`.  
\- Mapped `egid` to `target.user.group_identifiers`.   
2023-03-27 |  Enhancement - Added support for `jsonPayload` containing logs.   
2023-02-28 |  Bug-fix - Enhanced parser to convert hex encoded string to ASCII.   
2023-02-09 |  Enhancement - Modified grok for logs containing `type=PATH` to fetch the correct hostname from logs.   
2023-01-24 |  Enhancement -  
\- Parsed log with eventType as `tac_plus`.  
\- Added conditions for mapping different event_types `NETWORK_CONNECTION`, `NETWORK_HTTP`, `USER_LOGIN`.   
2022-12-02 |  Enhancement -  
\- Mapped `user_name` to `principal.user.userid`.  
\- added conditional check for `dst_ip`, `dst_port`.   
2022-11-16 |  Enhancement -  
\- Improved `GENERIC_EVENT` to `STATUS_UPDATE` for log types containing `Access Logs`.   
2022-10-31 |  Enhancement -  
\- Enhanced the parser to parse the log with type=ADD_USER, USER_MGMT, DEL_USER.  
\- Added null checks for `principal_hostname`.  
\- Added on_error checks for `principal.process.file.full_path`, `type_syscall_props.key`, `type_syscall_props.arch`, `msg2`.  
\- Added conditional checks for mapping to event_type=`FILE_OPEN`, `USER_UNCATEGORIZED`, `STATUS_UPDATE`, `USER_DELETION`.  
\- Mapped `principal_user_userid` to `principal.user.userid`.   
2022-10-14 |  Enhancement -  
\- Migrated customer parser to default parser.   
2022-10-13 |  Enhancement - Mapped `vendor_name` to `Linux`.  
\- Mapped `product_name` to `AuditD`.  
\- Parsed the logs containing `ProxySG` and mapped `ip` to `target.ip`, `port` to `target.port` wherever possible.  
\- Modified `event_type` from `GENERIC_EVENT` to `STATUS_UPDATE`.  
\- Modified mapping for `intermediary.hostname` to `principal.hostname`.   
2022-07-28 |  Enhancement -  
\- Mapped the field `auid` to about.user.userid'.  
\- Mapped the field `AUID` to `about.user.user_display_name`.  
\- Mapped the field `proctitle` to `target.process.file.full_path`.  
\- Enhanced the parser to parse the log with type=DAEMON_END, CRYPTO_SESSION, CONFIG_CHANGE, PROCTITLE, USER_ERR, CRYPTO_KEY_USER.  
\- Added conditional check for laddr, addr, cipher, pfs, direction, acct, pid, ppid, cmd, exe, ses.   
2022-06-17 |  Enhancement - Mapped/Modified the following fields :  
\- Changed mapping of `auid` from `security_result.about.user.userid` to `about.user.userid`.  
\- Changed `event_type` for type=SYSCALL from `SYSTEM_AUDIT_LOG_UNCATEGORIZED` to `USER_UNCATEGORIZED`.  
\- Mapped `success` to `security_result.summary`.  
\- Mapped `syscall`, `exit`, `tty`, `a0`, `a1`, `a2`, `a3` to `security_result.about.labels`.  
\- Dropped the logs in ASCII format.   
2022-06-14 |  Enhancement  
\- Enhanced the parser to parse the USER_CMD type of logs.  
\- Mapped the field `cmd` to `principal.process.command_line`.  
\- Mapped the field `ses` to `network.session_id`.  
\- Mapped the field `res` to `security_result.action` and `security_result.action_details`.  
\- Mapped the fields `auid` and `cwd` to `security_result.detection_fields`.   
2022-04-26 |  Enhancement  
\- Increased the parsing percentage by parsing all the unparsed logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
