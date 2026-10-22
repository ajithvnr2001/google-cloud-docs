---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-s3-server-access/
title: Collect AWS S3 server access logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:16.339342+00:00
---

# Collect AWS S3 server access logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-s3-server-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS S3 server access logs

**Parser Version:** 4.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect AWS S3 server access logs by setting up a Google Security Operations feed. The parser extracts fields using grok patterns, handles potential JSON input, and maps the extracted fields to the UDM. It performs data transformations, type conversions, and conditional logic based on the presence and values of specific fields to ensure accurate UDM representation.

## Before you begin

Ensure you have the following prerequisites:

  * Google SecOps instance
  * Privileged access to AWS



## How to configure AWS S3 server access logging

Google SecOps supports log collection using Amazon S3 through Amazon SQS.

  1. Sign in to the **AWS Management** console.
  2. Access the Amazon S3 console.
  3. Go to **Amazon S3 > Buckets**. 
  4. Select an existing bucket or create a new one.
  5. Click **Properties**.
  6. In the **Server access logging** section, click **Edit**.
  7. Select **Enable**.
  8. In the **Target bucket** field, enter a name for the new bucket to send the log record objects to or select an existing bucket as the target.

**Note:** Your target bucket cannot have server access logging enabled. You can deliver logs to any bucket you own in the same region as the source bucket. However, it is not recommended to use the original source bucket.

  1. Click **Save changes**.
  2. To create the SQS queue for the S3 bucket, configure an Amazon SQS instance with the S3 storage. For more information, see [Configuring a bucket for notifications (SNS topic or SQS queue)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ways-to-add-notification-config-to-bucket.html).

**Note:** IAM user and KMS key policies are required for Amazon S3, AWS KMS, and Amazon SQS.**Note:** For more information, see [Using IAM policies with AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html).

Based on the service and region, identify the endpoints for connectivity by referring to the following AWS documentation:

  * For information about any logging source, see [AWS Identity and Access Management endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/iam-service.html).
  * For information about S3 logging sources, see [Amazon Simple Storage Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html).
  * For information about SQS logging sources, see [Amazon Simple Queue Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sqs-service.html).



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**



## How to set up the AWS S3 Service Access feed

  1. Click the **Amazon Cloud Platform** pack.
  2. Locate the **AWS S3 Service Access** log type.
  3. Google SecOps supports log collection using an access key ID and secret method. To create the access key ID and secret, see [Configure tool authentication with AWS](https://docs.aws.amazon.com/powershell/latest/userguide/creds-idc.html).
  4. Specify the values in the following fields.

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
  5. Click **Create feed**.


**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`aclRequired` | `target.resource.attribute.labels.key`: "aclRequired"  
`target.resource.attribute.labels.value`: Value of `aclRequired` | Directly mapped from the raw log field `aclRequired`.  
`authenticationtype` | `extensions.auth.auth_details` | Directly mapped from the raw log field `authenticationtype`.  
`bucket` | `target.resource.name` | Directly mapped from the raw log field `bucket`.  
`bucket` | `target.resource.resource_type`: "STORAGE_BUCKET" | The parser sets the `resource_type` to "STORAGE_BUCKET" if the `bucket` field is present.  
`bucketowner` | `target.resource.product_object_id` | Directly mapped from the raw log field `bucketowner`.  
`bytes_sent` | `network.sent_bytes` | Directly mapped from the raw log field `bytes_sent` after converting it to an unsigned integer and replacing "-" with "0".  
`ciphersuite` | `network.application_protocol`: "HTTPS" | The parser sets the `application_protocol` to "HTTPS" if the `ciphersuite` field is present.  
`ciphersuite` | `network.tls.cipher` | Directly mapped from the raw log field `ciphersuite`.  
`errorcode` | `security_result.action_details` | Directly mapped from the raw log field `errorcode`.  
`errorcode` | `security_result.action`: "BLOCK" | The parser sets the `action` to "BLOCK" if the `errorcode` field contains "AccessDenied" (case-insensitive).  
`hostheader` | `target.hostname` | Extracted from the raw log field `hostheader`, potentially removing the port number.  
`hostheader` | `target.port` | Extracted from the raw log field `hostheader` if a port number is present.  
`hostid` | `target.resource.attribute.labels.key`: "S3 Extended Request ID"  
`target.resource.attribute.labels.value`: Value of `hostid` | Directly mapped from the raw log field `hostid`.  
`http_capture` | `network.http.method` | The HTTP method is extracted from the `http_capture` field.  
`http_capture` | `network.http.version` | The HTTP version is extracted from the `http_capture` field.  
`http_capture` | `target.url` | The target URL is constructed using `hostheader` and `http_request_uri` (extracted from `http_capture`), prefixed with "http://" or "https://" based on the presence of `ciphersuite`.  
`httpstatus` | `network.http.response_code` | Directly mapped from the raw log field `httpstatus` after converting it to an integer.  
`object_version_id` | `target.resource.product_object_id` | Directly mapped from the raw log field `object_version_id`.  
`objectsize` | `target.file.size` | Directly mapped from the raw log field `objectsize` after converting it to an unsigned integer and replacing "-" with "0".  
`operation` | `metadata.product_event_type` | Directly mapped from the raw log field `operation`.  
`referrer` | `network.http.referral_url` | Directly mapped from the raw log field `referrer` after removing quotes.  
`remoteip` | `metadata.event_type`: "USER_RESOURCE_ACCESS" | The parser sets the `event_type` to "USER_RESOURCE_ACCESS" if the `remoteip` field is empty.  
`remoteip` | `principal.ip` | Directly mapped from the raw log field `remoteip`.  
`requester` | `target.resource.attribute.labels.key`: "Access Point ARN"  
`target.resource.attribute.labels.value`: Value of `requester` | Directly mapped from the raw log field `requester`.  
`requester_user` | `principal.user.userid` | Directly mapped from the raw log field `requester_user`.  
`requestid` | `network.session_id` | Directly mapped from the raw log field `requestid`.  
`request_time_ms` | `network.session_duration.nanos` | Directly mapped from the raw log field `request_time_ms` after converting it to an integer, replacing "-" with "0", and padding with zeros to represent nanoseconds.  
`signatureversion` | `target.resource.attribute.labels.key`: "Signature Version"  
`target.resource.attribute.labels.value`: Value of `signatureversion` | Directly mapped from the raw log field `signatureversion`.  
`time` | `metadata.event_timestamp` | Parsed from the raw log field `time` and converted to a timestamp.  
`tlsVersion` | `network.tls.version` | Directly mapped from the raw log field `tlsVersion`.  
`useragent` | `network.http.user_agent` | Directly mapped from the raw log field `useragent` after removing quotes.  
(Parser Logic) | `metadata.event_type`: "NETWORK_HTTP" | The parser sets the default `event_type` to "NETWORK_HTTP".  
(Parser Logic) | `metadata.log_type`: "AWS_S3_SERVER_ACCESS" | The parser sets the `log_type` to "AWS_S3_SERVER_ACCESS".  
(Parser Logic) | `metadata.product_name`: "AWS S3 Server Access" | The parser sets the `product_name` to "AWS S3 Server Access".  
(Parser Logic) | `metadata.product_version`: "HTTP/`http_version`" | The parser sets the `product_version` using the extracted `http_version`.  
(Parser Logic) | `metadata.vendor_name`: "AMAZON" | The parser sets the `vendor_name` to "AMAZON".  
(Parser Logic) | `network.application_protocol`: "HTTP" | The parser sets the `application_protocol` to "HTTP" if the `ciphersuite` field is not present.  
(Parser Logic) | `timestamp` | The parser sets the event `timestamp` to the current time when the event is processed.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-s3-server-access-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
