---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-mail-relay/
title: Collect Forcepoint Mail Relay logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:48:58.829130+00:00
---

# Collect Forcepoint Mail Relay logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-mail-relay/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Forcepoint Mail Relay logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Forcepoint Mail Relay logs to Google Security Operations using Amazon S3.

Forcepoint Mail Relay is a cloud-based email security solution that protects organizations from email-borne threats including spam, phishing, malware, and data loss. The solution provides comprehensive email filtering, data loss prevention (DLP), encryption, and advanced threat protection for both inbound and outbound email traffic.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to **Forcepoint Mail Relay Cloud** portal
  * Privileged access to **AWS** (S3, IAM)
  * **Log Export** permission enabled for your Forcepoint administrator account



## Configure Forcepoint Mail Relay Cloud SIEM storage

To configure Forcepoint Mail Relay Cloud to export logs to your AWS S3 bucket, do the following:

  1. Create one or more AWS S3 buckets on the AWS portal.

**Note:** Bucket names must be globally unique. Encryption for the AWS S3 buckets is not supported.
  2. Sign in to the **Forcepoint Cloud Security Gateway Portal**.

  3. Go to **Account > SIEM Storage**.

  4. In the **Storage type** section, select the **Bring your own storage** radio button.

  5. Click **Add** to add your bucket to the **Storage List: Bring Your Own** table.

  6. In the **Add Bucket** dialog, enter the following:

     * **Bucket name** : Enter the bucket name from the AWS portal (for example, `forcepoint-email-logs`).
     * **Prefix** (optional): Enter a prefix to organize log files. Use `/` to create a folder (for example, `email-logs/`). If no `/` is included, the prefix is prepended to the filename.
  7. Click **Save**. The bucket information is added to the table.

  8. In the **Storage List: Bring Your Own** table, click the **JSON** link in the row for the bucket you just added.

  9. On the **Bucket Policy** page, click **Copy Text** to copy the contents of the JSON pane to a clipboard.

  10. In the **AWS Management Console** , open the **S3** service.

  11. Select your bucket (for example, `forcepoint-email-logs`).

  12. Go to **Permissions > Bucket policy**.

  13. Click **Edit**.

  14. Paste the JSON policy copied from the Forcepoint portal.

  15. Click **Save changes**.

  16. Return to the Forcepoint portal **SIEM Storage** page.

  17. In the **Storage List: Bring Your Own** table, click **Check connection** for your bucket.

**Note:** If the connection is successful, a token file is written to confirm that files can be written to the bucket. The token number appears in the `connection_token` object in the AWS S3 bucket. If a folder was created based on the prefix, the `connection_token` appears in that folder. The generated token is valid for 3 hours.
  18. After the connection test succeeds, select the **Active** radio button for your bucket in the **Storage List: Bring Your Own** table.

**Note:** Only one bucket can be selected as Active. SIEM data is exported to the active bucket.
  19. Click **Save** at the bottom of the page.




## Enable SIEM logging and configure export format

  1. In the Forcepoint portal, go to **Reporting > Account Reports > SIEM Integration**.
  2. From the **Data type** list, select **Email Security**.
  3. Set the **Enable data export** toggle to **ON**.

**Note:** The option to export data cannot be set to ON unless a valid storage option has been configured on **Account > SIEM Storage**.
  4. From the **Attributes** section on the left, drag the following attributes into the **Columns** section:

     * Direction
     * From: Address
     * Policy
     * Recipient Address
     * Recipient Domain
     * Sender Domain
     * Sender Name
     * Subject
     * Action
     * Black/Whitelisted
     * Blocked Attachment Ext
     * Filtering Reason
     * Sender IP
     * Sender IP Country
     * Attachment File Type
     * Attachment Filename
     * Emb. URL Risk Class
     * Emb. URL Severity
     * Advanced Encryption
     * File Sandbox status
     * Virus Name
     * Date & Time
     * Message Size
     * Spam score
     * Attachment Size
**Note:** Make sure all the above attributes are selected. Data ingest won't work as expected if data is missing.
  5. Click **Save**.




## Configure AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)

**Note:** You can use the same bucket created for Forcepoint export, or create a separate bucket for Google SecOps ingestion.
  2. Save bucket **Name** and **Region** for future reference (for example, `forcepoint-email-logs`).

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




## Configure a feed in Google SecOps to ingest Forcepoint Mail Relay logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. Enter a unique name for the **Feed name**.
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Forcepoint Mail Relay** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Specify values for the following fields:

     * **S3 URI** : `s3://forcepoint-email-logs/email-logs/`.
     * **Source deletion option** : Select the deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
  9. Click **Next** and then click **Submit**.




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
| hybridSpamScore_label.key | Set to "hybridSpamScore"  
hybridSpamScore | hybridSpamScore_label.value | Value copied directly  
| localSpamScore_label.key | Set to "localSpamScore"  
localSpamScore | localSpamScore_label.value | Value copied directly  
| metadata.event_type | Set to "GENERIC_EVENT" initially; set to "EMAIL_TRANSACTION" if has_network_email is true; else set to "NETWORK_CONNECTION" if has_principal and has_target are true; else set to "STATUS_UPDATE" if has_principal is true; else "GENERIC_EVENT"  
product_event_type | metadata.product_event_type | Value copied directly  
| metadata.product_name | Set to "FORCEPOINT_MAIL_RELAY"  
| metadata.vendor_name | Set to "FORCEPOINT_MAIL_RELAY"  
sender | network.email.from | Value copied directly  
subject | network.email.subject | Value copied directly  
recipient | network.email.to | Value copied directly  
identHostName | principal.asset.hostname | Value copied directly  
identSrc, trueSrc, src | principal.asset.ip | Value from src if not empty, else trueSrc if not empty, else identSrc  
identHostName | principal.hostname | Value copied directly  
identSrc, trueSrc, src | principal.ip | Value from src if not empty, else trueSrc if not empty, else identSrc  
sender | principal.user.email_addresses | Value copied directly  
summary | security_result.action | Set to "ALLOW" if summary matches (?i)clean  
act | security_result.action_details | Value copied directly  
hybridSpamScore_label, localSpamScore_label | security_result.detection_fields | Merged from hybridSpamScore_label and localSpamScore_label  
summary | security_result.summary | Value copied directly  
dst | target.asset.ip | Value copied directly  
dst | target.ip | Value copied directly  
recipient | target.user.email_addresses | Value copied directly  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forcepoint-mail-relay-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
