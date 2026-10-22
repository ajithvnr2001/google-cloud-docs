---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one-observed-attack-techniques/
title: Collect Trend Micro Vision One Observed Attack Techniques logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:39.089957+00:00
---

# Collect Trend Micro Vision One Observed Attack Techniques logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one-observed-attack-techniques/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trend Micro Vision One Observed Attack Techniques logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Trend Micro Vision One Observed Attack Techniques logs to Google Security Operations using AWS S3. The parser transforms the logs from JSON format into a Unified Data Model (UDM).

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
  6. Under **Data transfer** , enable the toggle next to **Observed Attack Techniques**.
  7. An S3 URI is generated and the data begins to be sent to the corresponding S3 bucket.
  8. Copy and save the S3 URL for use at a later time.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Trend Micro Vision One Observed Attack Techniques Logs`).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Trend Micro Vision One Observed Attack Techniques** as the **Log type**.
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
`_field` | `additional.fields` | Merged  
`onefield` | `additional.fields` | Merged  
`detectionTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`object_File_Creation` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`parent_File_Creation` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`process_File_Creation` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`v` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`v` | `metadata.product_event_type` | Directly mapped  
`v` | `metadata.product_log_id` | Directly mapped  
`v` | `metadata.product_version` | Directly mapped  
`v` | `network.parent_session_id` | Directly mapped  
`v` | `network.session_id` | Directly mapped  
`v` | `principal.administrative_domain` | Directly mapped  
`endpoint.guid` | `principal.asset.asset_id` | Directly mapped  
`endpoint.name` | `principal.asset.hostname` | Directly mapped  
`ip` | `principal.asset.ip` | Merged  
`k` | `principal.asset.ip` | Mapped: `"tags","userDomain","endpointIp","endpointMacAddress","suser","highlightedRequest",...  
`vIp` | `principal.asset.ip` | Merged  
`k` | `principal.asset.mac` | Mapped: `"tags","userDomain","endpointIp","endpointMacAddress","suser","highlightedRequest",...  
`vmac` | `principal.asset.mac` | Merged  
`v` | `principal.asset.type` | Directly mapped  
`endpoint.name` | `principal.hostname` | Directly mapped  
`ip` | `principal.ip` | Merged  
`k` | `principal.ip` | Mapped: `"tags","userDomain","endpointIp","endpointMacAddress","suser","highlightedRequest",...  
`vIp` | `principal.ip` | Merged  
`k` | `principal.mac` | Mapped: `"tags","userDomain","endpointIp","endpointMacAddress","suser","highlightedRequest",...  
`vmac` | `principal.mac` | Merged  
`k` | `principal.platform` | Mapped: `osName` → `LINUX`, `osName` → `WINDOWS`, `osName` → `MAC`  
`v` | `principal.platform` | Mapped: `(?i)Linux` → `LINUX`, `(?i)Windows` → `WINDOWS`, `(?i)mac/ios` → `MAC`  
`v` | `principal.platform_patch_level` | Directly mapped  
`v` | `principal.platform_version` | Directly mapped  
`highlight.value` | `principal.process.command_line` | Directly mapped  
`highlight.value` | `principal.process.file.full_path` | Directly mapped  
`v` | `principal.process.file.md5` | Directly mapped  
`k` | `principal.process.file.names` | Mapped: `"processName","processFileOriginalName"` → `v`  
`v` | `principal.process.file.names` | Merged  
`v` | `principal.process.file.sha1` | Directly mapped  
`v` | `principal.process.file.sha256` | Directly mapped  
`process_signers` | `principal.process.file.signature_info.sigcheck.signers` | Merged  
`k` | `principal.process.file.size` | Mapped: `processFileSize` → `uinteger`  
`v` | `principal.process.file.size` | Directly mapped  
`k` | `principal.process.integrity_level_rid` | Mapped: `integrityLevel` → `uinteger`, `integrityLevel` → `v`  
`v` | `principal.process.integrity_level_rid` | Directly mapped  
`highlight.value` | `principal.process.parent_process.command_line` | Directly mapped  
`v` | `principal.process.parent_process.file.full_path` | Directly mapped  
`v` | `principal.process.parent_process.file.md5` | Directly mapped  
`k` | `principal.process.parent_process.file.names` | Mapped: `"parentName","parentFileOriginalName"` → `v`  
`v` | `principal.process.parent_process.file.names` | Merged  
`v` | `principal.process.parent_process.file.sha1` | Directly mapped  
`v` | `principal.process.parent_process.file.sha256` | Directly mapped  
`parent_signers` | `principal.process.parent_process.file.signature_info.sigcheck.signers` | Merged  
`k` | `principal.process.parent_process.file.size` | Mapped: `parentFileSize` → `uinteger`  
`v` | `principal.process.parent_process.file.size` | Directly mapped  
`k` | `principal.process.parent_process.integrity_level_rid` | Mapped: `parentIntegrityLevel` → `uinteger`, `parentIntegrityLevel` → `v`  
`v` | `principal.process.parent_process.integrity_level_rid` | Directly mapped  
`v` | `principal.process.parent_process.pid` | Directly mapped  
`v` | `principal.process.pid` | Directly mapped  
`k` | `principal.user.group_identifiers` | Mapped: `"tags","userDomain","endpointIp","endpointMacAddress","suser","highlightedRequest",...  
`vuser` | `principal.user.group_identifiers` | Merged  
`k` | `principal.user.managers` | Mapped: `parentUser` → `user_manager`  
`user_manager` | `principal.user.managers` | Merged  
`entityName` | `principal.user.userid` | Directly mapped  
`v` | `principal.user.userid` | Directly mapped  
`vuser` | `principal.user.userid` | Directly mapped  
`sec_result` | `security_result` | Merged  
`one_tactic` | `security_result.attack_details.tactics` | Merged  
`one_tech` | `security_result.attack_details.techniques` | Merged  
`fl.description` | `security_result.description` | Directly mapped  
`df` | `security_result.detection_fields` | Merged  
`highlight_field` | `security_result.detection_fields` | Merged  
`master_label` | `security_result.detection_fields` | Merged  
`riskLevel_label` | `security_result.detection_fields` | Merged  
`type_label` | `security_result.detection_fields` | Merged  
`fl.id` | `security_result.rule_id` | Directly mapped  
`fl.name` | `security_result.rule_name` | Directly mapped  
`fl.unique_id` | `security_result.rule_version` | Directly mapped  
`flevel` | `security_result.severity` | Mapped: `INFO` → `INFORMATIONAL`  
`object_signers` | `target.file.signature_info.sigcheck.signers` | Merged  
`k` | `target.file.size` | Mapped: `objectFileSize` → `uinteger`  
`v` | `target.file.size` | Directly mapped  
`highlight.value` | `target.process.command_line` | Directly mapped  
`highlight.value` | `target.process.file.full_path` | Directly mapped  
`v` | `target.process.file.md5` | Directly mapped  
`k` | `target.process.file.names` | Mapped: `"objectName","objectFileOriginalName"` → `v`  
`v` | `target.process.file.names` | Merged  
`v` | `target.process.file.sha1` | Directly mapped  
`v` | `target.process.file.sha256` | Directly mapped  
`k` | `target.process.integrity_level_rid` | Mapped: `objectIntegrityLevel` → `uinteger`, `objectIntegrityLevel` → `v`  
`v` | `target.process.integrity_level_rid` | Directly mapped  
`v` | `target.process.pid` | Directly mapped  
`v` | `target.registry.registry_key` | Directly mapped  
`v` | `target.registry.registry_value_data` | Directly mapped  
`v` | `target.registry.registry_value_name` | Directly mapped  
`k` | `target.user.group_identifiers` | Mapped: `"tags","userDomain","endpointIp","endpointMacAddress","suser","highlightedRequest",...  
`v` | `target.user.group_identifiers` | Merged  
`vguser` | `target.user.group_identifiers` | Merged  
`v` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `TREND VISION ONE OAT`  
N/A | `metadata.vendor_name` | Constant: `TREND VISION ONE OAT`  
N/A | `principal.platform` | Constant: `LINUX`  
N/A | `principal.process.integrity_level_rid` | Constant: `v`  
N/A | `principal.process.parent_process.integrity_level_rid` | Constant: `v`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
N/A | `target.process.integrity_level_rid` | Constant: `v`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
