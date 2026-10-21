---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/commvault-br/
title: Collect CommVault Backup and Recovery logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:24:04.646822+00:00
---

# Collect CommVault Backup and Recovery logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/commvault-br/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect CommVault Backup and Recovery logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest CommVault Backup and Recovery (CommCell) logs to Google Security Operations using the Bindplane agent.

CommVault CommCell generates syslog messages for alerts, audit trails, and events related to backup and recovery operations. The parser extracts fields and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the CommVault CommCell system
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Commvault CommCell web UI



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

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

## Configure Bindplane agent to ingest syslog and send to Google SecOps

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
            chronicle/commvault_commcell:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: COMMVAULT_COMMCELL
                raw_log_field: body
        
        service:
            pipelines:
                logs/commvault_commcell_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/commvault_commcell
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list



### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux, run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

    1. Verify the service is running:
           
           ```bash
           sudo systemctl status observiq-otel-collector
           ```
           

    2. Check logs for errors:
           
           ```bash
           sudo journalctl -u observiq-otel-collector -f
           ```
           

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
             




## Configure the Commvault syslog server

  1. Sign in to the **Commvault CommCell** web UI.
  2. Select **Manage > System**.
  3. Click **Syslog server**.
  4. Specify the following details of the syslog server: 
     * **Hostname** : enter the IP address of the Bindplane agent.
     * **Port** : enter the Bindplane port; for example, `514`.
     * Click **Enable** toggle to activate the syslog server setting.
     * In the **Forward to syslog** field, select **Alerts** , **Audit trails** and **Events**.
  5. Click **Submit**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
AgentType | observer.application | Directly mapped from the `AgentType` field in the event log.  
Alertid | security_result.detection_fields.Alertid.value | Directly mapped from the `Alertid` field in the alert log.  
Alertname | security_result.detection_fields.Alertname.value | Directly mapped from the `Alertname` field in the alert log.  
Alertseverity | security_result.severity | Mapped from the `Alertseverity` field in the alert log. Translated to UDM severity levels (INFORMATIONAL, HIGH, LOW, CRITICAL).  
Alerttime | metadata.event_timestamp | Parsed from the `Alerttime` field in the alert log and converted to a timestamp.  
Audittime | metadata.event_timestamp | Parsed from the `Audittime` field in the audit log and converted to a timestamp.  
Client | principal.hostname, principal.asset.hostname | Directly mapped from the `Client` field in the event, alert, or audit log.  
CommCell |  | This UDM field does not come from the raw log. It is set to `backupcv` if extracted from alert description.  
Computer |  | This UDM field does not come from the raw log. It is set to `backupcv` if extracted from event log.  
Description | security_result.description | Mapped from either the `Description` field in the event log or the parsed `event_description` field from the `Alertdescription` field in the alert log. If the `Description` field contains `A suspicious file`, it is overwritten with `A suspicious file is Detected`.  
Details |  | Used to extract the `Client` field using grok.  
duration |  | This UDM field does not come from the raw log. It is set to the duration extracted from event description.  
Eventid | metadata.product_log_id | Directly mapped from the `Eventid` field in the event log.  
Eventseverity | security_result.severity | Mapped from the `Eventseverity` field in the event log. Translated to UDM severity levels (INFORMATIONAL, HIGH, LOW, CRITICAL).  
file_name | security_result.detection_fields.SuspiciousFileName.value | Extracted from the `Alertdescription` field in the alert log using grok.  
Jobid | principal.process.pid | Directly mapped from the `Jobid` field in the event or alert log.  
media_agent | security_result.detection_fields.MediaAgent.value | Extracted from the `Alertdescription` field in the alert log using grok.  
no_of_files_created | security_result.detection_fields.no_of_files_created.value | Extracted from the `Alertdescription` field in the alert log using grok.  
no_of_files_deleted | security_result.detection_fields.no_of_files_deleted.value | Extracted from the `Alertdescription` field in the alert log using grok.  
no_of_files_modified | security_result.detection_fields.no_of_files_modified.value | Extracted from the `Alertdescription` field in the alert log using grok.  
no_of_files_renamed | security_result.detection_fields.no_of_files_renamed.value | Extracted from the `Alertdescription` field in the alert log using grok.  
Occurrencetime | metadata.event_timestamp | Parsed from the `Occurrencetime` field in the event log and converted to a timestamp.  
Operation | security_result.detection_fields.Operation.value | Directly mapped from the `Operation` field in the audit log.  
Opid | security_result.detection_fields.Opid.value | Directly mapped from the `Opid` field in the audit log.  
Program | principal.application | Directly mapped from the `Program` field in the event log.  
Severitylevel | security_result.severity | Mapped from the `Severitylevel` field in the audit log. Translated to UDM severity levels (INFORMATIONAL, HIGH, LOW, CRITICAL).  
Type | security_result.detection_fields.Type.value | Directly mapped from the `Type` field extracted from the `Alertdescription` field in the alert log.  
url | network.http.referral_url | Directly mapped from the `url` field extracted from the `Alertdescription` field in the alert log.  
Username | principal.user.userid | Directly mapped from the `Username` field in the audit log. If the username is `Administrator`, the `principal.user.user_role` field is set to `ADMINISTRATOR` instead.  
- | metadata.vendor_name | This UDM field does not come from the raw log. It is set to `COMMVAULT`.  
- | metadata.product_name | This UDM field does not come from the raw log. It is set to `COMMVAULT_COMMCELL`.  
- | metadata.log_type | This UDM field does not come from the raw log. It is set to `COMMVAULT_COMMCELL`.  
- | metadata.event_type | This UDM field does not come from the raw log. It is set to `STATUS_UPDATE` if the `Client` field is present, otherwise set to `GENERIC_EVENT`.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
