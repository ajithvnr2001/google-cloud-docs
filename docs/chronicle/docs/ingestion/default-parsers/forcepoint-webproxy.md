---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-webproxy/
title: Collect Forcepoint Web Security logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:21:43.198360+00:00
---

# Collect Forcepoint Web Security logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-webproxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Forcepoint Web Security logs

**Parser Version:** 12.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Forcepoint Web Security logs to Google Security Operations using the Bindplane agent.

Forcepoint Web Security is a web proxy and security gateway that generates syslog messages in CEF (Common Event Format) for web access, security events, authentication, and policy enforcement. The parser extracts fields from CEF and syslog-formatted logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and Forcepoint Web Security
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to Forcepoint Security Manager or appliance management interface



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

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

You can configure the Bindplane agent to receive syslog messages over TCP (recommended) or UDP.

### Locate the configuration file

  * **Linux:**
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

Replace the entire contents of `config.yaml` with the configuration for your chosen protocol:

  * **Option A: TCP Configuration (Recommended)**
        
        receivers:
            tcplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/forcepoint_webproxy:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: FORCEPOINT_WEBPROXY
                raw_log_field: body
        
        service:
            pipelines:
                logs/forcepoint_tcp_to_chronicle:
                    receivers:
                        - tcplog
                    exporters:
                        - chronicle/forcepoint_webproxy
        

  * **Option B: UDP Configuration**
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/forcepoint_webproxy:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: FORCEPOINT_WEBPROXY
                raw_log_field: body
        
        service:
            pipelines:
                logs/forcepoint_udp_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/forcepoint_webproxy
        




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
             




## Configure syslog forwarding on Forcepoint Web Security

Configure Forcepoint Web Security to forward logs to the Bindplane agent in CEF (Common Event Format) format.

### Using Forcepoint Security Manager

  1. Sign in to the **Forcepoint Security Manager** with administrative credentials.
  2. Go to **Settings > Logging**.
  3. In the left navigation, select **Log Servers**.
  4. Click **Add** to create a new log server configuration.
  5. Provide the following configuration details: 
     * **Server Type** : Select **Syslog Server** or **CEF Server**.
     * **Name** : Enter a descriptive name (for example, `Google Security Operations Bindplane CEF`).
     * **Host** : Enter the Bindplane agent IP address or hostname.
     * **Port** : Enter the Bindplane agent port number (for example, `514`).
     * **Protocol** : Select the protocol that matches your Bindplane configuration: 
       * Select **TCP** if you configured `tcplog` receiver in Bindplane (recommended).
       * Select **UDP** if you configured `udplog` receiver in Bindplane.
     * **Format** : Select **CEF** (Common Event Format).
     * **Facility** : Select **Local0** (or another available facility).
     * **Severity** : Select **Informational** (to capture all log levels).
  6. Under **Log Categories** or **Event Types** , select the events to forward: 
     * **Web Access Logs** (transaction logs)
     * **Security Events** (threat detections)
     * **Authentication Events** (user login/logout)
     * **System Events** (system and configuration changes)
     * Or select **All Events** to forward all available log types.
  7. Optional: Configure additional settings: 
     * **Batch Size** : Set to `1` for real-time forwarding or higher for batch processing.
     * **Message Format** : Ensure CEF format is selected.
     * **Include User Information** : Enable to include user identity in logs.
  8. Click **Test Connection** to verify connectivity to the Bindplane agent.
  9. Click **Save** to apply the configuration.
  10. Click **Deploy** to push the configuration to all Forcepoint Web Security gateways.



### Using Forcepoint Web Security Appliance (direct configuration)

If you are configuring directly on the appliance:

  1. Sign in to the **Forcepoint Web Security Appliance** management interface.
  2. Go to **System > Log Server**.
  3. Click **Add** or **Edit** to create or modify a log server.
  4. Provide the following configuration details: 
     * **Server Address** : Enter the Bindplane agent IP address.
     * **Port** : Enter `514` (or your custom port).
     * **Protocol** : Select **TCP** or **UDP** to match your Bindplane configuration.
     * **Format** : Select **CEF** or **Common Event Format**.
     * **Facility** : Select **Local0**.
  5. Under **Log Types** , select the logs to forward: 
     * **Access Logs**
     * **Security Logs**
     * **Admin Logs**
  6. Click **Apply** or **Save**.
  7. If using multiple appliances, repeat this configuration on each appliance.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`action` | `security_result.summary` | If `action_msg` is not empty, it is mapped to `security_result.summary`. Otherwise, if `action` is not empty, it is mapped to `security_result.summary`. Otherwise, if `act` is not empty, it is mapped to `security_result.summary`.  
`action_msg` | `security_result.summary` | If `action_msg` is not empty, it is mapped to `security_result.summary`. Otherwise, if `action` is not empty, it is mapped to `security_result.summary`. Otherwise, if `act` is not empty, it is mapped to `security_result.summary`.  
`app` | `target.application` | If `destinationServiceName` is not empty, it is mapped to `app_name`. Otherwise, if `app` is not empty and does not contain http or HTTP, it is mapped to `app_name`. Finally, `app_name` is mapped to `target.application`.  
`bytes_in` | `network.received_bytes` | If `in` is not empty, it is mapped to `bytes_in`. Finally, `bytes_in` is mapped to `network.received_bytes`.  
`bytes_out` | `network.sent_bytes` | If `out` is not empty, it is mapped to `bytes_out`. Finally, `bytes_out` is mapped to `network.sent_bytes`.  
`cat` | `security_result.category_details` | If `cat` is not empty, it is mapped to `category`. Finally, `category` is mapped to `security_result.category_details`.  
`category_no` | `security_result.detection_fields.value` | If `category_no` is not empty, it is mapped to `security_result.detection_fields.value` with key `Category Number`.  
`cn1` | `security_result.detection_fields.value` | If `cn1` is not empty, it is mapped to `security_result.detection_fields.value` with key `Disposition Number`.  
`ContentType` | `target.file.mime_type` | If `contentType` is not empty, it is mapped to `ContentType`. Finally, `ContentType` is mapped to `target.file.mime_type`.  
`cs1` | `target_role.description` | `cs1` is mapped to `target_role.description`.  
`cs2` | `security_result.category_details` | If `cs2` is not empty and not `0`, it is mapped to `security_result.category_details` with the prefix `Dynamic Category:`.  
`cs3` | `target.file.mime_type` | `cs3` is mapped to `target.file.mime_type`.  
`description` | `metadata.description` | If `description` is not empty, it is mapped to `metadata.description`.  
`destinationServiceName` | `target.application` | If `destinationServiceName` is not empty, it is mapped to `app_name`. Finally, `app_name` is mapped to `target.application`.  
`deviceFacility` | `metadata.product_event_type` | If `product_event` and `deviceFacility` are not empty, they are concatenated with `-` and mapped to `metadata.product_event_type`. Otherwise, `product_event` is mapped to `metadata.product_event_type`.  
`disposition` | `security_result.detection_fields.value` | If `disposition` is not empty, it is mapped to `security_result.detection_fields.value` with key `Disposition Number`.  
`dst` | `target.ip` | If `dst` is not empty and `dvchost` is empty, it is mapped to `dst_ip`. Finally, `dst_ip` is mapped to `target.ip`.  
`dst_host` | `target.hostname` | If `dst` is not empty and `dvchost` is empty, it is mapped to `dst_host`. Finally, `dst_host` is mapped to `target.hostname`.  
`dst_ip` | `target.ip` | If `dst` is not empty and `dvchost` is empty, it is mapped to `dst_ip`. Finally, `dst_ip` is mapped to `target.ip`.  
`dst_port` | `target.port` | If `dst` is not empty and `dvchost` is empty, it is mapped to `dst_port`. Finally, `dst_port` is mapped to `target.port`.  
`duration` | `network.session_duration.seconds` | If `duration` is not empty and not `0`, it is mapped to `network.session_duration.seconds`.  
`dvchost` | `intermediary.ip` | If `dvchost` is not empty, it is mapped to `int_ip`. Finally, `int_ip` is mapped to `intermediary.ip` if it is a valid IP address, otherwise it is mapped to `intermediary.hostname`.  
`file_path` | `target.file.full_path` | If `file_path` is not empty, it is mapped to `target.file.full_path`.  
`host` | `principal.ip` | If `host` is not empty, it is mapped to `src`. Finally, `src` is mapped to `principal.ip`.  
`http_method` | `network.http.method` | If `requestMethod` is not empty, it is mapped to `http_method`. Otherwise, if `method` is not empty, it is mapped to `http_method`. Finally, `http_method` is mapped to `network.http.method`.  
`http_proxy_status_code` | `network.http.response_code` | If `http_response` is empty or `0` or `-`, and `http_proxy_status_code` is not empty, it is mapped to `network.http.response_code`.  
`http_response` | `network.http.response_code` | If `http_response` is not empty and not `0` and not `-`, it is mapped to `network.http.response_code`.  
`http_user_agent` | `network.http.user_agent` | If `http_user_agent` is not empty and not `-` it is mapped to `network.http.user_agent`.  
`in` | `network.received_bytes` | If `in` is not empty, it is mapped to `bytes_in`. Finally, `bytes_in` is mapped to `network.received_bytes`.  
`int_host` | `intermediary.hostname` | If `int_ip` is not empty and `int_host` is not empty and different from `int_ip`, it is mapped to `intermediary.hostname`.  
`int_ip` | `intermediary.ip` | If `dvchost` is not empty, it is mapped to `int_ip`. Finally, `int_ip` is mapped to `intermediary.ip` if it is a valid IP address, otherwise it is mapped to `intermediary.hostname`.  
`level` | `target_role.name` | If `level` is not empty and `role` is empty, it is mapped to `role`. Finally, `role` is mapped to `target_role.name`.  
`log_level` | `security_result.severity` | If `severity` is `1` or `log_level` contains `info` or `message` contains `notice`, `security_result.severity` is set to `INFORMATIONAL`. If `severity` is `7`, `security_result.severity` is set to `HIGH`.  
`loginID` | `principal.user.userid` | If `loginID` is not empty, it is mapped to `user`. Finally, if `user` is not empty and not `-`, and does not contain `LDAP`, it is mapped to `principal.user.userid`.  
`method` | `network.http.method` | If `requestMethod` is not empty, it is mapped to `http_method`. Otherwise, if `method` is not empty, it is mapped to `http_method`. Finally, `http_method` is mapped to `network.http.method`.  
`NatRuleId` | `security_result.detection_fields.value` | If `NatRuleId` is not empty, it is mapped to `security_result.detection_fields.value` with key `NatRuleId`.  
`out` | `network.sent_bytes` | If `out` is not empty, it is mapped to `bytes_out`. Finally, `bytes_out` is mapped to `network.sent_bytes`.  
`pid` | `target.process.pid` | If `pid` is not empty, it is mapped to `target.process.pid`.  
`policy` | `target_role.description` | If `Policy` is not empty, it is mapped to `policy`. If `policy` is not empty and not `-`, it is mapped to `target_role.description`.  
`Policy` | `target_role.description` | If `Policy` is not empty, it is mapped to `policy`. If `policy` is not empty and not `-`, it is mapped to `target_role.description`.  
`product_event` | `metadata.product_event_type` | If `product` is not empty, it is mapped to `product_event`. If `product_event` and `deviceFacility` are not empty, they are concatenated with `-` and mapped to `metadata.product_event_type`. Otherwise, `product_event` is mapped to `metadata.product_event_type`.  
`proxyStatus-code` | `network.http.response_code` | If `http_response` is empty or `0` or `-`, and `http_proxy_status_code` is empty and `proxyStatus-code` is not empty, it is mapped to `network.http.response_code`.  
`refererUrl` | `network.http.referral_url` | If `refererUrl` is not empty and not `-`, it is mapped to `network.http.referral_url`.  
`requestClientApplication` | `network.http.user_agent` | If `requestMethod` is not empty, it is mapped to `http_user_agent`. Finally, `http_user_agent` is mapped to `network.http.user_agent`.  
`requestMethod` | `network.http.method` | If `requestMethod` is not empty, it is mapped to `http_method`. Finally, `http_method` is mapped to `network.http.method`.  
`role` | `target_role.name` | If `level` is not empty and `role` is empty, it is mapped to `role`. Finally, `role` is mapped to `target_role.name`.  
`RuleID` | `security_result.rule_id` | If `RuleID` is not empty, it is mapped to `security_result.rule_id`.  
`serverStatus-code` | `network.http.response_code` | If `http_response` is empty or `0` or `-`, and `http_proxy_status_code` is empty and `proxyStatus-code` is not empty, it is mapped to `network.http.response_code`.  
`severity` | `security_result.severity` | If `severity` is `1` or `log_level` contains `info` or `message` contains `notice`, `security_result.severity` is set to `INFORMATIONAL`. If `severity` is `7`, `security_result.severity` is set to `HIGH`.  
`spt` | `principal.port` | If `spt` is not empty, it is mapped to `src_port`. Finally, `src_port` is mapped to `principal.port`.  
`src` | `principal.ip` | If `src_host` is not empty, it is mapped to `source_ip_temp`. If `source_ip_temp` is a valid IP address and `src` is empty, it is mapped to `src`. If `host` is not empty, it is mapped to `src`. Finally, `src` is mapped to `principal.ip`.  
`src_host` | `principal.hostname` | If `src_host` is not empty, it is mapped to `source_ip_temp`. If `source_ip_temp` is not a valid IP address, it is mapped to `principal.hostname`. If `source_ip_temp` is a valid IP address and `src` is empty, it is mapped to `src`. Finally, `src` is mapped to `principal.ip`.  
`src_port` | `principal.port` | If `src_port` is not empty, it is mapped to `principal.port`.  
`suser` | `principal.user.userid` | If `loginID` is not empty, it is mapped to `user`. If `suser` is not empty, it is mapped to `user`. Finally, if `user` is not empty and not `-`, and does not contain `LDAP`, it is mapped to `principal.user.userid`.  
`url` | `target.url` | If `url` is not empty, it is mapped to `target.url`.  
`user` | `principal.user.userid` | If `loginID` is not empty, it is mapped to `user`. If `suser` is not empty, it is mapped to `user`. Otherwise, if `usrName` is not empty, it is mapped to `user`. Finally, if `user` is not empty and not `-`, and does not contain `LDAP`, it is mapped to `principal.user.userid`.  
`usrName` | `principal.user.userid` | If `loginID` is not empty, it is mapped to `user`. If `suser` is not empty, it is mapped to `user`. Otherwise, if `usrName` is not empty, it is mapped to `user`. Finally, if `user` is not empty and not `-`, and does not contain `LDAP`, it is mapped to `principal.user.userid`.  
`when` | `metadata.event_timestamp` | If `when` is not empty, it is parsed and mapped to `metadata.event_timestamp`.  
N/A | `metadata.log_type` | The value `FORCEPOINT_WEBPROXY` is hardcoded into `metadata.log_type`.  
N/A | `metadata.product_name` | The value `Forcepoint Webproxy` is hardcoded into `metadata.product_name`.  
N/A | `metadata.vendor_name` | The value `Forcepoint` is hardcoded into `metadata.vendor_name`.  
N/A | `network.application_protocol` | If `dst_port` is `80`, `network.application_protocol` is set to `HTTP`. If `dst_port` is `443`, `network.application_protocol` is set to `HTTPS`.  
N/A | `principal.user.group_identifiers` | If `user` is not empty and not `-` and contains `LDAP`, the OU part of the user string is extracted and mapped to `principal.user.group_identifiers`.  
N/A | `principal.user.user_display_name` | If `user` is not empty and not `-` and contains `LDAP`, the username part of the user string is extracted and mapped to `principal.user.user_display_name`.  
N/A | `security_result.action` | If `action_msg`, `action`, or `act` are not empty, `sec_action` is set to `ALLOW` or `BLOCK` based on their values. Finally, `sec_action` is mapped to `security_result.action`.  
N/A | `security_result.detection_fields.key` | The value `Disposition Number` is hardcoded into `security_result.detection_fields.key` when mapping `disposition` or `cn1`. The value `NatRuleId` is hardcoded into `security_result.detection_fields.key` when mapping `NatRuleId`. The value `Category Number` is hardcoded into `security_result.detection_fields.key` when mapping `category_no`.  
`reason` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`extension` | `event.idm.read_only_udm.target.process.file.mime_type` | Mapped from changelog  
`filetype` | `event.idm.read_only_udm.target.file.mime_type` | Mapped from changelog  
`method` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`received_bytes` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`sent_bytes` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`response_code` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`region` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`protocol` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`sec_description` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`version` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`city` | `event.idm.read_only_udm.principal.location.city` | Mapped from changelog  
`turl` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`userid` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`email` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`_action` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`descrip` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`status` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`appname` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`tip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`tip` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`pip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`pip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`p_ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`p_ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`log_timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`status` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`dhost` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`rt` | `event.timestamp` | Mapped from changelog  
`host-url` | `principal.url` | Mapped from changelog  
`cs-uri` | `target.url` | Mapped from changelog  
`cs-uri-query" , "time-taken" , "filter-category" , "cs-uri-path" , "cs-uri-extension" and "rs_content_type` | `additional.fields` | Mapped from changelog  
`cs-auth-group` | `principal.user_group_identifiers` | Mapped from changelog  
`cs-method` | `network.http.method` | Mapped from changelog  
`sc-status` | `response_code` | Mapped from changelog  
`s-action` | `security_result.detection_fields` | Mapped from changelog  
`srcport` | `principal.port` | Mapped from changelog  
`dstport` | `target.port` | Mapped from changelog  
`sc-bytes` | `network.received_bytes` | Mapped from changelog  
`cs-bytes` | `network.sent_bytes` | Mapped from changelog  
`cs_referer` | `network.http.referral_url` | Mapped from changelog  
`cs-host` | `target.hostname` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forcepoint-webproxy-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
