---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/steelhead/
title: Collect Riverbed SteelHead logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:59.873253+00:00
---

# Collect Riverbed SteelHead logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/steelhead/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Riverbed SteelHead logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Riverbed SteelHead logs to Google Security Operations using the Bindplane agent.

Riverbed SteelHead is a WAN optimization appliance for accelerating application performance across wide area networks. The parser extracts fields from SteelHead log entries and maps them to the Unified Data Model (UDM), capturing network flow details, authentication events, security results, and system metadata.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Riverbed SteelHead appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Riverbed SteelHead Management Console with administrator permissions



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
          chronicle/steelhead:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: STEELHEAD
            raw_log_field: body
        
        service:
          pipelines:
            logs/steelhead:
              receivers:
                - udplog
              exporters:
                - chronicle/steelhead
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `udplog`: The receiver type based on protocol: 
      * `udplog` for UDP syslog
      * `tcplog` for TCP syslog
      * `syslog` for RFC 3164/5424 syslog
    * `0.0.0.0`: IP address to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Specific IP address to listen on one interface
    * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)
  * **Exporter configuration:**

    * `<customer_id>`: Customer ID from the earlier step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * Adjust the `creds_file_path` to the path of your service account JSON key file (Option 1), depending on the platform: 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/steelhead:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: STEELHEAD
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
             




## Configure Riverbed SteelHead syslog forwarding

  1. Sign in to the **SteelHead Management Console**.
  2. Go to **Administration > System Settings > Logging**.
  3. Scroll to the **Remote Syslog** section.
  4. Click **Add** to add a new remote syslog server.
  5. Provide the following configuration details: 
     * **Server IP Address** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (must match the Bindplane receiver port).
     * **Protocol** : Select **UDP** (must match the Bindplane receiver type).
  6. Click **Apply**.

**Note:** SteelHead also supports TCP and TLS for syslog transport. If you select TCP or TLS, update the Bindplane receiver type accordingly (`tcplog` for TCP).



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
ephemeral_id_label, request_consumer_chain_label, sport_label, event_id_label, port_label, transport_label, sock_label, id_label, remote_inner_port_label, lport_label, rport_label, outer_lport_label, sfe_port_label, cfe_port_label, configuration_parameters_label, response_consumer_chain_label, client_connected_label, sportid_label, storeid_label, wan_tos_label, lan_tos_label, lan_classid_label, wan_classid_label, lan_classid_ingress_label, wan_classid_ingress_label, irm_region_label, irm_site_label, irm_environment_label, tag_labels | additional.fields | Merged from various label fields  
auth_mechanism | extensions.auth.mechanism | Set to "LOCAL" based on conditions  
| extensions.auth.type | Set to "TACACS" or "AUTHTYPE_UNSPECIFIED" based on conditions  
host.architecture | hardware.cpu_platform | Set to host.architecture  
intermediary, intermediary3 | intermediary | Merged from intermediary and intermediary3  
agent.type, agent.version | intermediary.application | Set to "%{agent.type} %{agent.version}"  
agent.type, agent.id | intermediary.asset_id | Set to "%{agent.type}: %{agent.id}"  
agent.name, inter_hostname | intermediary.hostname | Value from agent.name if not empty, else inter_hostname  
@createTimestamp | metadata.collected_timestamp | Copied from @createTimestamp  
descript, desc, description, netflow.tcp_control_flags | metadata.description | Value from descript if not empty, else desc, else description, else set to "TCP Control Flags: %{netflow.tcp_control_flags}"  
ts, log_timestamp | metadata.event_timestamp | Set from ts with date match if present, else from log_timestamp with date match  
| metadata.event_type | Set to "NETWORK_FLOW", then changed based on conditions  
logstash.ingest.timestamp | metadata.ingested_timestamp | Converted using date match from logstash.ingest.timestamp  
event_data | metadata.product_event_type | Set to event_data  
log_id | metadata.product_log_id | Set to log_id  
| metadata.product_name | Set to "Steelhead"  
| metadata.vendor_name | Set to "Riverbed"  
network.community_id | network.community_id | Set to network.community_id  
network.direction | network.direction | Set to uppercase network.direction if in [BROADCAST, INBOUND, OUTBOUND]  
response_code | network.http.response_code | Converted to integer from response_code  
network.transport | network.ip_protocol | Set to uppercase network.transport if not UNKNOWN  
network.bytes | network.sent_bytes | Converted to uinteger from network.bytes  
logstash.collect.host | observer.hostname | Set to logstash.collect.host if not an IP  
observer.ip, collect_ip | observer.ip | Value from observer.ip, merged with collect_ip if logstash.collect.host is IP  
observer.port | observer.port | Converted to integer from observer.port  
source.ip, log.source.address, src_ip, cfe_ip, principal_user | principal.asset.ip | Merged from various IP sources  
source.ip, log.source.address, src_ip, cfe_ip, principal_user | principal.ip | Merged from various IP sources  
src_mac | principal.mac | Set to src_mac  
source.port, src_port | principal.port | Converted to integer from source.port or src_port  
cmd_line | principal.process.command_line | Set to cmd_line  
user_name | principal.user.email_addresses | Set to user_name if matches email pattern  
user_name | principal.user.user_display_name | Set to user_name if not matches email pattern  
userid | principal.user.userid | Set to userid  
security_result | security_result | Merged from security_result  
event.category | security_result.category_details | Merged from event.category array  
sec_description | security_result.description | Set to sec_description  
syslog_severity | security_result.severity | Set to INFORMATIONAL if matches (?i)(DEFAULT|DEBUG|INFO|NOTICE), ERROR if (?i)ERROR, MEDIUM if (?i)WARNING, HIGH if (?i)(CRITICAL|ALERT|EMERGENCY)  
syslog_severity | security_result.severity_details | Set to syslog_severity  
hardware | target.asset.hardware | Merged from hardware  
hostname, host.hostname | target.asset.hostname | Value from hostname if not empty, else host.hostname  
destination.ip, target_ip, sfe_ip, ips | target.asset.ip | Merged from destination.ip, target_ip, sfe_ip, and host.ip array  
host.id | target.asset_id | Set to "Host Id: %{host.id}"  
hostname, host.hostname | target.hostname | Value from hostname if not empty, else host.hostname  
destination.ip, target_ip, sfe_ip, ips | target.ip | Merged from destination.ip, target_ip, sfe_ip, and host.ip array  
target_mac, macs | target.mac | Merged from target_mac and host.mac array  
host.os.platform | target.platform | Set to "LINUX" if host.os.platform matches (?i)centos, else set to uppercase host.os.platform  
host.os.kernel | target.platform_patch_level | Set to host.os.kernel  
host.os.version | target.platform_version | Set to host.os.version  
destination.port, target_port | target.port | Converted to integer from destination.port or target_port  
uri | target.url | Set to uri  
target_user | target.user.userid | Set to target_user  
`ts` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`desc` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`target_user` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`principal_ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/steelhead-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
