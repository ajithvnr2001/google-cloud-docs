---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/barracuda-cloudgen-firewall/
title: Collect Barracuda CloudGen Firewall logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:37.872090+00:00
---

# Collect Barracuda CloudGen Firewall logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/barracuda-cloudgen-firewall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Barracuda CloudGen Firewall logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Barracuda CloudGen Firewall logs to Google Security Operations using the Bindplane agent.

Barracuda CloudGen Firewall is a next-generation firewall that generates syslog messages for network traffic, security events, authentication, and system operations via its Syslog Streaming feature.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Barracuda CloudGen Firewall
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Barracuda Firewall Control Center



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
          chronicle/barracuda_cloudgen_firewall:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: BARRACUDA_CLOUDGEN_FIREWALL
            raw_log_field: body
        
        service:
          pipelines:
            logs/barracuda_cloudgen_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/barracuda_cloudgen_firewall
        




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
          chronicle/barracuda_cloudgen_firewall:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: BARRACUDA_CLOUDGEN_FIREWALL
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
             




## Enable syslog streaming for Barracuda CloudGen Firewall

  1. Sign in to the **Barracuda Firewall Control Center** at the box level.
  2. Go to **Configuration > Full Configuration > Box > Infrastructure Services > Syslog Streaming**.
  3. Click the **Lock** icon to enable editing.
  4. Switch **Enable Syslog Streaming** to **Yes**.
  5. Click **Send Changes > Activate**.



## Configure logdata filters for Barracuda CloudGen Firewall

  1. Go to **Configuration > Full Configuration > Box > Infrastructure Services > Syslog Streaming**.
  2. Select **Logdata Filters**.
  3. Click the **Configuration Mode** menu and select **Switch to Advanced View**.
  4. Click the **Lock** icon to enable editing.
  5. Click **Add** to add a new entry.
  6. Provide a unique name in the **Filters** dialog.
  7. Click **OK**.
  8. In the **Affected Box Logdata** section, select **logs sent via syslog**.
  9. Click **Add** next to **Data Selection**.
  10. Provide a unique name for the **group**.
  11. Click **OK**.
  12. Select the following items from the **Data Selection** or your specific categories for logging: 
     * `Auth-All`
     * `Config-All`
     * `Control-All`
     * `Event-All`
     * `Firewall-All`
     * `Network-All`
     * `Settings-All`
     * `SSH-All`
     * `System-All`
  13. Select the following items from **Message Types** or your specific severity for logging: 
     * `Panic`
     * `Security`
     * `Fatal`
     * `Error`
     * `Warning`
     * `Notice`
  14. Click **OK**.
  15. Click **Send Changes > Activate**.



## Configure logstream destination for Barracuda CloudGen Firewall

  1. Go to **Configuration > Full Configuration > Box > Infrastructure Services > Syslog Streaming**.
  2. Select **Logstream Destinations**.
  3. Click the **Configuration Mode** menu and select **Switch to Advanced View**.
  4. Click the **Lock** icon to enable editing.
  5. Click **Add** to add a new entry.
  6. Provide a unique name for the **destination**.
  7. Click **OK**.
  8. Select the newly created **Logstream Destination**.
  9. Click **Explicit IP**.
  10. Provide the following configuration details: 
     * **Destination IP Address** : Enter the Bindplane agent IP address.
     * **Destination Port** : Enter the Bindplane agent port number.
     * **Transmission Mode** : Select **UDP**.
  11. Click **OK**.
  12. Click **Send Changes > Activate**.



## Configure logdata streams for Barracuda CloudGen Firewall

  1. Go to **Configuration > Full Configuration > Box > Infrastructure Services > Syslog Streaming**.
  2. Select **Logdata Streams**.
  3. Click the **Configuration Mode** menu and select **Switch to Advanced View**.
  4. Click the **Lock** icon to enable editing.
  5. Click **Add** to add a new entry.
  6. Provide a unique name for the **configuration**.
  7. Click **OK**.
  8. Set **Active Streams** to **Yes**.
  9. Set **Log Destinations** to the destination created earlier.
  10. Set **Log Filters** to the filter created earlier.
  11. Click **OK**.
  12. Click **Send Changes > Activate**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`connection_type_label` | `additional.fields` | Merged  
`details_label` | `additional.fields` | Merged  
`id_label` | `additional.fields` | Merged  
`process_name_label` | `additional.fields` | Merged  
`desc` | `metadata.description` | Directly mapped  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`host` | `principal.asset.hostname` | Directly mapped  
`column13` | `principal.asset.ip` | Merged  
`src_ip` | `principal.asset.ip` | Merged  
`host` | `principal.hostname` | Directly mapped  
`column13` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`column6` | `principal.mac` | Merged  
`column5` | `principal.port` | Renamed/mapped  
`src_port` | `principal.port` | Directly mapped  
`_action` | `security_result.action` | Merged  
`action` | `security_result.action` | Mapped: `Allow` → `_action`  
`action` | `security_result.action_details` | Directly mapped  
`severity` | `security_result.severity` | Mapped: `INFO` → `INFORMATIONAL`, `WARNING` → `MEDIUM`, `BLOCK` → `ERROR`  
`severity` | `security_result.severity_details` | Directly mapped  
`tar_app` | `target.application` | Directly mapped  
`column14` | `target.asset.ip` | Merged  
`column7` | `target.asset.ip` | Merged  
`dst_ip` | `target.asset.ip` | Merged  
`column14` | `target.ip` | Merged  
`column7` | `target.ip` | Merged  
`dst_ip` | `target.ip` | Merged  
`mac` | `target.mac` | Merged  
`column8` | `target.port` | Renamed/mapped  
`dst_port` | `target.port` | Renamed/mapped  
`product_id` | `target.process.pid` | Directly mapped  
`user_id` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `NETWORK_CONNECTION`  
N/A | `metadata.product_name` | Constant: `BARRACUDA CLOUDGEN FIREWALL`  
N/A | `metadata.vendor_name` | Constant: `BARRACUDA CLOUDGEN FIREWALL`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
`server` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`service` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`box` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`startport` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`endport` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`request_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`request_key` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslogpriority` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`peer` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`origin` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`desc` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`principal_user_id` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`cn_data` | `event.idm.read_only_udm.principal.user.group_identifiers` | Mapped from changelog  
`src_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`column1` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column3` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column9` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column12` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`column4` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`column2` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`ts_timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/barracuda-cloudgen-firewall-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
