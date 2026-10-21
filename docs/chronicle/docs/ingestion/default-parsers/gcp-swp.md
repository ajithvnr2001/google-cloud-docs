---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-swp/
title: Collect Secure Web Proxy logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:10:44.150134+00:00
---

# Collect Secure Web Proxy logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-swp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Secure Web Proxy logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to export and ingest Secure Web Proxy into Google Security Operations using Cloud Storage. The parser extracts fields from JSON logs, transforming them into the Unified Data Model (UDM). It initializes UDM fields, parses the JSON payload, extracts network information, security details, resource attributes, and sets the event type based on the presence of principal and target information.

## Before you begin

Ensure that you have the following prerequisites:

  * Google SecOps instance.
  * Secure Web Proxy is active and configured in your Google Cloud environment.
  * Privileged access to Google Cloud and appropriate permissions to access Secure Web Proxy logs.



## Create a Cloud Storage bucket

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/).
  2. Go to the **Cloud Storage Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  3. Click **Create**.

  4. On the **Create a bucket** page, enter your bucket information. After each of the following steps, click **Continue** to proceed to the next step:

     1. In the **Get started** section, do the following:

        1. Enter a unique name that meets the bucket name requirements; for example, **gcp-swp-logs**.
        2. To enable hierarchical namespace, click the expander arrow to expand the **Optimize for file oriented and data-intensive workloads** section, and then select **Enable Hierarchical namespace on this bucket**.

**Note:** You cannot enable hierarchical namespace on an existing bucket.
        3. To add a bucket label, click the expander arrow to expand the **Labels** section.

        4. Click **Add label** , and specify a key and a value for your label.

     2. In the **Choose where to store your data** section, do the following:

        1. Select a **Location type**.
        2. Use the location type menu to select a **Location** where object data within your bucket will be permanently stored.

**Note:** If you select the **dual-region** location type, you can also choose to enable **turbo replication** by using the relevant checkbox.
        3. To set up cross-bucket replication, expand the **Set up cross-bucket replication** section.

     3. In the **Choose a storage class for your data** section, either select a **default storage class** for the bucket, or select **Autoclass** for automatic storage class management of your bucket's data.

     4. In the **Choose how to control access to objects** section, select **not** to enforce **public access prevention** , and select an **access control model** for your bucket's objects.

**Note:** If public access prevention is already enforced by your project's organization policy, the **Prevent public access** checkbox is locked.
     5. In the **Choose how to protect object data** section, do the following:

        1. Select any of the options under **Data protection** that you want to set for your bucket.
        2. To choose how your object data will be encrypted, click the expander arrow labeled **Data encryption** , and select a **Data encryption method**.
  5. Click **Create**.


**Note:** Be sure to provide your Google SecOps service account with permissions to Read or Read & Write to the newly created bucket.

## Configure Secure Web Proxy logs export

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/).
  2. Go to **Logging > Log Router**.
  3. Click **Create Sink**.
  4. Provide the following configuration parameters:

     * **Sink Name** : enter a meaningful name; for example, `SWP-Export-Sink`.
     * **Sink Destination** : select **Cloud Storage Storage** and enter the URI for your bucket; for example, `gs://gcp-swp-logs/`.
     * **Log Filter** :
    
    logName="projects/<your-project-id>/logs/networkservices.googleapis.com/gateway_requests"
    

  5. Click **Create**.




## Configure permissions for Cloud Storage

  1. Go to **IAM & Admin > IAM**.
  2. Locate the **Cloud Logging** service account.
  3. Grant the **roles/storage.admin** on the bucket.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed; for example, **Google Cloud SWP Logs**.
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **GCP Secure Web Proxy** as the **Log type**.
  7. Click **Get Service Account** next to the **Chronicle Service Account** field.
  8. Click **Next**.
  9. Specify values for the following input parameters:

     * **Storage Bucket URI** : Cloud Storage bucket URL; for example, `gs://gcp-swp-logs/`. This URL must end with a trailing forward slash (/).
     * **Source deletion options** : select the deletion option according to your preference.

**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Includes files modified in the last number of days. Default is 180 days.

  10. Click **Next**.

  11. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`httpRequest.latency` | `additional.fields[].key`: `HTTPRequest Latency`  
`additional.fields[].value.string_value`: `0.124462s` | Directly mapped from the raw log field.  
`httpRequest.protocol` | `network.application_protocol`: `HTTP`  
`network.application_protocol_version`: `2` | The protocol and version are extracted from the `httpRequest.protocol` field using a grok pattern.  
`httpRequest.remoteIp` | `target.asset.ip`: `1.1.0.1`  
`target.ip`: `1.1.0.1` | The IP address is extracted from the `httpRequest.remoteIp` field using a grok pattern.  
`httpRequest.requestMethod` | `network.http.method`: `GET` | Directly mapped from the raw log field.  
`httpRequest.requestSize` | `network.sent_bytes`: 144 | Directly mapped from the raw log field and converted to an integer.  
`httpRequest.requestUrl` | `target.url`: `https://github.com/tempuslabs/tempusutils/info/refs?service=git-upload-pack` | Directly mapped from the raw log field.  
`httpRequest.responseSize` | `network.received_bytes`: 225 | Directly mapped from the raw log field and converted to an integer.  
`httpRequest.serverIp` | `principal.asset.ip`: `1.8.1.4`  
`principal.ip`: `1.8.1.4` | The IP address is extracted from the `httpRequest.serverIp` field using a grok pattern.  
`httpRequest.status` | `network.http.response_code`: 401 | Directly mapped from the raw log field and converted to an integer.  
`httpRequest.userAgent` | `network.http.user_agent`: `git/2.34.1`  
`network.http.parsed_user_agent`: {  
`family`: `USER_DEFINED`,  
`device`: `git`,  
`device_version`: `2.34.1`  
} | Directly mapped from the raw log field. The `parsed_user_agent` field is derived by parsing the `httpRequest.userAgent` field.  
`insertId` | `metadata.product_log_id`: `1yh8wczer5o8n` | Directly mapped from the raw log field.  
`jsonPayload.@type` | `additional.fields[].key`: `Log Type`  
`additional.fields[].value.string_value`: `type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry` | Directly mapped from the raw log field.  
`jsonPayload.enforcedGatewaySecurityPolicy.hostname` | `target.asset.hostname`: `github.com`  
`target.hostname`: `github.com` | Directly mapped from the raw log field.  
`jsonPayload.enforcedGatewaySecurityPolicy.matchedRules[].action` | `security_result.action`: `ALLOW`  
`security_result.action_details`: `ALLOWED` | The `security_result.action` is derived based on the value of `jsonPayload.enforcedGatewaySecurityPolicy.matchedRules[].action`. If the action is `ALLOWED`, the UDM field is set to `ALLOW`. If the action is `DENIED`, the UDM field is set to `BLOCK`.  
`jsonPayload.enforcedGatewaySecurityPolicy.matchedRules[].name` | `security_result.rule_name`: `projects/671807354785/locations/us-central1/gatewaySecurityPolicies/github-access-gateway-security-policy-5cec30cd/rules/github-access-gateway-security-policy-rule-5cec30cd` | Directly mapped from the raw log field.  
`jsonPayload.enforcedGatewaySecurityPolicy.requestWasTlsIntercepted` | `security_result.detection_fields[].key`: `requestWasTlsIntercepted`  
`security_result.detection_fields[].value`: `true` | Directly mapped from the raw log field.  
`logName` | `additional.fields[].key`: `Log Name`  
`additional.fields[].value.string_value`: `projects/rws-w6uza3pn5jzzh6z3hc3d/logs/networkservices.googleapis.com%2Fgateway_requests` | Directly mapped from the raw log field.  
`receiveTimestamp` | `metadata.collected_timestamp`: {  
`seconds`: 1710189647,  
`nanos`: 661101224  
} | Parsed from the raw log field using the RFC 3339 date format.  
`resource.labels.gateway_name` | `security_result.detection_fields[].key`: `gateway-name`  
`security_result.detection_fields[].value`: `github-access-gateway-5cec30cd` | Directly mapped from the raw log field.  
`resource.labels.gateway_type` | `security_result.detection_fields[].key`: `gateway-type`  
`security_result.detection_fields[].value`: `SECURE_WEB_GATEWAY` | Directly mapped from the raw log field.  
`resource.labels.location` | `target.resource.attribute.cloud.availability_zone`: `us-central1` | Directly mapped from the raw log field.  
`resource.labels.network_name` | `target.resource.attribute.labels[].key`: `rc_network_name`  
`target.resource.attribute.labels[].value`: `projects/rws-w6uza3pn5jzzh6z3hc3d/global/networks/rws-tr-pilot-workspace` | Directly mapped from the raw log field.  
`resource.type` | `target.resource.attribute.labels[].key`: `Resource Type`  
`target.resource.attribute.labels[].value`: `networkservices.googleapis.com/Gateway` | Directly mapped from the raw log field.  
`severity` | `security_result.severity`: `MEDIUM` | Mapped from the raw log field. The value is translated to a UDM severity level. In this case, `WARNING` is mapped to `MEDIUM`.  
`timestamp` | `metadata.event_timestamp`: {  
`seconds`: 1710189639,  
`nanos`: 952848000  
} | Parsed from the raw log field using the RFC 3339 date format.  
(Parser Logic) | `metadata.event_type`: `NETWORK_HTTP` | Determined by parser logic based on the presence of `has_principal`, `has_target`, and a protocol matching `http`.  
(Parser Logic) | `metadata.log_type`: `GCP_SWP` | Hardcoded value based on the product.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-swp-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
