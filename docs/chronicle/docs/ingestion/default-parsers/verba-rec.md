---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/verba-rec/
title: Collect Verba Recording System logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:42:52.422973+00:00
---

# Collect Verba Recording System logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/verba-rec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Verba Recording System logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest Verba Recording System logs to Google Security Operations using Bindplane.

Verba Recording System (now Verint) is a communications compliance recording platform used for capturing and archiving voice, video, and messaging interactions. The Bindplane agent collects Verba log files directly from the local file system.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later with `observiq-otel-collector` service support
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Verba Recording System server with administrator permissions



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

Install the Bindplane agent on your Windows operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         




The service should show as **RUNNING**.

### Additional installation resources

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure Bindplane agent to ingest logs and send to Google SecOps

### Locate the configuration file

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            filelog:
                include:
                    - C:\Program Files\Verba\log\*.log
                start_at: beginning
        
        exporters:
            chronicle/verba_rec:
                compression: gzip
                creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: VERBA_REC
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/verba_to_chronicle:
                    receivers:
                        - filelog
                    exporters:
                        - chronicle/verba_rec
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `filelog`: The receiver type for collecting log files from disk
    * `include`: List of file paths to monitor. Default Verba Recording System log locations: 
      * `C:\Program Files\Verba\log\*.log`
      * `C:\Verba\log\*.log` (alternative installation path)
    * `start_at`: Set to `beginning` to read existing logs or `end` to only read new entries
  * **Exporter configuration:**

    * `verba_rec`: Descriptive name for the exporter
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `VERBA_REC`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `verba_to_chronicle`: Descriptive name for the pipeline



### Save the configuration file

  * After editing, save the file: 
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

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
         




## Configure Verba Recording System logging

Verba Recording System stores audit and compliance recording logs on the application server. You can collect logs from the file system or export them from the web console.

### Verify log file locations

  1. Sign in to the **Verba Recording System** server with administrator privileges.
  2. Navigate to the Verba log directory. Default locations include:

     * `C:\Program Files\Verba\log\`
     * `C:\Verba\log` (alternative installation path)
**Note:** The exact log path depends on your Verba installation configuration. Consult the Verba Recording System Administration Guide for your version.
  3. Ensure the Bindplane agent `include` path in `config.yaml` matches the actual log file location on your Verba server.




### (Optional) Export audit logs from Verba Web Console

  1. Sign in to the **Verba Recording System** web console as an administrator.
  2. Go to **System > Logs > Audit Trail**.
  3. Configure the search parameters: 
     * **Date Range** : Select the start and end dates.
     * **Event Category** : Select the log categories to export (for example, recording events, user activity, system events, compliance events).
     * **User** : Optionally filter by specific user.
  4. Click **Search** to retrieve the audit records.
  5. Click **Export to CSV** to download the log data.
  6. Save the exported file to the log directory monitored by the Bindplane agent (for example, `C:\Program Files\Verba\log`).

**Note:** The Bindplane agent service account must have read access to the Verba log directory.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
column2, column3, column4, column5, column7 | metadata.description | Value copied directly if not empty  
| metadata.event_type | Set to "USER_UNCATEGORIZED" if column1 or column6 not empty, else "GENERIC_EVENT"  
column1 | principal.user.userid | Value from column1 after applying regex to remove " \\([^)]+\\)$" if not empty  
column8 | security_result.action_details | Value copied directly if not empty  
column2, column3, column4, column5, column7 | security_result.detection_fields | Merged with label objects created from each column if not empty; each label has key set to specific string (e.g., "Timestamp" for column2) and value copied from column  
column9 | security_result.summary | Value copied directly if not empty  
column6 | target.user.userid | Value from column6 after applying regex to remove " \\([^)]+\\)$" if not empty  
| metadata.product_name | Set to "Verba_Recording_Systems"  
| metadata.vendor_name | Set to "Verba_Recording_Systems"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/verba-rec-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
