---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extreme-switch/
title: Collect Extreme Networks switch logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:20.314372+00:00
---

# Collect Extreme Networks switch logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extreme-switch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Extreme Networks switch logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Extreme Networks switch logs to Google Security Operations using the Bindplane agent.

Extreme Networks switches generate syslog messages for port status changes, SLPP events, user authentication, VLAN operations, and system events. The parser extracts fields from RFC-5424 formatted syslog and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Extreme Networks switch
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Extreme Networks switch CLI



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
          chronicle/extreme_switch:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: EXTREME_SWITCH
            raw_log_field: body
        
        service:
          pipelines:
            logs/extreme_switch_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/extreme_switch
        




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
          chronicle/extreme_switch:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: EXTREME_SWITCH
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
             




## Configure syslog on Extreme Networks switch

  1. Sign in to the switch using CLI or Console.
  2. Enter the configure command to access the global configuration level:
         
         device# configure terminal
         

  3. Enter the syslog-server IP address command to add a syslog server:

     * Replace `<bindplane_ip>` with the actual Bindplane agent IP address.
    
    logging syslog-server <bindplane_ip>
    

  4. Enter the format command to configure the RFC-5424 format for messages:
         
         format RFC-5424
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`account_type` | `target.user.user_role` | If `account_type` is "Administrative" or "admin", set to "ADMINISTRATOR". Otherwise, map to `target.user.attribute.roles.name`.  
`application` | `target.application` | Directly mapped.  
`attr` | `additional.fields` | Parsed to extract the WWN and create a key-value pair with key "wwn" and the extracted WWN as the string value.  
`class` | `additional.fields` | Creates a key-value pair with key "class" and the value of the `class` field as the string value.  
`Cause` | `additional.fields` | Creates a key-value pair with key "Cause" and the value of the `Cause` field as the string value. Empty object created if no specific auth fields are present.  
`Info` | `security_result.summary` | Directly mapped.  
`interface` | `additional.fields` | Creates a key-value pair with key "interface" and the value of the `interface` field as the string value.  
`ip` | `principal.ip` | Directly mapped.  
`intermediary_ip` | `intermediary.ip` | Directly mapped.  
`kv_data` | Various | Used to extract key-value pairs and map them to different UDM fields based on the key. For example, `VrIpAddr` is mapped to `intermediary.ip`, `IP` and `Addr` are mapped to `principal.ip`, `SlppRxPort` is mapped to `principal.port`, and various `rc*` fields are mapped to `security_result.detection_fields`.  
`log_data` | Various | Parsed to extract information about user logins, logouts, and other events. Used to populate fields like `principal.ip`, `principal.resource.name`, `target.user.userid`, `target.application`, `security_result.summary`, `security_result.description`, and `metadata.description`.  
`log_type` | `additional.fields` | Creates a key-value pair with key "log" and the value of the `log_type` field as the string value.  
`message` | Various | The original log message. Parsed to extract various fields. The timestamp is extracted from either the `timestamp` field (if present and in "yyyy-mm-ddTHH:mm:ss" format) or from the `message` field using grok patterns. If extracted from the message field, it's the timestamp within the log message itself. Determined based on the presence of `has_principal`, `has_target`, `user_login`, and `user_logout` flags. Can be "USER_LOGIN", "USER_LOGOUT", "STATUS_UPDATE", or "GENERIC_EVENT". Mapped from the `msgid` field. Static value: "EXTREME_SWITCH". Mapped from the `ver` field. Static value: "EXTREME_SWITCH".  
`msgid` | `metadata.product_log_id` | Directly mapped.  
`port` | `principal.port` | Directly mapped and converted to an integer.  
`protocol` | `additional.fields` | Creates a key-value pair with key "Protocol" and the value of the `protocol` field as the string value.  
`rcPortVLacpAdminEnable` | `security_result.detection_fields` | Creates a key-value pair with key "rcPortVLacpAdminEnable" and its value.  
`rcSyslogHostAddress` | `principal.hostname` | Directly mapped.  
`rcSyslogHostAddressType` | `security_result.detection_fields` | Creates a key-value pair with key "rcSyslogHostAddressType" and its value.  
`rcSyslogHostEnable` | `security_result.detection_fields` | Creates a key-value pair with key "rcSyslogHostEnable" and its value.  
`rcSyslogHostFacility` | `security_result.detection_fields` | Creates a key-value pair with key "rcSyslogHostFacility" and its value.  
`rcSyslogHostMapErrorSeverity` | `security_result.detection_fields` | Creates a key-value pair with key "rcSyslogHostMapErrorSeverity" and its value.  
`rcSyslogHostMapFatalSeverity` | `security_result.detection_fields` | Creates a key-value pair with key "rcSyslogHostMapFatalSeverity" and its value.  
`rcSyslogHostMapInfoSeverity` | `security_result.detection_fields` | Creates a key-value pair with key "rcSyslogHostMapInfoSeverity" and its value.  
`rcSyslogHostMapWarningSeverity` | `security_result.detection_fields` | Creates a key-value pair with key "rcSyslogHostMapWarningSeverity" and its value.  
`rcSyslogHostRowStatus` | `security_result.detection_fields` | Creates a key-value pair with key "rcSyslogHostRowStatus" and its value.  
`rcSyslogHostSeverity` | `security_result.detection_fields` | Creates a key-value pair with key "rcSyslogHostSeverity" and its value.  
`resource` | `principal.resource.name` | Directly mapped.  
`sec_description` | `security_result.description` | Directly mapped.  
`seqnum` | `additional.fields` | Creates a key-value pair with key "seqnum" and the value of the `seqnum` field as the string value.  
`session_id` | `network.session_id` | Directly mapped.  
`severity` | `security_result.severity` | Mapped with conversion: "CRITICAL", "ERROR", "HIGH" are mapped directly; "INFO" is mapped to "INFORMATIONAL"; "WARNING" is mapped to "MEDIUM"; "LOW", "MEDIUM", and "INFORMATIONAL" are mapped directly.  
`SlppIncomingVlanId` | `additional.fields` | Creates a key-value pair with key "SlppIncomingVlanId" and the value of the `SlppIncomingVlanId` field as the string value.  
`SlppRxVlan` | `additional.fields` | Creates a key-value pair with key "SlppRxVlan" and the value of the `SlppRxVlan` field as the string value.  
`SlppSrcMacAddress` | `principal.mac` | Directly mapped.  
`Status` | `additional.fields` | Creates a key-value pair with key "Status" and the value of the `Status` field as the string value.  
`swname` | `additional.fields` | Creates a key-value pair with key "swname" and the value of the `swname` field as the string value.  
`timestamp` | `metadata.event_timestamp` | Parsed and converted to a timestamp object.  
`tz` | `additional.fields` | Creates a key-value pair with key "tz" and the value of the `tz` field as the string value.  
`Type` | `additional.fields` | Creates a key-value pair with key "Type" and the value of the `Type` field as the string value.  
`username` | `target.user.userid` | Directly mapped.  
`ver` | `metadata.product_version` | Directly mapped.  
`VrId` | `additional.fields` | Creates a key-value pair with key "VrId" and the value of the `VrId` field as the string value.  
`protocol", "VrId", "SlppRxVlan", "SlppIncomingVlanId", "Type", "Cause` | `additional.fields` | Mapped from changelog  
`ver` | `metadata.version` | Mapped from changelog  
`rcPortVLacpAdminEnable", "rcSyslogHostMapFatalSeverity", "rcSyslogHostMapWarningSeverity", "rcSyslogHostRowStatus", "rcSyslogHostFacility", "rcSyslogHostAddressType", "rcSyslogHostMapErrorSeverity", "rcSyslogHostMapInfoSeverity", "rcSyslogHostSeverity", "rcSyslogHostEnable` | `security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/extreme-switch-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
