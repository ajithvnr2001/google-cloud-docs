---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/manage-engine-ad360/
title: Collect ManageEngine AD360 logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:50:43.293989+00:00
---

# Collect ManageEngine AD360 logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/manage-engine-ad360/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ManageEngine AD360 logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest ManageEngine AD360 logs to Google Security Operations using the Bindplane agent.

ManageEngine AD360 is an integrated identity and access management solution that generates syslog messages for Active Directory changes, authentication events, network connections, and security policy violations. The parser extracts fields from syslog-formatted logs using grok patterns and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the ManageEngine AD360 server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the ManageEngine AD360 web UI



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
            chronicle/manage_engine_ad360:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: MANAGE_ENGINE_AD360
                raw_log_field: body
        
        service:
            pipelines:
                logs/manage_engine_ad360_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/manage_engine_ad360
        




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
             




## Configure ManageEngine AD360 syslog export

  1. Sign in to the **AD360** web UI.
  2. Go to **Admin > Administration > SIEM Integration**.
  3. Click the **Configure Now** link beside the **ADSelfService** component.
  4. Provide the following configuration details: 
     * **Server Type** : Select **Syslog**.
     * **Server Name/IP** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number.
     * **Protocol** : Select **UDP**.
     * **Syslog Standard** : Select **RFC 5424**.
     * Click the **Advanced** list.
     * **Severity** : Select **Informational**.
  5. Click **Configure** to save.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
AccessControlRuleName | security_result.rule_name | Value taken from the field `AccessControlRuleName` if exists, else from the field `rule_name`  
ACPolicy | security_result.rule_labels.value | Value taken from the field `ACPolicy`  
action | security_result.action_details | Directly mapped to UDM  
action_id | security_result.detection_fields.value | Value taken from the field `action_id`  
application_protocol | network.application_protocol | Directly mapped to UDM  
bytes | network.sent_bytes | Directly mapped to UDM  
client_ip | principal.ip | Directly mapped to UDM  
ConnectionID | network.session_id | Value taken from the field `connection_id` if exists, else from the field `ConnectionID`, else from the field `ses`  
destination_ip | target.ip | Directly mapped to UDM  
destination_port | target.port | Directly mapped to UDM  
DeviceUUID | target.asset_id | Value taken from the field `DeviceUUID` if exists, else from the field `distinguished_name_device_id`  
distinguished_name_device_id | target.asset_id | Value taken from the field `DeviceUUID` if exists, else from the field `distinguished_name_device_id`  
distinguished_name_user | target.user.userid | Directly mapped to UDM  
DST | target.ip | Value taken from the field `DST` if exists, else from the field `DstIP`  
DPT | target.port | Value taken from the field `DPT` if exists, else from the field `DstPort`, else from the field `destination_port`  
DstIP | target.ip | Value taken from the field `DST` if exists, else from the field `DstIP`  
DstPort | target.port | Value taken from the field `DPT` if exists, else from the field `DstPort`, else from the field `destination_port`  
EgressInterface | additional.fields.value.string_value | Directly mapped to UDM  
EgressZone | target.location.name | Directly mapped to UDM  
EventPriority | security_result.severity | Mapped to different severity levels based on the value of `EventPriority` field.  
exe | principal.process.command_line | Directly mapped to UDM  
geoip.city_name | principal.location.city | Directly mapped to UDM  
geoip.country_name | principal.location.country_or_region | Directly mapped to UDM  
geoip.latitude | principal.location.region_latitude | Directly mapped to UDM  
geoip.longitude | principal.location.region_longitude | Directly mapped to UDM  
http_status | network.http.response_code | Directly mapped to UDM  
id | metadata.product_log_id | Directly mapped to UDM  
IngressInterface | additional.fields.value.string_value | Directly mapped to UDM  
IngressZone | principal.location.name | Directly mapped to UDM  
LEN | additional.fields.value.string_value | Directly mapped to UDM  
message_number |  | Not Mapped  
NAPPolicy | security_result.rule_labels.value | Value taken from the field `NAPPolicy`  
network_direction | network.direction | Directly mapped to UDM  
OUT | additional.fields.value.string_value | Directly mapped to UDM  
pid | target.process.pid | Directly mapped to UDM  
ppid | target.process.parent_process.pid | Directly mapped to UDM  
PREC | additional.fields.value.string_value | Directly mapped to UDM  
principal_hostname | principal.hostname | Directly mapped to UDM  
product_event_type | metadata.product_event_type | Directly mapped to UDM  
protocol | network.ip_protocol | Used to populate the `PROTO` field and then mapped to UDM using a lookup table.  
PROTO | network.ip_protocol | Mapped to UDM using a lookup table based on the protocol number.  
request_method | network.http.method | Directly mapped to UDM  
rule_name | security_result.rule_name | Value taken from the field `AccessControlRuleName` if exists, else from the field `rule_name`  
ses | network.session_id | Value taken from the field `connection_id` if exists, else from the field `ConnectionID`, else from the field `ses`  
source_ip | principal.ip | Directly mapped to UDM  
source_port | principal.port | Directly mapped to UDM  
SPT | principal.port | Value taken from the field `SPT` if exists, else from the field `SrcPort`, else from the field `source_port`  
SRC | principal.ip | Value taken from the field `SRC` if exists, else from the field `SrcIP`, else from the field `client_ip`  
SrcIP | principal.ip | Value taken from the field `SRC` if exists, else from the field `SrcIP`, else from the field `client_ip`  
SrcPort | principal.port | Value taken from the field `SPT` if exists, else from the field `SrcPort`, else from the field `source_port`  
timestamp | metadata.event_timestamp | Directly mapped to UDM  
TOS | additional.fields.value.string_value | Directly mapped to UDM  
TTL | additional.fields.value.string_value | Directly mapped to UDM  
URL | target.url | Directly mapped to UDM  
user_agent | network.http.user_agent | Directly mapped to UDM  
WINDOW | additional.fields.value.string_value | Directly mapped to UDM  
| metadata.vendor_name | Value is hardcoded to `MANAGE_ENGINE_AD360`  
| metadata.product_name | Value is hardcoded to `MANAGE_ENGINE_AD360`  
| metadata.log_type | Value is hardcoded to `MANAGE_ENGINE_AD360`  
| metadata.event_type | Value set to `NETWORK_CONNECTION` if both `SRC` and `DST` fields are present, else set to `STATUS_UPDATE` if either `SRC` or `principal_hostname` is present. If none of these conditions are met, it defaults to `GENERIC_EVENT`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/manage-engine-ad360-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
