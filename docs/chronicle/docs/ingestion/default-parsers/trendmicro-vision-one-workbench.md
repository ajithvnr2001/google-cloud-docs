---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one-workbench/
title: Collect Trend Micro Vision One Workbench logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:24.042377+00:00
---

# Collect Trend Micro Vision One Workbench logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one-workbench/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trend Micro Vision One Workbench logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Trend Micro Vision One Workbench logs to Google Security Operations using AWS S3. The parser transforms Trend Micro Vision One Workbench logs from JSON format into a Unified Data Model (UDM).

## Before you begin

  * Google SecOps instance
  * Privileged access to Trend Micro Vision One



## Configure Logging on Trend Micro Vision One

  1. Sign in to the **Trend Micro Vision One** console.
  2. Go to **Workflow and Automation > Third-Party Integration**.
  3. Click **Google Security Operations SIEM**.
  4. Under **Access key** , click **Generate key**.
  5. Copy and save the **access key ID** and **secret access key**.
  6. Under **Data transfer** , enable the toggle next to **Workbench Data**.
  7. An S3 URI is generated and the data begins to be sent to the corresponding S3 bucket.
  8. Copy and save the S3 URL for use at a later time.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Trend Micro Vision One Workbench Logs`).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Trend Micro Vision One Workbench** as the **Log type**.
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
`indicator_value` | `about.file.full_path` | Directly mapped  
`indicator_value` | `about.url` | Directly mapped  
`_field` | `additional.fields` | Merged  
`alertProvider_label` | `additional.fields` | Merged  
`eventSourceType_label` | `additional.fields` | Merged  
`hostId_label` | `additional.fields` | Merged  
`incidentId_label` | `additional.fields` | Merged  
`logKey_label` | `additional.fields` | Merged  
`model_label` | `additional.fields` | Merged  
`mpname_label` | `additional.fields` | Merged  
`mpver_label` | `additional.fields` | Merged  
`productCode_label` | `additional.fields` | Merged  
`rtDate_label` | `additional.fields` | Merged  
`description` | `metadata.description` | Directly mapped  
`createdDateTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`logReceivedTime` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`rt` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`updatedDateTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`fileOperation` | `metadata.event_type` | Mapped: `Updated` → `FILE_MODIFICATION`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `FILE_UNCATEGORIZED`, `true` → `FILE_MODIFICATION`, `true` → `PROCESS_UNCAT...  
`eventName` | `metadata.product_event_type` | Directly mapped  
`eventId` | `metadata.product_log_id` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`pname` | `metadata.product_name` | Directly mapped  
`pver` | `metadata.product_version` | Directly mapped  
`schemaVersion` | `metadata.product_version` | Directly mapped  
`indicator_value` | `network.email.mail_id` | Directly mapped  
`indicator.value` | `network.email.subject` | Merged  
`AccountDomain` | `principal.administrative_domain` | Directly mapped  
`domain` | `principal.administrative_domain` | Directly mapped  
`mDeviceGUID` | `principal.asset.asset_id` | Directly mapped  
`endpointHostName` | `principal.asset.hostname` | Directly mapped  
`entity.entityValue.name` | `principal.asset.hostname` | Directly mapped  
`entityValue_name` | `principal.asset.ip` | Merged  
`ip` | `principal.asset.ip` | Merged  
`src_ip` | `principal.asset.ip` | Merged  
`endpointHostName` | `principal.hostname` | Directly mapped  
`entity.entityValue.name` | `principal.hostname` | Directly mapped  
`entityValue_name` | `principal.ip` | Merged  
`ip` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`indicator_value` | `principal.process.command_line` | Directly mapped  
`indicator_value` | `principal.process.file.sha256` | Directly mapped  
`indicator_value` | `principal.process.parent_process.command_line` | Directly mapped  
`_field` | `principal.resource.attribute.labels` | Merged  
`endpointGUID_label` | `principal.resource.attribute.labels` | Merged  
`entityId_label` | `principal.resource.attribute.labels` | Merged  
`entityValue_name_label` | `principal.resource.attribute.labels` | Merged  
`key` | `principal.resource.attribute.labels` | Mapped: `srchwvendor` → `_field`  
`managementScopeGroupId_label` | `principal.resource.attribute.labels` | Merged  
`managementScopeInstanceId_label` | `principal.resource.attribute.labels` | Merged  
`managementScopePartitionKey_label` | `principal.resource.attribute.labels` | Merged  
`senderGUID_label` | `principal.resource.attribute.labels` | Merged  
`uuid_label` | `principal.resource.attribute.labels` | Merged  
`entity.entityValue` | `principal.user.email_addresses` | Merged  
`indicator_value` | `principal.user.email_addresses` | Merged  
`domain_value` | `principal.user.user_display_name` | Directly mapped  
`AccountName` | `principal.user.userid` | Directly mapped  
`entity_entityValue` | `principal.user.userid` | Directly mapped  
`indicator_value` | `principal.user.userid` | Directly mapped  
`suid` | `principal.user.userid` | Directly mapped  
`user_id_value` | `principal.user.userid` | Directly mapped  
`SecurityID` | `principal.user.windows_sid` | Directly mapped  
`sec` | `security_result` | Merged  
`sec_isEntity` | `security_result` | Merged  
`sec_res` | `security_result` | Merged  
`sec_wasEntity` | `security_result` | Merged  
`investigationResult` | `security_result.about.investigation.comments` | Merged  
`investigationStatus` | `security_result.about.investigation.status` | Mapped: `New` → `NEW`, `Closed` → `CLOSED`, `Open` → `OPEN`, `Reviewed` → `REVIEWED`  
`fileOperation` | `security_result.action_details` | Directly mapped  
`cat` | `security_result.category_details` | Merged  
`msg` | `security_result.description` | Directly mapped  
`LogonID_label` | `security_result.detection_fields` | Merged  
`_field` | `security_result.detection_fields` | Merged  
`access_right_label` | `security_result.detection_fields` | Merged  
`detectionType_label` | `security_result.detection_fields` | Merged  
`key` | `security_result.detection_fields` | Mapped: `"status", "auditid"` → `_field`  
`modelId_label` | `security_result.detection_fields` | Merged  
`modelType_label` | `security_result.detection_fields` | Merged  
`ownerIds_label` | `security_result.detection_fields` | Merged  
`prov_enance_label` | `security_result.detection_fields` | Merged  
`proven_ance_label` | `security_result.detection_fields` | Merged  
`relatedEntitie_label` | `security_result.detection_fields` | Merged  
`relatedIndicatorId_label` | `security_result.detection_fields` | Merged  
`status_label` | `security_result.detection_fields` | Merged  
`subRuleId_label` | `security_result.detection_fields` | Merged  
`subRuleName_label` | `security_result.detection_fields` | Merged  
`winEventId_label` | `security_result.detection_fields` | Merged  
`createdDateTime` | `security_result.first_discovered_time` | Renamed/mapped  
`updatedDateTime` | `security_result.last_updated_time` | Renamed/mapped  
`Score` | `security_result.risk_score` | Renamed/mapped  
`score` | `security_result.risk_score` | Renamed/mapped  
`ruleId` | `security_result.rule_id` | Directly mapped  
`ruleName` | `security_result.rule_name` | Directly mapped  
`severity` | `security_result.severity_details` | Directly mapped  
`workbenchLink` | `security_result.url_back_to_product` | Renamed/mapped  
`filePathName` | `target.file.full_path` | Directly mapped  
`fullPath` | `target.file.full_path` | Directly mapped  
`file` | `target.file.names` | Merged  
`indicator_value` | `target.process.command_line` | Directly mapped  
`processName` | `target.process.file.full_path` | Directly mapped  
`TarAccountName` | `target.user.userid` | Directly mapped  
`duser.0` | `target.user.userid` | Directly mapped  
`TarAccountName` | `target.user.windows_sid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `TRENDMICRO VISION ONE WORKBENCH`  
N/A | `metadata.vendor_name` | Constant: `TRENDMICRO VISION ONE WORKBENCH`  
N/A | `security_result.about.investigation.status` | Constant: `NEW`  
N/A | `security_result.severity` | Constant: `CRITICAL`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-workbench-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
