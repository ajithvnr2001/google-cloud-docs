---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/salesforce/
title: Collect Salesforce logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:49.821215+00:00
---

# Collect Salesforce logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/salesforce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Salesforce logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect Salesforce logs by setting up a Google Security Operations feed using the Third Party API.

Salesforce is a cloud-based customer relationship management (CRM) platform that provides tools for sales, service, marketing, and analytics. Salesforce logs capture user activity, security events, system changes, and API usage across the platform.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * Salesforce Enterprise Edition or higher (API access enabled)
  * Salesforce Shield Event Monitoring license enabled (required for `EventLogFile` access)
  * Salesforce System Administrator permissions
  * OpenSSL installed (for certificate generation)

**Note:** Salesforce requires External Client Apps (introduced in Spring '26 release) for OAuth JWT Bearer Flow authentication. Connected Apps are deprecated for new integrations.**Note:** This integration ingests logs from the Salesforce **EventLogFile** API only. The Real-Time Event Monitoring (streaming) API and arbitrary data extraction through custom SOQL queries are not supported.

## Generate RSA key pair and certificate

Generate an RSA private key and self-signed X.509 certificate for JWT signing.

### Generate private key

  * Generate the key in **PKCS#8** format. The Google SecOps feed only accepts PKCS#8 keys (header `-----BEGIN PRIVATE KEY-----`); legacy PKCS#1 keys (`-----BEGIN RSA PRIVATE KEY-----`) cause parsing errors at feed creation.
        
        openssl genpkey -algorithm RSA -out salesforce_private.key -pkeyopt rsa_keygen_bits:2048
        


**Note:** If you already have an RSA key in PKCS#1 format, convert it with `openssl pkcs8 -topk8 -nocrypt -in old_rsa.key -out salesforce_private.key`. The header and footer must read `-----BEGIN PRIVATE KEY-----` / `-----END PRIVATE KEY-----` (without the word `RSA`).

### Generate self-signed certificate

  * Use your private key to generate a self-signed X.509 certificate valid for 365 days.
        
        openssl req -new -x509 -key salesforce_private.key -out salesforce_certificate.crt -days 365
        




When prompted, enter certificate details:

  * **Country Name** : Enter your 2-letter country code (for example, `US`).
  * **State or Province Name** : Enter your state (for example, `California`).
  * **Locality Name** : Enter your city (for example, `San Francisco`).
  * **Organization Name** : Enter your organization name (for example, `Acme Corp`).
  * **Organizational Unit Name** : Enter department (for example, `IT Security`).
  * **Common Name** : Enter a descriptive name (for example, `SecOps Integration`).
  * **Email Address** : Enter contact email.

**Note:** Save `salesforce_private.key` (private key) and `salesforce_certificate.crt` (certificate) in a secure location. The private key will be used in Google SecOps feed configuration. The certificate will be uploaded to the Salesforce External Client App.

## Create Salesforce External Client App

External Client Apps are the recommended method for OAuth authentication in Salesforce (Spring '26 and later).

  1. Sign in to **Salesforce**.
  2. Go to **Setup** (gear icon in top right).
  3. In the **Quick Find** box, enter `External Client Apps`.
  4. Click **External Client App Manager**.
  5. Click **New External Client App**.



### Configure basic information

  1. Provide the following configuration details: 
     * **External Client App Name** : Enter a descriptive name (for example, `Google SecOps Integration`).
     * **API Name** : Auto-populated based on app name. Leave as default or customize.
     * **Contact Email** : Enter your email address.
     * **Distribution State** : Select **Local**.
  2. Click **Continue**.



### Enable OAuth settings

  1. Select the **Enable OAuth** checkbox.
  2. Provide the following configuration details: 
     * **Callback URL** : Enter `https://login.salesforce.com/services/oauth2/callback`.

**Note:** The callback URL is required but not used for JWT Bearer Flow. This is a placeholder value.

  1. In the **OAuth Scopes** section, move the following scopes from **Available OAuth Scopes** to **Selected OAuth Scopes** : 
     * **Manage user data via APIs (api)**
     * **Perform requests at any time (refresh_token, offline_access) (refresh_token, offline_access)**



### Enable JWT Bearer Flow and upload certificate

  1. In the **Flow Enablement** section, select the **Enable JWT Bearer Flow** checkbox.
  2. The **Certificate Upload** section appears.
  3. Click **Upload Files** or drag and drop your certificate file.
  4. Select the `salesforce_certificate.crt` file.
  5. Wait for the upload to complete. The certificate filename should appear below the upload button.

**Note:** You must upload a valid X.509 certificate in `.crt`, `.cer`, or `.pem` format. The certificate's public key will be used by Salesforce to verify JWT signatures.

### Configure OAuth policies

  1. In the **OAuth Policies** section: 
     * **Permitted Users** : Select **Admin approved users are pre-authorized**.
  2. Click **Save**.

**Note:** The app may take 2-10 minutes to activate after creation.

## Get consumer key

After creating the External Client App, retrieve the Consumer Key for Google SecOps feed configuration.

  1. In the **External Client App Manager** , click on your app name (for example, `Google SecOps Integration`).
  2. Go to the **Settings** tab.
  3. In the **OAuth Settings** section, click **Consumer Key and Secret**.
  4. Copy and save the **Consumer Key** value.

**Note:** The Consumer Key is required for Google SecOps feed configuration. Do not share this value publicly.

  * Example Consumer Key format:
        
        3MVG9IKcPoNiNVBIPjdw4z.pcfRjTFBp7xC8x9k4U8jZ0HlLQdPqX5bKjR8yNzQ9_YvY.8xD3F2W6nXb5YgNx
        




## Pre-authorize the External Client App

Salesforce requires pre-authorization for JWT Bearer Flow. Pre-authorize by assigning the External Client App to a user via permission set.

### Create permission set

  1. Go to **Setup > Users > Permission Sets**.
  2. Click **New**.
  3. Provide the following configuration details: 
     * **Label** : Enter `SecOps Integration Users` (for example).
     * **API Name** : Auto-populated based on label.
  4. Click **Save**.



### Assign permission set to External Client App

  1. Go to **Setup > External Client App Manager**.
  2. Click on your External Client App (for example, `Google SecOps Integration`).
  3. Click the **Policies** tab.
  4. In the **App Policies** section, under **Select Permission Sets** : 
     1. Move your permission set (for example, `SecOps Integration Users`) from **Available Permission Sets** to **Selected Permission Sets**.
  5. Click **Save**.



### Assign permission set to user

  1. From the permission set detail page, click **Manage Assignments**.
  2. Click **Add Assignments**.
  3. Select the checkbox next to the user account that will be used for Google SecOps integration (for example, `integration@acme.com`).
  4. Click **Assign**.
  5. Click **Done**.

**Note:** This user's username will be used as the JWT Claims Subject in Google SecOps feed configuration.

## Configure a feed in Google SecOps to ingest Salesforce logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Salesforce EventLogFile`).
  5. Select **Third Party API** as the **Source type**.
  6. Select **SALESFORCE** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **API Hostname** : Enter your Salesforce instance hostname (for example, `acme.my.salesforce.com`).
**Note:** Do not include `https://` in the hostname. For production orgs, use `yourcompany.my.salesforce.com`. For sandboxes, use `yourcompany--sandboxname.sandbox.my.salesforce.com`. For My Domain instances, use your custom domain (for example, `acme.my.salesforce.com`).
     * **OAuth JWT Endpoint** : Enter the OAuth token endpoint URL. The `grant_type` query parameter is **required** by the Google SecOps feed fetcher and must be appended to the URL exactly as shown: 
       * Production orgs: `https://login.salesforce.com/services/oauth2/token?grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer`
       * Sandbox orgs: `https://test.salesforce.com/services/oauth2/token?grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer`
       * My Domain: `https://acme.my.salesforce.com/services/oauth2/token?grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer`
     * **JWT Claims Issuer** : Enter the Consumer Key from the External Client App.
     * **JWT Claims Subject** : Enter the Salesforce username of the pre-authorized user (for example, `integration@acme.com`).
     * **JWT Claims Audience** : Enter the authorization server URL. Use only one of the two values below; do not substitute a My Domain URL, because Salesforce rejects it during JWT signature validation: 
       * Production orgs and My Domain orgs: `https://login.salesforce.com`
       * Sandbox orgs: `https://test.salesforce.com`
     * **RSA Private Key** : Paste the complete PKCS#8 private key contents including the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` markers. The header and footer must **not** contain the word `RSA`. A key with `-----BEGIN RSA PRIVATE KEY-----` (PKCS#1) is rejected by the feed parser.

     * To get the private key contents:
           
           cat salesforce_private.key
           

Copy the entire output including the header and footer lines.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Salesforce instance types reference

The OAuth JWT endpoint and audience values depend on your Salesforce instance type:

Instance Type | OAuth JWT Endpoint | JWT Claims Audience | API Hostname Format  
---|---|---|---  
**Production** | `https://login.salesforce.com/services/oauth2/token?grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer` | `https://login.salesforce.com` | `company.my.salesforce.com`  
**Sandbox** | `https://test.salesforce.com/services/oauth2/token?grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer` | `https://test.salesforce.com` | `company--sandbox.sandbox.my.salesforce.com`  
**My Domain** | `https://domain.my.salesforce.com/services/oauth2/token?grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer` | `https://login.salesforce.com` | `domain.my.salesforce.com`  
**Note:** My Domain is recommended for production deployments. My Domain provides a custom, branded login URL and is required for certain Salesforce features.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`ApiType_label` | `additional.fields` | Merged  
`ApiVersion_label` | `additional.fields` | Merged  
`Application_label` | `additional.fields` | Merged  
`AuthMethodReference_label` | `additional.fields` | Merged  
`Browser_label` | `additional.fields` | Merged  
`ConnectedAppId_label` | `additional.fields` | Merged  
`CountryIso_label` | `additional.fields` | Merged  
`CreatedByContext_label` | `additional.fields` | Merged  
`CreatedById_label` | `additional.fields` | Merged  
`CreatedByIssuer_label` | `additional.fields` | Merged  
`CreatedBy_FederationIdentifier_label` | `additional.fields` | Merged  
`CreatedDate_label` | `additional.fields` | Merged  
`DeviceSessionId_label` | `additional.fields` | Merged  
`EffectivePageTimeDeviationReason_label` | `additional.fields` | Merged  
`EffectivePageTime_label` | `additional.fields` | Merged  
`Entityid_label` | `additional.fields` | Merged  
`EventIdentifier_label` | `additional.fields` | Merged  
`EventUuid_label` | `additional.fields` | Merged  
`FederationIdentifier_label` | `additional.fields` | Merged  
`HasEffectivePageTimeDeviation_label` | `additional.fields` | Merged  
`Id_label` | `additional.fields` | Merged  
`LoginGeoId_label` | `additional.fields` | Merged  
`LoginHistoryId_label` | `additional.fields` | Merged  
`LoginKey_label` | `additional.fields` | Merged  
`LoginSubType_label` | `additional.fields` | Merged  
`LoginType_label` | `additional.fields` | Merged  
`NetId_label` | `additional.fields` | Merged  
`NetworkId_label` | `additional.fields` | Merged  
`Operation_label` | `additional.fields` | Merged  
`OptionsIsGet_label` | `additional.fields` | Merged  
`OptionsIsPost_label` | `additional.fields` | Merged  
`Platform_label` | `additional.fields` | Merged  
`PolicyId_label` | `additional.fields` | Merged  
`PreviousPageAppName_label` | `additional.fields` | Merged  
`PreviousPageEntityType_label` | `additional.fields` | Merged  
`QueriedEntities_label` | `additional.fields` | Merged  
`RelatedEventIdentifier_label` | `additional.fields` | Merged  
`RequestIdentifier_label` | `additional.fields` | Merged  
`RowsProcessed_label` | `additional.fields` | Merged  
`RowsReturned_label` | `additional.fields` | Merged  
`SdkVersion_label` | `additional.fields` | Merged  
`SessionKey_label` | `additional.fields` | Merged  
`SessionLevel_label` | `additional.fields` | Merged  
`Subdivision_label` | `additional.fields` | Merged  
`api_token_label` | `additional.fields` | Merged  
`api_type_label` | `additional.fields` | Merged  
`auth_service_id_label` | `additional.fields` | Merged  
`auth_token` | `additional.fields` | Merged  
`browser_version_label` | `additional.fields` | Merged  
`channel_label` | `additional.fields` | Merged  
`connection_type_label` | `additional.fields` | Merged  
`customerName_label` | `additional.fields` | Merged  
`datacell_label` | `additional.fields` | Merged  
`decoded_body_size_label` | `additional.fields` | Merged  
`delegate_user_label` | `additional.fields` | Merged  
`device_label` | `additional.fields` | Merged  
`device_platform` | `additional.fields` | Mapped: `:` → `device_label`  
`done_label` | `additional.fields` | Merged  
`encoded_body_size_label` | `additional.fields` | Merged  
`evaluation_time_label` | `additional.fields` | Merged  
`event_id` | `additional.fields` | Mapped: `"LightningInteraction", "LightningPerformance", "LightningPageView", "LightningUriE...  
`initiator_type_label` | `additional.fields` | Merged  
`login_key_label` | `additional.fields` | Merged  
`loginkey_label` | `additional.fields` | Merged  
`map_field` | `additional.fields` | Merged  
`next_hop_protocol_label` | `additional.fields` | Merged  
`page_app_name_label` | `additional.fields` | Merged  
`page_context_label` | `additional.fields` | Merged  
`page_entity_id_label` | `additional.fields` | Merged  
`page_entity_type_label` | `additional.fields` | Merged  
`page_url_label` | `additional.fields` | Merged  
`parent_ui_element_label` | `additional.fields` | Merged  
`platform_label` | `additional.fields` | Merged  
`postal_code_label` | `additional.fields` | Merged  
`redirect_start_label` | `additional.fields` | Merged  
`render_blocking_status_label` | `additional.fields` | Merged  
`replayId_label` | `additional.fields` | Merged  
`request_start_label` | `additional.fields` | Merged  
`response_end_label` | `additional.fields` | Merged  
`response_start_label` | `additional.fields` | Merged  
`responsible_namespace_prefix_label` | `additional.fields` | Merged  
`schemaId_label` | `additional.fields` | Merged  
`schema_label` | `additional.fields` | Merged  
`section_label` | `additional.fields` | Merged  
`server_request_id_label` | `additional.fields` | Merged  
`target_ui_element_label` | `additional.fields` | Merged  
`totalSize_label` | `additional.fields` | Merged  
`transfer_size_label` | `additional.fields` | Merged  
`ts_label` | `additional.fields` | Merged  
`ui_event_id_label` | `additional.fields` | Merged  
`ui_event_sequence_num_label` | `additional.fields` | Merged  
`ui_event_source_label` | `additional.fields` | Merged  
`ui_event_timestamp_label` | `additional.fields` | Merged  
`ui_event_type_label` | `additional.fields` | Merged  
`ui_root_activity_id_label` | `additional.fields` | Merged  
`ui_thread_response_delay_label` | `additional.fields` | Merged  
`worker_start_label` | `additional.fields` | Merged  
`Login_type` | `extensions.auth.auth_details` | Directly mapped  
`auth.mechanism` | `extensions.auth.mechanism` | Merged  
`csv_format` | `extensions.auth.mechanism` | Mapped: `false` → `auth.mechanism`  
`event_id` | `extensions.auth.mechanism` | Mapped: `Login: Success` → `auth.mechanism`  
`mechanism` | `extensions.auth.mechanism` | Merged  
`LoginType` | `extensions.auth.type` | Mapped: `Application` → `AUTHTYPE_UNSPECIFIED`  
`csv_format` | `extensions.auth.type` | Mapped: `false` → `AUTHTYPE_UNSPECIFIED`  
`event_id` | `extensions.auth.type` | Mapped values (8 total, e.g. `"IdentityProviderEventStore", "LoginEventStream", "WaveDownloa...  
`logintype` | `extensions.auth.type` | Mapped: `SAML Sfdc Initiated SSO` → `SSO`  
`intermediary_ip` | `intermediary.ip` | Merged  
`user_name` | `intermediary.user.user_display_name` | Directly mapped  
`userid` | `intermediary.user.userid` | Directly mapped  
`Report_description` | `metadata.description` | Directly mapped  
`data.properties.Description.str` | `metadata.description` | Directly mapped  
`metadata_description` | `metadata.description` | Directly mapped  
`properties.Description` | `metadata.description` | Directly mapped  
`@timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`LoginTime` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSS+0000`  
`TIMESTAMP` | `metadata.event_timestamp` | Parsed as `UNIX`  
`TIMESTAMP_DERIVED` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`User.LastLoginDate` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSS+0000`  
`collected_timestamp` | `metadata.event_timestamp` | Parsed as `yyyyMMddHHmmss`  
`column6` | `metadata.event_timestamp` | Parsed as `yyyyMMddHHmmss`  
`createdAt` | `metadata.event_timestamp` | Parsed as `UNIX`  
`detail.payload.EventDate` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`payload.EventDate` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`properties.EventDate` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`recordDate` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`startTime` | `metadata.event_timestamp` | Parsed as `MMM d yyyy, HH:mm:ss:SSS`  
`time_stamp` | `metadata.event_timestamp` | Parsed as `YYYY-MM-ddTHH:mm:ss`  
`timestamp` | `metadata.event_timestamp` | Parsed as `yyyyMMddHHmmss`  
`ts_date` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss.SSSZ`  
`event_type` | `metadata.event_type` | Mapped: `"", "GENERIC_EVENT"` → `USER_UNCATEGORIZED`, `"", "GENERIC_EVENT"` → `NETWORK_CONNE...  
`principal_machine_id_present` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`principal_user_present` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`label` | `metadata.ingestion_labels` | Merged  
`resource_name` | `metadata.ingestion_labels` | Mapped: `"ReportEvent","SessionHijackingEventStore","BulkApiResultEventStore","CredentialStu...  
`action` | `metadata.product_event_type` | Directly mapped  
`attrs.cat` | `metadata.product_event_type` | Directly mapped  
`event_id` | `metadata.product_event_type` | Directly mapped  
`name` | `metadata.product_event_type` | Directly mapped  
`REQUEST_ID` | `metadata.product_log_id` | Directly mapped  
`column9` | `metadata.product_log_id` | Directly mapped  
`data.properties.EventIdentifier.str` | `metadata.product_log_id` | Directly mapped  
`event_identifier` | `metadata.product_log_id` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`payload.EventIdentifier` | `metadata.product_log_id` | Directly mapped  
`product_log_id` | `metadata.product_log_id` | Directly mapped  
`properties.EventIdentifier` | `metadata.product_log_id` | Directly mapped  
`ClientVersion` | `metadata.product_version` | Directly mapped  
`payload.ClientVersion` | `metadata.product_version` | Directly mapped  
`data.properties.LoginUrl.str` | `metadata.url_back_to_product` | Directly mapped  
`data.properties.PageUrl.str` | `metadata.url_back_to_product` | Directly mapped  
`payload.PreviousPageUrl` | `metadata.url_back_to_product` | Directly mapped  
`protocol` | `network.application_protocol` | Directly mapped  
`METHOD` | `network.http.method` | Directly mapped  
`data.properties.HttpMethod.str` | `network.http.method` | Directly mapped  
`method` | `network.http.method` | Directly mapped  
`payload.HttpMethod` | `network.http.method` | Directly mapped  
`properties.HttpMethod` | `network.http.method` | Directly mapped  
`properties.UserAgent` | `network.http.parsed_user_agent` | Directly mapped  
`user_agent` | `network.http.parsed_user_agent` | Directly mapped  
`referral_url` | `network.http.referral_url` | Directly mapped  
`STATUS_CODE` | `network.http.response_code` | Directly mapped  
`request_status` | `network.http.response_code` | Directly mapped  
`Browser_type` | `network.http.user_agent` | Directly mapped  
`Client_info` | `network.http.user_agent` | Directly mapped  
`data.properties.UserAgent.str` | `network.http.user_agent` | Directly mapped  
`detail.payload.UserAgent` | `network.http.user_agent` | Directly mapped  
`payload.UserAgent` | `network.http.user_agent` | Directly mapped  
`properties.UserAgent` | `network.http.user_agent` | Directly mapped  
`user_agent` | `network.http.user_agent` | Directly mapped  
`RESPONSE_SIZE` | `network.received_bytes` | Renamed/mapped  
`REQUEST_SIZE` | `network.sent_bytes` | Renamed/mapped  
`column17` | `network.sent_bytes` | Directly mapped  
`event_id` | `network.sent_bytes` | Mapped: `AuraRequest` → `uinteger`  
`LOGIN_KEY` | `network.session_id` | Directly mapped  
`SESSION_KEY` | `network.session_id` | Directly mapped  
`data.properties.SESSION_KEY.str` | `network.session_id` | Directly mapped  
`data.properties.SessionKey.str` | `network.session_id` | Directly mapped  
`payload.SessionKey` | `network.session_id` | Directly mapped  
`properties.SessionKey` | `network.session_id` | Directly mapped  
`session_id` | `network.session_id` | Directly mapped  
`session_key` | `network.session_id` | Directly mapped  
`cipher_suite` | `network.tls.cipher` | Directly mapped  
`data.properties.CipherSuite.str` | `network.tls.cipher` | Directly mapped  
`payload.CipherSuite` | `network.tls.cipher` | Directly mapped  
`properties.CipherSuite` | `network.tls.cipher` | Directly mapped  
`data.properties.TlsProtocol.str` | `network.tls.version` | Directly mapped  
`payload.TlsProtocol` | `network.tls.version` | Directly mapped  
`properties.TlsProtocol` | `network.tls.version` | Directly mapped  
`tls_protocol` | `network.tls.version_protocol` | Directly mapped  
`data.properties.DelegatedUsername.str` | `observer.user.userid` | Directly mapped  
`application` | `principal.application` | Directly mapped  
`attrs.Application` | `principal.application` | Renamed/mapped  
`data.properties.Application.str` | `principal.application` | Directly mapped  
`payload.Application` | `principal.application` | Directly mapped  
`properties.Application` | `principal.application` | Directly mapped  
`src_app_name` | `principal.application` | Directly mapped  
`SourceIp` | `principal.asset.hostname` | Directly mapped  
`client_host` | `principal.asset.hostname` | Directly mapped  
`client_ip_1` | `principal.asset.hostname` | Directly mapped  
`detail.payload.Client` | `principal.asset.hostname` | Directly mapped  
`CLIENT_IP` | `principal.asset.ip` | Merged  
`Client_ip` | `principal.asset.ip` | Merged  
`SourceIp` | `principal.asset.ip` | Merged  
`attrs.src` | `principal.asset.ip` | Merged  
`client_ip` | `principal.asset.ip` | Merged  
`client_ip_1` | `principal.asset.ip` | Merged  
`column28` | `principal.asset.ip` | Merged  
`csv_format` | `principal.asset.ip` | Mapped: `false` → `attrs.src`  
`event_id` | `principal.asset.ip` | Mapped: `API` → `prin_ip`, `Sites` → `column28`, `Login: Success` → `attrs.src`  
`ip` | `principal.asset.ip` | Merged  
`prin_ip` | `principal.asset.ip` | Merged  
`principal_ip_address` | `principal.asset.ip` | Merged  
`src_ip1` | `principal.asset.ip` | Merged  
`value` | `principal.asset.ip` | Merged  
`data.properties.ASSET_ID.str` | `principal.asset_id` | Directly mapped  
`SourceIp` | `principal.hostname` | Directly mapped  
`client_host` | `principal.hostname` | Directly mapped  
`client_ip_1` | `principal.hostname` | Directly mapped  
`detail.payload.Client` | `principal.hostname` | Directly mapped  
`CLIENT_IP` | `principal.ip` | Merged  
`Client_ip` | `principal.ip` | Merged  
`SourceIp` | `principal.ip` | Merged  
`attrs.src` | `principal.ip` | Merged  
`client_ip` | `principal.ip` | Merged  
`client_ip_1` | `principal.ip` | Merged  
`column28` | `principal.ip` | Merged  
`csv_format` | `principal.ip` | Mapped: `false` → `attrs.src`  
`event_id` | `principal.ip` | Mapped: `API` → `prin_ip`, `Sites` → `column28`, `Login: Success` → `attrs.src`  
`ip` | `principal.ip` | Merged  
`prin_ip` | `principal.ip` | Merged  
`principal_ip` | `principal.ip` | Merged  
`principal_ip_address` | `principal.ip` | Merged  
`src_ip1` | `principal.ip` | Merged  
`value` | `principal.ip` | Merged  
`ApiType_label` | `principal.labels` | Merged  
`Client_label` | `principal.labels` | Merged  
`ConApp_label` | `principal.labels` | Merged  
`OrderBy_label` | `principal.labels` | Merged  
`Org_id` | `principal.labels` | Merged  
`Qentry_label` | `principal.labels` | Merged  
`Query_label` | `principal.labels` | Merged  
`Records_label` | `principal.labels` | Merged  
`channel` | `principal.labels` | Merged  
`colhdr_label` | `principal.labels` | Merged  
`disp_field_hdr_label` | `principal.labels` | Merged  
`evt_src_label` | `principal.labels` | Merged  
`federation_identifier` | `principal.labels` | Merged  
`grouped_colhdr_label` | `principal.labels` | Merged  
`city` | `principal.location.city` | Directly mapped  
`data.properties.City.str` | `principal.location.city` | Directly mapped  
`geoip_src.city_name` | `principal.location.city` | Directly mapped  
`payload.City` | `principal.location.city` | Directly mapped  
`properties.City` | `principal.location.city` | Directly mapped  
`client_geo` | `principal.location.country_or_region` | Directly mapped  
`data.properties.Country.str` | `principal.location.country_or_region` | Directly mapped  
`geoip_src.country_name` | `principal.location.country_or_region` | Directly mapped  
`payload.CountryIso` | `principal.location.country_or_region` | Directly mapped  
`properties.Country` | `principal.location.country_or_region` | Directly mapped  
`region` | `principal.location.country_or_region` | Directly mapped  
`data.properties.LoginLatitude.number` | `principal.location.region_latitude` | Renamed/mapped  
`payload.LoginLatitude` | `principal.location.region_latitude` | Renamed/mapped  
`properties.LoginLatitude` | `principal.location.region_latitude` | Renamed/mapped  
`data.properties.LoginLongitude.number` | `principal.location.region_longitude` | Renamed/mapped  
`payload.LoginLongitude` | `principal.location.region_longitude` | Renamed/mapped  
`properties.LoginLongitude` | `principal.location.region_longitude` | Renamed/mapped  
`geoip_src.region_name` | `principal.location.state` | Directly mapped  
`namespace` | `principal.namespace` | Directly mapped  
`source_ip` | `principal.nat_ip` | Merged  
`Platform` | `principal.platform` | Mapped: `Windows` → `WINDOWS`, `Linux` → `LINUX`, `Mac` → `MAC`  
`data.properties.OsName.str` | `principal.platform` | Directly mapped  
`os_name` | `principal.platform` | Directly mapped  
`payload.OsName` | `principal.platform` | Directly mapped  
`platform` | `principal.platform` | Directly mapped  
`data.properties.Platform.str` | `principal.platform_version` | Directly mapped  
`os_version` | `principal.platform_version` | Directly mapped  
`payload.OsVersion` | `principal.platform_version` | Directly mapped  
`properties.OsVersion` | `principal.platform_version` | Directly mapped  
`ApiVersion_label` | `principal.resource.attribute.labels` | Merged  
`IsDeleted_label` | `principal.resource.attribute.labels` | Merged  
`LogFileContentType_label` | `principal.resource.attribute.labels` | Merged  
`LogFileLength_label` | `principal.resource.attribute.labels` | Merged  
`LogFile_label` | `principal.resource.attribute.labels` | Merged  
`created_by_id_label` | `principal.resource.attribute.labels` | Merged  
`key` | `principal.resource.attribute.labels` | Mapped: `DisplayedFieldEntities` → `map_field`  
`map_field` | `principal.resource.attribute.labels` | Merged  
`os_name_label` | `principal.resource.attribute.labels` | Merged  
`principal_ip_address` | `principal.resource.attribute.labels` | Merged  
`browser_name` | `principal.resource.name` | Directly mapped  
`data.properties.Browser.str` | `principal.resource.name` | Directly mapped  
`product_object_id` | `principal.resource.product_object_id` | Directly mapped  
`principal_resource_type` | `principal.resource.type` | Directly mapped  
`LoginUrl` | `principal.url` | Directly mapped  
`user_labels` | `principal.user.attribute.labels` | Merged  
`user_permission_label` | `principal.user.attribute.labels` | Merged  
`roles` | `principal.user.attribute.roles` | Merged  
`CreatedBy.Email` | `principal.user.email_addresses` | Merged  
`Email` | `principal.user.email_addresses` | Merged  
`User.Email` | `principal.user.email_addresses` | Merged  
`User.Username` | `principal.user.email_addresses` | Directly mapped  
`attrs.usrName` | `principal.user.email_addresses` | Merged  
`csv_format` | `principal.user.email_addresses` | Mapped: `false` → `attrs.usrName`  
`email` | `principal.user.email_addresses` | Merged  
`properties.Username` | `principal.user.email_addresses` | Merged  
`src_email` | `principal.user.email_addresses` | Mapped: `^.+@.+$` → `src_email`  
`User.Id` | `principal.user.product_object_id` | Directly mapped  
`attrs.USER_ID_DERIVED` | `principal.user.product_object_id` | Renamed/mapped  
`data.properties.USER_ID_DERIVED.str` | `principal.user.product_object_id` | Directly mapped  
`principal_product_object_id` | `principal.user.product_object_id` | Directly mapped  
`payload.UserType` | `principal.user.role_name` | Directly mapped  
`properties.UserType` | `principal.user.role_name` | Directly mapped  
`CreatedBy.Name` | `principal.user.user_display_name` | Directly mapped  
`Name` | `principal.user.user_display_name` | Directly mapped  
`User.Name` | `principal.user.user_display_name` | Directly mapped  
`email` | `principal.user.user_display_name` | Directly mapped  
`profile_name` | `principal.user.user_display_name` | Directly mapped  
`user_display_name` | `principal.user.user_display_name` | Directly mapped  
`username` | `principal.user.user_display_name` | Directly mapped  
`Id` | `principal.user.userid` | Directly mapped  
`USER_ID` | `principal.user.userid` | Directly mapped  
`account` | `principal.user.userid` | Directly mapped  
`attrs.usrName` | `principal.user.userid` | Directly mapped  
`data.properties.LoginKey.str` | `principal.user.userid` | Directly mapped  
`data.properties.USER_ID.str` | `principal.user.userid` | Directly mapped  
`login_key` | `principal.user.userid` | Directly mapped  
`payload.UserId` | `principal.user.userid` | Directly mapped  
`principal_user` | `principal.user.userid` | Directly mapped  
`properties.UserId` | `principal.user.userid` | Directly mapped  
`user_id` | `principal.user.userid` | Directly mapped  
`username` | `principal.user.userid` | Directly mapped  
`action` | `security_result.action` | Mapped: `"ALLOW", "BLOCK"` → `action`  
`csv_format` | `security_result.action` | Mapped: `false` → `sec_action`  
`event_id` | `security_result.action` | Mapped: ` "Login", "LoginAsEvent", "IdentityVerificationEvent"...  
`sec_action` | `security_result.action` | Merged  
`status` | `security_result.action` | Mapped: `Success` → `sec_action`  
`Status` | `security_result.action_details` | Directly mapped  
`action` | `security_result.action_details` | Directly mapped  
`data.properties.Status.str` | `security_result.action_details` | Directly mapped  
`properties.Status` | `security_result.action_details` | Directly mapped  
`detail.payload.Query` | `security_result.category_details` | Merged  
`LoginType` | `security_result.description` | Directly mapped  
`description` | `security_result.description` | Directly mapped  
`logintype` | `security_result.description` | Directly mapped  
`ActionMessage_label` | `security_result.detection_fields` | Merged  
`ElapsedTime_label` | `security_result.detection_fields` | Merged  
`EvaluationTime_label` | `security_result.detection_fields` | Merged  
`Id_label` | `security_result.detection_fields` | Merged  
`NumberOfFailedLogins_label` | `security_result.detection_fields` | Merged  
`PolicyOutcome_label` | `security_result.detection_fields` | Merged  
`User_url_label` | `security_result.detection_fields` | Merged  
`event_id` | `security_result.detection_fields` | Mapped: `AuraRequest` → `ActionMessage_label`  
`type_label` | `security_result.detection_fields` | Merged  
`column5` | `security_result.rule_author` | Directly mapped  
`column1` | `security_result.rule_id` | Directly mapped  
`payload.PolicyId` | `security_result.rule_id` | Directly mapped  
`properties.PolicyId` | `security_result.rule_id` | Directly mapped  
`column4` | `security_result.rule_name` | Directly mapped  
`rule_name` | `security_result.rule_name` | Directly mapped  
`REQUEST_STATUS` | `security_result.summary` | Directly mapped  
`column10` | `security_result.summary` | Directly mapped  
`data.properties.LoginType.str` | `security_result.summary` | Directly mapped  
`forecastcategory` | `security_result.summary` | Directly mapped  
`newvalue` | `security_result.summary` | Directly mapped  
`oldvalue` | `security_result.summary` | Directly mapped  
`summary` | `security_result.summary` | Directly mapped  
`ORGANIZATION_ID` | `target.administrative_domain` | Directly mapped  
`domain` | `target.administrative_domain` | Directly mapped  
`organization_id` | `target.administrative_domain` | Directly mapped  
`properties.OrgName` | `target.administrative_domain` | Directly mapped  
`app_name` | `target.application` | Directly mapped  
`data.properties.Application.str` | `target.application` | Directly mapped  
`payload.AppName` | `target.application` | Directly mapped  
`properties.AppName` | `target.application` | Directly mapped  
`target_host` | `target.asset.hostname` | Directly mapped  
`target_hostname` | `target.asset.hostname` | Directly mapped  
`data.properties.CLIENT_IP.str` | `target.asset.ip` | Merged  
`device_id` | `target.asset_id` | Directly mapped  
`file_type` | `target.file.mime_type` | Directly mapped  
`size_bytes` | `target.file.size` | Directly mapped  
`target_host` | `target.hostname` | Directly mapped  
`target_hostname` | `target.hostname` | Directly mapped  
`data.properties.CLIENT_IP.str` | `target.ip` | Merged  
`QUERY_IDENTIFIER` | `target.process.command_line` | Directly mapped  
`cmd_line` | `target.process.command_line` | Directly mapped  
`data.properties.Query.str` | `target.process.command_line` | Directly mapped  
`query_exec` | `target.process.command_line` | Directly mapped  
`job_id` | `target.process.pid` | Directly mapped  
`PageStartTime_label` | `target.resource.attribute.labels` | Merged  
`call_time` | `target.resource.attribute.labels` | Merged  
`counts_against_api_limit_label` | `target.resource.attribute.labels` | Merged  
`cpu` | `target.resource.attribute.labels` | Merged  
`cpu_time_label` | `target.resource.attribute.labels` | Merged  
`db_blocks_label` | `target.resource.attribute.labels` | Merged  
`db_cpu` | `target.resource.attribute.labels` | Merged  
`db_cpu_time_label` | `target.resource.attribute.labels` | Merged  
`db_total_time_label` | `target.resource.attribute.labels` | Merged  
`db_type` | `target.resource.attribute.labels` | Merged  
`duration_time` | `target.resource.attribute.labels` | Merged  
`entity_name` | `target.resource.attribute.labels` | Merged  
`entity_name_label` | `target.resource.attribute.labels` | Merged  
`entry_p` | `target.resource.attribute.labels` | Merged  
`event_id` | `target.resource.attribute.labels` | Mapped values (5 total, e.g. `ApiEventStream` → `ope`, `ApiEventStream` → `ses_level`, `ApiT...  
`exception_label` | `target.resource.attribute.labels` | Merged  
`exe_time` | `target.resource.attribute.labels` | Merged  
`key` | `target.resource.attribute.labels` | Mapped: `"PageStartTime", "PreviousPageUrl", "Description", "ReportId"` → `map_field`  
`label` | `target.resource.attribute.labels` | Merged  
`map_field` | `target.resource.attribute.labels` | Merged  
`media_type_label` | `target.resource.attribute.labels` | Merged  
`no_sql_que` | `target.resource.attribute.labels` | Merged  
`number_fields_label` | `target.resource.attribute.labels` | Merged  
`ope` | `target.resource.attribute.labels` | Merged  
`query_type_label` | `target.resource.attribute.labels` | Merged  
`rows_proc` | `target.resource.attribute.labels` | Merged  
`rows_proc_label` | `target.resource.attribute.labels` | Merged  
`run` | `target.resource.attribute.labels` | Merged  
`run_time_label` | `target.resource.attribute.labels` | Merged  
`ses_level` | `target.resource.attribute.labels` | Merged  
`sql_id_label` | `target.resource.attribute.labels` | Merged  
`ss_type` | `target.resource.attribute.labels` | Merged  
`total_time` | `target.resource.attribute.labels` | Merged  
`uripath_label` | `target.resource.attribute.labels` | Merged  
`user_derieved_label` | `target.resource.attribute.labels` | Merged  
`user_ty` | `target.resource.attribute.labels` | Merged  
`user_type_label` | `target.resource.attribute.labels` | Merged  
`verify_method` | `target.resource.attribute.labels` | Merged  
`wave` | `target.resource.attribute.labels` | Merged  
`URI` | `target.resource.id` | Directly mapped  
`accountid` | `target.resource.id` | Directly mapped  
`attrs.AccountId` | `target.resource.id` | Renamed/mapped  
`attrs.CaseId` | `target.resource.id` | Renamed/mapped  
`attrs.ContactId` | `target.resource.id` | Renamed/mapped  
`caseid` | `target.resource.id` | Directly mapped  
`contactid` | `target.resource.id` | Directly mapped  
`detail.id` | `target.resource.id` | Directly mapped  
`leadid` | `target.resource.id` | Directly mapped  
`opportunityid` | `target.resource.id` | Directly mapped  
`payload.RecordId` | `target.resource.id` | Directly mapped  
`properties.RecordId` | `target.resource.id` | Directly mapped  
`request_id` | `target.resource.id` | Directly mapped  
`StageName` | `target.resource.name` | Directly mapped  
`data.properties.DATASET_IDS.str` | `target.resource.name` | Directly mapped  
`field` | `target.resource.name` | Directly mapped  
`properties.Name` | `target.resource.name` | Directly mapped  
`resource_name` | `target.resource.name` | Directly mapped  
`column13` | `target.resource.product_object_id` | Directly mapped  
`data.properties.REQUEST_ID.str` | `target.resource.product_object_id` | Directly mapped  
`properties.OrgId` | `target.resource.product_object_id` | Directly mapped  
`target_product_object_id` | `target.resource.product_object_id` | Directly mapped  
`event_id` | `target.resource.resource_type` | Mapped: `PlatformEncryption` → `ACCESS_POLICY`, `ApexCallout` → `ACCESS_POLICY`, `ApexTrigge...  
`target_resource_type` | `target.resource.resource_type` | Directly mapped  
`event_id` | `target.resource.type` | Mapped: `(QueuedExecution/ApexExecution)` → `BATCH`, `ApexTrigger` → `DATABASE_TRIGGER`, `Co...  
`URI` | `target.url` | Directly mapped  
`attrs.LoginUrl` | `target.url` | Renamed/mapped  
`attrs.attributes.url` | `target.url` | Renamed/mapped  
`login_url` | `target.url` | Directly mapped  
`payload.LoginUrl` | `target.url` | Directly mapped  
`properties.LoginUrl` | `target.url` | Directly mapped  
`properties.PageUrl` | `target.url` | Directly mapped  
`uri` | `target.url` | Directly mapped  
`uripath` | `target.url` | Directly mapped  
`attrs.usrName` | `target.user.email_addresses` | Merged  
`csv_format` | `target.user.email_addresses` | Mapped: `false` → `attrs.usrName`  
`email_address` | `target.user.email_addresses` | Merged  
`event_id` | `target.user.email_addresses` | Mapped: `Logout` → `attrs.usrName`  
`target_user_display_name` | `target.user.user_display_name` | Directly mapped  
`column5` | `target.user.userid` | Directly mapped  
`data.properties.CreatedById.str` | `target.user.userid` | Directly mapped  
`data.properties.UserId.str` | `target.user.userid` | Directly mapped  
`detail.payload.UserId` | `target.user.userid` | Directly mapped  
`target_login_key` | `target.user.userid` | Directly mapped  
`target_user_id` | `target.user.userid` | Directly mapped  
`target_user_name` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.auth_details` | Constant: `ACTIVE`  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `USER_UNCATEGORIZED`  
N/A | `metadata.product_name` | Constant: `SALESFORCE`  
N/A | `metadata.vendor_name` | Constant: `SALESFORCE`  
N/A | `network.application_protocol` | Constant: `HTTP`  
N/A | `network.http.parsed_user_agent` | Constant: `parseduseragent`  
N/A | `principal.platform` | Constant: `WINDOWS`  
N/A | `principal.resource.type` | Constant: `USER`  
N/A | `target.resource.resource_type` | Constant: `ACCESS_POLICY`  
N/A | `target.resource.type` | Constant: `BATCH`  
`column17` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`column5` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`user_type` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`USER_ID_DERIVED` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`ApiVersion` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column9` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`column9` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`column9` | `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
`column4` | `event.idm.read_only_udm.target.administrative_domain` | Mapped from changelog  
`column18` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`request_id` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`column13` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`column18` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`column20` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column8` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`column7` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column16` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`login_subtype` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column28` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column26` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`source_ip` | `event.idm.read_only_udm.principal.nat_ip` | Mapped from changelog  
`x_forwarded_for_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column13` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`column14` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`properties.Description` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`properties.City` | `event.idm.read_only_udm.principal.location.city` | Mapped from changelog  
`properties.AppName` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`properties.OrgId` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`properties.OrgName` | `event.idm.read_only_udm.target.administrative_domain` | Mapped from changelog  
`namespace` | `event.idm.read_only_udm.principal.namespace` | Mapped from changelog  
`properties.LoginUrl, properties.PageUrl` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`properties.Application` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`recordDate` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`name` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`properties.Username` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`properties.UserId` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`properties.UserType` | `event.idm.read_only_udm.principal.user.role_name` | Mapped from changelog  
`properties.Country` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`properties.SourceIp` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`properties.SourceIp` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`properties.SourceIp (if not a valid IP), properties.OsName (if not Windows, Linux, or Mac), properties.DisplayedFieldEntities` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`properties.TlsProtocol` | `event.idm.read_only_udm.network.tls.version` | Mapped from changelog  
`properties.CipherSuite` | `event.idm.read_only_udm.network.tls.cipher` | Mapped from changelog  
`properties.EventDate, startTime` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`properties.EventIdentifier` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`properties.HttpMethod` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`properties.HttpMethod` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`properties.LoginLatitude` | `event.idm.read_only_udm.principal.location.region_latitude` | Mapped from changelog  
`properties.LoginLongitude` | `event.idm.read_only_udm.principal.location.region_longitude` | Mapped from changelog  
`properties.OsName, properties.Platform` | `event.idm.read_only_udm.principal.platform` | Mapped from changelog  
`properties.OsVersion` | `event.idm.read_only_udm.principal.platform_version` | Mapped from changelog  
`properties.RecordId` | `event.idm.read_only_udm.target.resource.id` | Mapped from changelog  
`properties.SessionKey` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`properties.UserAgent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`properties.UserAgent` | `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
`properties.PageStartTime, properties.PreviousPageUrl, properties.Description, properties.ReportId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`properties.Name` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`and` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detail.payload.ConnectedAppId` | `additional.fields` | Mapped from changelog  
`detail.payload.Platform` | `additional.fields` | Mapped from changelog  
`detail.payload.EvaluationTime` | `additional.fields` | Mapped from changelog  
`detail.payload.Operation` | `additional.fields` | Mapped from changelog  
`detail.payload.LoginHistoryId` | `additional.fields` | Mapped from changelog  
`detail.payload.CreatedById` | `additional.fields` | Mapped from changelog  
`detail.payload.SessionKey` | `additional.fields` | Mapped from changelog  
`detail.payload.ApiType` | `additional.fields` | Mapped from changelog  
`detail.payload.PolicyOutcome` | `security_result.detection_fields` | Mapped from changelog  
`detail.payload.EventIdentifier` | `additional.fields` | Mapped from changelog  
`detail.payload.RequestIdentifier` | `additional.fields` | Mapped from changelog  
`detail.payload.ApiVersion` | `additional.fields` | Mapped from changelog  
`detail.payload.RelatedEventIdentifier` | `additional.fields` | Mapped from changelog  
`detail.payload.Username` | `target.user.email_addresses` | Mapped from changelog  
`detail.payload.RowsProcessed` | `additional.fields` | Mapped from changelog  
`detail.payload.RowsReturned` | `additional.fields` | Mapped from changelog  
`detail.payload.SourceIp` | `principal.ip` | Mapped from changelog  
`detail.payload.CreatedDate` | `additional.fields` | Mapped from changelog  
`detail.payload.LoginKey` | `additional.fields` | Mapped from changelog  
`detail.payload.Application` | `additional.fields` | Mapped from changelog  
`detail.payload.PolicyId` | `additional.fields` | Mapped from changelog  
`detail.payload.QueriedEntities` | `additional.fields` | Mapped from changelog  
`detail.payload.SessionLevel` | `additional.fields` | Mapped from changelog  
`detail.schemaId` | `additional.fields` | Mapped from changelog  
`records_index.attributes.type` | `security_result.detection_fields` | Mapped from changelog  
`column25` | `network.http.user_agent` | Mapped from changelog  
`column24` | `network.http.user_agent` | Mapped from changelog  
`column24` | `network.http.method` | Mapped from changelog  
`CreatedBy.FederationIdentifier` | `additional.fields` | Mapped from changelog  
`Section` | `additional.fields` | Mapped from changelog  
`DelegateUser` | `additional.fields` | Mapped from changelog  
`ResponsibleNamespacePrefix` | `additional.fields` | Mapped from changelog  
`payload.PreviousPageEntityId", "payload.SdkVersion", "payload.Operation", "payload.PageUrl", "HasEffectivePageTimeDeviation_label", "payload.EffectivePageTime", "payload.EffectivePageTimeDeviationReason", "payload.DeviceSessionId", "payload.PreviousPageAppName", and "payload.PreviousPageEntityType` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/salesforce-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
