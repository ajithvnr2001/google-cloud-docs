---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-discover/
title: Collect Tanium Discover logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:30:40.675395+00:00
---

# Collect Tanium Discover logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-discover/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Tanium Discover logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Tanium Discover logs to Google Security Operations using Amazon S3 using Tanium Connect's native S3 export capability. Tanium Discover automatically discovers network interfaces and assets across your environment, providing visibility into managed and unmanaged endpoints, network devices, and other connected systems. The parser extracts fields from the JSON logs, transforms specific fields like MAC addresses and OS information, and maps them to the UDM. It handles various data types, adds metadata like vendor and product details, and merges the extracted fields into the final UDM event structure.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to **Tanium Connect** and **Tanium Console**
  * **Tanium Discover** 2.11 or later installed and configured
  * Privileged access to **AWS** (S3, IAM)



## Configure AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save bucket **Name** and **Region** for future reference (for example, `tanium-discover-logs`).
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
                 "arn:aws:s3:::tanium-discover-logs",
                 "arn:aws:s3:::tanium-discover-logs/*"
               ]
             }
           ]
         }
         

  4. Replace the following variables:

     * Change `YOUR_ACCOUNT_ID` to your AWS account ID.
     * Change `tanium-discover-logs` to your actual bucket name if different.
     * Change `tanium-connect-s3-user` to your actual IAM username if different.
  5. Click **Save**.




## Configure Tanium Connect for S3 export

  1. Sign in to the **Tanium Console** as an administrator.
  2. Go to **Tanium Connect > Connections**.
  3. Click **Create Connection**.
  4. In the **General Information** section, provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Tanium Discover to S3`).
     * **Description** : Enter a meaningful description (for example, `Export Tanium Discover interface data to S3 for Google SecOps ingestion`).
     * **Enable** : Select to enable the connection.
     * **Log Level** : Select **Information** (default) or adjust as needed.
  5. In the **Configuration** section, for **Source** , select **Tanium Discover**.
  6. Configure the Discover source settings: 
     * **Report Type** : Select the type of interfaces to export: 
       * **All** : Export all interfaces in Discover.
       * **Managed** : Export interfaces that have the Tanium Client installed.
       * **Unmanaged** : Export interfaces that do not have the Tanium Client installed.
       * **Labeled** : Export all interfaces that have a label applied.
       * **Unlabeled** : Export interfaces that do not have any labels applied.
       * **Ignored** : Export interfaces marked as ignored.
       * **Unmanageable** : Export interfaces that were marked as unmanageable.
  7. For **Destination** , select **AWS S3**.
  8. Provide the following configuration details: 
     * **Destination Name** : Enter a name (for example, `Google SecOps S3 Bucket`).
     * **AWS Access Key** : Enter the Access Key ID from the IAM user created earlier.
     * **AWS Secret Key** : Enter the Secret Access Key from the IAM user created earlier.
     * **Bucket Name** : Enter your S3 bucket name (for example, `tanium-discover-logs`).
     * **Bucket Path** : Optional. Enter a path prefix (for example, `tanium/discover/`).
     * **Region** : Select the AWS region where your bucket resides (for example, `us-east-1`).
  9. In the **Format** section, configure the output format: 
     * **Format Type** : Select **JSON**.
     * **Include Column Headers** : Select if you want column headers included.
     * **Generate Document** : Deselect this option to send raw JSON data.
  10. Optional: In the **Configure Output** section, configure filters: 
     * **Filter** : You can use filters to export specific labels. For example, if you want to export all interfaces tagged with "Lost Interface", apply a regular expression filter and type "Lost Interface" as the text to match on the Labels target column.
     * **Custom Columns** : Add any custom columns that are relevant for your use case.
  11. In the **Schedule** section, configure when the connection runs: 
     * **Schedule Type** : Select **Cron**.
     * **Cron Expression** : Enter a cron expression for regular exports (for example, `0 */6 * * *` for every 6 hours).
     * **Start Date** : Set the start date for the schedule.
  12. Click **Save Changes**.
  13. From the **Connect Overview** page, go to **Connections**.
  14. Click the connection you created (**Tanium Discover to S3**).
  15. Click **Run Now** to test the connection.
  16. Confirm that you want to run the connection.
  17. Monitor the connection status and verify that discover interface data is being exported to your S3 bucket.



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
               "Resource": "arn:aws:s3:::tanium-discover-logs/*"
             },
             {
               "Effect": "Allow",
               "Action": ["s3:ListBucket"],
               "Resource": "arn:aws:s3:::tanium-discover-logs"
             }
           ]
         }
         

  7. Set the name to `secops-reader-policy`.

  8. Go to **Create policy > search/select > Next > Add permissions**.

  9. Go to **Security credentials > Access keys > Create access key**.

  10. Download the **CSV** (these values are entered into the feed).




## Configure a feed in Google SecOps to ingest Tanium Discover logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **\+ Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `Tanium Discover logs`).
  4. Select **Amazon S3 V2** as the **Source type**.
  5. Select **Tanium Discover** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters: 
     * **S3 URI** : `s3://tanium-discover-logs/tanium/discover/` (adjust path if you used a different bucket name or path).
     * **Source deletion options** : Select deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Access Key ID** : User access key with access to the S3 bucket (from the read-only user created above).
     * **Secret Access Key** : User secret key with access to the S3 bucket (from the read-only user created above).
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  8. Click **Next**.
  9. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`CentralizedNmap` | `principal.asset.attribute.labels.key` | The value "CentralizedNmap" is assigned by the parser.  
`CentralizedNmap` | `principal.asset.attribute.labels.value` | Directly taken from the `CentralizedNmap` field in the raw log and converted to string.  
`IpAddress` | `principal.asset.ip` | Directly taken from the `IpAddress` field in the raw log.  
`IpAddress` | `principal.ip` | Directly taken from the `IpAddress` field in the raw log.  
`Labels` | `principal.asset.attribute.labels.key` | The value "Labels" is assigned by the parser.  
`Labels` | `principal.asset.attribute.labels.value` | Directly taken from the `Labels` field in the raw log.  
`MacAddress` | `principal.asset.mac` | Directly taken from the `MacAddress` field in the raw log, hyphens are replaced with colons, and the value is converted to lowercase.  
`MacAddress` | `principal.asset.product_object_id` | Concatenates "TANIUM:" with the `MacAddress` field (after converting it to lowercase and replacing hyphens with colons).  
`MacAddress` | `principal.mac` | Directly taken from the `MacAddress` field in the raw log, hyphens are replaced with colons, and the value is converted to lowercase.  
`MacOrganization` | `principal.asset.attribute.labels.key` | The value "MacOrganization" is assigned by the parser.  
`MacOrganization` | `principal.asset.attribute.labels.value` | Directly taken from the `MacOrganization` field in the raw log and converted to string.  
`Managed` | `principal.asset.attribute.labels.key` | The value "Managed" is assigned by the parser.  
`Managed` | `principal.asset.attribute.labels.value` | Directly taken from the `Managed` field in the raw log and converted to string.  
`Os` | `principal.asset.platform_software.platform` | If `Os` is "Windows", the value is set to "WINDOWS". If `Os` is "Linux", the value is set to "LINUX". Otherwise, the value is set to "UNKNOWN_PLATFORM".  
`Os` | `principal.platform` | If `Os` is "Windows", the value is set to "WINDOWS". If `Os` is "Linux", the value is set to "LINUX". Otherwise, the value is set to "UNKNOWN_PLATFORM".  
`OsGeneration` | `principal.asset.platform_software.platform_version` | Directly taken from the `OsGeneration` field in the raw log and converted to string.  
`OsGeneration` | `principal.platform_version` | Directly taken from the `OsGeneration` field in the raw log and converted to string.  
`Ports` | `principal.asset.attribute.labels.key` | The value "Ports" is assigned by the parser.  
`Ports` | `principal.asset.attribute.labels.value` | Directly taken from the `Ports` field in the raw log.  
`Profile` | `principal.asset.attribute.labels.key` | The value "Profile" is assigned by the parser.  
`Profile` | `principal.asset.attribute.labels.value` | Directly taken from the `Profile` field in the raw log.  
`TaniumComputerId` | `principal.asset.attribute.labels.key` | The value "TaniumComputerId" is assigned by the parser.  
`TaniumComputerId` | `principal.asset.attribute.labels.value` | Directly taken from the `TaniumComputerId` field in the raw log and converted to string.  
`Unmanageable` | `principal.asset.attribute.labels.key` | The value "Unmanageable" is assigned by the parser.  
`Unmanageable` | `principal.asset.attribute.labels.value` | Directly taken from the `Unmanageable` field in the raw log and converted to string. Taken from the `time` field in the raw log, parsed and converted to epoch seconds. The value "SCAN_NETWORK" is assigned by the parser. The value "TANIUM_DISCOVER" is assigned by the parser. The value "Discover" is assigned by the parser. The value "Tanium" is assigned by the parser. Directly taken from the `HostName` field in the raw log. Taken from the `time` field in the raw log, parsed and converted to epoch seconds.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-discover-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
