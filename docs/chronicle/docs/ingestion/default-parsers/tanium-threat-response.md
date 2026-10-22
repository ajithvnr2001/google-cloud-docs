---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-threat-response/
title: Collect Tanium Threat Response logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:09.183099+00:00
---

# Collect Tanium Threat Response logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-threat-response/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Tanium Threat Response logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Tanium Threat Response logs to Google Security Operations using Tanium Connect's native AWS S3 export functionality. Tanium Threat Response produces threat detection alerts, investigation findings, and incident response data in JSON format, which can be directly exported to S3 using Tanium Connect without requiring custom Lambda functions. The parser transforms raw JSON data from Tanium Threat Response into a unified data model (UDM). It first attempts to parse the incoming message as JSON, handles potential errors, and then extracts and maps relevant fields to the UDM structure, including details about the affected host, user, process, network activity, and security findings. 

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * **Tanium Core Platform** 7.0 or later
  * **Tanium Threat Response** module installed and configured
  * **Tanium Connect** module installed with valid license
  * **Tanium Direct Connect** 1.9.30 or later for investigation capabilities
  * Privileged access to **Tanium Console** with administrative rights
  * Privileged access to **AWS** (S3, IAM)



## Configure Tanium Threat Response service account

  1. Sign in to the **Tanium Console**.
  2. Go to **Modules > Threat Response**.
  3. Click **Settings** at the top right.
  4. In the **Service Account** section, configure the following: 
     * **Service Account User** : Select a user with appropriate Threat Response permissions.
     * **Verify** the account has Connect User role privilege.
     * **Confirm** access to Threat Response alerts and investigation data.
  5. Click **Save** to apply the service account configuration.



## Collect Tanium Threat Response prerequisites

  1. Sign in to the **Tanium Console** as an administrator.
  2. Go to **Administration > Permissions > Users**.
  3. Create or identify a service account user with the following roles: 
     * **Threat Response Administrator** or **Threat Response Read Only User** role.
     * **Connect User** role privilege.
     * Access to monitored computer groups (recommended: **All Computers** group).
     * **Read Saved Question** permission for Threat Response content sets.

**Note:** The service account credentials are used internally by Tanium Connect to authenticate and retrieve Threat Response alerts and investigation data. These credentials are configured during the Tanium Connect source setup within the Tanium Console interface.

## Configure AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save bucket **Name** and **Region** for future reference (for example, `tanium-threat-response-logs`).
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



## Configure Tanium Connect AWS S3 destination

  1. Sign in to the **Tanium Console**.
  2. Go to **Modules > Connect**.
  3. Click **Create Connection**.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Threat Response Alerts to S3 for SecOps`).
     * **Description** : Optional description (for example, `Export threat detection alerts and investigation findings to AWS S3 for Google SecOps ingestion`).
     * **Enable** : Select to enable the connection to run on schedule.
  5. Click **Next**.



### Configure the connection source

  1. In the **Source** section, provide the following configuration details: 
     * **Source Type** : Select **Saved Question**.
     * **Saved Question** : Select one of the following Threat Response-related saved questions: 
       * **Threat Response - Alerts** for threat detection alerts.
       * **Threat Response - Investigation Results** for investigation findings.
       * **Threat Response - Intel Matches** for threat intelligence matches.
       * **Threat Response - Endpoint Activity** for suspicious endpoint activity.
       * **Threat Response - Network Connections** for network-based threats.
     * **Computer Group** : Select **All Computers** or specific computer groups to monitor.
     * **Refresh Interval** : Set appropriate interval for data collection (for example, **10 minutes** for threat alerts).
  2. Click **Next**.



### Configure AWS S3 destination

  1. In the **Destination** section, provide the following configuration details: 
     * **Destination Type** : Select **AWS S3**.
     * **Destination Name** : Enter a unique name (for example, `Google SecOps ThreatResponse S3 Destination`).
     * **AWS Access Key** : Enter the AWS access key from the CSV file downloaded in the AWS S3 configuration step.
     * **AWS Secret Access Key** : Enter the AWS secret access key from the CSV file downloaded in the AWS S3 configuration step.
     * **Bucket Name** : Enter your S3 bucket name (for example, `tanium-threat-response-logs`).
     * **Region** : Select the AWS region where your S3 bucket is located.
     * **Key Prefix** : Enter a prefix for the S3 objects (for example, `tanium/threat-response/`).
  2. Click **Next**.



### Configure filters

  1. In the **Filters** section, configure data filtering options: 
     * **Send new items only** : Select this option to send only new threat alerts since the last export.
     * **Column filters** : Add filters based on specific alert attributes if needed (for example, filter by alert severity, threat type, or investigation status).
  2. Click **Next**.



### Format data for AWS S3

  1. In the **Format** section, configure the data format: 
     * **Format** : Select **JSON**.
     * **Options** : 
       * **Include headers** : Deselect to avoid headers in JSON output.
       * **Include empty cells** : Select based on your preference.
     * **Advanced Options** : 
       * **File naming** : Use default timestamp-based naming.
       * **Compression** : Select **Gzip** to reduce storage costs and transfer time.
  2. Click **Next**.



### Schedule the connection

  1. In the **Schedule** section, configure the export schedule: 
     * **Enable schedule** : Select to enable automatic scheduled exports.
     * **Schedule type** : Select **Recurring**.
     * **Frequency** : Select **Every 10 minutes** for timely threat response alerts.
     * **Start time** : Set appropriate start time for the first export.
  2. Click **Next**.



### Save and verify connection

  1. Review the connection configuration in the summary screen.
  2. Click **Save** to create the connection.
  3. Click **Test Connection** to verify the configuration.
  4. If the test is successful, click **Run Now** to perform an initial export.
  5. Monitor the connection status in the **Connect Overview** page.



## Configure a feed in Google SecOps to ingest Tanium Threat Response logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **\+ Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `Tanium Threat Response logs`).
  4. Select **Amazon S3 V2** as the **Source type**.
  5. Select **Tanium Threat Response** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters: 
     * **S3 URI** : `s3://tanium-threat-response-logs/tanium/threat-response/`
     * **Source deletion options** : Select deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label applied to the events from this feed.
  8. Click **Next**.
  9. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



## UDM Mapping Table

Log field | UDM mapping | Logic  
---|---|---  
Alert Id | security_result.rule_instance | The value of this field is taken from the "Alert Id" field in the raw log.  
Computer IP | principal.ip | The value of this field is taken from the "Computer IP" field in the raw log.  
Computer IP | target.ip | The value of this field is taken from the "Computer IP" field in the raw log.  
Computer Name | principal.hostname | The value of this field is taken from the "Computer Name" field in the raw log.  
Computer Name | target.hostname | The value of this field is taken from the "Computer Name" field in the raw log.  
id | target.resource.attribute.labels | The value of this field is taken from the "id" field in the raw log. The key is hardcoded to "id".  
Intel Id | security_result.rule_id | The value of this field is taken from the "Intel Id" field in the raw log.  
Intel Labels | security_result.description | The value of this field is taken from the "Intel Labels" field in the raw log.  
Intel Name | security_result.summary | The value of this field is taken from the "Intel Name" field in the raw log.  
Intel Name | security_result.threat_name | The value of this field is taken from the "Intel Name" field in the raw log.  
Intel Type | security_result.rule_type | The value of this field is taken from the "Intel Type" field in the raw log.  
MatchDetails.finding.system_info.bits | principal.asset.platform_software.bits | The value of this field is taken from the "MatchDetails.finding.system_info.bits" field in the raw log.  
MatchDetails.finding.system_info.os | principal.asset.platform_software.platform_version | The value of this field is taken from the "MatchDetails.finding.system_info.os" field in the raw log.  
MatchDetails.finding.system_info.patch_level | principal.asset.platform_software.platform_patch_level | The value of this field is taken from the "MatchDetails.finding.system_info.patch_level" field in the raw log.  
MatchDetails.finding.system_info.platform | principal.asset.platform_software.platform | The value of this field is taken from the "MatchDetails.finding.system_info.platform" field in the raw log.  
MatchDetails.match.contexts.0.event.registrySet.keyPath | target.registry.registry_key | The value of this field is taken from the "MatchDetails.match.contexts.0.event.registrySet.keyPath" field in the raw log.  
MatchDetails.match.contexts.0.event.registrySet.valueName | target.registry.registry_value_name | The value of this field is taken from the "MatchDetails.match.contexts.0.event.registrySet.valueName" field in the raw log.  
MatchDetails.match.properties.args | security_result.about.process.command_line | The value of this field is taken from the "MatchDetails.match.properties.args" field in the raw log.  
MatchDetails.match.properties.file.fullpath | target.process.file.full_path | The value of this field is taken from the "MatchDetails.match.properties.file.fullpath" field in the raw log.  
MatchDetails.match.properties.file.md5 | target.process.file.md5 | The value of this field is taken from the "MatchDetails.match.properties.file.md5" field in the raw log.  
MatchDetails.match.properties.file.sha1 | target.process.file.sha1 | The value of this field is taken from the "MatchDetails.match.properties.file.sha1" field in the raw log.  
MatchDetails.match.properties.file.sha256 | target.process.file.sha256 | The value of this field is taken from the "MatchDetails.match.properties.file.sha256" field in the raw log.  
MatchDetails.match.properties.fullpath | target.process.file.full_path | The value of this field is taken from the "MatchDetails.match.properties.fullpath" field in the raw log.  
MatchDetails.match.properties.local_port | principal.port | The value of this field is taken from the "MatchDetails.match.properties.local_port" field in the raw log.  
MatchDetails.match.properties.md5 | target.process.file.md5 | The value of this field is taken from the "MatchDetails.match.properties.md5" field in the raw log.  
MatchDetails.match.properties.parent.args | security_result.about.process.command_line | The value of this field is taken from the "MatchDetails.match.properties.parent.args" field in the raw log.  
MatchDetails.match.properties.parent.file.fullpath | target.process.parent_process.file.full_path | The value of this field is taken from the "MatchDetails.match.properties.parent.file.fullpath" field in the raw log.  
MatchDetails.match.properties.parent.file.md5 | target.process.parent_process.file.md5 | The value of this field is taken from the "MatchDetails.match.properties.parent.file.md5" field in the raw log.  
MatchDetails.match.properties.parent.parent.file.fullpath | target.process.parent_process.parent_process.file.full_path | The value of this field is taken from the "MatchDetails.match.properties.parent.parent.file.fullpath" field in the raw log.  
MatchDetails.match.properties.parent.parent.file.md5 | target.process.parent_process.parent_process.file.md5 | The value of this field is taken from the "MatchDetails.match.properties.parent.parent.file.md5" field in the raw log.  
MatchDetails.match.properties.parent.parent.parent.file.fullpath | target.process.parent_process.parent_process.parent_process.file.full_path | The value of this field is taken from the "MatchDetails.match.properties.parent.parent.parent.file.fullpath" field in the raw log.  
MatchDetails.match.properties.parent.parent.parent.file.md5 | target.process.parent_process.parent_process.parent_process.file.md5 | The value of this field is taken from the "MatchDetails.match.properties.parent.parent.parent.file.md5" field in the raw log.  
MatchDetails.match.properties.parent.parent.parent.parent.file.fullpath | target.process.parent_process.parent_process.parent_process.parent_process.file.full_path | The value of this field is taken from the "MatchDetails.match.properties.parent.parent.parent.parent.file.fullpath" field in the raw log.  
MatchDetails.match.properties.parent.parent.parent.parent.file.md5 | target.process.parent_process.parent_process.parent_process.parent_process.file.md5 | The value of this field is taken from the "MatchDetails.match.properties.parent.parent.parent.parent.file.md5" field in the raw log.  
MatchDetails.match.properties.parent.parent.parent.parent.parent.file.fullpath | target.process.parent_process.parent_process.parent_process.parent_process.parent_process.file.full_path | The value of this field is taken from the "MatchDetails.match.properties.parent.parent.parent.parent.parent.file.fullpath" field in the raw log.  
MatchDetails.match.properties.parent.parent.parent.parent.parent.file.md5 | target.process.parent_process.parent_process.parent_process.parent_process.parent_process.file.md5 | The value of this field is taken from the "MatchDetails.match.properties.parent.parent.parent.parent.parent.file.md5" field in the raw log.  
MatchDetails.match.properties.parent.pid | target.process.parent_process.pid | The value of this field is taken from the "MatchDetails.match.properties.parent.pid" field in the raw log.  
MatchDetails.match.properties.parent.parent.pid | target.process.parent_process.parent_process.pid | The value of this field is taken from the "MatchDetails.match.properties.parent.parent.pid" field in the raw log.  
MatchDetails.match.properties.parent.parent.parent.pid | target.process.parent_process.parent_process.parent_process.pid | The value of this field is taken from the "MatchDetails.match.properties.parent.parent.parent.pid" field in the raw log.  
MatchDetails.match.properties.parent.parent.parent.parent.pid | target.process.parent_process.parent_process.parent_process.parent_process.pid | The value of this field is taken from the "MatchDetails.match.properties.parent.parent.parent.parent.pid" field in the raw log.  
MatchDetails.match.properties.parent.parent.parent.parent.parent.pid | target.process.parent_process.parent_process.parent_process.parent_process.parent_process.pid | The value of this field is taken from the "MatchDetails.match.properties.parent.parent.parent.parent.parent.pid" field in the raw log.  
MatchDetails.match.properties.pid | target.process.pid | The value of this field is taken from the "MatchDetails.match.properties.pid" field in the raw log.  
MatchDetails.match.properties.protocol | network.ip_protocol | The value of this field is taken from the "MatchDetails.match.properties.protocol" field in the raw log.  
MatchDetails.match.properties.remote_ip | target.ip | The value of this field is taken from the "MatchDetails.match.properties.remote_ip" field in the raw log.  
MatchDetails.match.properties.remote_port | target.port | The value of this field is taken from the "MatchDetails.match.properties.remote_port" field in the raw log.  
MatchDetails.match.properties.sha1 | target.process.file.sha1 | The value of this field is taken from the "MatchDetails.match.properties.sha1" field in the raw log.  
MatchDetails.match.properties.sha256 | target.process.file.sha256 | The value of this field is taken from the "MatchDetails.match.properties.sha256" field in the raw log.  
MatchDetails.match.properties.user | target.administrative_domain | The domain name is extracted from the "MatchDetails.match.properties.user" field in the raw log by looking for a backslash character (""). The characters before the backslash are considered as the domain name.  
MatchDetails.match.properties.user | target.user.userid | The username is extracted from the "MatchDetails.match.properties.user" field in the raw log by looking for a backslash character (""). The characters after the backslash are considered as the username.  
MITRE Techniques | security_result.threat_id | The value of this field is taken from the "MITRE Techniques" field in the raw log.  
params | security_result.detection_fields | The value of this field is taken from the "params" field in the raw log. The key is hardcoded to "params_" concatenated with the index of the parameter.  
Timestamp | metadata.event_timestamp | The value of this field is taken from the "Timestamp" field in the raw log.  
N/A | is_alert | This field is hardcoded to "true" if the "Computer IP" field in the raw log is not empty.  
N/A | metadata.log_type | This field is hardcoded to "TANIUM_THREAT_RESPONSE".  
N/A | metadata.product_event_type | This field is hardcoded to "Tanium Signal".  
N/A | metadata.product_name | This field is hardcoded to "Threat Response".  
N/A | metadata.vendor_name | This field is hardcoded to "Tanium".  
N/A | network.http.method | This field is hardcoded to "POST" if the value of the "method" field in the raw log is "submit".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-threat-response-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
