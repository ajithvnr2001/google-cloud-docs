---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-nx-audit/
title: Collect Trellix Network Security Audit (formerly FireEye NX Audit) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:50.312831+00:00
---

# Collect Trellix Network Security Audit (formerly FireEye NX Audit) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-nx-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trellix Network Security Audit (formerly FireEye NX Audit) logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Trellix Network Security Audit (formerly known as FireEye NX Audit) logs to Google Security Operations using Bindplane.

Trellix Network Security is a network security appliance that detects and blocks attacks from the web, protecting against drive-by malware and highly targeted zero-day exploits. It leverages the Multi-Vector Virtual Execution (MVX) engine to identify malicious activity and command-and-control callbacks with extremely low false positive rates.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows Server 2016 or later, or a Linux host with `systemd`.
  * Network connectivity between the Bindplane agent and the FireEye NX Audit appliance.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the FireEye NX Audit management console or appliance.



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Collection Agents**.
  3. Download the **Ingestion Authentication File**. 
  4. Save the file securely on the system where Bindplane will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.

## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



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

  1. Open a terminal with **root** or **sudo** privileges.
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

  * **Linux:** `/etc/bindplane-agent/config.yaml`
  * **Windows:** `C:\Program Files\observIQ OpenTelemetry Collector\config.yaml`



### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/fireeye_nx:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: 'YOUR_CUSTOMER_ID'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: FIREEYE_NX_AUDIT
                raw_log_field: body
                ingestion_labels:
                    env: production
                    source: trellix_nx
        
        service:
            pipelines:
                logs/fireeye_nx_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/fireeye_nx
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on. * `0.0.0.0:514` (requires root/admin privileges). * `0.0.0.0:1514` for unprivileged port (recommended for Linux non-root).
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file.
    * `customer_id`: Your Google SecOps customer ID.
    * `endpoint`: Regional endpoint URL (e.g., `malachiteingestion-pa.googleapis.com`).
    * `log_type`: Set to `FIREEYE_NX_AUDIT`.
    * `ingestion_labels`: Optional labels for categorizing logs.



### Save the configuration file

  * **Linux:** Press `Ctrl+O`, then `Enter`, then `Ctrl+X`.
  * **Windows:** Click **File** > **Save**.



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
         




## Configure FireEye NX Audit syslog forwarding

  1. Sign in to the **FireEye NX Audit** console.
  2. Go to **Settings** > **Notifications**.
  3. Click the **rsyslog** tab.
  4. Select the **Event type** checkbox.
  5. In the **Settings** panel, select **CEF** (Common Event Format) as the **Default format**.

**Note:** CEF format is required. LEEF format is not supported for this log type.
  6. In the **Rsyslog Server Listing** section:

     1. Add a new server (e.g., `Google SecOps Bindplane`).
     2. **IP Address** : Enter the IP address of the Bindplane agent host.
     3. **Port** : Enter the Bindplane agent port number (e.g., `514`).
     4. **Protocol** : Select **UDP** or **TCP** based on your Bindplane receiver configuration.
     5. **Delivery** : Select **Per Event**.
     6. **Notifications** : Select **All Events**.
  7. Click **Update** to save.




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`alert.dst.ip` | `target.ip` | Direct mapping.  
`alert.dst.port` | `target.port` | Direct mapping.  
`alert.src.ip` | `principal.ip` | Direct mapping.  
`alert.occurred` | `metadata.event_timestamp` | Direct mapping.  
`alert.name` | `metadata.product_event_type` | Direct mapping.  
`security_result.action` | `security_result.action` | **ALLOW** if "notified", **BLOCK** if "blocked".  
`metadata.log_type` | `metadata.log_type` | Set to `FIREEYE_NX_AUDIT`.  
`metadata.vendor_name` | `metadata.vendor_name` | Set to `FireEye`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-nx-audit-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
