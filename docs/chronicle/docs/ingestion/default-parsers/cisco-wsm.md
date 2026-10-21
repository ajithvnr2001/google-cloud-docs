---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wsm/
title: Collect Cisco WSM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:03:37.571035+00:00
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



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agent**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.



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
             compression: gzip
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             customer_id: '<customer_id>'
             endpoint: malachiteingestion-pa.googleapis.com
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
  * Replace `<customer_id>` with the actual customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the path where the authentication file was saved in the Get Google SecOps ingestion authentication file section.



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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
