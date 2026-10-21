---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hp-procurve/
title: Collect HP ProCurve logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:09:59.327005+00:00
---

# Collect HP ProCurve logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hp-procurve/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect HP ProCurve logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest HP ProCurve logs to Google Security Operations using the Bindplane agent.

HP ProCurve is a line of network switches that generate syslog messages for authentication events, configuration changes, network activity, and system events. The parser extracts fields from syslog-formatted logs, parses key-value pairs and descriptions, and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the HP ProCurve switch
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * SSH access to the HP ProCurve switch



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

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

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
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/hp_procurve:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: HP_PROCURVE
            raw_log_field: body
        
        service:
          pipelines:
            logs/hp_procurve_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/hp_procurve
        




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
          chronicle/hp_procurve:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: HP_PROCURVE
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
             




## Configure syslog on HP ProCurve switch

  1. Sign in to the **HP ProCurve switch** with SSH.
  2. Verify the switch interface by using the following command:
         
         show ip int br
         

  3. Enable config mode on the switch using the following command:
         
         console# conf t
         

  4. Configure the switch to send logs using the following commands:
         
         logging host <bindplane-server-ip> transport <udp/tcp> port <port-number>
         logging facility syslog
         logging trap informational
         logging buffer 65536
         logging origin-id hostname
         logging source-interface <interface>
         

     * Replace `<bindplane-server-ip>` with the Bindplane agent IP address.
     * Replace `<port-number>` with the configured port (default: `514`).
     * Replace `<interface>` with the source interface for syslog traffic.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
AAAScheme | read_only_udm.security_result.detection_fields.value | Value extracted from `descrip` field if the key is `AAAScheme`  
AAAType | read_only_udm.security_result.detection_fields.value | Value extracted from `descrip` field if the key is `AAAType`  
Chassis ID | read_only_udm.security_result.detection_fields.value | Value extracted from `description` field if the key is `Chassis ID`  
Command is | read_only_udm.security_result.detection_fields.value | Text after `Command is` in the `commandInfo` field  
CommandSource | read_only_udm.security_result.detection_fields.value | Value extracted from `descrip` field if the key is `CommandSource`  
Config-Method | read_only_udm.additional.fields.value.string_value | If the field exists in the log, it's placed in the additional fields as `config_method`  
ConfigDestination | read_only_udm.security_result.detection_fields.value | Value extracted from `descrip` field if the key is `ConfigDestination`  
ConfigSource | read_only_udm.security_result.detection_fields.value | Value extracted from `descrip` field if the key is `ConfigSource`  
Device-Name | read_only_udm.principal.hostname | If the field exists in the log, it's mapped to principal hostname and asset hostname  
Event-ID | read_only_udm.additional.fields.value.string_value | If the field exists in the log, it's placed in the additional fields as `event_id`  
EventIndex | read_only_udm.security_result.detection_fields.value | Value extracted from `descrip` field if the key is `EventIndex`  
IfIndex | read_only_udm.security_result.detection_fields.value | Value extracted from `description` field if the key is `IfIndex`  
IP: %{IP:IPAddr} | read_only_udm.target.ip, read_only_udm.target.asset.ip | IP address extracted from the `desc` field and mapped to target IP and target asset IP  
IPAddr | read_only_udm.target.ip, read_only_udm.target.asset.ip | If the field exists in the log, it's mapped to target IP and target asset IP  
Notice-Type | read_only_udm.additional.fields.value.string_value | If the field exists in the log, it's placed in the additional fields as `notice_type`  
Port ID | read_only_udm.security_result.detection_fields.value | Value extracted from `description` field if the key is `Port ID`  
Remote-IP-Address | read_only_udm.additional.fields.value.string_value | If the field exists in the log, it's placed in the additional fields as `remote_ip_address`  
Service | read_only_udm.security_result.detection_fields.value | Value extracted from `descrip` field if the key is `Service`  
Task | read_only_udm.security_result.detection_fields.value | Value extracted from `descrip` field if the key is `Task`  
User | read_only_udm.principal.user.userid | If the field exists in the log, it's mapped to principal user ID  
User-Name | read_only_udm.principal.user.userid | If the field exists in the log, it's mapped to principal user ID  
UserName | read_only_udm.principal.user.userid | If the field exists in the log, it's mapped to principal user ID  
UserService | read_only_udm.security_result.detection_fields.value | Value extracted from `desc` field if the key is `UserService`  
collection_time.seconds | read_only_udm.metadata.event_timestamp.seconds | Seconds part of the event timestamp  
data |  | This field contains the raw log message and is parsed to extract other fields. It's not mapped to the UDM.  
desc | read_only_udm.security_result.description | Description extracted from the log message  
descrip |  | Description extracted from the `desc` field, further parsed for key-value pairs. It's not mapped to the UDM.  
description | read_only_udm.security_result.description | If the field exists in the log, it's mapped to the security result description  
descript | read_only_udm.metadata.description | If the field exists in the log, it's mapped to the metadata description  
event_id | read_only_udm.additional.fields.value.string_value | If the field exists in the log, it's placed in the additional fields as `event_id`  
eventId | read_only_udm.metadata.product_event_type | Event ID extracted from the log message  
hostname | read_only_udm.principal.hostname, read_only_udm.principal.asset.hostname | Hostname extracted from the log message and mapped to principal hostname and asset hostname  
inter_ip | read_only_udm.additional.fields.value.string_value, read_only_udm.intermediary.ip | If the field exists in the log and is a valid IP, it's mapped to intermediary IP. Otherwise, it's placed in the additional fields as `inter_ip`  
notice_type | read_only_udm.additional.fields.value.string_value | If the field exists in the log, it's placed in the additional fields as `notice_type`  
pid | read_only_udm.principal.process.pid | If the field exists in the log, it's mapped to principal process PID  
program |  | Program information extracted from the log message, further parsed to extract module, severity, and action. It's not mapped to the UDM.  
proto | read_only_udm.network.application_protocol, read_only_udm.additional.fields.value.string_value | Protocol extracted from the log message. If it matches known protocols, it's mapped to application protocol. Otherwise, it's placed in the additional fields as `Application Protocol`  
remote_ip_address | read_only_udm.principal.ip, read_only_udm.principal.asset.ip, read_only_udm.additional.fields.value.string_value | If the field exists in the log and is a valid IP, it's mapped to principal IP and principal asset IP. Otherwise, it's placed in the additional fields as `remote_ip_address`  
severity | read_only_udm.security_result.severity, read_only_udm.security_result.severity_details | Severity extracted from the `program` field after splitting by `/`. It's mapped to UDM severity levels and also stored as raw severity details  
src_ip | read_only_udm.principal.ip, read_only_udm.principal.asset.ip | Source IP extracted from the log message and mapped to principal IP and principal asset IP  
status | read_only_udm.additional.fields.value.string_value | If the field exists in the log, it's placed in the additional fields as `status`  
targetHostname | read_only_udm.target.hostname, read_only_udm.target.asset.ip | If the field exists in the log, it's mapped to target hostname and target asset IP  
target_ip | read_only_udm.target.ip, read_only_udm.target.asset.ip | Target IP extracted from the log message and mapped to target IP and target asset IP  
timestamp | read_only_udm.metadata.event_timestamp.seconds | Timestamp extracted from the log message and converted to event timestamp  
timestamp.seconds | read_only_udm.metadata.event_timestamp.seconds | Seconds part of the event timestamp  
username | read_only_udm.principal.user.userid | If the field exists in the log, it's mapped to principal user ID  
| read_only_udm.metadata.event_type | Determined based on a combination of fields and logic:   
\- `NETWORK_CONNECTION`: if `has_principal` and `has_target` are true.   
\- `USER_LOGOUT`: if `action` is `WEBOPT_LOGOUT`, `LOGOUT`, or `SHELL_LOGOUT`.   
\- `USER_LOGIN`: if `action` is `LOGIN` or `WEBOPT_LOGIN_SUC`.   
\- `STATUS_UPDATE`: if `action` is not empty or `src_ip`/`hostname` are not empty.   
\- `USER_UNCATEGORIZED`: if `has_user` is true.   
\- `GENERIC_EVENT`: if none of the these conditions are met.  
| read_only_udm.metadata.product_name | Hardcoded to `Procurve`  
| read_only_udm.metadata.vendor_name | Hardcoded to `HP`  
| read_only_udm.extensions.auth.type | Set to `MACHINE` if `event_type` is `USER_LOGOUT` or `USER_LOGIN`  
`ts` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`prin_app` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`DHCP` | `network.application_protocol` | Mapped from changelog  
`prin_port` | `principal.port` | Mapped from changelog  
`status", "config_method", "event_id", and "notice_type` | `additional.fields` | Mapped from changelog  
`target_mac` | `target.mac` | Mapped from changelog  
`msg` | `metadata.description` | Mapped from changelog  
`src_mac` | `principal.mac` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hp-procurve-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
