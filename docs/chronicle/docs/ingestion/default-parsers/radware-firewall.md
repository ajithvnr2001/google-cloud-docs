---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/radware-firewall/
title: Collect Radware Web Application Firewall logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:16:19.393803+00:00
---

# Collect Radware Web Application Firewall logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/radware-firewall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Radware Web Application Firewall logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Radware Web Application Firewall logs to Google Security Operations using the Bindplane agent.

Radware Web Application Firewall (AppWall) is an application security solution that generates syslog messages for web attack detection, policy violations, bot mitigation events, and access control decisions. The parser extracts fields from syslog-formatted logs using grok patterns and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Radware AppWall or Vision Reporter
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Radware AppWall or Vision Reporter management console



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
            chronicle/radware_firewall:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: RADWARE_FIREWALL
                raw_log_field: body
        
        service:
            pipelines:
                logs/radware_firewall_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/radware_firewall
        




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
             




## Configure Radware AppWall to forward logs to Bindplane

You can configure syslog forwarding from AppWall standalone, integrated AppWall in Alteon, or Vision Reporter.

### Option 1: AppWall standalone using Vision Reporter

  1. Sign in to the **AppWall** management console.
  2. Go to **Configuration > Services > Vision Support > Vision Reporter**.
  3. Enable **Send events to Vision Reporter**.
  4. Set the **Server IP** to the Vision Reporter IP address.
  5. Set the **Port** (for example, `514`).
  6. Set the **Protocol** to **UDP**.
  7. Optional: Enable **Send replies** to forward response data.
  8. Click **Save**.



### Option 2: Integrated AppWall in Alteon

  1. Sign in to the **Alteon** management console.
  2. Go to **Configuration > Security > Web Security > Vision Reporter**.
  3. Enable the Vision Reporter integration.
  4. Set the **Server IP** to the Vision Reporter IP address.
  5. Set the **Port** (for example, `514`).
  6. Set the **Protocol** to **UDP**.
  7. Click **Save**.



### Option 3: Vision Reporter forwarding to Bindplane

  1. Sign in to the **Vision Reporter** management console.
  2. Go to **Configuration > SIEM & External Logging**.
  3. Click **\+ Add New SIEM Destination**.
  4. Provide the following configuration details: 
     * **Name** : Enter a name (for example, `Google SecOps Forwarder`).
     * **Log Export Type** : Select **Syslog RFC 5424**.
     * **Remote Syslog Server** : Enter the Bindplane agent IP address.
     * **Port** : Enter `514`.
     * **Protocol** : Select **UDP**.
  5. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`action` | `event.idm.read_only_udm.security_result.action` | If `action` is "drop", set to "BLOCK".  
`attack_desc` | `event.idm.read_only_udm.security_result.description` | Directly mapped.  
`attack_type` | `event.idm.read_only_udm.security_result.threat_name` | Directly mapped.  
`command` | `event.idm.read_only_udm.principal.process.command_line` | Directly mapped.  
`description` | `event.idm.read_only_udm.security_result.description` | Directly mapped if `attack_desc` is empty.  
`dst_ip` | `event.idm.read_only_udm.target.ip` | Directly mapped.  
`dst_port` | `event.idm.read_only_udm.target.port` | Directly mapped, converted to integer. Set to "MACHINE" if `username` is present and `command` is not. Copied from the `collection_time` field of the raw log. Defaults to "NETWORK_CONNECTION". Set to "GENERIC_EVENT" if either `src_ip` or `dst_ip` are missing. Set to "USER_LOGIN" if `username` is present and `command` is not present. Can be overridden by logic based on `attack_id`. Set to "RADWARE_FIREWALL". Mapped from the `product` field. Set to "Radware".  
`intermediary_ip` | `event.idm.read_only_udm.intermediary.ip` | Directly mapped.  
`obv_ip` | `event.idm.read_only_udm.observer.ip` | Directly mapped.  
`product` | `event.idm.read_only_udm.metadata.product_name` | Directly mapped.  
`protocol_number_src` | `event.idm.read_only_udm.network.ip_protocol` | Parsed using the `parse_ip_protocol.include` logic.  
`rule_id` | `event.idm.read_only_udm.security_result.rule_id` | Directly mapped. Derived based on the value of `attack_id`. Values include "ACL_VIOLATION", "NETWORK_DENIAL_OF_SERVICE", "NETWORK_SUSPICIOUS", "NETWORK_RECON".  
`src_ip` | `event.idm.read_only_udm.principal.ip` | Directly mapped.  
`src_port` | `event.idm.read_only_udm.principal.port` | Directly mapped, converted to integer.  
`ts` | `event.idm.read_only_udm.metadata.event_timestamp` | Parsed and converted to timestamp.  
`username` | `event.idm.read_only_udm.target.user.userid` | Directly mapped if `command` is not present.  
`username` | `event.idm.read_only_udm.principal.user.userid` | Directly mapped if `command` is present.  
`component` | `event.idm.read_only_udm.metadata.product_name` | Mapped from changelog  
`device_module` | `event.idm.read_only_udm.metadata.product_name` | Mapped from changelog  
`SVC` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`webappname` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`tunnel` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`proto` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`sport` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`threatcategory` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`sev` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`component` | `event.idm.read_only_udm.intermediary.application` | Mapped from changelog  
`id` | `event.idm.read_only_udm.observer.asset.asset_id` | Mapped from changelog  
`attackname` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`method` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`protocol` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`dhost` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`referer` | `event.idm.read_only_udm.network.http.referral_url` | Mapped from changelog  
`apath` | `event.idm.read_only_udm.principal.url` | Mapped from changelog  
`version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`refinecrc_field` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`refine_field` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Hosts` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`connection` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`access` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Origin` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sec_fetch` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`fetch_site` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`fetch_dest` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Referer` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`accept_encoding` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`req` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`directory` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`request_header` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`record_name` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`record_violation_reason` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`record_category` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`record_bot_category` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`record_totalVolume` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`record_totalPackets` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record_session_cookie` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record_headers` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`country_Code` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record_ID` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`record_tid` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`record_status` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`record_signature_pattern` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`record_site` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`record_url` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`record_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`record_sourceIP` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`record_ua` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`record_policy_id` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`record_destinationIP` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`record.time` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`app_protocol_output` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`app_protocol_src` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`community` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`login_result` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`enrichmentContainer_geoLocation_countryCode` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`contractId` | `event.idm.read_only_udm.target.labels` | Mapped from changelog  
`applicationId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`record.enrichmentContainer.owaspCategory2021` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`module` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`refinecrcvalue` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`host` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`msg_host` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`externalIp` | `event.idm.read_only_udm.observer.ip` | Mapped from changelog  
`http_version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tenant` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`role` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`targetModule` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`security` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`title` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`violationCategory` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`violationType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`webApp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cookie` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`lport` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`pragma` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cache_control` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`accept_charset` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`accept_language` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`accept_header` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`milli` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`devtype` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`act` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dir` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`attackrisk` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SVC` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`msg_title` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`min` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`policy` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`protection` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`useraction` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`severity_code` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tmodule` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`uriii` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vhosts` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`msg_parameter` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`msg_module` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`msg_error_number` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`device_module` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vhost` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vhost_field` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`request_uri` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`authenticated_role_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`authenticated_role_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_authentication` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sourceIp` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`lip_IP` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`extip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`dip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`sourcePort` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`violationDetails` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`subj` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`transId` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`evtid` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`applicationName` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`receivedTimeStamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`apath` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`req` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`engineversion` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`user_agent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`et` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`host_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`sip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`lip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`dhost` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`cmip` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`sourceIp` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`lport` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`dport` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`msg_description` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`msg_referer` | `event.idm.read_only_udm.network.http.referral_url` | Mapped from changelog  
`msg_suggestion` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`msg_authenticated_as` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`user_agent_val` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`log_level` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`radware_field_1` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`radware_field_2` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`radware_field_3` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`radware_field_4` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`radware_field_5` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`uuid` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`Type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`SourceIP` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`SourcePort` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`Host` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`WebUser` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`Role` | `event.idm.read_only_udm.principal.user.role_name` | Mapped from changelog  
`WebApp,` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`URI` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`TransID` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`http_method` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`ref_url` | `event.idm.read_only_udm.network.http.referral_url` | Mapped from changelog  
`AppPath,` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Object,` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ParamName,` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ParamType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog_ip` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`ServerName,` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`Description` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`Title` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`Attackname` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`RuleID` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`Threatcategory` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`Priority` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`IsPassive` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`x_forwarded_for_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`apikey` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`canary` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`client-version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`content-type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`client-request-id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`X-RDWR-APP-ID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`X-RDWR-IP` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`X-RDWR-PORT` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`X-RDWR-PORT-MM` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`X-RDWR-PORT-MM-ORIG-FE-PORT` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`hpgrequestid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`accept-language` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`purpose` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`upload-time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`site` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`headers` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`client-request-id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`client-id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`category` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`policy_id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`signature_pattern` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`status` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`violation_reason` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`user-agent` | `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
`User-Agent` | `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
`ID` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`destinationIP` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`sourceIP` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`country_code` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`application_name` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`session_cookie` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`tid` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`url` | `event.idm.read_only_udm.network.http.referral_url` | Mapped from changelog  
`ua` | `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
`sec_action` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`bot_category` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`externalIp` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`Referer` | `event.idm.read_only_udm.network.http.referral_url` | Mapped from changelog  
`referrer` | `event.idm.read_only_udm.network.http.referral_url` | Mapped from changelog  
`date` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`hostip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`hostip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`host` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`host` | `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`time` | `event.idm.read_only_udm.network.session_duration.seconds` | Mapped from changelog  
`et` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`total_bytes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`blocked_bytes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`passive_bytes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`clean_bytes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tunnel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tunnel_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`message_severity` | `event.idm.read_only_udm.security_result.severity_details` | Mapped from changelog  
`sent_bytes` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`rule_id` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`product` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`action` | `event.idm.read_only_udm.metadata.action_details` | Mapped from changelog  
`action` | `subevent.idm.read_only_udm.sec_result.action` | Mapped from changelog  
`application_id` | `subevent.idm.read_only_udm.additional.fields` | Mapped from changelog  
`accept_language` | `subevent.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cookie` | `subevent.idm.read_only_udm.additional.fields` | Mapped from changelog  
`request` | `subevent.idm.read_only_udm.additional.fields` | Mapped from changelog  
`received_timestamp` | `subevent.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tenant_name` | `subevent.idm.read_only_udm.additional.fields` | Mapped from changelog  
`x-forwarded-for` | `subevent.idm.read_only_udm.additional.fields` | Mapped from changelog  
`application_name` | `subevent.idm.read_only_udm.principal.application` | Mapped from changelog  
`country_code` | `subevent.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`destination_port` | `subevent.idm.read_only_udm.target.port` | Mapped from changelog  
`directory` | `subevent.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`http_bytes_in` | `subevent.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`http_bytes_out` | `subevent.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`http_method` | `subevent.idm.read_only_udm.network.http.method` | Mapped from changelog  
`protocol` | `subevent.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`response_code` | `subevent.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`source_port` | `subevent.idm.read_only_udm.principal.port` | Mapped from changelog  
`user_agent` | `subevent.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`applicationName` | `principal.application` | Mapped from changelog  
`action` | `security_result.action_details` | Mapped from changelog  
`appPath` | `principal.file.full_path` | Mapped from changelog  
`destinationIp` | `target.ip` | Mapped from changelog  
`destinationPort` | `target.port` | Mapped from changelog  
`directory` | `principal.process.file.full_path` | Mapped from changelog  
`enrichmentContainer.geoLocation.countryCode` | `principal.location.country_or_region` | Mapped from changelog  
`enrichmentContainer.contractId` | `additional.fields` | Mapped from changelog  
`applicationId` | `additional.fields` | Mapped from changelog  
`tenant` | `additional.fields` | Mapped from changelog  
`owaspCategory2021` | `additional.fields` | Mapped from changelog  
`externalIp` | `intermediary.ip` | Mapped from changelog  
`host` | `principal.hostname` | Mapped from changelog  
`method` | `network.http.method` | Mapped from changelog  
`passive` | `additional.fields` | Mapped from changelog  
`protocol` | `network.application_protocol` | Mapped from changelog  
`request` | `additional.fields` | Mapped from changelog  
`role` | `principal.user.role_name` | Mapped from changelog  
`security` | `additional.fields` | Mapped from changelog  
`sourceIp` | `` | Mapped from changelog  
`sourcePort` | `principal.port` | Mapped from changelog  
`targetModule` | `additional.fields` | Mapped from changelog  
`title` | `metadata.description` | Mapped from changelog  
`transId` | `additional.fields` | Mapped from changelog  
`URI` | `target.file.full_path` | Mapped from changelog  
`user` | `principal.user.role_description` | Mapped from changelog  
`vhost` | `security_result.detection_fields` | Mapped from changelog  
`violationCategory` | `additional.fields` | Mapped from changelog  
`violationDetails` | `security_result.summary` | Mapped from changelog  
`violationType` | `security_result.description` | Mapped from changelog  
`webApp` | `additional.fields` | Mapped from changelog  
`severity` | `security_result.severity` | Mapped from changelog  
`paramName` | `additional.fields` | Mapped from changelog  
`paramValue` | `additional.fields` | Mapped from changelog  
`paramType` | `additional.fields` | Mapped from changelog  
`receivedTimeStamp` | `metadata.event_timestamp` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/radware-firewall-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
