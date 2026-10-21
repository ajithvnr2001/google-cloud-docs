---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wsm/
title: Collect Cisco WSM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:32.936655+00:00
---

# Collect Cisco WSM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wsm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco WSM logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Wireless Services Module logs to Google Security Operations using Bindplane. The Cisco Wireless Services Module (WiSM) is an integrated wireless LAN controller module for Cisco Catalyst 6500 Series switches that manages wireless access points, handles client authentication, and enforces wireless security policies across enterprise wireless networks.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Cisco Wireless Services Module or Wireless LAN Controller (WLC).



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



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

For additional installation options, consult the [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it is in the `/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/cisco_wsm:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             customer_id: '<customer_id>'
             endpoint: chronicle.googleapis.com
             log_type: CISCO_WSM
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/cisco_wsm:
               receivers:
                 - udplog
               exporters:
                 - chronicle/cisco_wsm
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * Replace `<customer_id>` with the actual customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the path where the service account key file (Option 1) was saved in the Get Google SecOps credentials for the Bindplane agent section.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/cisco_wsm:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CISCO_WSM
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

To restart the Bindplane agent in Linux: 

  1. Run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. Verify the service is running:
         
         sudo systemctl status observiq-otel-collector
         

  3. Check logs for errors:
         
         sudo journalctl -u observiq-otel-collector -f
         




To restart the Bindplane agent in Windows:

  1. Choose one of the following options:

     * Command Prompt or PowerShell as administrator:
    
    net stop observiq-otel-collector && net start observiq-otel-collector
    

     * Services console: 
       1. Press `Win+R`, type `services.msc`, and press Enter.
       2. Locate **observIQ OpenTelemetry Collector**.
       3. Right-click and select **Restart**.
  2. Verify the service is running:
         
         sc query observiq-otel-collector
         

  3. Check logs for errors:
         
         type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
         




## Configure syslog forwarding on Cisco Wireless Services Module

### Configure syslog via the WLC web interface

  1. Sign in to the **Cisco Wireless LAN Controller** web interface.
  2. Go to **Management > Logs > Config**.
  3. In the **Syslog Server IP Address** field, enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
  4. Click **Add**.
  5. Set the following syslog parameters: 
     * **Syslog Level** : Select **Informational** (or your preferred severity level).
     * **Syslog Facility** : Select **Local6**.
  6. Click **Apply**.
  7. Click **Save Configuration** to save the settings.

**Note:** The WLC sends syslog messages on UDP port 514 by default. This port is not configurable on AireOS-based controllers. Ensure the Bindplane agent is listening on port 514.



### Configure syslog via the WLC CLI

  1. Connect to the Cisco Wireless LAN Controller via SSH or console.
  2. Add the syslog server (replace `<BINDPLANE_IP>` with the IP address of the Bindplane agent host):
         
         config logging syslog host <BINDPLANE_IP>
         

  3. Set the syslog logging level:
         
         config logging syslog level informational
         

  4. Set the syslog facility:
         
         config logging syslog facility local6
         

  5. Save the configuration:
         
         save config
         

  6. Verify the syslog configuration:
         
         show logging
         

**Note:** The WLC sends syslog messages on UDP port 514 by default. This port is not configurable via the CLI on AireOS-based controllers.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`auth_mechanism` | `extensions.auth.mechanism` | Merged  
`cisco_mnemonic` | `extensions.auth.mechanism` | Mapped: `AAA_MAX_RETRY` → `auth_mechanism`  
`cisco_mnemonic` | `extensions.auth.type` | Mapped: `"LOGOUT","SESS_LOGOUT","RELOAD"` → `MACHINE`, `"LOGIN_SUCCESS","WEBLOGIN_SUCCESS","...  
`hostname` | `intermediary.hostname` | Directly mapped  
`intermediary_ip` | `intermediary.ip` | Merged  
`cisco_message` | `metadata.description` | Directly mapped  
`syslogtimestamp` | `metadata.event_timestamp` | Parsed as `MMM d HH:mm:ss`  
`cisco_mnemonic` | `metadata.event_type` | Mapped values (20 total, e.g. `"LOGOUT","SESS_LOGOUT","RELOAD"` → `NETWORK_CONNECTION`, `"LO...  
`cisco_tag` | `metadata.product_event_type` | Directly mapped  
`auditid` | `metadata.product_log_id` | Directly mapped  
`cisco_mnemonic` | `network.direction` | Mapped: `"USER_NAME_CREATED", "Q_IND","INVALID_STATE_EVENT","ENTRY_CHANGED","ENTRY_DELETED",...  
`cisco_mnemonic` | `network.ip_protocol` | Mapped: `"ESTABLISHED_TO_PEER", "HANDSHAKE_FAILURE"` → `UDP`  
`cipher` | `network.tls.cipher` | Directly mapped  
`hostname` | `principal.hostname` | Directly mapped  
`principal_hostname` | `principal.hostname` | Directly mapped  
`cisco_mnemonic` | `principal.ip` | Mapped: `"LOGOUT","SESS_LOGOUT","RELOAD"` → `principal_ip`, `"LOGIN_SUCCESS","WEBLOGIN_SUCCE...  
`principal_ip` | `principal.ip` | Merged  
`cisco_mnemonic` | `principal.mac` | Mapped values (6 total, e.g. `"USER_NAME_CREATED", "Q_IND","INVALID_STATE_EVENT","ENTRY_CHAN...  
`principal_mac` | `principal.mac` | Mapped: `^(([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2})$` → `principal_mac`  
`principal_port` | `principal.port` | Directly mapped  
`principal_process_id` | `principal.process.pid` | Directly mapped  
`cisco_facility` | `principal.resource.type` | Directly mapped  
`username` | `principal.user.userid` | Directly mapped  
`action` | `security_result.action` | Merged  
`cisco_mnemonic` | `security_result.action` | Mapped: `"ESTABLISHED_TO_PEER", "HANDSHAKE_FAILURE"` → `action`, `"SIG_INFO1", "ECHO_ERR"` →...  
`category` | `security_result.category` | Merged  
`cisco_mnemonic` | `security_result.category` | Mapped: `AAA_MAX_RETRY` → `category`, `ABORT_AUTH` → `category`  
`cisco_mnemonic` | `security_result.description` | Mapped values (7 total, e.g. `"USER_NAME_CREATED", "Q_IND","INVALID_STATE_EVENT","ENTRY_CHAN...  
`database_detection_fields` | `security_result.detection_fields` | Merged  
`profile_detection_fields` | `security_result.detection_fields` | Merged  
`tls_local_ip_detection_fields` | `security_result.detection_fields` | Merged  
`tls_remote_detection_fields` | `security_result.detection_fields` | Merged  
`cisco_severity` | `security_result.severity` | Mapped values (8 total, e.g. `0` → `ALERT`, `1` → `CRITICAL`, `2` → `HIGH`)  
`cisco_severity` | `security_result.severity_details` | Mapped values (8 total, e.g. `0` → `System unusable`, `1` → `Immediate action needed`, `2` ...  
`cisco_mnemonic` | `security_result.summary` | Mapped values (11 total, e.g. `"USER_NAME_CREATED", "Q_IND","INVALID_STATE_EVENT","ENTRY_CHA...  
`reason_message` | `security_result.summary` | Directly mapped  
`terminal` | `target.hostname` | Directly mapped  
`cisco_mnemonic` | `target.ip` | Mapped: `"LOGOUT","SESS_LOGOUT","RELOAD"` → `target_ip`, `"USER_NAME_CREATED", "Q_IND","INVA...  
`target_ip` | `target.ip` | Merged  
`cisco_mnemonic` | `target.mac` | Mapped: `"USER_NAME_CREATED", "Q_IND","INVALID_STATE_EVENT","ENTRY_CHANGED","ENTRY_DELETED",...  
`target_mac` | `target.mac` | Mapped: `^(([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2})$` → `target_mac`  
`username` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `MACHINE`  
N/A | `metadata.event_type` | Constant: `NETWORK_CONNECTION`  
N/A | `metadata.product_name` | Constant: `CISCO_WSM`  
N/A | `metadata.vendor_name` | Constant: `CISCO_WSM`  
N/A | `network.direction` | Constant: `BROADCAST`  
N/A | `network.ip_protocol` | Constant: `UDP`  
N/A | `security_result.description` | Constant: `The system has detected an orphaned ARP packet`  
N/A | `security_result.severity` | Constant: `ALERT`  
N/A | `security_result.severity_details` | Constant: `System unusable`  
N/A | `security_result.summary` | Constant: `ARP request received with invalid Source IP Address`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-wsm-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
