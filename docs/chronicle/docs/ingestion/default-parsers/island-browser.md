---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/island-browser/
title: Collect Island Enterprise Browser logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:45.373127+00:00
---

# Collect Island Enterprise Browser logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/island-browser/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Island Enterprise Browser logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to configure Island Enterprise Browser to push logs to Google Security Operations using webhooks.

Island Enterprise Browser is a Chromium-based enterprise browser designed to enhance corporate security and IT governance. It enables organizations to control and monitor how users interact with web applications, providing fine-grained policy control over every facet of browser activity including copy, paste, download, upload, and screenshot capture. Island delivers complete visibility, governance, and compliance for critical SaaS and internal web applications while supporting built-in safe browsing, web filtering, exploit prevention, and Zero Trust network access.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * Island Enterprise Browser supports webhook-based SIEM log delivery via HTTPS
  * Access to Google Cloud Console (for API key creation)
  * Access to the Island Management Console with administrator permissions (Full Admin or System Admin role)



## Create webhook feed in Google SecOps

### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Island Enterprise Browser Logs`).
  5. Select **Webhook** as the **Source type**.
  6. Select **Island Enterprise Browser** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** (optional): Enter `\n` to split NDJSON events by newline
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



### Generate and save secret key

After creating the feed, you must generate a secret key for authentication:

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. **Copy and save** the secret key securely.



**Important** : The secret key is displayed only once and cannot be retrieved later. If you lose it, you must generate a new secret key.

### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**.
  3. The URL format is:
         
         https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import
         

Where `{region}` is the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`), and `{parent}` is the resource path in the format `projects/<PROJECT_ID>/locations/<LOCATION>/instances/<INSTANCE_ID>/logTypes/<LOG_TYPE>`.

  4. Save this URL for the next steps.

  5. Click **Done**.




## Create Google Cloud API key

Chronicle requires an API key for authentication. Create a restricted API key in the Google Cloud Console.

### Create the API key

  1. Go to the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project (the project associated with your Chronicle instance).
  3. Click **Create credentials > API key**.
  4. An API key is created and displayed in a dialog.
  5. Click **Edit API key** to restrict the key.



### Restrict the API key

  1. In the **API key** settings page: 
     * **Name** : Enter a descriptive name (for example, `Chronicle Webhook API Key - Island`)
  2. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the **Select APIs** dropdown, search for and select **Google SecOps API** (or **Chronicle API**).
  3. Click **Save**.
  4. **Copy** the API key value from the **API key** field at the top of the page.
  5. Save the API key securely.

**Note:** Restricting the API key ensures it can only be used with the Chronicle API, reducing security risk if the key is compromised.

## Configure Island Enterprise Browser webhook

### Construct the webhook URL

  * Combine the Chronicle endpoint URL and API key:
        
        <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
        

  * **Example:**
        
        https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...&secret=abcd1234...
        




### Create the SIEM integration in Island Management Console

  1. Sign in to the **Island Management Console** as an administrator (Full Admin or System Admin).
  2. Navigate to **Modules > Platform Settings > System Settings > Integrations > SIEM**.
  3. Click **Setup** for the **Generic SIEM Integration**.
  4. The **Generic SIEM Integration Settings** drawer is displayed.
  5. In the **Authentication Type** field, select **HTTPS**.
  6. In the **Server URL** field, paste the complete webhook URL constructed in the previous step (the Chronicle endpoint URL with the API key and secret key appended as query parameters).
  7. Click **Check Connection** to confirm the connection to the configured endpoint.
  8. Click **Create Integration**.
  9. If the integration is successful, the **Up and Running** status is displayed below the **Settings** button for the Generic SIEM Integration.

**Note:** Island Enterprise Browser sends logs in NDJSON format. Each line represents a single event containing fields such as `tenant_id`, `timestamp`, `email`, `user_id`, `user_name`, `type`, `verdict`, `device_id`, `source_ip`, `public_ip`, `top_level_url`, `rule_id`, `rule_name`, `saas_application_name`, and `machine_name`.

### Generate a SIEM API key (alternative method)

If the Generic SIEM Integration requires an API key for authentication instead of HTTPS URL parameters, generate one as follows:

  1. Sign in to the **Island Management Console** as an administrator.
  2. Navigate to **Modules > Platform Settings > System Settings > Integrations > SIEM**.
  3. Click **Setup** for the **Generic SIEM Integration**.
  4. Click **Generate API Key** to create a new key.
  5. The **Create a New API Key Integration** drawer is displayed, showing the generated API key.
  6. **Copy the API Key** to your clipboard and save it securely.
  7. Click **Close**.



**Important** : The API key is displayed only once during generation. Copy and save it immediately.

### Required permissions

The Island Management Console account used to configure the SIEM integration must have one of the following roles:

Role | Description  
---|---  
**Full Admin** | Full administrative access to the Island Management Console  
**System Admin** | System-level administrative access with permissions to manage integrations  
  
## Authentication methods reference

Chronicle webhook feeds support multiple authentication methods. Choose the method that your vendor supports.

### Method 1: Custom headers (Recommended)

If your vendor supports custom HTTP headers, use this method for better security.

  * **Request format:**
        
        POST <ENDPOINT_URL> HTTP/1.1
        Content-Type: application/json
        x-goog-chronicle-auth: <API_KEY>
        x-chronicle-auth: <SECRET_KEY>
        
        {
                "event": "data",
                "timestamp": "2025-01-15T10:30:00Z"
        }
        




**Advantages:**

  * API key and secret not visible in URL
  * More secure (headers not logged in web server access logs)
  * Preferred method when vendor supports it



### Method 2: Query parameters

If your vendor does not support custom headers, append credentials to the URL.

  * **URL format:**
        
        <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
        

  * **Example:**
        
        https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...&secret=abcd1234...
        

  * **Request format:**
        
        POST <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY> HTTP/1.1
        Content-Type: application/json
        
        {
                "event": "data",
                "timestamp": "2025-01-15T10:30:00Z"
        }
        




**Disadvantages:**

  * Credentials visible in URL
  * May be logged in web server access logs
  * Less secure than headers



### Method 3: Hybrid (URL + Header)

Some configurations use API key in URL and secret key in header.

  * **Request format:**
        
        POST <ENDPOINT_URL>?key=<API_KEY> HTTP/1.1
        Content-Type: application/json
        x-chronicle-auth: <SECRET_KEY>
        
        {
                "event": "data",
                "timestamp": "2025-01-15T10:30:00Z"
        }
        




### Authentication header names

Chronicle accepts the following header names for authentication:

**For API key:**

  * `x-goog-chronicle-auth` (recommended)
  * `X-Goog-Chronicle-Auth` (case-insensitive)



**For secret key:**

  * `x-chronicle-auth` (recommended)
  * `X-Chronicle-Auth` (case-insensitive)



## Webhook limits and best practices

### Request limits

Limit | Value  
---|---  
**Max request size** | 4 MB  
**Max QPS (queries per second)** | 15,000  
**Request timeout** | 30 seconds  
**Retry behavior** | Automatic with exponential backoff  
  
## Regional API endpoints

Island Enterprise Browser uses different Management Console URLs based on your region:

Region | Management Console URL | API Base URL  
---|---|---  
**US** | `https://management.island.io` | `https://management.island.io/api/external/v1/`  
**EU** | `https://eu.management.island.io` | `https://eu.management.island.io/api/external/v1/`  
  
Use the Management Console URL that corresponds to your Island Enterprise Browser tenant region.

## UDM mapping table

The following table lists the log fields of the `ISLAND_BROWSER` log type and their corresponding UDM fields.

Log field | UDM mapping  
---|---  
`timestamp` | `metadata.event_timestamp`  
`id` | `metadata.product_log_id`  
`type` | `metadata.product_event_type`  
`email` | `principal.user.email_addresses`  
`user_id` | `principal.user.userid`  
`user_name` | `principal.user.user_display_name`  
`source_ip` | `principal.ip`, `principal.asset.ip`  
`public_ip` | `principal.ip`, `principal.asset.ip`  
`machine_name` | `principal.hostname`, `principal.asset.hostname`  
`machine_id` | `principal.asset.asset_id`  
`os_platform` | `principal.asset.platform_software.platform`  
`country` | `principal.location.country_or_region`  
`region` | `principal.location.state`  
`top_level_url` | `target.url`  
`saas_application_name` | `target.application`  
`saas_application_id` | `target.resource.id`  
`rule_id` | `security_result.rule_id`  
`rule_name` | `security_result.rule_name`  
`verdict` | `security_result.action_details`  
`verdict_reason` | `security_result.description`  
`url_web_reputation` | `security_result.confidence_score`  
`saas_application_category` | `security_result.category_details`  
`client_event_id` | `network.session_id`  
`version` | `metadata.product_version`  
`window_id` | `principal.resource.id`  
`frame_url` | `about.url`  
`device_id` | `principal.asset.attribute.labels`  
`os_user_name` | `principal.asset.attribute.labels`  
`tab_id` | `security_result.detection_fields`  
`signature` | `security_result.detection_fields`  
`compatibility_mode` | `additional.fields`  
`processed_date` | `additional.fields`  
`country_code` | `additional.fields`  
`is_island_private_access` | `additional.fields`  
`url_web_categories` | `additional.fields`  
`origin` | `additional.fields`  
`tenant_id` | `additional.fields`  
`matched_user_group` | `principal.group.group_display_name`  
`matched_device_posture.domain` | `principal.domain.name`  
`details.application_parameters_details_list.parameters.parameter_value` | `event.idm.read_only_udm.target.resource_ancestors.name`  
`details.application_parameters_details_list.parameters.parameter_value` | `event.idm.read_only_udm.target.administrative_domain`  
`details.application_parameters_details_list.parameters.parameter_name` | `event.idm.read_only_udm.additional.fields`  
`matchedDevicePosture.azure_ad` | `event.idm.read_only_udm.additional.fields`  
`matchedDevicePosture.registry_keys` | `event.idm.read_only_udm.additional.fields`  
`matchedDevicePosture.client_certificates` | `event.idm.read_only_udm.security_result.detection_fields`  
`logMessage.userId` | `event.idm.read_only_udm.principal.user.userid`  
`logMessage.email` | `event.idm.read_only_udm.principal.user.email_addresses`  
`logMessage.userName` | `event.idm.read_only_udm.principal.user.user_display_name`  
`logMessage.type` | `event.idm.read_only_udm.metadata.product_event_type`  
`logMessage.verdict` | `event.idm.read_only_udm.security_result.action_details`  
`logMessage.topLevelUrl` | `event.idm.read_only_udm.network.http.referral_url`  
`logMessage.sourceIp` | `event.idm.read_only_udm.principal.ip`  
`logMessage.publicIp` | `event.idm.read_only_udm.principal.ip`  
`logMessage.sourceIp` | `event.idm.read_only_udm.principal.asset.ip`  
`logMessage.publicIp` | `event.idm.read_only_udm.principal.asset.ip`  
`logMessage.saasApplicationName` | `event.idm.read_only_udm.target.application`  
`logMessage.saasApplicationCategory` | `event.idm.read_only_udm.security_result.category_details`  
`logMessage.country` | `event.idm.read_only_udm.principal.location.country_or_region`  
`logMessage.region` | `event.idm.read_only_udm.principal.location.state`  
`logMessage.osUserName` | `event.idm.read_only_udm.principal.administrative_domain`  
`logMessage.machineId` | `event.idm.read_only_udm.principal.asset.asset_id`  
`logMessage.saasApplicationId` | `event.idm.read_only_udm.target.resource.product_object_id`  
`logMessage.timestamp` | `event.idm.read_only_udm.metadata.event_timestamp`  
`logMessage.tenantId` | `event.idm.read_only_udm.metadata.product_deployment_id`  
`logMessage.id` | `event.idm.read_only_udm.metadata.product_log_id`  
`logMessage.createdDate` | `event.idm.read_only_udm.target.resource.attribute.creation_time`  
`logMessage.updatedDate` | `event.idm.read_only_udm.target.resource.attribute.last_update_time`  
`logMessage.frameUrl` | `event.idm.read_only_udm.additional.fields`  
`logMessage.urlWebCategories` | `event.idm.read_only_udm.additional.fields`  
`logMessage.urlWebReputation` | `event.idm.read_only_udm.additional.fields`  
`logMessage.countryCode` | `event.idm.read_only_udm.additional.fields`  
`logMessage.origin` | `event.idm.read_only_udm.additional.fields`  
`logMessage.tabId` | `event.idm.read_only_udm.additional.fields`  
`,` | `event.idm.read_only_udm.additional.fields`  
`and` | `event.idm.read_only_udm.additional.fields`  
`logMessage.details.navigation_details.is_fail_open_close_active` | `event.idm.read_only_udm.security_result.detection_fields`  
`logMessage.details.navigation_details.is_iframe` | `event.idm.read_only_udm.security_result.detection_fields`  
`logMessage.details.policy_version_details.application_access_policy_version` | `event.idm.read_only_udm.security_result.detection_fields`  
`logMessage.details.policy_version_details.browser_access_policy_version` | `event.idm.read_only_udm.security_result.detection_fields`  
`logMessage.details.policy_version_details.browser_policy_version` | `event.idm.read_only_udm.security_result.detection_fields`  
`logMessage.details.policy_version_details.dlp_policy_version` | `event.idm.read_only_udm.security_result.detection_fields`  
`logMessage.details.policy_version_details.pam_policy_version` | `event.idm.read_only_udm.security_result.detection_fields`  
`logMessage.isIslandPrivateAccess` | `event.idm.read_only_udm.security_result.detection_fields`  
`logMessage.compatibilityMode` | `event.idm.read_only_udm.security_result.detection_fields`  
`logMessage.matchedDevicePosture.client_certificates.issuer` | `event.idm.read_only_udm.security_result.detection_fields`  
`logMessage.matchedDevicePosture.client_certificates.subject` | `event.idm.read_only_udm.security_result.detection_fields`  
`logMessage.matchedDevicePosture.client_certificates.thumbprint` | `event.idm.read_only_udm.security_result.detection_fields`  
`logMessage.machineName` | `event.idm.read_only_udm.security_result.detection_fields`  
`logMessage.deviceId` | `event.idm.read_only_udm.security_result.detection_fields`  
`logMessage.ruleName` | `event.idm.read_only_udm.security_result.rule_name`  
`logMessage.ruleId` | `event.idm.read_only_udm.security_result.rule_id`  
`machineName` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`  
`region` | `event.idm.read_only_udm.principal.location.state`  
`osUserName` | `event.idm.read_only_udm.principal.administrative_domain`  
`machineId` | `event.idm.read_only_udm.principal.asset.asset_id`  
`saasApplicationId` | `event.idm.read_only_udm.target.resource.product_object_id`  
`matchedDevicePosture.architecture` | `event.idm.read_only_udm.principal.asset.hardware.cpu_platform`  
`matchedDevicePosture.browser_name` | `event.idm.read_only_udm.principal.application`  
`matchedDevicePosture.os_code_name` | `event.idm.read_only_udm.principal.platform_version`  
`matchedDevicePosture.os_version` | `event.idm.read_only_udm.principal.platform_patch_level`  
`matchedDevicePosture.device_type` | `event.idm.read_only_udm.principal.resource.attribute.labels`  
`matchedDevicePosture.disk_encryption` | `event.idm.read_only_udm.principal.resource.attribute.labels`  
`matchedDevicePosture.domain` | `event.idm.read_only_udm.principal.resource.attribute.labels`  
`matchedDevicePosture.is_default_browser` | `event.idm.read_only_udm.principal.resource.attribute.labels`  
`matchedDevicePosture.island_platform` | `event.idm.read_only_udm.principal.resource.attribute.labels`  
`matchedDevicePosture.machine_name` | `event.idm.read_only_udm.additional.fields`  
`matchedDevicePosture.os_firewall_enabled` | `event.idm.read_only_udm.additional.fields`  
`matchedDevicePosture.os_screen_lock_enabled` | `event.idm.read_only_udm.additional.fields`  
`matchedDevicePosture.secure_boot` | `event.idm.read_only_udm.additional.fields`  
`countryCode,details.ipa_details.ipa_forwarding_method` | `event.idm.read_only_udm.additional.fields`  
`details.ipa_details.ipa_rule` | `event.idm.read_only_udm.additional.fields`  
`details.navigation_details.is_fail_open_close_active` | `event.idm.read_only_udm.additional.fields`  
`details.navigation_details.is_iframe` | `event.idm.read_only_udm.additional.fields`  
`details.policy_version_details.application_access_policy_version` | `event.idm.read_only_udm.additional.fields`  
`details.policy_version_details.browser_access_policy_version` | `event.idm.read_only_udm.additional.fields`  
`details.policy_version_details.browser_policy_version` | `event.idm.read_only_udm.additional.fields`  
`details.policy_version_details.dlp_policy_version` | `event.idm.read_only_udm.additional.fields`  
`details.policy_version_details.pam_policy_version,windowId,compatibilityMode` | `event.idm.read_only_udm.additional.fields`  
`createdDate` | `event.idm.read_only_udm.additional.fields`  
`syslogConnectorId` | `event.idm.read_only_udm.additional.fields`  
`product.enabled` | `event.idm.read_only_udm.security_result.detection_fields`  
`product.name` | `event.idm.read_only_udm.security_result.detection_fields`  
`product.signatures_are_up_to_date` | `event.idm.read_only_udm.security_result.detection_fields`  
`art` | `event.idm.read_only_udm.additional.fields`  
`application_access_policy_version` | `event.idm.read_only_udm.additional.fields`  
`sourceDnsDomain` | `event.idm.read_only_udm.additional.fields`  
`av` | `event.idm.read_only_udm.additional.fields`  
`geid` | `event.idm.read_only_udm.additional.fields`  
`policy_version_details.application_access_policy_version` | `event.idm.read_only_udm.additional.fields`  
`policy_version_details.browser_access_policy_version` | `event.idm.read_only_udm.additional.fields`  
`policy_version_details.browser_policy_version` | `event.idm.read_only_udm.additional.fields`  
`policy_version_details.dlp_policy_version` | `event.idm.read_only_udm.additional.fields`  
`policy_version_details.pam_policy_version` | `event.idm.read_only_udm.additional.fields`  
`parent_frame_url` | `event.idm.read_only_udm.additional.fields`  
`aid` | `event.idm.read_only_udm.network.session_id`  
`agentZoneURI` | `event.idm.read_only_udm.network.http.referral_url`  
`at` | `event.idm.read_only_udm.principal.application`  
`ahost` | `event.idm.read_only_udm.principal.hostname`  
`ahost` | `event.idm.read_only_udm.principal.asset.hostname`  
`agt` | `event.idm.read_only_udm.principal.ip`  
`agt` | `event.idm.read_only_udm.principal.asset.ip`  
`amac` | `event.idm.read_only_udm.principal.mac`  
`deviceZoneURI` | `event.idm.read_only_udm.principal.resource.attribute.labels`  
`catdt` | `event.idm.read_only_udm.security_result.category_details`  
`deviceSeverity` | `event.idm.read_only_udm.security_result.severity_details`  
`atz` | `event.idm.read_only_udm.target.location.country_or_region`  
`user_name` | `event.idm.read_only_udm.principal.user.user_display_name`  
`device_id` | `event.idm.read_only_udm.principal.asset.attribute.labels`  
`machine_name` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`  
`os_platform` | `event.idm.read_only_udm.principal.asset.platform_software.platform`  
`country` | `event.idm.read_only_udm.principal.location.country_or_region`  
`os_user_name` | `event.idm.read_only_udm.principal.user.attribute.labels`  
`top_level_url` | `event.idm.read_only_udm.target.url`  
`rule_id` | `event.idm.read_only_udm.security_result.rule_id`  
`rule_name` | `event.idm.read_only_udm.security_result.rule_name`  
`client_event_id` | `event.idm.read_only_udm.network.session_id`  
`country_code` | `event.idm.read_only_udm.additional.fields`  
`tenant_id` | `event.idm.read_only_udm.additional.fields`  
`tab_id` | `event.idm.read_only_udm.security_result.detection_fields`  
`signature` | `event.idm.read_only_udm.security_result.detection_fields`  
`source` | `event.idm.read_only_udm.additional.fields`  
`public_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`  
`source_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`  
`processed_date` | `event.idm.read_only_udm.additional.fields`  
`matched_user_group` | `event.idm.read_only_udm.principal.group.group_display_name`  
`frame_url` | `event.idm.read_only_udm.additional.fields`  
`url_web_categories` | `event.idm.read_only_udm.additional.fields`  
`client_sending_date` | `event.idm.read_only_udm.additional.fields`  
`matched_device_posture.anti_malware_product.name` | `event.idm.read_only_udm.additional.fields`  
`matched_device_posture.anti_malware_product.enabled` | `event.idm.read_only_udm.additional.fields`  
`matched_device_posture.anti_malware_product.signatures_are_up_to_date` | `event.idm.read_only_udm.additional.fields`  
`matched_device_posture.anti_malware_product.signatures_last_updated` | `event.idm.read_only_udm.additional.fields`  
`matched_device_posture.client_certificates.issuer` | `event.idm.read_only_udm.additional.fields`  
`matched_device_posture.client_certificates.subject` | `event.idm.read_only_udm.additional.fields`  
`matched_device_posture.client_certificates.thumbprint` | `event.idm.read_only_udm.security_result.detection_fields`  
`matched_device_posture.domain` | `event.idm.read_only_udm.principal.domain.name`  
`matched_device_posture.os_code_name` | `event.idm.read_only_udm.principal.asset.platform_software.platform_version`  
`matched_device_posture.machine_name` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`  
`matched_device_posture.disk_encryption` | `event.idm.read_only_udm.additional.fields`  
`matched_device_posture.is_virtual_machine` | `event.idm.read_only_udm.additional.fields`  
`matched_device_posture.processes` | `event.idm.read_only_udm.principal.file.full_path`  
`origin` | `event.idm.read_only_udm.additional.fields`  
`url_web_reputation` | `event.idm.read_only_udm.security_result.confidence_score`  
`is_island_private_access` | `event.idm.read_only_udm.additional.fields`  
`window_id` | `event.idm.read_only_udm.principal.resource.id`  
`compatibility_mode` | `event.idm.read_only_udm.additional.fields`  
`version` | `event.idm.read_only_udm.metadata.product_version`  
`userId` | `principal.user.userid`  
`topLevelUrl` | `network.http.referral_url`  
`ruleId` | `security_result.rule_id`  
`ruleName` | `security_result.rule_name`  
`Verdict" and "verdict` | `security_result.action_details`  
`sourceIp" and "publicIp` | `principal.ip`  
`verdictReason` | `security_result.description`  
`tabId", "urlWebReputation", "updatedDate", "processedDate", "service", "id", "deviceId", "frameUrl", "urlWebCategories", "isIslandPrivateAccess", "tenantId", "saasApplicationCategory", "saasApplicationName", "machineName", "details.navigationDetails.isIframe", "details.navigationDetails.is_iframe", "navigation_details.is_iframe", "matchedDevicePosture.domain", "matchedDevicePosture.workgroup", and "incognito` | `additional.fields`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/island-browser-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
