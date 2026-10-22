---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tableau/
title: Collect Tableau logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:07.567152+00:00
---

# Collect Tableau logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tableau/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Tableau logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Tableau logs to Google Security Operations using Bindplane.

Tableau is a business intelligence and data visualization platform that generates user activity, authentication, and audit logs. Tableau Server stores log files on the server file system, making file-based collection ideal for ingestion.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Tableau Server host
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Tableau Server with administrator permissions
  * Access to Tableau Server log files on the server file system



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

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure Bindplane agent to ingest syslog and send to Google SecOps

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
              - /var/opt/tableau/tableau_server/data/tabsvc/logs/httpd/access.*.log
              - /var/opt/tableau/tableau_server/data/tabsvc/logs/vizqlserver/*.log
              - /var/opt/tableau/tableau_server/data/tabsvc/logs/backgrounder/*.log
            start_at: beginning
        
        exporters:
          chronicle/tableau:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: TABLEAU
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/tableau_to_chronicle:
              receivers:
                - filelog
              exporters:
                - chronicle/tableau
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `filelog`: The receiver type for collecting log files from disk
    * `include`: List of file paths or glob patterns to monitor: 
      * **Linux** : `/var/opt/tableau/tableau_server/data/tabsvc/logs/`
      * **Windows** : `C:\ProgramData\Tableau\Tableau Server\data\tabsvc\logs\`
      * Key log files include `httpd/access.*.log` (Apache access logs), `vizqlserver/*.log` (VizQL server logs), and `backgrounder/*.log` (background task logs)
      * Adjust the paths to match your Tableau Server installation
    * `start_at`: Set to `beginning` to read existing log files from the start, or `end` to only read new entries
  * **Exporter configuration:**

    * `tableau`: Descriptive name for the exporter
    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `TABLEAU`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)



**Pipeline configuration:** * `tableau_to_chronicle`: Descriptive name for the pipeline

### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/tableau:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: TABLEAU
            raw_log_field: body
            ingestion_labels:
              env: production
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

To restart the Bindplane agent in Linux: 

  1. Run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. Verify the service is running:
         
         sudo systemctl status observiq-otel-collector
         

  3. Check logs for errors:
         
         sudo journalctl -u observiq-otel-collector -f
         




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
         




## Verify Tableau Server log file locations

  1. Sign in to the Tableau Server host with administrator privileges.
  2. Verify the log file directories: 
     * **Linux** : `/var/opt/tableau/tableau_server/data/tabsvc/logs/`
     * **Windows** : `C:\ProgramData\Tableau\Tableau Server\data\tabsvc\logs\`
  3. Key log subdirectories and files: 
     * `httpd/access.*.log`: Apache access logs with HTTP request details
     * `vizqlserver/*.log`: VizQL server logs with visualization query activity
     * `backgrounder/*.log`: Background task logs with scheduled job activity
  4. (Optional) Generate a log archive using the TSM command-line tool for verification:
         
         tsm maintenance ziplogs -a -t -o -f tableau-logs.zip
         

**Note:** The `-a` flag includes all logs, `-t` includes temp files, `-o` overwrites existing archive. The archive is saved to `/var/opt/tableau/tableau_server/data/tabsvc/files/backups/` (Linux) or `C:\ProgramData\Tableau\Tableau Server\data\tabsvc\files\backups` (Windows).
  5. Update the `include` paths in the Bindplane agent `config.yaml` if the log directory differs from the defaults.

**Note:** Ensure the Bindplane agent has read access to the Tableau Server log directories.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
dataserver_permissions, local_dataserver, saved_credentials_viewerid, locale, server_oauth, :id, server_viewerid, dataserver_version, tablename, ElapsedTime, LastStatus, Timeszone | additional.fields | Merged key-value pairs from specified fields  
Content | metadata.description | Value copied directly after removing "_"  
ID, RemoteHost | metadata.event_type | Set to USER_UNCATEGORIZED if ID not empty, STATUS_UPDATE if RemoteHost present, GENERIC_EVENT otherwise  
protocol | network.application_protocol | Value copied directly  
http_version | network.application_protocol_version | Value copied directly  
method | network.http.method | Value copied directly after removing ""  
SizeBytes | network.received_bytes | Converted to uinteger  
session_id | network.session_id | Value copied directly  
Workername | principal.asset.hostname | Value copied directly  
RemoteHost | principal.asset.ip | Value copied directly  
Workername | principal.hostname | Value copied directly  
RemoteHost | principal.ip | Value copied directly  
Port | principal.nat_port | Converted to integer  
ID | principal.user.product_object_id | Value copied directly  
RemoteUser | principal.user.userid | Value copied directly if not empty or "_"  
logging_ctx | security_result.detection_fields | Merged key-value pair from logging_ctx  
path | target.file.full_path | Value copied directly  
dbname | target.resource.name | Value copied directly  
| metadata.product_name | Set to "Tableau"  
| metadata.vendor_name | Set to "TABLEAU"  
`temp_user` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`user_name` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`temp_domain` | `event.idm.read_only_udm.principal.administrative_domain` | Mapped from changelog  
`temp_role` | `event.idm.read_only_udm.principal.user.attribute.roles` | Mapped from changelog  
`source_info` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_application` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`temp_http_uri` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`temp_api_call` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`temp_site_id` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`java_method` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`java_class` | `event.idm.read_only_udm.target.resource.type` | Mapped from changelog  
`temp_http_method` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`temp_http_status` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`"Computer"` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`"TimeGenerated"` | `event.idm.read_only_udm.security_result.first_discovered_time` | Mapped from changelog  
`"_TimeReceived"` | `event.idm.read_only_udm.security_result.last_discovered_time` | Mapped from changelog  
`"_IsBillable"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`"_BilledSize"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`"_Internal_WorkspaceResourceId"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`"_ItemId"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`"TenantId"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`"_SubscriptionId"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`"_ResourceId"` | `event.idm.read_only_udm.principal.resource.id` | Mapped from changelog  
`"FilePath"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`"Type"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`"temp_message"` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`"temp_logger_name"` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`"temp_pid"` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`"temp_thread_name"` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`"temp_log_level"` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`appname` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`id2` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`pid` | `event.idm.read_only_udm.observer.process.pid` | Mapped from changelog  
`timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`user` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`id1` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`logger` | `event.idm.read_only_udm.observer.process.command_line` | Mapped from changelog  
`loglevel` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`user_id` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`site_id` | `event.idm.read_only_udm.target.resource.id` | Mapped from changelog  
`message` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`script_type` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`id3` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`thread` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`function_name` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tableau-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
