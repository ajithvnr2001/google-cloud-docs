---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-secure-access/
title: Collect Cisco Secure Access logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:18.902100+00:00
---

# Collect Cisco Secure Access logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-secure-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Secure Access logs

**Parser Version:** 4.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Secure Access logs to Google Security Operations using Amazon S3.

Cisco Secure Access is a cloud-delivered Security Service Edge (SSE) solution that provides zero trust network access, secure web gateway, cloud-delivered firewall, DNS-layer security, and data loss prevention. It unifies multiple security functions to protect users and devices accessing applications from any location.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to **Cisco Secure Access** with the **Full Admin** user role
  * Privileged access to **AWS** (S3, IAM)



## Configure an Amazon S3 bucket for Cisco Secure Access

  1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/).
  2. Go to **Amazon S3 > Buckets**.
  3. Click **Create bucket**.
  4. Enter a unique **Bucket name** (for example, `cisco-secure-access-logs`).

**Note:** Periods in S3 bucket names are not supported by Cisco Secure Access. Don't use periods in the bucket name.
  5. Select the **AWS Region** where the bucket should be created.

  6. Leave the remaining settings as default and click **Create bucket**.

  7. Select the newly created bucket.

  8. Go to **Permissions > Bucket policy**.

  9. Click **Edit** and paste the following JSON policy, replacing `bucketname` with your actual bucket name:
         
         {
             "Version": "2008-10-17",
             "Statement": [
                 {
                     "Sid": "",
                     "Effect": "Allow",
                     "Principal": {
                         "AWS": "arn:aws:iam::568526795995:user/logs"
                     },
                     "Action": "s3:PutObject",
                     "Resource": "arn:aws:s3:::bucketname/*"
                 },
                 {
                     "Sid": "",
                     "Effect": "Deny",
                     "Principal": {
                         "AWS": "arn:aws:iam::568526795995:user/logs"
                     },
                     "Action": "s3:GetObject",
                     "Resource": "arn:aws:s3:::bucketname/*"
                 },
                 {
                     "Sid": "",
                     "Effect": "Allow",
                     "Principal": {
                         "AWS": "arn:aws:iam::568526795995:user/logs"
                     },
                     "Action": "s3:GetBucketLocation",
                     "Resource": "arn:aws:s3:::bucketname"
                 },
                 {
                     "Sid": "",
                     "Effect": "Allow",
                     "Principal": {
                         "AWS": "arn:aws:iam::568526795995:user/logs"
                     },
                     "Action": "s3:ListBucket",
                     "Resource": "arn:aws:s3:::bucketname"
                 }
             ]
         }
         

  10. Click **Save changes**.




## Configure an AWS S3 IAM user for Google SecOps

  1. In the **AWS Management Console** , go to **IAM > Users**.
  2. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  3. Select the created **User**.
  4. Select **Security credentials** tab.
  5. Click **Create Access Key** in section **Access Keys**.
  6. Select **Third-party service** as **Use case**.
  7. Click **Next**. 
     * Optional: Add a description tag.
  8. Click **Create access key**.
  9. Click **Download .csv file** to save the **Access Key** and **Secret Access Key** for future reference.
  10. Click **Done**.
  11. Select **Permissions** tab.
  12. Click **Add permissions** in section **Permissions policies**.
  13. Select **Add permissions**.
  14. Select **Attach policies directly**.
  15. Search for **AmazonS3FullAccess** policy.
  16. Select the policy.
  17. Click **Next**.
  18. Click **Add permissions**.



## Configure Cisco Secure Access to export logs to your S3 bucket

  1. Sign in to the **Cisco Secure Access Dashboard** at <https://dashboard.sse.cisco.com>.
  2. Go to **Admin > Log Management**.
  3. In the **Amazon S3** area, select **Use your company-managed Amazon S3 bucket**.
  4. In the **Amazon S3 Bucket** field, enter the exact name of the S3 bucket you created (for example, `cisco-secure-access-logs`).
  5. Click **Verify**.

**Note:** Cisco Secure Access verifies the bucket, connects to it, and saves a `README_FROM_UMBRELLA.txt` file to the bucket.
  6. Open the `README_FROM_UMBRELLA.txt` file that Cisco Secure Access saved to your S3 bucket.

  7. Copy the token listed in the file.

  8. Paste the token into the **Token Number** field in the Cisco Secure Access dashboard.

  9. Click **Save**.

**Note:** Cisco Secure Access logs are CSV-formatted, gzip-compressed, and uploaded every 10 minutes. Within the first two hours after configuration, you should receive your first log upload. Logs are stored in the S3 bucket using the path format: `<bucket-name>-<region>/<prefix>`.



## Configure a feed in Google SecOps to ingest Cisco Secure Access logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. Enter a unique name for the **Feed name** (for example, `Cisco Secure Access Logs`).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Cisco Secure Access** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Specify values for the following fields:

     * **S3 URI** : `s3://<BUCKET_NAME>/` Replace `<BUCKET_NAME>` with the name of your S3 bucket (for example, `cisco-secure-access-logs`).
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
`_field` | `additional.fields` | Merged  
`column10_label` | `additional.fields` | Merged  
`column11_label` | `additional.fields` | Merged  
`column15` | `additional.fields` | Mapped: `[null]` → `column15_label`  
`column15_label` | `additional.fields` | Merged  
`column16_label` | `additional.fields` | Merged  
`column22_label` | `additional.fields` | Merged  
`column23_label` | `additional.fields` | Merged  
`column24_label` | `additional.fields` | Merged  
`column27_label` | `additional.fields` | Merged  
`column28_label` | `additional.fields` | Merged  
`column29_label` | `additional.fields` | Merged  
`column30` | `additional.fields` | Mapped: `^[0-9]+$` → `column30_label`  
`column30_label` | `additional.fields` | Merged  
`column33_label` | `additional.fields` | Merged  
`column42_label` | `additional.fields` | Merged  
`column43` | `additional.fields` | Mapped: `"true", "false"` → `column43_label`  
`column43_label` | `additional.fields` | Merged  
`column44_label` | `additional.fields` | Merged  
`column45` | `additional.fields` | Mapped: `,` → `column45_label`  
`column45_label` | `additional.fields` | Merged  
`column51_label` | `additional.fields` | Merged  
`column52_label` | `additional.fields` | Merged  
`column53_label` | `additional.fields` | Merged  
`column55_label` | `additional.fields` | Merged  
`column6_label` | `additional.fields` | Merged  
`column9_label` | `additional.fields` | Merged  
`key` | `additional.fields` | Mapped: `"col13_label", "col14_label", "col17_label", "col18_label", "col19_label", "col25_l...  
`auth_event` | `extensions.auth.type` | Mapped: `true` → `AUTHTYPE_UNSPECIFIED`  
`intermediary_entity` | `intermediary` | Merged  
`column1` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`auth_event` | `metadata.event_type` | Mapped: `true` → `USER_LOGIN`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`column26` | `metadata.product_log_id` | Directly mapped  
`column26` | `network.http.method` | Directly mapped  
`column10` | `network.http.user_agent` | Directly mapped  
`column34` | `network.ip_protocol` | Directly mapped  
`column15` | `network.received_bytes` | Mapped: `^-?[0-9]+$` → `uinteger`  
`p_bytes` | `network.received_bytes` | Directly mapped  
`p_bytes` | `network.sent_bytes` | Directly mapped  
`column20` | `network.session_id` | Directly mapped  
`column12` | `principal.application` | Directly mapped  
`column2` | `principal.asset.hostname` | Directly mapped  
`column3` | `principal.asset.hostname` | Directly mapped  
`column7` | `principal.asset.hostname` | Directly mapped  
`p_hostname` | `principal.asset.hostname` | Directly mapped  
`column15` | `principal.asset.ip` | Merged  
`column4` | `principal.asset.ip` | Mapped: `DISCONNECTED` → `column15`  
`p_ip` | `principal.asset.ip` | Merged  
`p_ip_from_host` | `principal.asset.ip` | Merged  
`user_ip` | `principal.asset.ip` | Merged  
`column31` | `principal.asset.product_object_id` | Directly mapped  
`software_obj` | `principal.asset.software` | Merged  
`column2` | `principal.hostname` | Directly mapped  
`column3` | `principal.hostname` | Directly mapped  
`column7` | `principal.hostname` | Directly mapped  
`p_hostname` | `principal.hostname` | Directly mapped  
`column15` | `principal.ip` | Merged  
`column4` | `principal.ip` | Mapped: `DISCONNECTED` → `column15`  
`p_ip` | `principal.ip` | Merged  
`p_ip_from_host` | `principal.ip` | Merged  
`user_ip` | `principal.ip` | Merged  
`column7` | `principal.platform_version` | Directly mapped  
`column41` | `principal.process.file.full_path` | Directly mapped  
`column40` | `principal.process.pid` | Directly mapped  
`column2` | `principal.user.email_addresses` | Mapped: `^.+@.+$` → `column2`  
`email` | `principal.user.email_addresses` | Mapped: `^.+@.+$` → `email`  
`column4` | `principal.user.group_identifiers` | Merged  
`column3` | `principal.user.user_display_name` | Directly mapped  
`user_display_name` | `principal.user.user_display_name` | Directly mapped  
`column43` | `principal.user.userid` | Directly mapped  
`column7` | `principal.user.userid` | Directly mapped  
`column45` | `principal.user.windows_sid` | Directly mapped  
`sid` | `principal.user.windows_sid` | Directly mapped  
`security_result_entry` | `security_result` | Merged  
`security_result_present` | `security_result` | Mapped: `true` → `security_result_entry`  
`column21` | `target.asset.hostname` | Directly mapped  
`column5` | `target.asset.hostname` | Directly mapped  
`column16` | `target.asset.ip` | Merged  
`column4` | `target.asset.ip` | Mapped: `DISCONNECTED` → `column16`  
`column5` | `target.asset.ip` | Merged  
`t_ip` | `target.asset.ip` | Merged  
`column21` | `target.hostname` | Directly mapped  
`column5` | `target.hostname` | Directly mapped  
`column16` | `target.ip` | Merged  
`column4` | `target.ip` | Mapped: `DISCONNECTED` → `column16`  
`column5` | `target.ip` | Merged  
`t_ip` | `target.ip` | Merged  
`column33` | `target.port` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `USER_LOGIN`  
N/A | `metadata.product_name` | Constant: `Secure Access`  
N/A | `metadata.vendor_name` | Constant: `Cisco`  
N/A | `network.application_protocol` | Constant: `DNS`  
`column22` | `event.idm.read_only_udm.principal.user.group_identifiers` | Mapped from changelog  
`column11` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`column16` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`column44` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`column44` | `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`column25` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`column8` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`column45` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column22` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column55` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column33` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column2` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`column3` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`column7` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`column4` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column10` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column15` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column5` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column16` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column22` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column7` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`column43` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`column1` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`column6` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column8` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column9` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column10` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column11` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column13` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column14` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column16` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column17` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column18` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column19` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column23` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column24` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column25` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column27` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column28` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column29` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column32` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column36` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column42` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column44` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column46` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column47` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column48` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column49` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column50` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column51` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column52` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column53` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column54` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column12` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`column15` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`column2` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`column20` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`column5` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`column21` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`column33` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`column34` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`column26` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`column3` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`column30` | `event.idm.read_only_udm.principal.asset.software` | Mapped from changelog  
`column31` | `event.idm.read_only_udm.principal.asset.product_object_id` | Mapped from changelog  
`column35` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`column4` | `event.idm.read_only_udm.principal.user.group_identifiers` | Mapped from changelog  
`column40` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`column41` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`column57` | `event.idm.read_only_udm.intermediary` | Mapped from changelog  
`column7` | `event.idm.read_only_udm.principal.platform_version` | Mapped from changelog  
`column56` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`column6` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`column45` | `event.idm.read_only_udm.principal.user.windows_sid` | Mapped from changelog  
`column12` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-secure-access-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
