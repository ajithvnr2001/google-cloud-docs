---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-network-firewall/
title: Collect AWS Network Firewall logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:09.695657+00:00
---

# Collect AWS Network Firewall logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-network-firewall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS Network Firewall logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest AWS Network Firewall logs to Google Security Operations. AWS Network Firewall is a managed service that provides protection to your VPC against malicious traffic. By sending Network Firewall logs to Google SecOps, you can improve your monitoring, analysis, and threat detection.

## Before you begin

Ensure you have the following prerequisites:

  * Google SecOps instance
  * Privileged access to AWS



## How to configure Logging for AWS Network Firewall

  1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/).
  2. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/).
  3. In the navigation pane, select **Firewalls**.
  4. Select the name of the firewall that you want to edit. 
  5. Select the **Firewall details** tab. 
  6. In the **Logging** section, click **Edit**.
  7. Select the log types: **Flow** , **Alert** and **TLS**.
  8. For each selected log type, choose **S3** for the destination type.

**Note:** In order to change the destination for an existing log type, you must first disable logging for the policy. Then, edit the policy and specify the new destination(s) for the log type.
  9. Click **Save**.




## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**



## How to set up the AWS Network Firewall feed

  1. Click the **Amazon Cloud Platform** pack.
  2. Locate the **AWS Network Firewall** log type.
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

## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`availability_zone` | `target.resource.attribute.cloud.availability_zone` | Directly mapped from the `availability_zone` field.  
`event.app_proto` | `network.application_protocol` | Directly mapped from the `event.app_proto` field, converted to uppercase if not one of the specified values (ikev2, tftp, failed, snmp, tls, ftp). HTTP2 is replaced with HTTP.  
`event.dest_ip` | `target.ip` | Directly mapped from the `event.dest_ip` field.  
`event.dest_port` | `target.port` | Directly mapped from the `event.dest_port` field, converted to integer.  
`event.event_type` | `additional.fields[event_type_label].key` | The key is hardcoded as "event_type".  
`event.event_type` | `additional.fields[event_type_label].value.string_value` | Directly mapped from the `event.event_type` field.  
`event.flow_id` | `network.session_id` | Directly mapped from the `event.flow_id` field, converted to string.  
`event.netflow.age` | `additional.fields[netflow_age_label].key` | The key is hardcoded as "netflow_age".  
`event.netflow.age` | `additional.fields[netflow_age_label].value.string_value` | Directly mapped from the `event.netflow.age` field, converted to string.  
`event.netflow.bytes` | `network.sent_bytes` | Directly mapped from the `event.netflow.bytes` field, converted to unsigned integer.  
`event.netflow.end` | `additional.fields[netflow_end_label].key` | The key is hardcoded as "netflow_end".  
`event.netflow.end` | `additional.fields[netflow_end_label].value.string_value` | Directly mapped from the `event.netflow.end` field.  
`event.netflow.max_ttl` | `additional.fields[netflow_max_ttl_label].key` | The key is hardcoded as "netflow_max_ttl".  
`event.netflow.max_ttl` | `additional.fields[netflow_max_ttl_label].value.string_value` | Directly mapped from the `event.netflow.max_ttl` field, converted to string.  
`event.netflow.min_ttl` | `additional.fields[netflow_min_ttl_label].key` | The key is hardcoded as "netflow_min_ttl".  
`event.netflow.min_ttl` | `additional.fields[netflow_min_ttl_label].value.string_value` | Directly mapped from the `event.netflow.min_ttl` field, converted to string.  
`event.netflow.pkts` | `network.sent_packets` | Directly mapped from the `event.netflow.pkts` field, converted to integer.  
`event.netflow.start` | `additional.fields[netflow_start_label].key` | The key is hardcoded as "netflow_start".  
`event.netflow.start` | `additional.fields[netflow_start_label].value.string_value` | Directly mapped from the `event.netflow.start` field.  
`event.proto` | `network.ip_protocol` | Directly mapped from the `event.proto` field. If the value is "IPv6-ICMP", it's replaced with "ICMP".  
`event.src_ip` | `principal.ip` | Directly mapped from the `event.src_ip` field.  
`event.src_port` | `principal.port` | Directly mapped from the `event.src_port` field, converted to integer.  
`event.tcp.syn` | `additional.fields[syn_label].key` | The key is hardcoded as "syn".  
`event.tcp.syn` | `additional.fields[syn_label].value.string_value` | Directly mapped from the `event.tcp.syn` field, converted to string.  
`event.tcp.tcp_flags` | `additional.fields[tcp_flags_label].key` | The key is hardcoded as "tcp_flags".  
`event.tcp.tcp_flags` | `additional.fields[tcp_flags_label].value.string_value` | Directly mapped from the `event.tcp.tcp_flags` field.  
`event_timestamp` | `metadata.event_timestamp.seconds` | Directly mapped from the `event_timestamp` field, parsed as a timestamp.  
`event_timestamp` | `timestamp.seconds` | Directly mapped from the `event_timestamp` field, parsed as a timestamp.  
`firewall_name` | `metadata.product_event_type` | Directly mapped from the `firewall_name` field. Set to "NETWORK_CONNECTION" if both `event.src_ip` and `event.dest_ip` are present, otherwise set to "GENERIC_EVENT". Hardcoded to "AWS Network Firewall". Hardcoded to "AWS".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-network-firewall-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
