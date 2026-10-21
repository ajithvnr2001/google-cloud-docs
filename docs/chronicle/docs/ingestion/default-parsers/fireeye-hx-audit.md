---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-hx-audit/
title: Collect Trellix Endpoint Security (HX) Audit (formerly FireEye HX) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:07:27.687764+00:00
---

# Collect Trellix Endpoint Security (HX) Audit (formerly FireEye HX) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-hx-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trellix Endpoint Security (HX) Audit (formerly FireEye HX) logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Trellix Endpoint Security (HX) Audit (formerly known as FireEye HX) logs to Google Security Operations using Bindplane.

Trellix Endpoint Security (HX) provides endpoint detection and response capabilities with advanced threat hunting, forensics data collection, and behavioral analysis to detect and respond to advanced threats on endpoints using machine learning built from thousands of incident response engagements.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * Windows Server 2016 or later, or a Linux host with `systemd`.
  * Network connectivity between the Bindplane agent and Trellix Endpoint Security (HX) appliance.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Trellix Endpoint Security (HX) management console.
  * Administrative access to the Trellix Endpoint Security (HX) appliance CLI (SSH or console access).



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
         
         msiexec /i "[https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi](https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi)" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         

The service should show as **RUNNING**.




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         

The service should show as **active (running)**.




### Additional installation resources

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:** `/opt/observiq-otel-collector/config.yaml`
  * **Windows:** `C:\Program Files\observIQ OpenTelemetry Collector\config.yaml`



### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            tcplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/trellix_hx:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: 'YOUR_CUSTOMER_ID'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: FIREEYE_HX_AUDIT
                raw_log_field: body
                ingestion_labels:
                    env: production
                    source: trellix_hx
        
        service:
            pipelines:
                logs/trellix_hx_to_chronicle:
                    receivers:
                        - tcplog
                    exporters:
                        - chronicle/trellix_hx
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `tcplog`: TCP receiver is used because the Trellix Endpoint Security (HX) appliance CLI configures syslog forwarding over TCP protocol.
    * `listen_address`: IP address and port to listen on. Use `0.0.0.0:514` to listen on all interfaces on port **514** , or specify a different port such as `0.0.0.0:1514` if running as non-root on Linux.
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file: * **Linux** : `/etc/bindplane-agent/ingestion-auth.json` * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `YOUR_CUSTOMER_ID`: Your actual Customer ID from the previous step.
    * `endpoint`: Regional endpoint URL (e.g., `malachiteingestion-pa.googleapis.com`).
    * `log_type`: Must be exactly `FIREEYE_HX_AUDIT`.
    * `ingestion_labels`: Optional labels for organizing logs.



### Save the configuration file

After editing, save the file:

  * **Linux:** Press `Ctrl+O`, then `Enter`, then `Ctrl+X`.
  * **Windows:** Click **File > Save**.



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
         




## Configure Trellix Endpoint Security (HX) syslog forwarding

Trellix Endpoint Security (HX) supports two methods for forwarding logs: Event Streamer module for Windows Event Logs and CLI configuration for appliance logs in CEF format.

### Method 1: Configure Event Streamer for Windows Event Logs (UI)

  1. Sign in to the **Trellix Endpoint Security (HX)** management console.
  2. Go to **Event Streamer**.
  3. Select **Enable Event Streamer on the host**.
  4. Click **Save** to apply the policy changes.
  5. Go to **Destinations > Server settings > Add syslog destination**.
  6. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps-Collector`).
     * **IP address** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter the port number configured in the Bindplane agent (for example, `514`).
  7. Click **Save**.

**Note:** The Event Streamer module supports streaming System, Application Experience, Security, AppLocker, PowerShell, Application, Windows Defender, Task Scheduler, Print Service, and Terminal Services Windows event logs using RFC 5424 syslog format.

### Method 2: Configure appliance syslog forwarding (CLI)

  1. Sign in to the **Trellix Endpoint Security (HX)** appliance using **SSH** or console access.
  2. Run the following command to enter privileged mode: `enable`
  3. Run the following command to enter configuration mode: `configure terminal`
  4. Run the following command to verify current logging configuration: `show logging`
  5. Run the following commands to configure syslog forwarding:
         
         logging BINDPLANE_IP_ADDRESS trap none
         logging BINDPLANE_IP_ADDRESS trap override class cef priority info
         logging BINDPLANE_IP_ADDRESS protocol tcp
         

_Replace`BINDPLANE_IP_ADDRESS` with the IP address of the Bindplane agent host._

  6. Run the following command to enable **RFC-3339** timestamp format: `logging fields timestamp format rfc-3339`

  7. Run the following command to save the configuration: `write memory`

  8. Run the following command to exit: `exit`




### Enable Data Acquisition for event log collection

  1. Sign in to the **Trellix Endpoint Security (HX)** Web UI with admin access.
  2. Go to **Admin > Data Acquisition Scripts**.
  3. Click **Standard Investigative Details**.
  4. On the **Script Description** page, click **ACTIONS** and select **Edit**.
  5. Click **Event Logs**.
  6. Enable **Security logs** in the **Windows event logs** section.
  7. Click **Save**.



### Enable Auto Triage

  1. Sign in to the **Trellix Endpoint Security (HX)** Web UI with admin access.
  2. Go to **Admin > Triage Settings**.
  3. Toggle the **Triage Settings switch to ON**.
  4. Click **Save**.



### Enable File and Data Audits

  1. Sign in to the **Trellix Endpoint Security (HX)** Web UI with admin access.
  2. Go to **Admin > Policies**.
  3. Under **Configurations** , click **Audits - version number**.
  4. Turn on **Enable the File and Data Audits on the host**.
  5. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`alert.agent._id` | `principal.asset.asset_id` | Agent ID prefixed with **AGENT ID:**  
`alert.agent.url` | `principal.labels.value` | Agent URL value.  
`alert.condition._id` | `additional.fields.value.string_value` | Condition ID with **=** characters removed.  
`alert.condition.url` | `additional.fields.value.string_value` | Condition URL with **=** characters removed.  
`alert.decorators[].data.fireeye_report.indicator_verdict.malware_families.0` | `security_result.threat_name` | Malware family from FireEye report.  
`alert.decorators[].data.fireeye_report.risk_summary` | `security_result.description` | Risk summary description.  
`alert.decorators[].data.fireeye_verdict` | `security_result.severity_details` | FireEye verdict details.  
`alert.event_at` | `read_only_udm.metadata.event_timestamp` | Event timestamp mapping.  
`alert.event_id` | `read_only_udm.metadata.product_log_id` | Product log identifier.  
`alert.event_type` | `read_only_udm.metadata.product_event_type` | Product event type identifier.  
`alert.event_values.fileWriteEvent/fullPath` | `target.file.full_path` | Target file path.  
`alert.event_values.fileWriteEvent/md5` | `target.file.md5` | Target file MD5 hash.  
`alert.event_values.fileWriteEvent/pid` | `principal.process.pid` | Writing process PID.  
`alert.event_values.fileWriteEvent/processPath` | `principal.process.file.full_path` | Writing process file path.  
`alert.event_values.fileWriteEvent/size` | `target.file.size` | Target file size.  
`alert.event_values.fileWriteEvent/username` | `principal.user.userid` | Writing user identifier.  
`alert.event_values.ipv4NetworkEvent/localIP` | `principal.ip` | Principal local IP.  
`alert.event_values.ipv4NetworkEvent/localPort` | `principal.port` | Principal local port.  
`alert.event_values.ipv4NetworkEvent/protocol` | `network.ip_protocol` | Network IP protocol.  
`alert.event_values.ipv4NetworkEvent/remoteIP` | `target.ip` | Target remote IP.  
`alert.event_values.ipv4NetworkEvent/remotePort` | `target.port` | Target remote port.  
`alert.event_values.processEvent/md5` | `target.process.file.md5` | Target process MD5.  
`alert.event_values.processEvent/pid` | `target.process.pid` | Target process PID.  
`alert.event_values.urlMonitorEvent/hostname` | `target.hostname` | Target destination hostname.  
`alert.event_values.urlMonitorEvent/requestUrl` | `target.url` | Target request URL.  
`alert.event_values.urlMonitorEvent/urlMethod` | `network.http.method` | Network HTTP method.  
`alert.event_values.urlMonitorEvent/userAgent` | `network.http.user_agent` | Network HTTP user agent.  
`alert.indicator.name` | `read_only_udm.security_result.summary` | Security result summary.  
`host.agent_version` | `read_only_udm.metadata.product_version` | Product version mapping.  
`host.containment_state` | `read_only_udm.principal.containment_state` | Principal containment state.  
`host.hostname` | `read_only_udm.principal.hostname` | Principal hostname.  
`host.os.platform` | `read_only_udm.principal.platform` | Principal OS platform.  
`host.primary_ip_address` | `read_only_udm.principal.ip` | Principal primary IP.  
`severity` | `security_result.severity` | Mapped to **LOW** , **MEDIUM** , or **HIGH**.  
`timestamp` | `timestamp` | Raw log timestamp.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-hx-audit-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
