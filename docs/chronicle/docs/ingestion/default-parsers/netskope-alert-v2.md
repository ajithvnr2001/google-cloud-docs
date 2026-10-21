---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-alert-v2/
title: Collect Netskope alert logs v2 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:43:49.401246+00:00
---

# Collect Netskope alert logs v2  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-alert-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Netskope alert logs v2

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This parser extracts Netskope alert logs from JSON-formatted messages, transforming them into the Google Security Operations UDM. It normalizes fields, parses timestamps, handles alerts and severities, extracts network information (IPs, ports, protocols), enriches user and file data, and maps fields to the UDM structure. The parser also handles specific Netskope activities like logins and DLP events and adds custom labels for enhanced context. 

**Note:** For more information, see [Netskope API Reference](https://docs.netskope.com/en/rest-api-v2-overview-312207/).

## Before you begin

Ensure that you have the following prerequisites:

  * Google SecOps instance.
  * Privileged access to Netskope.



## Create a Service Account and Generate a REST API Token in Netskope

To integrate with Google SecOps, you need to create a dedicated service account in Netskope and generate an API token.

  1. Sign in to the Netskope tenant using your administrator credentials.
  2. Navigate to **Settings** > **Administration & Roles**.
  3. Click the **Administrators** tab, and then select the **Service Accounts** button.
  4. In the "New Service Account" dialog, enter a descriptive **Service Account Name** (e.g., "Google SecOps Ingestion").
  5. Under **Role** , select the appropriate role that has permissions to access the required API endpoints (e.g., a custom role with read access to alerts).

     * Role permissions and API endpoint transparency: 
       * When selecting a role (or creating a custom one), Netskope provides transparency regarding the associated API endpoints: 
         * Create custom roles: As you define the permissions for your custom role, the system instantly displays the API endpoint data associated with each permission category. 
         * Check predefined roles: You can review predefined roles and click any role to see a detailed breakdown of its permissions. This includes the associated API endpoints and categories.
  6. Under **REST API Authentication Methods** , select **API Key**.

  7. Check the box for **Generate token now with expiry** and set the selected expiration period (e.g., 365 Days).

  8. Click the **Create** button.

> **Warning:** A dialog will appear displaying the new REST API token. You **must** copy and securely store this token immediately. It will not be shown again.

  9. Keep this token safe; you will need it to configure the feed in Google SecOps.


**Note:** For more information, see [Netskope SCIM User Provisioning with RBAC v3](https://docs.netskope.com/en/scim-user-provisioning-with-rbacv3).

## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed; for example, **Netskope Alert Logs v2**.
  5. Select **Third party API** as the **Source type**.
  6. Select **Netskope V2** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Authentication HTTP Header:** token previously generated in a `Netskope-Api-Token:<value>` format (for example, **Netskope-Api-Token:AAAABBBBCCCC111122223333**).
     * **API Hostname:** The FQDN (fully qualified domain name) of your Netskope REST API endpoint (for example `myinstance.goskope.com`).
     * **API Endpoint:** Enter **alerts**.
     * **Content Type:** Allowed values for **alerts** are **uba** , **securityassessment** , **quarantine** , **remediation** , **policy** , **malware** , **malsite** , **compromisedcredential** , **ctep** , **dlp** , **watchlist**.
  9. Click **Next**.
  10. Review the feed configuration in the **Finalize** screen, and then click **Submit**.



## Optional: Add a feed configuration to ingest Netskope Event logs v2

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add new feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, **Netskope Event Logs v2**).
  5. Select **Third party API** as the **Source type**.
  6. Select **Netskope V2** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Authentication HTTP Header:** Enter the REST API token in the format `Netskope-Api-Token: <your-generated-token>`, where `<your-generated-token>` is the API token you copied from the Netskope platform in the previous section. This header is used to authenticate against the Netskope API.
     * **API Hostname:** The FQDN (fully qualified domain name) of your Netskope REST API endpoint (for example `myinstance.goskope.com`).
     * **API Endpoint:** Enter **events**.
     * **Content Type:** Allowed values for **events** are **application** , **audit** , **connection** , **incident** , **infrastructure** , **network** , **page**.
     * **Asset namespace** : the [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : the label applied to the events from this feed.
  9. Click **Next**.
  10. Review the feed configuration in the **Finalize** screen, and then click **Submit**.



## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`_id` | `metadata.product_log_id` | Directly mapped from `_id`.  
`access_method` | `extensions.auth.auth_details` | Directly mapped from `access_method`.  
`action` | `security_result.action` | Mapped to `QUARANTINE` because the value is "alert". Also mapped to `security_result.action_details` as "alert".  
`app` | `target.application` | Directly mapped from `app`.  
`appcategory` | `security_result.category_details` | Directly mapped from `appcategory`.  
`browser` | `network.http.user_agent` | Directly mapped from `browser`.  
`browser_session_id` | `network.session_id` | Directly mapped from `browser_session_id`.  
`browser_version` | `network.http.parsed_user_agent.browser_version` | Directly mapped from `browser_version`.  
`ccl` | `security_result.confidence_details` | Directly mapped from `ccl`.  
`device` | `principal.resource.type`, `principal.resource.resource_subtype` | `principal.resource.type` is set to "DEVICE". `principal.resource.resource_subtype` is directly mapped from `device`.  
`dst_country` | `target.location.country_or_region` | Directly mapped from `dst_country`.  
`dst_latitude` | `target.location.region_coordinates.latitude` | Directly mapped from `dst_latitude`.  
`dst_longitude` | `target.location.region_coordinates.longitude` | Directly mapped from `dst_longitude`.  
`dst_region` | `target.location.name` | Directly mapped from `dst_region`.  
`dstip` | `target.ip`, `target.asset.ip` | Directly mapped from `dstip`.  
`metadata.event_type` | `metadata.event_type` | Set to `NETWORK_CONNECTION` because both principal and target IP addresses are present and the protocol is not HTTP.  
`metadata.product_event_type` | `metadata.product_event_type` | Directly mapped from `type`.  
`metadata.product_name` | `metadata.product_name` | Set to "NETSKOPE_ALERT_V2" by the parser.  
`metadata.vendor_name` | `metadata.vendor_name` | Set to "NETSKOPE_ALERT_V2" by the parser.  
`object_type` | `additional.fields` | Added as a key-value pair to `additional.fields` where key is "object_type" and value is the content of `object_type`.  
`organization_unit` | `principal.administrative_domain` | Directly mapped from `organization_unit`.  
`os` | `principal.platform` | Mapped to `WINDOWS` because the value matches the regex "(?i)Windows.*".  
`policy` | `security_result.summary` | Directly mapped from `policy`.  
`site` | `additional.fields` | Added as a key-value pair to `additional.fields` where key is "site" and value is the content of `site`.  
`src_country` | `principal.location.country_or_region` | Directly mapped from `src_country`.  
`src_latitude` | `principal.location.region_coordinates.latitude` | Directly mapped from `src_latitude`.  
`src_longitude` | `principal.location.region_coordinates.longitude` | Directly mapped from `src_longitude`.  
`src_region` | `principal.location.name` | Directly mapped from `src_region`.  
`srcip` | `principal.ip`, `principal.asset.ip` | Directly mapped from `srcip`.  
`timestamp` | `metadata.event_timestamp.seconds` | Directly mapped from `timestamp`.  
`type` | `metadata.product_event_type` | Directly mapped from `type`.  
`ur_normalized` | `principal.user.email_addresses` | Directly mapped from `ur_normalized`.  
`url` | `target.url` | Directly mapped from `url`.  
`user` | `principal.user.email_addresses` | Directly mapped from `user`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netskope-alert-v2-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
