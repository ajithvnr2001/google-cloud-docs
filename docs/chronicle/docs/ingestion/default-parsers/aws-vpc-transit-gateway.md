---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-vpc-transit-gateway/
title: Collect Amazon VPC Transit Gateway Flow Logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:48:34.710277+00:00
---

# Collect Amazon VPC Transit Gateway Flow Logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-vpc-transit-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Amazon VPC Transit Gateway Flow Logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Amazon VPC Transit Gateway Flow Logs into Google Security Operations using Amazon S3 or Amazon Kinesis Data Firehose. Transit Gateway Flow Logs capture detailed network traffic metadata (source and destination IPs, ports, protocols, byte and packet counts, actions) across your Transit Gateway attachments. This data enables security monitoring, anomaly detection, and compliance auditing within Google SecOps.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * Privileged access to AWS with permissions to: 
    * Create and manage Transit Gateway flow logs
    * Create S3 buckets (for S3 export option)
    * Create IAM users, policies, and roles
    * Configure Kinesis Data Firehose delivery streams (for Firehose option)
    * Access CloudWatch Logs and create subscription filters (for Firehose option)



## Option - Export to Amazon S3

### Enable Transit Gateway Flow Logs (to S3)

  1. Open the **Amazon VPC console** at <https://console.aws.amazon.com/vpc/>.
  2. In the navigation pane, choose **Transit gateways**.
  3. Select the checkboxes for one or more transit gateways and choose **Actions > Create flow log**.
  4. For **Destination** , select **Send to an Amazon S3 bucket**.
  5. For **S3 bucket ARN** , enter the ARN of an existing S3 bucket (for example, `arn:aws:s3:::tgw-flowlogs-bucket`).

**Note:** You can include a subfolder path in the ARN (for example, `arn:aws:s3:::tgw-flowlogs-bucket/flow-logs/`).
  6. For **Log record format** , select the format for the flow log record:

     * **AWS default format** \- includes all version 2 through version 6 fields.
     * **Custom format** \- select only the fields you need.
  7. For **Log file format** , select **Text** (default) or **Parquet**.

  8. For **Hive-compatible S3 prefix** , optionally select **Enable** to use Hive-compatible prefixes for partitioning.

  9. For **Partition logs by time** , select **Every 1 hour (60 min)** or **Every 24 hours (1440 min)**.

  10. (Optional) Choose **Add new tag** to apply tags to the flow log.

  11. Click **Create flow log**.




### Create an Amazon S3 bucket

**Note:** Skip this section if you already have an S3 bucket for Transit Gateway flow logs.

  1. Open the **Amazon S3 console**.
  2. Click **Create bucket**.
  3. Provide the following configuration details: 
     * **Bucket name** : Enter a unique name (for example, `tgw-flowlogs-bucket`)
     * **AWS Region** : Select the same Region where your Transit Gateway resides
  4. Click **Create bucket**.



### Create an IAM user with access to Amazon S3

  1. Open the **IAM console**.
  2. Click **Users > Add user**.
  3. Enter a **user name** (for example, `chronicle-tgw-s3-reader`).
  4. Select **Programmatic access**.
  5. Click **Next: Permissions**.
  6. Choose **Attach existing policies directly**.
  7. Search for and select the **AmazonS3ReadOnlyAccess** policy.
  8. Click **Next: Tags > Next: Review > Create user**.
  9. Copy the **Access Key ID** and **Secret Access Key** for the Google SecOps feed configuration.



### Configure a feed in Google SecOps to ingest Amazon VPC Transit Gateway Flow Logs (S3)

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `AWS Transit Gateway Flow Logs - S3`).
  4. Select **Amazon S3** as the **Source type**.
  5. Select **Amazon VPC Transit Gateway Flow Logs** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters:

     * **S3 URI** : The bucket URI (for example, `s3://tgw-flowlogs-bucket/flow-logs/`)
**Note:** Include the trailing slash (/) at the end of the S3 URI.
     * **Source deletion option** : Select the deletion option according to your preference: 
       * **Never** : Never deletes any files after transfers.
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Access Key ID** : The IAM user access key with access to the S3 bucket
     * **Secret Access Key** : The IAM user secret key with access to the S3 bucket
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  8. Click **Next**.

  9. Review the feed configuration and click **Submit**.




## Option - Stream via Amazon Kinesis Data Firehose

### Enable Transit Gateway Flow Logs (to CloudWatch Logs)

  1. Open the **Amazon VPC console** at <https://console.aws.amazon.com/vpc/>.
  2. In the navigation pane, choose **Transit gateways**.
  3. Select the checkboxes for one or more transit gateways and choose **Actions > Create flow log**.
  4. For **Destination** , select **Send to CloudWatch Logs**.
  5. For **Destination log group** , choose an existing log group or enter a new name to create one (for example, `/aws/tgw/flowlogs`).

**Note:** If the destination log group does not yet exist, entering a new name creates it automatically.
  6. For **IAM role** , specify a role that has permissions to publish logs to CloudWatch Logs.

  7. For **Log record format** , select the format for the flow log record:

     * **AWS default format** \- includes all version 2 through version 6 fields.
     * **Custom format** \- select only the fields you need.
  8. (Optional) Choose **Add new tag** to apply tags to the flow log.

  9. Click **Create flow log**.




### Create a feed in Google SecOps to ingest Amazon VPC Transit Gateway Flow Logs (Firehose)

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `AWS Transit Gateway Flow Logs - Firehose`).
  4. Select **Amazon Data Firehose** as the **Source type**.
  5. Select **Amazon VPC Transit Gateway Flow Logs** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters: 
     * **Split delimiter** : Enter `\n`
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  8. Click **Next**.
  9. Review the feed configuration and click **Submit**.
  10. Click **Generate Secret Key** to generate a secret key to authenticate this feed.
  11. **Copy** and **save** the secret key. You cannot view this secret again.
  12. Go to the **Details** tab.
  13. **Copy** the feed endpoint URL from the **Endpoint Information** field.
  14. Click **Done**.



### Create an API key for the Amazon Data Firehose feed

  1. Go to the **Google Cloud console** **Credentials** page at <https://console.cloud.google.com/apis/credentials>.
  2. Click **Create credentials** , and then select **API key**.
  3. Click **Edit API key** to restrict the key.
  4. Under **API restrictions** , select **Restrict key**.
  5. Search for and select **Google SecOps API**.
  6. Click **Save**.
  7. **Copy** and **save** the API key.



### Construct the endpoint URL

  * Append the API key to the feed endpoint URL in the following format:
        
        <FEED_ENDPOINT_URL>?key=<API_KEY>
        




Replace the following:

  * `<FEED_ENDPOINT_URL>`: The feed endpoint URL
  * `<API_KEY>`: The API key

  * Example:
        
        https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=AIzaSyD...
        




Save this full URL for the next step.

### Create IAM policy for Firehose

  1. In the **AWS Console** , go to **IAM > Policies > Create policy > JSON tab**.
  2. Paste the following policy JSON:
         
         {
             "Version": "2012-10-17",
             "Statement": [
                 {
                     "Effect": "Allow",
                     "Action": [
                         "firehose:PutRecord",
                         "firehose:PutRecordBatch"
                     ],
                     "Resource": "arn:aws:firehose:<REGION>:<ACCOUNT_ID>:deliverystream/<DELIVERY_STREAM_NAME>"
                 }
             ]
         }
         

  3. Replace the following:

     * `<REGION>`: Your AWS Region (for example, `us-east-1`)
     * `<ACCOUNT_ID>`: Your AWS account ID (12-digit number)
     * `<DELIVERY_STREAM_NAME>`: Your Firehose delivery stream name (you will create this in the next step)
  4. Name the policy `TGWFlowLogsToFirehosePolicy` (for example) and click **Create policy**.




### Create IAM role for CloudWatch Logs

  1. Go to **IAM > Roles > Create role**.
  2. Select **Custom trust policy** and paste:
         
         {
             "Version": "2012-10-17",
             "Statement": [
                 {
                     "Effect": "Allow",
                     "Principal": {
                         "Service": "logs.<REGION>.amazonaws.com"
                     },
                     "Action": "sts:AssumeRole"
                 }
             ]
         }
         

  3. Replace `<REGION>` with your AWS Region.

  4. Click **Next**.

  5. Search for and select the policy `TGWFlowLogsToFirehosePolicy`.

  6. Click **Next**.

  7. Name the role `TGWFlowLogsToFirehoseRole` (for example) and click **Create role**.




### Create Kinesis Data Firehose delivery stream

  1. In the **AWS Console** , go to **Kinesis > Data Firehose > Create delivery stream**.
  2. Provide the following configuration details:

     * **Source and destination:**

       * **Source** : Select **Direct PUT or other sources**
       * **Destination** : Select **HTTP endpoint**
     * **Delivery stream name:**

       * **Delivery stream name** : Enter a name (for example, `tgw-flowlogs-to-secops`)
     * **HTTP endpoint destination:**

       * **HTTP endpoint URL** : Enter the full endpoint URL you constructed (feed endpoint + API key)
       * **Content encoding** : Select **GZIP**
     * **Custom HTTP headers:**

       * Click **Add custom HTTP header**
       * **Header name** : Enter `X-Goog-Chronicle-Auth`
       * **Header value** : Enter the secret key you saved from the feed creation step
     * **Backup settings:**

       * **Source record backup in Amazon S3** : Select **Failed data only**
       * **S3 bucket** : Select an existing bucket or create a new one for failed records
     * **Buffer hints:**

       * **Buffer size** : Enter `1` MiB
       * **Buffer interval** : Enter `60` seconds
  3. Click **Create delivery stream**.

  4. Wait for the delivery stream status to change to **Active**.




### Subscribe CloudWatch Log Group to Firehose

  1. In the **AWS Console** , go to **CloudWatch > Logs > Log groups**.
  2. Select the Transit Gateway flow log group (for example, `/aws/tgw/flowlogs`).
  3. Click the **Subscription filters** tab.
  4. Click **Create > Create Amazon Kinesis Data Firehose subscription filter**.
  5. Provide the following configuration details: 
     * **Destination** : Select delivery stream `tgw-flowlogs-to-secops`
     * **Grant permission** : Select role `TGWFlowLogsToFirehoseRole`
     * **Subscription filter name** : Enter a name (for example, `tgw-flowlogs-to-chronicle`)
     * **Log format** : Select **Other**
     * **Subscription filter pattern** : Leave empty to send all events
  6. Click **Start streaming**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`packets_lost_blackhole_label` | `additional.fields` | Merged  
`packets_lost_mtu_exceeded_label` | `additional.fields` | Merged  
`packets_lost_no_route_label` | `additional.fields` | Merged  
`packets_lost_ttl_expired_label` | `additional.fields` | Merged  
`start_time_label` | `additional.fields` | Merged  
`tcp_flags_label` | `additional.fields` | Merged  
`tgw_attachment_id_label` | `additional.fields` | Merged  
`tgw_id_label` | `additional.fields` | Merged  
`tgw_pair_attachment_id_label` | `additional.fields` | Merged  
`type_label` | `additional.fields` | Merged  
`end_time` | `metadata.event_timestamp` | Parsed as `UNIX`  
`event_type` | `metadata.event_type` | Directly mapped  
`account_id` | `metadata.product_log_id` | Directly mapped  
`version` | `metadata.product_version` | Directly mapped  
`flow_direction` | `network.direction` | Mapped: `(?i)ingress` → `INBOUND`, `(?i)egress` → `OUTBOUND`  
`bytes` | `network.sent_bytes` | Directly mapped  
`packets` | `network.sent_packets` | Directly mapped  
`tgw_src_eni` | `principal.asset.asset_id` | Directly mapped  
`srcaddr` | `principal.asset.ip` | Merged  
`srcaddr` | `principal.ip` | Merged  
`region` | `principal.location.country_or_region` | Directly mapped  
`tgw_src_az_id` | `principal.location.country_or_region` | Directly mapped  
`srcport` | `principal.port` | Directly mapped  
`pkt_src_aws_service_label` | `principal.resource.attribute.labels` | Merged  
`tgw_src_az_id_label` | `principal.resource.attribute.labels` | Merged  
`tgw_src_subnet_id` | `principal.resource.name` | Directly mapped  
`tgw_src_vpc_id` | `principal.resource.product_object_id` | Directly mapped  
`resource_type` | `principal.resource.resource_subtype` | Directly mapped  
`tgw_src_vpc_account_id` | `principal.user.userid` | Directly mapped  
`security_result_action` | `security_result.action` | Merged  
`protocol_label` | `security_result.detection_fields` | Merged  
`tgw_dst_eni` | `target.asset.asset_id` | Directly mapped  
`dstaddr` | `target.asset.ip` | Merged  
`dstaddr` | `target.ip` | Merged  
`tgw_dst_az_id` | `target.location.country_or_region` | Directly mapped  
`dstport` | `target.port` | Directly mapped  
`pkt_dst_aws_service_label` | `target.resource.attribute.labels` | Merged  
`tgw_dst_subnet_id` | `target.resource.name` | Directly mapped  
`tgw_dst_vpc_id` | `target.resource.product_object_id` | Directly mapped  
`tgw_dst_vpc_account_id` | `target.user.userid` | Directly mapped  
N/A | `metadata.product_name` | Constant: `AWS VPC Transit Gateway`  
N/A | `metadata.vendor_name` | Constant: `AWS`  
N/A | `network.direction` | Constant: `INBOUND`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-vpc-transit-gateway-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
