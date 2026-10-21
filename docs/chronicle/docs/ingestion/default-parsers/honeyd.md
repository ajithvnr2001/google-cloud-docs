---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/honeyd/
title: Collect Honeyd logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:35:12.329564+00:00
---

# Collect Honeyd logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/honeyd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Honeyd logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Honeyd logs to Google Security Operations using the Bindplane agent.

Honeyd is an open-source honeypot framework that simulates virtual hosts to detect unauthorized access and network scanning. It generates logs for connection attempts, port scans, and attacker interactions with honeypot services.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Honeyd host
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * A running Honeyd deployment with logging enabled



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where Bindplane will be installed.

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
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/honeyd:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: HONEYD
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/honeyd_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/honeyd
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `udplog`: The receiver type based on protocol: 
      * `udplog` for UDP syslog
      * `tcplog` for TCP syslog
    * `0.0.0.0`: IP address to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Specific IP address to listen on one interface
    * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)
  * **Exporter configuration:**

    * `honeyd`: Descriptive name for the exporter
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `HONEYD`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `honeyd_to_chronicle`: Descriptive name for the pipeline



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
             




## Configure Honeyd syslog forwarding

Honeyd writes connection and interaction logs to local files. To forward these logs using syslog to the Bindplane agent, configure rsyslog on the Honeyd host.

  1. Sign in to the Honeyd host with root or sudo privileges.
  2. Identify the Honeyd log file location. By default, Honeyd logs to the path specified with the `-l` flag at startup (for example, `/var/log/honeyd/honeyd.log`).
  3. Create an rsyslog configuration file to forward Honeyd logs:
         
         sudo nano /etc/rsyslog.d/honeyd-forward.conf
         

  4. Add the following configuration:
         
         module(load="imfile")
         input(type="imfile"
             File="/var/log/honeyd/honeyd.log"
             Tag="honeyd:"
             Severity="info"
             Facility="local6")
         local6.* @<BINDPLANE_AGENT_IP>:514
         

     * Replace `<BINDPLANE_AGENT_IP>` with the IP address of the Bindplane agent host.
     * Replace `/var/log/honeyd/honeyd.log` with the actual path to your Honeyd log file.
     * Use `@@` instead of `@` for TCP forwarding (must match the Bindplane agent receiver type).
  5. Restart rsyslog to apply the changes:
         
         sudo systemctl restart rsyslog
         

  6. Verify that syslog messages are being received by checking the Bindplane agent logs.

**Note:** If Honeyd and the Bindplane agent run on the same host, you can configure the Bindplane agent to read the log file directly using a filelog receiver instead of syslog.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
comment | metadata.event_type | Set to "NETWORK_HTTP" if network.application_protocol in ["HTTP","HTTPS"]; "NETWORK_FTP" if dst_port == "21"; "NETWORK_SMTP" if dst_port == "25"; else "NETWORK_CONNECTION"  
| metadata.product_name | Set to "Honeyd"  
| metadata.vendor_name | Set to "Niels Provos"  
dst_port | network.application_protocol | Set to "UNKNOWN_APPLICATION_PROTOCOL", then updated to app_protocol_output derived from dst_port if dst_port present and app_protocol_output not empty  
protocol | network.ip_protocol | Converted from protocol_number_src (protocol) using ip_protocol_out mapping  
received_bytes | network.received_bytes | Set to received_bytes if type == "E", converted to uinteger  
sent_bytes | network.sent_bytes | Set to sent_bytes if type == "E" or protocol == "1", converted to uinteger  
src_ip | principal.asset.ip | Value copied directly  
src_ip | principal.ip | Value copied directly  
src_port | principal.port | Value copied directly, converted to integer  
dst_ip | target.asset.ip | Value copied directly  
dst_ip | target.ip | Value copied directly  
comment | target.platform | Set to "WINDOWS" if matches (?i)WINDOWS; "LINUX" if matches (?i)LINUX  
comment | target.platform_patch_level | Extracted from comment using grok pattern  
comment | target.platform_version | Extracted from comment using grok pattern  
dst_port | target.port | Value copied directly, converted to integer  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/honeyd-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
