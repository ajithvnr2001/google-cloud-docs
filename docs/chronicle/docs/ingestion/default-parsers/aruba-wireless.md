---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-wireless/
title: Collect Aruba Wireless Controller and Access Point logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:10.959331+00:00
---

# Collect Aruba Wireless Controller and Access Point logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-wireless/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Aruba Wireless Controller and Access Point logs

**Parser Version:** 12.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Aruba Wireless Controller and Access Point logs to Google Security Operations using the Bindplane agent.

Aruba Wireless Controllers and Access Points generate syslog messages for wireless events, client associations, authentication, access control, and system operations. The parser processes syslog messages, extracting fields related to observer, intermediary, and access point details.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Aruba Wireless Controller
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to an Aruba Wireless Controller



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

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

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
          chronicle/aruba_wireless:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: ARUBA_WIRELESS
            raw_log_field: body
        
        service:
          pipelines:
            logs/aruba_wireless_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/aruba_wireless
        




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
          chronicle/aruba_wireless:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: ARUBA_WIRELESS
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
             




## Configure Aruba Wireless Controller and Access Point

  1. Sign in to the Aruba controller web UI.
  2. Go to the top menu and select **Configuration > System**.
  3. Select **Logging** to open the logging configuration page.
  4. In the **Syslog servers** section, click **\+ Add** to add a new syslog server.
  5. Enter the following details: 
     * **Name** : Enter a unique name for the syslog server; for example, `Google SecOps Syslog`.
     * **IP Address** : Enter the Bindplane IP address.
     * **Port** : Enter the Bindplane port number (typically `514` for UDP).
     * **Logging Facility** : Select **local 6** (commonly used for network devices).
     * **Logging Level** : Select **Informational** to capture information logs.
     * **Format** : Select **bsd-standard** format (this is the default syslog format used by Aruba controllers).
  6. Click **Submit** to save your settings.
  7. Click **Pending Changes**.
  8. Click **Deploy Changes** to apply the new syslog server configuration.

**Note:** After deploying the changes, configure the logging level for specific categories of logs.
  9. Go to the **Logging Level** settings and set the **Logging Level** to **Informational** for each of the following categories:

     * Network
     * All
     * Cluster
     * DHCP
     * GP
     * Mobility
     * Packet-Dump
     * SDN



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`Additional Info` | `read_only_udm.security_result.description` | The value of `Additional Info` from the raw log is mapped to the UDM field `security_result.description`.  
`AP` | `read_only_udm.target.hostname` | When present in the raw log, the value after `AP:` is extracted and mapped to the UDM field `target.hostname`.  
`BSSID` | `read_only_udm.target.mac`, `read_only_udm.principal.resource.name` (when resource type is BSSID) | The BSSID value from the raw log is mapped to `target.mac`. It's also used as the resource name when the `principal.resource.type` is `BSSID`.  
`COMMAND` | `read_only_udm.principal.process.command_line` | The command value from the raw log is mapped to the UDM field `principal.process.command_line`.  
`Dst-MAC` | `read_only_udm.target.mac` | When present, the Dst-MAC value from the raw log is mapped to the UDM field `target.mac`.  
`SERVER` | `read_only_udm.target.hostname` | When present, the server name from the raw log is mapped to the UDM field `target.hostname`.  
`SERVER-IP` | `read_only_udm.target.ip` | When present, the server IP from the raw log is mapped to the UDM field `target.ip`.  
`Src-MAC` | `read_only_udm.principal.mac` | When present, the Src-MAC value from the raw log is mapped to the UDM field `principal.mac`.  
`SSID` | `read_only_udm.target.resource.name` (when resource type is SSID) | The SSID value from the raw log is used as the resource name when the `target.resource.type` is `SSID`.  
`USER` | `read_only_udm.target.user.userid` | When present, the user ID from the raw log is mapped to the UDM field `target.user.userid`.  
`USERIP` | `read_only_udm.principal.ip`, `read_only_udm.observer.ip` | When present, the user IP from the raw log is mapped to the UDM field `principal.ip` and `observer.ip`.  
`USERMAC` | `read_only_udm.principal.mac` | When present, the user MAC from the raw log is mapped to the UDM field `principal.mac`.  
`USERNAME` | `read_only_udm.principal.user.userid` | When present, the username from the raw log is mapped to the UDM field `principal.user.userid`.  
`action` | `read_only_udm.security_result.action` | The action value from the raw log (e.g., `permit`, `deny`) is mapped to the UDM field `security_result.action`.  
`apname` | `read_only_udm.target.hostname` | When present, the AP name from the raw log is mapped to the UDM field `target.hostname`.  
`bssid` | `read_only_udm.target.mac` | When present, the BSSID value from the raw log is mapped to the UDM field `target.mac`.  
`collection_time.seconds` | `read_only_udm.metadata.event_timestamp.seconds` | The seconds value of the collection time from the raw log is mapped to the UDM field `metadata.event_timestamp.seconds`.  
`device_ip` | `read_only_udm.intermediary.ip` | The device IP from the raw log or from `logstash` is mapped to the UDM field `intermediary.ip`.  
`dstip` | `read_only_udm.target.ip` | When present, the destination IP from the raw log is mapped to the UDM field `target.ip`.  
`dstport` | `read_only_udm.target.port` | When present, the destination port from the raw log is mapped to the UDM field `target.port`.  
`event_id` | `read_only_udm.metadata.product_event_type` | The event ID from the raw log is used to construct the `metadata.product_event_type` field in the UDM, prefixed with `Event ID:`.  
`event_message` | `read_only_udm.security_result.summary` | The event message from the raw log is mapped to the UDM field `security_result.summary`.  
`log.source.address` | `read_only_udm.observer.ip` | The log source address is mapped to the UDM field `observer.ip`.  
`log_type` | `read_only_udm.metadata.log_type` | The log type from the raw log is mapped to the UDM field `metadata.log_type`.  
`logstash.collect.host` | `read_only_udm.observer.ip` or `read_only_udm.observer.hostname` | The logstash collect host is mapped to either `observer.ip` if it's an IP address, or `observer.hostname` if it's a hostname.  
`logstash.ingest.host` | `read_only_udm.intermediary.hostname` | The logstash ingest host is mapped to the UDM field `intermediary.hostname`.  
`logstash.process.host` | `read_only_udm.intermediary.hostname` | The logstash process host is mapped to the UDM field `intermediary.hostname`.  
`program` | `read_only_udm.target.application` | The program name from the raw log is mapped to the UDM field `target.application`.  
`serverip` | `read_only_udm.target.ip` | When present, the server IP from the raw log is mapped to the UDM field `target.ip`.  
`servername` | `read_only_udm.target.hostname` | When present, the server name from the raw log is mapped to the UDM field `target.hostname`.  
`srcip` | `read_only_udm.principal.ip` | When present, the source IP from the raw log is mapped to the UDM field `principal.ip`.  
`srcport` | `read_only_udm.principal.port` | When present, the source port from the raw log is mapped to the UDM field `principal.port`.  
`syslog_host` | `read_only_udm.intermediary.hostname` | The syslog host from the raw log is mapped to the UDM field `intermediary.hostname`.  
`timestamp` | `read_only_udm.metadata.event_timestamp` | The timestamp from the raw log is parsed and mapped to the UDM field `metadata.event_timestamp`.  
`userip` | `read_only_udm.principal.ip`, `read_only_udm.observer.ip` | When present, the user IP from the raw log is mapped to the UDM field `principal.ip` and `observer.ip`.  
`usermac` | `read_only_udm.principal.mac` | When present, the user MAC from the raw log is mapped to the UDM field `principal.mac`.  
`username` | `read_only_udm.principal.user.userid` | When present, the username from the raw log is mapped to the UDM field `principal.user.userid`. Derived from the `event_id` and logic within the parser. Determined by the parser based on the event ID and log message content. Hardcoded to `Wireless`. Hardcoded to `Aruba`. Determined by the parser based on the event ID and log message content. Determined by the parser based on the event ID and log message content. Extracted from the raw log message using regex. Determined by the parser based on the event ID and log message content. An empty object is added when the event_type is USER_LOGIN or a related authentication event. Determined by the parser based on the network protocol used in the event (e.g., TCP, UDP, ICMP, IGMP). Contains additional fields extracted from the raw log based on specific conditions. For example, the `ap_name` is added as a key-value pair when present. Set to `BSSID` when a BSSID is present in the principal's context. Set to `SSID` when an SSID is present in the target's context. Contains key-value pairs of relevant detection information extracted from the raw log, such as BSSID or SSID.  
`event_code` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`function_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`thread_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`station_macaddress` | `event.idm.read_only_udm.principal.mac` | Mapped from changelog  
`station_macaddress` | `event.idm.read_only_udm.principal.asset.mac` | Mapped from changelog  
`event_details` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`application` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`priority` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`module` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`instance` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`role` | `event.idm.read_only_udm.principal.user.attribute.roles.name` | Mapped from changelog  
`policy` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`command_status` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`p_host` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`p_host` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`p_host` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`p_host` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`t_user` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`p_ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`p_ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`cmd` | `event.idm.read_only_udm.target.process.command_line` | Mapped from changelog  
`node` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`principal_ip_value` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`p_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`t_hostname` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`details` | `metadata.description` | Mapped from changelog  
`ap_name` | `additional.fields` | Mapped from changelog  
`logstash.irm_site", "logstash.irm_environment", "logstash.irm_region` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-wireless-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
