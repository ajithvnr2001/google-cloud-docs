---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-webproxy/
title: Collect Netskope web proxy logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:40.140460+00:00
---

# Collect Netskope web proxy logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-webproxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Netskope web proxy logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Netskope web proxy logs to Google Security Operations using Cloud Storage V2.

Netskope provides a cloud-native secure web gateway that inspects and controls web traffic in real time. Web transaction (WebTx) logs capture detailed records of every HTTP and HTTPS session processed by the Netskope proxy, including user identity, application, URL category, threat and DLP verdicts, and network metadata.

**Note:** The Netskope Cloud Exchange Log Shipper Google Chronicle plugin does **not** support WebTx logs. To ingest WebTx logs in Google SecOps, you must use one of the cloud storage-based methods described in this guide. Both options deliver WebTx logs as compressed `.gzip` files to a cloud storage bucket, which Google SecOps then reads through a Cloud Storage V2 feed.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage Cloud Storage buckets
  * Permissions to manage Identity and Access Management (IAM) policies on Cloud Storage buckets
  * Privileged access to the Netskope tenant with administrator credentials



## Option 1: Netskope Log Streaming to Cloud Storage

Use this option if you have a Netskope Log Streaming subscription enabled on your tenant. Netskope Log Streaming pushes WebTx log files directly to your Cloud Storage bucket as compressed `.gzip` files at a fixed interval of 240 seconds.

**Note:** Netskope Log Streaming is a for-fee subscription. Contact your Netskope account team to verify that Log Streaming is enabled on your tenant.

### Create a Cloud Storage bucket

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `netskope-webtx-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location closest to your organization (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




### Create a Google Cloud service account

Netskope Log Streaming requires a Google Cloud service account with write permissions to your Cloud Storage bucket. The JSON key file of this service account is used by Netskope to authenticate when pushing log files.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `netskope-log-streaming`
     * **Service account description** : Enter `Service account for Netskope Log Streaming to push WebTx logs to GCS`
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section: 
     1. Click **Select a role**.
     2. Search for and select **Storage Object Creator**.
  6. Click **Continue**.
  7. Click **Done**.



### Generate the JSON key

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**, click the service account `netskope-log-streaming`.
  2. Select the **Keys** tab.
  3. Click **Add Key > Create new key**.
  4. Select **JSON** as the key type.
  5. Click **Create**.
  6. A JSON key file downloads automatically. Save this file securely. You will paste the complete contents of this file into Netskope in the next section.

**Note:** The JSON key file can only be downloaded once. If you lose this file, you must create a new key.



### Grant write permissions on a Cloud Storage bucket

  1. In the Google Cloud console, go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `netskope-webtx-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `netskope-log-streaming@YOUR_PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Creator**
  6. Click **Save**.

**Note:** If the bucket's project is inside a VPC Service Controls perimeter, Netskope's writes arrive from outside the perimeter and are blocked until you add an ingress rule. In **Security > VPC Service Controls**, edit the perimeter and add an ingress policy with the service account email as the identity, **All sources** as the source, and **Cloud Storage API** with the `google.storage.objects.create` method as the target. Without this, stream validation fails even though the IAM grant is correct.



### Create the log stream

  1. Sign in to the **Netskope** tenant with administrator credentials.
  2. Go to **Settings > Tools > Log Streaming**.
  3. Click **Create Stream**.
  4. In the **Name** field, enter a human-readable name for the stream. For example, `Google SecOps WebTx GCS`.
  5. Select **GCP Cloud Storage** as the destination type.
  6. Provide the following configuration details:

     * **Bucket** : Enter the name of the Cloud Storage bucket (for example, `netskope-webtx-logs`).

**Note:** Follow [bucket naming conventions](https://docs.cloud.google.com/storage/docs/naming-buckets) for Cloud Storage.
       * **Path** (optional): Enter a folder path within the bucket where logs will be stored (for example, `netskope/webtx/{%Y}`).
**Note:** In Cloud Storage, paths work as object names. When you enter a path such as `netskope/webtx/{%Y}`, Cloud Storage doesn't create separate folders in the bucket. Instead, the objects are stored in one bucket and named with the path as a prefix (for example,`netskope/webtx/2026/filename`). See [object naming guidelines](https://docs.cloud.google.com/storage/docs/objects#naming) for details.
     * **Private Key** : Paste the complete contents of the JSON key file generated in the previous section, as a single JSON object starting with `{` and ending with `}`. It includes the `type`, `project_id`, `private_key_id`, `private_key`, `client_email` and `client_id` fields.

**Note:** Don't paste just the `private_key` value. Despite the field name, Netskope expects the whole service account key file; a standalone PEM key fails credential validation when you save the stream.
  7. Review the **Delivery Options** : Push frequency is an ongoing 240 seconds.

  8. Click **Save** (or **Create**) to activate the stream. Netskope validates the credentials by writing a test object named `netskope-test-file.txt` to the bucket.

**Note:** Stream activation can take up to 60 minutes from creation. After activation, Netskope pushes WebTx log files as compressed `.gzip` files to your Cloud Storage bucket every 240 seconds. These files contain the original web transaction data without modification.



### Configure a feed in Google SecOps to ingest Netskope WebTx logs from Cloud Storage

See the following steps to create the Google SecOps feed and grant IAM permissions:

#### Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your Cloud Storage bucket. You must grant this service account access to your bucket.

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Netskope WebTx Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Netskope Web Proxy** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the Cloud Storage bucket URI with the prefix path:
           
           gs://netskope-webtx-logs/netskope/webtx/
           

       * Replace: 
         * `netskope-webtx-logs`: Your Cloud Storage bucket name.
         * `netskope/webtx/`: The path prefix configured in Netskope Log Streaming (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never delete files** : Never delete files from the source (recommended for testing).
       * **Delete transferred files and empty directories** : Delete files and empty directories from the source after a successful fetch completes.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  12. Click **Next**.

  13. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




#### Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs two roles on your Cloud Storage bucket: **Storage Object Viewer** to read the log objects, and a bucket-level role to read the bucket metadata.

  1. Go to **Cloud Storage > Buckets**.
  2. click your bucket name (for example, `netskope-webtx-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email (for example, `chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com`)
     * **Assign roles** : Select both of the following: 
       * **Storage Object Viewer** : reads the log objects.
       * **Storage Legacy Bucket Reader** : reads the bucket metadata. If you selected the **Delete transferred files and empty directories** deletion option, select **Storage Legacy Bucket Writer** instead, which also grants the delete permission.
  6. Click **Save**.

**Note:** Grant both roles. **Storage Object Viewer** does not grant the bucket-level permission the feed needs, and the **Storage Legacy Bucket** roles do not grant permission to read object contents.

## Option 2: Use the Netskope Cloud Exchange Log Shipper to Cloud Storage

Use this option if you have the **Netskope Cloud Exchange** platform deployed with the **Log Shipper** module configured. The Log Shipper pulls WebTx logs from your Netskope tenant and pushes them as compressed `.gzip` files to a Cloud Storage bucket, which Google SecOps then reads through a Cloud Storage V2 feed.

**Note:** The Google Chronicle plugin for Log Shipper (v3.0.0) **does not** support WebTx ingestion. For WebTx logs, you must use a cloud storage destination plugin (Google Cloud Storage, AWS S3, or Microsoft Azure Blob Storage). These plugins push the original `.gzip` files obtained from Netskope to the cloud storage provider without decompressing or modifying the content.

### Before you begin (Cloud Exchange)

Make sure you have the following additional prerequisites for this option:

  * A Netskope Cloud Exchange tenant with the Tenant plugin and Log Shipper module already configured.
  * The Netskope CLS source plugin configured in Log Shipper (this pulls data from the Netskope tenant).
  * A Cloud Storage bucket created for storing WebTx logs. If you haven't created one, follow the steps in Create Cloud Storage bucket.
  * A Google Cloud service account with write access to the Cloud Storage bucket. If you haven't created one, follow the steps in Create a Google Cloud service account, Generate the JSON key, and Grant write permissions on aCloud Storage bucket.



### Configure the Cloud Storage destination plugin

  1. In **Cloud Exchange** , go to **Settings > Plugin Store**.
  2. Search for and select the **Google Cloud SCC (Google GCS)** plugin.
  3. Click **Configure New Plugin** (or add a new plugin configuration).
  4. Provide the following configuration details: 
     * **Configuration Name** : Enter a descriptive name (for example, `GCS WebTx Destination`).
     * **Mapping** : Select a mapping file. For WebTx logs that are pushed as original `.gzip` files, no mapping transformation is applied.
     * **Bucket** : Enter the name of the Cloud Storage bucket (for example, `netskope-webtx-logs`).
     * **Path** (optional): Enter a folder path (for example, `netskope/webtx/`).
     * **Key File** : Paste the complete contents of the service account JSON key file, not only the `private_key` value.
  5. Click **Save**.
  6. The new plugin configuration will appear on the **Log Shipper > Plugins** page.



### Configure a business rule (optional)

By default, the **All** business rule filters all alerts and events. If you want to filter WebTx logs specifically, create a new business rule:

  1. In **Log Shipper** , go to **Business Rules**.
  2. Click **Create New Rule**.
  3. Enter a **Rule Name** (for example, `WebTx Only`).
  4. Configure your filter(s) to include only WebTx data.
  5. Click **Save**.



### Configure Log Delivery

  1. In **Log Shipper** , go to **Log Delivery**.
  2. Click **Add Log Delivery Configuration**.
  3. Provide the following configuration details: 
     * **Source Configuration** : Select the Netskope CLS source plugin (for example, `WebTxCLS` or `Netskope CLS`).
     * **Destination Configuration** : Select the Cloud Storage destination plugin you configured (for example, `GCS WebTx Destination`).
     * **Business Rule** : Select a business rule (for example, `All` or `WebTx Only`).
  4. Click **Save**.

**Note:** As soon as the Log Delivery is saved, Cloud Exchange will do a historical pull for events (default period: 1 hour) and alerts (default period: 7 days).
  5. To get additional historical data, click the **Pull Historical Data** icon from the **Log Delivery** actions.

  6. Select a **Historical From** and **To** date range and click **Pull**.




### Configure a feed in Google SecOps to ingest Netskope WebTx logs from Cloud Storage

Follow the same steps as in the Netskope Log Streaming option to create a Google SecOps feed and grant IAM permissions:

  1. Retrieve the Google SecOps service account — create a feed with **Google Cloud Storage V2** as the source type and **Netskope web proxy** as the log type.
  2. Grant IAM permissions to the Google SecOps service account — grant the **Storage Object Viewer** and **Storage Legacy Bucket Reader** roles (use **Storage Legacy Bucket Writer** if using the deletion option) on the Cloud Storage bucket to the Google SecOps service account.



### Verify log delivery

To verify that WebTx logs are being delivered to the Cloud Storage bucket:

  1. In **Cloud Exchange** , go to **Log Shipper > Log Delivery**.
  2. Check the **Total Logs/WebTx Sent to External Receiver** and **Total WebTx Sent to Storage Bucket** columns to confirm that data is being pushed to the destination.
  3. In the **GCS bucket** , confirm that `.gzip` files are being written by the Log Shipper.



### Configure Log Shipper Global Settings (optional)

Only Admins can change Log Shipper Global Settings. Go to **Settings > Log Shipper**. There are two tabs: General and Mappings.

On the **General** tab, you can configure the retry strategy for log delivery:

  * **Default (3 Retries)** : In the event of a failed log delivery, Log Shipper will initiate 3 attempts to push the logs to the destination. If all 3 retry attempts fail, the corresponding batch of logs will be discarded.
  * **Retry till Successful Delivery** : Unlimited retries till successful delivery of logs.

**Note:** The "Retry till Successful Delivery" option may impact overall Cloud Exchange performance, including other Cloud Exchange modules.



You can also enable **UTF-8 encoding** for Alerts, Events, and WebTx to ensure seamless handling of UTF-8 encoded data. By default, this feature is disabled.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
applicationType | security_result.detection_fields[].key: "applicationType", security_result.detection_fields[].value: applicationType | Directly mapped from the corresponding CEF field  
appcategory | security_result.category_details[]: appcategory | Directly mapped from the corresponding CEF field  
browser | security_result.detection_fields[].key: "browser", security_result.detection_fields[].value: browser | Directly mapped from the corresponding CEF field  
c-ip | principal.asset.ip[]: c-ip, principal.ip[]: c-ip | Directly mapped from the corresponding JSON field  
cci | security_result.detection_fields[].key: "cci", security_result.detection_fields[].value: cci | Directly mapped from the corresponding CEF field  
ccl | security_result.confidence: Derived value, security_result.confidence_details: ccl | security_result.confidence is derived based on the value of ccl: "excellent" or "high" maps to HIGH_CONFIDENCE, "medium" maps to MEDIUM_CONFIDENCE, "low" or "poor" maps to LOW_CONFIDENCE, and "unknown" or "not_defined" maps to UNKNOWN_CONFIDENCE. security_result.confidence_details is directly mapped from ccl.  
clientBytes | network.sent_bytes: clientBytes | Directly mapped from the corresponding CEF field  
cs-access-method | additional.fields[].key: "accessMethod", additional.fields[].value.string_value: cs-access-method | Directly mapped from the corresponding JSON field  
cs-app | additional.fields[].key: "x-cs-app", additional.fields[].value.string_value: cs-app, principal.application: cs-app | Directly mapped from the corresponding JSON field  
cs-app-activity | additional.fields[].key: "x-cs-app-activity", additional.fields[].value.string_value: cs-app-activity | Directly mapped from the corresponding JSON field  
cs-app-category | additional.fields[].key: "x-cs-app-category", additional.fields[].value.string_value: cs-app-category | Directly mapped from the corresponding JSON field  
cs-app-cci | additional.fields[].key: "x-cs-app-cci", additional.fields[].value.string_value: cs-app-cci | Directly mapped from the corresponding JSON field  
cs-app-ccl | additional.fields[].key: "x-cs-app-ccl", additional.fields[].value.string_value: cs-app-ccl | Directly mapped from the corresponding JSON field  
cs-app-from-user | additional.fields[].key: "x-cs-app-from-user", additional.fields[].value.string_value: cs-app-from-user, principal.user.email_addresses[]: cs-app-from-user | Directly mapped from the corresponding JSON field  
cs-app-instance-id | additional.fields[].key: "x-cs-app-instance-id", additional.fields[].value.string_value: cs-app-instance-id | Directly mapped from the corresponding JSON field  
cs-app-object-name | additional.fields[].key: "x-cs-app-object-name", additional.fields[].value.string_value: cs-app-object-name | Directly mapped from the corresponding JSON field  
cs-app-object-type | additional.fields[].key: "x-cs-app-object-type", additional.fields[].value.string_value: cs-app-object-type | Directly mapped from the corresponding JSON field  
cs-app-suite | additional.fields[].key: "x-cs-app-suite", additional.fields[].value.string_value: cs-app-suite | Directly mapped from the corresponding JSON field  
cs-app-tags | additional.fields[].key: "x-cs-app-tags", additional.fields[].value.string_value: cs-app-tags | Directly mapped from the corresponding JSON field  
cs-bytes | network.sent_bytes: cs-bytes | Directly mapped from the corresponding JSON field  
cs-content-type | additional.fields[].key: "sc-content-type", additional.fields[].value.string_value: cs-content-type | Directly mapped from the corresponding JSON field  
cs-dns | target.asset.hostname[]: cs-dns, target.hostname: cs-dns | Directly mapped from the corresponding JSON field  
cs-host | target.asset.hostname[]: cs-host, target.hostname: cs-host | Directly mapped from the corresponding JSON field  
cs-method | network.http.method: cs-method | Directly mapped from the corresponding JSON field  
cs-referer | network.http.referral_url: cs-referer | Directly mapped from the corresponding JSON field  
cs-uri | additional.fields[].key: "cs-uri", additional.fields[].value.string_value: cs-uri | Directly mapped from the corresponding JSON field  
cs-uri-path | additional.fields[].key: "x-cs-uri-path", additional.fields[].value.string_value: cs-uri-path | Directly mapped from the corresponding JSON field  
cs-uri-port | additional.fields[].key: "cs-uri-port", additional.fields[].value.string_value: cs-uri-port | Directly mapped from the corresponding JSON field  
cs-uri-scheme | network.application_protocol: cs-uri-scheme | Directly mapped from the corresponding JSON field after converting to uppercase  
cs-user-agent | network.http.parsed_user_agent: Parsed user agent, network.http.user_agent: cs-user-agent | network.http.parsed_user_agent is derived by parsing the cs-user-agent field using the "parseduseragent" filter  
cs-username | principal.user.userid: cs-username | Directly mapped from the corresponding JSON field  
date | metadata.event_timestamp.seconds: Epoch seconds from date and time fields, metadata.event_timestamp.nanos: 0 | The date and time are combined and converted to epoch seconds and nanoseconds. Nanoseconds are set to 0.  
device | intermediary.hostname: device | Directly mapped from the corresponding CEF field  
dst | target.ip[]: dst | Directly mapped from the corresponding CEF field  
dst_country | target.location.country_or_region: dst_country | Directly mapped from the corresponding grokked field  
dst_ip | target.asset.ip[]: dst_ip, target.ip[]: dst_ip | Directly mapped from the corresponding grokked field  
dst_location | target.location.city: dst_location | Directly mapped from the corresponding grokked field  
dst_region | target.location.state: dst_region | Directly mapped from the corresponding grokked field  
dst_zip | Not mapped | This field is not mapped to the UDM  
duser | target.user.email_addresses[]: duser, target.user.user_display_name: duser | Directly mapped from the corresponding CEF field  
dvchost | about.hostname: dvchost, target.asset.hostname[]: dvchost, target.hostname: dvchost | Directly mapped from the corresponding CEF field  
event_timestamp | metadata.event_timestamp.seconds: event_timestamp | Directly mapped from the corresponding grokked field  
hostname | target.asset.hostname[]: hostname, target.hostname: hostname | Directly mapped from the corresponding CEF field  
IncidentID | security_result.detection_fields[].key: "IncidentID", security_result.detection_fields[].value: IncidentID | Directly mapped from the corresponding CEF field  
intermediary | intermediary: intermediary | Directly mapped from the corresponding CEF field  
md5 | target.file.md5: md5 | Directly mapped from the corresponding CEF field  
message | Various UDM fields | The message field is parsed based on whether it contains "CEF". If it does, it's treated as a CEF log. Otherwise, it's parsed as either a space-delimited string or JSON.  
mwDetectionEngine | additional.fields[].key: "mwDetectionEngine", additional.fields[].value.string_value: mwDetectionEngine | Directly mapped from the corresponding CEF field  
mwType | metadata.description: mwType | Directly mapped from the corresponding CEF field  
os | principal.platform: Derived value | The platform is derived from the os field: "Windows" maps to WINDOWS, "MAC" maps to MAC, and "LINUX" maps to LINUX  
page | network.http.referral_url: page | Directly mapped from the corresponding CEF field  
referer | network.http.referral_url: referer | Directly mapped from the corresponding CEF field  
requestClientApplication | network.http.parsed_user_agent: Parsed user agent, network.http.user_agent: requestClientApplication | network.http.parsed_user_agent is derived by parsing the requestClientApplication field using the "parseduseragent" filter  
request_method | network.http.method: request_method | Directly mapped from the corresponding grokked field  
rs-status | additional.fields[].key: "rs-status", additional.fields[].value.string_value: rs-status, network.http.response_code: rs-status | Directly mapped from the corresponding JSON field  
s-ip | target.asset.ip[]: s-ip, target.ip[]: s-ip | Directly mapped from the corresponding JSON field  
sc-bytes | network.received_bytes: sc-bytes | Directly mapped from the corresponding JSON field  
sc-content-type | additional.fields[].key: "sc-content-type", additional.fields[].value.string_value: sc-content-type | Directly mapped from the corresponding JSON field  
sc-status | network.http.response_code: sc-status | Directly mapped from the corresponding JSON field  
serverBytes | network.received_bytes: serverBytes | Directly mapped from the corresponding CEF field  
sha256 | target.file.sha256: sha256 | Directly mapped from the corresponding CEF field  
src | principal.ip[]: src | Directly mapped from the corresponding CEF field  
src_country | principal.location.country_or_region: src_country | Directly mapped from the corresponding grokked field  
src_ip | principal.asset.ip[]: src_ip, principal.ip[]: src_ip | Directly mapped from the corresponding grokked field  
src_location | principal.location.city: src_location | Directly mapped from the corresponding grokked field  
src_region | principal.location.state: src_region | Directly mapped from the corresponding grokked field  
src_latitude | Not mapped | This field is not mapped to the UDM  
src_longitude | Not mapped | This field is not mapped to the UDM  
src_zip | Not mapped | This field is not mapped to the UDM  
suser | principal.user.user_display_name: suser | Directly mapped from the corresponding CEF field  
target_host | target.asset.hostname[]: target_host, target.hostname: target_host | Directly mapped from the corresponding grokked field  
time | metadata.event_timestamp.seconds: Epoch seconds from date and time fields, metadata.event_timestamp.nanos: 0 | The date and time are combined and converted to epoch seconds and nanoseconds. Nanoseconds are set to 0.  
timestamp | metadata.event_timestamp.seconds: timestamp | Directly mapped from the corresponding CEF field  
ts | metadata.event_timestamp.seconds: Epoch seconds from ts, metadata.event_timestamp.nanos: 0 | The timestamp is converted to epoch seconds and nanoseconds. Nanoseconds are set to 0.  
url | target.url: url | Directly mapped from the corresponding CEF field  
user_agent | network.http.parsed_user_agent: Parsed user agent, network.http.user_agent: user_agent | network.http.parsed_user_agent is derived by parsing the user_agent field using the "parseduseragent" filter  
user_key | principal.user.email_addresses[]: user_key | Directly mapped from the corresponding grokked field  
version | Not mapped | This field is not mapped to the UDM  
x-c-browser | additional.fields[].key: "x-c-browser", additional.fields[].value.string_value: x-c-browser | Directly mapped from the corresponding JSON field  
x-c-browser-version | additional.fields[].key: "x-c-browser-version", additional.fields[].value.string_value: x-c-browser-version | Directly mapped from the corresponding JSON field  
x-c-country | principal.location.country_or_region: x-c-country | Directly mapped from the corresponding JSON field  
x-c-device | additional.fields[].key: "x-c-device", additional.fields[].value.string_value: x-c-device | Directly mapped from the corresponding JSON field  
x-c-latitude | principal.location.region_coordinates.latitude: x-c-latitude | Directly mapped from the corresponding JSON field  
x-c-local-time | security_result.detection_fields[].key: "x-c-local-time", security_result.detection_fields[].value: x-c-local-time | Directly mapped from the corresponding JSON field  
x-c-location | principal.location.name: x-c-location | Directly mapped from the corresponding JSON field  
x-c-longitude | principal.location.region_coordinates.longitude: x-c-longitude | Directly mapped from the corresponding JSON field  
x-c-os | principal.platform: Derived value | The platform is derived from the x-c-os field: "Windows" maps to WINDOWS, "MAC" maps to MAC, and "LINUX" maps to LINUX  
x-c-region | principal.location.state: x-c-region | Directly mapped from the corresponding JSON field  
x-c-zipcode | additional.fields[].key: "x-c-zipcode", additional.fields[].value.string_value: x-c-zipcode | Directly mapped from the corresponding JSON field  
x-category | additional.fields[].key: "x-category", additional.fields[].value.string_value: x-category | Directly mapped from the corresponding JSON field  
x-category-id | additional.fields[].key: "x-category-id", additional.fields[].value.string_value: x-category-id | Directly mapped from the corresponding JSON field  
x-cs-access-method | additional.fields[].key: "accessMethod", additional.fields[].value.string_value: x-cs-access-method | Directly mapped from the corresponding JSON field  
x-cs-app | principal.application: x-cs-app, additional.fields[].key: "x-cs-app", additional.fields[].value.string_value: x-cs-app | Directly mapped from the corresponding JSON field  
x-cs-app-activity | additional.fields[].key: "x-cs-app-activity", additional.fields[].value.string_value: x-cs-app-activity | Directly mapped from the corresponding JSON field  
x-cs-app-category | additional.fields[].key: "x-cs-app-category", additional.fields[].value.string_value: x-cs-app-category | Directly mapped from the corresponding JSON field  
x-cs-app-cci | additional.fields[].key: "x-cs-app-cci", additional.fields[].value.string_value: x-cs-app-cci | Directly mapped from the corresponding JSON field  
x-cs-app-from-user | additional.fields[].key: "x-cs-app-from-user", additional.fields[].value.string_value: x-cs-app-from-user | Directly mapped from the corresponding JSON field  
x-cs-app-object-id | additional.fields[].key: "x-cs-app-object-id", additional.fields[].value.string_value: x-cs-app-object-id | Directly mapped from the corresponding JSON field  
x-cs-app-object-name | additional.fields[].key: "x-cs-app-object-name", additional.fields[].value.string_value: x-cs-app-object-name | Directly mapped from the corresponding JSON field  
x-cs-app-object-type | additional.fields[].key: "x-cs-app-object-type", additional.fields[].value.string_value: x-cs-app-object-type | Directly mapped from the corresponding JSON field  
x-cs-app-suite | additional.fields[].key: "x-cs-app-suite", additional.fields[].value.string_value: x-cs-app-suite | Directly mapped from the corresponding JSON field  
x-cs-app-tags | additional.fields[].key: "x-cs-app-tags", additional.fields[].value.string_value: x-cs-app-tags | Directly mapped from the corresponding JSON field  
x-cs-app-to-user | additional.fields[].key: "x-cs-app-to-user", additional.fields[].value.string_value: x-cs-app-to-user | Directly mapped from the corresponding JSON field  
x-cs-dst-ip | security_result.detection_fields[].key: "x-cs-dst-ip", security_result.detection_fields[].value: x-cs-dst-ip, target.asset.ip[]: x-cs-dst-ip, target.ip[]: x-cs-dst-ip | Directly mapped from the corresponding JSON field  
x-cs-dst-port | security_result.detection_fields[].key: "x-cs-dst-port", security_result.detection_fields[].value: x-cs-dst-port, target.port: x-cs-dst-port | Directly mapped from the corresponding JSON field  
x-cs-http-version | security_result.detection_fields[].key: "x-cs-http-version", security_result.detection_fields[].value: x-cs-http-version | Directly mapped from the corresponding JSON field  
x-cs-page-id | additional.fields[].key: "x-cs-page-id", additional.fields[].value.string_value: x-cs-page-id | Directly mapped from the corresponding JSON field  
x-cs-session-id | network.session_id: x-cs-session-id | Directly mapped from the corresponding JSON field  
x-cs-site | additional.fields[].key: "x-cs-site", additional.fields[].value.string_value: x-cs-site | Directly mapped from the corresponding JSON field  
x-cs-sni | network.tls.client.server_name: x-cs-sni | Directly mapped from the corresponding JSON field  
x-cs-src-ip | principal.asset.ip[]: x-cs-src-ip, principal.ip[]: x-cs-src-ip, security_result.detection_fields[].key: "x-cs-src-ip", security_result.detection_fields[].value: x-cs-src-ip | Directly mapped from the corresponding JSON field  
x-cs-src-ip-egress | principal.asset.ip[]: x-cs-src-ip-egress, principal.ip[]: x-cs-src-ip-egress, security_result.detection_fields[].key: "x-cs-src-ip-egress", security_result.detection_fields[].value: x-cs-src-ip-egress | Directly mapped from the corresponding JSON field  
x-cs-src-port | principal.port: x-cs-src-port, security_result.detection_fields[].key: "x-cs-src-port", security_result.detection_fields[].value: x-cs-src-port | Directly mapped from the corresponding JSON field  
x-cs-ssl-cipher | network.tls.cipher: x-cs-ssl-cipher | Directly mapped from the corresponding JSON field  
x-cs-ssl-fronting-error | security_result.detection_fields[].key: "x-cs-ssl-fronting-error", security_result.detection_fields[].value: x-cs-ssl-fronting-error | Directly mapped from the corresponding JSON field  
x-cs-ssl-handshake-error | security_result.detection_fields[].key: "x-cs-ssl-handshake-error", security_result.detection_fields[].value: x-cs-ssl-handshake-error | Directly mapped from the corresponding JSON field  
x-cs-ssl-ja3 | network.tls.client.ja3: x-cs-ssl-ja3 | Directly mapped from the corresponding JSON field  
x-cs-ssl-version | network.tls.version: x-cs-ssl-version | Directly mapped from the corresponding JSON field  
x-cs-timestamp | metadata.event_timestamp.seconds: x-cs-timestamp | Directly mapped from the corresponding JSON field  
x-cs-traffic-type | additional.fields[].key: "trafficType", additional.fields[].value.string_value: x-cs-traffic-type | Directly mapped from the corresponding JSON field  
x-cs-tunnel-src-ip | security_result.detection_fields[].key: "x-cs-tunnel-src-ip", security_result.detection_fields[].value: x-cs-tunnel-src-ip | Directly mapped from the corresponding JSON field  
x-cs-uri-path | additional.fields[].key: "x-cs-uri-path", additional.fields[].value.string_value: x-cs-uri-path | Directly mapped from the corresponding JSON field  
x-cs-url | target.url: x-cs-url | Directly mapped from the corresponding JSON field  
x-cs-userip | security_result.detection_fields[].key: "x-cs-userip", security_result.detection_fields[].value: x-cs-userip | Directly mapped from the corresponding JSON field  
x-other-category | security_result.category_details[]: x-other-category | Directly mapped from the corresponding JSON field  
x-other-category-id | security_result.detection_fields[].key: "x-other-category-id", security_result.detection_fields[].value: x-other-category-id | Directly mapped from the corresponding JSON field  
x-policy-action | security_result.action: Derived value, security_result.action_details: x-policy-action | security_result.action is derived by converting x-policy-action to uppercase. If the uppercase value is "ALLOW" or "BLOCK", it's used directly. Otherwise, it's not mapped. security_result.action_details is directly mapped from x-policy-action.  
x-policy-dst-host | security_result.detection_fields[].key: "x-policy-dst-host", security_result.detection_fields[].value: x-policy-dst-host | Directly mapped from the corresponding JSON field  
x-policy-dst-host-source | security_result.detection_fields[].key: "x-policy-dst-host-source", security_result.detection_fields[].value: x-policy-dst-host-source | Directly mapped from the corresponding JSON field  
x-policy-dst-ip | security_result.detection_fields[].key: "x-policy-dst-ip", security_result.detection_fields[].value: x-policy-dst-ip | Directly mapped from the corresponding JSON field  
x-policy-name | security_result.rule_name: x-policy-name | Directly mapped from the corresponding JSON field  
x-policy-src-ip | security_result.detection_fields[].key: "x-policy-src-ip", security_result.detection_fields[].value: x-policy-src-ip | Directly mapped from the corresponding JSON field  
x-r-cert-enddate | network.tls.server.certificate.not_after.seconds: Epoch seconds from x-r-cert-enddate | The date is converted to epoch seconds  
x-r-cert-expired | additional.fields[].key: "x-r-cert-expired", additional.fields[].value.string_value: x-r-cert-expired | Directly mapped from the corresponding JSON field  
x-r-cert-incomplete-chain | additional.fields[].key: "x-r-cert-incomplete-chain", additional.fields[].value.string_value: x-r-cert-incomplete-chain | Directly mapped from the corresponding JSON field  
x-r-cert-issuer-cn | network.tls.server.certificate.issuer: x-r-cert-issuer-cn | Directly mapped from the corresponding JSON field  
x-r-cert-mismatch | additional.fields[].key: "x-r-cert-mismatch", additional.fields[].value.string_value: x-r-cert-mismatch | Directly mapped from the corresponding JSON field  
x-r-cert-revoked | additional.fields[].key: "x-r-cert-revoked", additional.fields[].value.string_value: x-r-cert-revoked | Directly mapped from the corresponding JSON field  
x-r-cert-self-signed | additional.fields[].key: "x-r-cert-self-signed", additional.fields[].value.string_value: x-r-cert-self-signed | Directly mapped from the corresponding JSON field  
x-r-cert-startdate | network.tls.server.certificate.not_before.seconds: Epoch seconds from x-r-cert-startdate | The date is converted to epoch seconds  
x-r-cert-subject-cn | network.tls.server.certificate.subject: x-r-cert-subject-cn | Directly mapped from the corresponding JSON field  
x-r-cert-untrusted-root | additional.fields[].key: "x-r-cert-untrusted-root", additional.fields[].value.string_value: x-r-cert-untrusted-root | Directly mapped from the corresponding JSON field  
x-r-cert-valid | additional.fields[].key: "x-r-cert-valid", additional.fields[].value.string_value: x-r-cert-valid | Directly mapped from the corresponding JSON field  
x-request-id | additional.fields[].key: "requestId", additional.fields[].value.string_value: x-request-id | Directly mapped from the corresponding JSON field  
x-rs-file-category | additional.fields[].key: "x-rs-file-category", additional.fields[].value.string_value: x-rs-file-category | Directly mapped from the corresponding JSON field  
x-rs-file-type | additional.fields[].key: "x-rs-file-type", additional.fields[].value.string_value: x-rs-file-type | Directly mapped from the corresponding JSON field  
x-s-country | target.location.country_or_region: x-s-country | Directly mapped from the corresponding JSON field  
x-s-dp-name | additional.fields[].key: "x-s-dp-name", additional.fields[].value.string_value: x-s-dp-name | Directly mapped from the corresponding JSON field  
x-s-latitude | target.location.region_coordinates.latitude: x-s-latitude | Directly mapped from the corresponding JSON field  
x-s-location | target.location.name: x-s-location | Directly mapped from the corresponding JSON field  
x-s-longitude | target.location.region_coordinates.longitude: x-s-longitude | Directly mapped from the corresponding JSON field  
x-s-region | target.location.state: x-s-region | Directly mapped from the corresponding JSON field  
x-s-zipcode | additional.fields[].key: "x-s-zipcode", additional.fields[].value.string_value: x-s-zipcode | Directly mapped from the corresponding JSON field  
x-sr-ssl-cipher | security_result.detection_fields[].key: "x-sr-ssl-cipher", security_result.detection_fields[].value: x-sr-ssl-cipher | Directly mapped from the corresponding JSON field  
x-sr-ssl-client-certificate-error | security_result.detection_fields[].key: "x-sr-ssl-client-certificate-error", security_result.detection_fields[].value: x-sr-ssl-client-certificate-error | Directly mapped from the corresponding JSON field  
x-sr-ssl-engine-action | security_result.detection_fields[].key: "x-sr-ssl-engine-action", security_result.detection_fields[].value: x-sr-ssl-engine-action | Directly mapped from the corresponding JSON field  
x-sr-ssl-engine-action-reason | security_result.detection_fields[].key: "x-sr-ssl-engine-action-reason", security_result.detection_fields[].value: x-sr-ssl-engine-action-reason | Directly mapped from the corresponding JSON field  
x-sr-ssl-handshake-error | security_result.detection_fields[].key: "x-sr-ssl-handshake-error", security_result.detection_fields[].value: x-sr-ssl-handshake-error | Directly mapped from the corresponding JSON field  
x-sr-ssl-ja3s | network.tls.server.ja3s: x-sr-ssl-ja3s | Directly mapped from the corresponding JSON field  
x-sr-ssl-malformed-ssl | security_result.detection_fields[].key: "x-sr-ssl-malformed-ssl", security_result.detection_fields[].value: x-sr-ssl-malformed-ssl | Directly mapped from the corresponding JSON field  
x-sr-ssl-version | security_result.detection_fields[].key: "x-sr-ssl-version", security_result.detection_fields[].value: x-sr-ssl-version | Directly mapped from the corresponding JSON field  
x-s-custom-signing-ca-error | security_result.detection_fields[].key: "x-s-custom-signing-ca-error", security_result.detection_fields[].value: x-s-custom-signing-ca-error | Directly mapped from the corresponding JSON field  
x-ssl-bypass | security_result.detection_fields[].key: "SSL BYPASS", security_result.detection_fields[].value: x-ssl-bypass or x-ssl-bypass-reason | If x-ssl-bypass is "Yes" and x-ssl-bypass-reason is present, the value of x-ssl-bypass-reason is used. Otherwise, the value of x-ssl-bypass is used.  
x-ssl-policy-action | security_result.detection_fields[].key: "x-ssl-policy-action", security_result.detection_fields[].value: x-ssl-policy-action | Directly mapped from the corresponding JSON field  
x-ssl-policy-categories | security_result.category_details[]: x-ssl-policy-categories | Directly mapped from the corresponding JSON field  
x-ssl-policy-dst-host | security_result.detection_fields[].key: "x-ssl-policy-dst-host", security_result.detection_fields[].value: x-ssl-policy-dst-host | Directly mapped from the corresponding JSON field  
x-ssl-policy-dst-host-source | security_result.detection_fields[].key: "x-ssl-policy-dst-host-source", security_result.detection_fields[].value: x-ssl-policy-dst-host-source | Directly mapped from the corresponding JSON field  
x-ssl-policy-dst-ip | security_result.detection_fields[].key: "x-ssl-policy-dst-ip", security_result.detection_fields[].value: x-ssl-policy-dst-ip | Directly mapped from the corresponding JSON field  
x-ssl-policy-name | security_result.rule_name: x-ssl-policy-name | Directly mapped from the corresponding JSON field  
x-ssl-policy-src-ip | security_result.detection_fields[].key: "x-ssl-policy-src-ip", security_result.detection_fields[].value: x-ssl-policy-src-ip | Directly mapped from the corresponding JSON field  
x-sr-dst-ip | security_result.detection_fields[].key: "x-sr-dst-ip", security_result.detection_fields[].value: x-sr-dst-ip | Directly mapped from the corresponding JSON field  
x-sr-dst-port | security_result.detection_fields[].key: "x-sr-dst-port", security_result.detection_fields[].value: x-sr-dst-port | Directly mapped from the corresponding JSON field  
x-type | additional.fields[].key: "xType", additional.fields[].value.string_value: x-type | Directly mapped from the corresponding JSON field  
x-transaction-id | additional.fields[].key: "transactionId", additional.fields[].value.string_value: x-transaction-id | Directly mapped from the corresponding JSON field  
| metadata.vendor_name | Set to "Netskope"  
| metadata.product_name | Set to "Netskope Webproxy" if not already present  
| metadata.log_type | Set to "NETSKOPE_WEBPROXY"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netskope-webproxy-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
