---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyolo-ot/
title: Collect Cyolo OT logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:40:14.094850+00:00
---

# Collect Cyolo OT logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyolo-ot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cyolo OT logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cyolo Secure Remote Access for OT logs to Google Security Operations using the Bindplane agent.

Cyolo provides secure remote access for operational technology (OT) environments. The platform generates syslog messages for access events, authentication, and session activities. The parser extracts fields and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Cyolo platform
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Cyolo Admin console



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
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/cyolo_ot:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: CYOLO_OT
            raw_log_field: body
        
        service:
          pipelines:
            logs/cyolo_ot_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/cyolo_ot
        




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
          chronicle/cyolo_ot:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CYOLO_OT
            raw_log_field: body
        


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
             




## Configure syslog on Cyolo

  1. Sign in to the **Cyolo** Admin console.
  2. Go to **Monitoring > Settings**.
  3. Toggle **on** the **Export Logs to System Logging Protocol (Syslog)**.
  4. Go to **Integrations > Syslog Server**.
  5. Provide the following configuration details: 
     * **Server name** : Enter a meaningful name for this server (for example, `Google SecOps Bindplane`).
     * **Sites** : Select a single **site** or **multiple sites** from the drop-down.
     * **IP Address** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number for UDP connection.
  6. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`_field` | `additional.fields` | Merged  
`authority_id_label` | `additional.fields` | Merged  
`authority_kind_label` | `additional.fields` | Merged  
`authority_name_label` | `additional.fields` | Merged  
`data_field` | `additional.fields` | Merged  
`duration_label` | `additional.fields` | Merged  
`kind_label` | `additional.fields` | Merged  
`log_level_label` | `additional.fields` | Merged  
`object_id_label` | `additional.fields` | Merged  
`object_kind_label` | `additional.fields` | Merged  
`object_name_label` | `additional.fields` | Merged  
`rules_label` | `additional.fields` | Merged  
`site_id_label` | `additional.fields` | Merged  
`subject_id_label` | `additional.fields` | Merged  
`subject_kind_label` | `additional.fields` | Merged  
`message` | `extensions.auth.type` | Mapped: `user disconnected` → `MACHINE`  
`syslog_object_name` | `extensions.auth.type` | Mapped: `login` → `MACHINE`  
`inter_host` | `intermediary.asset.hostname` | Directly mapped  
`inter_host` | `intermediary.hostname` | Directly mapped  
`message` | `metadata.description` | Directly mapped  
`msg` | `metadata.description` | Directly mapped  
`syslog_message` | `metadata.description` | Directly mapped  
`syslog_timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`time` | `metadata.event_timestamp` | Parsed as `MMM d HH:mm:ss`  
`timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`event_type` | `metadata.event_type` | Directly mapped  
`kind` | `metadata.product_event_type` | Directly mapped  
`prod_type` | `metadata.product_event_type` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`syslog_event_id` | `metadata.product_log_id` | Directly mapped  
`product_version` | `metadata.product_version` | Directly mapped  
`message` | `network.application_protocol` | Mapped: `rdp` → `RDP`  
`client` | `network.http.parsed_user_agent` | Directly mapped  
`cyolouagent` | `network.http.parsed_user_agent` | Directly mapped  
`client` | `network.http.user_agent` | Directly mapped  
`cyolouagent` | `network.http.user_agent` | Directly mapped  
`syslog_client` | `network.http.user_agent` | Directly mapped  
`cyolosessionid` | `network.session_id` | Directly mapped  
`session_id` | `network.session_id` | Directly mapped  
`hostname` | `observer.hostname` | Directly mapped  
`container_id_label` | `observer.resource.attribute.labels` | Merged  
`internal_event_id_label` | `observer.resource.attribute.labels` | Merged  
`log_source_label` | `observer.resource.attribute.labels` | Merged  
`site_id_label` | `observer.resource.attribute.labels` | Merged  
`site_name_label` | `observer.resource.attribute.labels` | Merged  
`transaction_id_label` | `observer.resource.attribute.labels` | Merged  
`node_id` | `observer.resource.product_object_id` | Directly mapped  
`syslog_hostname` | `principal.asset.hostname` | Directly mapped  
`remote_address` | `principal.asset.ip` | Merged  
`syslog_remote_address` | `principal.asset.ip` | Merged  
`syslog_hostname` | `principal.hostname` | Directly mapped  
`remote_address` | `principal.ip` | Merged  
`syslog_remote_address` | `principal.ip` | Merged  
`country_code` | `principal.location.country_or_region` | Directly mapped  
`cyolocountrycode` | `principal.location.country_or_region` | Directly mapped  
`syslog_country_code` | `principal.location.country_or_region` | Directly mapped  
`node_id_label` | `principal.resource.attribute.labels` | Merged  
`site_name_label` | `principal.resource.attribute.labels` | Merged  
`transaction_id_label` | `principal.resource.attribute.labels` | Merged  
`cyolosubjectkind` | `principal.resource.resource_subtype` | Directly mapped  
`credentials_id_label` | `principal.user.attribute.labels` | Merged  
`credentials_name_label` | `principal.user.attribute.labels` | Merged  
`credentials_origin_label` | `principal.user.attribute.labels` | Merged  
`cyolosubjectid` | `principal.user.product_object_id` | Directly mapped  
`subject_id` | `principal.user.product_object_id` | Directly mapped  
`syslog_session_id` | `principal.user.product_object_id` | Directly mapped  
`cyolosubjectname` | `principal.user.userid` | Directly mapped  
`subject_name` | `principal.user.userid` | Directly mapped  
`syslog_id` | `principal.user.userid` | Directly mapped  
`action` | `security_result.action` | Merged  
`result` | `security_result.action` | Mapped: `failure` → `sr_action`, `success` → `sr_action`  
`sr_action` | `security_result.action` | Merged  
`syslog_result` | `security_result.action_details` | Directly mapped  
`_field` | `security_result.detection_fields` | Merged  
`field` | `security_result.detection_fields` | Merged  
`key` | `security_result.detection_fields` | Mapped: `"cyoloauthkind", "cyolokind","cyoloresult"` → `_field`  
`result` | `security_result.outcome` | Mapped: `failure` → `FAIL`, `success` → `PASS`  
`authority_id` | `security_result.rule_id` | Directly mapped  
`cyoloauthid` | `security_result.rule_id` | Directly mapped  
`authority_name` | `security_result.rule_name` | Directly mapped  
`cyoloauthname` | `security_result.rule_name` | Directly mapped  
`severity` | `security_result.severity` | Mapped: `1` → `LOW`  
`cyoloobjname` | `target.application` | Directly mapped  
`object_name` | `target.application` | Directly mapped  
`asset_id` | `target.asset.asset_id` | Directly mapped  
`destination_host` | `target.asset.hostname` | Directly mapped  
`dst` | `target.asset.ip` | Merged  
`asset_name` | `target.asset.product_object_id` | Directly mapped  
`destination_host` | `target.hostname` | Directly mapped  
`dst` | `target.ip` | Merged  
`destination_port` | `target.port` | Directly mapped  
`_field` | `target.resource.attribute.labels` | Merged  
`key` | `target.resource.attribute.labels` | Mapped: `cyolodstid` → `_field`  
`cyoloobjid` | `target.resource.product_object_id` | Directly mapped  
`object_id` | `target.resource.product_object_id` | Directly mapped  
`cyoloobjkind` | `target.resource.resource_subtype` | Directly mapped  
`syslog_subject_name` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `MACHINE`  
N/A | `metadata.product_name` | Constant: `CYOLO_OT`  
N/A | `metadata.vendor_name` | Constant: `CYOLO_OT`  
N/A | `network.application_protocol` | Constant: `RDP`  
N/A | `network.http.parsed_user_agent` | Constant: `parseduseragent`  
N/A | `security_result.outcome` | Constant: `FAIL`  
N/A | `security_result.severity` | Constant: `LOW`  
`inter_host` | `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`cyolosubjectname` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`cyolocountrycode` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`cyolosubjectid` | `event.idm.read_only_udm.principal.user.product_object_id` | Mapped from changelog  
`dst` | `event.idm.read_only_udm.target.ip`and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`cyoloobjname` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`cyoloobjid` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`cyolosessionid` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`cyolouagent` | `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
`cyoloauthid` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`cyoloauthname` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`cyolosubjectkind` | `event.idm.read_only_udm.principal.resource.resource_subtype` | Mapped from changelog  
`cyoloobjkind` | `event.idm.read_only_udm.target.resource.resource_subtype` | Mapped from changelog  
`prod_type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`cyoloauthkind` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`cyolokind` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`cyoloresult` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`cyolodstid` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`cef_version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Signature_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cef_severity` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`start` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`act` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cyolotransid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cyolocredentialsorigin` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cyolocredentialsid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cyolocredentialsname` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`time` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`remote_address` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`remote_address` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`country_code` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`destination_host` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`destination_host` | `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`destination_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`message` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`subject_name` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`subject_id` | `event.idm.read_only_udm.principal.user.product_object_id` | Mapped from changelog  
`timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`object_name` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`object_id` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`session_id` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`duration_str` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`message` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`subject_kind` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`authority_kind` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`log_level` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`object_kind` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`client` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`client` | `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
`authority_id` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`authority_name` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`rules` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.observer.hostname` | Mapped from changelog  
`node_id` | `event.idm.read_only_udm.observer.resource.product_object_id` | Mapped from changelog  
`site_id` | `event.idm.read_only_udm.observer.resource.attribute.labels` | Mapped from changelog  
`log_source` | `event.idm.read_only_udm.observer.resource.attribute.labels` | Mapped from changelog  
`site_name` | `event.idm.read_only_udm.observer.resource.attribute.labels` | Mapped from changelog  
`container_id` | `event.idm.read_only_udm.observer.resource.attribute.labels` | Mapped from changelog  
`transaction_id` | `event.idm.read_only_udm.observer.resource.attribute.labels` | Mapped from changelog  
`event_id` | `event.idm.read_only_udm.observer.resource.attribute.labels` | Mapped from changelog  
`kind` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`syslog_timestamp` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyolo-ot-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
