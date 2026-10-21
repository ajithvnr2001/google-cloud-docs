---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ai-hunter/
title: Collect Active Countermeasures AC-Hunter logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:07:15.523287+00:00
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



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.



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

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo systemctl status observiq-otel-collector
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/ac_hunter:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<CUSTOMER_ID>'
                endpoint: malachiteingestion-pa.googleapis.com
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
    * `/etc/bindplane-agent/ingestion-auth.json`: Full path to the ingestion authentication file. 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for a complete list.



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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
