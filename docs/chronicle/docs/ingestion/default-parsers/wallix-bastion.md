---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/wallix-bastion/
title: Collect Wallix Bastion logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:54:01.690126+00:00
---

# Collect Wallix Bastion logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/wallix-bastion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Wallix Bastion logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Wallix Bastion logs to Google Security Operations using the Bindplane agent.

Wallix Bastion is a privileged access management (PAM) platform that generates syslog messages for session recordings, authentication events, password management, and administrative actions.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Wallix Bastion appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Wallix Bastion web UI



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
          chronicle/wallix_bastion:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: WALLIX_BASTION
            raw_log_field: body
        
        service:
          pipelines:
            logs/wallix_bastion_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/wallix_bastion
        




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
          chronicle/wallix_bastion:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: WALLIX_BASTION
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
             




## Configure syslog in Wallix Bastion

  1. Sign in to the **Wallix Bastion** web UI.
  2. Go to **Configuration > Syslog**.
  3. Click **Add** to add a new syslog server.
  4. Provide the following configuration details: 
     * **Server Address** : Enter the Bindplane agent IP address.
     * **Port** : Enter `514`.
     * **Protocol** : Select **UDP**.
     * **Facility** : Select **Local0**.
  5. Click **Activate**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`status_label` | `additional.fields` | Merged  
`type_label` | `additional.fields` | Merged  
`infos` | `extensions.auth.type` | Mapped: `(Authentication started/Authentication success)` → `AUTHTYPE_UNSPECIFIED`, `Closed ...  
`hostname` | `intermediary.hostname` | Directly mapped  
`infos` | `metadata.description` | Directly mapped  
`msg` | `metadata.description` | Directly mapped  
`ts` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`event_type` | `metadata.event_type` | Directly mapped  
`event_details` | `metadata.product_event_type` | Directly mapped  
`uid` | `metadata.product_log_id` | Directly mapped  
`total_bytes_recv` | `network.received_bytes` | Renamed/mapped  
`total_bytes_send` | `network.sent_bytes` | Renamed/mapped  
`client_ip` | `principal.asset.ip` | Merged  
`ip` | `principal.asset.ip` | Merged  
`src_ip` | `principal.asset.ip` | Merged  
`client_ip` | `principal.ip` | Merged  
`ip` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`src_port` | `principal.port` | Directly mapped  
`action` | `security_result.action_details` | Directly mapped  
`process` | `target.application` | Directly mapped  
`dest_ip` | `target.asset.ip` | Merged  
`dest_ip` | `target.ip` | Merged  
`dest_port` | `target.port` | Directly mapped  
`pid` | `target.process.pid` | Directly mapped  
`user` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.product_name` | Constant: `Wallix Bastion`  
N/A | `metadata.vendor_name` | Constant: `WALLIX_BASTION`  
N/A | `network.ip_protocol` | Constant: `TCP`  
`partial_data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`StartTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`EndTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ReplicationSuccessCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ReplicationSize_octets` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`psid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vault` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`session` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`TTY` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`service` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`format` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`channel_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RSA_SHA256` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`account` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`target_data` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`partial_data` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`principal_user` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`USER` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`login` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`PWD` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`command_line` | `event.idm.read_only_udm.target.process.command_line` | Mapped from changelog  
`COMMAND` | `event.idm.read_only_udm.target.process.command_line` | Mapped from changelog  
`command_line_details` | `event.idm.read_only_udm.principal.process.command_line` | Mapped from changelog  
`principal_process_file_name` | `event.idm.read_only_udm.principal.process.file.names` | Mapped from changelog  
`target_ip` | `event.idm.read_only_udm.target.ip`,`event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`target_ip` | `event.idm.read_only_udm.target.hostname`,`event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`device` | `event.idm.read_only_udm.principal.hostname`,`event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`service` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`size` | `event.idm.read_only_udm.target.file.size` | Mapped from changelog  
`length` | `event.idm.read_only_udm.target.file.size` | Mapped from changelog  
`file_name` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`sha256` | `event.idm.read_only_udm.target.file.sha256` | Mapped from changelog  
`desc` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`result` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`target_file_name` | `event.idm.read_only_udm.target.file.names` | Mapped from changelog  
`port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`principal_ip` | `event.idm.read_only_udm.principal.ip`,`event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`principal_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`host` | `event.idm.read_only_udm.target.ip`,`event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`target_ip_details` | `event.idm.read_only_udm.target.ip`,`event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`target_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`psid` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`session_id` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`summary_details` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/wallix-bastion-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
