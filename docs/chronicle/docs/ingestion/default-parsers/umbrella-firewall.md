---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/umbrella-firewall/
title: Collect Cisco Umbrella Cloud Firewall logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:57.592611+00:00
---

# Collect Cisco Umbrella Cloud Firewall logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/umbrella-firewall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Umbrella Cloud Firewall logs

**Parser Version:** 4.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Umbrella Cloud Firewall logs into Google Security Operations using Amazon S3.

Cisco Umbrella Cloud Firewall (CDFW) provides cloud-delivered firewall protection that inspects and controls network traffic based on IP addresses, ports, and protocols. CDFW enforces firewall policies for users connecting through IPsec tunnels or roaming clients, blocking malicious traffic and unauthorized applications, while providing detailed visibility into network activity with comprehensive logging of all firewall events, including packet counts, byte transfers, application identification, and posture information.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to **Cisco Umbrella** console with Full Admin role
  * Privileged access to **AWS** (S3, Identity and Access Management (IAM))



## Configure Cisco Umbrella for S3 log export

Cisco Umbrella supports two S3 export options: Cisco-managed buckets and self-managed buckets. This guide covers the Cisco-managed option for simplified setup.

  1. Sign in to the **Cisco Umbrella Dashboard** at https://dashboard.umbrella.com
  2. Go to **Admin > Log Management**.
  3. In the **Amazon S3** section, click **Use a Cisco-managed Amazon S3 bucket**.
  4. In the **Select a Region** dropdown, select the AWS region closest to your location (available options: **US East (N. Virginia)** , **US West (Oregon)** , **EU (Frankfurt)** , **AP (Sydney)**).
  5. In the **Select a Retention Duration** dropdown, select your preferred retention period (**7 days** , **14 days** , or **30 days**).

**Note:** Retention duration determines how long Cisco retains logs in the managed bucket. Select a duration that aligns with your ingestion frequency.
  6. Click **Save**.

  7. Click **Continue** to confirm the configuration.

  8. Wait for Umbrella to provision the S3 bucket. When it is complete, the **Amazon S3 Summary** page displays.

  9. Copy and securely save the following credentials:

     * **Access Key** (displayed in the **Access** field)
     * **Secret Key** (displayed in the **Secret** field)
     * **S3 URI** (displayed in the **S3 URI** field, in the format `s3://cisco-managed-<region>/<organization-id>/`)
**Note:** These credentials are displayed only once. If they are lost, you must rotate the keys through **Admin > Log Management > Rotate Keys**.
  10. Select the **Got it** checkbox.

  11. Click **Continue**.

Umbrella begins uploading firewall logs to the S3 bucket every 10 minutes in gzipped CSV format.




## S3 bucket folder structure

  * Umbrella organizes Cloud Firewall logs in the S3 bucket using the following structure:
        
        s3://cisco-managed-<region>/<organization-id>/firewalllogs/YYYY-MM-DD/YYYY-MM-DD-HH-MM-<xxxx>.csv.gz
        

For example:
        
        s3://cisco-managed-us-west-2/1234567890/firewalllogs/2026-02-03/2026-02-03-14-30-0001.csv.gz
        

**Note:** Each file contains up to 10 minutes of firewall events in CSV format, compressed with gzip. The `<xxxx>` suffix is a sequence number for files generated in the same 10-minute interval.



## Configure AWS S3 bucket and IAM for Google SecOps

Since Cisco manages the S3 bucket, you must create an IAM user with read-only access to retrieve logs for Google SecOps ingestion.

  1. Create a **User** by following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  2. Select the created **User**.
  3. Select the **Security credentials** tab.
  4. Click **Create Access Key** in the **Access Keys** section.
  5. Select **Third-party service** as **Use case**.
  6. Click **Next**.
  7. Optional: Add a description tag.
  8. Click **Create access key**.
  9. Click **Download .csv file** to save the **Access Key** and **Secret Access Key** for future reference.
  10. Click **Done**.
  11. Select **Permissions** tab.
  12. Click **Add permissions** in the **Permissions policies** section.
  13. Select **Add permissions**.
  14. Select **Attach policies directly**.
  15. Search for the **AmazonS3ReadOnlyAccess** policy.
  16. Select the policy.
  17. Click **Next**.
  18. Click **Add permissions**.

**Note:** Read-only access is sufficient since Cisco Umbrella manages write permissions to the bucket.



## Configure a feed in Google SecOps to ingest Cisco Umbrella Cloud Firewall logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. Enter a unique name for the **Feed name**.
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **UMBRELLA_FIREWALL** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Specify values for the following fields:

     * **S3 URI** : Enter the S3 URI from step 9 of Cisco Umbrella configuration (for example, `s3://cisco-managed-us-west-2/1234567890/firewalllogs/`).
     * **Source deletion option** : Select **Do not delete transferred files**.

**Note:** For Cisco-managed buckets, always select **Do not delete transferred files** to avoid permission errors. Cisco manages log retention based on the duration configured in step 5 of the Configure Cisco Umbrella for S3 log export section.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Access Key ID** : Enter the access key from step 9 of AWS IAM configuration.

     * **Secret Access Key** : Enter the secret key from step 9 of AWS IAM configuration.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next** and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
dns_question | additional.fields | Merged from dns_return_message_label  
daction | security_result.action_details | Value copied directly from sec_action  
verdict, security_action | security_result.action | Value from verdict if in ALLOW/DENY/DROP/ALLOW_WITH_MODIFICATION, else from security_action mapped to ALLOW or BLOCK  
ruleId, column20 | security_result.rule_id | Value from ruleId, or from column20 if integer  
verdict, pcdetails, tcdetails, phost, thost | security_result.category_details | Value from verdict if not in standard actions, else from pcdetails or tcdetails or phost or thost if not in specific host types  
originId | intermediary.resource.id | Value copied directly  
identity | intermediary.resource.name | Value copied directly  
dataCenter | intermediary.location.name | Value copied directly  
intermediary | intermediary | Merged from intermediary object  
metadata.event_type | metadata.event_type | Set to "NETWORK_CONNECTION" initially, then "STATUS_UPDATE" if has_principal true and has_target false, else "GENERIC_EVENT" if both false  
desc | metadata.description | Value copied directly  
proto | network.ip_protocol | Value set to "ICMP" if ipProtocol 1, "TCP" if 6, "UDP" if 17  
packetSize, response_size | network.received_bytes | Value from packetSize if direction INBOUND, or from response_size  
packetSize | network.sent_bytes | Value from packetSize if direction OUTBOUND  
direction | network.direction | Value copied directly if in BROADCAST/INBOUND/OUTBOUND  
http_method | network.http.method | Value copied directly  
http_reponse_code | network.http.response_code | Converted to integer from http_reponse_code  
usr_agent | network.http.user_agent | Value copied directly  
refer_url | network.http.referral_url | Value copied directly  
dns_question | network.dns.questions | Merged from dns_question  
response_code | network.dns.response_code | Converted to numeric code from response_code mappings  
principal_ip, principalip, sourceIp, _internalip, _externalip | principal.ip | Value from principal_ip (direction) if IP, else principalip (packetSize) if IP, else sourceIp, else _internalip if IP, else _externalip if IP and different  
principal_ip, principalip, sourceIp, _internalip, _externalip | principal.asset.ip | Value from principal_ip (direction) if IP, else principalip (packetSize) if IP, else sourceIp, else _internalip if IP, else _externalip if IP and different  
sourcePort | principal.port | Value copied directly  
prin_host, phost | principal.hostname | Value from prin_host if in specific types, else from phost if in specific types  
phost | principal.asset.hostname | Value copied directly if in specific host types  
organization_id_label, most_granular_identity_label | principal.asset.attribute.labels | Merged from organization_id_label and most_granular_identity_label  
destinationIp | target.ip | Value copied directly  
destinationIp | target.asset.ip | Value copied directly  
destinationPort | target.port | Converted to integer from destinationPort  
target_host, thost | target.hostname | Value from target_host if in specific types, else from thost if in specific types  
thost | target.asset.hostname | Value copied directly if in specific host types  
target_url | target.url | Value copied directly  
granular_identity_label | target.asset.attribute.labels | Merged from granular_identity_label  
| metadata.vendor_name | Set to "Cisco"  
| metadata.product_name | Set to "Umbrella Cloud Firewall"  
`http_response_code` | `network.http.response_code` | Mapped from changelog  
`rule_Id` | `security_result.rule_id` | Mapped from changelog  
`sec_description` | `security_result.description` | Mapped from changelog  
`intermediary_hostname` | `intermediary.hostname` | Mapped from changelog  
`dns_rrtype` | `network.dns.questions` | Mapped from changelog  
`principal_host` | `principal.hostname` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/umbrella-firewall-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
