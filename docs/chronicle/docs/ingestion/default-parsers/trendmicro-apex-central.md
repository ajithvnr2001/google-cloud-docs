---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-apex-central/
title: Collect Trend Micro Apex Central logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:58.593643+00:00
---

# Collect Trend Micro Apex Central logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-apex-central/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trend Micro Apex Central logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Trend Micro Apex Central logs to Google Security Operations using the Bindplane agent.

Trend Micro Apex Central is a centralized security management console for Trend Micro products that provides threat detection, policy management, and security event logs across endpoints, servers, and network layers. It outputs logs in CEF format via syslog.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Trend Micro Apex Central server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Trend Micro Apex Central with administrator permissions



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

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          tcplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/trendmicro_apex_central:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: TRENDMICRO_APEX_CENTRAL
            raw_log_field: body
        
        service:
          pipelines:
            logs/trendmicro_apex_central_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/trendmicro_apex_central
        




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
          chronicle/trendmicro_apex_central:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: TRENDMICRO_APEX_CENTRAL
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
             




## Configure Trend Micro Apex Central syslog forwarding

  1. Sign in to the **Apex Central** management console.
  2. Go to **Administration > Settings > Syslog Settings**.
  3. Enable syslog forwarding by selecting the **Enable Syslog Forwarding** checkbox.
  4. Provide the following configuration details: 
     * **Server address** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Protocol** : Select **TCP**.
     * **Format** : Select **CEF** (Common Event Format).
  5. Select the log types to forward: 
     * Detection logs
     * Policy violation events
     * Security events
     * System events
  6. Click **Save** to apply the configuration.
  7. Verify that logs are being sent by checking the Bindplane agent logs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
var_eventFormatVersion, var_severity, dntdom_label, additional_cs6, additional_product_version, additional_cat, additional_msg, additional_dvchost, var_cs1_label, var_cs1, var_cs2, var_cs5, var_deviceExternalId, var_c6a3, var_cn1_label, var_cn1, var_cn2, var_cs4_label, var_cs4, var_c6a2, var_cn3, var_cnt, var_TMCMLogTarget, var_deviceDirection | additional.fields | Additional vendor-specific event data  
rt | metadata.event_timestamp | Timestamp when the event occurred  
event_name | metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)  
event_id | metadata.product_event_type | Type of event from the product  
devicePayloadId | metadata.product_log_id | Unique identifier for the log entry from the product  
cs3, product_version | metadata.product_version | Version of the product  
vendor | metadata.vendor_name | Vendor/company name  
product_name | metadata.product_name | Product name  
app | network.application_protocol | Application protocol  
deviceDirection | network.direction | Direction of the network traffic  
proto | network.ip_protocol | IP protocol  
domain, dntdom | principal.administrative_domain | Administrative domain of the principal  
dhost | principal.asset.hostname | Hostname of the asset  
TMCMLogDetectedIP, princ_ip | principal.asset.ip | IP address of the asset  
platform | principal.asset.platform | Platform of the asset  
patch_level | principal.asset.platform_patch_level | Patch level of the platform  
version | principal.asset.platform_version | Version of the platform  
dvchost, dhost | principal.hostname | Source hostname  
TMCMLogDetectedIP, princ_ip | principal.ip | IP address of the principal  
smac | principal.mac | MAC address of the principal  
spt | principal.port | Port of the principal  
deviceProcessName | principal.process.file.full_path | Full path of the process file  
duser | principal.user.userid | User ID of the principal  
security_result | security_result | Security result  
act | security_result.action | Action taken by the security product  
act, cs5 | security_result.action_details | Details of the action taken  
cs4 | security_result.category_details | Details about the category  
cs1, cn2 | security_result.description | Description of the security result  
var_cn2_label | security_result.detection_fields | Fields related to detection  
cn1 | security_result.rule_id | ID of the rule  
cs1 | security_result.rule_name | Name of the rule  
cn3, severity, cn4, cn2 | security_result.severity | Severity of the security result  
event_name | security_result.threat_name | Name of the threat  
cnt | security_result.verdict_info | Information about the verdict  
shost | src.hostname | Source hostname  
src, host_ip | src.ip | Source IP address  
suser | src.user.userid | User ID of the source  
deviceNtDomain | target.administrative_domain | Administrative domain of the target  
c6a3 | target.asset.ip | IP address of the asset  
filePath, sproc | target.file.full_path | Full path of the file  
fname | target.file.names | Names of the file  
fileHash | target.file.sha1 | SHA1 hash of the file  
c6a3 | target.ip | IP address of the target  
dmac | target.mac | MAC address of the target  
dpt | target.port | Port of the target  
cs3, sproc | target.process.file.full_path | Full path of the process file  
request | target.url | URL of the target  
duser | target.user.userid | User ID of the target  
`cs3` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Product_Version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`var_cn2_label.value` | `N/A` | Mapped from changelog  
`var_cn2_label.value` | `Unknown` | Mapped from changelog  
`var_cn2_label.value` | `Clean` | Mapped from changelog  
`var_cn2_label.value` | `Delete` | Mapped from changelog  
`var_cn2_label.value` | `Move` | Mapped from changelog  
`var_cn2_label.value` | `Rename` | Mapped from changelog  
`var_cn2_label.value` | `Pass/Log` | Mapped from changelog  
`var_cn2_label.value` | `Strip` | Mapped from changelog  
`var_cn2_label.value` | `Drop` | Mapped from changelog  
`var_cn2_label.value` | `Quarantine` | Mapped from changelog  
`cnt` | `security_result.verdict_info.malicious_count` | Mapped from changelog  
`metadata.event_type` | `STATUS_UPDATE` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-apex-central-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
