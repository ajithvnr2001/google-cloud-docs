---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/eset-av/
title: Collect ESET AV logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:20:40.918785+00:00
---

# Collect ESET AV logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/eset-av/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ESET AV logs

**Parser Version:** 6.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest ESET antivirus logs to Google Security Operations using the Bindplane agent.

ESET is an endpoint security solution that generates syslog messages for threat detections, firewall events, HIPS alerts, and audit actions. The parser extracts key-value pairs from JSON-formatted syslog and maps them to the Unified Data Model (UDM).

## Before you begin

  * Make sure you have the following prerequisites:

  * A Google SecOps instance

  * Windows Server 2016 or later, or Linux host with `systemd`

  * Network connectivity between the Bindplane agent and the ESET PROTECT server

  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements

  * Privileged access to ESET PROTECT console (on-premises or Cloud)




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
          chronicle/eset_av:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: ESET_AV
            raw_log_field: body
        
        service:
          pipelines:
            logs/eset_av_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/eset_av
        




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
          chronicle/eset_av:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: ESET_AV
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
             




## Configure syslog on ESET PROTECT on-premises

  1. Sign in to the **ESET PROTECT** web console.
  2. Click **More > Settings > Advanced Settings > Syslog Server**.
  3. Toggle the **Enable Syslog** switch to enable syslog.
  4. Provide the following configuration details: 
     * **Host** : Enter the Bindplane agent IP address.
     * **Port** : Enter `514`.
     * **Format** : Select **Syslog**.
     * **Transport** : Select **UDP**.
     * **Trace log verbosity** : Select **Informational**.
     * **Export logs to Syslog** : Set to **Enable**.
     * **Exported logs format** : Select **JSON**.
  5. Click **Save**.



## Configure syslog on ESET PROTECT Cloud

  1. Sign in to the **ESET PROTECT Cloud** console.
  2. Click **More > Settings > Syslog Server**.
  3. Toggle the **Enable Syslog** switch to enable syslog.
  4. Provide the following configuration details: 
     * **Format of payload** : Select **JSON**.
     * **Format of envelope** : Select **Syslog**.
     * **Minimum log Level** : Select **Informational**.
     * **Event types to log** : Select **All** (or specific types as needed).
     * **Destination IP** : Enter the Bindplane agent IP address.
     * **Port** : Enter `514`.
  5. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
account | principal.administrative_domain | Extracted from the `account` field using grok pattern `%{DATA:admin_domain}\\\\%{WORD:user_id}`.  
account | principal.user.userid | Extracted from the `account` field using grok pattern `%{DATA:admin_domain}\\\\%{WORD:user_id}`.  
action | security_result.action | If `action` is `Block` (case-insensitive), set to `BLOCK`. If `action` is `Start` (case-insensitive), set to `ALLOW`.  
action_taken | security_result.action_details | Directly mapped from the `action_taken` field.  
computer_severity_score | security_result.detection_fields | A key-value pair is created with the key `computer_severity_score` and the value from the `computer_severity_score` field. This pair is appended to the `security_result.detection_fields` array.  
detail | security_result.description | Directly mapped from the `detail` field.  
domain | principal.domain.name | Directly mapped from the `domain` field.  
eialarmid | security_result.detection_fields | A key-value pair is created with the key `eialarmid` and the value from the `eialarmid` field. This pair is appended to the `security_result.detection_fields` array.  
eiconsolelink | principal.url | Directly mapped from the `eiconsolelink` field.  
event | metadata.description | Renamed from `event` to `event_desc` and mapped to `metadata.description`.  
event_type | metadata.product_event_type | Directly mapped from the `event_type` field.  
group_name | principal.group.group_display_name | Directly mapped from the `group_name` field.  
hash | principal.file.sha1 | Converted to lowercase. If the lowercase value matches the SHA-1 regex, mapped to `principal.file.sha1`.  
hash | principal.resource.attribute.labels | A key-value pair is created with the key `hash` and the value from the `hash` field. This pair is appended to the `principal.resource.attribute.labels` array.  
hostname | principal.asset.hostname | Directly mapped from the `hostname` field.  
hostname | principal.hostname | Directly mapped from the `hostname` field.  
inbound | network.direction | If true, set to `INBOUND`. If false, set to `OUTBOUND`.  
ipv4 | target.asset.ip | Directly mapped from the `ipv4` field if `target_address` is empty.  
ipv4 | target.ip | Directly mapped from the `ipv4` field if `target_address` is empty.  
json_data |  | Parsed as JSON to extract various fields.  
message |  | Parsed using grok to extract timestamp, host, and json_data.  
need_restart | additional.fields | A key-value pair is created with the key `need_restart` and the value from the `need_restart` field (converted to string). This pair is appended to the `additional.fields` array.  
os_name | principal.platform | If contains `Window` or `window` (case-insensitive), set to `WINDOWS`. If contains `Linux` or `linux` (case-insensitive), set to `LINUX`. If contains `Mac` or `mac` (case-insensitive), set to `MAC`.  
os_name | principal.platform_version | Directly mapped from the `os_name` field.  
process_name | principal.process.file.full_path | Directly mapped from the `process_name` field. If empty, takes the value of `processname`.  
processname | principal.process.file.full_path | If `process_name` is empty, mapped to `process_name`.  
protocol | network.ip_protocol | Converted to uppercase. If the uppercase value matches known protocols (TCP, UDP, ICMP, etc.), mapped to `network.ip_protocol`.  
result | security_result.summary | Directly mapped from the `result` field.  
rulename | security_result.rule_name | Directly mapped from the `rulename` field.  
scan_id | security_result.detection_fields | A key-value pair is created with the key `scan_id` and the value from the `scan_id` field. This pair is appended to the `security_result.detection_fields` array.  
scanner_id | security_result.detection_fields | A key-value pair is created with the key `scanner_id` and the value from the `scanner_id` field. This pair is appended to the `security_result.detection_fields` array.  
severity | security_result.severity | If contains `Warn` or `warn` (case-insensitive), set to `HIGH`. If contains `Info` or `info` (case-insensitive), set to `LOW`.  
severity_score | security_result.detection_fields | A key-value pair is created with the key `severity_score` and the value from the `severity_score` field. This pair is appended to the `security_result.detection_fields` array.  
source_address | principal.asset.ip | Directly mapped from the `source_address` field.  
source_address | principal.ip | Directly mapped from the `source_address` field.  
source_port | principal.port | Converted to string and then to integer. Mapped to `principal.port`.  
source_uuid | metadata.product_log_id | Directly mapped from the `source_uuid` field.  
target |  | Renamed to `target1`.  
target_address | target.asset.ip | Directly mapped from the `target_address` field.  
target_address | target.ip | Directly mapped from the `target_address` field.  
target_port | target.port | Converted to string and then to integer. Mapped to `target.port`.  
threat_handled | security_result.detection_fields | A key-value pair is created with the key `threat_handled` and the value from the `threat_handled` field (converted to string). This pair is appended to the `security_result.detection_fields` array.  
threat_name | security_result.threat_name | Directly mapped from the `threat_name` field.  
threat_type | security_result.threat_id | Directly mapped from the `threat_type` field.  
time | metadata.event_timestamp | Used to populate `metadata.event_timestamp`.  
username | principal.user.userid | Directly mapped from the `username` field if `user_id` and `user` are empty.  
user | principal.user.userid | Directly mapped from the `user` field if `user_id` is empty.  
| metadata.event_type | If `source_address` and `target_address` are not empty, set to `NETWORK_CONNECTION`. Else if `has_user` is true, set to `USER_UNCATEGORIZED`. Else if `has_principal` is true, set to `STATUS_UPDATE`. Otherwise, set to `GENERIC_EVENT`.  
| metadata.log_type | Set to `ESET_AV`.  
| metadata.product_name | Set to `ESET_AV`.  
| metadata.vendor_name | Set to `ESET_AV`.  
| intermediary.hostname | The value of this field is taken from the `host` field extracted from the log message.  
| principal.user.userid | If the field `account` is not empty, the parser extracts the user ID from the `account` field using a grok pattern. Otherwise it checks if the field `user` is not empty, if so it takes its value. If both `account` and `user` are empty, it checks if the field `username` is not empty, if so it takes its value.  
`timestamp` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`event_id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`process_pid` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`desc` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`occurred` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`threatHandled` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`actionTaken` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`threatName` | `event.idm.read_only_udm.security_result.threat_name` | Mapped from changelog  
`threatType` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`target` | `target.resource.attribute.labels` | Mapped from changelog  
`object_uri` | `target.url` | Mapped from changelog  
`severity` | `security_result.severity_details` | Mapped from changelog  
`threat_flags` | `security_result.detection_fields` | Mapped from changelog  
`category` | `security_result.category_details` | Mapped from changelog  
`object_type" and "engine_version` | `principal.resource.attribute.labels` | Mapped from changelog  
`circumstances` | `security_result.description` | Mapped from changelog  
`security_result_action` | `BLOCK` | Mapped from changelog  
`security_result_action` | `ALLOW` | Mapped from changelog  
`scan_id", "scanner_id", and "threat_handled` | `security_result.detection_fields` | Mapped from changelog  
`group_name` | `principal.group_display_name` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/eset-av-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
