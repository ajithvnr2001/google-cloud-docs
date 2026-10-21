---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudflare-waf/
title: Collect Cloudflare WAF logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:31:41.078720+00:00
---

# Collect Cloudflare WAF logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudflare-waf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cloudflare WAF logs

**Parser Version:** 6.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This parser extracts fields from Cloudflare Web Application Firewall (WAF) JSON logs, transforms and maps them to the Unified Data Model (UDM). It handles various Cloudflare actions, enriching the data with metadata and network information before structuring the output into the UDM format.

## Before you begin

Ensure that you have the following prerequisites:

  * Google SecOps instance.
  * Privileged access to Google Cloud.
  * Cloudflare Enterprise plan.
  * Privileged access to Cloudflare. For details, see [Cloudflare](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudflare#enable-cloudflare-iam).



## Create a Google Cloud Storage Bucket

  1. Sign in to the Google Cloud console.
  2. Go to the **Cloud Storage Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  3. Click **Create**.

  4. Configure the bucket:

     * **Name** : enter a unique name that meets the bucket name requirements (for example, **cloudflare-waf**).
     * **Choose where to store your data** : select a location.
     * **Choose a storage class for your data** : either select a **default storage class** for the bucket, or select **Autoclass** for automatic storage class management.
     * **Choose how to control access to objects** : select **not** to enforce **public access prevention** , and select an **access control model** for your bucket's objects.
**Note:** If public access prevention is already enforced by your project's organization policy, the **Prevent public access** checkbox is locked.
     * **Storage class** : Choose based on your needs (for example, **Standard**).
  5. Click **Create**.


**Note:** Don't set a retention policy, as the last data entry may need to be overwritten in case of a timeout.

## Grant bucket permissions to Cloudflare IAM user

  1. In Google Cloud, go to **Storage** > **Browser** > **Bucket** > **Permissions**.
  2. Add the account logpush@cloudflare-data.iam.gserviceaccount.com with Storage Object Admin permission.



## Create a Logpush Job for WAF Logs using Cloudflare UI

  1. Sign in to Cloudflare.
  2. Go to **Analytics & Logs** > **Logpush**.
  3. Select **Create a Logpush job**.
  4. In **Select a destination** , choose **Google Cloud Storage**.
  5. Enter the following destination details: 
     * **Bucket** : Google Cloud Storage bucket name
     * **Path** : Bucket location within the storage container
     * Select **Organize logs into daily subfolders**
  6. Click **Continue**.

**Note:** To prove ownership, Cloudflare will send a file to your designated destination. To find the token, select the Open button in the **Overview** tab of the ownership challenge file, then paste it into the Cloudflare dashboard to verify your access to the bucket. Enter the Ownership Token and select Continue.

  1. Select the **Security (WAF)** dataset to push to the storage.
  2. Configure the logpush job: 
     * Enter the **Job name**.
     * Under If logs match, you can select the events to include or remove from your logs. Refer to **Filters** for more information. Not all datasets have this option available.
     * In **Send the following** fields, you can choose to either push all logs to your storage destination or selectively choose which logs you want to push.
  3. Click **Submit**.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, **Cloudflare WAF Logs**).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Cloudflare WAF** as the **Log type**.
  7. Click **Get Service Account**.
  8. Click **Next**.
  9. Specify values for the following input parameters:

     * **Storage Bucket URI** : the Cloud Storage URL.
     * **Source deletion options** : select the deletion option according to your preference.
**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account. * **Maximum File Age** : Includes files modified in the last number of days. Default is 180 days.
  10. Click **Next**.

  11. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`Action` | `security_result.action_details` | The value of `Action` from the raw log is directly assigned to this UDM field.  
`Action` | `security_result.action` | The value of this field is derived from the `Action` field in the raw log. If `Action` is "allow", the UDM field is set to `ALLOW`. If `Action` is "challengeSolved", "jschallengeSolved", "managedchallengenoninteractivesolved", or "managedchallengeinteractivesolved", the UDM field is set to `ALLOW_WITH_MODIFICATION`. If `Action` is "drop", "block", or "connectionclose", the UDM field is set to `BLOCK`. If `Action` is "challengefailed" or "jschallengefailed", the UDM field is set to `FAIL`. Otherwise, it's set to `UNKNOWN_ACTION`.  
`ClientASN` | `network.asn` | The value of `ClientASN` from the raw log is directly assigned to this UDM field after converting it to a string.  
`ClientASNDescription` | `additional.fields.key` | The key is statically set to "ClientASNDescription".  
`ClientASNDescription` | `additional.fields.value.string_value` | The value of `ClientASNDescription` from the raw log is directly assigned to this UDM field.  
`ClientCountry` | `principal.location.country_or_region` | The value of `ClientCountry` from the raw log is directly assigned to this UDM field.  
`ClientIP` | `principal.ip` | The value of `ClientIP` from the raw log is directly assigned to this UDM field.  
`ClientRefererHost` | `intermediary.hostname` | The value of `ClientRefererHost` from the raw log is directly assigned to this UDM field.  
`ClientRefererPath` | `network.http.referral_url` | The value of `ClientRefererPath` from the raw log is directly assigned to this UDM field.  
`ClientRequestHost` | `target.hostname` | The value of `ClientRequestHost` from the raw log is directly assigned to this UDM field.  
`ClientRequestMethod` | `network.http.method` | The value of `ClientRequestMethod` from the raw log is directly assigned to this UDM field.  
`ClientRequestPath` | `target.file.full_path` | The value of `ClientRequestPath` from the raw log is directly assigned to this UDM field.  
`ClientRequestProtocol` | `network.application_protocol` | The protocol part of `ClientRequestProtocol` (e.g., "HTTP" from "HTTP/1.1") is extracted using grok, converted to uppercase, and assigned to this UDM field.  
`ClientRequestUserAgent` | `network.http.user_agent` | The value of `ClientRequestUserAgent` from the raw log is directly assigned to this UDM field.  
`Datetime` | `metadata.event_timestamp` | The value of `Datetime` from the raw log is parsed as an RFC 3339 timestamp and assigned to this UDM field.  
`EdgeColoCode` | `additional.fields.key` | The key is statically set to "EdgeColoCode".  
`EdgeColoCode` | `additional.fields.value.string_value` | The value of `EdgeColoCode` from the raw log is directly assigned to this UDM field.  
`EdgeResponseStatus` | `network.http.response_code` | The value of `EdgeResponseStatus` from the raw log is directly assigned to this UDM field and converted to an integer.  
`Kind` | `metadata.product_event_type` | The value of `Kind` from the raw log is directly assigned to this UDM field.  
`Metadata.filter` | `target.resource.attribute.labels.value` | The value of `Metadata.filter` from the raw log is assigned to the `value` field of a label within `target.resource.attribute.labels`. The `key` for this label is statically set to "Metadata filter".  
`Metadata.type` | `target.resource.attribute.labels.value` | The value of `Metadata.type` from the raw log is assigned to the `value` field of a label within `target.resource.attribute.labels`. The `key` for this label is statically set to "Metadata type". The value of this field is derived based on the presence and values of `ClientIP`, `ClientRequestHost`, and `app_protocol`. See parser code for the specific logic. Statically set to "Cloudflare". Statically set to "Cloudflare log Aggregator". Statically set to "CLOUDFLARE_WAF".  
`RayID` | `metadata.product_log_id` | The value of `RayID` from the raw log is directly assigned to this UDM field.  
`RuleID` | `security_result.rule_id` | The value of `RuleID` from the raw log is directly assigned to this UDM field.  
`Source` | `security_result.rule_name` | The value of `Source` from the raw log is directly assigned to this UDM field.  
`timestamp` | `metadata.event_timestamp`, `events.timestamp` | The value of `timestamp` from the raw log is directly assigned to these UDM fields.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudflare-waf-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
