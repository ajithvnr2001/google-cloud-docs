---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-sandbox/
title: Collect Fortinet FortiSandbox logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:43:25.868987+00:00
---

# Collect Fortinet FortiSandbox logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-sandbox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Fortinet FortiSandbox logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Fortinet FortiSandbox logs to Google Security Operations using the Bindplane agent.

Fortinet FortiSandbox is an advanced threat detection appliance that analyzes suspicious files and URLs in a sandboxed environment to detect zero-day malware and APTs. It generates syslog-formatted logs for sandbox analysis results, verdicts, system status, and behavioral indicators.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the FortiSandbox appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the FortiSandbox appliance with administrator permissions



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
            chronicle/fortisandbox:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: FORTINET_SANDBOX
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/fortisandbox_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/fortisandbox
        




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

    * `fortisandbox`: Descriptive name for the exporter
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `FORTINET_SANDBOX`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `fortisandbox_to_chronicle`: Descriptive name for the pipeline



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
             




## Configure Fortinet FortiSandbox syslog forwarding

  1. Sign in to the **FortiSandbox** web interface.
  2. Go to **Log & Report > Log Servers**.
  3. Click **Add** to create a new log server entry.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Chronicle-Bindplane`).
     * **IP Address** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (must match the Bindplane agent receiver port).
     * **Protocol** : Select **UDP**.
  5. Select the log types to forward: 
     * Sandbox analysis results
     * Malware verdicts
     * System events
     * Administrative actions
  6. Click **OK** to save the configuration.
  7. Verify that syslog messages are being received by checking the Bindplane agent logs.

**Note:** FortiSandbox outputs syslog-formatted logs. Ensure the port and protocol match the Bindplane agent receiver configuration.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
letype, logver, reason, cpu, mem, disk, pending, cpu_usage, mem_usage, disk_usage, pending_jobs | additional.fields | Merged as labels from each field if not empty  
msg | metadata.description | Value copied directly  
Time | metadata.event_timestamp | Converted to timestamp using ISO8601 format  
| metadata.event_type | Set to "USER_LOGOUT" if msg contains "session timeout", else "NETWORK_CONNECTION" if has_principal is "true" and has_target is "true", else "STATUS_UPDATE" if has_principal is "true", else "GENERIC_EVENT"  
logid | metadata.product_log_id | Value copied directly  
admin | principal.administrative_domain | Value copied directly  
devhost | principal.asset.hostname | Value copied directly  
principal_ip, msg_ip | principal.asset.ip | Value from principal_ip if not empty, else msg_ip  
devid | principal.asset.product_object_id | Value copied directly  
devhost | principal.hostname | Value copied directly  
principal_ip, msg_ip | principal.ip | Value from principal_ip if not empty, else msg_ip  
action | security_result.action_details | Value copied directly  
status, ui | security_result.detection_fields | Merged as labels from status and ui if not empty  
level | security_result.severity | Mapped from level after uppercasing: CRITICAL if "CRITICAL", ERROR if "ERROR", HIGH if "ALERT" or "EMERGENCY", INFORMATIONAL if "INFO" or "NOTICE", LOW if "DEBUG", MEDIUM if "WARNING", UNKNOWN_SEVERITY otherwise  
ip | target.asset.ip | Value copied directly  
ip | target.ip | Value copied directly  
user | target.user.userid | Value copied directly  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-sandbox-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
