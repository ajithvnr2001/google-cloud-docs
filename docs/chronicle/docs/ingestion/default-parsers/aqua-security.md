---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aqua-security/
title: Collect Aqua Security logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:05.637421+00:00
---

# Collect Aqua Security logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aqua-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Aqua Security logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This parser extracts fields from Aqua Security logs, transforming them into the Unified Data Model (UDM). It parses the `message` field as JSON, extracts user, source IP, and other relevant fields, maps them to UDM fields, and categorizes events based on the `action` field, enriching the data with security context like rule names, descriptions, and CVE details.

## Before you begin

Ensure that you have the following prerequisites:

  * Google SecOps instance.
  * Privileged access to Aqua Security management console.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, **Aqua Security Logs**).
  5. Select **Webhook** as the **Source type**.
  6. Select **Aqua Security** as the **Log type**.
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



## Creating a Webhook in Aqua Security for Google SecOps

  1. Sign in to Aqua Security console.
  2. Go to **Settings** > **Image Scan Results Webhook**.
  3. Check the **Enable sending image scan results** checkbox.
  4. Enter the `<ENDPOINT_URL>`, followed by `<API_KEY>` and `<SECRET>`.
  5. Click **Save**.



## UDM Mapping Table

Log Field (Ascending) | UDM Mapping | Logic  
---|---|---  
jsonPayload.action | metadata.event_type | Mapped based on the value of 'jsonPayload.action'. See parser code for specific mappings.  
jsonPayload.action | security_result.summary | Directly mapped.  
jsonPayload.adjective | target.file.full_path | Directly mapped if 'jsonPayload.container' is empty.  
jsonPayload.category | target.asset.category | Directly mapped.  
jsonPayload.cfappname | target.application | Directly mapped.  
jsonPayload.cfspace | principal.user.userid | Directly mapped if 'jsonPayload.user' is empty.  
jsonPayload.command | principal.ip | Extracted using grok pattern "user %{GREEDYDATA:user_id} \\(%{IP:src_ip}\\)".  
jsonPayload.command | principal.user.userid | Extracted using grok pattern "user %{GREEDYDATA:user_id} \\(%{IP:src_ip}\\)".  
jsonPayload.container | target.asset.product_object_id | Directly mapped.  
jsonPayload.data | security_result.detection_fields | Parsed as key-value pairs and mapped to individual fields within 'security_result.detection_fields'.  
jsonPayload.description | security_result.description | Directly mapped if 'jsonPayload.reason' is empty.  
jsonPayload.host | principal.hostname | Directly mapped.  
jsonPayload.hostgroup | target.group.group_display_name | Directly mapped.  
jsonPayload.hostid | target.asset_id | Mapped as "host id: %{jsonPayload.hostid}".  
jsonPayload.hostip | target.ip | Directly mapped.  
jsonPayload.image | target.file.full_path | Directly mapped.  
jsonPayload.level | security_result.action | Set to "ALLOW" if 'jsonPayload.level' is "success".  
jsonPayload.reason | security_result.description | Directly mapped.  
jsonPayload.rule | security_result.rule_name | Directly mapped.  
jsonPayload.user | principal.user.userid | Directly mapped.  
jsonPayload.vm_location | target.asset.location.name | Directly mapped.  
jsonPayload.vm_name | target.resource.name | Directly mapped.  
resource.labels.instance_id | target.resource.id | Directly mapped.  
resource.labels.project_id | target.asset.attribute.cloud.project.id | Directly mapped.  
resource.labels.zone | target.asset.attribute.cloud.availability_zone | Directly mapped.  
timestamp | metadata.event_timestamp | Directly mapped after converting to ISO8601 format.  
| extensions.auth.type | Set to "SSO" if 'jsonPayload.description' contains "SAML", otherwise set to "AUTHTYPE_UNSPECIFIED" if 'jsonPayload.action' is "login" or "Login".  
| metadata.log_type | Set to "AQUA_SECURITY".  
| metadata.product_name | Set to "AQUA_SECURITY".  
| metadata.vendor_name | Set to "AQUA_SECURITY".  
| target.asset.attribute.cloud.environment | Set to "GOOGLE_CLOUD_PLATFORM".  
| target.resource.type | Set to "VIRTUAL_MACHINE".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aqua-security-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
