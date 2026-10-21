---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/halcyon/
title: Collect Halcyon Anti-Ransomware logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:07:40.902190+00:00
---

# Collect Halcyon Anti-Ransomware logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/halcyon/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Halcyon Anti-Ransomware logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Halcyon Anti-Ransomware logs into Google Security Operations using Google Cloud Storage V2.

Halcyon is an anti-ransomware platform that uses AI to detect, prevent, and recover from ransomware attacks. It generates alerts for ransomware detection events, encryption attempts, and recovery actions. The parser maps JSON-formatted log fields to the Unified Data Model (UDM), handling event types such as file operations, user activity, and security results.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets and IAM policies
  * Privileged access to the Halcyon console with log export capabilities



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `halcyon-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Export Halcyon logs to Google Cloud Storage

Halcyon supports exporting log data in JSON format. Use one of the following approaches to deliver logs to GCS.

### Option A: Export logs using the Halcyon API and upload to GCS

  1. Sign in to the **Halcyon** management console.
  2. Go to **Settings > API Access** and generate an API key with read permissions.
  3. Copy and save the **API Key**.
  4. Use a scheduled script or Cloud Run function to call the Halcyon REST API, fetch event logs, and write them to GCS in JSON format.



### Option B: Configure SIEM integration and forward to GCS

  1. Sign in to the **Halcyon** management console.
  2. Go to **Settings > Integrations > SIEM**.
  3. Configure the log export destination to write JSON-formatted events to a local directory or intermediate storage.
  4. Use a Cloud Run function to periodically upload logs to your GCS bucket.

     * Make sure the exported files are in JSON format.
     * Each file should contain one or more event records.



## Retrieve the Google SecOps service account

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Feeds**.
  3. Click **Add New Feed**.
  4. Click **Configure a single feed**.
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Halcyon Anti Ransomware** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.


**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.

## Grant IAM permissions to the Google SecOps service account

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

     * If you plan to use the deletion option (delete transferred files), grant **Storage Object Admin** role instead of Storage Object Viewer.



## Configure a feed in Google SecOps to ingest Halcyon Anti-Ransomware logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Halcyon Anti-Ransomware logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Halcyon Anti Ransomware** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

Field | Value  
---|---  
**Storage bucket URI** | `gs://halcyon-logs/halcyon/events/`  
**Source Deletion Option** | Select the deletion option according to your preference  
**Maximum File Age (Days)** | Default is 180 days  
**Asset namespace** | The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)  
**Ingestion labels** | The label to be applied to the events from this feed  
     * Replace `halcyon-logs` with your actual GCS bucket name.
     * Always include the trailing slash (`/`) at the end of the URI.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
sshd, tty, euid, dataType, filterName, totalOccurrences, occurredAt, count, occurrences.IncorrectPasswords, occurrences.FailedPassword, occurrences.AuthFailure, policyMode, action | additional.fields | Merged with labels created from each field if present; totalOccurrences, count, occurrences fields converted to string  
dnsArtifact.uri | network.dns.questions | Merged with questions array containing the name  
asset.id | principal.asset.asset_id | Concatenated as "ASSET:" + asset.id  
asset.kind | principal.asset.attribute.labels | Merged with asset_kind_label created from asset.kind  
asset.name | principal.asset.hostname | Value copied directly  
ipArtifact.ipAddress | principal.asset.ip | Value copied directly  
summary.applicationName | principal.application | Value copied directly  
phost, asset.name | principal.hostname | Value from phost if present, overwritten by asset.name if present  
ipArtifact.ipAddress | principal.ip | Value copied directly  
process.commandLine | principal.process.command_line | Value copied directly  
modifiedFilePath, artifact.filePath, process.artifact.filePath, processes.artifact.filePath | principal.process.file.full_path | Value set to modifiedFilePath if present, overwritten by artifact.filePath if present, overwritten by process.artifact.filePath if present, overwritten by processes.artifact.filePath if present (quotes removed for processes.artifact.filePath)  
lastOccurredAt | principal.process.file.last_seen_time | Converted using date filter with ISO8601 format  
process.artifact.kind, artifact.kind, primaryProcess.artifact.kind | principal.process.file.mime_type | Value from process.artifact.kind if present, overwritten by artifact.kind if present, overwritten by primaryProcess.artifact.kind if present  
artifact.sha256, process.artifact.sha256, processes.artifact.sha256 | principal.process.file.sha256 | Value from artifact.sha256 if present, overwritten by process.artifact.sha256 if present, overwritten by processes.artifact.sha256 if present  
process.parentPid | principal.process.parent_pid | Value copied directly  
process.pid | principal.process.pid | Value copied directly  
user_displayname | principal.user.user_display_name | Value copied directly  
user | principal.user.userid | Value copied directly  
summary.artifact.filePath | target.file.full_path | Value copied directly  
summary.artifact.sha256 | target.file.sha256 | Value copied directly  
primaryProcess.commandLine | target.process.command_line | Value copied directly after removing quotes  
primaryProcess.kind | target.process.file.mime_type | Value copied directly  
primaryProcess.parentPid | target.process.parent_process.pid | Value copied directly  
primaryProcess.pid | target.process.pid | Value copied directly  
uid | target.user.userid | Value copied directly  
id | target.asset_id | Concatenated as "ASSET:" + id  
action | security_result.action | Uppercased if action is "Block" or "Allow"  
reason.exitCode | security_result.action_details | Value copied directly  
dxpRule, monitoringReason, tenantId | security_result.detection_fields | Merged with labels created from each field if present; backslashes removed for dxpRule  
dxpRuleType | security_result.rule_type | Value copied directly  
ipArtifact.version | security_result.rule_version | Value copied directly  
msg, reason.cause | security_result.summary | Value from msg if present, overwritten by reason.cause if present  
timestamp | metadata.event_timestamp | Converted using date filter with formats MMM dd HH:mm:ss or MMM d HH:mm:ss  
phost, ipArtifact.ipAddress, asset.name, user, uid, summary.artifact.sha256, summary.artifact.filePath | metadata.event_type | Set to FILE_UNCATEGORIZED if has_principal and has_target_file; USER_UNCATEGORIZED if has_principal and has_target; STATUS_UPDATE if has_principal; else GENERIC_EVENT (flags derived from sources)  
kind | metadata.product_event_type | Value copied directly  
gupid, guid | metadata.product_log_id | Value from gupid if present, overwritten by guid if present  
| metadata.product_name | Set to "Halcyon Anti Ransomware"  
| metadata.vendor_name | Set to "Halcyon"  
`primaryProcess.kind` | `event.idm.read_only_udm.target.process.file.mime_type` | Mapped from changelog  
`primaryProcess.artifact.kind` | `event.idm.read_only_udm.principal.process.file.mime_type` | Mapped from changelog  
`processes.artifact.filePath` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`processes.artifact.sha256` | `event.idm.read_only_udm.principal.process.file.sha256` | Mapped from changelog  
`action` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`filterName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`policyMode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`euid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`occurrences.AuthFailure` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`occurrences.FailedPassword` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`occurredAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`occurrences.IncorrectPasswords` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`guid` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`gupid` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`count` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`artifact.filePath` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`artifact.sha256` | `event.idm.read_only_udm.principal.process.file.sha256` | Mapped from changelog  
`artifact.kind` | `event.idm.read_only_udm.principal.process.file.mime_type` | Mapped from changelog  
`monitoringReason` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`dxpRule` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`modifiedFilePath` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`ipArtifact.version` | `event.idm.read_only_udm.security_result.rule_version` | Mapped from changelog  
`ipArtifact.ipAddress` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`ipArtifact.ipAddress` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`process.parentPid` | `event.idm.read_only_udm.principal.process.parent_pid` | Mapped from changelog  
`dxpRuleType` | `event.idm.read_only_udm.security_result.rule_type` | Mapped from changelog  
`summary.applicationName` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`process.pid` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`reason.exitCode` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`reason.cause` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`dnsArtifact_uri` | `event.idm.read_only_udm.network.dns.questions` | Mapped from changelog  
`uid` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`tty` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sshd` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`phost` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`user_displayname` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`msg` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`user` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/halcyon-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
