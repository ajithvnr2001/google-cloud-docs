---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-app-engine/
title: Collect Google App Engine logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:28.777698+00:00
---

# Collect Google App Engine logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-app-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Google App Engine logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Google App Engine logs to Google Security Operations using Google Cloud Storage V2.

Google App Engine is a fully managed serverless platform for building and deploying web applications and APIs. App Engine automatically generates request logs for HTTP requests and application logs from your code. These logs are sent to Cloud Logging and can be exported to Cloud Storage for ingestion into Google Security Operations.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Logging sinks (roles/logging.configWriter)
  * An active App Engine application (standard or flexible environment)



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `appengine-logs-export`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Configure Cloud Logging to export App Engine logs to GCS

Cloud Logging uses log sinks to route log entries to supported destinations, including Cloud Storage buckets. The sink's writer identity requires the Storage Object Creator role (roles/storage.objectCreator) on the destination bucket.

### Create a Cloud Logging sink

  1. In the [Google Cloud Console](https://console.cloud.google.com/), go to **Logging > Log Router**.
  2. Click **Create sink**.
  3. Provide the following configuration details: 
     * **Sink name** : Enter a descriptive name (for example, `appengine-to-gcs`).
     * **Sink description** : Optional description.
  4. Click **Next**.
  5. In the **Select sink service** section: 
     * **Sink service** : Select **Cloud Storage bucket**.
     * **Select Cloud Storage bucket** : Select `appengine-logs-export` from the dropdown.
  6. Click **Next**.
  7. In the **Choose logs to include in sink** section, enter a filter query to select App Engine logs. The resource type must be exactly "gae_app".

For all App Engine logs (request and application logs):
         
         resource.type="gae_app"
         

For App Engine request logs only:
         
         resource.type="gae_app"
         logName="projects/PROJECT_ID/logs/appengine.googleapis.com/request_log"
         

For App Engine application logs (stdout/stderr):
         
         resource.type="gae_app"
         (logName="projects/PROJECT_ID/logs/stdout" OR logName="projects/PROJECT_ID/logs/stderr")
         

Replace `PROJECT_ID` with your GCP project ID.

  8. Click **Next**.

  9. Review the configuration and click **Create sink**.




### Grant permissions to the sink writer identity

After creating the sink, you must grant the sink's writer identity the Storage Object Creator role on the destination bucket. The writer identity for the service account looks similar to: serviceAccount:service-123456789012@gcp-sa-logging.iam.gserviceaccount.com

  1. In the **Log Router** page, locate the newly created sink.
  2. Click the menu icon (three vertical dots) next to the sink name.
  3. Select **View sink details**.
  4. Copy the **Writer identity** (service account email).
  5. Go to **Cloud Storage > Buckets**.
  6. Click the bucket name (`appengine-logs-export`).
  7. Go to the **Permissions** tab.
  8. Click **Grant access**.
  9. Provide the following configuration details: 
     * **Add principals** : Paste the sink's writer identity (service account email).
     * **Assign roles** : Select **Storage Object Creator**.
  10. Click **Save**.



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Configure a feed in Google SecOps to ingest App Engine logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `App Engine Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **GCP_APP_ENGINE** as the **Log type**.

  7. Click **Get Service Account**.

  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address. You will use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://appengine-logs-export/
           

Cloud Logging organizes exported log files in directory hierarchies by log type and date. The log type can be a compound name like appengine.googleapis.com/request_log. Files are sharded and named with time periods (for example, 08:00:00_08:59:59_S0.json).

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  12. Click **Next**.

  13. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on the bucket name (`appengine-logs-export`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## Understanding App Engine log structure

App Engine automatically sends both request logs and app logs to Cloud Logging. App Engine automatically emits logs for requests sent to your app, so there is no need to write request logs. This section covers how to write app logs.

App Engine request logs have log entries containing protoPayload fields which hold objects of type RequestLog with @type "type.googleapis.com/google.appengine.logging.v1.RequestLog". The resource type is "gae_app".

By default, the log payload is a text string stored in the textPayload field of the log entry. The strings appear as messages in the Logs Explorer and are associated with the App Engine service and version that emitted them.

To write structured logs, you write logs in the form of a single line of serialized JSON. When you provide a structured log as a JSON dictionary, some special fields are stripped from the jsonPayload and are written to the corresponding field in the generated LogEntry. For example, if your JSON includes a severity property, it is removed from the jsonPayload and appears instead as the log entry's severity.

## Known limitations

When you route logs from log sink to Cloud Storage, the Cloud Storage destination only contains request logs. App Engine writes app logs to different folders.

Routed log entries are saved to Cloud Storage buckets in hourly batches. It might take from 2 to 3 hours before the first entries begin to appear.

In the App Engine flexible environment, logging works automatically. However, the logs are collected in a different format. Logs will not be bundled by requests, and logs from stdout and stderr are collected separately.

## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
jsonPayload.logger, taskTypeName, jsonPayload.@type, jsonPayload.backendTargetProjectNumber, jsonPayload.cacheDecision, resource.labels.version_id, resource.labels.module_id, logName, spanId, trace, protoPayload.@type, labels.clone_id, operation.producer | additional.fields | Merged with key-value labels created from each field  
metadata | metadata | Renamed from metadata  
receiveTimestamp | metadata.collected_timestamp | Parsed using date filter with RFC 3339  
| metadata.event_type | Set to "USER_LOGIN" if has_principal, has_target, has_principal_user; "NETWORK_CONNECTION" if has_principal and has_target; "USER_UNCATEGORIZED" if not has_principal and has_target; "STATUS_UPDATE" if has_principal; "USER_UNCATEGORIZED" if has_principal_user; else "GENERIC_EVENT"  
| metadata.extensions.auth.type | Set to "AUTHTYPE_UNSPECIFIED" if has_principal, has_target, has_principal_user  
insertId | metadata.product_log_id | Value copied directly  
httpRequest.requestMethod,protoPayload.method | network.http.method | Value from httpRequest.requestMethod if not empty, else protoPayload.method  
httpRequest.userAgent | network.http.parsed_user_agent | Converted to parseduseragent  
httpRequest.status | network.http.response_code | Converted to string then to integer  
httpRequest.userAgent | network.http.user_agent | Value copied directly  
httpRequest.responseSize | network.received_bytes | Converted to uinteger  
httpRequest.requestSize | network.sent_bytes | Converted to uinteger  
principal | principal | Renamed from principal if not empty  
protoPayload.host | principal.asset.hostname | Value copied directly  
httpRequest.serverIp, protoPayload.ip | principal.asset.ip | Merged with server_ip from httpRequest.serverIp or protoPayload.ip  
protoPayload.host | principal.hostname | Value copied directly  
httpRequest.serverIp, protoPayload.ip | principal.ip | Merged with server_ip from httpRequest.serverIp or protoPayload.ip  
protoPayload.appId | principal.resource.attribute.labels | Merged with appId_label containing key "appId" and value from the field  
requestUser | principal.user.email_addresses | Merged with requestUser if matches email pattern  
security_result | security_result | Merged from security_result  
resource.labels.forwarding_rule_name | security_result.rule_labels | Merged with rule_label containing key "forwarding_rule_name" and value from the field  
severity | security_result.severity | Set to severity if matches (?i)ERROR|CRITICAL, INFORMATIONAL if matches (?i)INFO, MEDIUM if matches (?i)WARN, LOW if matches (?i)DEBUG, else UNKNOWN_SEVERITY  
jsonPayload.statusDetails | security_result.summary | Value copied directly  
target | target | Renamed from target if not empty  
resource.labels.backend_service_name | target.application | Value copied directly  
httpRequest.remoteIp, jsonPayload.remoteIp | target.asset.ip | Merged with remote_ip extracted from httpRequest.remoteIp or jsonPayload.remoteIp  
resource.labels.project_id | target.cloud.project.name | Value copied directly  
httpRequest.remoteIp, jsonPayload.remoteIp | target.ip | Merged with remote_ip extracted from httpRequest.remoteIp or jsonPayload.remoteIp  
resource.labels.zone | target.resource.attribute.cloud.availability_zone | Value copied directly  
resource.labels.target_proxy_name, resource.labels.url_map_name | target.resource.attribute.labels | Merged with labels from each source  
resource.type | target.resource.type | Value copied directly  
httpRequest.requestUrl | target.url | Value copied directly  
| metadata.product_name | Set to "GCP_APP_ENGINE"  
| metadata.vendor_name | Set to "GCP"  
`protoPayload.requestMetadata.callerIp` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`protoPayload.requestMetadata.callerIp` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`protoPayload.authenticationInfo.principalEmail` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`protoPayload.methodName` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`protoPayload.resourceName` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`protoPayload.serviceName` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`protoPayload.resourceLocation.currentLocations` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`protoPayload.authenticationInfo.oauthInfo.oauthClientId` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`protoPayload.requestMetadata.requestAttributes.time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`operation.first` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`protoPayload.serviceData.updateService.request.updateMask` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`operation.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`protoPayload.authenticationInfo.serviceAccountKeyName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`protoPayload.authorizationInfo.permission` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`protoPayload.authorizationInfo.permissionType` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`protoPayload.authorizationInfo.granted` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`protoPayload.@type" , "labels.clone_id" and "operation.producer` | `additional.labels` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-app-engine-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
