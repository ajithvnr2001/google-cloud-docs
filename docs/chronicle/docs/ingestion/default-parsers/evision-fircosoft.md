---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/evision-fircosoft/
title: Collect Evision FircoSoft logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:46:22.907415+00:00
---

# Collect Evision FircoSoft logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/evision-fircosoft/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Evision FircoSoft logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Evision FircoSoft logs to Google Security Operations using the Bindplane agent.

Evision FircoSoft (now part of LexisNexis Risk Solutions as Firco Compliance Link) is an on-premises financial crime compliance screening platform for financial institutions. It detects sanctions violations, PEP matches, and AML risks in transactions and messages. The application stores audit records including screening decisions, user access events, table access events, and configuration changes as log files on the local file system.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later with `observiq-otel-collector` service support
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the FircoSoft (Firco Compliance Link) server and its log directory



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

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest logs and send to Google SecOps

### Locate the configuration file

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            filelog:
                include:
                    - C:\FircoSoft\logs\*.log
                start_at: beginning
        
        exporters:
            chronicle/evision_fircosoft:
                compression: gzip
                creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: EVISION_FIRCOSOFT
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/fircosoft_to_chronicle:
                    receivers:
                        - filelog
                    exporters:
                        - chronicle/evision_fircosoft
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `filelog`: The receiver type for collecting log files from disk
    * `include`: List of file paths to monitor. Set this to the location where FircoSoft writes its log files (for example, `C:\FircoSoft\logs\*.log`). Adjust the path to match your installation directory
    * `start_at`: Set to `beginning` to read existing logs or `end` to only read new entries
  * **Exporter configuration:**

    * `evision_fircosoft`: Descriptive name for the exporter
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `EVISION_FIRCOSOFT`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `fircosoft_to_chronicle`: Descriptive name for the pipeline



### Save the configuration file

  * After editing, save the file: 
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

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
             




## Identify FircoSoft log file locations

FircoSoft (Firco Compliance Link) writes audit and operational log files to the local file system. The exact location depends on your installation configuration.

  1. Common default log directories:

     * `C:\FircoSoft\logs\`
     * `C:\Program Files\FircoSoft\Firco Compliance Link\logs\`
     * A custom directory configured during installation
  2. To determine the log directory for your deployment:

     1. Sign in to the **FircoSoft** (Firco Compliance Link) administration console.
     2. Go to **Administration > System Configuration** (or **Server Settings**).
     3. Locate the **Log directory** or **Output directory** setting.
     4. Note the configured path.
  3. FircoSoft typically writes the following log file types:

     * Audit trail logs (user access, screening decisions, configuration changes)
     * Statistics logs (transaction screening volumes and results)
     * Application operational logs
  4. Update the `include` path in the Bindplane agent `config.yaml` to match the actual log directory on your server:
         
         receivers:
             filelog:
                 include:
                     - C:\FircoSoft\logs\*.log
         

     * Replace `C:\FircoSoft\logs` with the actual path from step 2.
     * Use wildcard patterns (`*.log`, `*.txt`, `*.xml`) to match the log file format used in your deployment.
**Note:** The Bindplane agent service account must have read access to the log directory. FircoSoft log files may be in delimited text or XML format depending on the deployment configuration.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
date, time | metadata.event_timestamp | Converted using format: yyyy-MM-dd HH:mm:ss.SSS  
| metadata.event_type | Set to "USER_RESOURCE_ACCESS"  
nature | metadata.product_event_type | Set to "Estadisticas" if nature == "C", else "Otros" if nature == "A"  
user | principal.user.userid | Value copied directly  
success | security_result.action | Set to "ALLOW" if success =~ "SI", else "BLOCK" if success =~ "NO"  
details | security_result.action_details | Value copied directly  
table | target.resource.name | Value copied directly  
| metadata.product_name | Set to "Fircosoft"  
| metadata.vendor_name | Set to "eVision"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/evision-fircosoft-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
