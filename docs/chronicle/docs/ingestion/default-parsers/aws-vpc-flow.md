---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-vpc-flow/
title: Collect AWS VPC Flow Logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:15.553955+00:00
---

# Collect AWS VPC Flow Logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-vpc-flow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS VPC Flow Logs

**Parser Version:** 17.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest AWS VPC Flow Logs to Google Security Operations using three different methods: Amazon S3 (Text format), Amazon CloudWatch Logs with Kinesis Data Firehose, and CSV format in Amazon S3. AWS VPC Flow Logs is a feature that lets you capture information about the IP traffic going to and from network interfaces in your VPC. This integration lets you send these logs to Google SecOps for analysis and monitoring.

## Supported AWS VPC Flow Log formats

Google SecOps supports the ingestion of AWS VPC Flow Logs in two primary text formats:

  * **JSON Format** : The `AWS_VPC_FLOW` log type parses logs in JSON format. In this format, each log entry includes both a key and its corresponding value, making the data self-describing.
  * **CSV Format** : Google SecOps also provides a parser for AWS VPC Flow Logs in CSV format. This format lists field keys only once in the header row, with subsequent rows containing only comma-separated values.



Because the CSV format doesn't include field keys in each log entry, the AWS_VPC_FLOW_CSV parser relies on a strict, predefined order of values. Your CSV files must adhere to the following field order for correct parsing:
    
    
       Version,Account_id,Interface_id,Srcaddr,Dstaddr,Srcport,Dstport,Protocol,Packets,Bytes,Start,End,Action,Log_status,Vpc_id,Subnet_id,Instance_id,Tcp_flags,Type,Pkt_srcaddr,Pkt_dstaddr,Region,Az_id,Sublocation_type,Sublocation_id,Pkt_src_aws_service,Pkt_dst_aws_service,Flow_direction,Traffic_path,Ecs_cluster_arn,Ecs_cluster_name,Ecs_container_instance_arn,Ecs_container_instance_id,Ecs_container_id,Ecs_second_container_id,Ecs_service_name,Ecs_task_definition_arn,Ecs_task_arn,Ecs_task_id
    

The following is an example of a CSV log line:
    
    
       7,369096419186,eni-0520bb5efed19d33a,10.119.32.34,10.119.223.3,51256,16020,6,14,3881,1723542839,1723542871,ACCEPT,OK,vpc-0769a6844ce873a6a,subnet-0cf9b2cb32f49f258,i-088d6080f45f5744f,0,IPv4,10.119.32.34,10.119.223.3,ap-northeast-1,apne1-az4,-,-,-,-,ingress,,-,-,-,-,-,-,-,-,-,-
    

For fields where no value is available, an empty value (for example, , ,) should be passed to maintain the correct positional order within the CSV row.

**Note:** If the field order is not maintained, the data may be parsed incorrectly.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance.
  * Privileged access to AWS.



## Option 1: Configure AWS VPC Flow Logs export using AWS S3 (Text format)

The following section outlines how to configure Amazon S3 and Identity and Access Management permissions to enable the export of VPC Flow Logs for analysis by Google SecOps.

### Configure AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket-overview.html).
  2. Save bucket **Name** and **Region** for future reference (for example, `aws-vpc-flowlogs`).
  3. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**.
  5. Select the **Security credentials** tab.
  6. Click **Create Access Key** in section **Access Keys**.
  7. Select **Third-party service** as **Use case**.
  8. Click **Next**.
  9. Optional: Add a description tag.
  10. Click **Create access key**.
  11. Click **Download CSV file** to save the **Access Key** and **Secret Access Key** for future reference.
  12. Click **Done**.
  13. Select the **Permissions** tab.
  14. Click **Add permissions** in section **Permissions policies**.
  15. Select **Add permissions**.
  16. Select **Attach policies directly**.
  17. Search for **AmazonS3FullAccess** policy.
  18. Select the policy.
  19. Click **Next**.
  20. Click **Add permissions**.



### Create VPC Flow Logs (destination: Amazon S3, Text format)

  1. Open **AWS Console > VPC > Your VPCs/Subnets/Network interfaces** and select the scope you want to log.
  2. Click **Actions > Create flow log**.
  3. Provide the following configuration details: 
     * **Filter** : Choose **All** (or **Accept** / **Reject**) per your policy.
     * **Maximum aggregation interval** : Select **1 minute** (recommended) or **10 minutes**.
     * **Destination** : **Send to an Amazon S3 bucket**.
     * **S3 bucket ARN** : Enter the bucket name created in the previous section in the following format: `arn:aws:s3:::<your-bucket>`.
     * **Log record format** : Select **AWS default format**.
     * **Log file format** : Select **Text (Plain)**.
     * Optional: Disable **Hive-compatible prefixes** and **Hourly partitions** unless you need them.
  4. Click **Create flow log**.

**Note:** Resulting S3 key prefix: `s3://<bucket>/AWSLogs/<account-id>/vpcflowlogs/<region>/<year>/<month>/<day>/` (gzip `.log.gz` files at ~5-minute cadence).

### Configure a feed in Google SecOps to ingest AWS VPC Flow Logs (S3 Text)

  1. Go to **SIEM Settings > Feeds**.
  2. Click **\+ Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `AWS VPC Flow Logs - S3 (Text)`).
  4. Select **Amazon S3 V2** as the **Source type**.
  5. Select **AWS VPC Flow** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters: 
     * **S3 URI** : Enter the S3 bucket address (for example, `s3://<your-bucket>/AWSLogs/<account-id>/vpcflowlogs/<region>/`).
     * **Source deletion options** : Select deletion option according to your preference.
     * **Maximum File Age** : Default 180 Days.
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label applied to the events from this feed.
  8. Click **Next**.
  9. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



## Option 2: Configure AWS VPC Flow Logs export using Amazon CloudWatch Logs and Kinesis Data Firehose

After setting up the flow logs to go to CloudWatch, this option provides an additional layer of data export by streaming that log data to a destination of your choice using Kinesis Data Firehose.

### Create VPC Flow Logs (destination: Amazon CloudWatch Logs)

  1. Open **AWS Console > VPC > Your VPCs/Subnets/Network interfaces**.
  2. Click **Actions > Create flow log**.
  3. Provide the following configuration details: 
     * **Filter** : Choose **All** (or **Accept** /**Reject**) per your policy.
     * **Maximum aggregation interval** : Select **1 minute** (recommended) or **10 minutes**.
     * **Destination** : Select **Send to CloudWatch Logs**.
     * **Destination log group** : Select or create a log group (for example, `/aws/vpc/flowlogs`).
     * **IAM role** : Select a role that can write to CloudWatch Logs.
     * **Log record format** : Select **AWS default** (version 2) or **Custom** (includes additional fields).
  4. Click **Create flow log**.



### Create a feed in Google SecOps to get Endpoint URL and Secret Key

  1. Go to **SIEM Settings > Feeds**.
  2. Click **\+ Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `AWS VPC Flow Logs - CloudWatch via Firehose`).
  4. Select **Amazon Data Firehose** as the **Source type**.
  5. Select **AWS VPC Flow** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters: 
     * **Split delimiter** : Optional `n`.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces) (for example, `aws.vpc.flowlogs.cwl`).
     * **Ingestion labels** : The label to be applied to the events from this feed (for example, `source=vpc_flow_firehose`).
  8. Click **Next**.
  9. Review the feed configuration and click **Submit**.
  10. Click **Generate Secret Key** to generate a secret key to authenticate this feed.
  11. **Copy** and **save** the secret key as you cannot view this secret again.
  12. Go to the **Details** tab.
  13. **Copy** the feed endpoint URL from the **Endpoint Information** field.
  14. Click **Done**.



### Create an API key for the Amazon Data Firehose feed

  1. Go to the **Google Cloud** console **Credentials** page.
  2. Click **Create** credentials, and then select **API key**.
  3. Copy and save the key in a secure location.
  4. Restrict the API key **access** to the **Google SecOps API**.



### Configure IAM permissions for CloudWatch Logs to Firehose

  1. In the **AWS Console** , go to **IAM > Policies > Create policy > JSON**.
  2. Paste the following policy JSON, replacing `<region>` and `<account-id>` with your AWS Region and account ID:
         
         {
         "Version": "2012-10-17",
         "Statement": [
            {
               "Effect": "Allow",
               "Action": [
               "firehose:PutRecord",
               "firehose:PutRecordBatch"
               ],
               "Resource": "arn:aws:firehose:<region>:<account-id>:deliverystream/cwlogs-to-secops"
            }
         ]
         }
         

  3. Name the policy `CWLtoFirehoseWrite` and click **Create policy**.

  4. Go to **IAM > Roles > Create role**.

  5. Select **Custom trust policy** and paste:
         
         {
         "Version": "2012-10-17",
         "Statement": [
            {
               "Effect": "Allow",
               "Principal": {
               "Service": "logs.<region>.amazonaws.com"
               },
               "Action": "sts:AssumeRole"
            }
         ]
         }
         

  6. Attach the policy `CWLtoFirehoseWrite` to the role.

  7. Name the role `CWLtoFirehoseRole` and click **Create role**.




### Configure Amazon Kinesis Data Firehose to Google SecOps

  1. In the **AWS Console** , go to **Kinesis > Data Firehose > Create delivery stream**.
  2. Provide the following configuration details: 
     * **Source** : Select **Direct PUT or other sources**.
     * **Destination** : Choose **HTTP endpoint**.
     * **Name** : `cwlogs-to-secops`
     * **HTTP endpoint URL** : Enter the **Feed HTTPS endpoint URL** from Google SecOps with the API Key appended: `<ENDPOINT_URL>?key=<API_KEY>`
     * **HTTP method** : Select **POST**.
  3. Under **Access key** : 
     * Enter the **Secret key** generated in Google SecOps feed (this becomes the `X-Amz-Firehose-Access-Key` header).
     * **Buffering hints** : set **Buffer size** = **1 MiB** , **Buffer interval** = **60 seconds**.
     * **Compression** : select **Disabled**.
     * **S3 backup** : select **Disabled**.
     * Leave **retry** and **logging** settings as **default**.
  4. Click **Create delivery stream**.



### Subscribe the CloudWatch Logs group to the Firehose stream

  1. Go to **CloudWatch > Logs > Log groups**.
  2. Select the target log group (for example, `/aws/vpc/flowlogs`).
  3. Open the **Subscription filters** tab and click **Create**.
  4. Choose **Create Amazon Kinesis Data Firehose subscription filter**.
  5. Provide the following configuration details: 
     * **Destination** : Select delivery stream `cwlogs-to-secops`.
     * **Grant permission** : Choose role `CWLtoFirehoseRole`.
     * **Filter name** : Enter `all-events`.
     * **Filter pattern** : Leave empty to send all events.
  6. Click **Start streaming**.



## Option 3: Configure AWS VPC Flow Logs in CSV format using Amazon S3

**Note:** AWS VPC Flow Logs natively publish to S3 as **Text** (space-delimited) or **Parquet**. If you require **CSV** , transform the logs to CSV (for example, with AWS Glue ETL or a Lambda transform) and store them in S1. Then configure a dedicated feed that uses the CSV parser.

### Transform logs to CSV format (optional)

  1. Ensure your CSV rows follow a **strict, consistent column order** that matches the fields you selected in your VPC Flow Log **custom format** (for example, the canonical v2 field set, or your v5/v7 set). Do **not** include a header row in production files unless your parser option expects one.
  2. Write CSV files to a stable prefix, for example: `s3://<your-bucket>/vpcflowlogs-csv/<region>/year=<year>/month=<month>/day=<day>/`.



### Configure a feed in Google SecOps to ingest AWS VPC Flow Logs (CSV)

  1. Go to **SIEM Settings > Feeds**.
  2. Click **\+ Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `AWS VPC Flow Logs - S3 (CSV)`).
  4. Select **Amazon S3 V2** as the **Source type**.
  5. Select **AWS VPC Flow (CSV)** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters: 
     * **S3 URI** : Enter the S3 bucket address (for example, `s3://<your-bucket>/vpcflowlogs-csv/<region>/`).
     * **Source deletion options** : Select deletion option according to your preference.
     * **Maximum File Age** : Default 180 Days.
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label applied to the events from this feed.
  8. Click **Next**.
  9. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



## UDM mapping table

Log sample | Log Field | UDM mapping  
---|---|---  
`"entries: { data: ""7,11111111111,eni-11aa1a1a1a1aa1a,1.1.1.1,2.2.2.2,51256,16020,6,14,3881,1723542839,1723542871,ACCEPT,OK,vpc-1aa1a1a1a1aa1aa,subnet-1aa1a1a1a1aa1a1,i-1aa1a1a1a1aa1a,0,IPv4,1.1.1.1,2.2.2.2,ap-northeast-1,masked_zone,-,-,-,-,ingress,,-,-,-,-,-,-,-,-,-,-"" collection_time: { seconds: 1741159282 nanos: 254633949 } }"` | `7` | `metadata.product_version`  
`11111111111` | `metadata.product_log_id`  
`eni-11aa1a1a1a1aa1a` | `principal.user.product_object_id`  
`1.1.1.1` | `principal.ip`  
`2.2.2.2` | `target.ip`  
`51256` | `principal.port`  
`16020` | `target.port`  
`6` | `network.ip_protocol`  
`14` | `network.sent_packets`  
`3881` | `network.received_bytes`  
`1723542839` | `metadata.event_timestamp about.resource.attribute.labels(start_time)`  
`1723542871` | `metadata.ingested_timestamp about.resource.attribute.labels(end_time)`  
`ACCEPT` | `security_result.action security_result.action_details`  
`OK` | `about.resource.attribute.labels (log-status)`  
`vpc-1aa1a1a1a1aa1a` | `principal.resource.attribute.labels (vpcID)`  
`subnet-a1a1a1a1a1` | `principal.asset_id`  
`i-1aa1a1a1a1aa1a` | `principal.resource_ancestors.product_object_id`  
`0` | `about.resource.attribute.labels (type)`  
`IPv4` | `additional.fields (pkt-srcaddr-ip)`  
`1.1.1.1` | `intermediary.ip`  
`2.2.2.2` | `additional.fields (tcp_flags)`  
`ap-northeast-1` | `not getting mapped`  
`masked_zone` | `not getting mapped`  
`-` | `about.resource.attribute.labels (sublocation_type)`  
`-` | `about.resource.attribute.labels (sublocation_id)`  
`-` | `about.resource.attribute.labels (pkt_src_aws_service)`  
`-` | `about.resource.attribute.labels (pkt_dst_aws_service)`  
`ingress` | `network.direction`  
` ` | `additional.fields (traffic_path)`  
`-` | `not getting mapped`  
`-` | `not getting mapped-`  
`"entries: { data: ""7,11111111111,eni-11aa1a1a1a1aa1a,5.5.5.5,2.2.2.2,53102,16020,6,8,2112,1723542839,1723542871,ACCEPT,OK,vpc-1aa1a1a1a1aa1a,subnet-1aa1a1a1a1aa1a,i-1aa1a1a1a1aa1a,0,IPv4,5.5.5.5,2.2.2.2,ap-northeast-1,masked_zone,-,-,-,-,ingress,,-,-,-,-,-,-,-,-,-,-"" collection_time: { seconds: 1741159390 nanos: 374934225 } }"` | `7` | `metadata.product_version`  
`11111111111` | `metadata.product_log_id`  
`eni-11aa1a1a1a1aa1a` | `principal.user.product_object_id`  
`5.5.5.5` | `principal.ip`  
`2.2.2.2` | `target.ip`  
`53102` | `principal.port`  
`16020` | `target.port`  
`6` | `network.ip_protocol`  
`8` | `network.sent_packets`  
`2112` | `network.received_bytes`  
`1723542839` | `metadata.event_timestamp about.resource.attribute.labels(start_time)`  
`1723542871` | `metadata.ingested_timestamp about.resource.attribute.labels(end_time)`  
`ACCEPT` | `security_result.action security_result.action_details`  
`OK` | `about.resource.attribute.labels (log-status)`  
`vpc-1aa1a1a1a1aa1a` | `principal.resource.attribute.labels (vpcID)`  
`subnet-1aa1a1a1a1aa1a` | `principal.asset_id`  
`i-1aa1a1a1a1aa1a` | `principal.resource_ancestors.product_object_id`  
`0` | `about.resource.attribute.labels (type)`  
`IPv4` | `additional.fields (pkt-srcaddr-ip)`  
`5.5.5.5` | `intermediary.ip`  
`2.2.2.2` | `additional.fields (tcp_flags)`  
`ap-northeast-1` | `not getting mapped`  
`masked_zone` | `not getting mapped`  
`-` | `about.resource.attribute.labels (sublocation_type)`  
`-` | `about.resource.attribute.labels (sublocation_id)`  
`-` | `about.resource.attribute.labels (pkt_src_aws_service)`  
`-` | `about.resource.attribute.labels (pkt_dst_aws_service)`  
`ingress` | `network.direction`  
` ` | `additional.fields (traffic_path)`  
`-` | `not getting mapped`  
`-` | `not getting mapped1`  
`"entries: { data: ""7,11111111111,eni-11aa1a1a1a1aa1a,1.1.2.2,1.1.2.1,36358,42659,6,1091,3.754327e+06,1747981553,1747981582,ACCEPT,OK,vpc-1aa1a1a1a1aa1a,subnet-1aa1a1a1a1aa1a,i-1aa1a1a1a1aa1a,0,IPv4,1.1.2.2,1.1.2.1,ap-northeast-1,apne1-az1,-,-,-,-,egress,1,-,-,-,-,-,-,-,-,-,-,604249"" collection_time: { seconds: 1748238552 nanos: 479960397 } }"` | `7` | `metadata.product_version`  
`11111111111` | `metadata.product_log_id`  
`eni-11aa1a1a1a1aa1a` | `about.resource.attribute.labels`  
`1.1.2.2` | `principal.ip`  
`1.1.2.1` | `target.ip`  
`36358` | `principal.port`  
`42659` | `target.port`  
`6` | `network.ip_protocol`  
`1091` | `network.sent_packets`  
`3.75E+06` | `network.sent_bytes`  
`1747981553` | `metadata.event_timestamp about.resource.attribute.labels(start_time)`  
`1747981582` | `metadata.ingested_timestamp about.resource.attribute.labels(end_time)`  
`ACCEPT` | `security_result.action security_result.action_details`  
`OK` | `about.resource.attribute.labels (log-status)`  
`vpc-1aa1a1a1a1aa1a` | `principal.resource.attribute.labels (vpcID)`  
`subnet-1aa1a1a1a1aa1a` | `principal.asset_id`  
`i-1aa1a1a1a1aa1a` | `principal.resource_ancestors.product_object_id`  
`0` | `additional.fields (tcp_flags)`  
`IPv4` | `about.resource.attribute.labels(type)`  
`1.1.2.2` | `"additional.fields (pkt-srcaddr-ip)`  
**Condition** :  
`if [pkt_dstaddr_ip] != [dstaddr] will map to intermediary.ip"`  
`1.1.2.1` | `"additional.fields (pkt-dstaddr-ip)`  
**Condition** :  
`if [pkt_srcaddr_ip] != [srcaddr] will map to intermediary.ip"`  
`ap-northeast-1` | `principal.location.country_or_region`  
`apne1-az1` | `principal.location.name`  
`-` | `about.resource.attribute.labels (sublocation_type)`  
`-` | `about.resource.attribute.labels (sublocation_id)`  
`-` | `about.resource.attribute.labels (pkt_src_aws_service)`  
`-` | `about.resource.attribute.labels (pkt_dst_aws_service)`  
`egress` | `network.direction`  
`1` | `additional.fields (traffic_path)`  
`-` | `not getting mapped`  
`604249` | `not getting mapped`  
| `Connection_info.Tcp_flags` | `additional.fields`  
| `connection_info.tcp_flags` | `additional.fields`  
| `Dst_endpoint.Interface_uid` | `target.user.product_object_id`  
| `Log_status` | `additional.fields`  
| `Src_endpoint.Instance_uid` | `principal.user.product_object_id`  
| `Tcp_flags` | `additional.fields`  
| `tcp_flags` | `additional.fields`  
| `tgw_dst_az_id` | `target.resource.attribute.cloud.availability_zone`  
| `tgw_id` | `target.resource.product_object_id`  
| `tgw_src_az_id` | `principal.location.name`  
| `Traffic_Bytes` | `network.sent_bytes`  
| `Traffic_Packets` | `network.sent_packets`  
  
## Release delta

Google SecOps released version 16.0 of the AWS VPC Flow Logs parser, which includes significant changes to the mapping of Parser_Name log fields to UDM fields and changes to the mapping of event types.

### Log-field mapping delta

Log field | Old mapping | Current mapping  
---|---|---  
`bytes` | `network.sent_bytes` | `Removed`  
`Connection_info.Tcp_flags` | `network.dhcp.flags` | `additional.fields`  
`connection_info.tcp_flags` | `network.dhcp.flags` | `additional.fields`  
`Dst_endpoint.Interface_uid` | `additional.fields` | `target.user.product_object_id`  
`flow_direction` | `about.resource.attribute.labels` | `Removed`  
`Log_status` | `about.resource.attribute.labels` | `additional.fields`  
`Src_endpoint.Instance_uid` | `additional.fields` | `principal.user.product_object_id`  
`Tcp_flags` | `network.dhcp.flags` | `additional.fields`  
`tcp_flags` | `network.dhcp.flags` | `additional.fields`  
`tgw_dst_az_id` | `target.resource.attribute.labels` | `target.resource.attribute.cloud.availability_zone`  
`tgw_id` | `additional.fields` | `target.resource.product_object_id`  
`tgw_src_az_id` | `principal.resource.attribute.labels` | `principal.location.name`  
`Traffic_Bytes` | `additional.fields` | `network.sent_bytes`  
`Traffic_Packets` | `additional.fields` | `network.sent_packets`  
  
### Event-type mapping delta

Multiple events that were classified generically are now properly classified with meaningful event types.

Event type | Fields from log | Reason  
---|---|---  
FILE_UNCATEGORIZED | `Bytes` | It's newly handled in this PR mapped to an appropriate, specific event type  
NETWORK_CONNECTION | `protocol` | It's newly handled in this PR mapped to an appropriate, specific event type  
NETWORK_UNCATEGORIZED | `Class_name` | It's newly handled in this PR mapped to an appropriate, specific event type  
NETWORK_UNCATEGORIZED | `flow_direction` | It's newly handled in this PR mapped to an appropriate, specific event type  
STATUS_UPDATE | `[src_endpoint][ip]` | It's newly handled in this PR mapped to an appropriate, specific event type  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-vpc-flow-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
