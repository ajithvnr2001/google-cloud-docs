---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/teradata-db/
title: Collect Teradata Database logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:20.112625+00:00
---

# Collect Teradata Database logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/teradata-db/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Teradata Database logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Teradata Database logs to Google Security Operations using Bindplane.

Teradata Database is an enterprise data warehouse platform that generates query, access, security audit, and system event logs. It provides high-performance analytics and data management for large-scale on-premise deployments.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Teradata Database server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Teradata Database system with administrator permissions



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
          tcplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/teradata_db:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: TERADATA_DB
            raw_log_field: body
        
        service:
          pipelines:
            logs/teradata_db_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/teradata_db
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/teradata_db:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: TERADATA_DB
            raw_log_field: body
        


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
         




## Configure Teradata Database syslog forwarding

  1. Sign in to the **Teradata Database** server as an administrator.
  2. Configure syslog forwarding using the Teradata Database Gateway logging facility. Edit the rsyslog configuration file:
         
         sudo nano /etc/rsyslog.d/teradata.conf
         

  3. Add the following lines to forward Teradata logs to the Bindplane agent:
         
         # Forward Teradata Database logs to Bindplane agent
         if $programname == 'teradata' then @@<bindplane-ip>:514
         

     * Replace `<bindplane-ip>` with the IP address of the Bindplane agent host.
  4. Restart the rsyslog service:
         
         sudo systemctl restart rsyslog
         

  5. Verify that logs are being sent by checking the Bindplane agent logs.

**Note:** Alternatively, you can use Teradata Parallel Transporter (TPT) or BTEQ to export log data from system tables (`DBC.DBQLogTbl`, `DBC.AccLogTbl`, `DBC.EventLog`) and forward them via a syslog agent.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
| additional.fields | Merged from various labels like collect_timestamp_label, logon_date_time_label, logon_source_label, protocol_label, remote_hostname_label, logon_details_label, port_label, connection_id_label, cid_label, jdbc_driver_info_label, request_mode_label, statement_group_label, statement_type_label  
app_id | target.asset.product_object_id | Value copied directly  
client_addr | principal.asset.hostname, principal.asset.ip, principal.hostname, principal.ip | Value copied directly to all  
client_id | target.asset.asset_id | Concatenated as CLIENT_ID:%{client_id}  
collect_timestamp | metadata.collected_timestamp | Converted using date match with formats RFC 3339, UNIX_MS, UNIX, ISO8601, yyyy-MM-dd HH:mm:ss  
default_database | target.resource.name, target.resource.resource_type | Value copied directly to name; set to DATABASE for resource_type  
error_code | network.http.response_code, additional.fields | Converted to integer for response_code; copied to error_code_label merged into additional.fields  
error_text | security_result.summary | Value copied directly  
host_name | principal.asset.hostname, principal.hostname | Value copied directly to both  
logon_date_time | metadata.event_timestamp | Converted using date match with formats ISO8601, yyyy-MM-dd HH:mm:ss  
logon_source | target.resource.parent | Value copied directly  
logon_source | additional.fields | Extracted logonSource using grok, then set as %{logonSource}LSS in logon_source_label merged into additional.fields  
logon_source | additional.fields | Extracted protocol, remote_hostname, port, logon_details, connection_id, cid, jdbc_driver_info using grok, then set in respective labels merged into additional.fields  
proc_id | target.resource.id | Value copied directly  
profile_name | target.resource.attribute.labels | Set in profile_name_label merged into attribute.labels  
query_text | target.process.command_line | Value copied directly  
request_mode | target.resource.resource_subtype, additional.fields | Value copied directly to resource_subtype; set in request_mode_label merged into additional.fields  
session_id | network.session_id | Value copied directly  
statement_group | principal.user.groupid, additional.fields | Value copied directly to groupid; set in statement_group_label merged into additional.fields  
statement_type | security_result.about.labels, additional.fields | Set in statementtype_value_label merged into about.labels; set in statement_type_label merged into additional.fields  
ts | metadata.event_timestamp | Converted using date match with formats MMM d HH:mm:ss, MMM dd HH:mm:ss, SYSLOGTIMESTAMP, RFC 3339, UNIX, ISO8601, UNIX_MS  
tt_granularity | target.resource.product_object_id | Value copied directly  
user_id | principal.user.userid | Value copied directly  
user_name | principal.user.user_display_name | Value copied directly  
| metadata.event_type | Set to USER_RESOURCE_ACCESS if has_principal, has_principal_user, has_target_resource true; else STATUS_UPDATE if has_principal true; else GENERIC_EVENT  
| metadata.product_name | Set to "TERADATA_DB"  
| metadata.vendor_name | Set to "TERADATA"  
`profile_name` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`proc_id` | `event.idm.read_only_udm.target.resource.id` | Mapped from changelog  
`user_id` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`collect_timestamp` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`logon_date_time` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`user_name` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`logon_source` | `event.idm.read_only_udm.target.resource.parent` | Mapped from changelog  
`app_id` | `event.idm.read_only_udm.target.asset.product_object_id` | Mapped from changelog  
`client_id` | `event.idm.read_only_udm.target.asset.asset_id` | Mapped from changelog  
`error_code` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`statement_type` | `event.idm.read_only_udm.security_result.about.labels` | Mapped from changelog  
`statement_group` | `event.idm.read_only_udm.principal.user.groupid` | Mapped from changelog  
`request_mode` | `event.idm.read_only_udm.target.resource.resource_subtype` | Mapped from changelog  
`tt_granularity` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`protocol` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`remote_hostname` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logon_details` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`connection_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`port` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`jdbc_driver_info` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`app_id` | `principal.application` | Mapped from changelog  
`collect_timestamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`error_code` | `security_result.detection_fields` | Mapped from changelog  
`logon_date_time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logon_source` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`proc_id` | `principal.process.pid` | Mapped from changelog  
`request_mode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`statement_group` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`statement_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_id` | `target.user.userid` | Mapped from changelog  
`user_name` | `target.user.user_display_name` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/teradata-db-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
