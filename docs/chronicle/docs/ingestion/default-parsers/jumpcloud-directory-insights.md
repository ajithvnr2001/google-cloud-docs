---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jumpcloud-directory-insights/
title: Collect JumpCloud Directory Insights logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:10.526173+00:00
---

# Collect JumpCloud Directory Insights logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jumpcloud-directory-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect JumpCloud Directory Insights logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest JumpCloud Directory Insights logs into Google Security Operations using Google Cloud Storage V2.

JumpCloud is a cloud directory platform that provides identity management, SSO, and device management. Directory Insights delivers audit and activity logs covering user authentication, admin actions, and system events. The parser maps log fields to the Unified Data Model (UDM), handling event types such as user logins, resource changes, and security actions.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets and IAM policies
  * A JumpCloud account with an **Admin** or **Manager** role and a valid API key



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `jumpcloud-directory-insights-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Export JumpCloud Directory Insights logs to Google Cloud Storage

JumpCloud Directory Insights exposes events through the [Directory Insights API](https://docs.jumpcloud.com/api/insights/directory/1.0/index.html). Use a scheduled script or Cloud Run function to pull events and write them to GCS.

  1. Generate a JumpCloud API key:

     1. Sign in to the **JumpCloud Admin Portal**.
     2. Go to your profile icon and select **My API Key**.
     3. Copy the API key.
  2. Create a Cloud Run function that queries the JumpCloud Directory Insights API, retrieves events, and writes them to GCS.

  3. Trigger the function on a schedule using Cloud Scheduler and Pub/Sub.



  * Ensure that the exported files retain their original JSON format.
  * Each file should contain one or more event records.



## Retrieve the Google SecOps service account

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Feeds**.
  3. Click **Add New Feed**.
  4. Click **Configure a single feed**.
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **JumpCloud Directory Insights** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.


**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.

## Grant IAM permissions to the Google SecOps service account

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option (delete transferred files), grant **Storage Object Admin** role instead of Storage Object Viewer.

## Configure a feed in Google SecOps to ingest JumpCloud Directory Insights logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `JumpCloud Directory Insights Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **JumpCloud Directory Insights** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

Field | Value  
---|---  
**Storage bucket URI** | `gs://jumpcloud-directory-insights-logs/jumpcloud/`  
**Source Deletion Option** | Select the deletion option according to your preference  
**Maximum File Age (Days)** | Default is 180 days  
**Asset namespace** | The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)  
**Ingestion labels** | The label to be applied to the events from this feed  
     * Replace `jumpcloud-directory-insights-logs` with your actual GCS bucket name.
     * Always include the trailing slash (`/`) at the end of the URI.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
data.profile_list.payload_content.payload_type, data.profile_list.payload_content.payload_identifier, data.profile_list.payload_content.payload_uuid, data.profile_list.payload_content.payload_organization, data.profile_list.payload_content.payload_display_name, data.profile_list.payload_content.payload_description | about | Merged with attribute labels from payloadContent  
data.association.op, data.association.action_source, data.geoip.region_code, data.service, data.event_type, data.@version, data.application.version, data.application.publisher, data.application.uninstall_string, data.changes.0.field, data.changes.0.from, data.changes.0.to, data.available_os_updates.allows_install_later | additional.fields | Merged with corresponding labels  
| extensions.auth.type | Set to "MACHINE" when event_type is USER_LOGIN  
data.timestamp | metadata.event_timestamp | Converted using date match ISO8601, RFC 3339, yyyy-MM-ddTHH:mm:ss.SSSSSSZ  
data.message, data.client_ip, data.initiated_by.username, data.system.hostname | metadata.event_type | Set to USER_LOGIN if message matches "logged in" and target not empty, else USER_UNCATEGORIZED if ip and userid present, else STATUS_UPDATE if hostname or ip present, else USER_UNCATEGORIZED if userid present, else GENERIC_EVENT  
data.id | metadata.product_log_id | Value copied directly  
data.@version, data.application.version | metadata.product_version | Set to data.@version, then replaced with data.application.version  
data.application.name | principal.application | Value copied directly  
data.mdm_type | principal.asset.hardware | Merged with manufacturer set to data.mdm_type  
data.command_uuid | principal.asset_id | Concatenated as "commandUuid:" + data.command_uuid  
data.system.hostname | principal.hostname | Value copied directly  
data.client_ip | principal.ip | Merged from data.client_ip  
data.geoip.country_code | principal.location.country_or_region | Value copied directly  
data.geoip.region_code | principal.location.name | Value copied directly  
data.geoip.latitude | principal.location.region_latitude | Converted to string then to float  
data.geoip.longitude | principal.location.region_longitude | Converted to string then to float  
data.geoip.region_name | principal.location.state | Value copied directly  
data.application.path, data.process_name | principal.process.file.full_path | Set to data.application.path, then replaced with data.process_name  
data.association.connection.from.name, data.mdm_device_manager_id, data.request_type | principal.resource.attribute.labels | Merged with labels for connection_from_name, mdm_device_manager_id, request_type  
data.system.id, data.resource.id, data.mdm_device_id | principal.resource.id | Set to data.system.id, then replaced with data.resource.id, then replaced with data.mdm_device_id  
data.resource.username | principal.resource.name | Value copied directly  
data.association.connection.from.object_id | principal.resource.product_object_id | Value copied directly  
data.association.connection.from.type | principal.resource.type | Value copied directly  
data.initiated_by.email | principal.user.email_addresses | Merged if email matches ^.+@.+$  
data.system.displayName | principal.user.user_display_name | Value copied directly  
data.initiated_by.username, data.admin_info.name | principal.user.userid | Set to data.initiated_by.username, then replaced with data.admin_info.name, then replaced with data.initiated_by.username  
data.success, data.status | sec_result.action | Set to ALLOW if success true or status Acknowledged, BLOCK if success false  
data.status, data.success | sec_result.action_details | Set to status if not empty, else success  
data.success, data.status, data.security_info.management_status.is_activation_lock_manageable, data.security_info.management_status.is_user_enrollment, data.security_info.management_status.enrolled_via_dep, data.organization, data.windows_meta.logon_type, data.security_info.management_status.user_approved_enrollment | sec_result.detection_fields | Merged with labels for is_activation_lock_manageable, is_user_enrollment, enrolled_via_dep, organization, logon_type, user_approved_enrollment  
data.query_responses.device_name | target.hostname | Value copied directly  
data.query_responses.wifi_mac | target.mac | Merged from data.query_responses.wifi_mac  
data.query_responses.model_name | target.platform | Set to "MAC" if matches (?i)mac  
data.query_responses.os_version | target.platform_version | Value copied directly  
data.query_responses.available_device_capacity, data.query_responses.device_capacity | target.resource.attribute.labels | Merged with labels for available_device_capacity, device_capacity  
data.association.connection.to.name | target.resource.name | Value copied directly  
data.association.connection.to.object_id | target.resource.product_object_id | Value copied directly  
data.association.connection.to.type | target.resource.type | Value copied directly  
data.profile_list.payload_organization | target.user.department | Merged from profile_payload_organization  
| metadata.vendor_name | Set to "JUMPCLOUD_DIRECTORY_INSIGHTS"  
| metadata.product_name | Set to "JUMPCLOUD_DIRECTORY_INSIGHTS"  
`data.alert_id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`data.alert_title` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`data.category` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`data.description` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`data.priority` | `event.idm.read_only_udm.security_result.priority` | Mapped from changelog  
`data.rule_id` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`data.event_description` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`data.di_event.event_type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`data.di_event.initiated_by.email` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`data.di_event.initiated_by.id` | `event.idm.read_only_udm.principal.user.product_object_id` | Mapped from changelog  
`data.di_event.client_ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`data.di_event.association.connection.from.name` | `event.idm.read_only_udm.target.group.group_display_name` | Mapped from changelog  
`data.di_event.association.connection.to.name` | `event.idm.read_only_udm.about.user.userid` | Mapped from changelog  
`data.di_event.association.connection.to.object_id` | `event.idm.read_only_udm.about.user.product_object_id` | Mapped from changelog  
`data.di_event.success` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`data.di_event.service` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`data.di_event.geoip.country_code` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`data.organization_name` | `event.idm.read_only_udm.principal.user.company_name` | Mapped from changelog  
`data.di_event.@version` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`data.source_url` | `event.idm.read_only_udm.principal.url` | Mapped from changelog  
`data.di_event.initiated_by.source` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`data.source_name` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`data.di_event.geoip.latitude` | `event.idm.read_only_udm.principal.location.region_latitude` | Mapped from changelog  
`data.di_event.geoip.longitude` | `event.idm.read_only_udm.principal.location.region_longitude` | Mapped from changelog  
`data.di_event.geoip.region_name` | `event.idm.read_only_udm.principal.location.state` | Mapped from changelog  
`data.di_event.organization` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`association_op", "action_source", and "sso_token_success` | `additional.fields` | Mapped from changelog  
`connection_from_type` | `principal.resource.resource_type` | Mapped from changelog  
`connection_from_object_id` | `principal.resource.product_object_id` | Mapped from changelog  
`connection_to_name` | `target.resource.name` | Mapped from changelog  
`connection_to_type` | `target.resource.resource_type` | Mapped from changelog  
`connection_to_object_id` | `target.resource.product_object_id` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jumpcloud-directory-insights-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
