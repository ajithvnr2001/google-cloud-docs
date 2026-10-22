---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/twingate/
title: Collect Twingate VPN logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:44.286466+00:00
---

# Collect Twingate VPN logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/twingate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Twingate VPN logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This Twingate parser extracts fields from Twingate VPN JSON logs, normalizes them, and maps them to the Unified Data Model (UDM). It handles various event types, including connection details, user information, resource access, and intermediary relays, enriching the data with metadata like vendor and product information.

## Before you begin

Ensure that you have the following prerequisites:

  * Google SecOps instance.
  * Privileged access to AWS IAM and S3.



## Configure Amazon S3 bucket

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save bucket **Name** and **Region** for future reference.
  3. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).

**Note:** Grant your AWS user access to the corresponding bucket. See the [AWS User Guide (Access)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/walkthrough1.html#walkthrough-grant-user1-permissions). Ensure the user has **s3:ListBucket** and **s3:PutObject** listed in their policy.
  4. Select the created **User**. 

  5. Select **Security credentials** tab.

  6. Click **Create Access Key** in section **Access Keys**.

  7. Select **Third-party service** as **Use case**.

  8. Click **Next**.

  9. Optional: add description tag.

  10. Click **Create access key**.

  11. Click **Download .csv file** for save the **Access Key** and **Secret Access Key** for future reference. 

  12. Click **Done**.

  13. Select **Permissions** tab.

  14. Click **Add permissions** in section **Permissions policies**.

  15. Select **Add permissions**.

  16. Select **Attach policies directly**.

  17. Search for **AmazonS3FullAccess** policy.

  18. Select the policy.

  19. Click **Next**.

  20. Click **Add permissions**.




## Configure Twingate sync with Amazon S3

  1. Go to the Twingate Admin Console.
  2. Go to **Settings** > **Reports**.
  3. Click **Sync to S3 Bucket**.
  4. Configure the S3 Sync:

     * **Bucket Name** : Provide the name of your S3 bucket.

**Note:** S3 bucket needs to have public access **enabled**.
     * **Access Key ID** : Enter the Access Key.

     * **Secret Access Key** : Enter the Secret Key.

  5. Click **Start Syncing**.




## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed; for example, **Twingate Logs**.
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Twingate** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **S3 URI** : the bucket URI. `s3:/BUCKET_NAME` Replace the following: 
       * `BUCKET_NAME`: the name of the bucket.
     * **Source deletion options** : select deletion option according to your preference.
**Note:** If you select the **Delete transferred files** or **Delete transferred files and empty directories** option, make sure that you granted appropriate permissions to the service account. * **Maximum File Age** : Includes files modified in the last number of days. Default is 180 days. * **Access Key ID** : the User access key with access to the s3 bucket. * **Secret Access Key** : the User secret key with access to the s3 bucket.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize screen** , and then click **Submit**.




## Field mapping reference

This parser transforms raw Twingate logs in JSON format into UDM. It normalizes the data and extracts relevant information, mapping it to corresponding UDM fields.

## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`connector.id` | `read_only_udm.additional.fields[].key` | Set to "connector_id".  
`connector.id` | `read_only_udm.additional.fields[].value.string_value` | Value from `connector.id`.  
`connector.name` | `read_only_udm.additional.fields[].key` | Set to "connector_name".  
`connector.name` | `read_only_udm.additional.fields[].value.string_value` | Value from `connector.name`.  
`connection.bytes_received` | `read_only_udm.network.received_bytes` | Value from `connection.bytes_received` (converted to an unsigned integer).  
`connection.bytes_transferred` | `read_only_udm.network.sent_bytes` | Value from `connection.bytes_transferred` (converted to an unsigned integer).  
`connection.client_ip` | `read_only_udm.principal.asset.ip` | Value from `connection.client_ip`.  
`connection.client_ip` | `read_only_udm.principal.ip` | Value from `connection.client_ip`.  
`connection.protocol` | `read_only_udm.network.ip_protocol` | Value from `connection.protocol` (converted to uppercase).  
`device.id` | `read_only_udm.principal.user.product_object_id` | Value from `device.id`.  
`event.id` | `read_only_udm.metadata.event_id` | Value from `event.id`  
`event.time` | `read_only_udm.metadata.event_timestamp.seconds` | Seconds part of the timestamp from `event.time`.  
`event.type` | `read_only_udm.event.type` | Value from `event.type`.  
`event.version` | `read_only_udm.metadata.product_version` | Value from `event.version`.  
`relays[].ip` | `read_only_udm.intermediary.ip` | Value from `relays[].ip`.  
`relays[].name` | `read_only_udm.intermediary.hostname` | Value from `relays[].name`.  
`relays[].port` | `read_only_udm.intermediary.port` | Value from `relays[].port` (converted to an integer).  
`remote_network.id` | `read_only_udm.network.session_id` | Value from `remote_network.id`.  
`remote_network.name` | `read_only_udm.network.dhcp.sname` | Value from `remote_network.name`.  
`resource.address` | `read_only_udm.principal.asset.hostname` | Value from `resource.address`.  
`resource.address` | `read_only_udm.principal.hostname` | Value from `resource.address`.  
`resource.id` | `read_only_udm.resource.product_object_id` | Value from `resource.id`.  
`resource.port` | `read_only_udm.principal.port` | Value from `resource.port` (converted to an integer).  
`status` | `read_only_udm.security_result.summary` | Value from `status`.  
`time` | `read_only_udm.event.timestamp.seconds` | Seconds part of the timestamp from `time`.  
`user.email` | `read_only_udm.principal.user.email_addresses` | Value from `user.email`.  
`user.id` | `read_only_udm.principal.user.userid` | Value from `user.id`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/twingate-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
