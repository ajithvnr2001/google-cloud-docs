---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azion/
title: Collect Azion firewall logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:08.002803+00:00
---

# Collect Azion firewall logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Azion firewall logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This parser extracts fields from Azion firewall JSON logs, performs data type conversions and enrichment (for example, user-agent parsing), and maps the extracted fields to the UDM. It generates **NETWORK_HTTP** , **SCAN_UNCATEGORIZED** , or **GENERIC_EVENT** events based on the presence of principal and target machines. It also handles WAF-related fields and actions, mapping them to UDM security result fields.

## Before you begin

Ensure that you have the following prerequisites:

  * Google SecOps instance.
  * Privileged access to AWS IAM and S3.
  * Privileged access to an active Azion account.



## Configure Amazon S3 bucket

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
  2. Save bucket **Name** and **Region** for future reference.
  3. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**. 
  5. Select **Security credentials** tab.
  6. Click **Create Access Key** in section **Access Keys**.
  7. Select **Third-party service** as **Use case**.
  8. Click **Next**.
  9. Optional: Add description tag.
  10. Click **Create access key**.
  11. Click **Download .csv file**. (Save **Access Key** and **Secret Access Key** for future reference). 
  12. Click **Done**.
  13. Select **Permissions** tab.
  14. Click **Add permissions** in section **Permissions policies**.
  15. Select **Add permissions**.
  16. Select **Attach policies directly**.
  17. Search for **AmazonS3FullAccess** policy.
  18. Select the policy.
  19. Click **Next**.
  20. Click **Add permissions**.



## Configure Azion for continuous log delivery to Amazon S3

  1. In the Azion console, go to to the **DataStream** section.
  2. Click **\+ Stream**.
  3. Specify values for the following parameters: 
     * **Name** : Provide a unique and descriptive name to identify the data stream.
     * **Source** : Select the source to collect the data from.
     * **Template** : A preset of variables for specific sources or an open template to choose variables. You have the option to filter domains.
  4. In **Destination** section, click **Connector** > **Simple Storage Service (S3)**. 
     * **URL** : the bucket URI. `s3:/BUCKET_NAME`. Replace the following: 
       * `BUCKET_NAME`: the name of the bucket.
     * **Bucket Name** : Name of the bucket to which the object will be sent.
     * **Region** : Region where your bucket is located.
     * **Access Key** : User access key with access to the s3 bucket.
     * **Secret Key** : User secret key with access to the s3 bucket.
     * **Content Type** : Select plain/text.
  5. Click **Save**.



For more information, see [How to use Amazon S3 to receive data from Data Stream](https://www.azion.com/en/documentation/products/guides/endpoint-amazon-s3/)

## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, **Azion Logs**).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select Azion as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **S3 URI** : the bucket URI. `s3:/BUCKET_NAME`. Replace the following:

       * `BUCKET_NAME`: the name of the bucket.
     * **Source deletion options** : select deletion option according to your preference.

     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days. Note: If you select the **Delete transferred files** or **Delete transferred files and empty directories** option, make sure that you granted appropriate permissions to the service account.

     * **Access Key ID** : the User access key with access to the s3 bucket.

     * **Secret Access Key** : the User secret key with access to the s3 bucket.

     * **Asset namespace** : the [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : the label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
**`asn`** | **`read_only_udm.network.asn`** | Directly mapped from the **`asn`** field.  
**`bytes_sent`** | **`read_only_udm.network.sent_bytes`** | Directly mapped from the **`bytes_sent`** field, converted to unsigned integer.  
**`country`** | **`read_only_udm.principal.location.country_or_region`** | Directly mapped from the **`country`** field.  
**`host`** | **`read_only_udm.principal.hostname`** | Directly mapped from the **`host`** field.  
**`http_referer`** | **`read_only_udm.network.http.referral_url`** | Directly mapped from the **`http_referer`** field.  
**`http_user_agent`** | **`read_only_udm.network.http.user_agent`** | Directly mapped from the **`http_user_agent`** field.  
**`http_user_agent`** | **`read_only_udm.network.http.parsed_user_agent`** | Parsed from the **`http_user_agent`** field using the **`parseduseragent`** filter.  
| **`read_only_udm.event_type`** | Determined by the parser based on the presence of **`principal`** and **`target`** information. Can be **NETWORK_HTTP** , **SCAN_UNCATEGORIZED** , or **GENERIC_EVENT**.  
| **`read_only_udm.metadata.product_name`** | Hardcoded to **"AZION"**.  
| **`read_only_udm.metadata.vendor_name`** | Hardcoded to **"AZION"**.  
| **`read_only_udm.metadata.product_version`** | Hardcoded to **"AZION"**.  
**`remote_addr`** | **`read_only_udm.principal.ip`** | Directly mapped from the **`remote_addr`** field.  
**`remote_port`** | **`read_only_udm.principal.port`** | Directly mapped from the **`remote_port`** field, converted to integer.  
**`requestPath`** | **`read_only_udm.target.url`** | Directly mapped from the **`requestPath`** field if **`request_uri`** is not present.  
**`request_method`** | **`read_only_udm.network.http.method`** | Directly mapped from the **`request_method`** field, converted to uppercase.  
**`request_time`** | **`read_only_udm.additional.fields`** | Added as a key-value pair to the **`additional.fields`** array, with key **"request_time"** and value from the **`request_time`** field.  
**`request_uri`** | **`read_only_udm.target.url`** | Directly mapped from the **`request_uri`** field if present.  
**`server_addr`** | **`read_only_udm.target.ip`** | Directly mapped from the **`server_addr`** field.  
**`server_port`** | **`read_only_udm.target.port`** | Directly mapped from the **`server_port`** field, converted to integer.  
**`ssl_cipher`** | **`read_only_udm.network.tls.cipher`** | Directly mapped from the **`ssl_cipher`** field.  
**`ssl_protocol`** | **`read_only_udm.network.tls.version_protocol`** | Directly mapped from the **`ssl_protocol`** field.  
**`ssl_server_name`** | **`read_only_udm.network.tls.client.server_name`** | Directly mapped from the **`ssl_server_name`** field.  
**`state`** | **`read_only_udm.principal.location.state`** | Directly mapped from the **`state`** field.  
**`status`** | **`read_only_udm.network.http.response_code`** | Directly mapped from the **`status`** field, converted to integer.  
**`time`** | **`read_only_udm.metadata.event_timestamp`** | Parsed from the **`time`** field using date filter and multiple date formats.  
**`upstream_addr`** | **`read_only_udm.intermediary.ip`** , **`read_only_udm.intermediary.port`** | Extracted from the **`upstream_addr`** field using grok, splitting into IP and port.  
**`upstream_status`** | **`read_only_udm.additional.fields`** | Added as a key-value pair to the **`additional.fields`** array, with key **"upstream_status"** and value from the **`upstream_status`** field.  
**`waf_args`** | **`read_only_udm.security_result.detection_fields`** | Added as a key-value pair to the **`security_result.detection_fields`** array.  
**`waf_attack_action`** | **`read_only_udm.security_result.detection_fields`** | Added as a key-value pair to the **`security_result.detection_fields`** array.  
**`waf_attack_family`** | **`read_only_udm.security_result.detection_fields`** | Added as a key-value pair to the **`security_result.detection_fields`** array.  
**`waf_headers`** | **`read_only_udm.security_result.detection_fields`** | Added as a key-value pair to the **`security_result.detection_fields`** array.  
**`waf_learning`** | **`read_only_udm.security_result.detection_fields`** | Added as a key-value pair to the **`security_result.detection_fields`** array.  
**`waf_match`** | **`read_only_udm.security_result.detection_fields`** | Added as a key-value pair to the **`security_result.detection_fields`** array.  
**`waf_score`** | **`read_only_udm.security_result.detection_fields`** | Added as a key-value pair to the **`security_result.detection_fields`** array.  
**`waf_server`** | **`read_only_udm.security_result.detection_fields`** | Added as a key-value pair to the **`security_result.detection_fields`** array.  
**`waf_total_blocked`** | **`read_only_udm.security_result.detection_fields`** | Added as a key-value pair to the **`security_result.detection_fields`** array.  
**`waf_total_processed`** | **`read_only_udm.security_result.detection_fields`** | Added as a key-value pair to the **`security_result.detection_fields`** array.  
**`waf_uri`** | **`read_only_udm.security_result.detection_fields`** | Added as a key-value pair to the **`security_result.detection_fields`** array.  
| **`read_only_udm.security_result.action`** | Determined by the parser based on the **`waf_block`** or **`blocked`** fields. Set to **ALLOW** or **BLOCK**.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azion-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
