---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-security-cloud/
title: Collect Jamf Security Cloud logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:34.682265+00:00
---

# Collect Jamf Security Cloud logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-security-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Jamf Security Cloud logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Jamf Security Cloud logs into Google Security Operations using Google Cloud Storage or Amazon S3. Jamf Security Cloud is a mobile threat defense and endpoint security platform for Apple devices. It generates threat detection, compliance, and device security event logs covering DNS-layer protection, phishing prevention, content filtering, and device risk assessment. Jamf Security Cloud exports logs using Data Streams. Each data stream configuration sends exactly one data type to one destination.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the **Jamf Security Cloud** portal
  * For Method 1: privileged access to **Google Cloud** (Google Cloud Storage, Cloud Run)
  * For Method 2: privileged access to **AWS** (S3, IAM)

**Note:** Only a **Super Admin** can enable the **Network traffic** , **Device data** , and **App insights** data streams. If **Data Streams** is not available in your Jamf Security Cloud portal, contact Jamf Support to enable the feature.

## Select data stream types to export

The Jamf Security Cloud parser supports all six data stream types. Create a separate data stream configuration for each data type that you want to ingest:

  * **Threat events** : detected threat events, including malicious network communications, malware, and risky apps
  * **Network traffic** : network traffic logs processed by Jamf's network infrastructure
  * **Access events** : allowed and denied requests from Jamf Connect Zero Trust Network Access (ZTNA) policies
  * **Device data** : information about devices
  * **App insights** : information about applications installed on devices
  * **Vulnerability data** : details about each discovered vulnerability and the device where it was found



## Method 1: Google Cloud Storage

Jamf Security Cloud has no built-in Google Cloud Storage destination, and Jamf notes that sending data directly to Google SecOps using the HTTP integration is not supported. This method uses the **Generic HTTP** data stream target to send events to a Cloud Run function that you own, which writes them to a Google Cloud Storage bucket. Google SecOps then ingests the bucket using a Google Cloud Storage V2 feed.

### Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `jamf-security-cloud-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




### Create a service account for the Cloud Run function

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `jamf-sc-receiver-sa`
     * **Service account description** : Enter `Service account for the Cloud Run function that receives Jamf Security Cloud events`
  4. Click **Create and Continue**.
  5. Click **Done**.



### Grant the service account access to the bucket

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `jamf-sc-receiver-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



### Create the Cloud Run function to receive events

  1. Generate a strong authentication token and save it for future reference, (for example, run `openssl rand -hex 32`). Jamf Security Cloud sends this token in a request header, and the function rejects requests without it.
  2. In the **GCP Console** , go to **Cloud Run**.
  3. Click **Create service**.
  4. Select **Function** (use an inline editor to create a function).
  5. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `jamf-sc-receiver`  
**Region** | Select the region matching your Cloud Storage bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  6. In the **Authentication** section, select **Allow unauthenticated invocations**.

**Note:** Jamf Security Cloud cannot authenticate with Identity and Access Management (IAM). Access is protected by the authentication token that the function verifies on every request.
  7. Expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `jamf-sc-receiver-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `jamf-security-cloud-logs` | Cloud Storage bucket name  
`GCS_PREFIX` | `jamf-security-cloud/` | Prefix for log files  
`AUTH_TOKEN` | `<your-generated-token>` | Token that Jamf Security Cloud sends in the `X-Auth-Token` header  
  10. Click **Create**.

  11. Wait for the service to be created. After the service is created, the **inline code editor** opens automatically.

  12. Enter **main** in the **Entry point** field.

  13. In the inline code editor, create two files:

     * **First file: main.py**
           
           import hashlib
           import os
           from datetime import datetime, timezone
           
           import functions_framework
           from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
           
           BUCKET = os.environ["GCS_BUCKET"]
           PREFIX = os.environ.get("GCS_PREFIX", "jamf-security-cloud/")
           AUTH_TOKEN = os.environ["AUTH_TOKEN"]
           
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           @functions_framework.http
           def main(request):
                   if request.headers.get("X-Auth-Token") != AUTH_TOKEN:
                           return ("Unauthorized", 401)
           
                   body = request.get_data()
                   if not body:
                           return ("OK", 200)
           
                   now = datetime.now(timezone.utc)
                   digest = hashlib.sha256(body).hexdigest()[:12]
                   object_name = f"{PREFIX}{now:%Y/%m/%d}/{now:%Y%m%dT%H%M%S%f}_{digest}.json"
                   storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(BUCKET).blob(object_name).[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                           body, content_type="application/json"
                   )
                   return ("OK", 200)
           

     * **Second file: requirements.txt**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           

  14. Click **Save and redeploy**.

  15. Copy and save the service **URL** (for example, `https://jamf-sc-receiver-abc123-uc.a.run.app`). You'll use the hostname in the next section.




### Configure a generic HTTP data stream in Jamf Security Cloud

  1. Sign in to the **Jamf Security Cloud** portal.
  2. Go to **Integrations > Data Streams**.
  3. Click **New configuration**.
  4. Select the data stream type (for example, **Threat events**).
  5. Select **Generic HTTP** as the data stream target type.
  6. Click **Continue**.
  7. Provide the following configuration details: 
     * **Protocol** : Select **https**
     * **Server Hostname/IP** : Enter the Cloud Run service hostname (for example, `jamf-sc-receiver-abc123-uc.a.run.app`)
     * **Port** : Enter `443`
     * **Endpoint** : Enter `/`
     * **Additional Headers** : Click **Add header** and enter the name `X-Auth-Token` with your generated token as the value
  8. Click **Test Configuration** and verify that the test succeeds.
  9. Click the **Enable configuration** toggle to activate the data stream.
  10. Click **Save**.
  11. Repeat these steps for each additional data stream type that you want to export.

**Note:** Only new events are exported after the stream is enabled. You cannot export historical events. The parser safely discards the test message that Jamf Security Cloud sends during configuration validation.

### Retrieve the Google SecOps service account

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Feeds**.
  3. Click **Add New Feed**.
  4. Click **Configure a single feed**.
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **JAMF Security Cloud** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You'll use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.



### Grant the Google SecOps service account access to the bucket

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

**Note:** If you plan to use the deletion option (delete transferred files), grant the **Storage Object Admin** role instead of Storage Object Viewer.



### Configure a feed in Google SecOps to ingest from Google Cloud Storage

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Jamf Security Cloud logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **JAMF Security Cloud** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

Field | Value  
---|---  
**Storage bucket URI** | `gs://jamf-security-cloud-logs/jamf-security-cloud/`  
**Source Deletion Option** | Select the deletion option according to your preference  
**Maximum File Age (Days)** | Default is 180 days  
**Asset namespace** | The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)  
**Ingestion labels** | The label to be applied to the events from this feed  
     * Replace `jamf-security-cloud-logs` with your actual bucket name.
     * Always include the trailing slash (`/`) at the end of the URI.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Method 2: Amazon S3

**Customer-owned AWS S3** is the only cloud storage destination that Jamf Security Cloud Data Streams supports natively. Jamf Security Cloud writes events directly to your S3 bucket, and Google SecOps ingests them using an Amazon S3 V2 feed.

**Note:** Jamf recommends Amazon S3 for low traffic data streams, such as threat events, and supports one AWS bucket per customer.

### Configure AWS S3 bucket and IAM role for Jamf Security Cloud

  1. Create an **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save the bucket **Name** and **Region** for future reference (for example, `jamf-security-cloud-logs`).
  3. Create an **IAM role** that Jamf Security Cloud assumes to upload data to the bucket. The role requires the `s3:PutObject` permission on the bucket and Jamf's AWS account listed as a trusted entity.

**Note:** Jamf provides the **JamfDataCloudFormation.prod.yaml** CloudFormation template that creates the S3 bucket and the IAM role automatically. You can download the template from the [Jamf documentation](https://learn.jamf.com/r/en-US/jamf-protect-documentation/Configuring_the_Threat_Events_Stream_to_Send_Events_to_Customer_Owned_AWS_S3).
  4. Save the IAM role `ARN` for future reference.




### Configure a customer-owned AWS S3 data stream in Jamf Security Cloud

  1. Sign in to the **Jamf Security Cloud** portal.
  2. Go to **Integrations > Data Streams**.
  3. Click **New configuration**.
  4. Select the data stream type (for example, **Threat events**).
  5. Select **Customer-owned AWS S3** as the data stream target type.
  6. Click **Continue**.
  7. Provide the following configuration details: 
     * **Amazon S3 bucket name** : Enter the bucket name (for example, `jamf-security-cloud-logs`)
     * **IAM role assumed by Jamf** : Enter the ARN of the IAM role you created for Jamf Security Cloud
     * **Region** : Select the region of your S3 bucket
  8. Click **Create configuration**.
  9. Optional: In **Advanced settings** , select **JSON** as the message format.

**Note:** JSON is the default message format. Do not select **CEF**. the Jamf Security Cloud parser processes JSON messages only. Vulnerability data is always sent as JSON.
  10. Click the **Enable configuration** toggle to activate the data stream.

  11. Click **Save**.

  12. Repeat these steps for each additional data stream type that you want to export.


**Note:** Only new events are exported after the stream is enabled. You cannot export historical events.

### Create an IAM user and access key for Google SecOps

  1. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  2. Select the created **User**.
  3. Select the **Security credentials** tab.
  4. Click **Create Access Key** in the **Access Keys** section.
  5. Select **Third-party service** as the **Use case**.
  6. Click **Next**.
  7. Optional: Add a description tag.
  8. Click **Create access key**.
  9. Click **Download .csv file** to save the **Access Key** and **Secret Access Key** for future reference.
  10. Click **Done**.
  11. Select the **Permissions** tab.
  12. Click **Add permissions** in the **Permissions policies** section.
  13. Select **Add permissions**.
  14. Select **Attach policies directly**.
  15. Search for the **AmazonS3FullAccess** policy.
  16. Select the policy.
  17. Click **Next**.
  18. Click **Add permissions**.



### Configure a feed in Google SecOps to ingest from Amazon S3

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Jamf Security Cloud logs`).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **JAMF Security Cloud** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

Field | Value  
---|---  
**S3 URI** | `s3://jamf-security-cloud-logs/`  
**Source deletion option** | Select the deletion option according to your preference  
**Maximum File Age (Days)** | Default is 180 days  
**Access Key ID** | User access key with access to the S3 bucket  
**Secret Access Key** | User secret key with access to the S3 bucket  
**Asset namespace** | The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)  
**Ingestion labels** | The label to be applied to the events from this feed  
     * Replace `jamf-security-cloud-logs` with your actual S3 bucket name.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`accessPoint_label` | `additional.fields` | Merged  
`action_label` | `additional.fields` | Merged  
`activated_label` | `additional.fields` | Merged  
`alertId_label` | `additional.fields` | Merged  
`appName_label` | `additional.fields` | Merged  
`appRiskIndexThreshold_label` | `additional.fields` | Merged  
`appVersion_label` | `additional.fields` | Merged  
`app_id_label` | `additional.fields` | Merged  
`carrierName_label` | `additional.fields` | Merged  
`category_label` | `additional.fields` | Merged  
`deploymentState_label` | `additional.fields` | Merged  
`developer_label` | `additional.fields` | Merged  
`deviceId_label` | `additional.fields` | Merged  
`deviceModel_label` | `additional.fields` | Merged  
`deviceName_label` | `additional.fields` | Merged  
`deviceRiskIndex_label` | `additional.fields` | Merged  
`device_os_label` | `additional.fields` | Merged  
`device_user_name_label` | `additional.fields` | Merged  
`eventTimeUtcMs_label` | `additional.fields` | Merged  
`eventType_label` | `additional.fields` | Merged  
`hwPlatform_label` | `additional.fields` | Merged  
`imei_label` | `additional.fields` | Merged  
`installationTimeUtcMs_label` | `additional.fields` | Merged  
`installedBy_label` | `additional.fields` | Merged  
`isoCountryCode_label` | `additional.fields` | Merged  
`lastMdmCheckInUtcMs_label` | `additional.fields` | Merged  
`lastNetworkTrafficUtcMs_label` | `additional.fields` | Merged  
`lastUpdatedUtcMs_label` | `additional.fields` | Merged  
`loc_isoCountryCode_label` | `additional.fields` | Merged  
`mcc_label` | `additional.fields` | Merged  
`mdmId_label` | `additional.fields` | Merged  
`mnc_label` | `additional.fields` | Merged  
`osVersion_label` | `additional.fields` | Merged  
`packageName_label` | `additional.fields` | Merged  
`parentId_label` | `additional.fields` | Merged  
`parentId_label_1` | `additional.fields` | Merged  
`platform_label` | `additional.fields` | Merged  
`profileId_label` | `additional.fields` | Merged  
`profileName_label` | `additional.fields` | Merged  
`profileStatus_label` | `additional.fields` | Merged  
`recordType_label` | `additional.fields` | Merged  
`resellerId_label` | `additional.fields` | Merged  
`routeName_label` | `additional.fields` | Merged  
`signatureId_id_label` | `additional.fields` | Merged  
`signatureId_name_label` | `additional.fields` | Merged  
`softwareId_label` | `additional.fields` | Merged  
`softwareName_label` | `additional.fields` | Merged  
`softwareVersion_label` | `additional.fields` | Merged  
`ssid_label` | `additional.fields` | Merged  
`system_label` | `additional.fields` | Merged  
`threat_result_label` | `additional.fields` | Merged  
`triggerTimeUtcMs_label` | `additional.fields` | Merged  
`triggerType_label` | `additional.fields` | Merged  
`types_list` | `additional.fields` | Merged  
`userId_label` | `additional.fields` | Merged  
`user_tld_label` | `additional.fields` | Merged  
`vpnActive_label` | `additional.fields` | Merged  
`wanderaAppVersion_label` | `additional.fields` | Merged  
`wifiActive_label` | `additional.fields` | Merged  
`event_data.receiptTime` | `metadata.collected_timestamp` | Directly mapped  
`event_data.cve.description` | `metadata.description` | Directly mapped  
`event_data_event_dataType_description` | `metadata.description` | Directly mapped  
`event_data.timestamp` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSSZ`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`event_data.md1.product` | `metadata.product_event_type` | Directly mapped  
`md1.product` | `metadata.product_event_type` | Directly mapped  
`event_data.device.externalId` | `metadata.product_log_id` | Directly mapped  
`event_data.externalId` | `metadata.product_log_id` | Directly mapped  
`md1.product` | `metadata.product_name` | Directly mapped  
`event_data.md1.schemaVersion` | `metadata.product_version` | Directly mapped  
`schemaVersion` | `metadata.product_version` | Directly mapped  
`dns_answers` | `network.dns.answers` | Merged  
`dns_questions` | `network.dns.questions` | Merged  
`event_data.domain` | `principal.administrative_domain` | Directly mapped  
`event_data.application` | `principal.application` | Directly mapped  
`event_data.hostName` | `principal.asset.hostname` | Directly mapped  
`event_data.source.ip` | `principal.asset.ip` | Merged  
`event_data.device.userDeviceName` | `principal.hostname` | Directly mapped  
`event_data.hostName` | `principal.hostname` | Directly mapped  
`event_data.source.ip` | `principal.ip` | Merged  
`event_data.source.port` | `principal.port` | Renamed/mapped  
`event_data_event_dataType_id` | `principal.process.pid` | Directly mapped  
`event_data.cve.consoleUrl` | `principal.url` | Directly mapped  
`event_data.event_dataUrl` | `principal.url` | Directly mapped  
`device.user.email` | `principal.user.email_addresses` | Merged  
`event_data.user.userEmail` | `principal.user.email_addresses` | Merged  
`event_data.account.name` | `principal.user.user_display_name` | Directly mapped  
`event_data.user.userName` | `principal.user.user_display_name` | Directly mapped  
`customer.customerId` | `principal.user.userid` | Directly mapped  
`customerId` | `principal.user.userid` | Directly mapped  
`device.user.email` | `principal.user.userid` | Directly mapped  
`event_data.account.customerId` | `principal.user.userid` | Directly mapped  
`event_data.customerId` | `principal.user.userid` | Directly mapped  
`actionforBlocked` | `security_result.action` | Merged  
`event_data_event_dataType_name` | `security_result.description` | Directly mapped  
`attribution_label` | `security_result.detection_fields` | Merged  
`baseScore_label` | `security_result.detection_fields` | Merged  
`cve_id_label` | `security_result.detection_fields` | Merged  
`exploitAvailable_label` | `security_result.detection_fields` | Merged  
`permission_label` | `security_result.detection_fields` | Merged  
`threats_label` | `security_result.detection_fields` | Merged  
`event_data.cve.severity` | `security_result.severity` | Directly mapped  
`event_data.blockReason` | `security_result.summary` | Directly mapped  
`event_data.cve.cveDetailUrl` | `security_result.url_back_to_product` | Directly mapped  
`event_data.device.deviceId` | `target.asset.asset_id` | Directly mapped  
`event_data.destination.name` | `target.asset.hostname` | Directly mapped  
`device.carrier.ipAddress` | `target.asset.ip` | Merged  
`device.network.assignedIp` | `target.asset.ip` | Merged  
`device.network.publicIp` | `target.asset.ip` | Merged  
`event_data.destination.ip` | `target.asset.ip` | Merged  
`event_data.destinationIp` | `target.asset.ip` | Merged  
`ip` | `target.asset.ip` | Merged  
`app_id_md5` | `target.file.md5` | Directly mapped  
`app_id_sha1` | `target.file.sha1` | Directly mapped  
`app_id_sha256` | `target.file.sha256` | Directly mapped  
`event_data.destination.name` | `target.hostname` | Directly mapped  
`device.carrier.ipAddress` | `target.ip` | Merged  
`device.network.assignedIp` | `target.ip` | Merged  
`device.network.publicIp` | `target.ip` | Merged  
`event_data.destination.ip` | `target.ip` | Merged  
`event_data.destinationIp` | `target.ip` | Merged  
`ip` | `target.ip` | Merged  
`device.location.countryName` | `target.location.country_or_region` | Directly mapped  
`event_data.location` | `target.location.name` | Directly mapped  
`device.hw.wifiMacAddress` | `target.mac` | Merged  
`device.network.bssid` | `target.mac` | Merged  
`event_data.accessPointBssid` | `target.mac` | Merged  
`event_data_device_os_osVersion` | `target.platform_version` | Directly mapped  
`event_data.destination.port` | `target.port` | Renamed/mapped  
`event_data.device.deviceName` | `target.resource.name` | Directly mapped  
`event_data.user.email` | `target.user.email_addresses` | Merged  
`event_data.user.email` | `target.user.userid` | Directly mapped  
`event_data.user.name` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `STATUS_UPDATE`  
N/A | `metadata.product_name` | Constant: `JAMF_SECURITY_CLOUD`  
N/A | `metadata.vendor_name` | Constant: `JAMF_SECURITY_CLOUD`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
N/A | `target.platform` | Constant: `WINDOWS`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-security-cloud-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
