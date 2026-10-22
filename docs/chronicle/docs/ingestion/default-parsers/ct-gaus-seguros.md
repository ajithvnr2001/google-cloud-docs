---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ct-gaus-seguros/
title: Collect Colinet Trotta GAUS SEGUROS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:15.984043+00:00
---

# Collect Colinet Trotta GAUS SEGUROS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ct-gaus-seguros/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Colinet Trotta GAUS SEGUROS logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Colinet Trotta GAUS SEGUROS logs to Google Security Operations using the Bindplane agent.

Colinet Trotta GAUS SEGUROS is an insurance management platform developed by Colinet Trotta S.A. (Argentina). It generates user activity and audit logs, including user account details, login events, and system operations. The platform does not provide public documentation for log export; the export process depends on your specific GAUS deployment and requires coordination with Colinet Trotta's technical support team.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the GAUS SEGUROS server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Colinet Trotta GAUS SEGUROS platform with administrator permissions
  * Access to the GAUS SEGUROS database or reporting module for log export



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
          filelog:
            include:
              - /path/to/gaus-seguros-logs/*.log
            start_at: beginning
        
        exporters:
          chronicle/ct_gaus_seguros:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: CT_GAUS_SEGUROS
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/ct_gaus_seguros_to_chronicle:
              receivers:
                - filelog
              exporters:
                - chronicle/ct_gaus_seguros
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `filelog`: The receiver type for collecting log files from disk
    * `include`: List of file paths or glob patterns to monitor: 
      * Adjust the path to match your GAUS SEGUROS log file location
      * Use glob patterns (for example, `*.log`, `*.csv`) to match multiple files
    * `start_at`: Set to `beginning` to read existing log files from the start, or `end` to only read new entries
  * **Exporter configuration:**

    * `ct_gaus_seguros`: Descriptive name for the exporter
    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `CT_GAUS_SEGUROS`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `ct_gaus_seguros_to_chronicle`: Descriptive name for the pipeline



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/ct_gaus_seguros:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CT_GAUS_SEGUROS
            raw_log_field: body
            ingestion_labels:
              env: production
        


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
             




## Export GAUS SEGUROS logs for collection

  1. Contact your **Colinet Trotta account representative** or **GAUS SEGUROS system administrator** to identify the available log export methods for your deployment.
  2. Common approaches for exporting audit data from GAUS SEGUROS include: 
     * **Database export** : GAUS stores user and audit data in a relational database. Your database administrator can export the relevant tables (for example, user account tables with columns for user ID, display name, email, status, and timestamps) as CSV or delimited text files.
     * **Application-level export** : If your GAUS deployment includes a reporting or audit module, use it to generate periodic audit reports and export them as files.
  3. Save the exported log files to the directory monitored by the Bindplane agent (for example, `/path/to/gaus-seguros-logs/`).
  4. (Optional) Schedule regular exports using a cron job or Windows Task Scheduler to automate log file generation.

**Note:** Based on the log parser, GAUS SEGUROS logs are expected in a column-delimited format with fields such as user ID, display name, description, email, and various user attribute fields. Ensure your export matches this format for successful parsing in Google SecOps.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`column3` | `metadata.description` | Directly mapped  
`column7` | `metadata.description` | Directly mapped  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`column10_label` | `principal.user.attribute.labels` | Merged  
`column11_label` | `principal.user.attribute.labels` | Merged  
`column12_label` | `principal.user.attribute.labels` | Merged  
`column13_label` | `principal.user.attribute.labels` | Merged  
`column14_label` | `principal.user.attribute.labels` | Merged  
`column15_label` | `principal.user.attribute.labels` | Merged  
`column16_label` | `principal.user.attribute.labels` | Merged  
`column17_label` | `principal.user.attribute.labels` | Merged  
`column18_label` | `principal.user.attribute.labels` | Merged  
`column19_label` | `principal.user.attribute.labels` | Merged  
`column20_label` | `principal.user.attribute.labels` | Merged  
`column21_label` | `principal.user.attribute.labels` | Merged  
`column22_label` | `principal.user.attribute.labels` | Merged  
`column23_label` | `principal.user.attribute.labels` | Merged  
`column24_label` | `principal.user.attribute.labels` | Merged  
`column25_label` | `principal.user.attribute.labels` | Merged  
`column26_label` | `principal.user.attribute.labels` | Merged  
`column27_label` | `principal.user.attribute.labels` | Merged  
`column28_label` | `principal.user.attribute.labels` | Merged  
`column29_label` | `principal.user.attribute.labels` | Merged  
`column30_label` | `principal.user.attribute.labels` | Merged  
`column31_label` | `principal.user.attribute.labels` | Merged  
`column32_label` | `principal.user.attribute.labels` | Merged  
`column33_label` | `principal.user.attribute.labels` | Merged  
`column34_label` | `principal.user.attribute.labels` | Merged  
`column35_label` | `principal.user.attribute.labels` | Merged  
`column36_label` | `principal.user.attribute.labels` | Merged  
`column37_label` | `principal.user.attribute.labels` | Merged  
`column38_label` | `principal.user.attribute.labels` | Merged  
`column39_label` | `principal.user.attribute.labels` | Merged  
`column6_label` | `principal.user.attribute.labels` | Merged  
`column7_label` | `principal.user.attribute.labels` | Merged  
`column8_label` | `principal.user.attribute.labels` | Merged  
`column9_label` | `principal.user.attribute.labels` | Merged  
`type_label` | `principal.user.attribute.labels` | Merged  
`column5` | `principal.user.email_addresses` | Mapped: `^.+@.+$` → `column5`  
`column1` | `principal.user.product_object_id` | Directly mapped  
`column3` | `principal.user.product_object_id` | Directly mapped  
`column2` | `principal.user.user_display_name` | Directly mapped  
`column1` | `principal.user.userid` | Directly mapped  
`column4` | `principal.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `USER_UNCATEGORIZED`  
N/A | `metadata.product_name` | Constant: `GAUS SEGUROS`  
N/A | `metadata.vendor_name` | Constant: `Colinet Trotta`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ct-gaus-seguros-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
