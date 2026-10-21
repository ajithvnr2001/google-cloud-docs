---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-inspector/
title: Collect AWS Inspector logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:31.610821+00:00
---

# Collect AWS Inspector logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-inspector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS Inspector logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest AWS Inspector logs to Google Security Operations using Amazon S3.

Amazon Inspector is a vulnerability management service that automatically discovers workloads and continually scans them for software vulnerabilities and unintended network exposure. It scans Amazon EC2 instances, container images in Amazon ECR, and AWS Lambda functions, producing detailed findings with severity scores and remediation recommendations. This integration uses Amazon Inspector's built-in findings export feature to deliver JSON-formatted findings reports to an S3 bucket, which Google SecOps then ingests using an Amazon S3 V2 feed.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the **AWS Management Console** with permissions to manage: 
    * **Amazon Inspector** (findings, reports)
    * **Amazon S3** (buckets, bucket policies)
    * **AWS KMS** (key policies)
    * **AWS IAM** (roles, policies, users)



## Configure an S3 bucket for Amazon Inspector findings exports

Amazon Inspector encrypts findings reports with an AWS KMS key before storing them in an S3 bucket. You must configure both the S3 bucket policy and the KMS key policy to allow Amazon Inspector access.

### Create and configure the S3 bucket

  1. Create an **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
  2. Save the bucket **Name** and **Region** for future reference (for example, `inspector-findings-to-secops`).

**Note:** The S3 bucket must be in the same AWS Region where Amazon Inspector is activated.
  3. Select the created bucket in the **Amazon S3 console** at <https://console.aws.amazon.com/s3>.

  4. Select the **Permissions** tab.

  5. In the **Bucket policy** section, click **Edit**.

  6. Add the following statement to the bucket policy (replace `inspector-findings-to-secops` with your bucket name, `111122223333` with your AWS account ID, and `us-east-1` with your AWS Region):
         
         {
             "Version": "2012-10-17",
             "Statement": [
                 {
                     "Sid": "allow-inspector",
                     "Effect": "Allow",
                     "Principal": {
                         "Service": "inspector2.amazonaws.com"
                     },
                     "Action": [
                         "s3:PutObject",
                         "s3:PutObjectAcl",
                         "s3:AbortMultipartUpload"
                     ],
                     "Resource": "arn:aws:s3:::inspector-findings-to-secops/*",
                     "Condition": {
                         "StringEquals": {
                             "aws:SourceAccount": "111122223333"
                         },
                         "ArnLike": {
                             "aws:SourceArn": "arn:aws:inspector2:us-east-1:111122223333:report/*"
                         }
                     }
                 }
             ]
         }
         

  7. Click **Save changes**.




### Configure an AWS KMS key

Amazon Inspector requires a customer managed, symmetric encryption AWS KMS key in the same Region as the S3 bucket to encrypt findings reports.

  1. Open the **AWS KMS console** at <https://console.aws.amazon.com/kms>.
  2. In the navigation pane, select **Customer managed keys**.
  3. Select the KMS key you want to use (or create a new symmetric encryption key).
  4. Select the **Key policy** tab and click **Edit**.
  5. Add the following statement to the key policy (replace `111122223333` with your AWS account ID and `us-east-1` with your AWS Region):
         
         {
             "Sid": "Allow Amazon Inspector to use the key",
             "Effect": "Allow",
             "Principal": {
                 "Service": "inspector2.amazonaws.com"
             },
             "Action": [
                 "kms:Decrypt",
                 "kms:GenerateDataKey*"
             ],
             "Resource": "*",
             "Condition": {
                 "StringEquals": {
                     "aws:SourceAccount": "111122223333"
                 },
                 "ArnLike": {
                     "aws:SourceArn": "arn:aws:inspector2:us-east-1:111122223333:report/*"
                 }
             }
         }
         

  6. Click **Save changes**.




## Export Amazon Inspector findings to S3

  1. Sign in to the **Amazon Inspector console** at <https://console.aws.amazon.com/inspector/v2/home>.
  2. In the navigation pane, go to **Findings > All findings**.
  3. Optional: Use the filter bar above the **Findings** table to specify which findings to include in the report.

**Note:** If you don't add filter criteria, the report will include all active findings in the current AWS Region. For organizations, this includes findings for all member accounts.
  4. Click **Export findings**.

  5. In the **Export settings** section, for **Export file type** , select **JSON**.

**Note:** The JSON format includes all fields for each finding, matching the [Finding](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Finding.html) data type in the Amazon Inspector API reference.
  6. Under **Export location** , for **S3 URI** , click **Browse S3** and select the S3 bucket `inspector-findings-to-secops`.

**Note:** You can optionally append a path prefix (for example, `/findings`) to organize reports in the bucket.
  7. For **KMS key** , select the AWS KMS key you configured.

  8. Click **Export**.

**Note:** You can export only one findings report at a time. Depending on the number of findings, the export can take several minutes to hours.



### Automate the findings export using AWS CLI

To export findings reports on a recurring basis, use the AWS CLI `create-findings-report` command. You can schedule this command using Amazon EventBridge Scheduler or a cron job.

  * Example command:
        
        aws inspector2 create-findings-report \
            --report-format JSON \
            --s3-destination bucketName=inspector-findings-to-secops,keyPrefix=findings/,kmsKeyArn=arn:aws:kms:us-east-1:111122223333:key/your-kms-key-id
        




For more information, see the [create-findings-report](https://docs.aws.amazon.com/cli/latest/reference/inspector2/create-findings-report.html) AWS CLI reference.

## Configure an IAM user for Google SecOps

Google SecOps needs an IAM user with read access to the S3 bucket to ingest the exported findings.

  1. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  2. Select the created **User**.
  3. Select **Security credentials** tab.
  4. Click **Create Access Key** in section **Access Keys**.
  5. Select **Third-party service** as **Use case**.
  6. Click **Next**. 
     * Optional: Add description tag.
  7. Click **Create access key**.
  8. Click **Download .csv file** to save the **Access Key** and **Secret Access Key** for future reference.
  9. Click **Done**.
  10. Select **Permissions** tab.
  11. Click **Add permissions** in section **Permissions policies**.
  12. Select **Add permissions**.
  13. Select **Attach policies directly**.
  14. Search for **AmazonS3FullAccess** policy.
  15. Select the policy.
  16. Click **Next**.
  17. Click **Add permissions**.



## Configure a feed in Google SecOps to ingest AWS Inspector logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. Enter a unique name for the **Feed name**.
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **AWS Inspector** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Specify values for the following fields:

     * **S3 URI** : `s3://inspector-findings-to-secops/findings/`
     * **Source deletion option** : Select the deletion option according to your preference
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Access Key ID** : User access key with access to the S3 bucket
     * **Secret Access Key** : User secret key with access to the S3 bucket
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
  9. Click **Next** and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`duration_ms_label` | `additional.fields` | Merged  
`evnt_app_class_label` | `additional.fields` | Merged  
`evnt_cloud_application_class_label` | `additional.fields` | Merged  
`evnt_cloud_sandbox_md5_label` | `additional.fields` | Merged  
`evnt_cloudapp_rule_label` | `additional.fields` | Merged  
`evnt_content_type_label` | `additional.fields` | Merged  
`evnt_customer_label` | `additional.fields` | Merged  
`evnt_department_label` | `additional.fields` | Merged  
`evnt_location_label` | `additional.fields` | Merged  
`evnt_lpclagg_label` | `additional.fields` | Merged  
`evnt_lpcltype_label` | `additional.fields` | Merged  
`evnt_network_service_label` | `additional.fields` | Merged  
`evnt_tenant_label` | `additional.fields` | Merged  
`evnt_url_category_label` | `additional.fields` | Merged  
`exception_label` | `additional.fields` | Merged  
`function_label` | `additional.fields` | Merged  
`id_label` | `additional.fields` | Merged  
`level_no_label` | `additional.fields` | Merged  
`line_label` | `additional.fields` | Merged  
`location_label` | `additional.fields` | Merged  
`logger_field` | `additional.fields` | Merged  
`msg_location_label` | `additional.fields` | Merged  
`msg_record_functionName_label` | `additional.fields` | Merged  
`msg_record_functionVersion_label` | `additional.fields` | Merged  
`msg_record_initializationType_label` | `additional.fields` | Merged  
`msg_record_instancId_label` | `additional.fields` | Merged  
`msg_record_instanceMaxMemory_label` | `additional.fields` | Merged  
`msg_record_phase_label` | `additional.fields` | Merged  
`msg_service_label` | `additional.fields` | Merged  
`msg_type_label` | `additional.fields` | Merged  
`msg_xray_trace_id_label` | `additional.fields` | Merged  
`protocol_label` | `additional.fields` | Merged  
`record_version_label` | `additional.fields` | Merged  
`repr_label` | `additional.fields` | Merged  
`service_label` | `additional.fields` | Merged  
`sourcetype_label` | `additional.fields` | Merged  
`thread_name_label` | `additional.fields` | Merged  
`type_label` | `additional.fields` | Merged  
`xray_trace_id_label` | `additional.fields` | Merged  
`evnt_device_hostname` | `intermediary.hostname` | Directly mapped  
`evnt_fwd_method_label` | `intermediary.resource.attribute.labels` | Merged  
`desc_msg` | `metadata.description` | Directly mapped  
`message` | `metadata.description` | Directly mapped  
`msg` | `metadata.description` | Directly mapped  
`msg_desc_msg` | `metadata.description` | Directly mapped  
`msg_record_desc_msg` | `metadata.description` | Directly mapped  
`msg_text` | `metadata.description` | Directly mapped  
`msg.time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`repr_time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`has_host` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_COMMUNICATION`, `true` → `USER_UNCATEGORIZED`  
`msg_record_module` | `metadata.product_event_type` | Directly mapped  
`id_1` | `metadata.product_log_id` | Directly mapped  
`evnt_bytes_in` | `network.received_bytes` | Directly mapped  
`evnt_bytes_out` | `network.sent_bytes` | Directly mapped  
`evnt_app_name` | `principal.application` | Directly mapped  
`msg_record_process_name` | `principal.application` | Directly mapped  
`evnt_device_app_version_label` | `principal.asset.attribute.labels` | Merged  
`evnt_ssl_policy_label` | `principal.asset.attribute.labels` | Merged  
`evnt_server_ip` | `principal.asset.ip` | Merged  
`evnt_src_ip` | `principal.asset.ip` | Merged  
`evnt_src_translated_ip` | `principal.asset.ip` | Merged  
`msg_record_file_path` | `principal.file.full_path` | Directly mapped  
`msg_record_file_name` | `principal.file.names` | Merged  
`evnt_hostname` | `principal.hostname` | Directly mapped  
`host` | `principal.hostname` | Directly mapped  
`evnt_server_ip` | `principal.ip` | Merged  
`evnt_src_ip` | `principal.ip` | Merged  
`evnt_src_translated_ip` | `principal.ip` | Merged  
`evnt_os` | `principal.platform` | Mapped: `Windows` → `WINDOWS`, `Linux` → `LINUX`  
`evnt_src_port` | `principal.port` | Directly mapped  
`port_number` | `principal.port` | Directly mapped  
`msg_record_process_id` | `principal.process.pid` | Directly mapped  
`cmd_status_label` | `principal.resource.attribute.labels` | Merged  
`evnt_format_label` | `principal.resource.attribute.labels` | Merged  
`evnt_os_label` | `principal.resource.attribute.labels` | Merged  
`msg_record_runtimeVersionArn_label` | `principal.resource.attribute.labels` | Merged  
`msg_record_runtimeVersion_label` | `principal.resource.attribute.labels` | Merged  
`record_requestId_labels` | `principal.resource.attribute.labels` | Merged  
`requestId_labels` | `principal.resource.attribute.labels` | Merged  
`msg_record_name` | `principal.resource.name` | Directly mapped  
`id` | `principal.resource.product_object_id` | Directly mapped  
`evnt_url` | `principal.url` | Directly mapped  
`evnt_device_owner` | `principal.user.user_display_name` | Directly mapped  
`evnt_user` | `principal.user.userid` | Directly mapped  
`msg_extra_desc_msg_body_account_id` | `principal.user.userid` | Directly mapped  
`evnt_action` | `security_result.action` | Mapped: `allow` → `security_result_action`  
`security_result_action` | `security_result.action` | Merged  
`security_result_category_details` | `security_result.category_details` | Merged  
`security_result_url_super_category` | `security_result.category_details` | Merged  
`elapsed_time_label` | `security_result.detection_fields` | Merged  
`evnt_session_count_label` | `security_result.detection_fields` | Merged  
`evnt_ssl_decrypted_label` | `security_result.detection_fields` | Merged  
`evnt_url_class_label` | `security_result.detection_fields` | Merged  
`level_icon_label` | `security_result.detection_fields` | Merged  
`level` | `security_result.severity` | Mapped: `INFO` → `INFORMATIONAL`, `WARNING` → `MEDIUM`  
`msg_level` | `security_result.severity` | Mapped: `INFO` → `INFORMATIONAL`, `WARNING` → `MEDIUM`  
`evnt_dest_ip` | `target.ip` | Merged  
`evnt_dest_country` | `target.location.country_or_region` | Directly mapped  
`evnt_dest_port` | `target.port` | Directly mapped  
`dst_url` | `target.url` | Directly mapped  
N/A | `metadata.event_type` | Constant: `USER_COMMUNICATION`  
N/A | `metadata.product_name` | Constant: `AWS Inspector`  
N/A | `metadata.vendor_name` | Constant: `AWS Inspector`  
N/A | `network.ip_protocol` | Constant: `UDP`  
N/A | `principal.platform` | Constant: `WINDOWS`  
N/A | `security_result.detection_fields` | Constant: `client_tunnel_ip_label`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-inspector-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
