---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-qradar/
title: Collect IBM QRadar logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:58:27.378029+00:00
---

# Collect IBM QRadar logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-qradar/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect IBM QRadar logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest IBM Security QRadar SIEM logs to Google Security Operations using the Bindplane agent.

IBM Security QRadar is a security information and event management platform that correlates events across the enterprise to detect threats. It generates offense alerts, event logs, and flow data. QRadar supports syslog forwarding for offenses and events in LEEF and JSON formats.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the IBM QRadar console
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to IBM QRadar with admin or log export permissions



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
            tcplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/ibm_qradar:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: IBM_QRADAR
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/qradar_to_chronicle:
                    receivers:
                        - tcplog
                    exporters:
                        - chronicle/ibm_qradar
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `tcplog`: The receiver type based on protocol: 
      * `udplog` for UDP syslog
      * `tcplog` for TCP syslog
    * `0.0.0.0`: IP address to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Specific IP address to listen on one interface
    * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)
  * **Exporter configuration:**

    * `ibm_qradar`: Descriptive name for the exporter
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `IBM_QRADAR`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `qradar_to_chronicle`: Descriptive name for the pipeline



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
             




## Configure IBM QRadar syslog forwarding

  1. Sign in to the **QRadar** console as an administrator.
  2. Go to **Admin > System and License Management > System Settings**.
  3. Under **Forwarding Destinations** , click **Add**.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Chronicle-Bindplane`).
     * **IP Address** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (must match the Bindplane agent receiver port).
     * **Protocol** : Select **TCP** (recommended for reliable delivery).
     * **Format** : Select **LEEF** (Log Event Extended Format).
  5. Click **Save**.
  6. Go to **Admin > Forwarding Profiles** to create or edit a forwarding profile.
  7. Select the event and flow types to forward: 
     * Offense events
     * Normalized events
     * Flow data (optional)
  8. Assign the forwarding destination created in step 4.
  9. Click **Save** and deploy changes.
  10. Verify that syslog messages are being received by checking the Bindplane agent logs.

**Note:** QRadar supports forwarding events in LEEF and JSON formats via syslog. The Chronicle parser handles JSON-formatted QRadar logs. Ensure the selected format matches your Chronicle parser configuration.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`application` | `extensions.auth.type` | Mapped: `httpd` → `AUTHTYPE_UNSPECIFIED`  
`_source.message` | `metadata.description` | Directly mapped  
`message_body` | `metadata.description` | Directly mapped  
`_source.eventTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`log_date` | `metadata.event_timestamp` | Parsed as `MMM dd HH:mm:ss`  
`application` | `metadata.event_type` | Mapped: `httpd` → `USER_LOGIN`, `logger` → `NETWORK_HTTP`, `CROND` → `PROCESS_LAUNCH`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_HTTP`, `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`_source.eventType` | `metadata.product_event_type` | Directly mapped  
`_source._id` | `metadata.product_log_id` | Directly mapped  
`_source.typeURI` | `metadata.url_back_to_product` | Directly mapped  
`_source.o_requestData.o_request_body.method` | `network.http.method` | Directly mapped  
`response` | `network.http.response_code` | Renamed/mapped  
`response_code` | `network.http.response_code` | Renamed/mapped  
`_source.o_requestData.o_headers.User-Agent` | `network.http.user_agent` | Directly mapped  
`crypto_algorithm` | `network.tls.cipher` | Directly mapped  
`tls_version` | `network.tls.version` | Directly mapped  
`_source.o_observer.name` | `observer.resource.name` | Directly mapped  
`application` | `principal.application` | Directly mapped  
`_source._host` | `principal.asset.hostname` | Directly mapped  
`_source._ip` | `principal.asset.ip` | Merged  
`_source.o_initiator.o_host.address` | `principal.asset.ip` | Merged  
`_source._file` | `principal.file.full_path` | Directly mapped  
`_source._host` | `principal.hostname` | Directly mapped  
`_source._ip` | `principal.ip` | Merged  
`_source.o_initiator.o_host.address` | `principal.ip` | Merged  
`log_ip` | `principal.ip` | Merged  
`event_id` | `principal.process.pid` | Directly mapped  
`o_credential` | `principal.resource.attribute.labels` | Merged  
`_source.o_requestData.initiatorGUID` | `principal.resource.product_object_id` | Directly mapped  
`_source.o_initiator.typeURI` | `principal.url` | Directly mapped  
`_source.o_requestData.o_request_body.user_name` | `principal.user.user_display_name` | Directly mapped  
`_source.o_initiator.authnId` | `principal.user.userid` | Directly mapped  
`action` | `security_result.action` | Merged  
`application` | `security_result.action` | Mapped: `httpd` → `action`  
`auth_status` | `security_result.action` | Mapped: `(?i)failed` → `action`  
`_source.o_requestData.o_request_body.action` | `security_result.action_details` | Directly mapped  
`_source.o_responseData.response_body` | `security_result.action_details` | Directly mapped  
`auth_status` | `security_result.description` | Directly mapped  
`correlationId` | `security_result.detection_fields` | Merged  
`dataEvent` | `security_result.detection_fields` | Merged  
`platform` | `security_result.detection_fields` | Merged  
`saveServiceCopy` | `security_result.detection_fields` | Merged  
`scenario_type` | `security_result.detection_fields` | Merged  
`log_level` | `security_result.severity` | Mapped: `(?i)(error/warning)` → `HIGH`, `(?i)notice` → `MEDIUM`, `(?i)(information/info)` → ...  
`_source.severity` | `security_result.severity_details` | Directly mapped  
`_source.o_target.o_host.address` | `target.asset.hostname` | Directly mapped  
`_source.o_target.o_host.address` | `target.hostname` | Directly mapped  
`application` | `target.ip` | Mapped: `httpd` → `host_ip`, `logger` → `ip`  
`host_ip` | `target.ip` | Merged  
`ip` | `target.ip` | Merged  
`command` | `target.process.command_line` | Directly mapped  
`clientid` | `target.resource.attribute.labels` | Merged  
`_source.o_target.typeURI` | `target.url` | Directly mapped  
`request` | `target.url` | Renamed/mapped  
`_source.o_target.name` | `target.user.user_display_name` | Directly mapped  
`_source.o_target.id` | `target.user.userid` | Directly mapped  
`auth` | `target.user.userid` | Renamed/mapped  
`target_host` | `target.user.userid` | Directly mapped  
`user_id` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `NETWORK_HTTP`  
N/A | `metadata.product_name` | Constant: `IBM QRADAR`  
N/A | `metadata.vendor_name` | Constant: `IBM QRADAR`  
N/A | `security_result.severity` | Constant: `MEDIUM`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-qradar-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
