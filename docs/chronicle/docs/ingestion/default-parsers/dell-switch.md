---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-switch/
title: Collect Dell switch logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:46:52.551014+00:00
---

# Collect Dell switch logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-switch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Dell switch logs

**Parser Version:** 11.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Dell switch logs to Google Security Operations using the Bindplane agent.

This parser extracts Dell switch logs, normalizes timestamps, and uses grok patterns to structure the log message into key-value pairs. It then maps these extracted fields to the Unified Data Model (UDM), handling various log formats and enriching the data with contextual information such as asset details and security severity.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Dell switch
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * An active connection and administrative credentials for a Dell switch



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
            chronicle/dell_switch:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: DELL_SWITCH
                raw_log_field: body
        
        service:
            pipelines:
                logs/dell_switch_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/dell_switch
        




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
             




## Configure syslog export from a Dell switch

  1. Connect to the Dell switch using SSH or the console port.
  2. Sign in with administrative credentials.
  3. Use the following command to specify the IP address or hostname of the syslog server (replace `<syslog-server-ip>`, `<udp|tcp>`, and `<syslog-port-number>` with the actual details):
         
         logging host <syslog-server-ip> transport <udp|tcp> port <syslog-port-number>
         

  4. Optional: Define the minimum severity level for messages to be sent to the syslog server. For example, to log informational messages and above:
         
         logging level informational
         

  5. Save the **running configuration** to the **startup configuration** to ensure changes persist across reboots:
         
         copy running-config startup-config
         

  6. Save the configuration:
         
         write memory
         




## Supported Dell Switch sample logs

  * **SYSLOG**
        
        {
          "priority": 165,
          "version": 1,
          "timestamp": "2023-10-12T12:37:17.249566+00:00",
          "hostname": "switch-lon-01",
          "app_name": "dn_alm",
          "proc_id": "940",
          "message": "Node.1-Unit.1:PRI [event], Dell EMC (OS10) %ALM_AUTH_EVENT: Authentication event was raised MESSAGE=pam_unix(sshd:session): session opened for user service_account by (uid=0)"
        }
        

  * **JSON**
        
        {
          "appname": "SNOOP",
          "facility": 23,
          "hostname": "access-switch-a1",
          "message": "snooping.c(2177) 70820228 %% DBG Report from intf Gi6/0/11 ignored -- no router ports on vlan 193",
          "priority": 191,
          "proc_id": "snoopTask"
        }
        

  * **KV / events format**
        
        Events: 
          Eventid        = {38812} 
          Occurrencetime = {3 Sept 2024 00:06:06} 
          Eventseverity  = {Minor} 
          Jobid          = {30506} 
          Computer       = {backup-server-01} 
          Program        = {DatabaseAgent} 
          Description    = {Block Change Tracking is found DISABLED on Oracle DB [PROD_DB]. Incremental backups may run slow.}
        

  * **Audit SYSLOG**
        
        {
            "priority": 110,
            "version": 1,
            "timestamp": "2023-12-12T00:58:26.893679+00:00",
            "hostname": "core-switch-palf",
            "app_name": ".clish",
            "proc_id": "29156",
            "message": "Node.1-Unit.1:PRI [audit], User sec_admin on /dev/pts/0 from 10.0.0.50 used cmd: 'terminal length 0' - completed"
        }
        

  * **SNMP trap / TRAPMGR format**
        
        {
          "priority": 189,
          "version": 1,
          "timestamp": "2023-12-28T23:37:27.394Z",
          "hostname": "dist-switch-01",
          "app_name": "TRAPMGR",
          "proc_id": "trapTask",
          "extensions": {
            "origin_ip": "192.168.1.1",
            "software": "N3000_Series",
            "swVersion": "6.3.2.3"
          },
          "message": "traputil.c(721) 1056839 %% Gi1/0/5 is transitioned from the Learning state to the Forwarding state"
        }
        




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
**`acct`** | **`principal.user.userid`** | Used as the **`userid`** if the **`user`** field is not present.  
**`addr`** | **`principal.asset.ip`** , **`principal.ip`** | Parsed as an IP address and used for the principal's IP and asset IP if it is a valid IP and different from the hostname.  
**`application`** | **`principal.application`** | Directly mapped.  
**`asset`** | **`principal.asset.attribute.labels.value`** | Directly mapped to the asset label value, with the key hardcoded as "Asset Name". If the asset field is empty and the message contains "Dell", the asset is set to "Dell".  
**`auid`** | **`principal.resource.attribute.labels.value`** | Directly mapped to a label with key **`auid`** within **`principal.resource.attribute.labels`**.  
**`datetime`** | **`metadata.event_timestamp`** | Parsed from various formats in the message field and converted to a timestamp.  
**`dest_ip`** | **`target.asset.ip`** , **`target.ip`** | Mapped to target IP and target asset IP.  
**`enterpriseId`** | **`principal.resource.attribute.labels.value`** | Mapped to a label with key **`enterpriseId`** within **`principal.resource.attribute.labels`**.  
**`exe`** | **`sec_result.detection_fields.value`** | Mapped to a detection field with key **`exe`**.  
**`File`** | **`target.file.full_path`** | Directly mapped.  
**`grantors`** | **`principal.resource.attribute.labels.value`** | Mapped to a label with key **`grantors`** within **`principal.resource.attribute.labels`**.  
**`host`** | **`principal.hostname`** , **`principal.asset.hostname`** , **`metadata.event_type`** | Used as principal hostname and asset hostname. If **`host`** is present, **`metadata.event_type`** is set to **`STATUS_UPDATE`**. If hostname is present but host is not, hostname is used as host.  
**`hostname`** | **`principal.asset.ip`** , **`principal.ip`** , **`host`** | If it is a valid IP, used for principal IP and asset IP. If **`host`** is empty, it is used as **`host`**.  
**`ID`** | **`principal.resource.attribute.labels.value`** | Mapped to a label with key **`ID`** within **`principal.resource.attribute.labels`**.  
**`ip`** | **`principal.asset.ip`** , **`principal.ip`** | Mapped to principal IP and asset IP.  
**`is_synced`** | **`sec_result.detection_fields.value`** | Mapped to a detection field with key **`is_synced`**.  
**`local`** | **`target.asset.ip`** , **`target.ip`** , **`target.port`** | Parsed to extract local IP and port, mapped to target IP, target asset IP, and target port.  
**`local_ip`** | **`target.asset.ip`** , **`target.ip`** | Extracted from the **`local`** field and mapped to target IP and target asset IP.  
**`local_port`** | **`target.port`** | Extracted from the **`local`** field and mapped to target port.  
**`mac`** | **`principal.mac`** | If it is a valid MAC address, mapped to principal MAC address.  
**`msg`** | **`metadata.description`** | Used as the event description if present. Also parsed for additional fields.  
**`msg1`** | **`metadata.description`** | Used as event description if **`msg2`** is not present.  
**`msg2`** | **`sec_result.description`** , **`metadata.event_type`** , **`extensions.auth.type`** | Used as security result description. If it contains "opened for user", event type is set to **`USER_LOGIN`** and auth type to **`MACHINE`**. If it contains "closed for user", event type is set to **`USER_LOGOUT`** and auth type to **`MACHINE`**.  
**`op`** | **`metadata.product_event_type`** | Used as product event type if present.  
**`pid`** | **`principal.process.pid`** | Directly mapped.  
**`port`** | **`principal.port`** | Directly mapped.  
**`prod_event_type`** | **`metadata.product_event_type`** | Used as product event type if present.  
**`res`** | **`sec_result.summary`** | Directly mapped.  
**`sec_description`** | **`sec_result.description`** , **`target.url`** , **`target.ip`** , **`target.asset.ip`** , **`sec_result.action_details`** | Parsed for target URL, IP, action details, and used as security result description.  
**`Server_ID`** | **`target.resource.product_object_id`** | Directly mapped.  
**`server`** | **`principal.asset.ip`** , **`principal.ip`** , **`principal.port`** | Parsed to extract server IP and port, mapped to principal IP, principal asset IP, and principal port.  
**`server_ip`** | **`principal.asset.ip`** , **`principal.ip`** | Extracted from the **`server`** field and mapped to principal IP and principal asset IP.  
**`server_port`** | **`principal.port`** | Extracted from the **`server`** field and mapped to principal port.  
**`ses`** | **`network.session_id`** | Directly mapped.  
**`severity`** | **`sec_result.severity`** , **`metadata.product_event_type`** | Used to determine security result severity and product event type based on specific values.  
**`software`** | **`principal.asset.software`** | Directly mapped.  
**`softwareName`** | **`software.name`** | Directly mapped.  
**`Status`** | **`sec_result.summary`** | Used as the security result summary if **`res`** is not present.  
**`subj`** | **`principal.resource.attribute.labels.value`** | Mapped to a label with key **`subj`** within **`principal.resource.attribute.labels`**.  
**`swVersion`** | **`software.version`** | Directly mapped.  
**`target_host`** | **`target.hostname`** , **`target.asset.hostname`** | Directly mapped to target hostname and target asset hostname.  
**`target_ip`** | **`target.asset.ip`** , **`target.ip`** | Directly mapped to target IP and target asset IP.  
**`target_url`** | **`target.url`** | Directly mapped.  
**`target_user_id`** | **`target.user.userid`** | Directly mapped.  
**`terminal`** | **`principal.resource.attribute.labels.value`** | Mapped to a label with key **`terminal`** within **`principal.resource.attribute.labels`**.  
**`tzknown`** | **`sec_result.detection_fields.value`** | Mapped to a detection field with key **`tzknown`**.  
**`uid`** | **`principal.resource.attribute.labels.value`** | Mapped to a label with key **`uid`** within **`principal.resource.attribute.labels`**.  
**`user`** | **`principal.user.userid`** , **`metadata.event_type`** | Used as principal user ID. If **`user`** is present, **`metadata.event_type`** is set to **`USER_UNCATEGORIZED`**.  
**`username`** | **`target.user.userid`** | Directly mapped to target user ID.  
N/A | **`metadata.vendor_name`** | Hardcoded to "Dell".  
N/A | **`metadata.product_name`** | Hardcoded to "Dell Switch".  
N/A | **`extensions.auth.type`** | Set to **`MACHINE`** for specific login/logout events.  
N/A | **`metadata.event_type`** | Determined by a complex logic based on various fields and conditions, defaults to **`GENERIC_EVENT`** if not set otherwise. Can be **`USER_LOGIN`** , **`USER_LOGOUT`** , **`USER_UNCATEGORIZED`** , **`NETWORK_CONNECTION`** , **`NETWORK_UNCATEGORIZED`** , **`STATUS_UPDATE`** , or **`GENERIC_EVENT`**.  
`reason_code` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Eventid` | `metadata.product_log_id` | Mapped from changelog  
`Eventseverity` | `security_result.severity` | Mapped from changelog  
`Computer` | `principal.hostname` | Mapped from changelog  
`Program` | `principal.application` | Mapped from changelog  
`Description` | `security_result.description` | Mapped from changelog  
`tzknown", "is_synced" and "exe` | `security_result.detection_fields` | Mapped from changelog  
`res` | `security_result.summary` | Mapped from changelog  
`status` | `security_result.summary` | Mapped from changelog  
`uid", "enterpriseId", "auid", "terminal", "subj", "grantors", and "ID` | `principal.resource.attribute.labels` | Mapped from changelog  
`sec_description` | `security_result.description` | Mapped from changelog  
`action_details` | `security_result.action_details` | Mapped from changelog  
`softwareName` | `principal.asset.software.name` | Mapped from changelog  
`swVersion` | `principal.asset.software.version` | Mapped from changelog  
`port` | `principal_port` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-switch-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
