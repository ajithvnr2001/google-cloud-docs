---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-route-53/
title: Collect AWS Route 53 logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:16.671877+00:00
---

# Collect AWS Route 53 logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-route-53/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS Route 53 logs

**Parser Version:** 5.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to configure AWS CloudTrail to store AWS Route 53 DNS logs in an S3 bucket and ingest the logs from S3 to Google Security Operations. Amazon Route 53 provides DNS query logging and the ability to monitor your resources using health checks. Route 53 is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Route 53.

## Before you begin

Ensure you have the following prerequisites:

  * Google SecOps instance
  * Privileged access to AWS



## How to configure AWS Cloudtrail and Route 53

  1. Sign in to the AWS Console.
  2. Search for **Cloudtrail**.
  3. If you don't already have a trail, click **Create trail**.

**Note:** If you already have an existing trail, select it, and ensure it is configured to log Route 53 events. Route 53 logs can be found under **Management Events** in CloudTrail logs.

  1. Provide a **Trail name** .
  2. Select **Create new S3 bucket** (you may also choose to use an existing S3 bucket).
  3. Provide a name for **AWS KMS alias** , or choose an existing **AWS KMS Key**.
  4. Leave the other settings as default, and click **Next**.
  5. Select **Event type** , make sure **Management events** is selected (these are the events that will include Route 53 API calls).
  6. Click **Next**.
  7. Review the settings in **Review and create**.
  8. Click **Create trail**.
  9. In the AWS console, search for **S3**.
  10. Click the newly created log bucket and select the **AWSLogs** folder .
  11. Click **Copy S3 URI** and save it.



## Configure AWS IAM User

  1. In the AWS console, search for **IAM**.
  2. Click **Users**.
  3. Click **Add Users**.
  4. Provide a name for the user (for example, chronicle-feed-user). 
  5. Select **Access key - Programmatic access** as the AWS credential type.
  6. Click **Next: Permissions**.
  7. Select **Attach existing policies directly**.
  8. Select **AmazonS3ReadOnlyAccess** or **AmazonS3FullAccess**. 

**Note:** **AmazonS3FullAccess** would be used if Google SecOps should **clear the S3 buckets after reading logs** , to optimize AWS S3 storage costs. 

  1. Click **Next: Tags**.
  2. Optional: add any tags if required.
  3. Click **Next: Review**.
  4. Review the configuration and click **Create user**.
  5. Copy the Access key ID and Secret access key of the created user.



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**



## How to set up the AWS Route 53 DNS feed

  1. Click the **Amazon Cloud Platform** pack.
  2. Locate the **AWS Route 53 DNS** log type.
  3. Optional: If you're using the Ingestion API for direct log ingestion, specify **AWS Route 53** as the log type.
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

Log field | UDM mapping | Logic  
---|---|---  
account_id | read_only_udm.principal.resource.product_object_id | The AWS account ID associated with the query.  
firewall_domain_list_id | read_only_udm.security_result.rule_labels.value | The ID of the domain list that the domain being queried is a part of.  
firewall_rule_action | read_only_udm.security_result.action | The action performed by the firewall rule that matched the query. Possible values are "ALLOW", "BLOCK", or "UNKNOWN_ACTION" if the action is not recognized.  
firewall_rule_group_id | read_only_udm.security_result.rule_id | The ID of the firewall rule group that matched the query.  
logEvents{}.id | read_only_udm.principal.resource.product_object_id | The unique ID of the log event. Used as a fallback if 'account_id' is not present.  
logEvents{}.message |  | This field is parsed into other UDM fields based on its format.  
logEvents{}.timestamp | read_only_udm.metadata.event_timestamp.seconds | The time when the DNS query was logged.  
messageType |  | This field is used to determine the structure of the log message.  
owner | read_only_udm.principal.user.userid | The AWS account ID of the owner of the log.  
query_class | read_only_udm.network.dns.questions.class | The class of the DNS query.  
query_name | read_only_udm.network.dns.questions.name | The domain name that was queried.  
query_timestamp | read_only_udm.metadata.event_timestamp.seconds | The time when the DNS query was made.  
query_type | read_only_udm.metadata.product_event_type | The type of DNS query.  
rcode | read_only_udm.metadata.description | The response code of the DNS query.  
region | read_only_udm.principal.location.name | The AWS region where the query originated.  
srcaddr | read_only_udm.principal.ip | The IP address of the client that made the DNS query.  
srcids.instance | read_only_udm.principal.hostname | The instance ID of the client that made the DNS query.  
srcids.resolver_endpoint | read_only_udm.security_result.rule_labels.value | The endpoint ID of the resolver that handled the query.  
srcids.resolver_network_interface | read_only_udm.security_result.rule_labels.value | The network interface ID of the resolver that handled the query.  
srcport | read_only_udm.principal.port | The port number of the client that made the DNS query.  
transport | read_only_udm.network.ip_protocol | The transport protocol used for the DNS query.  
version | read_only_udm.metadata.product_version | The version of the Route 53 Resolver Query Logs format.  
N/A | read_only_udm.metadata.event_type | Hardcoded to "NETWORK_DNS".  
N/A | read_only_udm.metadata.product_name | Hardcoded to "AWS Route 53".  
N/A | read_only_udm.metadata.vendor_name | Hardcoded to "AMAZON".  
N/A | read_only_udm.principal.cloud.environment | Hardcoded to "AMAZON_WEB_SERVICES".  
N/A | read_only_udm.network.application_protocol | Hardcoded to "DNS".  
N/A | read_only_udm.network.dns.response_code | Mapped from the "rcode" field using a lookup table.  
N/A | read_only_udm.network.dns.questions.type | Mapped from the "query_type" field using a lookup table.  
N/A | read_only_udm.metadata.product_deployment_id | Extracted from the 'logevent.message_data' field using grok pattern.  
N/A | read_only_udm.network.dns.authority.name | Extracted from the 'logevent.message_data' field using grok pattern.  
N/A | read_only_udm.security_result.rule_labels.key | Set to "firewall_domain_list_id", "resolver_endpoint", or "resolver_network_interface" depending on the available fields.  
N/A | read_only_udm.security_result.action_details | Set to the value of "firewall_rule_action" if it is not "ALLOW" or "BLOCK".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-route-53-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
