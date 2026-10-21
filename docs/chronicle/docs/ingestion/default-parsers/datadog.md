---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/datadog/
title: Collect Datadog logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:41:34.943898+00:00
---

# Collect Datadog logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/datadog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Datadog logs

**Parser Version:** 4.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Datadog logs to Google Security Operations. Datadog is a cloud-based monitoring and analytics platform that collects metrics, traces, and logs from applications, infrastructure, and cloud services. You can share Datadog logs to Google SecOps using either Cloud Storage or a webhook.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * Privileged user access to Datadog
  * Access to Google Cloud console (for API key creation or Cloud Storage configuration)



## Option 1: Datadog log sharing through Cloud Storage configuration

### Configure Datadog integration with Google Cloud

Set up an integration for [Google Cloudin Datadog](https://app.datadoghq.com/integrations/google-cloud-platform). For more information, see the [Datadog Google Cloud integration setup](https://docs.datadoghq.com/integrations/google_cloud_platform/?tab=dataflowmethodrecommended#setup).

### Create a Cloud Storage Bucket

  1. Sign in to the Google Cloud console.
  2. Go to the **Cloud Storage Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  3. Click **Create**.

  4. On the **Create a bucket** page, enter your bucket information. After each of the following steps, click **Continue** to proceed to the next step:

     1. In the **Get started** section, do the following:

        1. Enter a unique name that meets the bucket name requirements (for example, `datadog-data`).
        2. To enable hierarchical namespace, click the expander arrow to expand the **Optimize for file oriented and data-intensive workloads** section, and then select **Enable Hierarchical namespace on this bucket**.

**Note:** You cannot enable hierarchical namespace in an existing bucket.
        3. To add a bucket label, click the expander arrow to expand the **Labels** section.

        4. Click **Add label** , and specify a key and a value for your label.

     2. In the **Choose where to store your data** section, do the following:

        1. Select a **Location type**.
        2. Use the location type drop-down to select a **Location** where object data within your bucket will be permanently stored.
     3. In the **Choose a storage class for your data** section, either select a **default storage class** for the bucket, or select **Autoclass** for automatic storage class management of your bucket's data.

     4. In the **Choose how to control access to objects** section, select **not** to enforce **public access prevention** , and select an **access control model** for your bucket's objects.

     5. In the **Choose how to protect object data** section, do the following:

        1. Select any of the options under **Data protection** that you want to set for your bucket.
        2. To choose how your object data will be encrypted, click the expander arrow labeled **Data encryption** , and select a **Data encryption method**.
  5. Click **Create**.

**Note:** Do not add a retention policy, as the latest data must be rewritten in case of a timeout.



### Create a Google Cloud Service Account

  1. Go to **IAM & Admin > Service Accounts**.
  2. Create a new service account.
  3. Give it a descriptive name (for example, `datadog-user`).
  4. Grant the service account with **Storage Object Admin** role on the Cloud Storage bucket you created in the previous step.
  5. [Create a key](https://docs.cloud.google.com/iam/docs/keys-create-delete) for the service account and select **JSON** as the key type.
  6. Download the JSON key file for the service account. Keep this file secure.



### Configure Datadog to send logs to Cloud Storage

  1. Sign in to Datadog using a privileged account.
  2. Go to **Logs > Log Forwarding**.
  3. Click **\+ Create New Archive**.
  4. Select **Google Cloud Storage**.
  5. Input the required parameters and click **Save**.



### Configure a feed in Google SecOps to ingest logs from the Cloud Storage bucket

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Datadog Logs GCS`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Datadog** as the **Log type**.
  7. Click **Get Service Account** to obtain the unique service account for this feed.
  8. Grant this service account the **Storage Object Viewer** role on the Cloud Storage bucket created earlier.
  9. Click **Next**.
  10. Specify values for the following input parameters: 
     * **Storage Bucket URI** : The CCloud Storage bucket URI in the format `gs://datadog-data`.
     * **Source deletion option** : Select the deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label applied to the events from this feed.
  11. Click **Next**.
  12. Review the feed configuration in the **Finalize** screen, and then click **Submit**.



## Option 2: Datadog log sharing through Webhook configuration

### Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Datadog Logs`).
  5. Select **Webhook** as the **Source type**.
  6. Select **Datadog** as the **Log type**.
  7. Click **Next**.
  8. Optional: Specify values for the following input parameters: 
     * **Split delimiter** : the delimiter that is used to separate log lines, such as `\n`.
  9. Click **Next**.
  10. Review the feed configuration in the **Finalize** screen, and then click **Submit**.
  11. Click **Generate Secret Key** to generate a secret key to authenticate this feed.
  12. Copy and store the secret key. You cannot view this secret key again. If needed, you can regenerate a new secret key, but this action makes the previous secret key obsolete.
  13. From the **Details** tab, copy the feed endpoint URL from the **Endpoint Information** field. You need to specify this endpoint URL in your client application.
  14. Click **Done**.



### Create an API key for the webhook feed

  1. Go to **Google Cloud console > Credentials**: [Go to Credentials](https://console.cloud.google.com/apis/credentials).
  2. Click **Create credentials** , and then select **API key**.
  3. Restrict the API key access to the **Chronicle API**.



### Specify the endpoint URL

  1. In your client application, specify the HTTPS endpoint URL provided in the webhook feed.
  2. Enable authentication by specifying the API key and secret key as part of the custom header in the following format:
         
         X-goog-api-key = API_KEY
         X-Webhook-Access-Key = SECRET
         

Recommendation: Specify the API key as a header instead of specifying it in the URL.

  3. If your webhook client doesn't support custom headers, you can specify the API key and secret key using query parameters in the following format:
         
         ENDPOINT_URL?key=API_KEY&secret=SECRET
         

Replace the following:

     * `ENDPOINT_URL`: the feed endpoint URL.
     * `API_KEY`: the API key to authenticate to Google Security Operations.
     * `SECRET`: the secret key that you generated to authenticate the feed.



### Configure Datadog to send logs to webhook

  1. Sign in to Datadog using a privileged account.
  2. Go to **Logs > Log Forwarding**.
  3. Select **Custom Destinations**.
  4. Click **\+ Create a New Destination**.
  5. Specify values for the following input parameters: 
     * **Choose a destination type** : Select **HTTP**.
     * **Name the destination** : Provide a descriptive name for the webhook (for example, `Google SecOps Webhook`).
     * **Configure the destination** : Paste the feed **ENDPOINT_URL**. Choose one of the following authentication options (not both): 
       * Option A (recommended): leave the URL without credentials and pass **API_KEY** and **SECRET** as custom headers (configured in the next step).
       * Option B: append the credentials to the URL as query parameters, in the format `ENDPOINT_URL?key=API_KEY&secret=SECRET`. Use this only if the client cannot send custom headers.
     * **Configure authentication settings** : Datadog requires at least one authentication header to save the destination. Add the following header. The webhook endpoint ignores it, so it does not affect the request. 
       * Header name: `Authorization`.
       * Header value: `application/json`.
  6. Click **Save**.



## Reference links

  * [Sharing Logs to CCloud Storage](https://docs.datadoghq.com/logs/log_configuration/archives/?tab=googlecloudstorage)
  * [Forwarding Logs to Webhook](https://docs.datadoghq.com/logs/log_configuration/forwarding_custom_destinations/?tab=http)



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`additional_field` | `additional.fields` | Merged  
`anonymous_label` | `additional.fields` | Merged  
`as_domain_label` | `additional.fields` | Merged  
`as_name_label` | `additional.fields` | Merged  
`as_number_label` | `additional.fields` | Merged  
`as_type_label` | `additional.fields` | Merged  
`auth_method_label` | `additional.fields` | Merged  
`category_label` | `additional.fields` | Merged  
`emitted_source_label` | `additional.fields` | Merged  
`event_type_label` | `additional.fields` | Merged  
`geo_continent_code_label` | `additional.fields` | Merged  
`geo_continent_label` | `additional.fields` | Merged  
`geo_continent_name_label` | `additional.fields` | Merged  
`geo_country_code_label` | `additional.fields` | Merged  
`geo_latitude_label` | `additional.fields` | Merged  
`geo_longitude_label` | `additional.fields` | Merged  
`geo_subdivision_code_label` | `additional.fields` | Merged  
`geo_subdivision_name_label` | `additional.fields` | Merged  
`geo_timezone_label` | `additional.fields` | Merged  
`http_level_label` | `additional.fields` | Merged  
`indicator_label` | `additional.fields` | Merged  
`indicators_matched_label` | `additional.fields` | Merged  
`infrastructure_label` | `additional.fields` | Merged  
`intention_label` | `additional.fields` | Merged  
`iso_code_label` | `additional.fields` | Merged  
`new_template_variable_name_label` | `additional.fields` | Merged  
`new_template_variable_preset_name_label` | `additional.fields` | Merged  
`new_template_variable_value_label` | `additional.fields` | Merged  
`new_widget_definition_background_color_label` | `additional.fields` | Merged  
`new_widget_definition_layout_type_label` | `additional.fields` | Merged  
`new_widget_definition_show_title_label` | `additional.fields` | Merged  
`new_widget_definition_title_label` | `additional.fields` | Merged  
`new_widget_definition_type_label` | `additional.fields` | Merged  
`new_widget_id_label` | `additional.fields` | Merged  
`new_widget_layout_height_label` | `additional.fields` | Merged  
`new_widget_layout_width_label` | `additional.fields` | Merged  
`new_widget_layout_x_label` | `additional.fields` | Merged  
`new_widget_layout_y_label` | `additional.fields` | Merged  
`record_attributes_asset_id_label` | `additional.fields` | Merged  
`record_attributes_asset_name_label` | `additional.fields` | Merged  
`record_attributes_asset_new_value_dashboard_definition_author_handle_label` | `additional.fields` | Merged  
`record_attributes_asset_new_value_dashboard_definition_author_name_label` | `additional.fields` | Merged  
`record_attributes_asset_new_value_dashboard_definition_description_label` | `additional.fields` | Merged  
`record_attributes_asset_new_value_dashboard_definition_id_label` | `additional.fields` | Merged  
`record_attributes_asset_new_value_dashboard_definition_reflow_type_label` | `additional.fields` | Merged  
`record_attributes_asset_new_value_dashboard_definition_title_label` | `additional.fields` | Merged  
`record_attributes_asset_new_value_dashboard_definition_url_label` | `additional.fields` | Merged  
`record_attributes_asset_prev_value_dashboard_definition_author_handle_label` | `additional.fields` | Merged  
`record_attributes_asset_prev_value_dashboard_definition_author_name_label` | `additional.fields` | Merged  
`record_attributes_asset_prev_value_dashboard_definition_description_label` | `additional.fields` | Merged  
`record_attributes_asset_prev_value_dashboard_definition_id_label` | `additional.fields` | Merged  
`record_attributes_asset_prev_value_dashboard_definition_reflow_type_label` | `additional.fields` | Merged  
`record_attributes_asset_prev_value_dashboard_definition_title_label` | `additional.fields` | Merged  
`record_attributes_asset_prev_value_dashboard_definition_url_label` | `additional.fields` | Merged  
`record_attributes_asset_type_label` | `additional.fields` | Merged  
`record_attributes_contextMap_cfRay_label` | `additional.fields` | Merged  
`record_attributes_contextMap_tradingAccountId_label` | `additional.fields` | Merged  
`record_attributes_evt_name_label` | `additional.fields` | Merged  
`record_attributes_network_client_geoip_as_number_label` | `additional.fields` | Merged  
`record_attributes_network_client_geoip_as_type_label` | `additional.fields` | Merged  
`record_attributes_network_client_geoip_location_latitude_label` | `additional.fields` | Merged  
`record_attributes_network_client_geoip_location_longitude_label` | `additional.fields` | Merged  
`record_attributes_network_client_geoip_subdivision_iso_code_label` | `additional.fields` | Merged  
`record_attributes_network_client_geoip_subdivision_name_label` | `additional.fields` | Merged  
`record_attributes_network_client_geoip_timezone_label` | `additional.fields` | Merged  
`record_trace_id_label` | `additional.fields` | Merged  
`request_id_label` | `additional.fields` | Merged  
`risk_label` | `additional.fields` | Merged  
`service_label` | `additional.fields` | Merged  
`source_name_label` | `additional.fields` | Merged  
`source_type_label` | `additional.fields` | Merged  
`source_url_label` | `additional.fields` | Merged  
`span_id_label` | `additional.fields` | Merged  
`symbol_label` | `additional.fields` | Merged  
`tag_label` | `additional.fields` | Merged  
`template_variable_name_label` | `additional.fields` | Merged  
`template_variable_preset_name_label` | `additional.fields` | Merged  
`template_variable_value_label` | `additional.fields` | Merged  
`timezone_label` | `additional.fields` | Merged  
`tunnels_operator_label` | `additional.fields` | Merged  
`tunnels_type_label` | `additional.fields` | Merged  
`type_label` | `additional.fields` | Merged  
`type_label1` | `additional.fields` | Merged  
`url_details_host_label` | `additional.fields` | Merged  
`url_details_path_label` | `additional.fields` | Merged  
`user_created_timestamp_label` | `additional.fields` | Merged  
`widget_definition_background_color_label` | `additional.fields` | Merged  
`widget_definition_layout_type_label` | `additional.fields` | Merged  
`widget_definition_show_title_label` | `additional.fields` | Merged  
`widget_definition_title_label` | `additional.fields` | Merged  
`widget_definition_type_label` | `additional.fields` | Merged  
`widget_id_label` | `additional.fields` | Merged  
`widget_layout_height_label` | `additional.fields` | Merged  
`widget_layout_width_label` | `additional.fields` | Merged  
`widget_layout_x_label` | `additional.fields` | Merged  
`widget_layout_y_label` | `additional.fields` | Merged  
`eventMessage` | `metadata.description` | Directly mapped  
`date1` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`record.date1` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`event_type` | `metadata.event_type` | Directly mapped  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`attributes._trace.origin.operation` | `metadata.product_event_type` | Directly mapped  
`eventType` | `metadata.product_event_type` | Directly mapped  
`record_attributes_contextMap_eventType` | `metadata.product_event_type` | Directly mapped  
`source` | `metadata.product_event_type` | Directly mapped  
`_id` | `metadata.product_log_id` | Directly mapped  
`record_attributes_thread_id` | `metadata.product_log_id` | Directly mapped  
`threadID` | `metadata.product_log_id` | Directly mapped  
`service` | `metadata.product_name` | Directly mapped  
`attributes.@version` | `metadata.product_version` | Directly mapped  
`attributes.http.method` | `network.http.method` | Directly mapped  
`agnt` | `network.http.parsed_user_agent` | Directly mapped  
`record_attributes_contextMap_userAgent` | `network.http.parsed_user_agent` | Directly mapped  
`attributes.http.status_code` | `network.http.response_code` | Renamed/mapped  
`agnt` | `network.http.user_agent` | Directly mapped  
`attributes.http.useragent` | `network.http.user_agent` | Directly mapped  
`record_attributes_contextMap_userAgent` | `network.http.user_agent` | Directly mapped  
`attributes.logger_name` | `principal.application` | Directly mapped  
`service` | `principal.application` | Directly mapped  
`attributes._trace.baggage.device_id` | `principal.asset.asset_id` | Directly mapped  
`attributes.metadata.host_metadata.hostname` | `principal.asset.hostname` | Directly mapped  
`attributes.usr.id` | `principal.asset.hostname` | Directly mapped  
`attributes.network.client.geoip.ipAddress` | `principal.asset.ip` | Merged  
`attributes.network.client.ip` | `principal.asset.ip` | Merged  
`ip1` | `principal.asset.ip` | Merged  
`ipAddress` | `principal.asset.ip` | Directly mapped  
`principal_ip_address` | `principal.asset.ip` | Merged  
`record_attributes_network_client_ip` | `principal.asset.ip` | Merged  
`org` | `principal.group.group_display_name` | Directly mapped  
`attributes.org.uuid` | `principal.group.product_object_id` | Directly mapped  
`attributes.metadata.host_metadata.hostname` | `principal.hostname` | Directly mapped  
`attributes.usr.id` | `principal.hostname` | Directly mapped  
`host` | `principal.hostname` | Directly mapped  
`record_host` | `principal.hostname` | Directly mapped  
`attributes.network.client.geoip.ipAddress` | `principal.ip` | Merged  
`attributes.network.client.ip` | `principal.ip` | Merged  
`ip1` | `principal.ip` | Merged  
`ipAddress` | `principal.ip` | Directly mapped  
`principal_ip_address` | `principal.ip` | Merged  
`record_attributes_network_client_ip` | `principal.ip` | Merged  
`record_attributes_http_url_details_host_label` | `principal.labels` | Merged  
`record_attributes_http_url_details_path_label` | `principal.labels` | Merged  
`record_attributes_http_useragent_label` | `principal.labels` | Merged  
`record_attributes_network_client_geoip_as_domain_label` | `principal.labels` | Merged  
`record_attributes_network_client_geoip_as_route_label` | `principal.labels` | Merged  
`record_attributes_network_client_geoip_city_name_label` | `principal.labels` | Merged  
`record_attributes_network_client_geoip_continent_code_label` | `principal.labels` | Merged  
`record_attributes_network_client_geoip_continent_name_label` | `principal.labels` | Merged  
`record_attributes_network_client_geoip_country_iso_code_label` | `principal.labels` | Merged  
`record_attributes_network_client_geoip_country_name_label` | `principal.labels` | Merged  
`record_attributes_usr_id_label` | `principal.labels` | Merged  
`attributes.network.client.geoip.city.name` | `principal.location.city` | Directly mapped  
`attributes.network.client.geoip.country.name` | `principal.location.country_or_region` | Directly mapped  
`port` | `principal.port` | Renamed/mapped  
`client_as_route_label` | `principal.resource.attribute.labels` | Merged  
`client_type_label` | `principal.resource.attribute.labels` | Merged  
`org_name_label` | `principal.resource.attribute.labels` | Merged  
`record_attributes_usr_uuid_label` | `principal.user.attribute.labels` | Merged  
`roles` | `principal.user.attribute.roles` | Merged  
`attributes.usr.email` | `principal.user.email_addresses` | Merged  
`email_id` | `principal.user.email_addresses` | Merged  
`record_attributes_usr_email` | `principal.user.email_addresses` | Merged  
`attributes.evt.actor.type` | `principal.user.role_name` | Directly mapped  
`attributes.metadata.user_uuid` | `principal.user.userid` | Directly mapped  
`attributes.usr.uuid` | `principal.user.userid` | Directly mapped  
`record_attributes_contextMap_user` | `principal.user.userid` | Directly mapped  
`user` | `principal.user.userid` | Directly mapped  
`BusArch_label` | `security_result.about.resource.attribute.labels` | Merged  
`CANDBVersion_label` | `security_result.about.resource.attribute.labels` | Merged  
`alert_label` | `security_result.about.resource.attribute.labels` | Merged  
`caller_label` | `security_result.about.resource.attribute.labels` | Merged  
`component_label` | `security_result.about.resource.attribute.labels` | Merged  
`esn_label` | `security_result.about.resource.attribute.labels` | Merged  
`ftcpVersion_label` | `security_result.about.resource.attribute.labels` | Merged  
`ingestMessageId_label` | `security_result.about.resource.attribute.labels` | Merged  
`label` | `security_result.about.resource.attribute.labels` | Merged  
`level_label` | `security_result.about.resource.attribute.labels` | Merged  
`msg_label` | `security_result.about.resource.attribute.labels` | Merged  
`query_label` | `security_result.about.resource.attribute.labels` | Merged  
`redactedVin_label` | `security_result.about.resource.attribute.labels` | Merged  
`updated_query_label` | `security_result.about.resource.attribute.labels` | Merged  
`vehicleId_label` | `security_result.about.resource.attribute.labels` | Merged  
`category1` | `security_result.category_details` | Merged  
`_id_label` | `security_result.detection_fields` | Merged  
`action_label` | `security_result.detection_fields` | Merged  
`org_uuid_label` | `security_result.detection_fields` | Merged  
`record_attributes_http_method_label` | `security_result.detection_fields` | Merged  
`record_message_label` | `security_result.detection_fields` | Merged  
`record_source_label` | `security_result.detection_fields` | Merged  
`record_status_label` | `security_result.detection_fields` | Merged  
`status` | `security_result.severity` | Mapped: `"INFO", "DEBUG", "debug", "info"` → `LOW`, `(?i)WARN` → `MEDIUM`  
`status` | `security_result.severity_details` | Directly mapped  
`context.AlertName` | `security_result.threat_name` | Directly mapped  
`src_ip_address` | `src.ip` | Merged  
`record_attributes_contextMap_dd_service` | `target.application` | Directly mapped  
`target_ip_address` | `target.asset.ip` | Mapped: `^(?:[0-9]{1,3}[.]){3}[0-9]{1,3}$` → `target_ip_address`  
`target_ip_address` | `target.ip` | Mapped: `^(?:[0-9]{1,3}[.]){3}[0-9]{1,3}$` → `target_ip_address`  
`record_attributes_contextMap_dd_version` | `target.platform_version` | Directly mapped  
`logger_fqcn_label` | `target.resource.attribute.labels` | Merged  
`logger_label` | `target.resource.attribute.labels` | Merged  
`modified_fields_label` | `target.resource.attribute.labels` | Merged  
`asset_name` | `target.resource.name` | Directly mapped  
`asset_id` | `target.resource.product_object_id` | Directly mapped  
`asset_type` | `target.resource.type` | Directly mapped  
`record_attributes_contextMap_dd_env` | `target.resource.type` | Directly mapped  
`record_attributes_contextMap_userId` | `target.user.userid` | Directly mapped  
`record_attributes_user` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `NETWORK_CONNECTION`  
N/A | `network.http.parsed_user_agent` | Constant: `parseduseragent`  
N/A | `security_result.severity` | Constant: `LOW`  
`org_name` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`modified_field` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`asset_name` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`asset_id` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`asset_type` | `event.idm.read_only_udm.target.resource.type` | Mapped from changelog  
`query` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`updated_query` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`request_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`http_level` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`timezone` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`iso_code` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_created_timestamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`client_as_route` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`client_type` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`source` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`status` | `event.idm.read_only_udm.security_result.severity_details` | Mapped from changelog  
`record.attributes.user` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`user` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`eventType` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`ipAddress` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`ipAddress` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`threadID` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`status` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`service` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`eventMessage` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`tags` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.attributes.contextMap.userId` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`record.attributes.contextMap.user` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`record.attributes.contextMap.eventType` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`record.attributes.contextMap.userAgent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`record.attributes.contextMap.userAgent` | `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
`record.attributes.contextMap.tradingAccountId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`principal_ip_address` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`principal_ip_address` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`target_ip_address` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`target_ip_address` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`record.attributes.contextMap.cfRay` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.attributes.contextMap.symbol` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.attributes.contextMap.dd.version` | `event.idm.read_only_udm.target.platform_version` | Mapped from changelog  
`record.attributes.contextMap.dd.env` | `event.idm.read_only_udm.target.resource.type` | Mapped from changelog  
`record.attributes.contextMap.dd.service` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`record.attributes.logger` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`record.attributes.loggerFqcn` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`record.attributes.threadId` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`record.trace_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.span_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.service` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.attributes.level` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`record.host` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/datadog-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
