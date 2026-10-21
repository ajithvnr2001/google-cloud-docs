---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one-audit/
title: Collect Trend Micro Vision One Audit logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:27:51.991534+00:00
---

# Collect Trend Micro Vision One Audit logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trend Micro Vision One Audit logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Trend Micro Vision One Audit logs to Google Security Operations using AWS S3. The parser transforms Trend Micro Vision One Audit logs from JSON format into a Unified Data Model (UDM).

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
  6. Under **Data transfer** , enable the toggle next to **Audit Data**.
  7. An S3 URI is generated and the data begins to be sent to the corresponding S3 bucket.
  8. Copy and save the S3 URL for use at a later time.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Trend Micro Vision One Audit Logs`).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Trend Micro Vision One Audit** as the **Log type**.
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
`Asset_name_field` | `additional.fields` | Merged  
`Asset_type_field` | `additional.fields` | Merged  
`accessType_field` | `additional.fields` | Merged  
`activity_field` | `additional.fields` | Merged  
`assTotalAssetsInvolved_field` | `additional.fields` | Merged  
`ass_EventList_field` | `additional.fields` | Merged  
`category_field` | `additional.fields` | Merged  
`details_field` | `additional.fields` | Merged  
`details_investigationResult_field` | `additional.fields` | Merged  
`details_role_field` | `additional.fields` | Merged  
`feedback_reason_id_field` | `additional.fields` | Merged  
`reason_field` | `additional.fields` | Merged  
`reason_value_field` | `additional.fields` | Merged  
`result_field` | `additional.fields` | Merged  
`details.description` | `metadata.description` | Directly mapped  
`ingestedDateTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`loggedDateTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`has_principal_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`details.traceId` | `metadata.product_deployment_id` | Directly mapped  
`details.identifier.type` | `metadata.product_event_type` | Directly mapped  
`details.serverId` | `principal.asset.product_object_id` | Directly mapped  
`removedAgent.xdrDeviceId` | `principal.asset.product_object_id` | Directly mapped  
`details.groupId` | `principal.group.product_object_id` | Directly mapped  
`removedAgent.hostname` | `principal.hostname` | Directly mapped  
`details.ipAddr` | `principal.ip` | Merged  
`requestId_field` | `principal.resource.attribute.labels` | Merged  
`details.instanceId` | `principal.resource.product_object_id` | Directly mapped  
`details.identifier.subType` | `principal.resource.resource_subtype` | Directly mapped  
`details.type` | `principal.resource.type` | Directly mapped  
`details.identifier.email` | `principal.user.email_addresses` | Merged  
`details.identifier.id` | `principal.user.product_object_id` | Directly mapped  
`details.identifier.name` | `principal.user.user_display_name` | Directly mapped  
`details.user` | `principal.user.user_display_name` | Directly mapped  
`loggedUser` | `principal.user.userid` | Directly mapped  
`details.action` | `security_result.action_details` | Directly mapped  
`details.feedback.description` | `security_result.description` | Directly mapped  
`details.assMitigateStatus` | `security_result.summary` | Directly mapped  
`details.status` | `security_result.summary` | Directly mapped  
`details.workbenchId` | `target.resource.id` | Directly mapped  
`endpoint.wsDeviceId` | `target.resource.product_object_id` | Directly mapped  
`endpoint.xdrDeviceId` | `target.resource.type` | Directly mapped  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `TREND VISION ONE AUDIT`  
N/A | `metadata.vendor_name` | Constant: `TREND VISION ONE AUDIT`  
N/A | `principal.user.user_role` | Constant: `ADMINISTRATOR`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-audit-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
