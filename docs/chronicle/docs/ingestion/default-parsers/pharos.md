---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pharos/
title: Collect Pharos logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:56.929646+00:00
---

# Collect Pharos logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pharos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Pharos logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Pharos logs to Google Security Operations using Bindplane.

Pharos is an on-premises print management platform for tracking, controlling, and auditing print activities across enterprise environments. Pharos Blueprint Enterprise stores print job data, user activity, and device events in a SQL Server database.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later
  * Network connectivity between the Bindplane agent and the Pharos Blueprint server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Pharos Blueprint server
  * Access to the Pharos SQL Server database or the Blueprint Administrator reporting console



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

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest logs and send to Google SecOps

  * Locate the configuration file
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          filelog:
            include:
              - 'C:\Pharos\Exports\*.csv'
            start_at: beginning
            poll_interval: 5s
        
        exporters:
          chronicle/pharos:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: PHAROS
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/pharos_to_chronicle:
              receivers:
                - filelog
              exporters:
                - chronicle/pharos
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `include`: Paths to Pharos export files: 
      * **Windows** : `C:\Pharos\Exports\*.csv`
      * Adjust the path based on where you export Pharos print activity reports
    * `start_at`: Set to `beginning` to read existing logs, or `end` to read only new entries
    * `poll_interval`: How often to check for new log data (default: `5s`)
  * **Exporter configuration:**

    * `pharos`: Descriptive name for the exporter
    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `PHAROS`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `pharos_to_chronicle`: Descriptive name for the pipeline



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/pharos:
            compression: gzip
            creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: PHAROS
            raw_log_field: body
            ingestion_labels:
              env: production
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

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
         




## Export Pharos print activity logs

Pharos Blueprint Enterprise stores print job data in a SQL Server database. You must export the data to CSV files that the Bindplane agent can read.

### Export print activity data from the Pharos SQL database

  1. On the Pharos Blueprint server, connect to the **Pharos SQL database** using SQL Server Management Studio or a command-line tool.
  2. Export print activity records using a SQL query:
         
         sqlcmd -S <sql_server> -d Pharos -Q "SELECT * FROM PrintJobLog WHERE JobDate >= DATEADD(day, -1, GETDATE())" -o "C:\Pharos\Exports\pharos_print_jobs.csv" -s "," -W
         

**Note:** Replace `<sql_server>` with your SQL Server hostname. Adjust the query and table names based on your Pharos database schema.
  3. Schedule this command to run at regular intervals (for example, every hour) using Windows Task Scheduler so the Bindplane agent continuously picks up new export files.




### Alternative: Export reports from the Blueprint Administrator console

  1. Open the **Pharos Blueprint Administrator** console.
  2. Navigate to **Insights > Reports**.
  3. Select the desired report type (for example, Print Activity, User Activity, Device Activity).
  4. Configure the date range and filters.
  5. Export the report as a CSV file to the export directory (for example, `C:\Pharos\Exports`).

**Note:** Pharos Cloud customers can access print activity data through the Pharos Cloud dashboard under **Insights > Reports** and download reports for the desired time period.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
msg.Building, msg.DataSource, msg.FactSubType, msg.FactType, msg.JobId, msg.JobName, msg.JobTimeutc, msg.PostalCode, msg.VpnConnected, mtd.customer, mtd.slt.node, mtd.slt.pipeline, mtd.source.database, mtd.timestamp.producer_process | additional.fields | Merged with Building_label if msg.Building not empty, datasource_label if msg.DataSource not empty, factsubtype_label if msg.FactSubType not empty, facttype_label if msg.FactType not empty, jobid_label if msg.JobId not empty, jobname_label if msg.JobName not empty, jobtimeutc_label if msg.JobTimeutc not empty, postalcode_label if msg.PostalCode not in ["", "Unknown"], vpnconnected_label if msg.VpnConnected not empty, customer_label if mtd.customer not empty, node_label if mtd.slt.node not empty, pipeline_label if mtd.slt.pipeline not empty, database_label if mtd.source.database not empty, producer_process_label if mtd.timestamp.producer_process not empty  
| metadata.event_type | Set to "STATUS_UPDATE" if has_principal is true, else "GENERIC_EVENT"  
msg.Application | principal.application | Value copied directly if not empty  
msg.HostName | principal.asset.hostname | Value copied directly if not empty  
msg.IPAddress | principal.asset.ip | Value copied directly if not in ["", "Unknown"]  
msg.City | principal.location.city | Value copied directly if not in ["", "Unknown"]  
msg.Country | principal.location.country_or_region | Value copied directly if not in ["", "Unknown"]  
msg.State | principal.location.state | Value copied directly if not in ["", "Unknown"]  
msg.HostName | principal.hostname | Value copied directly if not empty  
msg.IPAddress | principal.ip | Value copied directly if not in ["", "Unknown"]  
msg.UserDisplayName | principal.user.user_display_name | Value copied directly if not empty  
mtd.source.host | src.hostname | Value copied directly if not empty  
mtd.source.port | src.port | Value copied directly if not in ["", "n/a"]  
mtd.source.type | src.resource.attribute.labels | Merged with sourcetype_label if not empty  
| metadata.product_name | Set to "PHAROS"  
| metadata.vendor_name | Set to "PHAROS"  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
