---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mimecast-mail-v2-changelog/
title: Change log for MIMECAST_MAIL_V2 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:54:05.116930+00:00
---

# Change log for MIMECAST_MAIL_V2  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mimecast-mail-v2-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MIMECAST_MAIL_V2

Date | Changes  
---|---  
2026-03-02 |  Enhancement:  
\- `event.idm.read_only_udm.about.file.full_path`: Removed mapping of `new_fileName` from `event.idm.read_only_udm.about.file.full_path` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.target.file.full_path`: Mapped `new_fileName` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.about.file.mime_type`: Removed mapping of `new_fileMime` from `event.idm.read_only_udm.about.file.mime_type` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.target.file.mime_type`: Mapped `new_fileMime` raw log field with `event.idm.read_only_udm.target.file.mime_type` UDM field.  
\- `event.idm.read_only_udm.about.file.sha256`: Removed mapping of `new_sha256` from `event.idm.read_only_udm.about.file.sha256` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.target.file.sha256`: Mapped `new_sha256` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- `event.idm.read_only_udm.about.file.md5`: Removed mapping of `new_md5` from `event.idm.read_only_udm.about.file.md5` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.target.file.md5`: Mapped `new_md5` raw log field with `event.idm.read_only_udm.target.file.md5` UDM field.  
\- `event.idm.read_only_udm.about.file.sha1`: Removed mapping of `new_sha1` from `event.idm.read_only_udm.about.file.sha1` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.target.file.sha1`: Mapped `new_sha1` raw log field with `event.idm.read_only_udm.target.file.sha1` UDM field.   
2025-12-31 |  Enhancement:  
\- `event.idm.read_only_udm.network.email.to`: Newly mapped `recipient` raw log field with `event.idm.read_only_udm.network.email.to' UDM field.   
2025-12-03 |  Enhancement:  
\- event.idm.read_only_udm.target.user.userid: Removed mapping of `data.accountId` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field in order to introduce a more accurate mapping for the raw log fields.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `data.accountId` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `route` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-10-24 |  Enhancement:  
\- event.idm.read_only_udm.security_result.action: Newly Mapped `new_delivered` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly Mapped `new_deliveryErrors` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `new_urlCategory` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.principal.asset.category: Newly Mapped `new_asset_category` raw log field with `event.idm.read_only_udm.principal.asset.category` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly Mapped `new_blockReason` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.action: Updated the mapping logic for `new_action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `new_route` raw log field with `event.idm.read_only_udm.additional.fields` UDM field if it is not null.  
\- Added a grok check to properly parse the email address for `new_senderEnvelope` and `new_senderHeader` fields.   
2025-07-17 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped spf.allow, spf.info, dkim.allow, dkim.info, dmarc.allow, dmarc.info, rbl.allow, rbl.info, greyEmail, managedSender.allow, and managedSender.info raw log fields to event.idm.read_only_udm.security_result.detection_fields.  
\- Refactored the parser logic to use a for loop to handle the mapping of `permittedSender.allow`, `permittedSender.info`, `managedSender.allow`, `managedSender.info`, `spf.allow`, `spf.info`, `dkim.allow`, `dkim.info`, `dmarc.allow`, `dmarc.info`, `rbl.allow`, `rbl.info`, `greyEmail`, `numberAttachments`, `subtypes`, `delivered`, `receiptErrors`, `attachments`, `totalSizeAttachments`, `senderDomainInternal`, `deliveryTime` and `deliveryAttempts` fields to additional.fields and security_result.detection_fields, improving code maintainability.   
2025-07-10 |  Enhancement:  
\- Modified the Grok pattern to parse the unparsed logs.   
2025-05-30 |  \- Newly created parser.  
\- Added Grok patterns to parse the logs.  
\- Added a JSON block to parse the logs.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `filename_for_malachite` raw log field with `event.idm.read_only_udm.principal.resource.name' UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_type' UDM field.  
\- `event.idm.read_only_udm.metadata.product_deployment_id`: Newly mapped `aggregateId` raw log field with `event.idm.read_only_udm.metadata.product_deployment_id' UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `Hostname` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname' UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `destinationIp` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip' UDM field.  
\- `event.idm.read_only_udm.about.file.full_path`: Newly mapped `fileName` raw log field with `event.idm.read_only_udm.about.file.full_path' UDM field.  
\- `event.idm.read_only_udm.about.file.sha256`: Newly mapped `sha256` raw log field with `event.idm.read_only_udm.about.file.sha256' UDM field.  
\- `event.idm.read_only_udm.about.file.md5`: Newly mapped `md5` raw log field with `event.idm.read_only_udm.about.file.md5' UDM field.  
\- `event.idm.read_only_udm.about.file.sha1`: Newly mapped `sha1` raw log field with `event.idm.read_only_udm.about.file.sha1' UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `customerIP` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip' UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `fileExtension` raw log field with `event.idm.read_only_udm.security_result.detection_fields' UDM field.  
\- `event.idm.read_only_udm.about.file.mime_type`: Newly mapped `fileMime` raw log field with `event.idm.read_only_udm.about.file.mime_type' UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `senderDomain` raw log field with `event.idm.read_only_udm.principal.administrative_domain' UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `delivered`, `_offset`, `emailSize`, `_partition`, `totalSizeAttachments`,`permittedSender.allow`, `permittedSender.info`, `sizeAttachment`, `numberAttachments`, `receiptErrors`, `new_attachments`, `deliveryAttempts`, `senderDomainInternal` and `deliveryTime` raw log field with `event.idm.read_only_udm.additional.fields' UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `processingId` raw log field with `event.idm.read_only_udm.metadata.product_log_id' UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `accountId` raw log field with `event.idm.read_only_udm.target.user.userid' UDM field.  
\- `event.idm.read_only_udm.network.email.mail_id`: Newly mapped `messageId` raw log field with `event.idm.read_only_udm.network.email.mail_id' UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `rejectionType` raw log field with `event.idm.read_only_udm.security_result.category_details' UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `rejectionInfo` raw log field with `event.idm.read_only_udm.security_result.summary' UDM field.  
\- `event.idm.read_only_udm.security_result.action_details` and `event.idm.read_only_udm.security_result.action`: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action_details` and `event.idm.read_only_udm.security_result.action' UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `rejectionCode` raw log field with `event.idm.read_only_udm.security_result.rule_id' UDM field.  
\- `event.idm.read_only_udm.network.email.subject`: Newly mapped `subject` raw log field with `event.idm.read_only_udm.network.email.subject' UDM field.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `tlsVersion` raw log field with `event.idm.read_only_udm.network.tls.version' UDM field.  
\- `event.idm.read_only_udm.network.tls.cipher`: Newly mapped `tlsCipher` raw log field with `event.idm.read_only_udm.network.tls.cipher' UDM field.  
\- `event.idm.read_only_udm.network.tls.established`: Newly mapped `tlsUsed` raw log field with `event.idm.read_only_udm.network.tls.established' UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `direction` and `route` raw log field with `event.idm.read_only_udm.network.direction' UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `senderIp` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip' UDM field.  
\- `event.idm.read_only_udm.network.email.from`: Newly mapped `senderEnvelope` raw log field with `event.idm.read_only_udm.network.email.from' UDM field.  
\- `event.idm.read_only_udm.network.email.to`: Newly mapped `recipients` raw log field with `event.idm.read_only_udm.network.email.to' UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `type` raw log field with `event.idm.read_only_udm.metadata.product_event_type' UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `holdReason` raw log field with `event.idm.read_only_udm.security_result.description' UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `virusFound` raw log field with `event.idm.read_only_udm.security_result.threat_name' UDM field.  
\- `event.idm.read_only_udm.security_result.confidence_score`: Newly mapped `spamScore` raw log field with `event.idm.read_only_udm.security_result.confidence_score' UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `spamDetectionLevel` raw log field with `event.idm.read_only_udm.security_result.detection_fields' UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `senderHeader` raw log field with `event.idm.read_only_udm.principal.user.email_addresses' UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_network_email_from` , `has_network_email_to` and `has_principal_email` flag is true then `event.idm.read_only_udm.metadata.event_type` is mapped to `EMAIL_TRANSACTION'.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` flag is true then `event.idm.read_only_udm.metadata.event_type` is mapped to `STATUS_UPDATE'.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
