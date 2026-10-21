---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/airlock-digital/
title: Collect Airlock Digital Application Allowlisting logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:29.059669+00:00
---

# Collect Airlock Digital Application Allowlisting logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/airlock-digital/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Airlock Digital Application Allowlisting logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Airlock Digital Application Allowlisting logs to Google Security Operations using the Bindplane agent.

Airlock Digital is an application allowlisting and execution control platform that enforces a deny-by-default security model on endpoints, ensuring only trusted applications, scripts, and processes are permitted to execute. The platform provides granular policy control at the file, path, publisher, and parent process level, along with comprehensive audit trails for compliance and threat management. Airlock Digital generates logs for execution events, blocked executions, policy changes, and administrative actions, which can be forwarded to SIEM solutions using syslog, CEF, JSON, or HTTP(S).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Airlock Digital Server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * An Airlock Digital Server (on-premise or cloud) with administrator access
  * Airlock Digital v4.7 or later (for syslog external logging support)



## Get a Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where Bindplane will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



## Get a Google SecOps customer ID

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
            tcplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/airlock_digital:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: AIRLOCK_DIGITAL
                raw_log_field: body
        
        service:
            pipelines:
                logs/airlock_digital:
                    receivers:
                        - tcplog
                    exporters:
                        - chronicle/airlock_digital
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `tcplog`: The receiver type based on protocol: 
      * `udplog` for UDP syslog
      * `tcplog` for TCP syslog
      * `syslog` for RFC 3164/5424 syslog
    * `0.0.0.0`: IP address to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Specific IP address to listen on one interface
    * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)
  * **Exporter configuration:**

    * `<customer_id>`: Customer ID from the earlier step
    * `malachiteingestion-pa.googleapis.com`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * Adjust the `creds_file_path` depending on the platform: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`



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
             




## Configure Airlock Digital external logging

Configure the Airlock Digital Server to forward logs using syslog to the Bindplane agent. Airlock Digital supports multiple external logging formats, including Generic Syslog, CEF, JSON, HTTP(S), and GELF.

  1. Sign in to the **Airlock Digital Server Console** with an administrator account.
  2. Go to **System > External Logging**.
  3. Click **Add** to create a new external logging configuration.
  4. In the **Logging Type** dropdown, select **Generic Syslog**.

**Note:** Generic Syslog is recommended for Google SecOps ingestion. The Google SecOps parser for Airlock Digital supports both syslog and JSON log formats.
  5. Provide the following configuration details:

     * **Server Address** : Enter the IP address or hostname of the Bindplane agent host (for example, `192.168.1.100`)
     * **Port** : Enter `514` (or the port configured in the Bindplane agent)
     * **Protocol** : Select **TCP**
**Note:** Use TCP to ensure reliable log delivery. If you select UDP, update the Bindplane agent receiver to `udplog` accordingly.
  6. In the **Log Categories** section, select the event types to forward:

     * Execution Events (blocked and allowed executions)
     * Policy Changes
     * Administrative Actions
     * Agent Events
     * Server Activity
**Note:** For comprehensive security monitoring, select all available log categories.
  7. Click **Save** to apply the external logging configuration.

  8. Verify that logs are being forwarded by checking the Bindplane agent logs or reviewing the **External Logging** status in the Airlock Digital Server Console.

**Note:** If the Airlock Digital Server cannot connect to the syslog destination over TCP, the service will queue log events and retry. Ensure network connectivity and firewall rules permit traffic from the Airlock Digital Server to the Bindplane agent on the configured port.



For more information about Airlock Digital SIEM integrations, see the [Airlock Digital SIEM integration page](https://www.airlockdigital.com/airlock-digital-siem).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`event_type` | `extensions.auth.type` | Mapped: `ServerActivityMessage` → `SSO`  
`product_event_type` | `extensions.auth.type` | Mapped: `(?i)Login` → `SSO`  
`task` | `extensions.auth.type` | Mapped: `Login` → `AUTHTYPE_UNSPECIFIED`, `Logout` → `AUTHTYPE_UNSPECIFIED`  
`intermediary_hostname` | `intermediary.hostname` | Directly mapped  
`description` | `metadata.description` | Directly mapped  
`metadata_description` | `metadata.description` | Directly mapped  
`event_timestamp` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss.SSS`  
`ingestion_time` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`event_type` | `metadata.event_type` | Mapped: `FileActivityMessage` → `STATUS_UPDATE`, `ServerActivityMessage` → `USER_LOGIN`, `Se...  
`has_principal` | `metadata.event_type` | Mapped: `true` → `FILE_UNCATEGORIZED`  
`product_event_type` | `metadata.event_type` | Mapped: `(?i)Login` → `USER_LOGIN`  
`task` | `metadata.event_type` | Mapped: `Login` → `USER_LOGIN`, `Logout` → `USER_LOGOUT`  
`event_type` | `metadata.product_event_type` | Directly mapped  
`product_event_type` | `metadata.product_event_type` | Directly mapped  
`checkpoint` | `metadata.product_log_id` | Directly mapped  
`browser` | `network.http.user_agent` | Directly mapped  
`netdomain` | `principal.administrative_domain` | Directly mapped  
`asset_category` | `principal.asset.category` | Directly mapped  
`hostname` | `principal.asset.hostname` | Directly mapped  
`srcip` | `principal.asset.ip` | Merged  
`software` | `principal.asset.software` | Merged  
`hostname` | `principal.hostname` | Directly mapped  
`principal_hostname` | `principal.hostname` | Directly mapped  
`srcip` | `principal.ip` | Merged  
`process_file_path` | `principal.process.file.full_path` | Directly mapped  
`file_md5` | `principal.process.file.md5` | Directly mapped  
`process_file_name` | `principal.process.file.names` | Merged  
`file_sha256` | `principal.process.file.sha256` | Directly mapped  
`parent_process_file` | `principal.process.parent_process.file.full_path` | Directly mapped  
`principal_user_userid` | `principal.user.userid` | Directly mapped  
`description` | `security_result.action` | Mapped: `Invalid login attempt` → `security_result_action`  
`metadata_description` | `security_result.action` | Mapped: `logged in success` → `security_result_action`  
`security_result_action` | `security_result.action` | Merged  
`file_sha128_label` | `security_result.detection_fields` | Merged  
`policyname_label` | `security_result.detection_fields` | Merged  
`policyver_label` | `security_result.detection_fields` | Merged  
`ppolicy_label` | `security_result.detection_fields` | Merged  
`sha128_label` | `security_result.detection_fields` | Merged  
`sha384_label` | `security_result.detection_fields` | Merged  
`sha512_label` | `security_result.detection_fields` | Merged  
`type_label` | `security_result.detection_fields` | Merged  
`source_file` | `src.file.full_path` | Directly mapped  
`source_file_name` | `src.file.full_path` | Directly mapped  
`filename` | `target.file.full_path` | Directly mapped  
`sha256` | `target.file.sha256` | Directly mapped  
`commandline` | `target.process.command_line` | Directly mapped  
`filename` | `target.process.file.full_path` | Directly mapped  
`InstanceURL` | `target.url` | Directly mapped  
`principal_user_userid` | `target.user.userid` | Directly mapped  
`user` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `USER_LOGIN`  
N/A | `metadata.product_name` | Constant: `Airlock Digital`  
N/A | `metadata.vendor_name` | Constant: `Airlock Digital`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/airlock-digital-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
