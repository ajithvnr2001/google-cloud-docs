---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dmp-entre/
title: Collect DMP Entre logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:22.518877+00:00
---

# Collect DMP Entre logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dmp-entre/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect DMP Entre logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest DMP Entre logs to Google Security Operations using the Bindplane agent.

DMP Entre is an intrusion alarm monitoring and access control software from Digital Monitoring Products (DMP). It manages entry and exit points, visitor management, and physical access events. The application stores event data (badge swipes, access grants/denials, arming status changes, and alarm events) in a Microsoft SQL Server database.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later
  * Network connectivity between the Bindplane agent and the DMP Entre server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the DMP Entre system
  * Access to the Entre SQL Server database or the ability to export event reports



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

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest logs and send to Google SecOps

### Locate the configuration file

  * Locate the configuration file as follows:
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          filelog:
            include:
              - 'C:\DMP\Entre\Exports\*.csv'
            start_at: beginning
            poll_interval: 5s
        
        exporters:
          chronicle/dmp_entre:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: DMP_ENTRE
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/dmp_entre_to_chronicle:
              receivers:
                - filelog
              exporters:
                - chronicle/dmp_entre
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `include`: Paths to DMP Entre export files: 
      * **Windows** : `C:\DMP\Entre\Exports\*.csv`
      * Adjust the path based on where you export Entre event reports
    * `start_at`: Set to `beginning` to read existing logs, or `end` to read only new entries
    * `poll_interval`: How often to check for new log data (default: `5s`)
  * **Exporter configuration:**

    * `dmp_entre`: Descriptive name for the exporter
    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `DMP_ENTRE`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `dmp_entre_to_chronicle`: Descriptive name for the pipeline



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/dmp_entre:
            compression: gzip
            creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: DMP_ENTRE
            raw_log_field: body
            ingestion_labels:
              env: production
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

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
             




## Export DMP Entre event data

DMP Entre stores event data in a Microsoft SQL Server database. You must export the events to CSV files that the Bindplane agent can read.

### Export event reports from DMP Entre GUI

  1. Sign in to the **DMP Entre** application on the Entre server.
  2. Navigate to **Reports** in the Entre menu bar.
  3. Select the appropriate event report type: 
     * **Event History Report** : Contains all system events including door access, alarm events, and arming status changes.
     * **Access Activity Report** : Contains badge swipe events with user, door, and timestamp details.
     * **Alarm Activity Report** : Contains alarm, trouble, and supervisory events.
  4. Configure the report filters: 
     * **Date Range** : Select the date range for the events you want to export.
     * **Panels/Devices** : Select the specific panels or all panels.
     * **Event Types** : Select the event categories to include.
  5. Click **Generate** (or **Run**) to generate the report.
  6. Export the report as a **CSV** file to the export directory (for example, `C:\DMP\Entre\Exports`).



### Alternative: Automate database exports

For automated exports, you can query the Entre SQL Server database directly using a scheduled SQL Server Agent job or Windows Task Scheduler:

  1. Connect to the Entre SQL Server database.
  2. Export event data using the `bcp` utility:
         
         bcp "SELECT date, time, event_type, p_event_title, p_event_action, user_display_name, userid, device_data, principal_host, data, log_level FROM [EntreDB].[dbo].[EventHistory] WHERE date >= DATEADD(day, -1, GETDATE())" queryout "C:\DMP\Entre\Exports\entre_events.csv" -c -t"," -S localhost -T
         

**Note:** Replace `[EntreDB]` with the actual Entre database name and adjust the table/column names according to your Entre version.
  3. Schedule this command to run at regular intervals (for example, every hour) using Windows Task Scheduler so the Bindplane agent continuously picks up new export files.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
date, time | metadata.event_timestamp | Concatenated from date and time, parsed using formats M/d/yyyy HH:mm:ss, MM/d/yyyy HH:mm:ss, etc.  
event_type | metadata.event_type | Value copied directly  
p_event_type | metadata.description | Set to p_event_type if event_type == "GENERIC_EVENT"  
| metadata.product_name | Set to "ENTRE"  
| metadata.vendor_name | Set to "DMP"  
p_event_title, p_event_action | event_type | Set to "GENERIC_EVENT" by default; "SETTING_MODIFICATION" if p_event_title == "arming status" or p_event_action == "set time"; "STATUS_HEARTBEAT" if p_event_action == "automatic recall test ok" or matches door locked/unlocked or zone open/closed/forced open; "USER_BADGE_IN" if p_event_title == "door access" and p_event_action == "door access granted"  
| extensions.auth.mechanism | Set to "BADGE_READER" for USER_BADGE_IN event  
| extensions.auth.type | Set to "PHYSICAL" for USER_BADGE_IN event  
inter_host | intermediary.hostname | Set if inter_host is not convertible to IP  
inter_host | intermediary.ip | Set if inter_host is convertible to IP  
principal_host, inter_host | principal.hostname | Value from principal_host if device_data present and principal_host not convertible to IP; else if principal empty and inter_host not convertible to IP, from inter_host  
principal_host, inter_host | principal.ip | Value from principal_host if convertible to IP; else if principal empty, from inter_ip  
device_data | principal.location.name | Value copied directly  
user_display_name | principal.user.user_display_name | Value copied directly  
userid | principal.user.userid | Value copied directly  
data | security_result.description | Value copied directly  
log_level | security_result.severity | Set to "LOW" if "INFO", "MEDIUM" if "WARNING", "HIGH" if "ERROR"  
log_level | security_result.severity_details | Value copied directly  
p_event_type | security_result.summary | Value copied directly  
device_data | target.location.name | Set for USER_BADGE_IN event  
| target.resource.name | Set to "Arming status" if p_event_title == "arming status"; "Panel command" if p_event_action == "set time"  
| target.resource.type | Set to "SETTING" for SETTING_MODIFICATION event  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
