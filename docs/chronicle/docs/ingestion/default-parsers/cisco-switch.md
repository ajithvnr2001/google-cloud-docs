---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-switch/
title: Collect Cisco switch logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:34.055122+00:00
---

# Collect Cisco switch logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-switch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco switch logs

**Parser Version:** 27.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco switch logs to Google Security Operations using the Bindplane agent.

Cisco switches generate syslog messages for port state changes, spanning tree events, ACL matches, authentication, and system operations. The parser extracts fields using grok patterns and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Cisco switch
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Cisco switch CLI



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
          chronicle/cisco_switch:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: CISCO_SWITCH
            raw_log_field: body
        
        service:
          pipelines:
            logs/cisco_switch_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/cisco_switch
        




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
          chronicle/cisco_switch:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CISCO_SWITCH
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
           
           ```bash
           sudo systemctl status observiq-otel-collector
           ```
           

    2. Check logs for errors:
           
           ```bash
           sudo journalctl -u observiq-otel-collector -f
           ```
           

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
             




## Configure syslog on a Cisco switch

  1. Sign in to the Cisco Switch.
  2. Escalate privileges:
         
         enable
         

  3. Switch to configuration mode:
         
         conf t
         

  4. Configure syslog:
         
         logging host <BINDPLANE_IP> transport <tcp/udp> port <PORT>
         logging source-interface <INTERFACE>
         

     * Replace `<BINDPLANE_IP>` with the Bindplane agent IP address.
     * Replace `<tcp/udp>` with the configured listening protocol (for example, `udp`).
     * Replace `<INTERFACE>` with the Cisco interface ID.
  5. Set the priority level:
         
         logging trap Informational
         logging console Informational
         logging severity Informational
         

  6. Set the syslog facility:
         
         logging facility local6
         

  7. Enable timestamps:
         
         service timestamps log datetime
         

  8. Save and exit.

  9. Save the configuration to survive restart:
         
         copy running-config startup-config
         




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
action | security_result.action_details | Value of this field is derived from the `action` field in the raw log.  
day |  |   
description | metadata.description | Value of this field is derived from the `description` field in the raw log.  
description | security_result.description | Value of this field is derived from the `description` field in the raw log.  
destination_ip | target.asset.ip | Value of this field is derived from the `destination_ip` field in the raw log.  
destination_ip | target.ip | Value of this field is derived from the `destination_ip` field in the raw log.  
destination_port | target.port | Value of this field is derived from the `destination_port` field in the raw log.  
device | principal.asset.hostname | Value of this field is derived from the `device` field in the raw log.  
device | principal.hostname | Value of this field is derived from the `device` field in the raw log.  
device | target.asset.hostname | Value of this field is derived from the `device` field in the raw log.  
device | target.hostname | Value of this field is derived from the `device` field in the raw log.  
device_ip | principal.asset.ip | Value of this field is derived from the `device_ip` field in the raw log.  
device_ip | principal.ip | Value of this field is derived from the `device_ip` field in the raw log.  
device_ip | target.asset.ip | Value of this field is derived from the `device_ip` field in the raw log.  
device_ip | target.ip | Value of this field is derived from the `device_ip` field in the raw log.  
facility | principal.resource.type | Value of this field is derived from the `facility` field in the raw log.  
header_data | metadata.product_log_id | Value of this field is derived from the `header_data` field in the raw log.  
header_data | target.asset.ip | Value of this field is derived from the `header_data` field in the raw log.  
header_data | target.ip | Value of this field is derived from the `header_data` field in the raw log.  
hostname | principal.asset.hostname | Value of this field is derived from the `hostname` field in the raw log.  
hostname | principal.hostname | Value of this field is derived from the `hostname` field in the raw log.  
ip | principal.asset.ip | Value of this field is derived from the `ip` field in the raw log.  
ip | principal.ip | Value of this field is derived from the `ip` field in the raw log.  
ip_address | principal.asset.ip | Value of this field is derived from the `ip_address` field in the raw log.  
ip_address | principal.ip | Value of this field is derived from the `ip_address` field in the raw log.  
ip_protocol | network.ip_protocol | Value of this field is derived from the `ip_protocol` field in the raw log.  
mac | principal.mac | Value of this field is derived from the `mac` field in the raw log.  
mnemonic | network.dhcp.opcode | Value of this field is derived from the `mnemonic` field in the raw log.  
mnemonic | metadata.product_event_type | Value of this field is derived from the `mnemonic` field in the raw log.  
month |  |   
p_ip | principal.asset.ip | Value of this field is derived from the `p_ip` field in the raw log.  
p_ip | principal.ip | Value of this field is derived from the `p_ip` field in the raw log.  
port | target.port | Value of this field is derived from the `port` field in the raw log.  
priority |  |   
protocol | network.ip_protocol | Value of this field is derived from the `protocol` field in the raw log.  
reason |  |   
rule | security_result.rule_id | Value of this field is derived from the `rule` field in the raw log.  
sec_result_action | security_result.action | Value of this field is derived from the `sec_result_action` field in the raw log.  
severity |  |   
source | principal.asset.ip | Value of this field is derived from the `source` field in the raw log.  
source | principal.ip | Value of this field is derived from the `source` field in the raw log.  
source_ip | network.dhcp.ciaddr | Value of this field is derived from the `source_ip` field in the raw log.  
source_ip | principal.asset.ip | Value of this field is derived from the `source_ip` field in the raw log.  
source_ip | principal.ip | Value of this field is derived from the `source_ip` field in the raw log.  
source_mac | network.dhcp.chaddr | Value of this field is derived from the `source_mac` field in the raw log.  
source_port | principal.port | Value of this field is derived from the `source_port` field in the raw log.  
summary | security_result.summary | Value of this field is derived from the `summary` field in the raw log.  
time |  |   
timezone |  |   
user | principal.user.userid | Value of this field is derived from the `user` field in the raw log.  
user | target.user.userid | Value of this field is derived from the `user` field in the raw log.  
when |  |   
year |  |   
| extensions.auth.type | MACHINE  
| metadata.log_type | CISCO_SWITCH  
| metadata.vendor_name | Cisco  
| metadata.product_name | Cisco Switch  
| network.application_protocol | DHCP  
| network.dhcp.type | REQUEST  
`intermediary_ip` | `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
`priority` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`product_log_id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`_time` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`vlan_data` | `event.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`intermediary_ip` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`intermediary_ip` | `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
`time_stamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`process_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`switch_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`log_seq_num` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`log_seq_num_2` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`p_interface` | `event.idm.read_only_udm.principal.resource.name` | Mapped from changelog  
`audit_session_id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`mac` | `event.idm.read_only_udm.principal.mac` | Mapped from changelog  
`packets` | `event.idm.read_only_udm.network.sent_packets` | Mapped from changelog  
`facility` | `event.idm.read_only_udm.principal.resource.resource_subtype` | Mapped from changelog  
`seq_num` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`device_hostname` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`id` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`seq_num` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`log_message` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`syslog_tag` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog_pri` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`appcat` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`applist` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dstintf` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dstintfrole` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`mastersrcmac` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`osname` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`poluuid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`service` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`srchwvendor` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`srcintf` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`srcintfrole` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`srcserver` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`transport` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`trandisp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vd` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vwlid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`devid` | `event.idm.read_only_udm.intermediary.asset.product_object_id` | Mapped from changelog  
`devname` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`logid` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`subtype` | `event.idm.read_only_udm.network.direction` | Mapped from changelog  
`proto` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`rcvdbyte` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`sentbyte` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`sentpkt` | `event.idm.read_only_udm.network.sent_packets` | Mapped from changelog  
`duration` | `event.idm.read_only_udm.network.session_duration.seconds` | Mapped from changelog  
`sessionid` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`srcname` | `event.idm.read_only_udm.principal.asset.hostname`, `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`srcip` | `event.idm.read_only_udm.principal.asset.ip`, `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`srcmac` | `event.idm.read_only_udm.principal.asset.mac`, `event.idm.read_only_udm.principal.mac` | Mapped from changelog  
`osname` | `event.idm.read_only_udm.principal.asset.platform_software.platform` | Mapped from changelog  
`srcswversion` | `event.idm.read_only_udm.principal.asset.platform_software.platform_version` | Mapped from changelog  
`srccountry` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`transip` | `event.idm.read_only_udm.principal.nat_ip` | Mapped from changelog  
`srcport` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`action` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`policyid` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`policyname` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`policytype` | `event.idm.read_only_udm.security_result.rule_type` | Mapped from changelog  
`level` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`action` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`dstip` | `event.idm.read_only_udm.target.asset.ip`, `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`dstcountry` | `event.idm.read_only_udm.target.location.country_or_region` | Mapped from changelog  
`dstport` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`device` | `principle.hostname` | Mapped from changelog  
`username3` | `principal.user.userid` | Mapped from changelog  
`login_status` | `security_result.summary` | Mapped from changelog  
`ecs.version` | `metadata.product_version` | Mapped from changelog  
`fileset.name", "flow.locality", "flow.id", "input.type", "netflow.exporter.source_id", and "netflow.exporter.uptime_millis` | `additional.fields` | Mapped from changelog  
`network.transport` | `network.ip_protocol` | Mapped from changelog  
`netflow.post_nat_source_ipv4_address` | `principal.ip` | Mapped from changelog  
`netflow.source_transport_port` | `principal.port` | Mapped from changelog  
`network.direction` | `network.direction` | Mapped from changelog  
`intermediary_ip` | `intermediary.ip` | Mapped from changelog  
`intermediary_hostname` | `intermediary.hostname` | Mapped from changelog  
`principal_host` | `principal.hostname` | Mapped from changelog  
`src_mac` | `principal.mac` | Mapped from changelog  
`eventSummary` | `metadata.product_event_type` | Mapped from changelog  
`error_msg` | `security_result.detection_fields` | Mapped from changelog  
`pid` | `principal.process.pid` | Mapped from changelog  
`srcPort` | `principal.port` | Mapped from changelog  
`srcUser` | `principal.user.userid` | Mapped from changelog  
`username1` | `target.user.userid` | Mapped from changelog  
`command` | `target.process.command_line` | Mapped from changelog  
`PWD` | `target.process.file.full_path` | Mapped from changelog  
`node_id", "cluster_id", "exception", "UniqueId", and "app_id` | `additional.fields` | Mapped from changelog  
`DEVICE` | `principal.mac` | Mapped from changelog  
`SRC` | `principal.ip` | Mapped from changelog  
`SPT` | `principal.port` | Mapped from changelog  
`DST` | `target.ip` | Mapped from changelog  
`DPT` | `target.port` | Mapped from changelog  
`ID` | `network.session_id` | Mapped from changelog  
`LEN` | `network.session_duration.seconds` | Mapped from changelog  
`PROTO` | `network.ip_protocol` | Mapped from changelog  
`IN", "OUT", "PHYSIN", "WINDOW", "RES, "TOS", "PREC", "TTL" ,"URGP", "MAC", "radio", "vap", "auth_type", "sugg_band", "ssid_id", "ssid_profile_name" and "protocol` | `additional.fields` | Mapped from changelog  
`client_mac` | `principal.mac` | Mapped from changelog  
`aid` | `network.session_id` | Mapped from changelog  
`rssi` | `intermediary.asset.product_object_id` | Mapped from changelog  
`channel` | `security_result.detection_fields` | Mapped from changelog  
`eventSummary", "dhcp_ip", "client_mac", "aid" and "ip_src` | `metadata.product_event_type` | Mapped from changelog  
`mac", "src", "sport", "dst", "dport", "action", "protocol", "url" and "signature` | `principal.mac` | Mapped from changelog  
`metadata.event_type" and "extensions.auth.type` | `USER_LOGIN` | Mapped from changelog  
`eventSummary", "aid", "rssi", "channel", "last_known_client_ip" and "event_type` | `security_result.summary` | Mapped from changelog  
`pid` | `target.process.pid` | Mapped from changelog  
`app_name` | `target.application` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-switch-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
