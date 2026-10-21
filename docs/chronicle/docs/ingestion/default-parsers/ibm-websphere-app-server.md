---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-websphere-app-server/
title: Collect IBM WebSphere Application Server logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:25:20.661813+00:00
---

# Collect IBM WebSphere Application Server logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-websphere-app-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect IBM WebSphere Application Server logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest IBM WebSphere Application Server logs to Google Security Operations using the Bindplane agent.

IBM WebSphere Application Server is a Java EE application server that generates system, security audit, and access logs. The parser maps these logs to the Unified Data Model (UDM), extracting process details, user information, event timestamps, and file metadata.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the IBM WebSphere Application Server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the IBM WebSphere Application Server



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

## Configure Bindplane agent to ingest logs and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            filelog:
                include:
                    - /opt/IBM/WebSphere/AppServer/profiles/*/logs/*/SystemOut.log
                    - /opt/IBM/WebSphere/AppServer/profiles/*/logs/*/SystemErr.log
                start_at: beginning
        
        exporters:
            chronicle/websphere:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: IBM_WEBSPHERE_APP_SERVER
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/websphere_to_chronicle:
                    receivers:
                        - filelog
                    exporters:
                        - chronicle/websphere
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `filelog`: The receiver type for collecting log files from disk
    * `include`: List of file paths to monitor. Default WebSphere log locations: 
      * **Linux** : `/opt/IBM/WebSphere/AppServer/profiles/<PROFILE>/logs/<SERVER>/SystemOut.log`
      * **Windows** : `C:\IBM\WebSphere\AppServer\profiles\<PROFILE>\logs\<SERVER>\SystemOut.log`
    * `start_at`: Set to `beginning` to read existing logs or `end` to only read new entries
  * **Exporter configuration:**

    * `websphere`: Descriptive name for the exporter
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `IBM_WEBSPHERE_APP_SERVER`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `websphere_to_chronicle`: Descriptive name for the pipeline



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
             




## Configure IBM WebSphere Application Server logging

  1. Sign in to the **IBM WebSphere Application Server** administrative console.
  2. Go to **Troubleshooting > Logs and Trace**.
  3. Select the server (for example, `server1`).
  4. Click **Diagnostic Trace** to configure trace logging levels, or click **JVM Logs** to configure SystemOut and SystemErr log settings.
  5. Under **JVM Logs** , verify the following settings: 
     * **System.out** log file name: `${SERVER_LOG_ROOT}/SystemOut.log`
     * **System.err** log file name: `${SERVER_LOG_ROOT}/SystemErr.log`
     * **Log file rotation** : Configure log rotation (for example, by file size or time) to prevent log files from growing indefinitely.
  6. Click **Apply** and then **Save** to save the configuration.
  7. Identify the log directories on your WebSphere server. Default locations include: 
     * `<WAS_HOME>/profiles/<PROFILE>/logs/<SERVER>/SystemOut.log`
     * `<WAS_HOME>/profiles/<PROFILE>/logs/<SERVER>/SystemErr.log`
     * `<WAS_HOME>/profiles/<PROFILE>/logs/<SERVER>/BinaryAudit*` (security audit logs, if auditing is enabled)
  8. Ensure the Bindplane agent `include` paths in `config.yaml` match the actual log file locations on your WebSphere server.

**Note:** If security auditing is enabled, you can also include `BinaryAudit*` files by adding the appropriate path to the `include` list in the Bindplane agent configuration. The Bindplane agent service account must have read access to the log directories.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
number, MemCount, JMSMessageID | additional | Merged as key-value pairs for each field  
TrgAction, description | metadata.description | Value from TrgAction if not empty, else description  
time | metadata.event_timestamp | Parsed using date filter with formats MM/dd/yy HH:mm:ss.SSS Z, M/dd/yy H:mm:ss.SSS Z, UNIX_MS  
| metadata.event_type | Set to "GENERIC_EVENT"  
Action | metadata.product_event_type | Value copied directly  
product_log_id | metadata.product_log_id | Value copied directly  
version | metadata.product_version | Value copied directly  
product | metadata.product_name | Value copied directly  
vendor | metadata.vendor_name | Value copied directly  
file_name | target.file.full_path | Value copied directly  
command | target.process.command_line | Value copied directly  
filename | target.process.file.full_path | Value copied directly  
Members | target.user.group_identifiers | Merged from processed Members array  
Eid | target.user.product_object_id | Value copied directly  
Profile | target.user.user_display_name | Value copied directly  
`principal_user` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`exception_code` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`exception_class` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`source_line` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`length` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`websphere_java_version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`websphere_platform_details` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`java_compiler` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`java_vm_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`parent_context` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_context` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`method_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`principal_application` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`os_version` | `event.idm.read_only_udm.principal.asset.platform_software.platform_version` | Mapped from changelog  
`os_name` | `event.idm.read_only_udm.principal.asset.platform_software.platform_patch_level` | Mapped from changelog  
`process_name` | `event.idm.read_only_udm.principal.resource.name` | Mapped from changelog  
`full_orb_version` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`target_application` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-websphere-app-server-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
