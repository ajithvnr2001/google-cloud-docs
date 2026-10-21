---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-mail-changelog/
title: Change log for PROOFPOINT_MAIL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:15:19.473636+00:00
---

# Change log for PROOFPOINT_MAIL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-mail-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PROOFPOINT_MAIL

Date | Changes  
---|---  
2026-09-08 |  Enhancement:  
\- Added a grok pattern to parse new format of syslog logs.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Removed mapping of `emails` from `event.idm.read_only_udm.principal.user.email_addresses` UDM field since this field is not present in the raw logs.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Removed mapping of `headerReplyTo` raw log field from `event.idm.read_only_udm.target.user.email_addresses` UDM field to remove duplicate value mapping since `orig_recipient` is already mapped to `event.idm.read_only_udm.target.user.email_addresses`.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `headerReplyTo` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Removed mapping of `headerFrom` raw log field from `event.idm.read_only_udm.principal.user.email_addresses` UDM field to remove duplicate value mapping since `sender` is already mapped to `event.idm.read_only_udm.principal.user.email_addresses`.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `headerFrom` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `partData.sandboxStatus`, `messageParts_sandboxStatus` and `msgPart.sandboxStatus` raw log fields from `event.idm.read_only_udm.additional.fields` UDM field to remove duplicate value mapping since it contains sandbox analysis result.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `partData.sandboxStatus`, `messageParts_sandboxStatus` and `msgPart.sandboxStatus` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Removed mapping of `file` raw log field from `event.idm.read_only_udm.principal.process.file.full_path` UDM field since it is semantically correct mapping for an email attachment and process-related paths are meant for endpoint/host executions, not mail logs.  
\- `event.idm.read_only_udm.about.process.file.full_path`: Mapped `file` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Removed mapping of `name` raw log field from `event.idm.read_only_udm.principal.process.file.full_path` UDM field since it is semantically correct mapping for an email attachment and process-related paths are meant for endpoint/host executions, not mail logs.  
\- `event.idm.read_only_udm.about.process.file.full_path`: Mapped `name` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `msg.lookalikeDomains.name` raw log field from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field since this field is not present in the raw logs.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `msg.lookalikeDomains.registrar`,`clicks.phishScore`, `clicks.spamScore` and `clicks.malwareScore`, `clicks.impostorScore` and `clicks.quarantineFolder` raw log fields from `event.idm.read_only_udm.security_result.detection_fields` UDM field since this field is not present in the raw logs.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `folder`, `msg.lookalikeDomains.registeredDate`, `msg.lookalikeDomains.expiresDate` and `msg.lookalikeDomains.updatedDate` raw log fields from `event.idm.read_only_udm.additional.fields` UDM field since this field is not present in the raw logs.  
\- `event.idm.read_only_udm.security_result.rule_name`: Removed mapping of `clicks.quarantineRule` raw log field from `event.idm.read_only_udm.security_result.rule_name` UDM field since it is not present in the raw logs.  
\- `event.idm.read_only_udm.security_result.priority`: Removed mapping of `clicks.quarantineFolder` raw log field from `event.idm.read_only_udm.security_result.priority` UDM field since it is not present in the raw logs.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `smtputf8`,`clusterId`, `headerTo`, `msg.headerCC` and `msg.clusterId` raw fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `threats.campaignId` raw field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type to `EMAIL_TRANSACTION` only if network email to or from address is present.  
\- `event.idm.read_only_udm.metadata.event_type`: Removed `event.idm.read_only_udm.metadata.event_type` of `EMAIL_UNCATEGORIZED` since only mail_id details are present and network email to or from address is not present.   
2026-08-14 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Added support to parse `replyToAddress` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added email regex check for `clicks_sender` raw log field before mapping with `event.idm.read_only_udm.principal.user.email_addresses` and `event.idm.read_only_udm.network.email.from` UDM fields.   
2026-04-09 |  Enhancement:  
\- Provided support for new JSON format of clicks related logs.  
\- Added multiple gsub mutations on clicks_url field to replace Cyrillic characters with English characters.  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels`: If `threats_threatType` is equal to `messageText`, updated the value of key to `threatType`.  
\- `event.idm.read_only_udm.security_result.category_details`: Mapped `threatsInfoMap_classification` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Added conditional logic to set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_HTTP` if url details are present and principal machine data such as sender_ip and clicks_clickIP are present.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly set `event.idm.read_only_udm.metadata.event_type` to `EMAIL_TRANSACTION` if email details are present.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` if principal machine data such as sender_ip and clicks_clickIP are present.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly set `event.idm.read_only_udm.metadata.event_type to `GENERIC_EVENT` if no user or machine data is present.   
2026-03-06 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `value` (key: value), `query` (key: query), `rcode` (key: rcode), `rcpt` (key: rcpt), `rcpts` (key: rcpts), `sts` (key: sts), `msgs` (key: msgs), `resolve` (key: resolve), `reverse` (key: reverse), `clx_result_group` (key: clx_result_group), `clx_score` (key: clx_score), `clx_shade` (key: clx_shade), `score` (key: score), `threshold` (key: threshold), `warn` (key: warn), `reject` (key: reject), `sendmail_queue_id` (key: sendmail_queue_id), `envid` (key: envid) raw log fields with event.idm.read_only_udm.additional.fields UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `impostor_score` (key: impostor_score), `priority_score` (key: priority_score), `helo` (key: helo), `lint` (key: lint) raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added new Grok patterns to parse new format of syslog logs.  
\- Added support for date format for `ts` field.  
\- Added logic to handle comma-separated values in `rcpt`, `rcpts` raw log fields and map to `event.idm.read_only_udm.network.email.to` UDM field.  
\- Added regex checks for `rcpt` and `rcpts` to validate raw log fields as valid email addresses before mapping with `event.idm.read_only_udm.network.email.to` UDM field.  
\- Added regex check for `sts` to validate the raw log field as an integer before mapping with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- Added a gsub pattern to remove the UTF-8 character encoding from the `subj` field.   
2026-02-24 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Changed mapping for `event.idm.read_only_udm.metadata.event_timestamp` from `ts` to a prioritized extraction logic including `messageTime`, `clickTime`, `max_threat_time`, `threatTime`, `ts`, `date_log_rebase`, and `date_log` raw fields for syslog log format.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Removed `msg.threattime` raw field from `event.idm.read_only_udm.metadata.event_timestamp` UDM field for messageBlocked or messageDelivered events and `clicks.threattime` raw field from `event.idm.read_only_udm.metadata.event_timestamp` UDM field for clicksBlocked or clicksDelivered.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Changed mapping for `event.idm.read_only_udm.metadata.event_timestamp` from `msg.threattime` to a prioritized extraction logic including `msg.messageTime` and `max_threat_time` raw fields for messageBlocked or messageDelivered events.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Changed mapping for `event.idm.read_only_udm.metadata.event_timestamp` from `clicks.threattime` to a prioritized extraction logic including `clicks.clickTime` and `clicks.threattime` raw fields for clicksBlocked or clicksDelivered events.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `threatsInfoMap_threatTime` raw field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field if `messageTime` is not present for CEF log format.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `msg.suborgs.sender` and `msg.suborgs.rcpts` raw fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-02-19 |  Enhancement:  
\- `event.idm.read_only_udm.network.email.subject`: Enhanced Grok pattern for `msg.subject` and applied gsub transformations to remove UTF-8 character encodings and trailing spaces.   
2025-11-20 |  Enhancement:  
\- Initialized `completelyRewritten_detection_fields` to null to avoid the value being overwritten.   
2025-08-25 |  Enhancement:  
\- Added support for new format of JSON logs.  
\- `event1.idm.read_only_udm.metadata.event_type`: Added support for the event `EMAIL_TRANSACTION` and relevant corresponding raw log fields when `has_email` is equal to `true` or `messagesBlocked` is present or `messagesDelivered` is present.  
\- `event1.idm.read_only_udm.security_result.action`: Newly mapped `security_action` raw field to `BLOCK` with `event1.idm.read_only_udm.security_result.action` UDM field if `msg_quarantineRule` is equal to `inbound_phish` and `quarantineFolderField` is equal to `Phish`.   
2025-08-05 |  Enhancement:  
\- Parser overhaul version to make it more efficient and increase fields coverage. You can see the full list of changes in the parser documentation page https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-mail.   
2025-07-24 |  Enhancement:  
\- event1.idm.read_only_udm.metadata.event_timestamp: Removed mapping `msg.messageTime` raw log field with `event1.idm.read_only_udm.metadata.event_timestamp` UDM field, as it was not the most accurate timestamp, and replaced it with a more accurate mapping.  
\- event1.idm.read_only_udm.metadata.event_timestamp: Newly mapped `msg.threatsInfoMap.threatTime` raw log field with `event1.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-06-11 |  Enhancement:  
\- Added conditional check for email format:  
\- When `messagesBlocked.fromAddress` is being mapped with `event1.idm.read_only_udm.principal.user.email_addresses`.  
\- When `messagesBlocked.toAddresses` is being mapped with `event1.idm.read_only_udm.target.user.email_addresses`.  
\- When `messagesBlocked.recipient` is being mapped with `event1.idm.read_only_udm.network.email.to`.  
\- event1.idm.read_only_udm.metadata.collected_timestamp: Modified the mapping of `queryEndTime` raw log field to correctly parse for all the events then mapped with `event1.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event1.idm.read_only_udm.additional.fields: Newly mapped `messagesBlocked.QID` and `messagesBlocked.cluster` raw log field with `event1.idm.read_only_udm.additional.fields` UDM field.   
2025-05-16 |  Enhancement:  
\- Added gsub to replace `,,\`` with `,\`` from `message` field to parse the JSON logs.  
\- Initialized `messageTime_label` with empty strings to ensure proper data mapping in the `proofpoint_mail.include` file.   
2025-04-14 |  Enhancement:  
\- Added gsub to remove `\\`\\\`\\s+\\"` to parse the logs.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `queryEndTime_value` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped msg.messageTime raw log field with event.idm.read_only_udm.metadata.event_timestamp UDM field in the `proofpoint_mail.include` file.   
2025-04-03 |  Enhancement:  
\- Added gsub to remove `\\r\\n` to parse the logs.  
\- Added gsub to replace ``\`\`` with ``` to parse the logs.  
\- event1.idm.read_only_udm.additional.fields: Newly mapped `msg.id` raw log field with `event1.idm.read_only_udm.additional.fields` UDM field.   
2025-02-19 |  Enhancement:  
\- Added `gsub` to remove malformed characters from `clicks.url` for log parsing.  
\- Mapped `clickIP` to `principal.ip`, `principal.asset.ip`, and `security_result.about.ip`.   
2025-02-12 |  Enhancement:  
\- Mapped `modulesRun` to `additional.fields`.   
2025-02-10 |  Enhancement:  
\- Mapped `malwareScore`, `impostorScore`, `phishscore`, and `spamscore` to `strings`.   
2025-01-29 |  Enhancement:  
\- Mapped `click_time` to `additional.fields`.  
\- Added support to accept `email_addresses` if their length is less than 253, else drop them.   
2025-01-24 |  Enhancement:  
\- Changed mapping for `msg.disposition`, `msg.sandboxStatus`, and `msg.contentType` from `about.labels` to `additional.fields`.   
2025-01-03 |  Enhancement:  
\- Fixed mapping issue for `messageSize`, `impostorScore`, `malwareScore`, `spamScore`, and `phishScore`.  
\- Mapped `messageParts.disposition`, `messageParts.sandboxStatus`, and `messageParts.contentType` to `about.labels`.  
\- Mapped `detectionType` to `security_result.detection_fields`.  
\- Mapped `modulesRun` to `additional.fields`.   
2024-11-08 |  Enhancement:  
\- Added Grok pattern to remove `?UTF-8?Q?` and `?=` from `msg.subject`.  
\- Added Grok pattern to remove `=?UTF-8?Q?`, `?=`, and `=?UTF-8?B?Y21ibS5vcmc=?` from `msg.headerFrom`.  
\- Added `gsub` to remove `<>` from `msg.headerFrom`.   
2024-08-14 |  Enhancement:  
Mapped `xmailer` to `security_result.detection_fields`.   
2024-08-13 |  Enhancement:  
\- When `threats.classification` is `toad`, then mapped `threats.classification` to `security_result.category_details`.   
2024-07-30 |  Enhancement:  
\- Added a new Grok pattern to parse a new format of SYSLOG logs.   
2024-07-16 |  Enhancement:  
\- Changed mapping of `metadata.event_timestamp` from `msg.messageTime` to `clicks.threatTime`.  
\- Mapped `msg.messageTime` to `additional.fields`.   
2024-05-27 |  Enhancement:  
\- Mapped `msg.policyRoutes` to `additional.fields`.   
2024-04-03 |  Enhancement:  
\- Extracted `sender_domain` from `msg.fromAddress` and `clicks.sender`, and mapped to `principal.domain.name`.  
\- Mapped `clicks.sender` to `principal.user.email_addresses`.  
\- Mapped `clicks.recipient` to `target.user.email_addresses`.   
2023-06-26 |  Enhancement -  
\- Mapped `clicks.threatStatus` to `security_result.threat_status`.   
2022-11-03 |  Enhancement - Added condition check for date field .  
`give the higher priority to the date which has maximum timestamp`.  
if `click_time` > `threat_time` date mapped to click_time else threat_time.   
2022-07-13 |  Enhancement - Modified the mapping for `intermediary.user.email_addresses` from `(messagesBlocked|messagesDelivered).*toAddresses` to `(messagesBlocked|messagesDelivered).*ccAddresses` .   
2022-06-29 |  Enhancement - Added gsub to remove `<>` from the fields `clicks.messageID` and `m` mapped to `network.email.mail_id`.   
2022-05-25 |  Mapped `messageSize` to `additional` field.  
Mapped `campaignID` to `security_result.rule_id` field.  
Mapped `ccAddresses` to `intermediary.user.email_addresses` field.  
Mapped `toAddresses` to `target.user.email_addresses` field.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
