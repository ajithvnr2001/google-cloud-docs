---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/xiting-xams/
title: Collect XAMS by Xiting logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:39:12.531135+00:00
---

# Collect XAMS by Xiting logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/xiting-xams/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect XAMS by Xiting logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest XAMS by Xiting logs to Google Security Operations using the Bindplane agent.

XAMS by Xiting is an SAP authorization management and security platform used for role design, access risk analysis, and compliance monitoring. It runs within an SAP environment and generates authorization management and compliance audit logs.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the SAP system with XAMS installed
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the SAP system with XAMS installed and appropriate authorization objects
  * Access to XAMS log files or the ability to export logs from XAMS



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.

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

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
        filelog:
          include:
            - /path/to/xams/logs/*.log
            - /path/to/xams/logs/*.csv
          start_at: beginning
        
        exporters:
        chronicle/xiting_xams:
          compression: gzip
          creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
          customer_id: '<customer_id>'
          endpoint: malachiteingestion-pa.googleapis.com
          log_type: XITING_XAMS
          raw_log_field: body
          ingestion_labels:
            env: production
        
        service:
        pipelines:
          logs/xams_to_chronicle:
            receivers:
              - filelog
            exporters:
              - chronicle/xiting_xams
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `filelog`: The receiver type for collecting log files from disk
    * `include`: List of file paths or glob patterns to monitor: 
      * Adjust the path to match your XAMS log export directory
      * Use glob patterns (for example, `*.log`, `*.csv`) to match multiple files
    * `start_at`: Set to `beginning` to read existing log files from the start, or `end` to only read new entries
  * **Exporter configuration:**

    * `xiting_xams`: Descriptive name for the exporter
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `XITING_XAMS`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `xams_to_chronicle`: Descriptive name for the pipeline



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
             




## Export XAMS by Xiting logs for collection

  1. Sign in to the **SAP GUI** with an account that has XAMS administrative access.
  2. Run transaction **/nXAMS** to open the XAMS dashboard.
  3. Go to **Administration > Audit Log** or **Reports > Change Log**.
  4. Configure the export parameters: 
     * **Date Range** : Select the start and end dates.
     * **Report Type** : Select the log type to export: 
       * **Authorization Changes** : Role modifications, profile assignments.
       * **Risk Analysis Results** : SoD (Segregation of Duties) violations and critical access findings.
       * **User Activity** : User creation, modification, and lock/unlock events.
  5. Click **Execute** to generate the report.
  6. Click **Export** (or use the ALV toolbar download icon) to save the data to a local file.
  7. Select the export format: **Spreadsheet** (CSV) or **Local File**.
  8. Save the exported file to the directory monitored by the Bindplane agent (for example, `/path/to/xams/logs/`).
  9. (Optional) Schedule periodic exports using SAP batch jobs to automate log file generation.

**Note:** XAMS log export requires the appropriate SAP authorization objects. Consult the XAMS by Xiting Administration Guide for required roles and permissions. Ensure the Bindplane agent has read access to the export directory.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
| extensions.auth.type | Authentication type  
hostname | intermediary.hostname | Hostname  
host_ip | intermediary.ip | IP address  
last_seen_timestamp | metadata.collected_timestamp | Timestamp when the event was collected  
event_name_value, column6 | metadata.description | Description of the event  
| metadata.event_type | Type of event  
sapEventId, column5 | metadata.product_event_type | Product-specific event type  
column4 | metadata.product_version | Product version  
devicePayloadId, shost | principal.application | Application name  
valid_source_address | principal.ip | Source IP address  
duser, cs1, suser | principal.user.user_display_name | User display name  
duser, cs1, suser | principal.user.userid | User ID  
action_value | security_result.action | Action taken  
sapClassName | security_result.category_details | Category details  
msg | security_result.description | Description  
column7 | security_result.severity | Severity level  
column7 | security_result.severity_details | Severity details  
cs3, sapParamX | target.user.user_display_name | User display name  
cs3 | target.user.userid | User ID  
column3, Security Audit Log | metadata.product_name | Product name  
column2, SAP | metadata.vendor_name | Vendor/company name  
`client` | `additional.fields` | Mapped from changelog  
`sapTsUtc` | `metadata.event_timestamp` | Mapped from changelog  
`sapClassName", "cs2` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/xiting-xams-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
