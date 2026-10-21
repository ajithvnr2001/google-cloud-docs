---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-cloudfront/
title: Collect Amazon CloudFront logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:46:51.913902+00:00
---

# Collect Amazon CloudFront logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-cloudfront/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Amazon CloudFront logs

**Parser Version:** 10.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how you can collect Amazon CloudFront logs by setting up a Google Security Operations feed.

For more information, see [Data ingestion to Google Security Operations overview](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow).

An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `AWS_CLOUDFRONT` ingestion label.

## Before you begin

Make sure that the Amazon S3 bucket is created. For more information, see [Create your first S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).

## Configure Amazon CloudFront

  1. Sign in to the [AWS Management](https://signin.aws.amazon.com/) console.
  2. Access the Amazon S3 console, and create the Amazon S3 bucket.
  3. Click **On** to enable logging.
  4. In the **Bucket for logs** field, specify the Amazon S3 bucket name.
  5. In the **Log prefix** field, specify an optional prefix.
  6. After the logs files are stored in the Amazon S3 bucket, create an SQS queue, and attach it with the Amazon S3 bucket.



## Identify the endpoints for connectivity

Check the required Identity and Access Management user and KMS key policies for S3, SQS, and KMS.

Based on the service and region, identify the endpoints for connectivity by referring to the following AWS documentation:

  * For information about any logging sources, see [AWS Identity and Access Management endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/iam-service.html).
  * For information about S3 logging sources, see [Amazon Simple Storage Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html).
  * For information about SQS logging sources, see [Amazon Simple Queue Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sqs-service.html).



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New**
  * **Content Hub > Content Packs > Get Started**



## How to set up the AWS CloudFront feed

  1. Click the **Amazon Cloud Platform** pack.
  2. Locate the **AWS CloudFront** log type.
  3. Specify the values in the following fields.

     * **Source Type** : Amazon SQS V2
     * **Queue Name** : The SQS queue name to read from
     * **S3 URI** : The bucket URI. 
       * `s3://your-log-bucket-name/`
         * Replace `your-log-bucket-name` with the actual name of your S3 bucket.
     * **Source deletion options** : Select the deletion option according to your ingestion preferences.

**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **SQS Queue Access Key ID** : An account access key that is a 20-character alphanumeric string.

     * **SQS Queue Secret Access Key** : An account access key that is a 40-character alphanumeric string.

**Advanced options**

     * **Feed Name** : A prepopulated value that identifies the feed.
     * **Asset Namespace** : Namespace associated with the feed.
     * **Ingestion Labels** : Labels applied to all events from this feed.
  4. Click **Create feed**.


**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

## Field mapping reference

This parser extracts fields from AWS CloudFront logs in either SYSLOG or JSON format, normalizing them into the UDM. It uses grok patterns to parse message strings, handles various data transformations (e.g., type conversions, renaming), and enriches the data with additional context like user agent parsing and application protocol identification.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`c-ip` | `principal.ip` | Directly mapped. Also mapped to `principal.asset.ip`.  
`c-port` | `principal.port` | Directly mapped.  
`cs(Cookie)` | `additional.fields[].key`: "cookie"  
`additional.fields[].value.string_value`: Directly mapped. | Conditionally mapped if `cs(Cookie)` is present and `agent` does not contain "://".  
`cs(Host)` | `principal.hostname` | Directly mapped. Also mapped to `principal.asset.hostname`. Used in constructing the `target.url` if other URL fields are not available.  
`cs(Referer)` | `network.http.referral_url` | Directly mapped.  
`cs(User-Agent)` | `network.http.user_agent` | Directly mapped. Also mapped to `network.http.parsed_user_agent` and parsed into its components if it does not contain "://".  
`cs-bytes` | `network.sent_bytes` | Directly mapped. Converted to unsigned integer.  
`cs-method` | `network.http.method` | Directly mapped.  
`cs-protocol` | `network.application_protocol` | Mapped after converting to uppercase. If the value is not recognized as a standard application protocol and `cs-protocol-version` contains "HTTP", then `network.application_protocol` is set to "HTTP".  
`dport` | `target.port` | Directly mapped. Converted to integer.  
`edge_location` | `principal.location.name` | Directly mapped.  
`fle-encrypted-fields` | `additional.fields[].key`: "fle-encrypted-fields"  
`additional.fields[].value.string_value`: Directly mapped. | Conditionally mapped if present.  
`fle-status` | `additional.fields[].key`: "fle-status"  
`additional.fields[].value.string_value`: Directly mapped. | Conditionally mapped if present.  
`host` | `principal.hostname`, `principal.asset.hostname` | Directly mapped.  
`id` | `principal.asset_id` | Directly mapped with the prefix "id: ".  
`ip` | `target.ip`, `target.asset.ip` | Directly mapped.  
`log_id` | `metadata.product_log_id` | Directly mapped.  
`resource` | `additional.fields[].key`: "resource"  
`additional.fields[].value.string_value`: Directly mapped. | Conditionally mapped if present.  
`result_type` | `additional.fields[].key`: "result_type"  
`additional.fields[].value.string_value`: Directly mapped. | Conditionally mapped if present.  
`sc-bytes` | `network.received_bytes` | Directly mapped. Converted to unsigned integer.  
`sc-content-len` | `additional.fields[].key`: "sc-content-len"  
`additional.fields[].value.string_value`: Directly mapped. | Conditionally mapped if present.  
`sc-content-type` | `additional.fields[].key`: "sc-content-type"  
`additional.fields[].value.string_value`: Directly mapped. | Conditionally mapped if present.  
`sc-status` | `network.http.response_code` | Directly mapped. Converted to integer.  
`ssl-cipher` | `network.tls.cipher` | Directly mapped.  
`ssl-protocol` | `network.tls.version` | Directly mapped.  
`timestamp` | `metadata.event_timestamp` | Parsed and mapped if available. Different formats are supported.  
`ts` | `metadata.event_timestamp` | Parsed and mapped if available. ISO8601 format is expected.  
`url` | `target.url` | Directly mapped.  
`url_back_to_product` | `metadata.url_back_to_product` | Directly mapped.  
`x-edge-detailed-result-type` | `additional.fields[].key`: "x-edge-detailed-result-type"  
`additional.fields[].value.string_value`: Directly mapped. | Conditionally mapped if present.  
`x-edge-location` | `additional.fields[].key`: "x-edge-location"  
`additional.fields[].value.string_value`: Directly mapped. | Conditionally mapped if present.  
`x-edge-request-id` | `additional.fields[].key`: "x-edge-request-id"  
`additional.fields[].value.string_value`: Directly mapped. | Conditionally mapped if present.  
`x-edge-response-result-type` | `additional.fields[].key`: "x-edge-response-result-type"  
`additional.fields[].value.string_value`: Directly mapped. | Conditionally mapped if present.  
`x-edge-result-type` | `additional.fields[].key`: "x-edge-result-type"  
`additional.fields[].value.string_value`: Directly mapped. | Conditionally mapped if present.  
`x-forwarded-for` | `target.ip`, `target.asset.ip` | Directly mapped. If multiple IPs are present (comma-separated), they are split and merged into the respective UDM fields.  
`x-host-header` | `target.hostname`, `target.asset.hostname` | Directly mapped. Set to "NETWORK_HTTP" if either `ip` or `x-forwarded-for` and `http_verb` are present. Otherwise, set to "GENERIC_EVENT". Hardcoded to "AWS_CLOUDFRONT". Hardcoded to "AWS CloudFront". Hardcoded to "AMAZON". The ingestion time of the log entry into Google Security Operations.  
`cs_cookie` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`time-taken` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`time-to-first-byte` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cribl_pipe` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs-referer` | `event.idm.read_only_udm.network.http.referer` | Mapped from changelog  
`cs-uri-query` | `event.idm.read_only_udm.network.http.url_details.query` | Mapped from changelog  
`cs-user-agent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`cs-uri-stem` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`x-forwarded-for` | `security_result.detection_fields` | Mapped from changelog  
`avgrequestTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`htmlType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`responseTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`securityKey` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`bytes` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`srcport` | `event.idm.read_only_udm.src.port` | Mapped from changelog  
`encryptionType` | `event.idm.read_only_udm.security_result.about.resource.name` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`scrip` | `event.idm.read_only_udm.src.ip` | Mapped from changelog  
`targetip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`targetip` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`tlsvVersion` | `event.idm.read_only_udm.network.tls.version` | Mapped from changelog  
`CloudFront-Is-Desktop-Viewer` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`CloudFront-Is-Mobile-Viewer` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`CloudFront-Is-SmartTV-Viewer` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`CloudFront-Is-Tablet-Viewer` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vDetails` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`x-envoy-expected-rq-timeout-ms` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x-envoy-external-address` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x-envoy-original-authority` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x-f5-cdn-tls-ja3` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x-f5-cdn-tls-ja4` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x-forwarded-proto` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`xc-trusted-source` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ipType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`method` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`x-request-id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`version` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`requestCode` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`ipAddress` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`uri_query` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Bucket` | `target.resource.name` | Mapped from changelog  
`accountID` | `principal.user.userid` | Mapped from changelog  
`file` | `target.file.full_path` | Mapped from changelog  
`region` | `principal.location.country_or_region` | Mapped from changelog  
`msg` | `metadata.description` | Mapped from changelog  
`service", "aggregation", "func", "requestID", "lpcltype", "lpclagg", "level" and "LoggingEnabled` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-cloudfront-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
