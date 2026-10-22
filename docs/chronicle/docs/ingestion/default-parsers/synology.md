---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/synology/
title: Collect Synology logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:37.893780+00:00
---

# Collect Synology logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/synology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Synology logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This parser extracts fields from Synology SYSLOG messages using grok patterns, mapping them to the UDM. It handles various log formats, identifies user logins and resource access, and categorizes events based on keywords, enriching the data with vendor and product information.

## Before you begin

Ensure that you have the following prerequisites:

  * Google SecOps instance.
  * Privileged access to Synology DSM.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed; for example, **Synology Logs**.
  5. Select **Webhook** as the **Source type**.
  6. Select **Synology** as the **Log type**.
  7. Click **Next**.
  8. Optional: Specify values for the following input parameters: 
     * **Split delimiter** : the delimiter that is used to separate log lines, such as `\n`.
     * **Asset namespace** : the [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : the label applied to the events from this feed.
  9. Click **Next**.
  10. Review the feed configuration in the **Finalize** screen, and then click **Submit**.
  11. Click **Generate Secret Key** to generate a secret key to authenticate this feed.
  12. Copy and store the secret key. You cannot view this secret key again. If needed, you can regenerate a new secret key, but this action makes the previous secret key obsolete.
  13. From the **Details** tab, copy the feed endpoint URL from the **Endpoint Information** field. You need to specify this endpoint URL in your client application.
  14. Click **Done**.



## Create an API key for the webhook feed

  1. Go to **Google Cloud console > Credentials**.

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. Click **Create credentials** , and then select **API key**.

  3. Restrict the API key access to the **Google Security Operations API**.




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
     * `API_KEY`: the API key to authenticate to Google Security Operations.
     * `SECRET`: the secret key that you generated to authenticate the feed.



## Creating a Webhook in Synology for Google SecOps

  1. Sign in to DiskStation Manager (DSM) on your Synology NAS.
  2. Go to **Control Panel** > **Notification** > **Webhook**.
  3. Click **Add**.
  4. Specify values for the following parameters:

     * **Provider** : Select **Custom**.
     * **Rule** : Select what kind of messages you want to send in your webhook.

**Note:** You can a create custom rule by selecting **Create**.
     * Click **Next**.

     * **Provider name** : Give the webhook a distinctive name (for example, **Google SecOps**).

     * **Subject** : Will be added as a prefix of the notification message. 

     * **Webhook URL** : Enter **ENDPOINT_URL**.

     * Select **Send notification messages in English**.

     * Click **Next**.

     * **HTTP Method** : Select **POST**.

     * Add Header **X-Webhook-Access-Key** , with **SECRET** value.

     * Add Header **X-goog-api-key** , with **API_KEY** value.

     * Click **Apply**.

  5. Click **Apply** to save the webhook.




## UDM Mapping Table

Log field | UDM mapping | Logic  
---|---|---  
`app` | `target.application` | The value of the `app` field extracted by the grok filter is assigned to `target.application`.  
`desc` | `metadata.description` | The value of the `desc` field extracted by the grok filter is assigned to `metadata.description`.  
`desc` | `target.file.names` | If the `desc` field contains "Closed)", the file path within the parentheses is extracted and assigned to `target.file.names`. If the `desc` field contains "accessed shared folder", the folder path within the brackets is extracted and assigned to `target.file.names`.  
`host` | `principal.hostname` | The value of the `host` field extracted by the grok filter from the `host_and_ip` field is assigned to `principal.hostname`.  
`host_and_ip` | `principal.ip` | The `host_and_ip` field is parsed. If an IP address (`ip1`) is found, it's assigned to `principal.ip`. If a second IP address (`ip2`) is found, it's also added to `principal.ip`.  
`intermediary_host` | `intermediary.hostname` | The value of the `intermediary_host` field extracted by the grok filter is assigned to `intermediary.hostname`. An empty `auth` object is created within `extensions` if the message contains "signed in" or "sign in". The timestamp from the raw log's `collection_time` field is used. If the message contains "signed in" or "sign in", the value is set to `USER_LOGIN`. If the message contains "accessed shared folder", the value is set to `USER_RESOURCE_ACCESS`. Otherwise, it defaults to `GENERIC_EVENT`. The value of the `type` field extracted by the grok filter is assigned to `metadata.product_event_type`. The value is statically set to "SYNOLOGY". The value is statically set to "SYNOLOGY". If the message contains "failed to sign", the value is set to `BLOCK`. If the message contains "success", the value is set to `ALLOW`. If the `severity` field (extracted by grok) is "INFO", the value is set to `INFORMATIONAL`.  
`severity` | `security_result.severity` | The value of the `severity` field extracted by the grok filter is used to determine the `security_result.severity`. If the value is "INFO", it's mapped to "INFORMATIONAL".  
`time` | `metadata.event_timestamp` | The `time` field, extracted by the grok filter, is parsed and converted to a timestamp. This timestamp is then assigned to `metadata.event_timestamp`.  
`type` | `metadata.product_event_type` | The value of the `type` field extracted by the grok filter is assigned to `metadata.product_event_type`.  
`user` | `target.administrative_domain` | If a domain is extracted from the `user` field, it's assigned to `target.administrative_domain`.  
`user` | `target.user.userid` | The username part of the `user` field (before the "\" if present) is extracted and assigned to `target.user.userid`. The timestamp from the raw log's `collection_time` field is used.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/synology-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
