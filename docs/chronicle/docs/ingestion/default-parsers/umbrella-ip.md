---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/umbrella-ip/
title: Collect Cisco Umbrella IP logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:41.030756+00:00
---

# Collect Cisco Umbrella IP logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/umbrella-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Umbrella IP logs

**Parser Version:** 8.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Umbrella IP logs into Google Security Operations using Amazon S3.

Cisco Umbrella is a cloud-delivered security service that provides the first line of defense against threats on the internet. The IP (Cloud Firewall) logs capture network traffic handled by Umbrella network tunnels, including source and destination IP addresses, ports, protocols, actions taken, and associated identities. These logs are exported as gzipped CSV files to Amazon S3 every 10 minutes.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to **Cisco Umbrella** console (Admin role)
  * Privileged access to **AWS** (S3, IAM)



## Configure Cisco Umbrella log export to S3

To configure Cisco Umbrella to export IP logs to S3, do the following:

  1. Sign in to the **Umbrella dashboard** at https://dashboard.umbrella.com
  2. Go to **Admin > Log Management**.
  3. In the **Log Management** page, locate the **Amazon S3** section.
  4. Click **Add** to configure S3 export.
  5. In the **Amazon S3 Configuration** dialog, select one of the following options:

     * **Cisco-managed S3 Bucket** : Cisco creates and manages the S3 bucket for you. Cisco provides AWS credentials to access the bucket.
     * **Customer-managed S3 Bucket** : You provide your own S3 bucket details and AWS credentials.
  6. For this guide, select **Cisco-managed S3 Bucket** (recommended for easier setup).

  7. In the **Log Types** section, select the checkbox for **IP Logs** (Cloud Firewall logs).

  8. You can also select additional log types if needed:

     * **DNS Logs**
     * **Proxy Logs**
     * **Intrusion Prevention Logs**
     * **Cloud Data Loss Prevention Logs**
  9. In the **Data Center** dropdown, select the AWS region closest to your location, or select **All Data Centers** to export logs from all regions.

  10. Click **Save**.

  11. After saving, Umbrella displays the **AWS Credentials** section with the following information:

     * **S3 Bucket Name** (for example, `umbrella-logs-1234567890`)
     * **S3 Path** (for example, `2024-01-15/`)
     * **AWS Access Key ID**
     * **AWS Secret Access Key**
     * **AWS Region**
  12. Click **Download Credentials** to save these credentials as a CSV file for future reference.

**Note:** Logs are exported to S3 every 10 minutes. The first export may take up to 10 minutes to appear in your S3 bucket.**Note:** For customer-managed S3 buckets, you must provide your own bucket name and AWS credentials, and configure appropriate IAM permissions. See [Cisco Umbrella Log Management documentation](https://docs.umbrella.com/deployment-umbrella/docs/log-management) for detailed instructions.



## Configure AWS S3 bucket and IAM for Google SecOps

If you selected **Cisco-managed S3 Bucket** in the previous section, Cisco has already created the S3 bucket and provided AWS credentials. You can skip to the "Configure a feed in Google SecOps" section below.

If you selected **Customer-managed S3 Bucket** , follow these steps:

  1. Create an **Amazon S3 bucket** by following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
  2. Save bucket **Name** and **Region** for future reference (for example, `umbrella-logs-custom`).
  3. Create a **User** by following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**.
  5. Select **Security credentials** tab.
  6. Click **Create Access Key** in the **Access Keys** section.
  7. Select **Third-party service** as **Use case**.
  8. Click **Next**.
  9. Optional: Add a description tag.
  10. Click **Create access key**.
  11. Click **Download .csv file** to save the **Access Key** and **Secret Access Key** for future reference.
  12. Click **Done**.
  13. Select **Permissions** tab.
  14. Click **Add permissions** in **Permissions policies** section.
  15. Select **Add permissions**.
  16. Select **Attach policies directly**.
  17. Search for the **AmazonS3FullAccess** policy.
  18. Select the policy.
  19. Click **Next**.
  20. Click **Add permissions**.



## Configure Cisco Umbrella customer-managed S3 bucket connection

If you selected **Cisco-managed S3 Bucket** , skip this section.

If you selected **Customer-managed S3 Bucket** , follow these steps:

  1. From the **Log Management** page (continuing from the "Configure Cisco Umbrella log export to S3" section), you should be on the **Amazon S3 Configuration** dialog.
  2. In the **Customer-managed S3 Bucket** section, enter the following:

     * **S3 Bucket Name** : Enter the bucket name you created (for example, `umbrella-logs-custom`).
     * **S3 Path** (optional): Enter a prefix for organizing logs (for example, `umbrella-ip-logs/`).
     * **AWS Access Key ID** : Enter the access key from step 11 of the AWS configuration.
     * **AWS Secret Access Key** : Enter the secret key from step 11 of the AWS configuration.
     * **AWS Region** : Select the region matching your S3 bucket from the dropdown.
  3. In the **Log Types** section, select the checkbox for **IP Logs** (Cloud Firewall logs).

  4. Click the **Test Connection** button.

  5. Wait for the test to complete. A green checkmark with the "Connection successful" message should appear.

  6. Click **Save**.

  7. On the **Log Management** page, verify that the **Amazon S3** section shows **Status: Active** and **Last Export** shows a recent timestamp.

**Note:** Umbrella requires the following IAM permissions on your S3 bucket: `s3:PutObject`, `s3:PutObjectAcl`, `s3:GetBucketLocation`, `s3:ListBucket`. See [Cisco Umbrella S3 Bucket documentation](https://docs.umbrella.com/deployment-umbrella/docs/cisco-managed-s3-bucket) for detailed IAM policy examples.



## Configure a feed in Google SecOps to ingest Cisco Umbrella IP logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. Enter a unique name for the **Feed name** (for example, `Umbrella IP Logs`).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Umbrella IP** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Specify values for the following fields:

     * **S3 URI** : Enter the S3 URI in the format: `s3://<bucket-name>/<path>/`

       * For Cisco-managed bucket: Use the **S3 Bucket Name** and **S3 Path** from step 11 of "Configure Cisco Umbrella log export to S3" (for example, `s3://umbrella-logs-1234567890/2024-01-15/`).
       * For customer-managed bucket: Use your bucket name and path (for example, `s3://umbrella-logs-custom/umbrella-ip-logs/`).
     * **Source deletion option** : Select **Do not delete transferred files** (recommended to preserve logs in S3).

**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Access Key ID** : Enter the **AWS Access Key ID** from step 11 of "Configure Cisco Umbrella log export to S3" (for Cisco-managed bucket) or step 11 of AWS configuration (for customer-managed bucket).

     * **Secret Access Key** : Enter the **AWS Secret Access Key** from step 11 of "Configure Cisco Umbrella log export to S3" (for Cisco-managed bucket) or step 11 of AWS configuration (for customer-managed bucket).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed (for example, `UMBRELLA_IP`).

  9. Click **Next** and then click **Submit**.

**Note:** Umbrella IP logs are exported as gzipped CSV files. The parser automatically handles decompression and CSV parsing. Log files are delivered to S3 every 10 minutes with a retention period of 30 days in Umbrella (perpetual retention in S3).



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
query_name | about.labels | Merged from query_name_label (key: DNS Lookup Type, value: query_name)  
response_code | additional.fields | Merged from dns_return_message (key: dns_return_message, value: response_code)  
application | intermediary | Merged from intermediary.application  
categories | metadata.description | Set to value of categories if present, else "DNS request and response were made."  
| metadata.event_type | Set to NETWORK_CONNECTION for IP logs, NETWORK_HTTP if destip and internal/external present, STATUS_UPDATE if principal present but no target, GENERIC_EVENT otherwise, or NETWORK_DNS for DNS logs  
| metadata.product_name | Set to "Cisco Umbrella" for proxy logs, "Cisco Umbrella IP Layer Enforcement" for IP logs  
| metadata.vendor_name | Set to "Cisco" for proxy logs, "Cisco Systems, Inc" for IP logs  
appProto, url | network.application_protocol | Extracted from url using grok pattern, uppercased, or set to DNS for DNS logs  
question | network.dns.questions | Merged from question (name from domain, type from query_type)  
response_code | network.dns.response_code | Converted from response_code using enum mapping to integer  
requestMethod | network.http.method | Value from requestMethod, uppercased  
userAgent | network.http.parsed_user_agent | Converted from userAgent to parseduseragent  
referer | network.http.referral_url | Value copied directly  
statusCode | network.http.response_code | Converted to integer  
userAgent | network.http.user_agent | Value copied directly  
| network.ip_protocol | Set to "TCP"  
responseSize | network.received_bytes | Converted to uinteger  
requestSize | network.sent_bytes | Converted to uinteger  
identity | principal.hostname | Value copied directly  
internal_ip, external_ip, source_ip | principal.ip | Value from internal_ip if valid IP, else external_ip if different from internalIp and valid IP, else source_ip  
source_port | principal.port | Converted to integer  
sha | security_result.about.file.sha256 | Value copied directly  
sec_action, action, security_result_action | security_result.action | Set to BLOCK if categories not empty, or ALLOW/BLOCK based on action, or ALLOW/BLOCK based on security_result_action  
sec_category, category, security_category | security_result.category | Set to ACL_VIOLATION if categories is "Unauthorized IP Tunnel Access", SOFTWARE_MALICIOUS if "Malware", NETWORK_SUSPICIOUS otherwise, or NETWORK_CATEGORIZED_CONTENT, or NETWORK_MALICIOUS/NETWORK_SUSPICIOUS based on categories in DNS  
categories | security_result.category_details | Transformed to array from categories  
responseBodySize, avDetections, puas, ampDisposition, ampMalware, ampScore, certificateErrors, destinationListID, isolateAction, fileAction, warnstatus, dlpstatus, contentType, verdict, rulesetID | security_result.detection_fields | Merged from various labels created from each field (key: field name, value: field value)  
ruleID | security_result.rule_id | Value copied directly  
verdict, contentType, dlpstatus | security_result.summary | Set to "Traffic %{verdict}" if verdict in allowed/blocked, "Traffic %{contentType}" if contentType present, or "Traffic %{dlpstatus}" if dlpstatus in allowed/blocked, or "Traffic blocked - %{blockedCategories}" if blocked  
blockedCategories | security_result.threat_name | Value copied directly  
temp_filename | target.file.names | Merged from temp_filename (value of fileName)  
destination_ip | target.ip | Value copied directly  
destination_port | target.port | Converted to integer  
url | target.url | Value copied directly  
`column3` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`column4` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column5` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column11` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`column15` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`column22` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`column13` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/umbrella-ip-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
