---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudgenix-sdwan/
title: Collect Palo Alto Prisma SD-WAN logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:44.362570+00:00
---

# Collect Palo Alto Prisma SD-WAN logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudgenix-sdwan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Palo Alto Prisma SD-WAN logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Palo Alto Prisma SD-WAN (formerly CloudGenix) logs to Google Security Operations using the Bindplane agent.

Palo Alto Prisma SD-WAN is a cloud-delivered software-defined wide area network solution that provides application-aware routing, centralized policy management, and automated branch connectivity. It simplifies WAN operations by replacing traditional router-centric networks with a secure, application-defined fabric that optimizes performance and reduces costs.

For more information, see [Palo Alto Prisma SD-WAN documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudgenix-sdwan).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Palo Alto Prisma SD-WAN management console (Strata Cloud Manager or legacy CloudGenix Controller)
  * Network connectivity between the Bindplane agent host and the Prisma SD-WAN ION devices



## Get Google SecOps Ingestion Authentication File

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



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
            chronicle/cloudgenix_sdwan:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<CUSTOMER_ID>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: CLOUDGENIX_SDWAN
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/cloudgenix_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/cloudgenix_sdwan
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on. Use `0.0.0.0` to listen on all interfaces. Port `514` is standard for syslog (requires root privileges on Linux; use `1514` for non-root).
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the Google SecOps ingestion authentication file. 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<CUSTOMER_ID>`: Google SecOps customer ID.
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for the complete list.



### Save the configuration file

  * After editing, save the file:

    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in **Linux** , run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

    1. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    2. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           

  * To restart the Bindplane agent in **Windows** , choose one of the following options:

    1. Command Prompt or PowerShell as administrator:
           
           net stop observiq-otel-collector && net start observiq-otel-collector
           

    2. Press `Win+R`, type `services.msc`, and press Enter.

    3. Locate **observIQ OpenTelemetry Collector**.

    4. Right-click and select **Restart**.

    5. Verify the service is running:
           
           sc query observiq-otel-collector
           

    6. Check logs for errors:
           
           type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
           




## Configure Palo Alto Prisma SD-WAN syslog forwarding

You can configure syslog forwarding on individual ION devices or create a reusable syslog profile that can be applied across multiple devices.

### Option 1: Configure syslog export on an individual ION device

  1. Sign in to the **Strata Cloud Manager** with administrator privileges.
  2. Go to **Configuration > Prisma SD-WAN > ION Devices > Claimed**.
  3. Select the ION device that you want to configure for syslog forwarding.
  4. Click **Configure the device**.
  5. Select **Syslog Export**.
  6. Click **Create Syslog Server**.
  7. Select **Enable this Syslog Server**.
  8. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `SecOps-Bindplane`).
     * **Server IP** or **Server FQDN** : Select **Server IP** and enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Server Port** : Enter `514` (or the port configured in the Bindplane agent). Default ports are `514` for TCP or UDP and `6514` for TLS.
     * **Protocol** : Select **UDP** (default), **TCP** , or **TLS**.
     * **Severity Level** : Select **critical** , **major** , or **minor**. Logs and events for the selected severity level and higher are exported.
  9. To export flow logs, enable the **Flow Logging** option.
  10. Click **Save**.
  11. Verify that syslog messages are being received by checking the Bindplane agent logs.

**Note:** The maximum number of syslog servers supported per ION device is 16. ION devices use the syslog RFC 5424 format for all protocols.



### Option 2: Create a reusable syslog profile

  1. Sign in to the **Strata Cloud Manager** with administrator privileges.
  2. Go to **Configuration > Prisma SD-WAN > Profiles and Templates > Syslog**.
  3. Click **Create Syslog Profile**.
  4. Provide the following configuration details: 
     * **Name** : Enter a name for the syslog profile (for example, `SecOps-Bindplane`).
     * **Description** : Optionally, enter a description.
     * **Server IP** or **Server FQDN** : Select **Server IP** and enter the IP address of the Bindplane agent host.
     * **Server Port** : Enter `514` (or the port configured in the Bindplane agent).
     * **Protocol** : Select **UDP**.
  5. Under **Security Logs** , select the log types to forward: 
     * **Threat** : Threat detection logs.
     * **DNS** : DNS security logs.
     * **URL** : URL filtering logs.
  6. Click **Save**.
  7. Assign the syslog profile to the desired ION devices through the device configuration.
  8. Verify that syslog messages are being received by checking the Bindplane agent logs.

**Note:** Syslog profiles allow you to apply the same syslog configuration across multiple ION devices. For more information, see [Prisma SD-WAN syslog documentation](https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-sites-and-devices/use-external-services-for-monitoring/syslog-server-support-in-prisma-sd-wan).



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`_about` | `about` | Merged  
`_intermediary` | `intermediary` | Merged  
`MSG` | `metadata.description` | Directly mapped  
`CODE` | `metadata.product_event_type` | Directly mapped  
`FACILITY` | `metadata.product_event_type` | Directly mapped  
`log_type` | `metadata.product_event_type` | Directly mapped  
`APP_NAME` | `network.http.user_agent` | Directly mapped  
`PROTOCOL_NAME` | `network.ip_protocol` | Directly mapped  
`BYTES_RECVD` | `network.received_bytes` | Directly mapped  
`BYTES_SENT` | `network.sent_bytes` | Directly mapped  
`CLOUDGENIX_HOST` | `principal.hostname` | Directly mapped  
`ION_HOST` | `principal.hostname` | Directly mapped  
`NAME` | `principal.hostname` | Directly mapped  
`SRC_INTERFACE` | `principal.hostname` | Directly mapped  
`SRC_IP` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`SRC_PORT` | `principal.port` | Directly mapped  
`PROCESS_NAME` | `principal.process.file.full_path` | Directly mapped  
`pid` | `principal.process.pid` | Directly mapped  
`sec_result` | `security_result` | Merged  
`DST_INTERFACE` | `target.hostname` | Directly mapped  
`REMOTE_HOSTNAME` | `target.hostname` | Directly mapped  
`DST_IP` | `target.ip` | Merged  
`REMOTE_IP` | `target.ip` | Merged  
`dest_ip` | `target.ip` | Merged  
`DST_PORT` | `target.port` | Directly mapped  
`VPN_LINK_ID` | `target.resource.id` | Directly mapped  
N/A | `about` | Constant: `_about`  
N/A | `intermediary` | Constant: `_intermediary`  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `CloudGenix SD-WAN`  
N/A | `metadata.vendor_name` | Constant: `Palo Alto Networks`  
N/A | `network.received_bytes` | Constant: `uinteger`  
N/A | `network.sent_bytes` | Constant: `uinteger`  
N/A | `principal.ip` | Constant: `src_ip`  
N/A | `security_result` | Constant: `sec_result`  
N/A | `target.ip` | Constant: `REMOTE_IP`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudgenix-sdwan-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
