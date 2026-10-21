---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/appomni/
title: Collect AppOmni logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:30.375189+00:00
---

# Collect AppOmni logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/appomni/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AppOmni logs

**Parser Version:** 6.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to configure AppOmni to push logs to Google Security Operations using webhooks.

AppOmni is a SaaS security platform that provides continuous posture management, threat detection, and data exposure monitoring across enterprise SaaS applications including Salesforce, Microsoft 365, ServiceNow, Workday, Google Workspace, Box, and Zoom. AppOmni normalizes hundreds of event types from monitored SaaS applications and can stream alerts, events, and posture findings to external SIEM destinations using its Event Streaming feature.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * An AppOmni account with administrator permissions
  * Access to Google Cloud Console (for API key creation)
  * AppOmni Threat Detection module enabled in your instance
  * At least one monitored SaaS application connected and ingesting events in AppOmni



## Create a webhook feed in Google SecOps

### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `AppOmni Events`).
  5. Select **Webhook** as the **Source type**.
  6. Select **AppOmni** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** : Enter `\n` (newline delimiter for NDJSON payloads)
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



### Generate and save a secret key

After creating the feed, you must generate a secret key for authentication:

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. **Copy and save** the secret key securely.

**Important:** The secret key is displayed only once and cannot be retrieved later. If you lose it, you must generate a new secret key.

### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**.
  3. The URL format is:
         
         https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate
         

or
         
         https://<REGION>-malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate
         

  4. Save this URL for the next steps.

  5. Click **Done**.




## Create a Google Cloud API key

Google SecOps requires an API key for authentication. Create a restricted API key in the Google Cloud Console.

### Create the API key

  1. Go to the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project (the project associated with your Google SecOps instance).
  3. Click **Create credentials > API key**.
  4. An API key is created and displayed in a dialog.
  5. Click **Edit API key** to restrict the key.



### Restrict the API key

  1. In the **API key** settings page: 
     * **Name** : Enter a descriptive name (for example, `Chronicle Webhook API Key`)
  2. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the **Select APIs** dropdown, search for and select **Google SecOps API** (or **Chronicle API**).
  3. Click **Save**.
  4. **Copy** the API key value from the **API key** field at the top of the page.
  5. Save the API key securely.

**Note:** Restricting the API key ensures it can only be used with the Google SecOps API, reducing security risk if the key is compromised.



## Configure the AppOmni Event Streaming destination

### Construct the webhook URL

  * Combine the Google SecOps endpoint URL, API key, and secret key:
        
        <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
        

  * **Example:**
        
        https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=AIzaSyD...&secret=abcd1234...
        




### Create a Custom Webhook destination in AppOmni

  1. Sign in to your **AppOmni** instance at `https://<your-organization>.appomni.com`.
  2. Navigate to **Threat Detection > Destinations**.
  3. Click **Add New Destination**.
  4. Click the **Custom Webhook** card.
  5. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Chronicle SIEM Webhook`)
     * **Description** (optional): Enter a description (for example, `Stream AppOmni events to SIEM via webhook`)
  6. Configure the following delivery settings:

     * **URL** : Paste the complete webhook URL with API key and secret key appended as query parameters:
           
           https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=YOUR_API_KEY&secret=YOUR_SECRET_KEY
           

     * **SSL Verification** : Select this checkbox (recommended)

     * **Hash Original Field** (optional): Select this checkbox to replace the original event field from the monitored SaaS application with a SHA256 hash, reducing event size

     * **Max Event Size** (optional): Leave at the default setting or set a custom value

     * **Max Payload Size** (optional): Leave at the default setting or set a custom value

**Note:** The Google SecOps webhook feed accepts a maximum request size of 4 MB. Ensure the Max Payload Size does not exceed this limit.
  7. Select the **Data Types** you want to stream to Google SecOps:

     * **Alerts** : Threat detection alerts generated by AppOmni rules (recommended)
     * **Events** : Normalized SaaS activity events collected from monitored applications (recommended)
     * **Policy** : Posture management findings for configuration compliance
**Note:** For comprehensive security monitoring, select all available data types. If you only need threat alerts, select Alerts. If you need raw SaaS activity logs for correlation in your SIEM, select Events.
  8. Click **Save**.




### Verify the destination

  1. In **AppOmni** , go to **Threat Detection > Destinations**.
  2. Locate the destination you created.
  3. Verify the destination status shows as active.
  4. Wait for AppOmni to generate and stream events based on your monitored SaaS applications.
  5. Verify the events in Google SecOps:

     1. Go to **SIEM Settings > Feeds**.
     2. Click on your AppOmni feed.
     3. Go to the **Status** tab.
     4. Verify that events are being received.
**Note:** Events may take a few minutes to appear depending on the activity volume across your monitored SaaS applications.



## AppOmni event types

AppOmni normalizes SaaS events using the AppOmni Common Event Schema (ACES), which is based on the Elastic Common Schema (ECS). The following event categories are commonly streamed:

Category | Description | Examples  
---|---|---  
Authentication | User authentication events | Login, logout, MFA challenges, SSO events  
Configuration | Application configuration changes | Permission changes, policy updates, role modifications  
Data access | Data access and sharing events | File downloads, record views, sharing changes  
Administrative | Administrative actions | User creation, group changes, app installations  
Threat detection | AppOmni-generated alerts | Anomalous behavior, privilege escalation, data exfiltration indicators  
  
## Authentication methods reference

Google SecOps webhook feeds support multiple authentication methods. Choose the method that your vendor supports.

### Method 1: Query parameters (Recommended for AppOmni)

AppOmni Custom Webhook destinations support URL-based authentication. Append credentials to the webhook URL.

  * **URL format:**
        
        <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
        

  * **Example:**
        
        https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=AIzaSyD...&secret=abcd1234...
        




### Method 2: Custom headers

If your AppOmni version supports custom HTTP headers for webhook destinations, you can use header-based authentication for improved security.

  * **Headers:**
        
        x-goog-chronicle-auth: <API_KEY>
          x-chronicle-auth: <SECRET_KEY>
        




**Advantages:**

  * API key and secret not visible in URL
  * More secure (headers not logged in web server access logs)



## Webhook limits and best practices

### Request limits

Limit | Value  
---|---  
**Max request size** | 4 MB  
**Max QPS (queries per second)** | 15,000  
**Request timeout** | 30 seconds  
**Retry behavior** | Automatic with exponential backoff  
  
### Best practices

  * Select only the data types you need to reduce event volume and ingestion costs.
  * Enable SSL Verification to ensure secure data transmission.
  * Monitor the destination status in AppOmni regularly for delivery failures.
  * Consider enabling the Hash Original Field option if event payloads are large.
  * Use the Events data type for comprehensive SaaS audit log coverage in your SIEM.
  * Use the Alerts data type for high-priority threat detection events that require immediate triage.



## Troubleshooting

### Events not appearing in Google SecOps

**Cause:** Events are being sent but not ingested

**Solution:**

  1. Go to **SIEM Settings > Feeds** in Google SecOps.
  2. Click on your AppOmni feed.
  3. Go to the **Status** tab.
  4. Check for ingestion errors.
  5. Verify the log type is set to **AppOmni**.
  6. Verify the secret key in the webhook URL matches the one generated during feed creation.



### Destination shows error in AppOmni

**Cause:** Google SecOps endpoint is not reachable or returns non-2xx status

**Solution:**

  1. Verify the Google SecOps endpoint URL is correct.
  2. Verify the API key is valid and has Google SecOps API access.
  3. Test the endpoint manually:
         
         curl -X POST "https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=YOUR_API_KEY&secret=YOUR_SECRET_KEY" \
             -H "Content-Type: application/json" \
             -d '{"test": "event"}'
         

  4. If the test succeeds, check the AppOmni destination configuration for typos or incorrect URL formatting.




### Payload exceeds maximum size

**Cause:** AppOmni is sending payloads larger than 4 MB

**Solution:**

  1. In **AppOmni** , go to **Threat Detection > Destinations**.
  2. Click on the destination.
  3. Reduce the **Max Payload Size** to a value below 4 MB.
  4. Enable **Hash Original Field** to reduce individual event sizes.
  5. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`additional_normalstatedata` | `additional.fields` | Merged  
`additional_normalstatedatacounts` | `additional.fields` | Merged  
`additional_normalstatedataresults` | `additional.fields` | Merged  
`additional_normalstatedomaincounts` | `additional.fields` | Merged  
`additional_normalstatedomainresults` | `additional.fields` | Merged  
`additional_normalstatenameresults` | `additional.fields` | Merged  
`additional_rarestatedata` | `additional.fields` | Merged  
`additional_rarestatedatacounts` | `additional.fields` | Merged  
`additional_rarestatedataresults` | `additional.fields` | Merged  
`additional_rarestatedomaincounts` | `additional.fields` | Merged  
`additional_rarestatedomainresults` | `additional.fields` | Merged  
`additional_rarestatenameresults` | `additional.fields` | Merged  
`anomalous_domain` | `additional.fields` | Merged  
`anomalous_fields_source_as_ip_label` | `additional.fields` | Merged  
`anomalous_fields_source_as_number_label` | `additional.fields` | Merged  
`appomni_service_slug_label` | `additional.fields` | Merged  
`changes_user_indicator_label` | `additional.fields` | Merged  
`configuration_name_label` | `additional.fields` | Merged  
`configuration_old_value_label` | `additional.fields` | Merged  
`configuration_value_label` | `additional.fields` | Merged  
`destination_as_service_label` | `additional.fields` | Merged  
`destination_as_type_label` | `additional.fields` | Merged  
`destination_indicators_label` | `additional.fields` | Merged  
`destination_user_indicators_label` | `additional.fields` | Merged  
`enrichments_value_label` | `additional.fields` | Merged  
`event_duration` | `additional.fields` | Merged  
`file_directory_label` | `additional.fields` | Merged  
`has_normal_state_authentication_name_counts` | `additional.fields` | Mapped: `true` → `additional_normalstatedatacounts`  
`has_normal_state_authentication_name_results` | `additional.fields` | Mapped: `true` → `additional_normalstatenameresults`  
`has_normal_state_authentication_raw_method_count` | `additional.fields` | Mapped: `true` → `additional_normalstatedata`  
`has_normal_state_authentication_raw_method_results` | `additional.fields` | Mapped: `true` → `additional_normalstatedataresults`  
`has_normal_state_domain_counts` | `additional.fields` | Mapped: `true` → `additional_normalstatedomaincounts`  
`has_normal_state_domain_results` | `additional.fields` | Mapped: `true` → `additional_normalstatedomainresults`  
`has_rare_state_authentication_name_counts` | `additional.fields` | Mapped: `true` → `additional_rarestatedatacounts`  
`has_rare_state_authentication_name_results` | `additional.fields` | Mapped: `true` → `additional_rarestatenameresults`  
`has_rare_state_authentication_raw_method_count` | `additional.fields` | Mapped: `true` → `additional_rarestatedata`  
`has_rare_state_authentication_raw_method_results` | `additional.fields` | Mapped: `true` → `additional_rarestatedataresults`  
`has_rare_state_domain_counts` | `additional.fields` | Mapped: `true` → `additional_rarestatedomaincounts`  
`has_rare_state_domain_results` | `additional.fields` | Mapped: `true` → `additional_rarestatedomainresults`  
`indicator_list` | `additional.fields` | Merged  
`labels_some_key_label` | `additional.fields` | Merged  
`normal_state_source_as_ip_label` | `additional.fields` | Merged  
`normal_state_source_as_number_label` | `additional.fields` | Merged  
`policy_category_label` | `additional.fields` | Merged  
`policy_description_label` | `additional.fields` | Merged  
`policy_id_label` | `additional.fields` | Merged  
`policy_name_label` | `additional.fields` | Merged  
`policy_outcome_label` | `additional.fields` | Merged  
`rare_state_source_as_ip_label` | `additional.fields` | Merged  
`rare_state_source_as_number_label` | `additional.fields` | Merged  
`related_services_id_label` | `additional.fields` | Merged  
`related_services_id_name_label` | `additional.fields` | Merged  
`related_services_type_label` | `additional.fields` | Merged  
`resource_count_label` | `additional.fields` | Merged  
`resource_owner_indicator_label` | `additional.fields` | Merged  
`resource_parent_count_label` | `additional.fields` | Merged  
`resource_parent_owner_domain_label` | `additional.fields` | Merged  
`resource_parent_owner_email_label` | `additional.fields` | Merged  
`resource_parent_owner_full_name_label` | `additional.fields` | Merged  
`resource_parent_owner_hash_label` | `additional.fields` | Merged  
`resource_parent_owner_id_label` | `additional.fields` | Merged  
`resource_parent_owner_indicator_label` | `additional.fields` | Merged  
`resource_parent_owner_name_label` | `additional.fields` | Merged  
`resource_parent_owner_role_label` | `additional.fields` | Merged  
`rule_vendor_id_label` | `additional.fields` | Merged  
`source_as_domain_label` | `additional.fields` | Merged  
`source_as_service_label` | `additional.fields` | Merged  
`source_as_type_label` | `additional.fields` | Merged  
`source_user_indicator_label` | `additional.fields` | Merged  
`tactic_reference_label` | `additional.fields` | Merged  
`technique_reference_label` | `additional.fields` | Merged  
`token_appomni_alert_channel` | `additional.fields` | Merged  
`token_appomni_event_ingestion_time` | `additional.fields` | Merged  
`token_appomni_event_parent_id` | `additional.fields` | Merged  
`token_appomni_event_sortable_event_id` | `additional.fields` | Merged  
`token_appomni_event_sortable_ingest_id` | `additional.fields` | Merged  
`token_appomni_organization_id` | `additional.fields` | Merged  
`token_authentication_raw_method` | `additional.fields` | Merged  
`token_error_id` | `additional.fields` | Merged  
`token_error_message` | `additional.fields` | Merged  
`token_error_type` | `additional.fields` | Merged  
`token_event_category` | `additional.fields` | Merged  
`token_event_code` | `additional.fields` | Merged  
`token_event_created` | `additional.fields` | Merged  
`token_event_end` | `additional.fields` | Merged  
`token_event_id` | `additional.fields` | Merged  
`token_event_kind` | `additional.fields` | Merged  
`token_event_original` | `additional.fields` | Merged  
`token_event_provider` | `additional.fields` | Merged  
`token_event_sequence` | `additional.fields` | Merged  
`token_event_start` | `additional.fields` | Merged  
`token_event_type` | `additional.fields` | Merged  
`token_labels` | `additional.fields` | Merged  
`token_rel_event` | `additional.fields` | Merged  
`token_rel_hash` | `additional.fields` | Merged  
`token_rel_host` | `additional.fields` | Merged  
`token_rel_idnt` | `additional.fields` | Merged  
`token_rel_res` | `additional.fields` | Merged  
`token_rel_user` | `additional.fields` | Merged  
`token_related_ip` | `additional.fields` | Merged  
`token_service_id` | `additional.fields` | Merged  
`token_service_name` | `additional.fields` | Merged  
`token_service_type` | `additional.fields` | Merged  
`token_session_kind` | `additional.fields` | Merged  
`token_source_user_hash` | `additional.fields` | Merged  
`token_space_category` | `additional.fields` | Merged  
`token_space_id` | `additional.fields` | Merged  
`token_space_name` | `additional.fields` | Merged  
`token_tag` | `additional.fields` | Merged  
`token_user_agent_os_kernel` | `additional.fields` | Merged  
`token_user_agent_os_platform` | `additional.fields` | Merged  
`token_user_identity_admin` | `additional.fields` | Merged  
`token_user_identity_elevated` | `additional.fields` | Merged  
`token_version` | `additional.fields` | Merged  
`user_effective_indicator_label` | `additional.fields` | Merged  
`user_indicator_label` | `additional.fields` | Merged  
`user_target_indicator_label` | `additional.fields` | Merged  
`authentication.provider` | `extensions.auth.auth_details` | Directly mapped  
`auth_mechanism` | `extensions.auth.mechanism` | Merged  
`message` | `metadata.description` | Directly mapped  
`appomni.event.collected_time` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`file.created` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`raw_event.ingested` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`raw_timestamp` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`principal_machineid_present` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `NETWORK_UNCATEGORIZED`, `true` → `STATUS_HE...  
`principal_userid_present` | `metadata.event_type` | Mapped values (13 total, e.g. `true` → `GROUP_CREATION`, `true` → `GROUP_DELETION`, `true` →...  
`raw_event.dataset` | `metadata.log_type` | Directly mapped  
`raw_event.action` | `metadata.product_event_type` | Directly mapped  
`appomni.event.id` | `metadata.product_log_id` | Directly mapped  
`raw_event.reference` | `metadata.url_back_to_product` | Directly mapped  
`session.id` | `network.session_id` | Directly mapped  
`source.user.domain` | `principal.administrative_domain` | Directly mapped  
`raw_event.module` | `principal.application` | Directly mapped  
`source.host.id` | `principal.asset.asset_id` | Directly mapped  
`source.host.hostname` | `principal.asset.hostname` | Directly mapped  
`source.host.name` | `principal.asset.hostname` | Directly mapped  
`src_host_mac` | `principal.asset.mac` | Merged  
`usr_agt_os_type` | `principal.asset.platform_software.platform` | Mapped: `mac` → `MAC`, `linux` → `LINUX`, `windows` → `WINDOWS`, `chrome` → `CHROME_OS`  
`appomni.source.id` | `principal.asset.product_object_id` | Directly mapped  
`asset_soft` | `principal.asset.software` | Merged  
`source_host_type` | `principal.asset.type` | Mapped: `"workstation" , "desktop"` → `WORKSTATION`, `server` → `SERVER`, `laptop` → `LAPTOP...  
`source.as.domain` | `principal.domain.name` | Directly mapped  
`user.group.name` | `principal.group.group_display_name` | Directly mapped  
`user.group.id` | `principal.group.product_object_id` | Directly mapped  
`source.address` | `principal.ip` | Merged  
`source.ip` | `principal.ip` | Merged  
`token_appomni_service_type` | `principal.labels` | Merged  
`token_own_role` | `principal.labels` | Merged  
`token_service_id` | `principal.labels` | Merged  
`token_service_name` | `principal.labels` | Merged  
`token_source_geo_continent_code` | `principal.labels` | Merged  
`token_source_geo_continent_name` | `principal.labels` | Merged  
`token_source_geo_country_iso_code` | `principal.labels` | Merged  
`token_source_geo_postal_code` | `principal.labels` | Merged  
`token_source_geo_region_iso_code` | `principal.labels` | Merged  
`token_source_geo_timezone` | `principal.labels` | Merged  
`token_user_identity_full_name` | `principal.labels` | Merged  
`token_user_identity_id` | `principal.labels` | Merged  
`source.geo.city_name` | `principal.location.city` | Directly mapped  
`source.as.country` | `principal.location.country_or_region` | Directly mapped  
`source.geo.country_name` | `principal.location.country_or_region` | Directly mapped  
`source.geo.name` | `principal.location.name` | Directly mapped  
`source.geo.location.lat` | `principal.location.region_coordinates.latitude` | Renamed/mapped  
`source.geo.location.lon` | `principal.location.region_coordinates.longitude` | Renamed/mapped  
`source.geo.region_name` | `principal.location.state` | Directly mapped  
`src_mac` | `principal.mac` | Merged  
`source.as.number` | `principal.network.asn` | Directly mapped  
`source.domain` | `principal.network.dns_domain` | Directly mapped  
`user_agent.original` | `principal.network.http.user_agent` | Directly mapped  
`raw_event.ueba.anomalous_fields.source.as.organization.name` | `principal.network.organization_name` | Directly mapped  
`source.as.organization.name` | `principal.network.organization_name` | Directly mapped  
`user_agent_os_name` | `principal.platform` | Mapped values (6 total, e.g. `macos` → `MAC`, `linux` → `LINUX`, `windows` → `WINDOWS`)  
`source.port` | `principal.port` | Renamed/mapped  
`service_name` | `principal.resource.name` | Directly mapped  
`service_id` | `principal.resource.product_object_id` | Directly mapped  
`service_type` | `principal.resource.resource_subtype` | Directly mapped  
`pri_res_ans` | `principal.resource_ancestors` | Merged  
`princ_res_ans` | `principal.resource_ancestors` | Merged  
`token_source_user_identity_admin` | `principal.user.attribute.labels` | Merged  
`token_source_user_identity_elevated` | `principal.user.attribute.labels` | Merged  
`token_source_user_identity_email` | `principal.user.attribute.labels` | Merged  
`token_source_user_identity_full_name` | `principal.user.attribute.labels` | Merged  
`token_source_user_identity_id` | `principal.user.attribute.labels` | Merged  
`token_user_domain` | `principal.user.attribute.labels` | Merged  
`token_user_hash` | `principal.user.attribute.labels` | Merged  
`token_role` | `principal.user.attribute.roles` | Merged  
`src_user_mail` | `principal.user.email_addresses` | Merged  
`user_mail` | `principal.user.email_addresses` | Merged  
`source.user.id` | `principal.user.product_object_id` | Directly mapped  
`user.id` | `principal.user.product_object_id` | Directly mapped  
`source.user.full_name` | `principal.user.user_display_name` | Directly mapped  
`user.full_name` | `principal.user.user_display_name` | Directly mapped  
`source.user.name` | `principal.user.userid` | Directly mapped  
`user.name` | `principal.user.userid` | Directly mapped  
`appomni.event.dataset` | `security_result.action_details` | Directly mapped  
`tactics` | `security_result.attack_details.tactics` | Merged  
`technique` | `security_result.attack_details.techniques` | Merged  
`rule.threat.framework` | `security_result.attack_details.version` | Directly mapped  
`appomni.source.id` | `src.user.product_object_id` | Directly mapped  
`destination.as.domain` | `target.administrative_domain` | Directly mapped  
`destination.host.id` | `target.asset.asset_id` | Directly mapped  
`token_destination_host_name` | `target.asset.attribute.labels` | Merged  
`token_destination_host_type` | `target.asset.attribute.labels` | Merged  
`dst_mac` | `target.asset.mac` | Merged  
`destination.domain` | `target.domain.name` | Directly mapped  
`file_extension` | `target.file.file_type` | Mapped: `"EPUB", "FB2", "MOBI"` → `FILE_TYPE_EBOOK`  
`file.path` | `target.file.full_path` | Directly mapped  
`file.hash` | `target.file.md5` | Directly mapped  
`file.name` | `target.file.names` | Merged  
`file.size` | `target.file.size` | Renamed/mapped  
`destination.host.hostname` | `target.hostname` | Directly mapped  
`destination.ip` | `target.ip` | Merged  
`token_destination_geo_continent_code` | `target.labels` | Merged  
`token_destination_geo_continent_name` | `target.labels` | Merged  
`token_destination_geo_country_iso_code` | `target.labels` | Merged  
`token_destination_geo_postal_code` | `target.labels` | Merged  
`token_destination_geo_region_iso_code` | `target.labels` | Merged  
`token_destination_geo_timezone` | `target.labels` | Merged  
`token_file_id` | `target.labels` | Merged  
`destination.geo.city_name` | `target.location.city` | Directly mapped  
`destination.as.country` | `target.location.country_or_region` | Directly mapped  
`destination.geo.country_name` | `target.location.country_or_region` | Directly mapped  
`destination.geo.region_name` | `target.location.country_or_region` | Directly mapped  
`destination.geo.name` | `target.location.name` | Directly mapped  
`destination.geo.location.lat` | `target.location.region_coordinates.latitude` | Renamed/mapped  
`destination.geo.location.lon` | `target.location.region_coordinates.longitude` | Renamed/mapped  
`dst_mac` | `target.mac` | Merged  
`destination.as.number` | `target.network.asn` | Directly mapped  
`destination.as.organization.name` | `target.network.organization_name` | Directly mapped  
`destination.port` | `target.port` | Renamed/mapped  
`token_resource_owner_domain` | `target.resource.attribute.labels` | Merged  
`token_resource_owner_email` | `target.resource.attribute.labels` | Merged  
`token_resource_owner_full_name` | `target.resource.attribute.labels` | Merged  
`token_resource_owner_hash` | `target.resource.attribute.labels` | Merged  
`token_resource_owner_id` | `target.resource.attribute.labels` | Merged  
`token_resource_owner_identity_admin` | `target.resource.attribute.labels` | Merged  
`token_resource_owner_identity_elevated` | `target.resource.attribute.labels` | Merged  
`token_resource_owner_identity_email` | `target.resource.attribute.labels` | Merged  
`token_resource_owner_identity_full_name` | `target.resource.attribute.labels` | Merged  
`token_resource_owner_identity_id` | `target.resource.attribute.labels` | Merged  
`token_resource_owner_name` | `target.resource.attribute.labels` | Merged  
`resource.name` | `target.resource.name` | Directly mapped  
`resource.id` | `target.resource.product_object_id` | Directly mapped  
`resource.type` | `target.resource.resource_subtype` | Directly mapped  
`tar_res_ans` | `target.resource_ancestors` | Merged  
`raw_event.url` | `target.url` | Directly mapped  
`token_destination_user_domain` | `target.user.attribute.labels` | Merged  
`token_destination_user_hash` | `target.user.attribute.labels` | Merged  
`token_destination_user_identity_admin` | `target.user.attribute.labels` | Merged  
`token_destination_user_identity_elevated` | `target.user.attribute.labels` | Merged  
`token_destination_user_identity_email` | `target.user.attribute.labels` | Merged  
`token_destination_user_identity_full_name` | `target.user.attribute.labels` | Merged  
`token_destination_user_identity_id` | `target.user.attribute.labels` | Merged  
`token_user_target_domain` | `target.user.attribute.labels` | Merged  
`token_user_target_hash` | `target.user.attribute.labels` | Merged  
`token_user_target_identity_admin` | `target.user.attribute.labels` | Merged  
`token_user_target_identity_elevated` | `target.user.attribute.labels` | Merged  
`token_user_target_identity_email` | `target.user.attribute.labels` | Merged  
`token_user_target_identity_full_name` | `target.user.attribute.labels` | Merged  
`token_user_target_identity_id` | `target.user.attribute.labels` | Merged  
`token_role` | `target.user.attribute.roles` | Merged  
`dst_user_mail` | `target.user.email_addresses` | Merged  
`user_tar_mail` | `target.user.email_addresses` | Merged  
`user.target.id` | `target.user.product_object_id` | Directly mapped  
`destination.user.full_name` | `target.user.user_display_name` | Directly mapped  
`user.target.full_name` | `target.user.user_display_name` | Directly mapped  
`destination.user.id` | `target.user.userid` | Directly mapped  
`destination.user.name` | `target.user.userid` | Directly mapped  
`user.target.name` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `APPOMNI`  
N/A | `metadata.vendor_name` | Constant: `APPOMNI`  
N/A | `principal.asset.platform_software.platform` | Constant: `MAC`  
N/A | `principal.asset.type` | Constant: `WORKSTATION`  
N/A | `principal.platform` | Constant: `MAC`  
N/A | `principal.resource.resource_type` | Constant: `BACKEND_SERVICE`  
N/A | `target.asset.type` | Constant: `WORKSTATION`  
N/A | `target.file.file_type` | Constant: `FILE_TYPE_EBOOK`  
N/A | `target.resource.resource_type` | Constant: `CLOUD_PROJECT`  
`source.as.domain` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`raw_event.ueba.anomalous_fields.source.as.domain` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`raw_event.ueba.normal_state.source.as.domain.results` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`raw_event.ueba.normal_state.source.as.domain.counts` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`raw_event.ueba.rare_state.source.as.domain.results` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`raw_event.ueba.rare_state.source.as.domain.counts` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`raw_event.dataset` | `event.idm.read_only_udm.metadata.log_type` | Mapped from changelog  
`raw_event.duration` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`appomni.event.dataset` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`raw_event.kind` | `event.idm.read_only_udm.security_result.alert_state` | Mapped from changelog  
`raw_event.url` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`source.host.name` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`source.host.type` | `event.idm.read_only_udm.principal.asset.type` | Mapped from changelog  
`source.address` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`source.domain` | `event.idm.read_only_udm.principal.network.dns_domain` | Mapped from changelog  
`user_agent.os.name` | `event.idm.read_only_udm.principal.platform` | Mapped from changelog  
`user_agent.os.kernel` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_agent.os.platform` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`destination.host.hostname` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`destination.domain` | `event.idm.read_only_udm.target.domain.name` | Mapped from changelog  
`destination.as.country` | `event.idm.read_only_udm.target.location.country_or_region` | Mapped from changelog  
`destination.user.id` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`user.identity.admin` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user.identity.elevated` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user.identity.email` | `event.idm.read_only_udm.intermediary.email` | Mapped from changelog  
`source.user.domain` | `event.idm.read_only_udm.principal.administrative_domain` | Mapped from changelog  
`source.user.hash` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`appomni.service.slug` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`source.as.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rule.threat.tactic.reference` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rule.threat.technique.reference` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`related.services.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`related.services.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`related.services.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`policy.category` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`policy.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`policy.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`appomni.event.enrichments` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`configuration.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`configuration.old_value` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`configuration.value` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`destination.as.service` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`destination.as.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`destination.indicators` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`destination.user.indicators` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`raw_event.ueba.anomalous_fields.source.as.number` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`raw_event.ueba.anomalous_fields.source.ip` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`raw_event.ueba.normal_state.source.as.number` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`raw_event.ueba.normal_state.source.ip` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`raw_event.ueba.rare_state.source.as.number` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`raw_event.ueba.rare_state.source.ip` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`file.directory` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`labels.some_key` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`policy.description` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`policy.outcome` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.count` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.owner.indicators` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.parent.count` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.parent.owner.domain` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.parent.owner.email` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.parent.owner.full_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.parent.owner.hash` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.parent.owner.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.parent.owner.indicators` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.parent.owner.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.parent.owner.roles` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rule.vendor_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`source.as.service` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`source.user.indicators` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user.changes.indicators` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user.effective.indicators` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user.target.indicators` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user.indicators` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`appomni.source.id` | `event.idm.read_only_udm.principal.asset.product_object_id` | Mapped from changelog  
`source.as.country` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`source.as.domain` | `event.idm.read_only_udm.principal.domain.name` | Mapped from changelog  
`rule.threat.framework` | `event.idm.read_only_udm.security_result.attack_details.version` | Mapped from changelog  
`rule.threat.tactic.id` | `event.idm.read_only_udm.security_result.attack_details.tactics.id` | Mapped from changelog  
`rule.threat.tactic.name` | `event.idm.read_only_udm.security_result.attack_details.tactics.name` | Mapped from changelog  
`rule.threat.technique.id` | `event.idm.read_only_udm.security_result.attack_details.techniques.id` | Mapped from changelog  
`rule.threat.technique.name` | `event.idm.read_only_udm.security_result.attack_details.techniques.name` | Mapped from changelog  
`appomni.source.id` | `event.idm.read_only_udm.src.user.product_object_id` | Mapped from changelog  
`file.hash` | `event.idm.read_only_udm.target.file.md5` | Mapped from changelog  
`user.identity.full_name` | `event.idm.read_only_udm.intermediary.user.user_display_name` | Mapped from changelog  
`user.identity.id` | `event.idm.read_only_udm.intermediary.user.userid` | Mapped from changelog  
`destination.as.domain` | `event.idm.read_only_udm.target.administrative_domain` | Mapped from changelog  
`event.ueba.normal_state.authentication.raw_method.counts", "event.ueba.normal_state.authentication.raw_method.results", "event.ueba.normal_state.source.as.organization.name.results", "event.ueba.normal_state.source.as.organization.name.counts", "event.ueba.rare_state.authentication.raw_method.counts", "event.ueba.rare_state.authentication.raw_method.results", "event.ueba.rare_state.source.as.organization.name.results", and "event.ueba.rare_state.source.as.organization.name.counts` | `additional.fields` | Mapped from changelog  
`resource.metadata.application` | `target.application` | Mapped from changelog  
`resource.metadata.entities` | `target.resource.attribute.labels` | Mapped from changelog  
`resource.metadata.query` | `target.process.command_line` | Mapped from changelog  
`resource.metadata.row_count` | `target.resource.attribute.labels` | Mapped from changelog  
`resource.metadata.type` | `target.resource.attribute.labels` | Mapped from changelog  
`resource.metadata.action_message` | `security_results.action_details` | Mapped from changelog  
`resource.metadata.language` | `security_results.about.label` | Mapped from changelog  
`labels.user_location` | `principal.asset.location.name` | Mapped from changelog  
`labels.login_key` | `principal.resource.attribute.labels` | Mapped from changelog  
`user.hash` | `principal.resource.attribute.labels` | Mapped from changelog  
`user.roles` | `principal.resource.attribute.labels` | Mapped from changelog  
`host.os.name` | `target.asset.platform_software.platform` | Mapped from changelog  
`host.os.version` | `target.asset.platform_software.platform_version` | Mapped from changelog  
`http.request.method` | `network.http.method` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/appomni-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
