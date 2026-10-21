---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trend-micro-vision-one-detections/
title: Collect Trend Micro Vision One Detections logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:43:58.830148+00:00
---

# Collect Trend Micro Vision One Detections logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trend-micro-vision-one-detections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trend Micro Vision One Detections logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Trend Micro Vision One Detections logs to Google Security Operations using AWS S3. The parser transforms Trend Micro Vision One Detections logs from JSON format into a Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance
  * Privileged access to Trend Micro Vision One



## Configure Logging on Trend Micro Vision One

  1. Sign in to the **Trend Micro Vision One** console.
  2. Go to **Workflow and Automation > Third-Party Integration**.
  3. Click **Google Security Operations SIEM**.
  4. Under **Access key** , click **Generate key**.
  5. Copy and save the **access key ID** and **secret access key**.
  6. Under **Data transfer** , enable the toggle next to **Detections Data**.
  7. An S3 URI is generated and the data begins to be sent to the corresponding S3 bucket.
  8. Copy and save the S3 URL for use at a later time.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Trend Micro Vision One Detections Logs`).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Trend Micro Vision One Detections** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **S3 URI** : The bucket URI (the format should be: `s3://log-bucket-name/`). Replace the following: 
       * `log-bucket-name`: the name of the bucket.
     * **Source deletion options** : Select **Never delete files**. Data in the S3 bucket is retained for 7 days before being purged.
     * **Maximum File Age** : Includes files modified in the last number of days. Default is 180 days.
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`about1` | `about` | Merged  
`about2` | `about` | Merged  
`about3` | `about` | Merged  
`about4` | `about` | Merged  
`attachmentFileHashMd5` | `about.file.md5` | Directly mapped  
`attachmentFileType` | `about.file.mime_type` | Directly mapped  
`fileName` | `about.file.names` | Merged  
`attachmentFileHash` | `about.file.sha1` | Directly mapped  
`attachmentFileHashSha1` | `about.file.sha1` | Directly mapped  
`attachmentFileHashSha256` | `about.file.sha256` | Directly mapped  
`process_cmd` | `about.process.command_line` | Directly mapped  
`actResult_label_1` | `additional.fields` | Merged  
`aggregatedCount_label` | `additional.fields` | Merged  
`aptCampaigns_label` | `additional.fields` | Merged  
`attachmentFileTlshes_label` | `additional.fields` | Merged  
`blocking_label` | `additional.fields` | Merged  
`eventID_label` | `additional.fields` | Merged  
`eventSubId_label` | `additional.fields` | Merged  
`field1` | `additional.fields` | Merged  
`groupIdCorrValues_label` | `additional.fields` | Merged  
`highlightedRequest_label` | `additional.fields` | Merged  
`integrity_level_label` | `additional.fields` | Merged  
`level_label` | `additional.fields` | Merged  
`mailMsgDirection_label` | `additional.fields` | Merged  
`process_hash_id_label` | `additional.fields` | Merged  
`process_launch_time_label` | `additional.fields` | Merged  
`process_name_label` | `additional.fields` | Merged  
`process_signer_label` | `additional.fields` | Merged  
`process_signer_valid_label` | `additional.fields` | Merged  
`process_sub_true_type_label` | `additional.fields` | Merged  
`process_true_type_label` | `additional.fields` | Merged  
`rating_label` | `additional.fields` | Merged  
`requests_label` | `additional.fields` | Merged  
`description` | `metadata.description` | Directly mapped  
`eventTime` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`logReceivedTime` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`objectLastModifyTime` | `metadata.event_timestamp` | Parsed as `TIMESTAMP`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`has_principal_mid` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`eventName` | `metadata.product_event_type` | Directly mapped  
`eventType` | `metadata.product_event_type` | Directly mapped  
`msgUuid` | `metadata.product_log_id` | Directly mapped  
`uuid` | `metadata.product_log_id` | Directly mapped  
`pname` | `metadata.product_name` | Directly mapped  
`pver` | `metadata.product_version` | Directly mapped  
`app` | `network.application_protocol` | Directly mapped  
`direction` | `network.direction` | Mapped: `OUTGOING` → `OUTBOUND`  
`suser.0` | `network.email.from` | Directly mapped  
`msgId` | `network.email.mail_id` | Directly mapped  
`highlightMailMsgSubject` | `network.email.subject` | Merged  
`mailMsgSubject` | `network.email.subject` | Merged  
`tmpUser` | `network.email.to` | Merged  
`requestMethod` | `network.http.method` | Directly mapped  
`httpReferer` | `network.http.referral_url` | Directly mapped  
`mailSmtpFromAddresses.0` | `network.smtp.mail_from` | Directly mapped  
`addr` | `network.smtp.rcpt_to` | Merged  
`computerDomain` | `principal.administrative_domain` | Directly mapped  
`deviceGUID` | `principal.asset.asset_id` | Directly mapped  
`endpointGUID` | `principal.asset.asset_id` | Directly mapped  
`mDeviceGUID` | `principal.asset.asset_id` | Directly mapped  
`peerEndpointGUID` | `principal.asset.asset_id` | Directly mapped  
`hardware` | `principal.asset.hardware` | Merged  
`dvchost` | `principal.asset.hostname` | Directly mapped  
`endpointHostName` | `principal.asset.hostname` | Directly mapped  
`tmpIp` | `principal.asset.ip` | Merged  
`deviceMacAddress` | `principal.asset.mac` | Merged  
`endpointMacAddress` | `principal.asset.mac` | Merged  
`domainName` | `principal.asset.network_domain` | Directly mapped  
`vul` | `principal.asset.vulnerabilities` | Merged  
`domainName` | `principal.domain.name` | Directly mapped  
`hostName` | `principal.domain.name` | Directly mapped  
`userDomain` | `principal.domain.name` | Directly mapped  
`groupId` | `principal.group.product_object_id` | Directly mapped  
`dvchost` | `principal.hostname` | Directly mapped  
`endpointHostName` | `principal.hostname` | Directly mapped  
`peerHost` | `principal.hostname` | Directly mapped  
`peerIpAddr` | `principal.ip` | Merged  
`srcIp` | `principal.ip` | Merged  
`tmpIp` | `principal.ip` | Merged  
`deviceMacAddress` | `principal.mac` | Merged  
`endpointMacAddress` | `principal.mac` | Merged  
`processCmd` | `principal.process.command_line` | Directly mapped  
`processFilePath` | `principal.process.file.full_path` | Directly mapped  
`processImagePath` | `principal.process.file.full_path` | Directly mapped  
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
`processPid` | `principal.process.pid` | Directly mapped  
`suser_label` | `principal.resource.attribute.labels` | Merged  
`uuid_label` | `principal.resource.attribute.labels` | Merged  
`userDepartment` | `principal.user.department` | Merged  
`tmpUser1` | `principal.user.email_addresses` | Merged  
`logonUsers.0` | `principal.user.userid` | Directly mapped  
`objectUser` | `principal.user.userid` | Directly mapped  
`principalName` | `principal.user.userid` | Directly mapped  
`suid` | `principal.user.userid` | Directly mapped  
`mailbox` | `security_result.about.email` | Directly mapped  
`security_result_action` | `security_result.action` | Merged  
`act.0` | `security_result.action_details` | Directly mapped  
`tactics` | `security_result.attack_details.tactics` | Merged  
`techniques` | `security_result.attack_details.techniques` | Merged  
`category` | `security_result.category_details` | Merged  
`index` | `security_result.category_details` | Merged  
`tag` | `security_result.category_details` | Merged  
`actResult_label` | `security_result.detection_fields` | Merged  
`cccaDetectionSource_label` | `security_result.detection_fields` | Merged  
`cccaRiskLevel_label` | `security_result.detection_fields` | Merged  
`field1` | `security_result.detection_fields` | Merged  
`key` | `security_result.detection_fields` | Mapped: `"engineOperation","engType","detectionAggressivenessLevel","patVer","channel","thre...  
`mailbox_label` | `security_result.detection_fields` | Merged  
`matchedFilter_id_label` | `security_result.detection_fields` | Merged  
`matchedFilter_name_label` | `security_result.detection_fields` | Merged  
`matchedRules_id_label` | `security_result.detection_fields` | Merged  
`matchedRules_name_label` | `security_result.detection_fields` | Merged  
`matchedRules_threatType_label` | `security_result.detection_fields` | Merged  
`riskType_label` | `security_result.detection_fields` | Merged  
`subRuleId_label` | `security_result.detection_fields` | Merged  
`score` | `security_result.risk_score` | Renamed/mapped  
`matchedRule.id` | `security_result.rule_id` | Directly mapped  
`ruleId` | `security_result.rule_id` | Directly mapped  
`matchedRule.name` | `security_result.rule_name` | Directly mapped  
`ruleName` | `security_result.rule_name` | Directly mapped  
`ruleType` | `security_result.rule_type` | Directly mapped  
`ruleVer` | `security_result.rule_version` | Directly mapped  
`filterRiskLevel` | `security_result.severity_details` | Directly mapped  
`malName` | `security_result.threat_name` | Directly mapped  
`matchedRule.threatType` | `security_result.threat_name` | Directly mapped  
`mergethreatNames` | `security_result.threat_name` | Directly mapped  
`threatName` | `security_result.threat_name` | Directly mapped  
`source` | `src` | Renamed/mapped  
`interestedHost` | `target.asset.hostname` | Directly mapped  
`malDst` | `target.asset.hostname` | Directly mapped  
`tmpIp` | `target.asset.ip` | Merged  
`requestBase` | `target.domain.name` | Directly mapped  
`objectFilePath` | `target.file.full_path` | Directly mapped  
`objectFileHashMd5` | `target.file.md5` | Directly mapped  
`objectFileName` | `target.file.names` | Merged  
`objectFileHashSha1` | `target.file.sha1` | Directly mapped  
`objectFileHashSha256` | `target.file.sha256` | Directly mapped  
`dstGroup` | `target.group.group_display_name` | Directly mapped  
`dhost` | `target.hostname` | Directly mapped  
`interestedHost` | `target.hostname` | Directly mapped  
`malDst` | `target.hostname` | Directly mapped  
`dstIp` | `target.ip` | Merged  
`objectIp` | `target.ip` | Merged  
`tmpIp` | `target.ip` | Merged  
`dmac` | `target.mac` | Merged  
`dOSName` | `target.platform_version` | Directly mapped  
`objectCmd` | `target.process.command_line` | Directly mapped  
`objectTargetProcess` | `target.process.file.full_path` | Directly mapped  
`objectPid` | `target.process.pid` | Directly mapped  
`objectRegistryKeyHandle` | `target.registry.registry_key` | Directly mapped  
`objectRegistryData` | `target.registry.registry_value_data` | Directly mapped  
`objectRegistryValue` | `target.registry.registry_value_name` | Directly mapped  
`tmpUser_label` | `target.resource.attribute.labels` | Merged  
`request` | `target.url` | Directly mapped  
`objectUser` | `target.user.userid` | Directly mapped  
`samUser` | `target.user.userid` | Directly mapped  
N/A | `about.file.size` | Constant: `attachmentFileSize`  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `TREND VISION ONE DETECTIONS`  
N/A | `metadata.vendor_name` | Constant: `TREND VISION ONE DETECTIONS`  
N/A | `network.direction` | Constant: `OUTBOUND`  
N/A | `network.http.response_code` | Constant: `respCode`  
N/A | `principal.process.integrity_level_rid` | Constant: `integrityLevel`  
N/A | `principal.process.parent_process.integrity_level_rid` | Constant: `parentIntegrityLevel`  
N/A | `target.port` | Constant: `dpt`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-detections-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
