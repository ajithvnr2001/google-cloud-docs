---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digi-modems/
title: Collect Digi Modems logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:30.571205+00:00
---

# Collect Digi Modems logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digi-modems/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Digi Modems logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Digi Modems logs to Google Security Operations using the Bindplane agent.

Digi Modems are industrial cellular modems that generate syslog messages for login events, authentication attempts, and network connections. The parser extracts fields using grok patterns and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Digi modem
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Digi Remote Manager or local Digi Modem web UI



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
          chronicle/digi_modems:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: DIGI_MODEMS
            raw_log_field: body
        
        service:
          pipelines:
            logs/digi_modems_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/digi_modems
        




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
          chronicle/digi_modems:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: DIGI_MODEMS
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
             




## Configure the syslog server on Digi Modem

  1. Sign in to the **Digi Remote Manager** , or the local **Digi Modem** web UI.
  2. Access the device configuration with **Remote Manager** : 
     * Locate the device you want to configure syslog for.
     * Click **Device ID > Settings > Config**.
  3. Access the device configuration with **local Digi Modem web UI** : 
     * Click **System > Configuration > Device Configuration**.
  4. Go to **System > Log**.
  5. Click to expand **Server list**.
  6. Click **Add Server +**.
  7. Provide the following configuration details: 
     * **Server** : Enter the Bindplane agent IP address.
     * Select the event categories that will be sent to the server (all event categories are enabled by default).
     * **Syslog egress Port** : Enter the Bindplane agent port number (default is `514`).
     * **Protocol** : Select **UDP**.
  8. Click **Apply**.



## Supported Digi modems sample logs

  * **SYSLOG**
        
        {
          "priority": 14,
          "timestamp": "Dec 28 17:27:45",
          "hostname": "host-device.router",
          "tag": "Eventlog",
          "message": "17:27:33, 28 Dec 2006,Login failure by Host: 10.0.0.25:23: CMD,Telnet"
        }
        

  * **SYSLOG**
        
        {
          "priority": 14,
          "timestamp": "May 25 11:03:55",
          "hostname": "internal-srv-01",
          "tag": "Eventlog",
          "message": "11:03:55, 25 May 2023,Login failure by sanitized_user: WEB"
        }
        

  * **SYSLOG**
        
        {
          "priority": 14,
          "timestamp": "Jun 11 23:58:26",
          "hostname": "internal-srv-01",
          "tag": "Eventlog",
          "message": "23:58:26, 11 Jun 2023,Login failure by GET /masked_path HTTP/1.0: CMD,Telnet"
        }
        

  * **SYSLOG**
        
        {
          "priority": 14,
          "timestamp": "Jun 19 19:52:19",
          "hostname": "gateway-device-02",
          "tag": "Eventlog",
          "message": "19:52:18, 19 Jun 2023,WEB Login OK by internal_admin lvl 0"
        }
        




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
content | security_result.description | Directly mapped from the `content` field after initial grok parsing.  
http_method | network.http.method | Extracted from the `content` field using a grok pattern.  
http_version | network.application_protocol_version | Extracted from the `content` field using a grok pattern.  
hostname | principal.hostname | Extracted from the log message using a grok pattern.  
ip | target.ip | Extracted from the `content` field using a grok pattern.  
port | target.port | Extracted from the `content` field using a grok pattern and converted to an integer.  
proto | network.application_protocol | Extracted from the `content` field using a grok pattern.  
ts | metadata.event_timestamp | Extracted from the log message using a grok pattern and converted to a timestamp.  
type | login_type_label.value | Extracted from the `content` field using a grok pattern.  
| extensions.auth.type | Set to `MACHINE` by parser logic.  
| login_type_label.key | Set to `Login type` by parser logic.  
| metadata.event_type | Determined by the presence of specific fields like `ip` or `user` and set accordingly to `NETWORK_CONNECTION` or `USER_LOGIN`.  
| metadata.log_type | Set to `DIGI_MODEMS` by parser logic.  
| metadata.product_event_type | Extracted from the `product_type` field in the log message.  
| metadata.product_name | Set to `DIGI_MODEMS` by parser logic.  
| metadata.vendor_name | Set to `DIGI_MODEMS` by parser logic.  
| security_result.action | Determined by the presence of `Login OK` or `Login failure` in the message and set to `ALLOW` or `BLOCK` respectively.  
user | target.user.userid | Extracted from the `content` field using a grok pattern.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/digi-modems-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
