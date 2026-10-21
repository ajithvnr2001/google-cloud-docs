---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bluecoat-webproxy/
title: Collect Blue Coat ProxySG logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:33.699739+00:00
---

# Collect Blue Coat ProxySG logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bluecoat-webproxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Blue Coat ProxySG logs

**Parser Version:** 32.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Blue Coat ProxySG logs to Google Security Operations using the Bindplane agent.

Blue Coat ProxySG (now Broadcom/Symantec) is a web proxy appliance that generates access logs for web traffic, including HTTP requests, categories, authentication, and security events. The parser normalizes fields and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Blue Coat ProxySG appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Blue Coat ProxySG management console



## Get Google SecOps credentials for the Bindplane agent

To authenticate the Bindplane agent to Google SecOps, choose one of the following methods:

  * **New deployments** : Use the Chronicle API (Option 1).
  * **Legacy deployments** : Continue using the ingestion authentication file (Option 2) until the Ingestion API is discontinued on July 20, 2027.



### Option 1: Create a service account for the Chronicle API (recommended)

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/) and select the Google Cloud project that is linked to your Google SecOps instance.
  2. Go to **IAM & Admin > Service Accounts**.
  3. Click **Create service account**.
  4. Provide the following configuration details: 
     * **Service account name** : Enter a name for the account (for example, `bindplane-ingest`).
     * **Service account description** : Enter a description (for example, `Bindplane agent log ingestion`).
  5. Click **Create and continue**.
  6. In the **Grant this service account access to project** section, click **Select a role** and select **Chronicle Editor**.
  7. Click **Continue** , and then click **Done**.
  8. Click the service account you created, and then go to the **Keys** tab.
  9. Click **Add key > Create new key**.
  10. Select **JSON** and click **Create**. The key file is downloaded to your computer.
  11. Save the key file as `ingestion-auth.json` in the Bindplane collector directory (`/opt/observiq-otel-collector/ingestion-auth.json` on Linux or `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json` on Windows), or update `creds_file_path` in `config.yaml` to match the path where you save it.
  12. Go to **IAM & Admin > Settings** and copy the **Project number**. You'll need it for the exporter configuration.

**Note:** The JSON key is a credential. Restrict access to the file on the Bindplane host and rotate the key according to your organization's policy.

### Option 2: Download the ingestion authentication file (legacy)

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **ingestion authentication file**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

**Note:** This file authenticates the agent to the legacy Ingestion API (`malachiteingestion-pa.googleapis.com`), which Google has scheduled for end of life on July 20, 2027. Plan to move to Option 1 before that date.

## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.

**Note:** The customer ID is required for configuring the Bindplane agent exporter.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         

The service should show as **RUNNING**.




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         

The service should show as **active (running)**.




### Additional installation resources

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          tcplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/bluecoat_webproxy:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: BLUECOAT_WEBPROXY
            raw_log_field: body
        
        service:
          pipelines:
            logs/bluecoat_webproxy_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/bluecoat_webproxy
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/bluecoat_webproxy:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: BLUECOAT_WEBPROXY
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux, run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

    1. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    2. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           

  * To restart the Bindplane agent in Windows, choose one of the following options:

    * Command Prompt or PowerShell as administrator:
          
          net stop observiq-otel-collector && net start observiq-otel-collector
          

    * Services console:

      1. Press `Win+R`, type `services.msc`, and press Enter.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.
      4. Verify the service is running:
             
             sc query observiq-otel-collector
             

      5. Check logs for errors:
             
             type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
             




## Configure syslog in Blue Coat ProxySG

  1. Sign in to the **Blue Coat ProxySG** management console.
  2. Go to **Maintenance > Event Logging > Syslog**.
  3. Click **New**.
  4. Provide the following configuration details: 
     * **Loghost** : Enter the Bindplane agent IP address.
     * Click **OK**.
  5. Select the **Enable Syslog** checkbox.
  6. Select **Level**.
  7. Select the **Verbose** checkbox.
  8. Click **Apply**.



## Configure a custom client in Blue Coat ProxySG

  1. Go to **Configuration > Access Logging > Logs > Upload Client**.
  2. Select **Streaming** in the Log list.
  3. Select **Custom Client** from the Client type list.
  4. Click **Settings**.
  5. Select to configure the **primary** or **alternate** custom server from the **Settings** list.
  6. Provide the following configuration details: 
     * **Host** : Enter the hostname or IP address of the upload destination.
     * **Port** : Set to **514**.
     * Use secure connections (SSL): Set to **Off**.
     * Click **OK**.
     * Click **Apply** to return to the **Upload Client** tab.
  7. For each log format you want to use among main, im, and streaming, complete the following steps: 
     * Select the **log**.
     * Assign the **Upload Client** to be the **Custom** client.
     * Select `<No Encryption>` and `<No Signing>`.
     * Save the log file as a text file.
     * Click **Upload Schedule > Upload Type**.
     * Select **Continuously** for **Upload the access log** to stream the access logs.
     * Click **OK**.
  8. Click **Apply**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`@timestamp` | `metadata.event_timestamp` | The timestamp of the event as recorded by the Blue Coat appliance. Parsed from the JSON data.  
`application-name` | `target.application` | The name of the application associated with the network traffic. Parsed from the JSON data.  
`c-ip` | `principal.asset.ipprincipal.ip` | Client IP address. Parsed from the JSON data.  
`c_ip` | `principal.ipprincipal.asset.ip` | Client IP address. Parsed from various log formats.  
`c_ip_host` | `principal.hostnameprincipal.asset.hostname` | Client hostname, if available. Parsed from the JSON data.  
`cs-auth-group` | principal_user_group_identifiers | Client authentication group. Parsed from the JSON data.  
`cs-bytes` | `network.sent_bytes` | Number of bytes sent by the client. Parsed from the JSON data.  
`cs-categories` | `security_result.category_details` | Categories assigned to the web request by the Blue Coat appliance. Parsed from the JSON data.  
`cs-host` | target_hostname | Hostname requested by the client. Parsed from the JSON data.  
`cs-icap-error-details` | `security_result.detection_fields` | ICAP error details from the client side. Parsed from the JSON data, key is "cs-icap-error-details".  
`cs-icap-status` | `security_result.description` | ICAP status from the client side. Parsed from the JSON data.  
`cs-method` | `network.http.method` | HTTP method used in the request. Parsed from the JSON data.  
`cs-threat-risk` | `security_result.risk_score` | Threat risk score assigned by the Blue Coat appliance. Parsed from the JSON data.  
`cs-uri-extension` | cs_uri_extension | Extension of the requested URI. Parsed from the JSON data.  
`cs-uri-path` | _uri_path | Path of the requested URI. Parsed from the JSON data.  
`cs-uri-port` | cs_uri_port | Port of the requested URI. Parsed from the JSON data.  
`cs-uri-query` | _uri_query | Query string of the requested URI. Parsed from the JSON data.  
`cs-uri-scheme` | _uri_scheme | Scheme of the requested URI (e.g., http, https). Parsed from the JSON data.  
`cs-userdn` | principal_user_userid | Client username. Parsed from the JSON data.  
`cs-version` | cs_version | HTTP version used by the client. Parsed from the JSON data.  
`cs(Referer)` | `network.http.referral_url` | Referrer URL. Parsed from the JSON data.  
`cs(User-Agent)` | `network.http.user_agent` | User-agent string. Parsed from the JSON data.  
`cs(X-Requested-With)` | `security_result.detection_fields` | Value of the X-Requested-With header. Parsed from the JSON data, key is "cs-X-Requested-With".  
`cs_auth_group` | principal_user_group_identifiers | Client authentication group. Parsed from various log formats.  
`cs_bytes` | `network.sent_bytes` | Number of bytes sent by the client. Parsed from various log formats.  
`cs_categories` | `security_result.category_details` | Categories assigned to the web request. Parsed from various log formats.  
`cs_host` | target_hostname | Hostname requested by the client. Parsed from various log formats.  
`cs_method` | `network.http.method` | HTTP method used in the request. Parsed from various log formats.  
`cs_referer` | `network.http.referral_url` | Referrer URL. Parsed from various log formats.  
`cs_threat_risk` | `security_result.risk_score` | Threat risk score assigned by the Blue Coat appliance. Parsed from the KV log format.  
`cs_uri` | `target.url` | Full requested URI. Parsed from the KV log format.  
`cs_uri_extension` | cs_uri_extension | Extension of the requested URI. Parsed from the KV log format.  
`cs_uri_path` | _uri_path | Path of the requested URI. Parsed from various log formats.  
`cs_uri_port` | target_port | Port of the requested URI. Parsed from various log formats.  
`cs_uri_query` | _uri_query | Query string of the requested URI. Parsed from various log formats.  
`cs_uri_scheme` | _uri_scheme | Scheme of the requested URI (e.g., http, https). Parsed from various log formats.  
`cs_user` | principal_user_userid | Client username. Parsed from the general log format.  
`cs_user_agent` | `network.http.user_agent` | User-agent string. Parsed from various log formats.  
`cs_username` | principal_user_userid | Client username. Parsed from various log formats.  
`cs_x_forwarded_for` | `_intermediary.ip` | X-Forwarded-For header value. Parsed from the general log format.  
`deviceHostname` | `_intermediary.hostname` | Hostname of the Blue Coat appliance. Parsed from the KV log format.  
`dst` | ip_target | Destination IP address. Parsed from the KV log format.  
`dst_ip` | ip_target | Destination IP address. Parsed from the SSL log format.  
`dst_user` | `target.user.userid` | Destination user ID. Parsed from the Proxy Reverse log format.  
`dstport` | target_port | Destination port. Parsed from the KV log format.  
`dstport` | `target.port` | Destination port. Parsed from the SSL log format.  
`exception-id` | _block_reason | Exception ID, indicating a blocked request. Parsed from the KV log format.  
`filter-category` | _categories | Category of the filter that triggered the event. Parsed from the KV log format.  
`filter-result` | _policy_action | Result of the filter applied to the request. Parsed from the KV log format.  
`hostname` | `principal.hostnameprincipal.asset.hostname` | Hostname of the device generating the log. Parsed from the SSL and general log formats.  
`isolation-url` | isolation-url | URL related to isolation, if applicable. Parsed from the JSON data.  
`ma-detonated` | ma-detonated | Malware detonation status. Parsed from the JSON data.  
`page-views` | page-views | Number of page views. Parsed from the JSON data.  
`r-ip` | ip_target | Remote IP address. Parsed from the JSON data.  
`r-supplier-country` | r-supplier-country | Country of the remote supplier. Parsed from the JSON data.  
`r_dns` | target_hostname | Remote DNS name. Parsed from the JSON data.  
`r_ip` | ip_target | Remote IP address. Parsed from various log formats.  
`r_port` | target_port | Remote port. Parsed from the JSON data.  
`risk-groups` | `security_result.detection_fields` | Risk groups associated with the event. Parsed from the JSON data, key is "risk-groups".  
`rs-icap-error-details` | `security_result.detection_fields` | ICAP error details from the remote server side. Parsed from the JSON data, key is "rs-icap-error-details".  
`rs-icap-status` | rs-icap-status | ICAP status from the remote server side. Parsed from the JSON data.  
`rs(Content-Type)` | `target.file.mime_type` | Content-type of the response from the remote server. Parsed from the KV log format.  
`rs_content_type` | `target.file.mime_type` | Content-type of the response from the remote server. Parsed from various log formats.  
`rs_server` | rs_server | Remote server information. Parsed from the JSON data.  
`rs_status` | `_network.http.response_code` | Response status code from the remote server. Parsed from the JSON data.  
`r_supplier_country` | `intermediary.location.country_or_region` | Country of the remote supplier. Parsed from the general log format.  
`r_supplier_ip` | `intermediary.ip` | IP address of the remote supplier. Parsed from the general log format.  
`s-action` | `_metadata.product_event_type` | Action taken by the proxy. Parsed from the KV log format.  
`s-ip` | `_intermediary.ip` | Server IP address. Parsed from the KV log format.  
`s-source-ip` | `_intermediary.ip` | Source IP address of the server. Parsed from the JSON data.  
`s_action` | `_metadata.product_event_type` | Action taken by the proxy. Parsed from various log formats.  
`s_ip` | `target.iptarget.asset.ip` | Server IP address. Parsed from various log formats.  
`s_ip_host` | `_intermediary.hostname` | Server hostname. Parsed from the JSON data.  
`s-supplier-country` | `intermediary.location.country_or_region` | Country of the supplier server. Parsed from the JSON data.  
`s-supplier-failures` | `security_result.detection_fields` | Supplier failures. Parsed from the JSON data, key is "s-supplier-failures".  
`s-supplier-ip` | `_intermediary.ip` | Supplier server IP address. Parsed from the JSON data.  
`s_supplier_ip` | `intermediary.ip` | Supplier server IP address. Parsed from the JSON data.  
`s_supplier_name` | `_intermediary.hostname` | Supplier server name. Parsed from the general log format.  
`sc-bytes` | `network.received_bytes` | Number of bytes received by the server. Parsed from the KV log format.  
`sc-filter-result` | _policy_action | Filter result from the server side. Parsed from the KV log format.  
`sc-status` | `_network.http.response_code` | Status code returned by the server. Parsed from the KV log format.  
`sc_bytes` | `network.received_bytes` | Number of bytes received by the server. Parsed from various log formats.  
`sc_connection` | sc_connection | Server connection information. Parsed from the general log format.  
`sc_filter_result` | _policy_action | Filter result from the server side. Parsed from various log formats.  
`sc_status` | `_network.http.response_code` | Status code returned by the server. Parsed from various log formats.  
`search_query` | `target.resource.attribute.labels` | Search query, if present in the URL. Extracted fromtarget_url, key is "search_query".  
`session_id` | `network.session_id` | Session ID. Parsed from the Proxy Reverse log format.  
`src` | ip_principal | Source IP address. Parsed from the KV log format.  
`src_hostname` | `principal.hostnameprincipal.asset.hostname` | Source hostname. Parsed from the general log format.  
`src_ip` | ip_principal | Source IP address. Parsed from the SSL log format.  
`srcport` | principal_port | Source port. Parsed from the KV log format.  
`src_port` | `principal.port` | Source port. Parsed from the SSL log format.  
`s_source_port` | `intermediary.port` | Source port of the server. Parsed from the general log format.  
`summary` | `security_result.summary` | Summary of the security result. Parsed from the Proxy Reverse and SSL log formats.  
`syslogtimestamp` | syslogtimestamp | Syslog timestamp. Parsed from the KV log format.  
`target_application` | `target.application` | Application targeted by the request. Derived fromx_bluecoat_application_nameorapplication-name.  
`target_hostname` | `target.hostnametarget.asset.hostname` | Target hostname. Derived fromr_dns,cs-host, or other fields depending on the log format.  
`target_port` | `target.port` | Target port. Derived fromr_port,cs_uri_port, ordstportdepending on the log format.  
`target_sip` | `target.iptarget.asset.ip` | Target server IP address. Parsed from the general log format.  
`target_url` | `target.url` | Target URL. Derived fromtarget_hostname,_uri_path, and_uri_queryorcs_uri.  
`time-taken` | `network.session_duration` | Duration of the session or request. Parsed from the KV log format and converted to seconds and nanoseconds.  
`time_taken` | `network.session_duration` | Duration of the session or request. Parsed from various log formats and converted to seconds and nanoseconds.  
`tls_version` | `network.tls.version` | TLS version used in the connection. Parsed from the SSL log format.  
`upload-source` | upload-source | Source of the upload. Parsed from the JSON data.  
`username` | principal_user_userid | Username. Parsed from the KV log format.  
`verdict` | `security_result.detection_fields` | Verdict of the security analysis. Parsed from the JSON data, key is "verdict".  
`wf-env` | wf_env | Environment of the web filtering service. Parsed from the JSON data.  
`wf_id` | `security_result.detection_fields` | Web filtering ID. Parsed from the JSON data, key is "wf_id".  
`wrong_cs_host` | `principal.hostnameprincipal.asset.hostname` | Incorrectly parsed client hostname, used as principal hostname if it's not an IP address. Parsed from the general log format.  
`x-bluecoat-access-type` | x-bluecoat-access-type | Type of access. Parsed from the JSON data.  
`x-bluecoat-appliance-name` | `intermediary.application` | Name of the Blue Coat appliance. Parsed from the JSON data.  
`x-bluecoat-application-name` | target_application | Name of the application. Parsed from the JSON data.  
`x-bluecoat-application-operation` | x_bluecoat_application_operation | Application operation. Parsed from the JSON data.  
`x-bluecoat-location-id` | x-bluecoat-location-id | Location ID. Parsed from the JSON data.  
`x-bluecoat-location-name` | x-bluecoat-location-name | Location name. Parsed from the JSON data.  
`x-bluecoat-placeholder` | `security_result.detection_fields` | Placeholder information. Parsed from the JSON data, key is "x-bluecoat-placeholder".  
`x-bluecoat-reference-id` | `security_result.detection_fields` | Reference ID. Parsed from the JSON data, key is "x-bluecoat-reference-id".  
`x-bluecoat-request-tenant-id` | x-bluecoat-request-tenant-id | Tenant ID of the request. Parsed from the JSON data.  
`x-bluecoat-transaction-uuid` | `metadata.product_log_id` | Transaction UUID. Parsed from the JSON data.  
`x-client-agent-sw` | `software.name` | Client agent software. Parsed from the JSON data and merged intoprincipal.asset.software.  
`x-client-agent-type` | `principal.application` | Client agent type. Parsed from the JSON data.  
`x-client-device-id` | `principal.resource.product_object_id` | Client device ID. Parsed from the JSON data.  
`x-client-device-name` | x-client-device-name | Client device name. Parsed from the JSON data.  
`x-client-device-type` | x-client-device-type | Client device type. Parsed from the JSON data.  
`x-client-os` | `principal.asset.platform_software.platform` | Client operating system. Parsed from the JSON data. If contains "Windows", sets platform to WINDOWS.  
`x-client-security-posture-details` | x-client-security-posture-details | Client security posture details. Parsed from the JSON data.  
`x-client-security-posture-risk-score` | `security_result.detection_fields` | Client security posture risk score. Parsed from the JSON data, key is "x-client-security-posture-risk-score".  
`x-cloud-rs` | `security_result.detection_fields` | Cloud-related remote server information. Parsed from the JSON data, key is "x-cloud-rs".  
`x-cs-certificate-subject` | x_cs_certificate_subject | Certificate subject from the client side. Parsed from the JSON data.  
`x-cs-client-ip-country` | x-cs-client-ip-country | Client IP country. Parsed from the JSON data.  
`x-cs-connection-negotiated-cipher` | `network.tls.cipher` | Negotiated cipher from the client side. Parsed from the JSON data.  
`x-cs-connection-negotiated-cipher-size` | `security_result.detection_fields` | Negotiated cipher size from the client side. Parsed from the JSON data, key is "x-cs-connection-negotiated-cipher-size".  
`x-cs-connection-negotiated-ssl-version` | `network.tls.version_protocol` | Negotiated SSL version from the client side. Parsed from the JSON data.  
`x-cs-ocsp-error` | `security_result.detection_fields` | OCSP error from the client side. Parsed from the JSON data, key is "x-cs-ocsp-error".  
`x-cs(referer)-uri-categories` | x-cs(referer)-uri-categories | Referrer URI categories from the client side. Parsed from the JSON data.  
`x-data-leak-detected` | `security_result.detection_fields` | Data leak detection status. Parsed from the JSON data, key is "x-data-leak-detected".  
`x-exception-id` | x_exception_id | Exception ID. Parsed from the JSON data.  
`x-http-connect-host` | x-http-connect-host | HTTP connect host. Parsed from the JSON data.  
`x-http-connect-port` | x-http-connect-port | HTTP connect port. Parsed from the JSON data.  
`x-icap-reqmod-header(x-icap-metadata)` | x_icap_reqmod_header | ICAP request modification header containing metadata. Parsed from the JSON data.  
`x-icap-respmod-header(x-icap-metadata)` | x_icap_respmod_header | ICAP response modification header containing metadata. Parsed from the JSON data.  
`x-rs-certificate-hostname` | `network.tls.client.server_name` | Certificate hostname from the remote server side. Parsed from the JSON data.  
`x-rs-certificate-hostname-categories` | x_rs_certificate_hostname_category | Certificate hostname categories from the remote server side. Parsed from the JSON data.  
`x-rs-certificate-hostname-category` | x_rs_certificate_hostname_category | Certificate hostname category from the remote server side. Parsed from the JSON data.  
`x-rs-certificate-hostname-threat-risk` | `security_result.detection_fields` | Certificate hostname threat risk from the remote server side. Parsed from the JSON data, key is "x-rs-certificate-hostname-threat-risk".  
`x-rs-certificate-observed-errors` | x_rs_certificate_observed_errors | Certificate observed errors from the remote server side. Parsed from the JSON data.  
`x-rs-certificate-validate-status` | `network.tls.server.certificate.subject` | Certificate validation status from the remote server side. Parsed from the JSON data.  
`x-rs-connection-negotiated-cipher` | x_rs_connection_negotiated_cipher | Negotiated cipher from the remote server side. Parsed from the JSON data.  
`x-rs-connection-negotiated-cipher-size` | `security_result.detection_fields` | Negotiated cipher size from the remote server side. Parsed from the JSON data, key is "x-rs-connection-negotiated-cipher-size".  
`x-rs-connection-negotiated-cipher-strength` | x_rs_connection_negotiated_cipher_strength | Negotiated cipher strength from the remote server side. Parsed from the JSON data.  
`x-rs-connection-negotiated-ssl-version` | x_rs_connection_negotiated_ssl_version | Negotiated SSL version from the remote server side. Parsed from the JSON data.  
`x-rs-ocsp-error` | x_rs_ocsp_error | OCSP error from the remote server side. Parsed from the JSON data.  
`x-sc-connection-issuer-keyring` | `security_result.detection_fields` | Connection issuer key ring. Parsed from the JSON data, key is "x-sc-connection-issuer-keyring".  
`x-sc-connection-issuer-keyring-alias` | x-sc-connection-issuer-keyring-alias | Connection issuer key ring alias. Parsed from the JSON data.  
`x-sr-vpop-country` | `principal.location.country_or_region` | VPOP country. Parsed from the JSON data.  
`x-sr-vpop-country-code` | `principal.location.country_or_region` | VPOP country code. Parsed from the JSON data.  
`x-sr-vpop-ip` | `principal.ipprincipal.asset.ip` | VPOP IP address. Parsed from the JSON data.  
`x-symc-dei-app` | x-symc-dei-app | Symantec DEI application. Parsed from the JSON data.  
`x-symc-dei-via` | `security_result.detection_fields` | Symantec DEI via. Parsed from the JSON data, key is "x-symc-dei-via".  
`x-tenant-id` | `security_result.detection_fields` | Tenant ID. Parsed from the JSON data, key is "x-tenant-id".  
`x-timestamp-unix` | x-timestamp-unix | Unix timestamp. Parsed from the JSON data.  
`x_bluecoat_application_name` | target_application | Application name. Parsed from various log formats.  
`x_bluecoat_application_operation` | x_bluecoat_application_operation | Application operation. Parsed from various log formats.  
`x_bluecoat_transaction_uuid` | `metadata.product_log_id` | Transaction UUID. Parsed from various log formats.  
`x_cs_certificate_subject` | x_cs_certificate_subject | Client-side certificate subject. Parsed from the general log format.  
`x_cs_client_effective_ip` | ip_principal | Client's effective IP address. Parsed from the general log format.  
`x_cs_connection_negotiated_cipher` | `network.tls.cipher` | Client-side negotiated cipher. Parsed from the general log format.  
`x_cs_connection_negotiated_ssl_version` | `network.tls.version_protocol` | Client-side negotiated SSL version. Parsed from the general log format.  
`x_exception_id` | _block_reason | Exception ID. Parsed from various log formats.  
`x_icap_reqmod_header` | x_icap_reqmod_header | ICAP request modification header. Parsed from the general log format.  
`x_icap_respmod_header` | x_icap_respmod_header | ICAP response modification header. Parsed from the general log format.  
`x_rs_certificate_hostname` | `network.tls.client.server_name` | Remote server certificate hostname. Parsed from the general log format.  
`x_rs_certificate_hostname_category` | x_rs_certificate_hostname_category | Remote server certificate hostname category. Parsed from the general log format.  
`x_rs_certificate_observed_errors` | x_rs_certificate_observed_errors | Remote server certificate observed errors. Parsed from the general log format.  
`x_rs_certificate_validate_status` | `network.tls.server.certificate.subject` | Remote server certificate validation status. Parsed from various log formats.  
`x_rs_connection_negotiated_cipher_strength` | x_rs_connection_negotiated_cipher_strength | Remote server negotiated cipher strength. Parsed from the general log format.  
`x_rs_connection_negotiated_ssl_version` | x_rs_connection_negotiated_ssl_version | Remote server negotiated SSL version. Parsed from the general log format.  
`x_virus_id` | `security_result.detection_fields` | Virus ID. Parsed from various log formats, key is "x-virus-id".  
`xbluecoat_application_operation` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs_host` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`c_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`c_ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`cs_host` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`cs_host` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`i_hostname` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`i_ip` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`descrip` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`description` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`sum1` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`sum2` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`sum3` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`details` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`ip_principal` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`ip_principal` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`t_ip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`t_ip` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`t_hostname` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`rc` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`cs_method` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`cs_user_agent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`cs_refer` | `event.idm.read_only_udm.network.http.referral_url` | Mapped from changelog  
`rs_service_latency` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_icap_reqmod_header` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_icap_respmod_header` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_bluecoat_app_operation` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_bluecoat_total_time_added` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`policy_evaluation_time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_bluecoat_appliance_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs_connection_ssl_server_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rs_connection_ssl_server_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x_data_leak_detected` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`r_Ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`s-ip` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`cs-uri-port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`cs-host` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`r-ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`c-ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`dest_host" and "target_hostname` | `target.url` | Mapped from changelog  
`proxy_name" and "column3` | `principal.asset.hostname` | Mapped from changelog  
`upload-source` | `additional.fields` | Mapped from changelog  
`time-taken` | `session_duration.session_duration` | Mapped from changelog  
`file_reputation` | `security_result.detection_fields` | Mapped from changelog  
`expect_sandbox` | `security_result.detection_fields` | Mapped from changelog  
`cs_auth_groups` | `principal.user.group_identifiers` | Mapped from changelog  
`time_taken` | `network.session_duration.nanos` | Mapped from changelog  
`cs-userdn` | `principal.user.userid` | Mapped from changelog  
`application-name` | `target.application` | Mapped from changelog  
`rs_server` | `security_result.about.labels` | Mapped from changelog  
`c_uri_path_query` | `target.file.full_path` | Mapped from changelog  
`metadata.event_type` | `STATUS_UPDATE` | Mapped from changelog  
`cs-uri-scheme` | `network.ip_protocol` | Mapped from changelog  
`rule_name` | `security_result.rule_name` | Mapped from changelog  
`application_protocol` | `network.application_protocol` | Mapped from changelog  
`communication_type` | `security_result.rule_name` | Mapped from changelog  
`rule_name` | `security_result.about.labels` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bluecoat-webproxy-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
