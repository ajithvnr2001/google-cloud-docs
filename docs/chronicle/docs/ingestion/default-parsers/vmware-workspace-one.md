---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-workspace-one/
title: Collect Omnissa Workspace ONE UEM (formerly VMware Workspace ONE) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:30:55.828286+00:00
---

# Collect Omnissa Workspace ONE UEM (formerly VMware Workspace ONE) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-workspace-one/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Omnissa Workspace ONE UEM (formerly VMware Workspace ONE) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Omnissa Workspace ONE UEM (formerly known as VMware Workspace ONE) logs to Google Security Operations using Bindplane.

Omnissa Workspace ONE UEM is a unified endpoint management platform that enables organizations to manage and secure devices, applications, and data across mobile, desktop, rugged, and IoT endpoints. The parser normalizes syslog messages from Workspace ONE UEM, extracting fields such as device compliance events, application management actions, enrollment status changes, and console administration activities, and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites: * A Google SecOps instance * Windows Server 2016 or later, or Linux host with `systemd` * Network connectivity between the Bindplane agent and the Omnissa Workspace ONE UEM console * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements * Administrative access to the Omnissa Workspace ONE UEM console

## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.

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
         
         msiexec /i "[https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi](https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi)" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         




The service should show as **RUNNING**.

### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         




The service should show as **active (running)**.

### Additional installation resources

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            tcplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/workspace_one:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: VMWARE_WORKSPACE_ONE
                raw_log_field: body
        
        service:
            pipelines:
                logs/workspace_one_to_chronicle:
                    receivers:
                        - tcplog
                    exporters:
                        - chronicle/workspace_one
        




### Configuration parameters

Replace the following placeholders:

**Receiver configuration:**

  * `listen_address`: IP address and port to listen on: 
    * `0.0.0.0` to listen on all interfaces (recommended)
    * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)



**Exporter configuration:**

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

To restart the Bindplane agent in Linux:

  1. Run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. Verify the service is running:
         
         sudo systemctl status observiq-otel-collector
         

  3. Check logs for errors:
         
         sudo journalctl -u observiq-otel-collector -f
         




To restart the Bindplane agent in Windows, choose one of the following options:

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
           




## Configure syslog forwarding in Omnissa Workspace ONE UEM

  1. Sign in to the **Omnissa Workspace ONE UEM** console.
  2. Go to **Settings > System > Enterprise Integration > Syslog**.
  3. Select **Enabled** to turn on syslog integration.
  4. Provide the following configuration details:

     * **Hostname** : Enter the IP address or hostname of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514`.
     * **Protocol** : Select **TCP**.
     * **Syslog Facility** : Select **Local0** or another facility appropriate for your environment.
     * **Message Tag** : Enter a descriptive tag (for example, `WorkspaceONE`).
**Note:** The protocol and port must match the Bindplane agent receiver configuration. This guide uses TCP on port 514.
  5. In the **Event Categories** section, select the event types to forward:

     * **Device Events** \- enrollment, compliance, and device status changes
     * **Console Events** \- administrator actions and configuration changes
     * **Application Events** \- application installation, removal, and management actions
     * **Compliance Events** \- compliance policy violations and remediation actions
  6. Click **Save** to apply the syslog configuration.

  7. Verify that logs are being sent by checking the Bindplane agent logs.

**Note:** In Workspace ONE UEM console version 2410 and later, the UI may display updated Omnissa branding while some internal references may still show VMware or AirWatch naming. This does not affect syslog functionality.



## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`AdminAccount` | `principal.user.userid` | The `AdminAccount` from the raw log is mapped to the `principal.user.userid` field.  
`Application` | `target.application` | The `Application` field from the raw log is mapped to the `target.application` field.  
`ApplicationUUID` | `additional.fields` | The `ApplicationUUID` field from the raw log is added as a key-value pair to the `additional.fields` array in the UDM. The key is "ApplicationUUID".  
`BytesReceived` | `network.received_bytes` | The `BytesReceived` field from the raw log is mapped to the `network.received_bytes` field.  
`Device` | `target.hostname` | The `Device` field from the raw log is mapped to the `target.hostname` field.  
`FriendlyName` | `target.hostname` | The `FriendlyName` field from the raw log is mapped to the `target.hostname` field when `Device` is not available.  
`GroupManagementData` | `security_result.description` | The `GroupManagementData` field from the raw log is mapped to the `security_result.description` field.  
`Hmac` | `additional.fields` | The `Hmac` field from the raw log is added as a key-value pair to the `additional.fields` array in the UDM. The key is "Hmac".  
`LoginSessionID` | `network.session_id` | The `LoginSessionID` field from the raw log is mapped to the `network.session_id` field.  
`LogDescription` | `metadata.description` | The `LogDescription` field from the raw log is mapped to the `metadata.description` field.  
`MessageText` | `metadata.description` | The `MessageText` field from the raw log is mapped to the `metadata.description` field.  
`OriginatingOrganizationGroup` | `principal.user.group_identifiers` | The `OriginatingOrganizationGroup` field from the raw log is mapped to the `principal.user.group_identifiers` field.  
`OwnershipType` | `additional.fields` | The `OwnershipType` field from the raw log is added as a key-value pair to the `additional.fields` array in the UDM. The key is "OwnershipType".  
`Profile` | `target.resource.name` | The `Profile` field from the raw log is mapped to the `target.resource.name` field when `ProfileName` is not available.  
`ProfileName` | `target.resource.name` | The `ProfileName` field from the raw log is mapped to the `target.resource.name` field.  
`Request Url` | `target.url` | The `Request Url` field from the raw log is mapped to the `target.url` field.  
`SmartGroupName` | `target.group.group_display_name` | The `SmartGroupName` field from the raw log is mapped to the `target.group.group_display_name` field.  
`Tags` | `additional.fields` | The `Tags` field from the raw log is added as a key-value pair to the `additional.fields` array in the UDM. The key is "Tags".  
`User` | `target.user.userid` | The `User` field from the raw log is mapped to the `target.user.userid` field. The `Event Category` from the raw log is added as a key-value pair to the `additional.fields` array in the UDM. The key is "Event Category". The `Event Module` from the raw log is added as a key-value pair to the `additional.fields` array in the UDM. The key is "Event Module". The `Event Source` from the raw log is added as a key-value pair to the `additional.fields` array in the UDM. The key is "Event Source". Set to "SSO" by the parser for specific events. Derived from the raw log's timestamp. The parser extracts the date and time from the raw log and converts it to a UDM timestamp. Determined by the parser based on the `event_name` and other fields. See parser code for the mapping logic. Set to "AIRWATCH" by the parser. The `event_name` from the raw log is mapped to the `metadata.product_event_type` field. Set to "AirWatch" by the parser. Set to "VMWare" by the parser. The `domain` from the raw log is mapped to the `principal.administrative_domain` field. The `hostname` is extracted from the `device_name` field in the raw log or mapped from the `Device` or `FriendlyName` fields. The `sys_ip` from the raw log is mapped to the `principal.ip` field. Extracted from the raw log for certain event types. Extracted from the raw log for certain event types. The `user_name` from the raw log is mapped to the `principal.user.userid` field. Extracted from the raw log for certain event types. Set by the parser for specific events. Set by the parser for specific events. The `event_category` from the raw log is mapped to the `security_result.category_details` field. Extracted from the raw log for certain event types. Extracted from the raw log for certain event types. The `domain` from the raw log is mapped to the `target.administrative_domain` field. Constructed by combining `DeviceSerialNumber` and `DeviceUdid` from the raw log for the "DeleteDeviceRequested" event. Extracted from the raw log for certain event types. Extracted from the raw log for certain event types. The `sys_ip` or other IP addresses from the raw log are mapped to the `target.ip` field. Extracted from the raw log for certain event types. Extracted from the raw log for certain event types. Set by the parser for specific events. Extracted from the raw log for certain event types. Extracted from the raw log for certain event types. Extracted from the raw log for certain event types.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-workspace-one-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
