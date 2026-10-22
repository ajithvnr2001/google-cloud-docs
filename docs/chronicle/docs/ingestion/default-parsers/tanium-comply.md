---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-comply/
title: Collect Tanium Comply logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:48.019658+00:00
---

# Collect Tanium Comply logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-comply/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Tanium Comply logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Tanium Comply logs to Google Security Operations using Amazon S3 using Tanium Connect's native S3 export capability. The parser transforms JSON log data into a unified data model (UDM). It extracts key vulnerability information like CVE ID, CVSS scores, affected IP addresses, and timestamps, then restructures them into the standardized UDM format for consistent security analysis. 

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to **Tanium Connect** and **Tanium Console**
  * **Tanium Comply** 2.1 or later installed and configured
  * Privileged access to **AWS** (S3, IAM)



## Configure AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save bucket **Name** and **Region** for future reference (for example, `tanium-comply-logs`).
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



## Configure permissions on Amazon S3 bucket

  1. In the **Amazon S3 console** , choose the bucket that you previously created.
  2. Click **Permissions > Bucket policy**.
  3. In the **Bucket Policy Editor** , add the following policy:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Principal": {
                 "AWS": "arn:aws:iam::YOUR_ACCOUNT_ID:user/tanium-connect-s3-user"
               },
               "Action": [
                 "s3:PutObject",
                 "s3:PutObjectAcl",
                 "s3:GetObject",
                 "s3:ListBucket"
               ],
               "Resource": [
                 "arn:aws:s3:::tanium-comply-logs",
                 "arn:aws:s3:::tanium-comply-logs/*"
               ]
             }
           ]
         }
         

  4. Replace the following variables:

     * Change `YOUR_ACCOUNT_ID` to your AWS account ID.
     * Change `tanium-comply-logs` to your actual bucket name if different.
     * Change `tanium-connect-s3-user` to your actual IAM username if different.
  5. Click **Save**.




## Configure Tanium Connect for S3 export

  1. Sign in to the **Tanium Console** as an administrator.
  2. Go to **Tanium Connect > Connections**.
  3. Click **Create Connection**.
  4. In the **General Information** section, provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Tanium Comply to S3`).
     * **Description** : Enter a meaningful description (for example, `Export Tanium Comply findings to S3 for Google SecOps ingestion`).
     * **Enable** : Select to enable the connection.
     * **Log Level** : Select **Information** (default) or adjust as needed.
  5. In the **Configuration** section, for **Source** , select **Tanium Comply (Findings)**.

**Note:** The Tanium Comply (Assessments) source is deprecated. Use the Tanium Comply (Findings) source for compliance and vulnerability findings data.
  6. Configure the Comply source settings:

     * **Finding Type** : Select the type of findings to export (All, Compliance, or Vulnerability).
     * **Include Resolved Findings** : Select whether to include findings that have been resolved.
     * **Computer Groups** : Select the computer groups to include in the export (default: All Computers).
  7. For **Destination** , select **AWS S3**.

  8. Provide the following configuration details:

     * **Destination Name** : Enter a name (for example, `Google SecOps S3 Bucket`).
     * **AWS Access Key** : Enter the Access Key ID from the IAM user created earlier.
     * **AWS Secret Key** : Enter the Secret Access Key from the IAM user created earlier.
     * **Bucket Name** : Enter your S3 bucket name (for example, `tanium-comply-logs`).
     * **Bucket Path** : Optional. Enter a path prefix (for example, `tanium/comply/`).
     * **Region** : Select the AWS region where your bucket resides (for example, `us-east-1`).
  9. In the **Format** section, configure the output format:

     * **Format Type** : Select **JSON**.
     * **Include Column Headers** : Select if you want column headers included.
     * **Generate Document** : Deselect this option to send raw JSON data.
  10. Optional: In the **Configure Output** section, configure filters and custom columns as needed.

  11. In the **Schedule** section, configure when the connection runs:

     * **Schedule Type** : Select **Cron**.
     * **Cron Expression** : Enter a cron expression for regular exports (for example, `0 */4 * * *` for every 4 hours).
     * **Start Date** : Set the start date for the schedule.
  12. Click **Save Changes**.

  13. From the **Connect Overview** page, go to **Connections**.

  14. Click the connection you created (**Tanium Comply to S3**).

  15. Click **Run Now** to test the connection.

  16. Confirm that you want to run the connection.

  17. Monitor the connection status and verify that compliance findings are being exported to your S3 bucket.




## Optional: Create read-only IAM user & keys for Google SecOps

  1. Go to **AWS Console > IAM > Users > Add users**.
  2. Click **Add users**.
  3. Provide the following configuration details: 
     * **User** : Enter `secops-reader`.
     * **Access type** : Select **Access key – Programmatic access**.
  4. Click **Create user**.
  5. Attach minimal read policy (custom): **Users > secops-reader > Permissions > Add permissions > Attach policies directly > Create policy**.
  6. In the JSON editor, enter the following policy:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Action": ["s3:GetObject"],
               "Resource": "arn:aws:s3:::tanium-comply-logs/*"
             },
             {
               "Effect": "Allow",
               "Action": ["s3:ListBucket"],
               "Resource": "arn:aws:s3:::tanium-comply-logs"
             }
           ]
         }
         

  7. Set the name to `secops-reader-policy`.

  8. Go to **Create policy > search/select > Next > Add permissions**.

  9. Go to **Security credentials > Access keys > Create access key**.

  10. Download the **CSV** (these values are entered into the feed).




## Configure a feed in Google SecOps to ingest Tanium Comply logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **\+ Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `Tanium Comply logs`).
  4. Select **Amazon S3 V2** as the **Source type**.
  5. Select **Tanium Comply** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters: 
     * **S3 URI** : `s3://tanium-comply-logs/tanium/comply/` (adjust path if you used a different bucket name or path).
     * **Source deletion options** : Select deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Access Key ID** : User access key with access to the S3 bucket (from the read-only user created above).
     * **Secret Access Key** : User secret key with access to the S3 bucket (from the read-only user created above).
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  8. Click **Next**.
  9. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



## UDM Mapping Table

Log field | UDM mapping | Logic  
---|---|---  
Computer Name | entity.entity.asset.hostname | Directly mapped from "Computer Name" field after replacing spaces with underscores.  
CVE | entity.entity.asset.vulnerabilities.cve_id | Directly mapped from "CVE" field.  
CVSS v3 Score | entity.entity.asset.vulnerabilities.cvss_base_score | Directly mapped from "CVSS v3 Score" field after renaming to cvss_base_score.  
CVSS v3 Severity | entity.entity.asset.vulnerabilities.severity_details | Directly mapped from "CVSS v3 Severity" field.  
CVSS v3 Vector | entity.entity.asset.vulnerabilities.cvss_vector | Directly mapped from "CVSS v3 Vector" field.  
First Found Date | entity.entity.asset.vulnerabilities.first_found | Parsed from "First Found Date" field and converted to RFC 3339 UTC format. If the date contains "-", it's appended with "T00:00:00Z". Otherwise, the date is extracted using grok and then converted.  
IP Address | entity.entity.asset.ip | Each IP address from the "IP Address" array is mapped to a separate "ip" field in the UDM.  
Last Found Date | entity.entity.asset.vulnerabilities.last_found | Parsed from "Last Found Date" field and converted to RFC 3339 UTC format. If the date contains "-", it's appended with "T00:00:00Z". Otherwise, the date is extracted using grok and then converted.  
Title | entity.entity.asset.vulnerabilities.name | Directly mapped from "Title" field.  
collection_time.nanos | entity.metadata.collected_timestamp.nanos | Directly mapped from the "collection_time.nanos" field.  
collection_time.seconds | entity.metadata.collected_timestamp.seconds | Directly mapped from the "collection_time.seconds" field.  
time | entity.metadata.interval.start_time | Parsed from "time" field and converted to RFC 3339 UTC format.  
- | entity.metadata.entity_type | Set to "ASSET".  
- | entity.metadata.product_entity_id | Set to "Tanium: " concatenated with the value of the "computerName" field.  
- | entity.metadata.product_name | Set to "Comply".  
- | entity.metadata.vendor_name | Set to "Tanium".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-comply-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
