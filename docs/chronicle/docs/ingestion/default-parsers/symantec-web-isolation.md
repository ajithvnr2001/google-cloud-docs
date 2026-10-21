---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-web-isolation/
title: Collect Symantec Web Isolation logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:08:31.301956+00:00
---

# Collect Symantec Web Isolation logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-web-isolation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Symantec Web Isolation logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Symantec Web Isolation logs to Google Security Operations using the Bindplane agent.

Symantec Web Isolation is a browser isolation platform that generates syslog messages for web browsing sessions, URL access events, file download activity, policy enforcement, and device management events. The parser extracts fields from JSON-formatted logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Symantec Web Isolation platform
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Symantec Web Isolation web UI



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where Bindplane will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



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

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/symantec_web_isolation:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: SYMANTEC_WEB_ISOLATION
                raw_log_field: body
        
        service:
            pipelines:
                logs/symantec_web_isolation_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/symantec_web_isolation
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list



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
             




## Configure syslog in Symantec Web Isolation platform

  1. Sign in to the **Symantec Web Isolation** web UI.
  2. Go to **System Configuration > External Log Server > New External Log Server > Syslog Server**.
  3. Provide the following configuration details: 
     * **Status** : Select the checkbox to **Enable**.
     * **Host** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number (for example, `514` for **UDP**).
     * **Protocol** : Select **UDP**.
     * **Appname** : Enter a **Tag** to identify the Web Isolation platform.
     * **Facility** : Syslog facility name related to Web Isolation logs.
  4. Click **Create**.
  5. Go to **Reports > Log Forwarding**.
  6. Click **Edit**.
  7. Provide the following configuration details: 
     * **Activity Logs** : Select the newly added Bindplane server.
     * **Management Audit Logs** : Select the newly added Bindplane server.
     * **Gateway Audit Logs** : Select the newly added Bindplane server.
  8. Click **Update**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`action` | `security_result.summary` | Concatenated with `action_reason` to form the summary.  
`action_reason` | `security_result.summary` | Concatenated with `action` to form the summary.  
`content_action` | `security_result.action_details` | Direct mapping.  
`createdAt` | `metadata.event_timestamp` | Converted to timestamp using UNIX_MS format.  
`creationDate` | `metadata.event_timestamp` | Converted to timestamp using UNIX_MS format.  
`data.level` | `security_result.severity` | Mapped to INFORMATIONAL, LOW, or HIGH based on value.  
`data.properties.environment.str` | `intermediary.location.name` | Direct mapping.  
`data.properties.hostname.str` | `intermediary.hostname` | Direct mapping.  
`destination_ip` | `target.ip` | Direct mapping.  
`destination_ip_country_name` | `target.location.country_or_region` | Direct mapping.  
`device.current_risk_warnings` | `security_result.category_details` | Direct mapping.  
`device.identifier` | `target.asset.product_object_id` | Direct mapping.  
`device.model` | `hardware.model` | Direct mapping.  
`device.os_version` | `target.asset.platform_software.platform_version` | Direct mapping.  
`device.serial_number` | `hardware.serial_number` | Direct mapping.  
`device.udid` | `target.asset.asset_id` | Prefixed with "UDID:" before mapping.  
`device.user.email` | `target.user.email_addresses` | Direct mapping.  
`device.user.id` | `target.user.userid` | Direct mapping.  
`device.user.name` | `target.user.user_display_name` | Direct mapping.  
`device.user.organization.id` | `target.user.groupid` | Direct mapping.  
`device.user.organization.name` | `target.user.group_identifiers` | Direct mapping.  
`event` | `metadata.product_event_type` | Direct mapping.  
`event_type` | `metadata.event_type` | Set to "GENERIC_EVENT" or "NETWORK_HTTP" based on log data.  
`file_name` | `target.file.names` | Direct mapping.  
`file_type` | `about.labels`, `about.resource.attribute.labels` | Added as a label with key "file_type".  
`id` | `metadata.product_log_id` | Direct mapping.  
`isolation_session_id` | `network.parent_session_id` | Direct mapping.  
`level` | `security_result.severity` | Mapped to INFORMATIONAL, LOW, or HIGH based on value.  
`original_source_ip` | `principal.ip` | Direct mapping.  
`policy_version` | `security_result.rule_version` | Direct mapping.  
`properties.environment` | `intermediary.location.name` | Direct mapping.  
`properties.hostname` | `intermediary.hostname` | Direct mapping.  
`referer_url` | `network.http.referral_url` | Direct mapping.  
`request_method` | `network.http.method` | Direct mapping.  
`resource_response_headers.x-nauthilus-traceid` | `network.community_id` | Direct mapping.  
`response_status_code` | `network.http.response_code` | Direct mapping.  
`rule_id` | `security_result.rule_id` | Direct mapping.  
`rule_name_at_log_time` | `security_result.rule_name` | Direct mapping.  
`rule_type` | `security_result.rule_type` | Direct mapping.  
`service` | `principal.application` | Direct mapping.  
`session_id` | `network.session_id` | Direct mapping.  
`severity` | `security_result.severity` | Mapped to LOW, MEDIUM, or HIGH based on value.  
`source_ip` | `principal.ip` | Direct mapping.  
`source_ip_country_name` | `principal.location.country_or_region` | Direct mapping.  
`source_port` | `principal.port` | Direct mapping.  
`sub_type` | `security_result.summary` | Direct mapping.  
`target.asset.type` | `target.asset.type` | Set to "MOBILE" if `device.model` contains "ipad" or "iphone".  
`target.asset.platform_software.platform` | `target.asset.platform_software.platform` | Set to "MAC" if `device.model` contains "ipad" or "iphone".  
`timestamp` | `metadata.event_timestamp` | Parsed using `yyyy-MM-dd HH:mm:ss.SSS Z` format.  
`total_bytes` | `network.received_bytes` | Direct mapping if greater than 0.  
`traceId` | `metadata.product_log_id` | Direct mapping.  
`type` | `metadata.product_event_type` | Direct mapping.  
`url` | `target.url` | Direct mapping.  
`url_host` | `principal.hostname` | Direct mapping.  
`user_download_usage_bytes` | `network.received_bytes` | Direct mapping.  
`user_total_usage_bytes` | `about.labels`, `about.resource.attribute.labels` | Added as a label with key "user_total_usage_bytes".  
`user_upload_usage_bytes` | `network.sent_bytes` | Direct mapping.  
`username` | `principal.user.user_display_name` | Direct mapping.  
`vendor_name` | `metadata.vendor_name` | Set to "Broadcom Inc.".  
`product_name` | `metadata.product_name` | Set to "Symantec Web Isolation".  
`log_type` | `metadata.log_type` | Set to "SYMANTEC_WEB_ISOLATION".  
`sandbox` | `about.labels`, `about.resource.attribute.labels` | Added as a label with key "Sandbox" and value extracted from the URL.  
`utub` | `about.labels`, `about.resource.attribute.labels` | Added as a label with key "user_total_usage_bytes".  
`userid` | `target.user.userid` | Extracted from the URL.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-web-isolation-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
