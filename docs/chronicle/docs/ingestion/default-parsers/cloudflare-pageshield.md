---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudflare-pageshield/
title: Collect Cloudflare Page Shield logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:32:42.251117+00:00
---

# Collect Cloudflare Page Shield logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudflare-pageshield/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cloudflare Page Shield logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cloudflare Page Shield logs to Google Security Operations using Amazon S3.

Page Shield helps manage resources loaded by your website visitors, including scripts, their connections, and cookies, and triggers alert notifications when resources change or are considered malicious.

## Before you begin

  * A Google SecOps instance
  * Cloudflare account with Page Shield enabled
  * Privileged access to **Cloudflare** dashboard
  * Privileged access to **AWS** (S3, IAM)



This option uses Cloudflare Logpush to export Page Shield events to Amazon S3, which Google SecOps then ingests.

### Enable Page Shield

  1. Sign in to the **Cloudflare dashboard**.
  2. Select your account and domain.
  3. Go to **Security > Page Shield**.
  4. Click **Enable Page Shield**.



### Create Amazon S3 bucket

  1. Open the **Amazon S3 console**.
  2. Click **Create Bucket**.
  3. Provide the following configuration details: 
     * **Bucket Name** : Enter a meaningful name for the bucket (for example, `cloudflare-pageshield-logs`).
     * **Region** : Select your preferred AWS region (for example, `us-east-1`).
  4. Click **Create**.
  5. Save the bucket name and region for future reference.



### Create IAM user with S3 access

  1. Open the **IAM console**.
  2. Click **Users > Add user**.
  3. Enter a **user name** (for example, `chronicle-s3-user`).
  4. Select **Programmatic access**.
  5. Click **Next: Permissions**.
  6. Choose **Attach existing policies directly**.
  7. Search for and select the **AmazonS3FullAccess** policy.
  8. Click **Next: Tags**.
  9. Click **Next: Review**.
  10. Click **Create user**.
  11. Click **Download .csv file** to save the **Access Key ID** and **Secret Access Key**.



### Configure S3 bucket policy for Cloudflare

  1. In the **Amazon S3 console** , select your bucket.
  2. Click **Permissions > Bucket policy**.
  3. Click **Edit**.
  4. Paste the following policy, replacing `<BUCKET_NAME>` with your bucket name:
         
         {
           "Id": "Policy1506627184792",
           "Version": "2012-10-17",
           "Statement": [
             {
               "Sid": "Stmt1506627150918",
               "Action": ["s3:PutObject"],
               "Effect": "Allow",
               "Resource": "arn:aws:s3:::<BUCKET_NAME>/*",
               "Principal": {
                 "AWS": ["arn:aws:iam::391854517948:user/cloudflare-logpush"]
               }
             }
           ]
         }
         

  5. Click **Save changes**.




### Create Cloudflare Logpush job

  1. Sign in to the **Cloudflare dashboard**.
  2. Select your account and domain.
  3. Go to **Analytics & Logs > Logs**.
  4. Click **Create a Logpush job**.
  5. In **Select a destination** , choose **Amazon S3**.
  6. Enter the following destination information: 
     * **Bucket name** : Enter your S3 bucket name (for example, `cloudflare-pageshield-logs`).
     * **Bucket region** : Select the region matching your S3 bucket.
     * **Bucket path** (optional): Enter a path prefix (for example, `pageshield/`).
  7. Click **Continue**.
  8. To prove ownership, Cloudflare will send a file to your designated destination. To find the token, select the Open button in the Overview tab of the ownership challenge file, then paste it into the Cloudflare dashboard to verify your access to the bucket. Enter the Ownership Token and select Continue.
  9. In **Select a dataset** , choose **Page Shield events**.
  10. Click **Next**.
  11. Configure your logpush job: 
     * **Job name** : Enter a descriptive name (for example, `pageshield-to-s3`).
     * **If logs match** : Leave empty to include all events or configure filters as needed.
     * **Send the following fields** : Select **All fields** or choose specific fields.
  12. Click **Submit**.



### Configure a feed in Google SecOps to ingest Page Shield logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Cloudflare Page Shield S3`).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Cloudflare Page Shield** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **S3 URI** : Enter the bucket URI in format: `s3://<BUCKET_NAME>/<BUCKET_PATH>/`

**Note:** Include the trailing slash (/) at the end of the S3 URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers.
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Access Key ID** : User access key with access to the S3 bucket.

     * **Secret Access Key** : User secret key with access to the S3 bucket.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
URLContainsCDNCGIPath | event.idm.read_only_udm.additional.fields.CGI_label | Value taken from URLContainsCDNCGIPath, set as string_value in label with key "CGI"  
Action | event.idm.read_only_udm.additional.fields.action_label | Value taken from Action, set as string_value in label with key "action"  
resource.first_page_url | event.idm.read_only_udm.additional.fields.first_page_label | Value taken from resource.first_page_url, set as string_value in label with key "first_page_url"  
resource.last_page_url | event.idm.read_only_udm.additional.fields.last_page_label | Value taken from resource.last_page_url, set as string_value in label with key "last_page_url"  
name | event.idm.read_only_udm.additional.fields.name_label | Value taken from name, set as string_value in label with key "name"  
ts | event.idm.read_only_udm.metadata.event_timestamp | Converted from ts (UNIX) to timestamp  
| event.idm.read_only_udm.metadata.event_type | Derived based on has_principal, has_target, has_target_user: NETWORK_CONNECTION if both principal and target; USER_UNCATEGORIZED if target_user; STATUS_UPDATE if principal; else GENERIC_EVENT  
resource.url | event.idm.read_only_udm.network.http.referral_url | Value taken from resource.url  
Host | event.idm.read_only_udm.principal.asset.hostname | Value taken from Host or host.hostname  
Host | event.idm.read_only_udm.principal.hostname | Value taken from Host or host.hostname  
alert_type | event.idm.read_only_udm.principal.resource.attribute.labels.alert_type_label | Value taken from alert_type, set as value in label with key "alert_type"  
resource.cryptomining_score | event.idm.read_only_udm.principal.resource.attribute.labels.crypto_label | Value taken from resource.cryptomining_score, set as value in label with key "cryptomining _score_ %{index2}"  
resource.dataflow_score | event.idm.read_only_udm.principal.resource.attribute.labels.dataflow_label | Value taken from resource.dataflow_score, set as value in label with key "dataflow _score_ %{index2}"  
policie.description | event.idm.read_only_udm.principal.resource.attribute.labels.desc_label | Value taken from policie.description, set as value in label with key "description_%{index}"  
version.fetched_at | event.idm.read_only_udm.principal.resource.attribute.labels.fetched_at_label | Value taken from version.fetched_at, set as value in label with key "fetched _at_ %{index2}"  
version.hash | event.idm.read_only_udm.principal.resource.attribute.labels.hash_label | Value taken from version.hash, set as value in label with key "hash_%{index2}"  
policie.id | event.idm.read_only_udm.principal.resource.attribute.labels.id_label | Value taken from policie.id, set as value in label with key "policy _id_ %{index}"  
data.options.remove_dashboard_links | event.idm.read_only_udm.principal.resource.attribute.labels.remove_dash_label | Value taken from data.options.remove_dashboard_links, set as value in label with key "remove_dashboard_links"  
resource.resource_type | event.idm.read_only_udm.principal.resource.attribute.labels.res_type_label | Value taken from resource.resource_type, set as value in label with key "resource _type_ %{index2}"  
data.type | event.idm.read_only_udm.principal.resource.attribute.labels.type_label | Value taken from data.type, set as value in label with key "type"  
data.zones | event.idm.read_only_udm.principal.resource.attribute.labels.zones_label | Value taken from data.zones, set as value in label with key "zones"  
resource.id | event.idm.read_only_udm.principal.resource.id | Value taken from resource.id  
PageURL | event.idm.read_only_udm.principal.url | Value taken from PageURL  
account_id | event.idm.read_only_udm.principal.user.product_object_id | Value taken from account_id  
policy_id | event.idm.read_only_udm.security_result.detection_fields.policy_id_label | Value taken from policy_id, set as value in label with key "policy_id"  
policy_name | event.idm.read_only_udm.security_result.detection_fields.policy_name_label | Value taken from policy_name, set as value in label with key "policy_name"  
text | event.idm.read_only_udm.security_result.description | Value taken from text  
resource.first_seen_at | event.idm.read_only_udm.security_result.first_discovered_time | Converted from resource.first_seen_at to ISO8601 timestamp  
PolicyID | event.idm.read_only_udm.security_result.rule_name | Value taken from PolicyID  
data.severity | event.idm.read_only_udm.security_result.severity | Derived from data.severity: if "INFO" → "INFORMATIONAL"; if "WARN" → "MEDIUM"; else "UNKNOWN_SEVERITY"  
URL | event.idm.read_only_udm.target.url | Value taken from URL  
URLHost | event.idm.read_only_udm.target.user.email_addresses | Value taken from URLHost if matches email pattern  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudflare-pageshield-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
