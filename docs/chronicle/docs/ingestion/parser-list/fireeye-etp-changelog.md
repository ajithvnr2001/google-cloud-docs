---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-etp-changelog/
title: Change log for FIREEYE_ETP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:02:25.178307+00:00
---

# Change log for FIREEYE_ETP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-etp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FIREEYE_ETP

Date | Changes  
---|---  
2026-06-11 |  Enhancement:  
\- Modified grok patterns to extract `ts`, `syslog_process`, `status_code_details`, `internal_id` and `msg_desc` fields.  
\- Added a new grok pattern on `msg_desc` field to extract `bytes` field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `ts` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.network.email.mail_id`: Newly mapped `original_msg_id` raw log field with `event.idm.read_only_udm.network.email.mail_id` UDM field when `original_msg_id` exceeds character limit.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `verdict_as`, `internal_id` and `status_code_details` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `msg_desc` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.   
2026-03-23 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.summary`: Removed mapping of `smtp-message.threat_type` raw log field from `event.idm.read_only_udm.security_result.summary` UDM field because the value represents the specific classification of the event as determined and categorized by the source product.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Mapped `smtp-message.threat_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `smtp-message.protocol` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-03-12 |  Enhancement:  
\- `event.idm.read_only_udm.principal.labels`: Removed mapping of `entry.attributes.email.smtp.rcpt_to` and `entry.attributes.email.smtp.mail_from` from `event.idm.read_only_udm.principal.labels` UDM field as it is deprecated.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `entry.attributes.email.smtp.rcpt_to` and `entry.attributes.email.smtp.mail_from` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.labels`: Removed mapping of `alert.smtp-message.last-malware`,`alert.smtp-message.protocol`,`alert.smtp-message.queue-id`,`alert.ack` from `event.idm.read_only_udm.target.labels` UDM field as it is deprecated.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `alert.smtp-message.last-malware`,`alert.smtp-message.protocol`,`alert.smtp-message.queue-id`,`alert.ack` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.labels`: Removed mapping of `mta_msg_id` from `event.idm.read_only_udm.target.labels` UDM field as it is deprecated.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `mta_msg_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.about.labels`: Removed mapping of `msg` from `event.idm.read_only_udm.about.labels` UDM field as it is deprecated.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `msg` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `domain` from `event.idm.read_only_udm.additional.fields` UDM field as it provides context for security analysis and having it in the general additional.fields is not preferred.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `domain` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `original` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `alert_date` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.ip`,`event.idm.read_only_udm.principal.asset.ip`: Newly mapped `smtp-message.ip_address` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `smtp-message.threat_type` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `smtp-message.threat_type_description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.network.email.to`: Newly mapped `email-header.to`,`smtp-message.to` raw log field with `event.idm.read_only_udm.network.email.to` UDM field.  
\- `event.idm.read_only_udm.network.email.from`: Newly mapped `email-header.from` raw log field with `event.idm.read_only_udm.network.email.from` UDM field.  
\- `event.idm.read_only_udm.network.email.cc`: Newly mapped `email-header.cc` raw log field with `event.idm.read_only_udm.network.email.cc` UDM field.  
\- `event.idm.read_only_udm.network.email.subject`: Newly mapped `email-header.subject` raw log field with `event.idm.read_only_udm.network.email.subject` UDM field.  
\- `event.idm.read_only_udm.network.email.mail_id`: Newly mapped `email-header.message-id` raw log field with `event.idm.read_only_udm.network.email.mail_id` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `malware.name` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_id`: Newly mapped `malware.stype` raw log field with `event.idm.read_only_udm.security_result.threat_id` UDM field.  
\- `event.idm.read_only_udm.security_result.about.file.sha256`: Newly mapped `sha256` raw log field with `event.idm.read_only_udm.security_result.about.file.sha256` UDM field.  
\- `event.idm.read_only_udm.security_result.about.file.md5`: Newly mapped `md5` raw log field with `event.idm.read_only_udm.security_result.about.file.md5` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `email_status` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `email_status` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.verdict_info.verdict_response`: If `verdict` is `Malicious`, updated the value of `event.idm.read_only_udm.security_result.verdict_info.verdict_response` to `MALICIOUS`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `smtp-message.from`,`smtp-message.last-malware`,`smtp-message.country`,`smtp-message.queue-id`,`ack` and `is_read` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-11-28 |  Enhancement:  
\- `event.idm.read_only_udm.target.file.names`: Removed mapping of `malwareValue_name` from `event.idm.read_only_udm.target.file.names` UDM field since it was a rule_name and related to security_result UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Mapped `malwareValue_name` raw log field to `event.idm.read_only_udm.security_result.rule_name` UDM field in order to map it to the appropriate UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `alert.smtp-message.threat_type_description`, `custom.riskware_action` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `custom.riskware_result`, `alert_type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_type`: Conditional mapping applied based on `malwareValue_name`:  
\- Mapped to `APT` if `malwareValue_name` contains `APT`.  
\- Mapped to `APT` if `malwareValue_name` contains `APTFIN`.  
\- Mapped to `POS` if `malwareValue_name` contains `POS`.  
\- `event.idm.read_only_udm.network.email.from`: Added length validation (must be between 1 and 256 characters) to the conditional mapping for the following raw fields `smtp_from`, `email.smtp.mail_from`, `send_email`, `alert.email-header.from`, `alert.smtp-message.from`, `alert.src.smtp-mail-from`.   
2025-09-22 |  Enhancement:  
\- event.idm.read_only_udm.network.direction: Newly mapped `traffic_type` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `domain_id`, 'object_uuid`, `product`, `client_id`, `accepted_time`, `alert_date`, `domain` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `custom`, `alert.smtp-message.threat_type` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.network.email.cc: Newly mapped `alert.email-header.cc` raw log field with `event.idm.read_only_udm.network.email.cc` UDM field.  
\- event.idm.read_only_udm.principal.domain.name: Extracted `extracted_domain` from `alert.src.url` raw log field and mapped it with `event.idm.read_only_udm.principal.domain.name` UDM field.  
\- event.idm.read_only_udm.target.domain.name: Extracted `extracted_domain` from `alert.src.url` raw log field and mapped it with `event.idm.read_only_udm.target.domain.name` UDM field.  
\- Added conditional check for `entry.attributes.email.source_ip`, `ip_value`, `src_ip_value` before mapping to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.  
\- Added conditional check for `alert.smtp-message.to` values to validate email format.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal` is `true` or `has_principal_ip` is `true`, updated to `SCAN_UNCATEGORIZED`.  
\- event.idm.read_only_udm.metadata.event_type: If none of the preceding conditions are met, updated to `GENERIC_EVENT`.  
\- Added logic to iterate through fields in the `custom` map, prefix each key with `custom_`, and map them as key-value pairs within `event.idm.read_only_udm.security_result.detection_fields`\- efactored event.idm.read_only_udm.metadata.vendor_name, event.idm.read_only_udm.metadata.product_name, and event.idm.read_only_udm.network.application_protocol to be set unconditionally in a single block.   
2025-07-10 |  Enhancement:  
\- Added grok pattern to parse new format of Syslog logs.  
\- event.idm.read_only_udm.security_result.detection_fields: Converted `email_size` into string to properly populate the `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `action_yara`, `verdict_yara` and `delivery_timestamp` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `syslog_process` and `timestamp` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Set `event_type1` to `NETWORK_CONNECTION` if principal and target is present else if only principal is present then set `event_type1` to `STATUS_UPDATE`.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `usr_display_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- Added regex check for email address to avoid parsing failure when `header_from` is being mapped to `event.idm.read_only_udm.principal.user.email_addresses` UDM field.   
2025-05-23 |  Enhancement:  
\- Added conditional check if `message` is not starting with `accepted_time` to avoid dropping the logs.  
\- event.idm.read_only_udm.additional.fields : Newly mapped `is_retro` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added Gsub function on `alert.email-header.to` to convert the string to array.  
\- Replaced `\\s+' with ``.  
\- Replaced `<` with ``,`<`.  
\- Replaced `>,` with `>`,``.  
\- Replaced `\\]}` with `"]}`.  
\- Replaced `:\\[` with `:["`.  
\- Replaced `\`\`` with `\"`.  
\- Replaced `,,` with `,`.  
\- Added grok pattern for `alert.email-header.to` raw log field to extract email address.  
\- event.idm.read_only_udm.target.user.email_addresses: Newly mapped `alert.email-header.to` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- Added character limit conditional check on `alert.email-header.to` raw log.   
2025-04-21 |  Enhancement:  
\- Added Gsub to replace ``\\\s+`to`` with ``,`to`` on `message` to parse the logs.  
\- Initialised `about.file.full_path`.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `alert.action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.target.file.first_seen_time: Newly mapped `alert.attack-time` raw log field with `event.idm.read_only_udm.target.file.first_seen_time` UDM field.  
\- event.idm.read_only_udm.target.user.email_addresses: Newly mapped `alert.dst.smtp-to` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.network.email.from: Newly mapped `alert.email-header.from` raw log field with `event.idm.read_only_udm.network.email.from` UDM field.  
\- event.idm.read_only_udm.network.email.mail_id: Newly mapped `alert.email-header.message-id` raw log field with `event.idm.read_only_udm.network.email.mail_id` UDM field.  
\- event.idm.read_only_udm.network.email.subject: Newly mapped `alert.email-header.subject` raw log field with `event.idm.read_only_udm.network.email.subject` UDM field.  
\- event.idm.read_only_udm.target.user.email_addresses: Newly mapped `alert.email-header.to` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.target.labels: Newly mapped `alert.ack` raw log field with `event.idm.read_only_udm.target.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `alert.explanation.malware-detected.malware.application` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `alert.explanation.malware-detected.malware.downloaded-at` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `alert.explanation.malware-detected.malware.executed-at` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.file.md5: Newly mapped `alert.explanation.malware-detected.malware.md5sum` raw log field with `event.idm.read_only_udm.target.file.md5` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `alert.explanation.malware-detected.malware.md5sum` raw log field with `event.idm.read_only_udm.additional.fields` UDM field if `event.idm.read_only_udm.target.file.md5` is already set.  
\- event.idm.read_only_udm.target.file.names: Newly mapped `alert.explanation.malware-detected.malware.name` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `alert.explanation.malware-detected.malware.original` raw log field with `event.idm.read_only_udm.target.url` UDM field if `alert.explanation.malware-detected.malware.type` is `url`.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `alert.explanation.malware-detected.malware.original` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `alert.explanation.malware-detected.malware.original` raw log field with `event.idm.read_only_udm.additional.fields` UDM field if `event.idm.read_only_udm.target.file.full_path` is already set.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `alert.explanation.malware-detected.malware.profile` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.file.sha256: Newly mapped `alert.explanation.malware-detected.malware.sha256` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `alert.explanation.malware-detected.malware.sha256` raw log field with `event.idm.read_only_udm.additional.fields` UDM field if `event.idm.read_only_udm.target.file.sha256` is already set.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `alert.explanation.malware-detected.malware.stype` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.file.first_submission_time: Newly mapped `alert.explanation.malware-detected.malware.submitted-at` raw log field with `event.idm.read_only_udm.target.file.first_submission_time` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `alert.explanation.malware-detected.malware.type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `alert.interface.interface` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `alert.interface.mode` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `alert.name` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `alert.occurred` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `alert.sc-version` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.severity UDM field,event.idm.read_only_udm.severity_details: Newly mapped `alert.severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field and `event.idm.read_only_udm.severity_details` UDM field.  
If `alert.severity` is `crit` then mapped `event.idm.read_only_udm.security_result.severity` to `CRITICAL` and `event.idm.read_only_udm.security_result.risk_score` to `5.0`.  
If `alert.severity` is `majr` then mapped `event.idm.read_only_udm.security_result.severity` to `HIGH` and `event.idm.read_only_udm.security_result.risk_score` to `10.0`.  
If `alert.severity` is `unkn` then mapped `event.idm.read_only_udm.security_result.severity` to `UNKNOWN_SEVERITY` and `event.idm.read_only_udm.security_result.risk_score` to `5.0`.  
If `alert.severity` is `minr` then mapped `event.idm.read_only_udm.security_result.severity` to `MEDIUM` and `event.idm.read_only_udm.security_result.risk_score` to `5.0`.  
If `alert.severity` is `low` then mapped `event.idm.read_only_udm.security_result.severity` to `LOW`.  
\- event.idm.read_only_udm.intermediary.location.country_or_region: Newly mapped `alert.smtp-message.country` raw log field with `event.idm.read_only_udm.intermediary.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `alert.smtp-message.date` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `alert.smtp-message.from` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `alert.smtp-message.ip_address` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.target.labels: Newly mapped `alert.smtp-message.last-malware` raw log field with `event.idm.read_only_udm.target.labels` UDM field.  
\- event.idm.read_only_udm.target.labels: Newly mapped `alert.smtp-message.protocol` raw log field with `event.idm.read_only_udm.target.labels` UDM field.  
\- event.idm.read_only_udm.target.labels: Newly mapped `alert.smtp-message.queue-id` raw log field with `event.idm.read_only_udm.target.labels` UDM field.  
\- event.idm.read_only_udm.network.email.to: Newly mapped `alert.smtp-message.to` raw log field with `event.idm.read_only_udm.network.email.to` UDM field.  
\- event.idm.read_only_udm.principal.administrative_domain: Newly mapped `alert.src.domain` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `alert.src.smtp-mail-from` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `alert.uuid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `mitre_mapping.bale.bale_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `mitre_mapping.bale.name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `mitre_mapping.bale.os_change_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `mitre_mapping.bale.severity` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `mitre_mapping.bale.description` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.attack_details.techniques: Newly mapped `mitre_mapping.bale.id` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques` UDM field.  
\- event.idm.read_only_udm.security_result.attack_details.tactics: Newly mapped `tactics_data` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics` UDM field.  
\- event.idm.read_only_udm.principal.url,event.idm.read_only_udm.additional.fields: Newly mapped `alert.src.url` raw log field with `event.idm.read_only_udm.principal.url` UDM field if `alert.explanation.malware-detected.malware.type` is `url` else mapped it to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.labels: Newly mapped `mta_msg_id` raw log field with `event.idm.read_only_udm.target.labels` UDM field.  
\- event.idm.read_only_udm.about.labels: Newly mapped `msg` raw log field with `event.idm.read_only_udm.about.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `parent_uuid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.verdict_info: Newly mapped `verdict` raw log field with `event.idm.read_only_udm.security_result.verdict_info` UDM field and `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `report_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `object_uuid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2024-08-14 |  Enhancement:  
\- Added Grok pattern for a new pattern of JSON logs.  
\- Mapped `type`, `InternalId`, `attributes.acceptedDateTime`, `attributes.lastModifiedDateTime`, `attributes.senderSMTP`, `attributes.status`, and `attributes.urlDomains` to `additional.fields`.  
\- Mapped `attributes.countryCode` to `principal.location.country_or_region`.  
\- Mapped `attributes.senderIP` to `principal.ip`.  
\- Mapped `attributes.recipientSMTP` to `network.email.to`.  
\- Mapped `attributes.senderHeader` to `network.email.from`.  
\- Mapped `attributes.subject` to `network.email.subject`.  
\- Mapped `attributes.domain` to `network.dns_domain`.   
2024-08-08 |  Enhancement:  
\- Added a new Grok pattern to parse unparsed SYSLOG logs.   
2024-03-07 |  Enhancement:  
\- Mapped `alert.attributes.alert.malware_md5` to `about.file.md5`.   
2024-01-30 |  Enhancement:  
\- Added support for new pattern of JSON logs.  
\- Mapped `id`, `alert.explanation.analysis`,`alert.explanation.malware_os_analysis`,`email.dod_report_id` and `email.status` to `security_result.detection_fields`.  
\- Mapped `alert.malware_md5` to `about.file.md5`.  
\- Mapped `alert.sha256` to `about.file.sha256`.  
\- Mapped `email.attachment` to `about.file.full_path`.  
\- When `email.attachment` is valid URL, then mapped it to `about.url`.  
\- Mapped `alert.severity` to `security_result.severity`.  
\- Mapped `email.smtp.mail_from` to `network.email.from`.  
\- Mapped `email.smtp.recipients` to `network.email.to`.  
\- Mapped `email.headers.subject` to `network.email.subject`.  
\- Mapped `email.source_ip` to `principal.ip` and `principal.asset_ip`.  
\- Mapped `alert.explanation.malware_detected.malware.threat_type` to `security_result.category`.  
\- Mapped `alert.explanation.malware_detected.malware.trace_iden` to `security_result.threat_id`.  
\- Mapped `alert.explanation.malware_detected.malware.name` to `security_result.threat_name`.  
\- Mapped `email.source_country` to `principal.location.country_or_region`.  
\- Mapped `alert.action` to `security_result.action`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
