---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cato-networks/
title: Collect Cato Networks logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:48.891776+00:00
---

# Collect Cato Networks logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cato-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cato Networks logs

**Parser Version:** 6.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cato Networks logs to Google Security Operations using AWS S3. The parser first initializes a set of fields to empty strings and then parses JSON-formatted Cato Networks logs. It then maps the extracted fields to the corresponding fields in the Google SecOps Unified Data Model (UDM) model, handling different event types and enriching the data with additional context.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance
  * Privileged access to AWS S3, AWS IAM
  * Privileged access to Cato Networks



## Configure AWS IAM and S3 Bucket

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save the bucket **Name** and **Region** for future reference.
  3. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**. 
  5. Select the **Security credentials** tab.
  6. Click **Create Access Key** in the **Access Keys** section.
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
  17. Search for the **AmazonS3FullAccess** policy and then select the policy.
  18. Click **Next**.
  19. Click **Add permissions**.



## Configure a New IAM Policy For S3 Bucket to enable data uploads

  1. In **Policy** , click the **JSON** tab.
  2. Edit the following **JSON** , replace `<bucket name>` with your S3 bucket, and then paste it in the tab.
         
         {
             "Version": "2012-10-17",
             "Statement": [
                 {
                     "Sid": "",
                     "Effect": "Allow",
                     "Action": [
                         "s3:ListBucket",
                         "s3:GetBucketLocation"
                     ],
                     "Resource": [
                         "arn:aws:s3:::<bucket name>"
                     ]
                 },
                 {
                     "Sid": "",
                     "Effect": "Allow",
                     "Action": [
                         "s3:PutObject"
                     ],
                     "Resource": [
                         "arn:aws:s3:::<bucket name>/*"
                     ]
                 }
             ]
         }
         

  3. Click **Create policy**.




## Configure a New IAM Role With Cato's ARN

  1. In the **Select trusted entity** screen, select **Custom Trust Policy** and add Cato's ARN to the role: arn:aws:iam::428465470022:role/cato-events-integration
         
         {
             "Version": "2012-10-17",
             "Statement": [
                 {
                     "Sid": "Statement1",
                     "Effect": "Allow",
                     "Principal": {
                         "AWS": "arn:aws:iam::428465470022:role/cato-events-integration"
                     },
                     "Action": "sts:AssumeRole"
                 }
             ]
         }
         

  2. Click **Next**.

  3. In the **Add permissions** screen, attach the policy that you created earlier to the role.

  4. Click **Next**.

  5. Enter the **Role name** and click **Create role**.




## Configure Cato Networks Events and S3 Integration

  1. Sign in to the **Cato Networks** web UI.
  2. Go to **Resources > Event Integrations**.
  3. Click **Enable integration with Cato events**.
  4. Click **New**.
  5. Provide the following configuration details: 
     * Enter the **Name** for the integration.
     * **Bucket Name** : Identical name of the S3 bucket.
     * **Folder** : Identical name for the folder path within the S3 bucket (if necessary).
     * **Region** : Identical region for the S3 bucket.
     * **Role ARN** : Copy and paste the ARN for the role for the S3 bucket.
     * (Optional) Define the filter settings for events that are uploaded to the S3 bucket (When you define multiple filters, there is an AND relationship, and the events that match all filters are uploaded).
  6. Click **Apply**.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Cato Logs`).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Cato Networks** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **S3 URI** : The bucket URI (the format should be: `s3://<your-log-bucket-name>`). Replace the following:

       * `your-log-bucket-name`: the name of the bucket.
     * **Source deletion options** : Select deletion option according to your preference.

**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account. * **Maximum File Age** : Includes files modified in the last number of days. Default is 180 days. * **Access Key ID** : the User access key with access to the S3 bucket. * **Secret Access Key** : the User secret key with access to the S3 bucket.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
account_id | target.user.userid | The value of this field is taken from the `account_id` field.  
action | additional.fields.value.string_value | The value of this field is taken from the `action` field.  
app_stack | additional.fields.value.list_value.values.string_value | The value of this field is taken from the `app_stack` field.  
application | principal.application | The value of this field is taken from the `application` field.  
categories | additional.fields.value.list_value.values.string_value | The value of this field is taken from the `categories` field.  
clientIP | principal.ip, principal.asset.ip | The value of this field is taken from the `clientIP` field.  
creationTime |  | This field is used to calculate the event timestamp.  
custom_categories | additional.fields.value.list_value.values.string_value | The value of this field is taken from the `custom_categories` field.  
dest_country | target.location.country_or_region | The value of this field is taken from the `dest_country` field.  
dest_country_code | target.resource.attribute.labels.value | The value of this field is taken from the `dest_country_code` field.  
dest_ip | target.ip, target.asset.ip | The value of this field is taken from the `dest_ip` field.  
dest_port | target.port | The value of this field is taken from the `dest_port` field.  
destinationCountry | target.location.country_or_region | The value of this field is taken from the `destinationCountry` field.  
destinationIp | target.ip, target.asset.ip | The value of this field is taken from the `destinationIp` field.  
destinationName | target.hostname, target.asset.hostname | The value of this field is taken from the `destinationName` field.  
device_name | network.dhcp.client_hostname | The value of this field is taken from the `device_name` field.  
dns_name | additional.fields.value.string_value | The value of this field is taken from the `dns_name` field.  
event_count | additional.fields.value.string_value | The value of this field is taken from the `event_count` field.  
event_sub_type | metadata.description | The value of this field is taken from the `event_sub_type` field.  
fieldsMap.ISP_name | additional.fields.value.string_value | The value of this field is taken from the `fieldsMap.ISP_name` field.  
fieldsMap.action | security_result.action_details | The value of this field is taken from the `fieldsMap.action` field.  
fieldsMap.categories | security_result.category_details | The value of this field is taken from the `fieldsMap.categories` field.  
fieldsMap.dest_country | target.location.country_or_region | The value of this field is taken from the `fieldsMap.dest_country` field.  
fieldsMap.dest_ip | target.ip, target.asset.ip | The value of this field is taken from the `fieldsMap.dest_ip` field.  
fieldsMap.dest_port | principal.port | The value of this field is taken from the `fieldsMap.dest_port` field.  
fieldsMap.domain_name | principal.administrative_domain | The value of this field is taken from the `fieldsMap.domain_name` field.  
fieldsMap.event_sub_type | metadata.description | The value of this field is taken from the `fieldsMap.event_sub_type` field.  
fieldsMap.event_type | metadata.product_event_type | The value of this field is taken from the `fieldsMap.event_type` field.  
fieldsMap.ip_protocol | network.ip_protocol | The value of this field is taken from the `fieldsMap.ip_protocol` field.  
fieldsMap.os_type |  | This field is used to determine the operating system of the principal.  
fieldsMap.pop_name | additional.fields.value.string_value | The value of this field is taken from the `fieldsMap.pop_name` field.  
fieldsMap.rule_id | security_result.rule_id | The value of this field is taken from the `fieldsMap.rule_id` field.  
fieldsMap.rule_name | security_result.rule_name | The value of this field is taken from the `fieldsMap.rule_name` field.  
fieldsMap.src_ip | principal.ip, principal.asset.ip | The value of this field is taken from the `fieldsMap.src_ip` field.  
fieldsMap.src_isp_ip | src.ip, src.asset.ip | The value of this field is taken from the `fieldsMap.src_isp_ip` field.  
fieldsMap.time |  | This field is used to calculate the event timestamp.  
file_hash | target.file.sha256 | The value of this field is taken from the `file_hash` field.  
file_name | target.file.full_path | The value of this field is taken from the `file_name` field.  
file_size | target.file.size | The value of this field is taken from the `file_size` field.  
http_host_name | principal.hostname, principal.asset.hostname | The value of this field is taken from the `http_host_name` field.  
insertionDate | additional.fields.value.string_value | The value of this field is taken from the `insertionDate` field.  
internalId | additional.fields.value.string_value | The value of this field is taken from the `internalId` field.  
ip_protocol | network.ip_protocol | The value of this field is taken from the `ip_protocol` field.  
is_sanctioned_app | security_result.detection_fields.value | The value of this field is taken from the `is_sanctioned_app` field.  
os_type | principal.platform | The value of this field is taken from the `os_type` field.  
pop_name |  | This field is used to populate the `fieldsMap.pop_name` field.  
prettyType | metadata.product_event_type | The value of this field is taken from the `prettyType` field.  
rule | additional.fields.value.string_value | The value of this field is taken from the `rule` field.  
rule_id | security_result.rule_id | The value of this field is taken from the `rule_id` field.  
rule_name | security_result.rule_name | The value of this field is taken from the `rule_name` field.  
server_port | target.port | The value of this field is taken from the `server_port` field.  
severity | security_result.severity_details | The value of this field is taken from the `severity` field.  
sourceCountry | principal.location.country_or_region | The value of this field is taken from the `sourceCountry` field.  
sourceInternalIp | principal.ip | The value of this field is taken from the `sourceInternalIp` field.  
sourceIp | src.ip, src.asset.ip | The value of this field is taken from the `sourceIp` field.  
sourceName | principal.user.user_display_name | The value of this field is taken from the `sourceName` field.  
sport | principal.port | The value of this field is taken from the `sport` field.  
src_country |  | This field is used to populate the `sourceCountry` field.  
src_country_code | principal.resource.attribute.labels.value | The value of this field is taken from the `src_country_code` field.  
src_ip | principal.ip, principal.asset.ip | The value of this field is taken from the `src_ip` field.  
src_is_site_or_vpn | security_result.detection_fields.value | The value of this field is taken from the `src_is_site_or_vpn` field.  
src_isp_ip | src.ip, src.asset.ip | The value of this field is taken from the `src_isp_ip` field.  
src_site | additional.fields.value.string_value | The value of this field is taken from the `src_site` field.  
src_site_name | additional.fields.value.string_value | The value of this field is taken from the `src_site_name` field.  
start |  | This field is used to calculate the event timestamp.  
subnet_name | additional.fields.value.string_value | The value of this field is taken from the `subnet_name` field.  
time |  | This field is used to calculate the event timestamp.  
time_str |  | This field is used to calculate the event timestamp.  
tunnel_host_logon_names | principal.user.userid | The value of this field is taken from the `tunnel_host_logon_names` field.  
URL | target.url | The value of this field is taken from the `url` field.  
user_id | principal.user.userid | The value of this field is taken from the `user_id` field.  
| metadata.event_type | The value of this field is set to `GENERIC_EVENT` and can be overridden to `NETWORK_CONNECTION`, `NETWORK_DHCP` or `NETWORK_HTTP` based on the event.  
| metadata.log_type | The value of this field is set to `CATO_NETWORKS`.  
| metadata.product_name | The value of this field is set to `SASE`.  
| metadata.vendor_name | The value of this field is set to `Cato Networks`.  
| network.application_protocol | The value of this field is set to `DHCP` for `Connected` events.  
| network.dhcp.chaddr | The value of this field is set to `01:23:45:ab:cd:ef` for `Connected` events.  
| network.dhcp.lease_time_seconds | The value of this field is set to `86400` for `Connected` events.  
| network.dhcp.opcode | The value of this field is set to `BOOTREPLY` for `Connected` events.  
| network.dhcp.type | The value of this field is set to `ACK` for `Connected` events.  
| network.direction | The value of this field is set to `OUTBOUND` for `Anti Malware` and `URL Filtering` events.  
| security_result.action | The value of this field is set to `ALLOW` if the `action` field is not `BLOCK`, otherwise it is set to `BLOCK`.  
event_type | metadata.description | The value of this field is taken from the `event_type` field.  
`creation_date` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`admin_id` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`admin` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`change_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`module` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`model_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`insertion_date` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`change_After_overrideCategories` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`change_Before_overrideCategories` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`model_type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`src_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`application_name` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`dest_site_id` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`dest_site_name` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`connection_origin` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dest_is_site_or_vpn` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`internal_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`link_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tunnel_protocol` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`visible_device_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_sub_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`connector_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`connector_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`epp_engine_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`incident_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`title` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vendor` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vendor_device_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`engine_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`recommended_actions` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`device_posture_profile` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`parent_connector_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`client_class` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`congestion_algorithm` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`custom_category` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`custom_category_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`custom_category_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tcp_acceleration` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sr_action` | `ALLOW` | Mapped from changelog  
`sr_action` | `BLOCK` | Mapped from changelog  
`sr_action` | `FAIL` | Mapped from changelog  
`sr_action` | `CHALLENGE` | Mapped from changelog  
`sr_action` | `UNKNOWN_ACTION` | Mapped from changelog  
`src_site_name", "event_type", "event_count", "dns_name", "insertionDate", "action", "subnet_name", "internalId", "src_site", "categories", "app_stack", "custom_categories", "ISP_name", and "rule` | `additional.fields` | Mapped from changelog  
`src_is_site_or_vpn", and "is_sanctioned_app` | `security_result.detection_fields` | Mapped from changelog  
`src_isp_ip" and "src_ip` | `src.ip` | Mapped from changelog  
`src_country" and "sourceCountry` | `principal.location.country_or_region` | Mapped from changelog  
`tar_ip" and "dest_ip` | `target.ip` | Mapped from changelog  
`prin_ip` | `principal.ip` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cato-networks-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
