---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cohesity/
title: Collect Cohesity logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:00.314994+00:00
---

# Collect Cohesity logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cohesity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cohesity logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This parser extracts fields from Cohesity backup software syslog messages using grok patterns. It handles both standard syslog messages and JSON-formatted logs, mapping extracted fields to the UDM and dynamically assigning an **event_type** based on the presence of principal and target identifiers.

## Before you begin

Ensure that you have the following prerequisites:

  * Google SecOps instance.
  * Privileged access to Cohesity management.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, feed (for example, **Cohesity Logs**).
  5. Select **Webhook** as the **Source type**.
  6. Select **Cohesity** as the **Log type**.
  7. Click **Next**.
  8. Optional: Specify values for the following input parameters: 
     * **Split delimiter** : the delimiter that is used to separate log lines, such as `\n`.
  9. Click **Next**.
  10. Review the feed configuration in the **Finalize** screen, and then click **Submit**.
  11. Click **Generate Secret Key** to generate a secret key to authenticate this feed.
  12. Copy and store the secret key. You cannot view this secret key again. If needed, you can regenerate a new secret key, but this action makes the previous secret key obsolete.
  13. From the **Details** tab, copy the feed endpoint URL from the **Endpoint Information** field. You need to specify this endpoint URL in your client application.
  14. Click **Done**.



## Create an API key for the webhook feed

  1. Go to **Google Cloud console** > **Credentials**.

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. Click **Create credentials** , and then select **API key**.

  3. Restrict the API key access to the **Chronicle API**.




## Specify the endpoint URL

  1. In your client application, specify the HTTPS endpoint URL provided in the webhook feed.
  2. Enable authentication by specifying the API key and secret key as part of the custom header in the following format:
         
         X-goog-api-key = API_KEY
         X-Webhook-Access-Key = SECRET
         

**Recommendation** : Specify the API key as a header instead of specifying it in the URL.

  3. If your webhook client doesn't support custom headers, you can specify the API key and secret key using query parameters in the following format:
         
         ENDPOINT_URL?key=API_KEY&secret=SECRET
         

Replace the following:

     * `ENDPOINT_URL`: the feed endpoint URL.
     * `API_KEY`: the API key to authenticate to Google SecOps.
     * `SECRET`: the secret key that you generated to authenticate the feed.



## Configuring a Webhook in Cohesity for Google SecOps

  1. Sign in to the Cohesity cluster management.
  2. Go to the **Protection Jobs** section.
  3. Select the protection job for which you want to configure the webhook.
  4. Click **Actions** menu (three vertical dots) next to the protection job > **Edit**.
  5. Select the **Alerting** tab.
  6. Click **\+ Add Webhook**.
  7. Specify values for the following parameters: 
     * **Name** : Provide a descriptive name for the webhook (for example, **Google SecOps**).
     * **URL** : Enter the Google SecOps `<ENDPOINT_URL>`.
     * **Method** : Select **POST**.
     * **Content Type** : Select **application/json**.
     * **Payload** : This field depends on the specific data you want to send.
     * **Enable Webhook** : Check the box to **enable** the webhook.
  8. **Save the Configuration:** Click **Save** to apply the webhook configuration to the protection job.



## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`ClientIP` | `principal.asset.ip` | Directly mapped from `ClientIP` field.  
`ClientIP` | `principal.ip` | Directly mapped from `ClientIP` field.  
`description` | `security_result.description` | Directly mapped from `description` field.  
`DomainName` | `target.asset.hostname` | Directly mapped from `DomainName` field.  
`DomainName` | `target.hostname` | Directly mapped from `DomainName` field.  
`EntityPath` | `target.url` | Directly mapped from `EntityPath` field.  
`host` | `principal.asset.hostname` | Directly mapped from `host` field.  
`host` | `principal.hostname` | Directly mapped from `host` field. Copied from the `ts` field after it's parsed to a timestamp. Determined by parser logic based on the presence of `principal_mid_present`, `target_mid_present`, and `principal_user_present`. Possible values: `NETWORK_CONNECTION`, `USER_UNCATEGORIZED`, `STATUS_UPDATE`, `GENERIC_EVENT`. Hardcoded to "Cohesity".  
`product_event_type` | `metadata.product_event_type` | Directly mapped from `product_event_type` field. Hardcoded to "COHESITY".  
`pid` | `principal.process.pid` | Directly mapped from `pid` field.  
`Protocol` | `network.application_protocol` | Directly mapped from `Protocol` field, converted to uppercase.  
`RecordID` | `additional.fields` (key: "RecordID", value: `RecordID`) | Directly mapped from `RecordID` field, nested under `additional.fields`.  
`RequestType` | `security_result.detection_fields` (key: "RequestType", value: `RequestType`) | Directly mapped from `RequestType` field, nested under `security_result.detection_fields`.  
`Result` | `security_result.summary` | Directly mapped from `Result` field.  
`sha_value` | `additional.fields` (key: "SHA256", value: `sha_value`) | Directly mapped from `sha_value` field, nested under `additional.fields`.  
`target_ip` | `target.asset.ip` | Directly mapped from `target_ip` field.  
`target_ip` | `target.ip` | Directly mapped from `target_ip` field.  
`target_port` | `target.port` | Directly mapped from `target_port` field, converted to integer.  
`Timestamp` | `metadata.collected_timestamp` | Directly mapped from `Timestamp` field after it's parsed to a timestamp.  
`ts` | `events.timestamp` | Directly mapped from `ts` field after it's parsed to a timestamp.  
`UserID` | `principal.user.userid` | Directly mapped from `UserID` field, converted to string.  
`UserName` | `principal.user.user_display_name` | Directly mapped from `UserName` field.  
`UserSID` | `principal.user.windows_sid` | Directly mapped from `UserSID` field.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cohesity-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
