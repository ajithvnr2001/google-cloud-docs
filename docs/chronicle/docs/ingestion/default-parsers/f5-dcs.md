---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-dcs/
title: Collect F5 Distributed Cloud Services logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:26.430494+00:00
---

# Collect F5 Distributed Cloud Services logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-dcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect F5 Distributed Cloud Services logs

**Parser Version:** 6.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest F5 Distributed Cloud Services logs into Google Security Operations using Google Cloud Storage V2.

F5 Distributed Cloud Services is a SaaS-based security, networking, and application management platform that provides distributed cloud infrastructure, application delivery, API security, and web application firewall capabilities across multi-cloud and edge locations.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Privileged access to F5 Distributed Cloud console
  * Permissions to create Global Log Receiver objects in F5 Distributed Cloud



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `f5-dcs-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Configure F5 Distributed Cloud to export to GCS

### Add GCS bucket to firewall allowlist

  1. F5 Distributed Cloud Global Log Receiver requires the following IP address ranges to be added to your firewall allowlist:

     * `193.16.236.64/29`
     * `185.160.8.152/29`
  2. If your GCS bucket uses VPC Service Controls or firewall rules, add these IP ranges to your allowlist.




### Create a Google Cloud service account for F5 Distributed Cloud

  1. In the **Google Cloud console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details:

     * **Service account name** : Enter `f5-dcs-log-writer` (or a descriptive name)
     * **Service account description** : Enter `Service account for F5 Distributed Cloud to write logs to GCS`
  4. Click **Create and Continue**.

  5. In the **Grant this service account access to project** section:

     1. Click **Select a role**.
     2. Search for and select **Storage Object Admin**.
  6. Click **Continue**.

  7. Click **Done**.




### Create a service account key

  1. In the **Service Accounts** list, click on the service account you created (for example, `f5-dcs-log-writer`).
  2. Go to the **Keys** tab.
  3. Click **Add Key > Create new key**.
  4. Select **JSON** as the key type.
  5. Click **Create**.
  6. The JSON key file is downloaded to your computer.
  7. Save this file securely. You will need it in the next steps.



### Grant IAM permissions on the GCS bucket

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `f5-dcs-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `f5-dcs-log-writer@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



### Create Google Cloud credentials in F5 Distributed Cloud console

  1. Sign in to the **F5 Distributed Cloud console** at `https://<tenant>.console.ves.volterra.io`.
  2. Select the **Multi-Cloud Network Connect** service from the homepage.
  3. Go to **Manage > Site Management > Cloud Credentials**.
  4. Click **Add Cloud Credentials**.
  5. In the **Metadata** section: 
     * **Name** : Enter a descriptive name (for example, `gcp-chronicle-logs`)
     * **Description** (optional): Enter `Cloud Storage credentials for Google SecOps log export`
  6. In the **Cloud Credentials Type** section, select **GCP Credentials**.
  7. Click **Configure** in the **GCP Credentials** field.
  8. In the **Credential Type** dropdown, select **Service Account Credentials File**.
  9. Click **Upload File** and select the JSON key file you downloaded in the previous steps.
  10. Click **Apply**.
  11. Click **Save and Exit**.



### Create a Global Log Receiver

  1. In the **F5 Distributed Cloud Console** , ensure you are in the **Multi-Cloud Network Connect** service.
  2. Go to **Manage > Log Management > Global Log Receiver**.
  3. Click **Add Global Log Receiver**.
  4. In the **Metadata** section:

     * **Name** : Enter a descriptive name (for example, `chronicle-gcs-receiver`)
     * **Description** (optional): Enter `Global log receiver for Google SecOps SIEM`
  5. In the **Log Type** dropdown, select the log types you want to export:

     * **Request Logs** : HTTP request/response logs with user, path, method, response codes
     * **Security Events** : WAF events, DDoS, API Protection, Bot Defense events
     * **Audit Logs** : Configuration changes via public APIs
     * **DNS Request Logs** : DNS query logs
**Note:** You can create multiple Global Log Receiver objects for different log types if needed.
  6. In the **Log Message Selection** dropdown, select one of the following:

     * **Select logs from current namespace** : Sends logs from the current namespace only
     * **Select logs from all namespaces** : Sends logs from all namespaces (recommended for comprehensive visibility)
     * **Select logs in specific namespaces** : Sends logs from specified namespaces (click **Add item** to add namespace names)
  7. In the **Receiver Configuration** dropdown, select **GCP Bucket Receiver**.

  8. In the **GCP Bucket Name** field, enter the name of your GCS bucket (for example, `f5-dcs-logs`).

  9. In the **GCP Cloud Credentials** dropdown, select the cloud credentials you created earlier (for example, `gcp-chronicle-logs`).

  10. Optional: Expand **Show Advanced Fields** to configure batch options:

     * **Batch Timeout Options** : Select **Timeout Seconds** and enter a value (default: `300` seconds)
     * **Batch Max Events** : Select **Max Events** and enter a value between 32 and 2000 (leave unset for no limit)
     * **Batch Bytes** : Select **Max Bytes** and enter a value between 4096 and 1048576 (default: `10485760` bytes / 10 MB)
**Note:** Logs are written to GCS every 5 minutes as compressed gzip files in NDJSON format. Batch options control when logs are sent before the 5-minute interval.
  11. Click **Save and Exit**.




### Test the connection

  1. In the **Global Log Receiver** list, locate the receiver you created (for example, `chronicle-gcs-receiver`).
  2. Click the three dots (**...**) in the **Actions** column.
  3. Select **Test Connection**.
  4. Wait for the test to complete.
  5. A message indicating successful connection should appear.

**Note:** F5 Distributed Cloud performs up to 20 retries in case of connection failure for HTTP response codes 429, 500 and above (except 501).



### Verify logs in the GCS bucket

  1. Go to **Cloud Storage > Buckets** in the GCP console.
  2. Click on your bucket name (for example, `f5-dcs-logs`).
  3. Verify that log files are being created in the bucket.
  4. F5 Distributed Cloud organizes logs in the following folder structure:
         
         YYYY/MM/DD/HH/
         

     * A folder is created for each day (YYYY/MM/DD)
     * Within each day folder, a subfolder is created for each hour (HH)
     * Every 5 minutes, new compressed gzip files are written to the hourly subfolder
     * Files are in NDJSON format (newline-delimited JSON)
  5. Click on a gzip file to download and inspect the log format.




## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `F5 DCS Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **F5 Distributed Cloud Services** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI:
           
           gs://f5-dcs-logs/
           

Replace `f5-dcs-logs` with your GCS bucket name.

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs the **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `f5-dcs-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details:

     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
_id | metadata.product_log_id | Value copied directly  
src | principal.namespace | Value copied directly  
kubernetes_labels_app | target.resource.attribute.labels | Merged from app_label (derived from kubernetes_labels_app)  
kubernetes_host | target.hostname | Value copied directly  
kubernetes_container_name | target.resource.product_object_id | Value copied directly  
bot_info.classification | security_result.detection_fields | Merged from bot_info_classification_label (derived from bot_info.classification)  
bot_info.name | security_result.detection_fields | Merged from bot_info_name_label (derived from bot_info.name)  
bot_info.type | security_result.detection_fields | Merged from bot_info_type_label (derived from bot_info.type)  
timestamp | @timestamp | Parsed using date filter with RFC 3339, UNIX, ISO8601  
visitor_id | security_result.detection_fields | Merged from visitor_id_label (derived from visitor_id)  
tag | security_result.detection_fields | Merged from tag_label (derived from tag)  
action | security_result.action | Set to ALLOW if matches allow, BLOCK if matches deny  
severity | security_result.severity | Set to HIGH if in error/warning; CRITICAL if critical; MEDIUM if notice; LOW if information/info  
severity | security_result.severity_details | Value copied directly  
api_endpoint | target.labels | Merged from api_endpoint_label (derived from api_endpoint)  
app_firewall_name | principal.process.command_line | Value copied directly  
app_type | security_result.detection_fields | Merged from about_app_type (derived from app_type)  
as_org | security_result.detection_fields | Merged from about_as_org (derived from as_org)  
asn | security_result.detection_fields | Merged from about_asn (derived from asn)  
kubernetes.pod_id | security_result.detection_fields | Merged from about_pod_id (derived from kubernetes.pod_id)  
kubernetes.pod_name | security_result.detection_fields | Merged from about_pod_name (derived from kubernetes.pod_name)  
latitude | principal.location.region_latitude | Converted to float  
longitude | principal.location.region_longitude | Converted to float  
req_params | additional.fields | Merged from about_req_params (derived from req_params)  
as_number | additional.fields | Merged from about_as_number (converted to string from as_number)  
x_forwarded_for | intermediary.ip | Merged if valid IP  
x_forwarded_for | security_result.about.resource.attribute.labels | Merged from x_forwarded_for_label if not IP  
policy_hit.malicious_user_mitigate_action | security_result.detection_fields | Merged from malicious_user_label (derived from policy_hit.malicious_user_mitigate_action)  
policy_hit.policy | security_result.about.resource.attribute.labels | Merged from policy_label (derived from policy_hit.policy)  
policy_hit.policy_namespace | additional.fields | Merged from policy_namespace_label (derived from policy_hit.policy_namespace)  
policy_hit.policy_rule | security_result.rule_name | Value copied directly  
policy_hit.policy_rule_description | security_result.description | Value copied directly  
policy_hit.policy_set | target.resource.name | Value copied directly  
policy_hit.result | additional.fields | Merged from result_label (derived from policy_hit.result)  
vhost_id | security_result.detection_fields | Merged from vhostlabel (derived from vhost_id)  
messageid | security_result.detection_fields | Merged from messageid_label (derived from messageid)  
sec_event_name | security_result.detection_fields | Merged from sec_event_name_label (derived from sec_event_name)  
sec_event_type | security_result.detection_fields | Merged from sec_event_type_label (derived from sec_event_type)  
vh_name | security_result.detection_fields | Merged from vhost_name_label (derived from vh_name)  
tls_fingerprint | security_result.detection_fields | Merged from tls_fingerprint_label (derived from tls_fingerprint)  
time | additional.fields | Merged from time_label (derived from time)  
kubernetes.namespace_name | additional.fields | Merged from namespace_name_label (derived from kubernetes.namespace_name)  
src_instance | additional.fields | Merged from src_instance_label (derived from src_instance)  
violation_rating | additional.fields | Merged from violation_rating_label (derived from violation_rating)  
req_size | additional.fields | Merged from req_size_label (converted to string from req_size)  
rsp_code | additional.fields | Merged from rsp_code_label (converted to string from rsp_code)  
rsp_code_class | additional.fields | Merged from rsp_code_class_label (converted to string from rsp_code_class)  
rsp_size | additional.fields | Merged from rsp_size_label (converted to string from rsp_size)  
original_path | additional.fields | Merged from original_path_label (derived from original_path)  
req_path | target.url | Value copied directly  
req_headers_size | additional.fields | Merged from req_headers_size_label (derived from req_headers_size)  
recommended_action | additional.fields | Merged from recommended_action_label (derived from recommended_action)  
enforcement_mode | additional.fields | Merged from enforcement_mode_label (derived from enforcement_mode)  
src_ip | principal.ip, principal.asset.ip | Merged if matches IPv4 regex  
host | principal.ip, principal.asset.ip | Merged if matches IPv4 regex  
hostname | principal.hostname, principal.asset.hostname | Value copied directly if not empty or -  
http_version | network.application_protocol_version | Value copied directly  
http_version | network.application_protocol | Set to HTTP if contains HTTP, HTTPS if contains HTTPS  
network | principal.nat_ip | Merged if matches IPv4 regex  
dst_ip | target.ip, target.asset.ip | Merged if matches IPv4 regex  
dst_port | target.port | Converted to integer  
src_port | principal.port | Converted to integer  
src_site | additional.fields | Merged from src_site_field (derived from src_site)  
site | additional.fields | Merged from site_field (derived from site)  
cluster_name | additional.fields | Merged from cluster_name_field (derived from cluster_name)  
domain | principal.administrative_domain | Value copied directly  
method | network.http.method | Value copied directly if not empty or N/A  
namespace | target.namespace | Value copied directly  
city | principal.location.city | Value copied directly  
stream | security_result.detection_fields | Merged from stream_label (derived from stream)  
region | principal.location.country_or_region | Value copied directly  
user | principal.user.userid | Extracted from user using grok pattern for user_id  
user_ip | target.ip, target.asset.ip | Merged from extracted user_ip  
Cookie | additional.fields | Merged from cookie (derived from Cookie in req_headers)  
X-F5-Request-Id | security_result.detection_fields | Merged from x_f5_request_id (derived from X-F5-Request-Id in req_headers)  
X-Request-Id | security_result.detection_fields | Merged from request_id (derived from X-Request-Id in req_headers)  
security_result | security_result | Merged directly  
has_network, has_principal, has_target | metadata.event_type | Set to NETWORK_CONNECTION if all true; STATUS_UPDATE if has_principal true; else GENERIC_EVENT  
| metadata.vendor_name | Set to "F5_DCS"  
| metadata.product_name | Set to "F5 DCS"  
intermediary | intermediary | Merged directly  
`rsp_size` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`dst` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`has_sec_event` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`app` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`node_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sample_rate` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`time_to_first_downstream_tx_byte` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`time_to_first_upstream_rx_byte` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`time_to_first_upstream_tx_byte` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`time_to_last_downstream_tx_byte` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`time_to_last_rx_byte` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`time_to_last_upstream_rx_byte` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`time_to_last_upstream_tx_byte` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`timeseries_enabled` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sni` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`terminated_time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rtt_downstream_seconds` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rtt_upstream_seconds` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rsp_code_details` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`authority` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`connected_time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`req_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`proxy_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vh_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dst_instance` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`lb_port` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`mtls` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ja4_tls_fingerprint` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`duration_with_data_tx_delay` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dst_site` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`protocol and scheme` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`referer` | `event.idm.read_only_udm.network.http.referral_url` | Mapped from changelog  
`tls_cipher_suite` | `event.idm.read_only_udm.network.tls.cipher` | Mapped from changelog  
`tls_version` | `event.idm.read_only_udm.network.tls.version` | Mapped from changelog  
`user_agent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`user_agent` | `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
`browser_type` | `event.idm.read_only_udm.principal.browser.browser_type` | Mapped from changelog  
`content-type` | `event.idm.read_only_udm.principal.process.file.mime_type` | Mapped from changelog  
`response_flags` | `security_result.detection_fields` | Mapped from changelog  
`original_authority` | `event.idm.read_only_udm.target.administrative_domain` | Mapped from changelog  
`country` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-dcs-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
