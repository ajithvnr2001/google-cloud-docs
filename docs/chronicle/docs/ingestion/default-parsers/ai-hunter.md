---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ai-hunter/
title: Collect Active Countermeasures AC-Hunter logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:08.536914+00:00
---

# Collect Active Countermeasures AC-Hunter logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ai-hunter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Active Countermeasures AC-Hunter logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Active Countermeasures AC-Hunter logs to Google Security Operations using Bindplane.

AC-Hunter is a network threat detection platform by Active Countermeasures that performs automated threat hunting by analyzing network traffic to identify compromised systems communicating with command and control servers. AC-Hunter runs in Docker containers on a Linux server and can forward threat alerts via the syslog protocol to a SIEM or centralized logging server.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * Windows Server 2016 or later, or a Linux host with `systemd`.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access (SSH with sudo) to the Active Countermeasures AC-Hunter server to edit the configuration file.
  * AC-Hunter version 5.3.0 or later (earlier versions contain a bug that blocks sending syslog messages).
  * Network path from the AC-Hunter server to the Bindplane agent host on your chosen syslog port (UDP or TCP).
  * IP forwarding enabled on the AC-Hunter host to allow Docker containers to send syslog to external servers.



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



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

For additional installation options, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

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
          chronicle/ac_hunter:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<CUSTOMER_ID>'
            endpoint: chronicle.googleapis.com
            log_type: AI_HUNTER
            raw_log_field: body
        
        service:
          pipelines:
            logs/ac_hunter_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/ac_hunter
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `udplog`: Use `udplog` for UDP syslog or `tcplog` for TCP syslog. Match the protocol configured in AC-Hunter.
    * `0.0.0.0:514`: IP address and port to listen on. Use `0.0.0.0` to listen on all interfaces.
  * **Exporter configuration:**

    * `<CUSTOMER_ID>`: Google SecOps Customer ID copied in the previous step.
    * `/opt/observiq-otel-collector/ingestion-auth.json`: Full path to the service account JSON key file (Option 1). 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/ac_hunter:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: AI_HUNTER
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

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
         




## Configure syslog forwarding on Active Countermeasures AC-Hunter

  1. Sign in to the **AC-Hunter server** via SSH with privileged access.
  2. Back up the existing configuration file:
         
         sudo cp /etc/AI-Hunter/config.yaml /etc/AI-Hunter/config.yaml.backup
         

  3. Open the configuration file in a text editor:
         
         sudo nano /etc/AI-Hunter/config.yaml
         

  4. Locate the **Alert:** section and the nested **Syslog:** section. Provide the following configuration details:
         
         Alert:
             Syslog:
                 Threshold: 20
                 Protocol: "udp"
                 Address: "BINDPLANE_IP:514"
                 Tag: " AC-Hunter "
         

     * **Threshold** : Enter the minimum threat score to trigger alerts (for example, `20`). Systems with scores at or above this value generate syslog alerts.
     * **Protocol** : Select `"udp"` or `"tcp"` to match the Bindplane agent receiver configuration. Use `""` (empty string) to write to the host `/dev/log` for rsyslog forwarding.
     * **Address** : Enter the Bindplane agent IP address and port (for example, `"10.1.2.3:514"`).
     * **Tag** : Enter an optional tag for log identification (for example, `" AC-Hunter "`). Include a trailing space before the closing quote so the tag does not run into the message text.
**Note:** Indentation is critical in this YAML file. Singly indented lines use 4 spaces, doubly indented lines use 8 spaces. Do not use tabs. Validate the file at [yamllint.com](http://www.yamllint.com) before saving.
  5. Save the configuration file and exit the editor.

  6. Restart AC-Hunter to apply the changes:
         
         hunt up -d --force-recreate
         

  7. Wait until approximately 20 minutes past the next hour. AC-Hunter imports new hourly logs from sensors and sends syslog alerts for systems that exceed the configured threshold during this import cycle.

  8. Verify that syslog messages are arriving at the Bindplane agent host by checking the local syslog log file:
         
         sudo tail -f /var/log/syslog
         

**Note:** AC-Hunter syslog messages use the `user.alert` facility and follow this format: `<timestamp> <hostname> AI-Hunter[<pid>]: Host: <IP> Score: <score> PreviousScore: <prev_score> Database: <db_name>`



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`api_msg_label` | `additional.fields` | Merged  
`prev_score` | `metadata.description` | Directly mapped  
`score` | `metadata.description` | Directly mapped  
`ts_date` | `metadata.event_timestamp` | Parsed as `MMM dd HH:mm:ss`  
`ts_iso8601` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UNCATEGORIZED`  
`src_ip` | `principal.asset.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`blacklist_avg_bytes_label` | `principal.labels` | Merged  
`blacklist_in_label` | `principal.labels` | Merged  
`blacklist_out_label` | `principal.labels` | Merged  
`database_label` | `principal.labels` | Merged  
`dns_txt_query_label` | `principal.labels` | Merged  
`invalid_cert_label` | `principal.labels` | Merged  
`max_beacon_label` | `principal.labels` | Merged  
`max_duration_label` | `principal.labels` | Merged  
`prev_score_label` | `principal.labels` | Merged  
`rare_client_label` | `principal.labels` | Merged  
`score_label` | `principal.labels` | Merged  
`unexpected_proto_label` | `principal.labels` | Merged  
`source_module_label` | `principal.resource.attribute.labels` | Merged  
`domain` | `target.asset.hostname` | Directly mapped  
`domain` | `target.hostname` | Directly mapped  
N/A | `metadata.event_type` | Constant: `STATUS_UNCATEGORIZED`  
N/A | `metadata.product_name` | Constant: `AI hunter`  
N/A | `metadata.vendor_name` | Constant: `Active Countermeasures`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ai-hunter-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
