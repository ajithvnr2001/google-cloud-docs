---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudpassage-halo/
title: Collect Fidelis CloudPassage Halo logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:38:18.116641+00:00
---

# Collect Fidelis CloudPassage Halo logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudpassage-halo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Fidelis CloudPassage Halo logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect CloudPassage Halo (formerly CloudPassage) logs by setting up a Google Security Operations feed using the Third party API.

An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `CLOUD_PASSAGE` ingestion label.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to CloudPassage Halo portal with administrator permissions
  * Active CloudPassage Halo account with API access enabled



## Configure CloudPassage Halo API access

To enable Google SecOps to pull event logs, you need to create an API key pair with read-only permissions.

### Create API key pair

  1. Sign in to the **CloudPassage Halo Portal**.
  2. Go to **Settings > Site Administration > API Keys**.
  3. Click **Create Key** or **New API Key**.
  4. Provide the following configuration details: 
     * **Key Name** : Enter a descriptive name (for example, `Google SecOps Integration`).
     * **Read Only** : Select **Yes** (read-only access is recommended for security).
  5. Click **Create**.



### Record API credentials

After creating the API key, you'll receive the following credentials:

  * **Key ID** : Your unique API key identifier (for example, `abc123def456`)
  * **Secret Key** : Your API secret key (for example, `xyz789uvw012`)



**Important** : Copy and save both the Key ID and Secret Key immediately. The Secret Key cannot be retrieved after closing the creation dialog.

**Note:** Store these credentials securely. You will need both values when configuring the Google SecOps feed.

## Required API permissions

CloudPassage Halo API keys support the following permission levels:

Permission Level | Access | Purpose  
---|---|---  
**Read Only** | Read | Retrieve event data and configuration (recommended)  
**Full Access** | Read + Write | Retrieve events and modify configuration (not required)  
**Note:** Using read-only API keys follows least-privilege security principles. Read-only access is sufficient for log ingestion to Google SecOps. Write permissions are not required and should not be granted.

## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `CloudPassage Halo Events`).
  5. Select **Third party API** as the **Source type**.
  6. Select **Cloud Passage** as the **Log type**.
  7. Click **Next**.



Specify values for the following input parameters:

  1. **Username** : Enter the **Key ID** from the CloudPassage Halo API key pair created earlier.
  2. **Secret** : Enter the **Secret Key** from the CloudPassage Halo API key pair created earlier.
  3. **Event types** (optional): Specify which event types to ingest. Enter one event type per line.

If you leave this field empty, the feed will automatically retrieve the following default event types:

     * `fim_target_integrity_changed` (File Integrity Monitoring events)
     * `lids_rule_failed` (Log-based Intrusion Detection System events)
     * `sca_rule_failed` (Security Configuration Assessment events)

To retrieve additional event types, enter them one per line. For example:
    
    fim\_target\_integrity\_changed
      lids\_rule\_failed
      sca\_rule\_failed
      lids\_rule\_passed
      sca\_rule\_passed
      agent\_connection\_lost
    

**Note:** Available event types include but are not limited to: `fim_*`, `lids_*`, `sca_*`, `agent_*`, `firewall_*`, and `server_*` events. Consult the CloudPassage Halo API documentation for a complete list of event types.
  4. **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

  5. **Ingestion labels** : The label to be applied to the events from this feed.

  6. Click **Next**.

  7. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




After setup, the feed begins to retrieve event logs from the CloudPassage Halo API in chronological order.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`id` | `metadata.product_log_id` | Unique event identifier  
`created_at` | `metadata.event_timestamp` | Event creation timestamp  
`type` | `metadata.product_event_type` | Event type (e.g., fim_target_integrity_changed)  
`server_hostname` | `target.hostname` | Hostname of the affected server  
`server_platform` | `target.platform` | Operating system platform  
`server_primary_ip_address` | `target.ip` | Primary IP address of the server  
`rule_name` | `security_result.rule_name` | Name of the security rule that triggered the event  
`critical` | `security_result.severity` | Criticality level of the event  
`policy_name` | `security_result.category` | Security policy name  
`user` | `principal.user.userid` | User associated with the event  
`message` | `security_result.description` | Event description or message  
`policy_name` | `security_result.detection_fields` | Mapped from changelog  
`server_group_name` | `target.group.attribute.labels` | Mapped from changelog  
`server_group_path` | `target.group.product_object_id` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloud-passage-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
