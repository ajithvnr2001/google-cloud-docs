---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tailscale/
title: Collect Tailscale logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:01.358805+00:00
---

# Collect Tailscale logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tailscale/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Tailscale logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Tailscale logs to Google Security Operations using Tailscale's native Amazon S3 log streaming feature. Tailscale produces operational data in the form of configuration audit logs and network flow logs. This integration uses Tailscale's built-in S3 streaming capability to automatically send these logs to Google SecOps for analysis and monitoring.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance
  * Privileged access to **Tailscale Admin Console** (Owner, Admin, Network admin, or IT admin role)
  * Privileged access to **AWS** (S3, IAM)



## Collect Tailscale prerequisites (tailnet information)

  1. Sign in to the **Tailscale Admin Console**.
  2. Note your **tailnet name** (for example, `example.com` or your organization name).
  3. Ensure you have the required plan: 
     * **Configuration audit log streaming** : Available on Personal, Personal Plus, and Enterprise plans.
     * **Network flow log streaming** : Available on Enterprise plan only.



## Configure AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save bucket **Name** and **Region** for future reference (for example, `tailscale-logs`).
  3. Create a user following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**. 
  5. Select the **Security credentials** tab.
  6. Click **Create Access Key** in the **Access Keys** section.
  7. Select **Third-party service** as the **Use case**.
  8. Click **Next**.
  9. Optional: add a description tag.
  10. Click **Create access key**.
  11. Click **Download CSV file** to save the **Access Key** and **Secret Access Key** for later use. 
  12. Click **Done**.
  13. Select the **Permissions** tab.
  14. Click **Add permissions** in the **Permissions policies** section.
  15. Select **Add permissions**.
  16. Select **Attach policies directly**
  17. Search for and select the **AmazonS3FullAccess** policy.
  18. Click **Next**.
  19. Click **Add permissions**.



## Configure the IAM policy and role for S3 uploads

  1. In the **AWS console** , go to **IAM > Policies > Create policy > JSON tab**.
  2. Enter the following policy:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Sid": "AllowTailscalePutObjects",
               "Effect": "Allow",
               "Action": [
                 "s3:PutObject",
                 "s3:PutObjectAcl"
               ],
               "Resource": "arn:aws:s3:::tailscale-logs/*"
             }
           ]
         }
         

     * Replace `tailscale-logs` if you entered a different bucket name.
  3. Click **Next > Create policy**.

  4. Go to **IAM > Roles > Create role > Custom trust policy**.

  5. Enter the following trust policy:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Principal": {
                 "AWS": "arn:aws:iam::982722776073:role/tailscale-log-streaming"
               },
               "Action": "sts:AssumeRole",
               "Condition": {
                 "StringEquals": {
                   "sts:ExternalId": "YOUR_TAILNET_NAME"
                 }
               }
             }
           ]
         }
         

     * Replace `YOUR_TAILNET_NAME` with your actual tailnet name.
  6. Click **Next**.

  7. Attach the policy created in step 1.

  8. Name the role `TailscaleS3StreamingRole` and click **Create role**.

  9. Copy the **Role ARN** for use in Tailscale configuration.




## Configure Tailscale native S3 log streaming

### Setup Configuration Audit Log streaming

  1. In the **Tailscale Admin Console** , go to **Logs > Configuration logs**.
  2. Click **Start streaming**.
  3. Select **Amazon S3** as the destination.
  4. Provide the following configuration details: 
     * **AWS Account ID** : Your AWS Account ID.
     * **S3 Bucket Name** : `tailscale-logs`.
     * **Role ARN** : The ARN of the IAM role you created.
     * **S3 Key Prefix** : `tailscale/configuration/` (optional).
  5. Click **Start streaming**.
  6. Verify the status shows as **Active**.



### Setup Network Flow Log streaming (Enterprise plan only)

  1. If not already enabled, go to **Settings > Network flow logs** and enable network flow logs for your tailnet.
  2. Go to **Logs > Network flow logs**.
  3. Click **Start streaming**.
  4. Select **Amazon S3** as the destination.
  5. Provide the following configuration details: 
     * **AWS Account ID** : Your AWS Account ID
     * **S3 Bucket Name** : `tailscale-logs`
     * **Role ARN** : The ARN of the IAM role you created
     * **S3 Key Prefix** : `tailscale/network/` (optional)
  6. Click **Start streaming**.
  7. Verify the status shows as **Active**.



## Optional: Create read-only IAM user & keys for Google SecOps

  1. In the **AWS Console**. go to **IAM > Users > Add users**.
  2. Click **Add users**.
  3. Provide the following configuration details: 
     * **User** : `secops-reader`
     * **Access type** : **Access key — Programmatic access**
  4. Click **Create user**.
  5. Attach minimal read policy (custom): **Users > secops-reader > Permissions > Add permissions > Attach policies directly > Create policy**.
  6. In the JSON editor, enter the following policy:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Action": ["s3:GetObject"],
               "Resource": "arn:aws:s3:::tailscale-logs/*"
             },
             {
               "Effect": "Allow",
               "Action": ["s3:ListBucket"],
               "Resource": "arn:aws:s3:::tailscale-logs"
             }
           ]
         }
         

  7. Set the name to `secops-reader-policy`.

  8. Go to **Create policy > search/select > Next > Add permissions**.

  9. Go to **Security credentials > Access keys > Create access key**.

  10. Download the **CSV** (these values are entered into the feed).




## Configure a feed in Google SecOps to ingest Tailscale logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **\+ Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `Tailscale logs`).
  4. Select **Amazon S3 V2** as the **Source type**.
  5. Select **Tailscale** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters: 
     * **S3 URI** : `s3://tailscale-logs/tailscale/`
     * **Source deletion options** : Select deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
     * **Asset namespace** : the [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : the label applied to the events from this feed.
  8. Click **Next**.
  9. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`exit_traf_src_port_label` | `additional.fields` | Merged  
`exit_traf_txBytes_label` | `additional.fields` | Merged  
`exit_traf_txPkts_label` | `additional.fields` | Merged  
`nodeId_label` | `additional.fields` | Merged  
`origin_label` | `additional.fields` | Merged  
`phy_traf_rxBytes_label` | `additional.fields` | Merged  
`phy_traf_rxPkts_label` | `additional.fields` | Merged  
`phy_traf_txBytes_label` | `additional.fields` | Merged  
`phy_traf_txPkts_label` | `additional.fields` | Merged  
`target1_id_label` | `additional.fields` | Merged  
`target1_type_label` | `additional.fields` | Merged  
`vir_traf_rxBytes_label` | `additional.fields` | Merged  
`vir_traf_rxPkts_label` | `additional.fields` | Merged  
`vir_traf_txBytes_label` | `additional.fields` | Merged  
`vir_traf_txPkts_label` | `additional.fields` | Merged  
`action` | `extensions.auth.type` | Mapped: `LOGIN` → `AUTHTYPE_UNSPECIFIED`  
`start` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`event_type` | `metadata.event_type` | Directly mapped  
`exit_traf.txPkts` | `network.received_bytes` | Directly mapped  
`index` | `network.received_bytes` | Mapped: `0` → `uinteger`  
`phy_traf.rxBytes` | `network.received_bytes` | Directly mapped  
`phy_traf.rxPkts` | `network.received_bytes` | Directly mapped  
`exit_traf.txBytes` | `network.sent_bytes` | Directly mapped  
`index` | `network.sent_bytes` | Mapped: `0` → `uinteger`  
`phy_traf.txBytes` | `network.sent_bytes` | Directly mapped  
`phy_traf.txPkts` | `network.sent_bytes` | Directly mapped  
`target1.name` | `principal.asset.hostname` | Directly mapped  
`src_ip` | `principal.asset.ip` | Merged  
`target1.name` | `principal.hostname` | Directly mapped  
`src_ip` | `principal.ip` | Merged  
`src_port` | `principal.port` | Directly mapped  
`action` | `security_result.action_details` | Directly mapped  
`action_details_label` | `security_result.detection_fields` | Merged  
`eventGroupID_label` | `security_result.detection_fields` | Merged  
`dst_ip` | `target.asset.ip` | Merged  
`dst_ip` | `target.ip` | Merged  
`dst_port` | `target.port` | Directly mapped  
`actor_loginName` | `target.user.email_addresses` | Merged  
`actor_display_name` | `target.user.user_display_name` | Directly mapped  
`actor_id` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tailscale-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
