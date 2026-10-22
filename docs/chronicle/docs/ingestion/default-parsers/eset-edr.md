---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/eset-edr/
title: Collect ESET EDR logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:25.327172+00:00
---

# Collect ESET EDR logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/eset-edr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ESET EDR logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest ESET EDR logs to Google Security Operations using the Bindplane agent.

ESET Endpoint Detection and Response (EDR) is a security solution that generates syslog messages for threat detections, firewall events, process activity, and security audit actions. The parser extracts fields from JSON-formatted syslog and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

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
          chronicle/eset_edr:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: ESET_EDR
            raw_log_field: body
        
        service:
          pipelines:
            logs/eset_edr_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/eset_edr
        




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
          chronicle/eset_edr:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: ESET_EDR
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
action | event1.idm.read_only_udm.security_result.action | Conditionally set to `BLOCK` if the value is `Blocked`.  
actionTaken | event2.idm.read_only_udm.metadata.event_type | Conditionally set to `SCAN_PROCESS` if the value is `Cleaned by deleting`.  
actionTaken | event1.idm.read_only_udm.security_result.action_details | Directly mapped from the `actionTaken` field.  
actionTaken | event2.idm.read_only_udm.security_result.action_details | Directly mapped from the `actionTaken` field.  
accountName | event2.idm.read_only_udm.additional.fields.value.string_value | Directly mapped from the `accountName` field. The key is set to `accountName`.  
app | event3.idm.read_only_udm.principal.application | Directly mapped from the `app` field.  
circumstances | event2.idm.read_only_udm.additional.fields.value.string_value | Directly mapped from the `circumstances` field. The key is set to `circumstances`.  
Computer_name | event3.idm.read_only_udm.principal.hostname | Directly mapped from the `Computer_name` field.  
Computer_name | event3.idm.read_only_udm.principal.asset.hostname | Directly mapped from the `Computer_name` field.  
date_time |  |   
Detection_name | event3.idm.read_only_udm.security_result.threat_name | Directly mapped from the `Detection_name` field.  
Detectiontype | event3.idm.read_only_udm.security_result.category_details | Directly mapped from the `Detectiontype` field.  
dst | event2.idm.read_only_udm.target.ip | Directly mapped from the `dst` field.  
dst | event2.idm.read_only_udm.target.asset.ip | Directly mapped from the `dst` field.  
dstPort | event2.idm.read_only_udm.target.port | Directly mapped from the `dstPort` field after converting it to an integer.  
event | event1.idm.read_only_udm.metadata.description | Directly mapped from the `event` field.  
event_type | event1.idm.read_only_udm.metadata.product_event_type | Directly mapped from the `event_type` field.  
event_type | event1.idm.read_only_udm.metadata.event_type | Conditionally set to `NETWORK_CONNECTION` if the value is `FirewallAggregated_Event`.  
hash | event1.idm.read_only_udm.target.file.sha1 | Directly mapped from the `hash` field after converting it to lowercase.  
hostname | event1.idm.read_only_udm.target.hostname | Directly mapped from the `hostname` field.  
hostname | event1.idm.read_only_udm.target.asset.hostname | Directly mapped from the `hostname` field.  
hostname | event.alert.devices.hostname | Directly mapped from the `hostname` field.  
ipv4 | event1.idm.read_only_udm.principal.ip | Directly mapped from the `ipv4` field. This field is first stored in a temporary field `udm_ip`.  
ipv4 | event1.idm.read_only_udm.principal.asset.ip | Directly mapped from the `ipv4` field. This field is first stored in a temporary field `udm_ip`.  
ipv4 | event.alert.devices.ip_addresses | Directly mapped from the `ipv4` field after converting it to an IP address.  
Logged_user | event3.idm.read_only_udm.principal.user.userid | Directly mapped from the `Logged_user` field.  
objectUri | event1.idm.read_only_udm.target.file.full_path | Directly mapped from the `objectUri` field.  
objectUri | event2.idm.read_only_udm.target.file.full_path | Directly mapped from the `objectUri` field.  
processName | event2.idm.read_only_udm.target.process.file.full_path | Directly mapped from the `processName` field.  
processName | event1.idm.read_only_udm.principal.process.file.full_path | Directly mapped from the `processName` field.  
process_id | event3.idm.read_only_udm.principal.process.pid | Directly mapped from the `process_id` field.  
process_id | event2.idm.read_only_udm.target.process.pid | Directly mapped from the `process_id` field.  
protocol | event1.idm.read_only_udm.network.ip_protocol | Directly mapped from the `protocol` field.  
proto | event2.idm.read_only_udm.network.ip_protocol | Directly mapped from the `proto` field.  
result | event2.idm.read_only_udm.security_result.action | Conditionally set to `ALLOW` if the value is `Success`.  
Scanner | event3.idm.read_only_udm.security_result.description | Directly mapped from the `Scanner` field.  
severity | event1.idm.read_only_udm.security_result.severity | Mapped from the `severity` field based on these conditions: - `INFO`, `Informational`, `DEBUG`, `info`: `INFORMATIONAL` \- `ERROR`, `error`: `ERROR` \- `WARNING`, `Warning`: `LOW`  
source_address | event1.idm.read_only_udm.principal.ip | Directly mapped from the `source_address` field.  
source_address | event1.idm.read_only_udm.principal.asset.ip | Directly mapped from the `source_address` field.  
source_port | event1.idm.read_only_udm.principal.port | Directly mapped from the `source_port` field after converting it to an integer.  
source_uuid | event1.idm.read_only_udm.metadata.product_log_id | Directly mapped from the `source_uuid` field.  
src | event2.idm.read_only_udm.principal.ip | Directly mapped from the `src` field.  
src | event2.idm.read_only_udm.principal.asset.ip | Directly mapped from the `src` field.  
srcPort | event2.idm.read_only_udm.principal.port | Directly mapped from the `srcPort` field after converting it to an integer.  
target_address | event1.idm.read_only_udm.target.ip | Directly mapped from the `target_address` field.  
target_address | event1.idm.read_only_udm.target.asset.ip | Directly mapped from the `target_address` field.  
target_port | event1.idm.read_only_udm.target.port | Directly mapped from the `target_port` field after converting it to an integer.  
threatName | event2.idm.read_only_udm.security_result.threat_name | Directly mapped from the `threatName` field.  
threatName | event.alert.alert_short_name | Directly mapped from the `threatName` field.  
Time_of_occurrence | event3.idm.read_only_udm.additional.fields.value.string_value | Directly mapped from the `Time_of_occurrence` field. The key is set to `Time_of_occurrence`.  
type | event2.idm.read_only_udm.security_result.category_details | Directly mapped from the `type` field.  
type | event2.idm.read_only_udm.metadata.event_type | Conditionally set to `GENERIC_EVENT` if no other specific event type is matched.  
user_id | event2.idm.read_only_udm.principal.user.userid | Directly mapped from the `user_id` field.  
| event1.idm.read_only_udm.metadata.event_type | Conditionally set to `FILE_UNCATEGORIZED` if the value of `event_type` is `Threat_Event`.  
| event1.idm.read_only_udm.metadata.log_type | Set to `ESET_EDR`.  
| event1.idm.read_only_udm.metadata.product_name | Conditionally set to `ESET` if the value of `event_type` is `FirewallAggregated_Event`.  
| event2.idm.read_only_udm.metadata.log_type | Set to `ESET_EDR`.  
| event2.idm.read_only_udm.metadata.product_name | Set to `EDR`.  
| event2.idm.read_only_udm.metadata.vendor_name | Set to `ESET`.  
| event3.idm.read_only_udm.metadata.event_type | Conditionally set based on these rules: - `USER_UNCATEGORIZED` if `principal_user_present` is `true`. - `STATUS_UPDATE` if `principal_machine_id_present` is `true`. - `GENERIC_EVENT` otherwise.  
| event3.idm.read_only_udm.metadata.log_type | Set to `ESET_EDR`.  
| event3.idm.read_only_udm.metadata.product_name | Set to `EDR`.  
| event3.idm.read_only_udm.metadata.vendor_name | Set to `ESET`.  
| event.alert.is_significant | Set to `true` and then converted to a boolean.  
| event3.idm.read_only_udm.security_result.description | Conditionally set to the value of `kv_data` if `Scanner` is empty.  
`Action_performed` | `security_result.action_details` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/eset-edr-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
