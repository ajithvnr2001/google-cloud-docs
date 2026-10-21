---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-datastream-2/
title: Collect Akamai DataStream 2 logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:18:52.913089+00:00
---

# Collect Akamai DataStream 2 logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-datastream-2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Akamai DataStream 2 logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Akamai DataStream 2 logs to Google Security Operations using Amazon S3.

Akamai DataStream 2 captures performance and security logs from the Akamai Intelligent Edge Platform and delivers them in near real-time to a destination of your choice. You can use DataStream 2 to monitor, debug, and analyze CDN and security events across your Akamai properties.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * Privileged access to **Akamai Control Center** with DataStream 2 configuration permissions.
  * Privileged access to **AWS** (S3, IAM).



## Configure AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
  2. Save bucket **Name** and **Region** for future reference (for example, `akamai-datastream2-logs`).
  3. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**.
  5. Select **Security credentials** tab.
  6. Click **Create Access Key** in section **Access Keys**.
  7. Select **Third-party service** as **Use case**.
  8. Click **Next**.
  9. Optional: Add description tag.
  10. Click **Create access key**.
  11. Click **Download .csv file** to save the **Access Key** and **Secret Access Key** for future reference.
  12. Click **Done**.
  13. Select **Permissions** tab.
  14. Click **Add permissions** in section **Permissions policies**.
  15. Select **Add permissions**.
  16. Select **Attach policies directly**.
  17. Search for **AmazonS3FullAccess** policy.
  18. Select the policy.
  19. Click **Next**.
  20. Click **Add permissions**.



## Configure the IAM policy for Akamai S3 uploads

  1. In the AWS console, go to **IAM > Policies > Create policy > JSON tab**.
  2. Copy and paste the policy below.
  3. **Policy JSON** (replace `akamai-datastream2-logs` if you used a different bucket name):
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Sid": "AllowAkamaiDataStreamWrite",
               "Effect": "Allow",
               "Action": [
                 "s3:PutObject",
                 "s3:GetObject",
                 "s3:ListBucket"
               ],
               "Resource": [
                 "arn:aws:s3:::akamai-datastream2-logs",
                 "arn:aws:s3:::akamai-datastream2-logs/*"
               ]
             }
           ]
         }
         

**Note:** Akamai DataStream 2 requires `s3:PutObject`, `s3:GetObject`, and `s3:ListBucket` permissions to deliver logs and validate the destination.
  4. Click **Next**.

  5. Enter a policy name (for example, `AkamaiDataStreamS3Policy`).

  6. Click **Create policy**.

  7. Go to **IAM > Users > Create user**.

  8. Enter a user name (for example, `akamai-datastream-writer`).

  9. Click **Next**.

  10. Select **Attach policies directly**.

  11. Search for and select the policy created above.

  12. Click **Next > Create user**.

  13. Select the created user, go to **Security credentials > Create access key**.

  14. Select **Third-party service** as **Use case** and click **Next > Create access key**.

  15. Click **Download .csv file** to save the **Access Key ID** and **Secret Access Key** for Akamai DataStream 2 configuration.




## Configure Akamai DataStream 2 to deliver logs to Amazon S3

  1. Sign in to **Akamai Control Center**.
  2. Go to **DataStream 2**.
  3. Click **Create a stream**.
  4. Select a **log type** appropriate for your property (for example, **Delivery** , **Edge DNS** , **GTM**).
  5. In **Data sets** , select the fields you require. Keep defaults unless you have a specific need.
  6. Go to **Destination** and select **Amazon S3**.
  7. Fill in the S3 destination details: 
     * **Name** : Enter a descriptive label for the destination (for example, `SIEM S3 Destination`).
     * **Bucket** : Enter your S3 bucket name (for example, `akamai-datastream2-logs`).
     * **Folder path** : Enter a folder path (for example, `datastream2/logs/`). Supports dynamic variables such as timestamps.
     * **Region** : Select the AWS region that matches your S3 bucket.
     * **Access Key ID** : Enter the access key ID of the IAM user created for Akamai.
     * **Secret Access Key** : Enter the secret access key of the IAM user created for Akamai.
  8. Click **Validate & Save**.

**Note:** Akamai creates a verification file (`Akamai_access_verification_[TimeStamp].txt`) in your S3 bucket to confirm the destination is reachable. If validation fails, verify the IAM permissions and bucket name.
  9. Optional: In **Delivery options** , configure the following:

     * **Push frequency** : Select **30 seconds** or **60 seconds**.
     * **Filename prefix** and **suffix** : Customize as needed. Avoid using `.` in prefixes.
  10. Click **Next > Activate**.




## (Optional) Create read-only IAM user for Google SecOps

If you prefer a separate read-only user for Google SecOps to ingest logs:

  1. Go to **AWS Console > IAM > Policies > Create policy > JSON tab**.
  2. Copy and paste the policy below (replace `akamai-datastream2-logs` if you used a different bucket name):
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Action": [
                 "s3:GetObject"
               ],
               "Resource": "arn:aws:s3:::akamai-datastream2-logs/*"
             },
             {
               "Effect": "Allow",
               "Action": [
                 "s3:ListBucket"
               ],
               "Resource": "arn:aws:s3:::akamai-datastream2-logs"
             }
           ]
         }
         

  3. Click **Next**.

  4. Enter a policy name (for example, `secops-reader-policy`).

  5. Click **Create policy**.

  6. Go to **IAM > Users > Create user**.

  7. Enter a user name (for example, `secops-reader`).

  8. Click **Next**.

  9. Select **Attach policies directly** and select the policy created above.

  10. Click **Next > Create user**.

  11. Select the created user, go to **Security credentials > Create access key**.

  12. Select **Third-party service** as **Use case** and click **Next > Create access key**.

  13. Click **Download .csv file** to save the **Access Key ID** and **Secret Access Key** for the Google SecOps feed configuration.




## Configure a feed in Google SecOps to ingest Akamai DataStream 2 logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. Enter a unique name for the **Feed name** (for example, `Akamai DataStream 2 Logs`).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Akamai DataStream 2** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Specify values for the following fields:

     * **S3 URI** : `s3://akamai-datastream2-logs/datastream2/logs/`
     * **Source deletion option** : Select the deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
  9. Click **Next** and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`billingRegion_label` | `additional.fields` | Merged  
`bytes_label` | `additional.fields` | Merged  
`cache_status_label` | `additional.fields` | Merged  
`customfield_label` | `additional.fields` | Merged  
`errorCode_label` | `additional.fields` | Merged  
`error_code_label` | `additional.fields` | Merged  
`fileSizeBucket_label` | `additional.fields` | Merged  
`jsonPayload_cookie_label` | `additional.fields` | Merged  
`jsonPayload_cp_label` | `additional.fields` | Merged  
`jsonPayload_overheadbytes_label` | `additional.fields` | Merged  
`objSize_label` | `additional.fields` | Merged  
`objsize_label` | `additional.fields` | Merged  
`overheadBytes_label` | `additional.fields` | Merged  
`rspContentLen_label` | `additional.fields` | Merged  
`rspcontentlen_label` | `additional.fields` | Merged  
`trace_label` | `additional.fields` | Merged  
`transferTimeMSec_label` | `additional.fields` | Merged  
`turnAroundTimeMSec_label` | `additional.fields` | Merged  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_HTTP`, `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`insertId` | `metadata.product_log_id` | Directly mapped  
`proto_type` | `network.application_protocol` | Directly mapped  
`jsonPayload.reqmethod` | `network.http.method` | Directly mapped  
`reqMethod` | `network.http.method` | Directly mapped  
`jsonPayload_referer` | `network.http.referral_url` | Directly mapped  
`jsonPayload.statuscode` | `network.http.response_code` | Directly mapped  
`statusCode` | `network.http.response_code` | Directly mapped  
`UA` | `network.http.user_agent` | Directly mapped  
`jsonPayload.ua` | `network.http.user_agent` | Directly mapped  
`jsonPayload.reqid` | `network.session_id` | Directly mapped  
`reqId` | `network.session_id` | Directly mapped  
`jsonPayload.tlsversion` | `network.tls.version` | Directly mapped  
`tlsVersion` | `network.tls.version` | Directly mapped  
`version` | `network.tls.version_protocol` | Directly mapped  
`cliIP` | `principal.asset.ip` | Merged  
`jsonPayload.cliip` | `principal.asset.ip` | Merged  
`cliIP` | `principal.ip` | Merged  
`jsonPayload.cliip` | `principal.ip` | Merged  
`jsonPayload.city` | `principal.location.city` | Directly mapped  
`jsonPayload.country` | `principal.location.country_or_region` | Directly mapped  
`jsonPayload.totalbytes` | `principal.network.received_bytes` | Renamed/mapped  
`totalBytes` | `principal.network.received_bytes` | Directly mapped  
`logName` | `security_result.category_details` | Merged  
`asn_label` | `security_result.detection_fields` | Merged  
`querystr_label` | `security_result.detection_fields` | Merged  
`securityrules_label` | `security_result.detection_fields` | Merged  
`service_name_label` | `security_result.detection_fields` | Merged  
`jsonPayload.reqhost` | `target.asset.hostname` | Directly mapped  
`jsonPayload.reqpath` | `target.file.full_path` | Directly mapped  
`reqPath` | `target.file.full_path` | Directly mapped  
`jsonPayload.rspcontenttype` | `target.file.mime_type` | Directly mapped  
`rspContentType` | `target.file.mime_type` | Directly mapped  
`jsonPayload.reqhost` | `target.hostname` | Directly mapped  
`jsonPayload.reqport` | `target.port` | Renamed/mapped  
`reqPort` | `target.port` | Renamed/mapped  
`uncompressedsize` | `target.process.file.size` | Directly mapped  
`resource.type` | `target.resource.resource_subtype` | Directly mapped  
N/A | `metadata.event_type` | Constant: `NETWORK_HTTP`  
N/A | `metadata.product_name` | Constant: `Akamai Datastream`  
N/A | `metadata.vendor_name` | Constant: `AkamaiDatastream`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-datastream-2-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
