---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-vpn/
title: Collect F5 VPN logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:04:38.445228+00:00
---

# Collect F5 VPN logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-vpn/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect F5 VPN logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest F5 VPN logs to Google Security Operations using the Bindplane agent.

F5 BIG-IP Access Policy Manager (APM) is a VPN and access management solution that generates syslog messages for user authentication, session management, policy evaluation, tunnel establishment, and network access events. The parser extracts fields from syslog-formatted logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the F5 BIG-IP appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to F5 BIG-IP tmsh (version 11.x or later)



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
            chronicle/f5_vpn:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: F5_VPN
                raw_log_field: body
        
        service:
            pipelines:
                logs/f5_vpn_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/f5_vpn
        




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
             




## Configure syslog forwarding on F5 BIG-IP APM

  1. Connect to the **F5 BIG-IP** command line.
  2. Open the **tmsh** shell:
         
         tmsh
         

  3. Configure a remote syslog server by running the following command:
         
         modify sys syslog remote-servers add { <Name> { host <bindplane-ip> remote-port <bindplane-port> } }
         

Replace the following:

     * `<Name>`: A unique name for this syslog destination (for example, `bindplane_server`).
     * `<bindplane-ip>`: The IP address of the Bindplane agent host.
     * `<bindplane-port>`: The port configured in the Bindplane agent receiver (default: `514`).
  4. Save the configuration:
         
         save sys config partitions all
         




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`cmd_data` | `principal.process.command_line` | The value is extracted from the msg field  
`errdefs_msgno` | `additional.fields.errdefs_msgno.string_value` | The value is extracted from the msg field  
`event_time` | `metadata.event_timestamp` | The value is parsed and converted to a timestamp  
`hostname` | `principal.hostname,`, `observer.hostname,`, `principal.asset.hostname,`, `observer.asset.hostname,` | The value is extracted from the message field and used to populate the hostname fields in the UDM. Also used to populate the hostip field  
`msg` | `security_result.description` | The value is extracted from the message field and used to populate the description field in the security_result object  
`prin_ip` | `principal.ip,`, `principal.asset.ip` | The value is extracted from the message field and used to populate the IP address fields in the UDM  
| `additional.fields.Canonical_Info.string_value` | The value is derived from the log message  
| `additional.fields.IDP.string_value` | The value is derived from the log message  
| `additional.fields.Plugin_Support.string_value` | The value is derived from the log message  
| `additional.fields.SMB`, `Stage.string_value` | The value is derived from the log message  
| `additional.fields.SP.string_value` | The value is derived from the log message  
| `additional.fields.Timezone.string_value` | The value is derived from the log message  
| `additional.fields.Tunnel`, `Type.string_value` | The value is derived from the log message  
| `additional.fields.UI_Mode.string_value` | The value is derived from the log message  
| `additional.fields.Version.string_value` | The value is derived from the log message  
| `additional.fields.from_rule_item.string_value` | The value is derived from the log message  
| `additional.fields.policy_result.string_value` | The value is derived from the log message  
| `additional.fields.ppp_id.string_value` | The value is derived from the log message  
| `additional.fields.resource.string_value` | The value is derived from the log message  
| `additional.fields.rule.string_value` | The value is derived from the log message  
| `additional.fields.server_vip_ip.string_value` | The value is derived from the log message  
| `additional.fields.server_vip_name.string_value` | The value is derived from the log message  
| `additional.fields.to_rule_item.string_value` | The value is derived from the log message  
| `additional.fields.tunnel_resource.string_value` | The value is derived from the log message  
| `metadata.description` | The value is derived from the log message  
| `metadata.event_type` | The value is hardcoded in the parser code for some events and is derived from the log message for others  
| `metadata.log_type` | The value is set to the batch type  
| `metadata.product_event_type` | The value is derived from the log message  
| `metadata.product_name` | The value is hardcoded in the parser code  
| `metadata.vendor_name` | The value is hardcoded in the parser code  
| `network.application_protocol` | The value is derived from the log message  
| `network.direction` | The value is derived from the log message  
| `network.http.method` | The value is derived from the log message  
| `network.http.parsed_user_agent` | The value is derived from the network.http.user_agent field  
| `network.http.referral_url` | The value is derived from the log message  
| `network.http.response_code` | The value is derived from the log message  
| `network.http.user_agent` | The value is derived from the log message  
| `network.ip_protocol` | The value is derived from the log message  
| `network.received_bytes` | The value is derived from the log message  
| `network.sent_bytes` | The value is derived from the log message  
| `network.session_id` | The value is derived from the log message  
| `network.tls.cipher` | The value is derived from the log message  
| `network.tls.version` | The value is derived from the log message  
| `observer.asset.hostname` | The value is set to the hostname field  
| `observer.asset.ip` | The value is set to the hostip field  
| `observer.hostname` | The value is set to the hostname field  
| `observer.ip` | The value is set to the hostip field  
| `principal.application` | The value is derived from the log message  
| `principal.asset.hostname` | The value is set to the hostname field  
| `principal.asset.ip` | The value is set to the hostip field or prin_ip field if it exists  
| `principal.asset.product_object_id` | The value is derived from the log message  
| `principal.hostname` | The value is set to the hostname field  
| `principal.ip` | The value is set to the hostip field or prin_ip field if it exists  
| `principal.location.country_or_region` | The value is derived from the log message  
| `principal.platform` | The value is derived from the log message  
| `principal.port` | The value is derived from the log message  
| `principal.process.command_line` | The value is derived from the log message  
| `principal.process.pid` | The value is derived from the log message  
| `principal.resource.name` | The value is derived from the log message  
| `principal.resource.type` | The value is hardcoded in the parser code for some events and is derived from the log message for others  
| `principal.user.email_addresses` | The value is derived from the log message  
| `principal.user.userid` | The value is derived from the log message  
| `security_result.action` | The value is derived from the log message  
| `security_result.description` | The value is derived from the log message  
| `security_result.rule_name` | The value is derived from the log message  
| `security_result.severity` | The value is derived from the log message  
| `security_result.severity_details` | The value is derived from the log message  
| `security_result.summary` | The value is derived from the log message  
| `src.ip` | The value is derived from the log message  
| `src.location.country_or_region` | The value is derived from the log message  
| `src.port` | The value is derived from the log message  
| `target.asset.hostname` | The value is derived from the log message  
| `target.asset.ip` | The value is derived from the log message  
| `target.hostname` | The value is derived from the log message  
| `target.ip` | The value is derived from the log message  
| `target.port` | The value is derived from the log message  
| `target.process.command_line` | The value is derived from the log message  
| `target.process.pid` | The value is derived from the log message  
| `target.resource.id` | The value is derived from the log message  
| `target.url` | The value is derived from the log message  
| `target.user.userid` | The value is derived from the log message  
`Hostname` | `target.hostname` | Mapped from changelog  
`sess_id` | `network.session_id` | Mapped from changelog  
`internal_ip` | `target.ip` | Mapped from changelog  
`file_path` | `principal.resource.name` | Mapped from changelog  
`useragent` | `network.http.user_agent` | Mapped from changelog  
`User-Agent" and "useragent` | `network.http.parsed_user_agent` | Mapped from changelog  
`username` | `target.user.userid` | Mapped from changelog  
`sid` | `target.user.windows_sid` | Mapped from changelog  
`bytes_out` | `network.sent_bytes` | Mapped from changelog  
`bytes_in` | `network.received_bytes` | Mapped from changelog  
`Platform` | `principal.platform` | Mapped from changelog  
`Platform_Version` | `principal.platform_version` | Mapped from changelog  
`Javascript_Support", "ActiveX_Support", "Plugin_Support", "Version", "Model", "CPU", "UI_Mode", "SP", "IDP", "to_rule_item", "from_rule_item", "policy_result", "rule", "resource", "ppp_id", "tunnel_resource", "server_vip_ip", "server_vip_name", and "Canonical_Info` | `additional.fields` | Mapped from changelog  
`uri_path` | `target.url` | Mapped from changelog  
`User-Agent` | `network.http.user_agent` | Mapped from changelog  
`s_ip` | `src.ip` | Mapped from changelog  
`t_ip` | `target.ip` | Mapped from changelog  
`t_port` | `target.port` | Mapped from changelog  
`s_nat_ip` | `target.nat_ip` | Mapped from changelog  
`cipher_name` | `network.tls.cipher` | Mapped from changelog  
`tls_version` | `network.tls.version` | Mapped from changelog  
`resource_id` | `target.resource.id` | Mapped from changelog  
`src_ip` | `principal.ip` | Mapped from changelog  
`status` | `network.http.response_code` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-vpn-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
