---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/commvault/
title: Collect Commvault logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:11:36.091993+00:00
---

# Collect Commvault logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/commvault/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Commvault logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Commvault logs to Google Security Operations using the Bindplane agent.

Commvault generates syslog messages for backup operations, alerts, events, and system activities. The parser extracts fields from the log messages and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Commvault system
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Commvault Management Console



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
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi&quot; /quiet
         

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
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/commvault:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
            <    custome>r_id: 'customer_id'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: COMMVAULT
                raw_log_field: body
        
        service:
            pipelines:
                logs/commvault_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/commvault
        




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
             




## Configure syslog in Commvault Cloud

  1. Sign in to the **Commvault** Management Console.
  2. Go to **Manage > System**.
  3. Click the **SIEM** connector tile.
  4. Click **Add connector**.
  5. On the **General** tab, enter the following details: 
     * **Connector name** : Enter a name for the connector.
     * **Connector type** : Select **Syslog**.
     * **Streaming data** : Select the data that you want to export.
  6. Click **Next**.
  7. On the **Connector Definition** tab, click **Add syslog server**.
  8. Provide the following configuration details: 
     * **Syslog server** : Enter the Bindplane agent IP address.
     * **Port number** : Enter the Bindplane agent port number.
  9. Click **Submit**.

**Note:** Custom ports are not allowed on the GUI due to security restrictions. Although the interface allows entering any port, only the default ports are permitted: `UDP Port: 514` and `TCP Port: 6514`.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
AgentType | event.idm.read_only_udm.observer.application | Value taken from `AgentType` field in the log message.  
Alertid | event.idm.read_only_udm.security_result.detection_fields.value | Value taken from `Alertid` field in the log message. This field is mapped under the `alert_id` key.  
Alertname | event.idm.read_only_udm.security_result.detection_fields.value | Value taken from `Alertname` field in the log message. This field is mapped under the `alert_name` key.  
Alertseverity | event.idm.read_only_udm.security_result.severity | This field is used to populate the `security_result.severity` field based on its value.  
Alerttime | event.idm.read_only_udm.metadata.event_timestamp | Value taken from `Alerttime` field in the log message and converted to a timestamp.  
BackupLevel | event.idm.read_only_udm.additional.fields.value.string_value | Value taken from `BackupLevel` field in the log message. This field is mapped under the `backup_level` key.  
BackupSet | event.idm.read_only_udm.additional.fields.value.string_value | Value taken from `BackupSet` field in the log message. This field is mapped under the `backup_set` key.  
Client | event.idm.read_only_udm.principal.hostname | Value taken from `Client` field in the log message.  
CommCell | event.idm.read_only_udm.additional.fields.value.string_value | Value taken from `CommCell` field in the log message. This field is mapped under the `comcell_field` key.  
Computer | event.idm.read_only_udm.additional.fields.value.string_value | Value taken from `Computer` field in the log message. This field is mapped under the `computer_field` key.  
Description | event.idm.read_only_udm.metadata.description | Value taken from `Description` field in the log message after some processing and cleanup.  
DetectedCriteria | event.idm.read_only_udm.security_result.detection_fields.value | Value taken from `DetectedCriteria` field in the log message. This field is mapped under the `detected_criteria` key.  
DetectedTime | event.idm.read_only_udm.security_result.detection_fields.value | Value taken from `DetectedTime` field in the log message. This field is mapped under the `detected_time` key.  
Details | event.idm.read_only_udm.additional.fields.value.string_value | Value taken from `Details` field in the log message. This field is mapped under the `details_field` key.  
Eventid | event.idm.read_only_udm.metadata.product_log_id | Value taken from `Eventid` field in the log message.  
Eventseverity | event.idm.read_only_udm.security_result.severity | This field is used to populate the `security_result.severity` field based on its value.  
Failure | event.idm.read_only_udm.security_result.detection_fields.value | Value taken from `Failure` field in the log message. This field is mapped under the `failure_filed` key.  
Instance | event.idm.read_only_udm.additional.fields.value.string_value | Value taken from `Instance` field in the log message. This field is mapped under the `instance_field` key.  
Jobid | event.idm.read_only_udm.principal.process.pid | Value taken from `Jobid` field in the log message.  
MonitoringCriteria | event.idm.read_only_udm.additional.fields.value.string_value | Value taken from `MonitoringCriteria` field in the log message. This field is mapped under the `monitoring_criteria` key.  
Occurencetime | event.idm.read_only_udm.metadata.event_timestamp | Value taken from `Occurencetime` field in the log message and converted to a timestamp.  
Opid | event.idm.read_only_udm.security_result.detection_fields.value | Value taken from `Opid` field in the log message. This field is mapped under the `op_id` key.  
Program | event.idm.read_only_udm.principal.application | Value taken from `Program` field in the log message.  
Severitylevel | event.idm.read_only_udm.security_result.severity | Value taken from `Severitylevel` field in the log message and mapped based on a predefined mapping.  
StoragePoliciesUsed | event.idm.read_only_udm.additional.fields.value.string_value | Value taken from `StoragePoliciesUsed` field in the log message. This field is mapped under the `storage_policies_used` key.  
Subclient | event.idm.read_only_udm.additional.fields.value.string_value | Value taken from `Subclient` field in the log message. This field is mapped under the `subclient_field` key.  
Type | event.idm.read_only_udm.security_result.detection_fields.value | Value taken from `Type` field in the log message. This field is mapped under the `alert_type` key.  
Username | event.idm.read_only_udm.principal.user.userid | Value taken from `Username` field in the log message.  
anomaly_type | event.idm.read_only_udm.security_result.detection_fields.value | Value extracted from the `Description` field using grok patterns. This field is mapped under the `detected_anomaly_type` key.  
errors | event.idm.read_only_udm.security_result.detection_fields.value | Value extracted from the `Description` field using grok patterns. This field is mapped under the `errors_field` key.  
file_name | event.idm.read_only_udm.security_result.detection_fields.value | Value extracted from the `Description` field using grok patterns. This field is mapped under the `detected_malicious_file` key.  
media_agent | event.idm.read_only_udm.security_result.detection_fields.value | Value extracted from the `Description` field using grok patterns. This field is mapped under the `detected_media_agent` key.  
no_of_files_created | event.idm.read_only_udm.security_result.detection_fields.value | Value extracted from the `Description` field using grok patterns. This field is mapped under the `no_of_files_created_field` key.  
no_of_files_deleted | event.idm.read_only_udm.security_result.detection_fields.value | Value extracted from the `Description` field using grok patterns. This field is mapped under the `no_of_files_deleted_field` key.  
no_of_files_modified | event.idm.read_only_udm.security_result.detection_fields.value | Value extracted from the `Description` field using grok patterns. This field is mapped under the `no_of_files_modified_field` key.  
no_of_files_renamed | event.idm.read_only_udm.security_result.detection_fields.value | Value extracted from the `Description` field using grok patterns. This field is mapped under the `no_of_files_renamed_field` key.  
URL | event.idm.read_only_udm.network.http.referral_url | Value extracted from the `Description` field using grok patterns.  
| event.idm.read_only_udm.metadata.event_type | This field is set to `STATUS_UPDATE` if the `Client` field is present, otherwise it's set to `GENERIC_EVENT`.  
| event.idm.read_only_udm.metadata.product_name | This field is set to `COMMVAULT`.  
| event.idm.read_only_udm.metadata.vendor_name | This field is set to `COMMVAULT`.  
| event.idm.read_only_udm.principal.user.user_role | This field is set to `ADMINISTRATOR` if the `User` field is `Administrator`.  
`Commcellname` | `additional.fields` | Mapped from changelog  
`Operation` | `metadata.description` | Mapped from changelog  
`Companyname` | `principal.user.company_name` | Mapped from changelog  
`machine_name` | `principal.hostname` | Mapped from changelog  
`locale` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/commvault-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
