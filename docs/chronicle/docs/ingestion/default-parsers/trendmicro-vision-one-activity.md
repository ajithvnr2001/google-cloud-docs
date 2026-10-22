---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one-activity/
title: Collect Trend Micro Vision One Activity logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:30.964653+00:00
---

# Collect Trend Micro Vision One Activity logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one-activity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trend Micro Vision One Activity logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Trend Micro Vision One Activity logs to Google Security Operations using AWS S3. The parser transforms Trend Micro Vision One Activity logs from JSON format into a Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance
  * Privileged access to Trend Micro Vision One.



## Configure Logging on Trend Micro Vision One

  1. Sign in to the **Trend Micro Vision One** console.
  2. Go to **Workflow and Automation > Third-Party Integration**.
  3. Click **Google Security Operations SIEM.**
  4. Under Access key, click **Generate key**.
  5. Copy and Save the **access key ID** and **secret access key**.
  6. Under Data transfer, **enable** the toggle next to **Activity Data**.
  7. An **S3 URI** is generated and the data begins to be sent to the corresponding S3 bucket. 
  8. Copy and save the S3 URI in a safe location.
  9. (Optional): For Events and Activity data, click **Edit** to modify the scope of the data (Modifying the scope does not change the generated S3 URI).



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, Trend Micro Vision One Activity Logs).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Trend Micro Vision One Activity** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **S3 URI** : The bucket URI (the format should be: `s3://log-bucket-name/`). Replace the following: 
       * `log-bucket-name`: the name of the bucket. .
     * **Source deletion options** : Select **Never delete files**. Data in the S3 bucket is retained for 7 days before being purged.
     * **Maximum File Age** : Includes files modified in the last number of days. Default is 180 days.
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`fileName` | `about.file.names` | Merged  
`_field` | `additional.fields` | Merged  
`apiVersion_label` | `additional.fields` | Merged  
`appLabel_label` | `additional.fields` | Merged  
`app_label` | `additional.fields` | Merged  
`application_label` | `additional.fields` | Merged  
`attachmentFileSizes_label` | `additional.fields` | Merged  
`attachmentMd5_label` | `additional.fields` | Merged  
`attachmentSha1_label` | `additional.fields` | Merged  
`attachmentSha256_label` | `additional.fields` | Merged  
`awsRegion_label` | `additional.fields` | Merged  
`clusterId_label` | `additional.fields` | Merged  
`clusterName_label` | `additional.fields` | Merged  
`eventID_label` | `additional.fields` | Merged  
`groupId_label` | `additional.fields` | Merged  
`id_label` | `additional.fields` | Merged  
`idpId_label` | `additional.fields` | Merged  
`k8sNamespace_label` | `additional.fields` | Merged  
`name_label` | `additional.fields` | Merged  
`productCode_label` | `additional.fields` | Merged  
`recipientAccountId_label` | `additional.fields` | Merged  
`spamResultHeader_label` | `additional.fields` | Merged  
`spamRidHeader_label` | `additional.fields` | Merged  
`vpcEndpointId_label` | `additional.fields` | Merged  
`remarks` | `metadata.description` | Directly mapped  
`eventTime` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`logReceivedTime` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`objectFileModifiedTime` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`objectFirstSeen` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`objectLastSeen` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`srcFileModifiedTime` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`srcFirstSeen` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`srcLastSeen` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`has_email` | `metadata.event_type` | Mapped: `true` → `EMAIL_TRANSACTION`  
`has_network` | `metadata.event_type` | Mapped: `true` → `NETWORK_UNCATEGORIZED`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `FILE_UNCATEGORIZED`, `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`has_process` | `metadata.event_type` | Mapped: `true` → `PROCESS_UNCATEGORIZED`  
`has_registry` | `metadata.event_type` | Mapped: `true` → `REGISTRY_UNCATEGORIZED`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`eventName` | `metadata.product_event_type` | Directly mapped  
`eventType` | `metadata.product_event_type` | Directly mapped  
`scanType` | `metadata.product_event_type` | Directly mapped  
`msgUuid` | `metadata.product_log_id` | Directly mapped  
`uuid` | `metadata.product_log_id` | Directly mapped  
`idpName` | `metadata.product_name` | Directly mapped  
`pname` | `metadata.product_name` | Directly mapped  
`pver` | `metadata.product_version` | Directly mapped  
`protocol` | `network.application_protocol` | Directly mapped  
`version` | `network.application_protocol_version` | Directly mapped  
`mailBccAddr` | `network.email.bcc` | Merged  
`mailccAddr` | `network.email.cc` | Merged  
`mailFromAddresses.0` | `network.email.from` | Directly mapped  
`suser` | `network.email.from` | Directly mapped  
`mailMsgId` | `network.email.mail_id` | Directly mapped  
`msgId` | `network.email.mail_id` | Directly mapped  
`mailReplyToAddr` | `network.email.reply_to` | Directly mapped  
`mailMsgSubject` | `network.email.subject` | Merged  
`duser` | `network.email.to` | Merged  
`mailToAddr` | `network.email.to` | Merged  
`requestMethod` | `network.http.method` | Directly mapped  
`userAgent` | `network.http.parsed_user_agent` | Directly mapped  
`httpReferer` | `network.http.referral_url` | Directly mapped  
`userAgent` | `network.http.user_agent` | Directly mapped  
`responseSize` | `network.received_bytes` | Directly mapped  
`requestSize` | `network.sent_bytes` | Directly mapped  
`duration` | `network.session_duration.seconds` | Directly mapped  
`tlsSelectedCipher` | `network.tls.cipher` | Directly mapped  
`clientTls` | `network.tls.version` | Directly mapped  
`downstreamTls` | `network.tls.version` | Directly mapped  
`clientId` | `principal.asset.asset_id` | Directly mapped  
`deviceGUID` | `principal.asset.asset_id` | Directly mapped  
`endpointGuid` | `principal.asset.asset_id` | Directly mapped  
`clientDisplayName_label` | `principal.asset.attribute.labels` | Merged  
`clientOS_label` | `principal.asset.attribute.labels` | Merged  
`hardware` | `principal.asset.hardware` | Merged  
`endpointHostName` | `principal.asset.hostname` | Directly mapped  
`sender` | `principal.asset.hostname` | Directly mapped  
`ipAddress` | `principal.asset.ip` | Merged  
`srcIp` | `principal.asset.ip` | Merged  
`tmpIp` | `principal.asset.ip` | Merged  
`tmpMac` | `principal.asset.mac` | Merged  
`hostName` | `principal.domain.name` | Directly mapped  
`endpointHostName` | `principal.hostname` | Directly mapped  
`sender` | `principal.hostname` | Directly mapped  
`sourceIPAddress` | `principal.ip` | Merged  
`srcIp` | `principal.ip` | Merged  
`tmpIp` | `principal.ip` | Merged  
`ip_location` | `principal.ip_location` | Merged  
`srcLocation` | `principal.location.country_or_region` | Directly mapped  
`tmpMac` | `principal.mac` | Merged  
`processFilePath` | `principal.process.file.full_path` | Directly mapped  
`processFileHashMd5` | `principal.process.file.md5` | Directly mapped  
`processName` | `principal.process.file.names` | Merged  
`processFileHashSha1` | `principal.process.file.sha1` | Directly mapped  
`processFileHashSha256` | `principal.process.file.sha256` | Directly mapped  
`parentCmd` | `principal.process.parent_process.command_line` | Directly mapped  
`parentFilePath` | `principal.process.parent_process.file.full_path` | Directly mapped  
`parentFileHashMd5` | `principal.process.parent_process.file.md5` | Directly mapped  
`parentName` | `principal.process.parent_process.file.names` | Merged  
`parentFileHashSha1` | `principal.process.parent_process.file.sha1` | Directly mapped  
`parentFileHashSha256` | `principal.process.parent_process.file.sha256` | Directly mapped  
`parentPid` | `principal.process.parent_process.pid` | Directly mapped  
`uuid_label` | `principal.resource.attribute.labels` | Merged  
`userId` | `principal.user.product_object_id` | Directly mapped  
`userDisplayName` | `principal.user.user_display_name` | Directly mapped  
`objectUser` | `principal.user.userid` | Directly mapped  
`principalName` | `principal.user.userid` | Directly mapped  
`mailbox` | `security_result.about.email` | Directly mapped  
`act` | `security_result.action_details` | Directly mapped  
`urlCat` | `security_result.category_details` | Merged  
`_field` | `security_result.detection_fields` | Merged  
`action_label` | `security_result.detection_fields` | Merged  
`detectionType_label` | `security_result.detection_fields` | Merged  
`eventSourceType_label` | `security_result.detection_fields` | Merged  
`key` | `security_result.detection_fields` | Mapped: `"failedHTTPSInspection", "serverProtocol", "score"` → `_field`  
`mailDirection_label` | `security_result.detection_fields` | Merged  
`type_label` | `security_result.detection_fields` | Merged  
`mailScore` | `security_result.risk_score` | Renamed/mapped  
`policyUuid` | `security_result.rule_id` | Directly mapped  
`ruleId` | `security_result.rule_id` | Directly mapped  
`ruleUuid` | `security_result.rule_id` | Directly mapped  
`ruleName` | `security_result.rule_name` | Directly mapped  
`ruleType` | `security_result.rule_type` | Directly mapped  
`filterRiskLevel` | `security_result.severity_details` | Directly mapped  
`deliveryStatus` | `security_result.summary` | Directly mapped  
`malName` | `security_result.threat_name` | Directly mapped  
`source` | `src` | Renamed/mapped  
`target_udm` | `target` | Renamed/mapped  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `TREND VISION ONE ACTIVITY`  
N/A | `metadata.vendor_name` | Constant: `TREND VISION ONE ACTIVITY`  
N/A | `network.http.parsed_user_agent` | Constant: `parseduseragent`  
N/A | `network.http.response_code` | Constant: `respCode`  
N/A | `principal.process.integrity_level_rid` | Constant: `integrityLevel`  
N/A | `principal.process.parent_process.integrity_level_rid` | Constant: `parentIntegrityLevel`  
N/A | `principal.process.pid` | Constant: `processPid`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-activity-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
