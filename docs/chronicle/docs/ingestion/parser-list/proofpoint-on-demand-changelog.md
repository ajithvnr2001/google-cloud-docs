---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-on-demand-changelog/
title: Change log for PROOFPOINT_ON_DEMAND \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:47.720745+00:00
---

# Change log for PROOFPOINT_ON_DEMAND  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-on-demand-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PROOFPOINT_ON_DEMAND

Date | Changes  
---|---  
2026-06-02 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.action`: If `filter.disposition` value is `accept`, `CLEAR`, `OK`, or `redirect` then set `event.idm.read_only_udm.security_result.action` to `ALLOW`.  
\- `event.idm.read_only_udm.security_result.action`: If `filter.disposition` value is `reject` then set the value of `event.idm.read_only_udm.security_result.action` to `BLOCK`.  
\- `event.idm.read_only_udm.security_result.action`: If `filter.disposition` value is `quarantine` then set the value of `event.idm.read_only_udm.security_result.action` to `QUARANTINE`.  
\- `event.idm.read_only_udm.security_result.action`: If `filter.disposition` value is `FAIL` or `TEMP` then set the value of `event.idm.read_only_udm.security_result.action` to `FAIL`.  
\- `event.idm.read_only_udm.security_result.action`: If `filter.disposition` value is `hold` or `retry` then set the value of `event.idm.read_only_udm.security_result.action` to `CHALLENGE`.   
2026-05-15 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Removed mapping of `msg.parsedAddresses.from` from `event.idm.read_only_udm.principal.user.email_addresses` UDM field as this field represents the sender of the email.  
\- `event.idm.read_only_udm.network.email.from`: Newly mapped `msg.parsedAddresses.from` raw log field with `event.idm.read_only_udm.network.email.from` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Removed mapping of `msgs.urls.url` from `event.idm.read_only_udm.principal.user.email_addresses` UDM field when it is a valid email address as this field doesn't represent the email address of the user.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `msgs.urls.url` raw log field with `event.idm.read_only_udm.additional.fields` UDM field when it is a valid email address.   
2026-05-08 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.category`: If `triggeredClassifier` is `spam` and `event.idm.read_only_udm.metadata.event_type` is `EMAIL_TRANSACTION`, then set the value of `event.idm.read_only_udm.security_result.category` to `MAIL_SPAM`.  
\- `event.idm.read_only_udm.security_result.category`: If `triggeredClassifier` is `phish` and `event.idm.read_only_udm.metadata.event_type` is `EMAIL_TRANSACTION`, then set the value of `event.idm.read_only_udm.security_result.category` to `MAIL_PHISHING`.  
\- `event.idm.read_only_udm.security_result.category`: If `triggeredClassifier` is `phish`, and `event.idm.read_only_udm.metadata.event_type` is not `EMAIL_TRANSACTION`, then set the value of `event.idm.read_only_udm.security_result.category` to `PHISHING`.  
\- `event.idm.read_only_udm.security_result.category`: If `triggeredClassifier` is `spoof` and `event.idm.read_only_udm.metadata.event_type` is `EMAIL_TRANSACTION`, then set the value of `event.idm.read_only_udm.security_result.category` to `MAIL_SPOOFING`.  
\- `event.idm.read_only_udm.security_result.category`: If `triggeredClassifier` is `malicious` or `malware`, then set the value of `event.idm.read_only_udm.security_result.category` to `NETWORK_MALICIOUS`.  
\- `event.idm.read_only_udm.security_result.category`: If `triggeredClassifier` is `suspicious`, then set the value of `event.idm.read_only_udm.security_result.category` to `NETWORK_SUSPICIOUS`.  
\- `event.idm.read_only_udm.security_result.category`: If `triggeredClassifier` is `auth`, then set the value of `event.idm.read_only_udm.security_result.category` to `AUTH_VIOLATION`.  
\- `event.idm.read_only_udm.security_result.category`: If `triggeredClassifier` is `EXPLOIT`, then set the value of `event.idm.read_only_udm.security_result.category` to `EXPLOIT`.  
\- `event.idm.read_only_udm.security_result.category`: If `triggeredClassifier` is `policy`, then set the value of `event.idm.read_only_udm.security_result.category` to `POLICY_VIOLATION`.   
2026-04-16 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `pps` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `pps.agent` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- Added a grok pattern to extract valid IP values from `sm.relay` raw log field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `sm.relay` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field if it contains valid IP address else mapped to `event.idm.read_only_udm.intermediary.hostname` UDM field.   
2026-03-11 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `msgUrls.url` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- Added a grok pattern on `msgUrls.url` to extract `from_mail`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `msgs.metadata.application`, `msgs.metadata.appname`, `msgs.metadata.pagecount`, `msgs.metadata.createdate`, `msgs.metadata.modifydate`, `msgs.metadata.documentid`, `msgs.metadata.instanceid`, `msgs.metadata.subject`, `msgs.metadata.title`, `msgs.metadata._PROOFPOINT_CONTENT_LENGTH_`, `filter.modules.urldefense.counts.noRewriteIsEmail` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields` : Added a conditional check for `displayName` to avoid null values getting mapped to `event.idm.read_only_udm.additional.fields`.   
2026-03-10 |  Enhancement:  
\- `event.idm.read_only_udm.about.labels`: Removed mapping of `msgPart.sandboxStatus`, `msgPart.isProtected`, `msgPart.detectedName`, `msgPart.labeledName`, `filter.modules.regulation.rules.name` from `event.idm.read_only_udm.about.labels` UDM field as this is a deprecated UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `msgPart.sandboxStatus`, `msgPart.isProtected`, `msgPart.detectedName`, `msgPart.labeledName` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field since this is the recommended transition UDM field for the deprecated `event.idm.read_only_udm.about.labels` UDM.  
\- `event.idm.read_only_udm.about.resource.attribute.labels`: Removed mapping of `filter.modules.regulation.rules.name` from `event.idm.read_only_udm.about.resource.attribute.labels` UDM field as the values are already mapped to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.labels`: Removed mapping of `metadata.customerId` from `event.idm.read_only_udm.principal.labels` UDM field as this is a deprecated UDM field.   
2026-02-26 |  Enhancement:  
\- `event.idm.read_only_udm.about.file.full_path`: Newly mapped `messagesBlocked.msgParts.labeledName` raw log field with `event.idm.read_only_udm.about.file.full_path` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `msg.header.subject`, `filter.modules.spam.authority.isTruncated`, `filter.modules.spam.authority.score`, `filter.modules.urldefense.version.engine`, `filter.modules.urldefense.counts.unique`, `filter.modules.urldefense.counts.unrewritten` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `msgUrls.src`, `filter.quarantine.expirationTs` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-02-10 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped as `SEND_MAIL` if logs contain `sendmail` keyword, or `FILTER` if logs contain `filter` keyword to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `sm_stat` raw log field to `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `sm.delay`, `sm.messageTs`, `sm.pri`, `sm.dsn`, `sm.xdelay`, `id`, `metadata.origin.data.theater`, and `metadata.origin.schemaVersion` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `sm.guid` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field when message contains `sendmail` keyword.   
2026-02-04 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `messagesBlocked.senderIP` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `messagesBlocked.sender` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.network.email.subject`: Newly mapped `messagesBlocked.subject` raw log field with `event.idm.read_only_udm.network.email.subject` UDM field.  
\- `event.idm.read_only_udm.about.file.sha256`: Newly mapped `messagesBlocked.msgParts.sha256` raw log field with `event.idm.read_only_udm.about.file.sha256` UDM field.  
\- `event.idm.read_only_udm.about.file.md5`: Newly mapped `messagesBlocked.msgParts.md5` raw log field with `event.idm.read_only_udm.about.file.md5` UDM field.  
\- `event.idm.read_only_udm.about.file.mime_type`: Newly mapped `messagesBlocked.msgParts.labeledMime`, `messagesBlocked.msgParts.contentType` raw log field(s) with `event.idm.read_only_udm.about.file.mime_type` UDM field.  
\- `event.idm.read_only_udm.about.file.full_path`: Newly mapped `messagesBlocked.msgParts.filename` raw log field with `event.idm.read_only_udm.about.file.full_path` UDM field.  
\- `event.idm.read_only_udm.about.labels`: Newly mapped `messagesBlocked.msgParts.sandboxStatus`, `messagesBlocked.msgParts.isProtected`, `messagesBlocked.msgParts.detectedName`, `messagesBlocked.msgParts.labeledName` raw log field(s) with `event.idm.read_only_udm.about.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `messagesBlocked.messageID`, `messagesBlocked.spamScore`, `messagesBlocked.phishScore`, `messagesBlocked.impostorScore`, `messagesBlocked.malwareScore`, `messagesBlocked.cluster`, `messagesBlocked.quarantineFolder`, `messagesBlocked.quarantineRule`, `messagesBlocked.messageSize`, `messagesBlocked.headerFrom`, `messagesBlocked.id`, `messagesBlocked.QID`, `messagesBlocked.GUID`, `messagesBlocked.threatsInfoMap.threatID`, `messagesBlocked.threatsInfoMap.threatStatus`, `messagesBlocked.threatsInfoMap.classification`, `messagesBlocked.threatsInfoMap.threatUrl`, `messagesBlocked.threatsInfoMap.threat`, `messagesBlocked.threatsInfoMap.threatType`, `quarantineRule`, `quarantineFolder` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `quarantineRule` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `policyRoutes`, `modulesRun` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-01-06 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `msg.header.x-originatororg`, `msg.parsedAddresses.fromDisplayNames`, `filter.modules.dmarc.records`, `filter.modules.spam.authority.analysis`, `filter.isMsgSplit`, `filter.splitType`, `filter.delivered.rcpts`, `filter.isMsgReinjected`, `filter.reinjectedType`, `msg.lang`, and `msg.header.x-originatororg` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `filter.modules.spam.triggeredClassifier` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Changed mapping for event.idm.read_only_udm.security_result.detection_fields from `isRewritten:%{msgUrls.isRewritten}` key to `url` key UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `filter.verified.rcpts`, `filter.modules.dkimv`, `filter.modules.pdr.v2.response`, `filter.modules.spam.authority.sigs` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-10-31 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.email_addresses`: Improved handling for multiple email addresses in `msg.header.to.0`. The raw field is now split by commas, from each resulting string, and each email address is individually merged into the `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `metadata.origin.data.mode`, `connection.resolveStatus`, `connection.tls.inbound.cipherBits`, `msg.sizeBytes`, `filter.msgSizeBytes`, `filter.suborgs.sender`, `filter.durationSecs`, `filter.aliasedRcpts`, `filter.suborgs.rcpts` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.smtp.helo`: Newly mapped `connection.helo` raw log field with `event.idm.read_only_udm.network.smtp.helo` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `connection.sid`, `filter.actions.isFinal` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `metadata.origin.data.theater` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.   
2025-10-02 |  Enhancement:  
\- Added conditional check for the check1 field to populate `action_field_.value.string_value` when the value is accept, continue, discard, redirect, reject, or retry.   
2025-09-05 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Reverted the changes to modify mappings for `filter.actions.rules`, `filter.actions.module` and `filter.actions.action` raw log fields from `event.idm.read_only_udm.additional.fields` list to `event.idm.read_only_udm.additional.fields` index based mapping.   
2025-07-17 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Added support to modify mappings for `filter.actions.rules`, `filter.actions.module` and `filter.actions.action` raw log fields from `event.idm.read_only_udm.additional.fields` index based mapping to `event.idm.read_only_udm.additional.fields` list.  
\- Refactored the logic for populating additional.fields from filter.actions, filter.modules.regulation.rules, and msgParts loops to aggregate values into lists before merging into additional.fields outside the loops.  
\- Added initialization for list variables `action_rules_list`, `action_modules_list`, `action_actions_list`, `rule_list`, `severity_list`, `detected_ext_list`.  
\- Added conditional checks to ensure lists are not empty before merging them into `event1.idm.read_only_udm.additional.fields`.   
2025-07-10 |  Enhancement:  
\- Added a condition to check if `isFinal` is `true`, then map `module` and `rule` fields to `event.idm.read_only_udm.security_result.detection_fields` else kept the original mapping to `event.idm.read_only_udm.additional.fields`.   
2025-04-08 |  Enhancement:  
\- event.idm.read_only_udm.network.email.subject: Removed mapping of `msg.header.subject` from `event.idm.read_only_udm.network.email.subject` UDM field.  
\- event.idm.read_only_udm.network.email.subject: Mapped `msg.normalizedHeader.subject` raw log field with `event.idm.read_only_udm.network.email.subject` UDM field.   
2025-02-26 |  Enhancement:  
\- Mapped `audit.user.id` to `principal.user.userid`.  
\- Mapped `audit.user.ipAddress` to `principal.asset.ip` and `principal.ip`.  
\- Mapped `audit.user.email` to `principal.user.email_addresses`.  
\- Mapped `audit.resourceType` to `target.resource.name`.  
\- Mapped `audit.action` to `sec_result.attribute.labels`.  
\- Mapped `audit.level` to `security_result.severity_details`.  
\- Mapped `audit.tags` to `sec_result.detection_fields`.   
2025-02-19 |  Enhancement:  
\- Mapped `filter.modules.regulation.rules.name` to `about.resource.attribute.labels and `about.labels".   
2025-02-12 |  Enhancement:  
\- Mapped `filter.actions.action` to `additional.fields`.  
\- Mapped `filter.actions.module` to `additional.fields`.   
2025-01-24 |  Enhancement:  
\- Mapped `filter.actions.rule` to `additional.fields`.   
2025-01-23 |  Enhancement:  
\- Mapped `filter.modules.dmarc.authResults.*` to `additional.fields`.   
2024-12-18 |  Enhancement:  
\- Mapped `filter.modules.regulation.rules.name` and `filter.modules.regulation.rules.severity` to `additional.fields`.   
2024-11-28 |  Enhancement:  
\- Mapped `msgParts.metadata.company` and `msgParts.metadata.author` to `security_result.detection_fields`.  
\- Removed duplicate mapping of `email.subject`.  
\- Changed mapping of `filter.modules.dmarc.authResults.*` fields from `additional.fields` to `security_result.detection_fields`.   
2024-08-28 |  Enhancement:  
\- Changed `security_result.detection_fields` key from `filterQid` to `qid`.   
2024-08-21 |  Enhancement:  
\- Mapped `metadata.origin.data.cid` to `additional.fields`.   
2024-07-22 |  Enhancement:  
\- If `about.file.size` is a valid Unsigned Integer, then mapped `msgPart.detectedSizeBytes` to `about.file.size`.  
\- Added support for new pattern of SYSLOG logs.   
2024-07-09 |  Enhancement:  
\- Mapped `msg.header.x-mailer` to `additional.fields`.   
2023-11-13 |  Enhancement:  
\- Mapped `subject` to `network.email.subject`.  
\- Mapped `messageID` to `network.email.mail_id`.  
\- Mapped `fromAddress` to `network.email.from`.  
\- Mapped `ccAddresses` to `network.email.cc`.  
\- Mapped `replyToAddress` to `network.email.reply_to`.  
\- Mapped `toAddresses` to `network.email.to`.  
\- Mapped `sender` to `principal.user.email_addresses`.  
\- Mapped `senderIP` to `principal.ip`.  
\- Mapped `recipient` to `target.user.email_addresses`.  
\- Mapped `spamScore`, `phishScore`, `threatsInfoMap`, `impostorScore`, `malwareScore`, "` to `security_result.detection_fields".   
2023-10-26 |  Enhancement:  
\- Mapped `msg.headeparsedAddressesr.from.0` to `principal.user.email_addresses`.  
\- Modified mappings from using deprecated UDM fields to alternative fields.  
\- Added mapping from `about.labels` to `about.resource.attribute.labels`.  
\- Added mapping from `principal.labels` to `principal.resource.attribute.labels`.   
2023-06-05 |  \- Added check to `msg.header.reply-to.0` prior mapping to UDM to check if it is any array of emails.  
\- Added not `-1` check to `msgPart.detectedSizeBytes` prior mapping to UDM.   
2022-07-14 |  Enhancement to map following element to UDM element:  
Mapped langs to additional.fields.  
Mapped definitions to security_result.summary.  
Mapped engine to metadata.product_version.   
2022-06-29 |  Enhancement - Added gsub to remove `<>` from the fields `sm.msgid` and `msg.header.message-id.0` mapped to `network.email.mail_id`.   
2022-05-20 |  Enhancement to map following elements to UDM elements:  
Mapped `tls.verify`, `filter.disposition` to `security_result.action_details`.  
Mapped `filter.modules.dmarc.authResults.result` to `additional.fields`.  
Mapped `filter.quarantine.module`, `filter.quarantine.folder`, `filter.quarantine.type`, `filter.quarantine.folderId`, `filter.modules.spam.scores.overall`, `filter.modules.spam.scores.engine`, `filter.modules.spam.scores.classifiers.spam`, `filter.modules.spam.scores.classifiers.mlxlog`, `filter.modules.spam.scores.classifiers.phish`, `filter.modules.spam.scores.classifiers.impostor`, `filter.modules.spam.scores.classifiers.lowpriority`, `filter.modules.spam.scores.classifiers.mlx`, `filter.modules.spam.scores.classifiers.bulk`, `filter.modules.spam.scores.classifiers.suspect`, `filter.modules.spam.scores.classifiers.malware`, `filter.modules.spam.scores.classifiers.adult` to `security_result.detection_fields`.   
2022-04-13 |  Enhancement to map following element to UDM element:  
Mapped filter.modules.av.virusNames to `security_result.threat_name`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
