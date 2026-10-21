---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-edr/
title: Collect Symantec EDR logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:39:21.211613+00:00
---

# Collect Symantec EDR logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-edr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Symantec EDR logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Symantec EDR logs to Google Security Operations using the Bindplane agent.

Symantec Endpoint Detection and Response (EDR) is a threat detection solution that generates syslog messages for endpoint activity, process execution, network connections, file operations, registry modifications, and security incidents. The parser extracts fields from JSON-formatted and CEF-formatted logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Symantec EDR appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Symantec EDR web UI



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
            chronicle/symantec_edr:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: SYMANTEC_EDR
                raw_log_field: body
        
        service:
            pipelines:
                logs/symantec_edr_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/symantec_edr
        




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
             




## Configure syslog in Symantec EDR

  1. Sign in to the **Symantec EDR** web UI.
  2. In the EDR cloud console, go to **Environment > Settings**.
  3. Select an **appliance** and then click **Appliances**.
  4. In the EDR appliance console, click **Settings > Appliances**.
  5. Click **Edit Default Appliance**.
  6. Double-click the **device** in the **Appliances** list.
  7. In the Syslog section, clear **Use default** (if it is marked).
  8. Click **+Add Syslog Server**.
  9. Provide the following configuration details: 
     * **Host** : Enter the Bindplane agent IP address.
     * **Protocol** : Select the configured protocol (for example, **UDP**).
     * **Port** : Enter the Bindplane agent port number (for example, `514`).
  10. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`actor.cmd_line` | `principal.process.command_line` | The command line executed by the actor process.  
`actor.file.md5` | `principal.process.file.md5` | The MD5 hash of the actor's executable file.  
`actor.file.path` | `principal.process.file.full_path` | The full path to the actor's executable file.  
`actor.file.sha2` | `principal.process.file.sha256` | The SHA256 hash of the actor's executable file.  
`actor.pid` | `principal.process.pid` | The process ID of the actor.  
`actor.uid` | `principal.resource.id` | Unique identifier for the actor.  
`actor.user.name` | `principal.user.userid` | The username of the actor.  
`actor.user.sid` | `principal.user.windows_sid` | The Windows SID of the actor user.  
`attack.technique_name` | `security_result.threat_name` | The name of the MITRE ATT&CK technique.  
`attack.technique_uid` | `security_result.description` | Used withattack.technique_nameto populatesecurity_result.descriptionin the format: .  
`collector_device_ip` | `intermediary.ip` | The IP address of the collector device.  
`collector_device_name` | `intermediary.hostname` | The hostname of the collector device.  
`collector_name` | `intermediary.resource.name` | The name of the collector.  
`collector_uid` | `intermediary.resource.id` | The unique identifier of the collector.  
`connection.bytes_download` | `network.received_bytes` | The number of bytes downloaded in the connection.  
`connection.bytes_upload` | `network.sent_bytes` | The number of bytes uploaded in the connection.  
`connection.direction_id` | `network.direction` | The direction of the network connection (1 for INBOUND, 2 for OUTBOUND).  
`connection.dst_ip` | `target.ip` | The destination IP address of the connection.  
`connection.dst_port` | `target.port` | The destination port of the connection.  
`connection.src_ip` | `principal.ip` | The source IP address of the connection.  
`connection.src_name` | `principal.hostname` | The source hostname of the connection.  
`connection.src_port` | `principal.port` | The source port of the connection.  
`connection.url.host` | `target.hostname` | The hostname in the connection URL.  
`connection.url.scheme` | `network.application_protocol` | The scheme of the connection URL (e.g., HTTP, HTTPS).  
`connection.url.text` | `target.url` | The full connection URL.  
`data_source_url_domain` | `target.url` | The domain of the data source URL.  
`device_domain` | `principal.administrative_domain/target.administrative_domain` | The domain of the device. Mapped to principal or target based on logic related toconnection.direction_id.  
`device_ip` | `principal.ip/target.ip` | The IP address of the device. Mapped to principal or target based on logic related toconnection.direction_id.  
`device_name` | `principal.hostname/target.hostname` | The name of the device. Mapped to principal or target based on logic related toconnection.direction_id.  
`device_os_name` | `principal.platform_version/target.platform_version` | The operating system of the device. Mapped to principal or target based on logic related toconnection.direction_id.  
`device_uid` | `target.asset_id` | The unique identifier of the device, prefixed withDevice ID:.  
`directory.path` | `target.file.full_path` | The path of the directory.  
`domain_name` | `target.administrative_domain` | The name of the domain.  
`event_actor.file.path` | `target.process.file.full_path` | The path to the event actor's executable file.  
`event_actor.pid` | `target.process.pid` | The process ID of the event actor.  
`event_desc` | `metadata.description` | Description of the event.  
`externalIP` | `target.ip` | The external IP address.  
`file.md5` | `target.file.md5` | The MD5 hash of the file.  
`file.path` | `target.file.full_path` | The path to the file.  
`file.rep_prevalence_band` | `additional.fields.value.number_value` | The reputation prevalence band of the file, mapped with keyprevalence_score.  
`file.rep_score_band` | `additional.fields.value.number_value` | The reputation score band of the file, mapped with keyreputation_score.  
`file.sha2` | `target.file.sha256` | The SHA256 hash of the file.  
`file.size` | `target.file.size` | The size of the file.  
`internalHost` | `principal.hostname` | The internal hostname.  
`internalIP` | `principal.ip` | The internal IP address.  
`internal_port` | `principal.port` | The internal port.  
`kernel.name` | `target.resource.name` | The name of the kernel object. Thetarget.resource.typeis set toMUTEX.  
`message` | `metadata.description` | The log message.  
`module.md5` | `target.process.file.md5` | The MD5 hash of the module.  
`module.path` | `target.process.file.full_path` | The path to the module.  
`module.sha2` | `target.process.file.sha256` | The SHA256 hash of the module.  
`module.size` | `target.process.file.size` | The size of the module.  
`process.cmd_line` | `target.process.command_line` | The command line of the process.  
`process.file.md5` | `target.process.file.md5` | The MD5 hash of the process's executable file.  
`process.file.path` | `target.process.file.full_path` | The path to the process's executable file.  
`process.file.sha2` | `target.process.file.sha256` | The SHA256 hash of the process's executable file.  
`process.pid` | `target.process.pid` | The process ID.  
`process.uid` | `target.resource.id` | The unique identifier of the process.  
`process.user.name` | `target.user.userid` | The username associated with the process.  
`process.user.sid` | `target.user.windows_sid` | The Windows SID of the process user.  
`product_name` | `metadata.product_name` | The name of the product generating the log.  
`product_ver` | `metadata.product_version` | The version of the product generating the log.  
`reg_key.path` | `target.registry.registry_key` | The registry key path.  
`reg_value.data` | `target.registry.registry_value_data` | The registry value data.  
`reg_value.name` | `target.registry.registry_value_name` | The registry value name.  
`reg_value.path` | `target.registry.registry_key` | The registry key path for the value.  
`security_result.severity` | `security_result.severity` | The severity of the security result. Translated from numeric value to UDM enum (e.g., 1 to LOW, 5 to MEDIUM, 10 to LOW, 15 to LOW).  
`session.id` | `network.session_id` | The session ID.  
`session.user.name` | `target.user.userid` | The username associated with the session.  
`sid` | `principal.user.userid` | The security identifier (SID).  
`status_detail` | `security_result.summary` | Additional details about the status.  
`type_id` | `metadata.product_event_type` | The event type ID.  
`user_agent_ip` | `target.ip` | The IP address of the user agent.  
`user_name` | `principal.user.userid/target.user.user_display_name` | The username. Mapped to principal or target based on logic related to CEF or JSON parsing.  
`user_uid` | `target.user.userid` | The unique identifier of the user.  
`uuid` | `metadata.product_log_id` | The UUID of the event.  
`event.idm.read_only_udm.metadata.event_timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | The timestamp of the event. Derived fromlog_timeor CEFdevice_time.  
`event.idm.read_only_udm.metadata.log_type` | `event.idm.read_only_udm.metadata.log_type` | The type of log. Hardcoded toSYMANTEC_EDR.  
`event.idm.read_only_udm.metadata.vendor_name` | `event.idm.read_only_udm.metadata.vendor_name` | The name of the vendor. Hardcoded toSymantec.  
`event.idm.read_only_udm.extensions.auth.type` | `event.idm.read_only_udm.extensions.auth.type` | The authentication type. Set toMACHINEfor login and logout events.  
`security_result.action` | `security_result.action` | The action taken as a result of the security event. Set toALLOWfor successful logins and logouts.  
`log_time` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`user_name` | `event.idm.read_only_udm.target.user.user_display_name` | Mapped from changelog  
`severity_id` | `event.idm.read_only_udm.security_result.severity_details` | Mapped from changelog  
`risk_ref_value` | `event.idm.read_only_udm.security_result.risk_score` | Mapped from changelog  
`attacks.technique_uid` | `event.idm.read_only_udm.security_result.attack_details.techniques` | Mapped from changelog  
`attacks.technique_uid` | `event.idm.read_only_udm.security_result.attack_details.tactics` | Mapped from changelog  
`event_actor.file.normalized_path` | `event.idm.read_only_udm.principal.file.full_path` | Mapped from changelog  
`event_actor.file.name` | `event.idm.read_only_udm.principal.process.file.names` | Mapped from changelog  
`user_sid` | `event.idm.read_only_udm.target.user.windows_sid` | Mapped from changelog  
`event_actor.file.signature_company_name` | `event.idm.read_only_udm.principal.group.group_display_name` | Mapped from changelog  
`event_actor.app_name` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`event_actor.integrity_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_actor_integrity_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_actor.signature_level_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_actor_signature_level_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_actor.start_time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_actor_start_time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_actor.file.modified` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_actor_file_modified` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`operation` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_actor.file.signature_value_ids` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`signature_value_id_0` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`signature_value_id_1` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`analysis` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`amsi_data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`log_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`scan_uid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`enriched_data.category_id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`category_id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-edr-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
