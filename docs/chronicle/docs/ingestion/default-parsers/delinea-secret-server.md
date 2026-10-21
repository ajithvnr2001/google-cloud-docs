---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/delinea-secret-server/
title: Collect Delinea Secret Server logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:10:10.566986+00:00
---

# Collect Delinea Secret Server logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/delinea-secret-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Delinea Secret Server logs

**Parser Version:** 5.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Delinea Secret Server logs to Google Security Operations using the Bindplane agent.

Delinea Secret Server (formerly Thycotic) is a privileged access management (PAM) solution that generates syslog messages in CEF format for secret access, user authentication, and audit events. The parser extracts fields and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Delinea Secret Server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrator credentials for Delinea Secret Server



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
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/delinea_secret_server:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: THYCOTIC
                raw_log_field: body
        
        service:
            pipelines:
                logs/delinea_secret_server_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/delinea_secret_server
        




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
             




## Configure Thycotic Secret Server to send logs using syslog

  1. Sign in to Thycotic Secret Server with administrator credentials.
  2. Go to **Admin > Configuration**.
  3. Click **Edit**.
  4. Select the **Enable Syslog/CEF logging** checkbox and specify the following details: 
     * **Syslog/CEF server** : Enter the IP address of your syslog server/Bindplane.
     * **Syslog/CEF protocol** : Select **UDP** or **TCP** (depending on your Bindplane configuration).
     * **Syslog/CEF port** : Enter the port number that the syslog server or Bindplane is configured to listen on.
  5. Click **Save**.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
Account_Domain | event1.idm.read_only_udm.principal.domain | The value is taken from the `Account_Domain` field in the `msg` field of the raw log.  
By User | event1.idm.read_only_udm.principal.user.userid | The value is taken from the `By User` field in the `msg` field of the raw log.  
Container Id | event1.idm.read_only_udm.principal.asset.asset_id | The value is taken from the `Container Id` field in the `msg` field of the raw log and is prefixed with `container_id:`.  
Container name | event1.idm.read_only_udm.principal.resource.name | The value is taken from the `Container name` field in the `msg` field of the raw log.  
cs2 | event1.idm.read_only_udm.additional.fields[].value.string_value | The value is taken from the `cs2` field in the `msg` field of the raw log.  
cs3 | event1.idm.read_only_udm.target.file.full_path | The value is taken from the `cs3` field in the `msg` field of the raw log.  
cs4 | event1.idm.read_only_udm.principal.user.user_display_name | The value is taken from the `cs4` field in the `msg` field of the raw log.  
Details | event1.idm.read_only_udm.additional.fields[].value.string_value | The value is taken from the `Details` field in the `msg` field of the raw log.  
fname | event1.idm.read_only_udm.target.file.full_path | The value is taken from the `fname` field in the `msg` field of the raw log.  
Host | event1.idm.read_only_udm.principal.hostname, event1.idm.read_only_udm.principal.asset.hostname | The value is taken from the `Host` field in the `msg` field of the raw log.  
Item Name | event1.idm.read_only_udm.target.user.userid | The value is taken from the `Item Name` field in the `msg` field of the raw log.  
| event1.idm.read_only_udm.additional.fields[].key | The value is hardcoded to `fname`.  
| event1.idm.read_only_udm.additional.fields[].key | The value is hardcoded to `Group or User`.  
| event1.idm.read_only_udm.additional.fields[].key | The value is hardcoded to `Details`.  
| event1.idm.read_only_udm.additional.fields[].key | The value is hardcoded to `type_id`.  
| event1.idm.read_only_udm.extensions.auth.type | The value is hardcoded to `MACHINE`.  
| event1.idm.read_only_udm.metadata.description | The value is taken from the `thycotic_event` field, which is extracted from the raw log using a grok pattern.  
| event1.idm.read_only_udm.metadata.event_timestamp.seconds | The value is derived from the `rt` field if present, otherwise from the `ts` field. Both fields are extracted from the raw log using grok patterns.  
| event1.idm.read_only_udm.metadata.event_type | The value is determined based on the `thycotic_event` field and other conditions. For example, if `thycotic_event` is `USER - LOGIN`, the event type is set to `USER_LOGIN`.  
| event1.idm.read_only_udm.metadata.log_type | The value is hardcoded to `THYCOTIC`.  
| event1.idm.read_only_udm.metadata.product_event_type | The value is taken from the `thycotic_event` field, which is extracted from the raw log using a grok pattern.  
| event1.idm.read_only_udm.metadata.product_log_id | The value is taken from the `action_id` field, which is extracted from the raw log using a grok pattern.  
| event1.idm.read_only_udm.metadata.product_name | The value is taken from the `device_product` field, which is extracted from the raw log using a grok pattern. If the field is empty, the value is hardcoded to `Secret Server`.  
| event1.idm.read_only_udm.metadata.product_version | The value is taken from the `device_version` field, which is extracted from the raw log using a grok pattern.  
| event1.idm.read_only_udm.metadata.vendor_name | The value is hardcoded to `Thycotic`.  
| event1.idm.read_only_udm.network.ip_protocol | The value is set to `TCP` if the `input.type` field is `tcp`.  
| event1.idm.read_only_udm.observer.application | The value is taken from the `agent.type` field if present, otherwise it is hardcoded to `Secret Server`.  
| event1.idm.read_only_udm.observer.asset_id | The value is set to `Agent ID:` concatenated with the `agent.id` field.  
| event1.idm.read_only_udm.observer.hostname | The value is taken from the `agent.hostname` field if present, otherwise from the `server` field.  
| event1.idm.read_only_udm.observer.platform_version | The value is taken from the `agent.version` field.  
| event1.idm.read_only_udm.observer.user.userid | The value is taken from the `agent.name` field.  
| event1.idm.read_only_udm.principal.asset.asset_id | The value is set to `ID:` concatenated with the `host.id` field.  
| event1.idm.read_only_udm.principal.asset.hardware.cpu_platform | The value is taken from the `host.architecture` field.  
| event1.idm.read_only_udm.principal.asset.hostname | The value is taken from the `server` field if present, otherwise from the `host.hostname` field.  
| event1.idm.read_only_udm.principal.asset.ip | The value is taken from the `src` field if present, otherwise from the `src_ip` field.  
| event1.idm.read_only_udm.principal.hostname | The value is taken from the `host.hostname` field if present, otherwise from the `server` field.  
| event1.idm.read_only_udm.principal.ip | The value is taken from the `src` field if present, otherwise from the `src_ip` field or from the `host.ip` field.  
| event1.idm.read_only_udm.principal.mac | The value is taken from the `host.mac` field.  
| event1.idm.read_only_udm.principal.platform | The value is set to `LINUX` if the `host_os_platform` field is `centos`, otherwise it is set to the uppercase value of the `host_os_platform` field.  
| event1.idm.read_only_udm.principal.platform_patch_level | The value is taken from the `host.os.kernel` field.  
| event1.idm.read_only_udm.principal.platform_version | The value is taken from the `host.os.version` field.  
| event1.idm.read_only_udm.principal.port | The value is taken from the `src_port` field, which is extracted from the `log.source.address` field using a grok pattern.  
| event1.idm.read_only_udm.principal.user.user_display_name | The value is taken from the `cs4` field in the `msg` field of the raw log.  
| event1.idm.read_only_udm.principal.user.userid | The value is taken from the `suser` field in the `msg` field of the raw log, or from the `By User` field if `thycotic_event` is `USER - LOGIN`, `USER - LOGOUT`, `USER - LOGINFAILURE`, or `USER - EDIT`.  
| event1.idm.read_only_udm.security_result.action | The value is taken from the `Action` field in the `msg` field of the raw log. It can also be set to `ALLOW` or `BLOCK` based on the value of `thycotic_event`.  
| event1.idm.read_only_udm.security_result.description | The value is taken from the `temp_message` field, which contains the remaining part of the `msg` field after extracting other fields.  
| event1.idm.read_only_udm.security_result.severity | The value is determined based on the `syslog_severity` field. For example, if `syslog_severity` contains `error` or `warning`, the severity is set to `HIGH`. If `thycotic_event` is `System Log`, the severity is set to `INFORMATIONAL`.  
| event1.idm.read_only_udm.security_result.severity_details | The value is taken from the `syslog_severity` field.  
| event1.idm.read_only_udm.target.file.full_path | The value is constructed by concatenating the `cs3` and `fname` fields with a `/` separator if both fields are present. If only one field is present, the value is taken from that field.  
| event1.idm.read_only_udm.target.resource.product_object_id | The value is taken from the `type_id` field.  
| event1.idm.read_only_udm.target.user.userid | The value is taken from the `item_name` field in the `msg` field of the raw log, or from the `Item Name` field if `thycotic_event` is `USER - LOGIN`, `USER - LOGOUT`, `USER - LOGINFAILURE`, or `USER - EDIT`.  
| events.timestamp.seconds | The value is derived from the `rt` field if present, otherwise from the `ts` field. Both fields are extracted from the raw log using grok patterns.  
rt | event1.idm.read_only_udm.metadata.event_timestamp.seconds | The value is taken from the `rt` field in the `msg` field of the raw log and is used to set the event timestamp.  
src | event1.idm.read_only_udm.principal.asset.ip, event1.idm.read_only_udm.principal.ip | The value is taken from the `src` field in the `msg` field of the raw log.  
src_ip | event1.idm.read_only_udm.principal.asset.ip, event1.idm.read_only_udm.principal.ip | The value is taken from the `src_ip` field, which is extracted from the `log.source.address` field using a grok pattern.  
`msg` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`suid` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`cs4Label` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`user_data` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`EventClassId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`item_Id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Details` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Event` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Action_data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`item_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`source_host_network_ipaddress` | `principal.ip` | Mapped from changelog  
`target_host_name` | `target_host_name` | Mapped from changelog  
`machineTimeZone` | `additional.fields` | Mapped from changelog  
`machineName` | `additional.fields` | Mapped from changelog  
`schemaVersion` | `additional.fields` | Mapped from changelog  
`byUserEmailAddress` | `principal.user.email_addresses` | Mapped from changelog  
`byUserDisplayName` | `principal.user.email_addresses` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/delinea-secret-server-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
