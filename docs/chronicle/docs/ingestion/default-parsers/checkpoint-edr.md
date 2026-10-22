---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-edr/
title: Collect Check Point EDR logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:28.029636+00:00
---

# Collect Check Point EDR logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-edr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Check Point EDR logs

**Parser Version:** 20.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Check Point EDR (SandBlast) logs to Google Security Operations using the Bindplane agent.

Check Point EDR generates logs for endpoint threat detection, process activity, file events, and network connections. The parser extracts CEF and key-value fields and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Check Point appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Check Point Appliance with SandBlast



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

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

**Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/checkpoint_edr:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: CHECKPOINT_EDR
            raw_log_field: body
        
        service:
          pipelines:
            logs/checkpoint_edr_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/checkpoint_edr
        




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
          chronicle/checkpoint_edr:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CHECKPOINT_EDR
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
             




## Configure syslog in Check Point 1500 Appliance Series

  1. Sign in to the **Checkpoint Appliance**.
  2. Go to **Logs & Monitoring > Log Servers > Syslog Servers**.
  3. Click **Configure**.
  4. Provide the following configuration details: 
     * **Protocol** : Select **UDP**.
     * **Name** : Enter a descriptive name.
     * **IP Address** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number.
     * Select **Enable** log server.
     * Select logs to forward: Both system and security logs.
  5. Click **Apply**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`action` | `event.idm.read_only_udm.security_result.action` | Directly mapped from the `action` CEF field.  
`action_comment` | `event.idm.read_only_udm.additional.fields[<N>].key`: `action_comment`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `action_comment` | Directly mapped from the `action_comment` field.  
`action_details` | `event.idm.read_only_udm.security_result.action_details` | Directly mapped from the `action_details` CEF field.  
`additional_info` | `event.idm.read_only_udm.additional.fields[<N>].key`: `additional_info`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `additional_info` | Directly mapped from the `additional_info` field.  
`am_update_proxy` | `event.idm.read_only_udm.intermediary.domain.name` | Directly mapped from the `am_update_proxy` field.  
`am_update_source` | `event.idm.read_only_udm.target.url` | Directly mapped from the `am_update_source` field.  
`client_version` | `event.idm.read_only_udm.metadata.product_version` | Directly mapped from the `client_version` field.  
`cn1` | `event.idm.read_only_udm.security_result.severity` | Mapped from the `cn1` CEF field and converted to UDM severity values (CRITICAL, HIGH, MEDIUM, LOW, INFO).  
`cs1` | `event.idm.read_only_udm.additional.fields[<N>].key`: `Connectivity State`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `cs1` | Directly mapped from the `cs1` field.  
`description` | `event.idm.read_only_udm.metadata.description` | Directly mapped from the `description` CEF field.  
`deviceDirection` | `event.idm.read_only_udm.network.direction` | Mapped from the `deviceDirection` field. A value of `0` is mapped to `INBOUND`, other values are not mapped.  
`deviceFacility` | `event.idm.read_only_udm.additional.fields[<N>].key`: `deviceFacility`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `deviceFacility` | Directly mapped from the `deviceFacility` field.  
`dst` | `event.idm.read_only_udm.network.target.ip` | Directly mapped from the `dst` field when `event_type` is `Firewall`.  
`engine_ver` | `event.idm.read_only_udm.additional.fields[<N>].key`: `engine_ver`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `engine_ver` | Directly mapped from the `engine_ver` field.  
`ep_rule_id` | `event.idm.read_only_udm.firewall.firewall_rule_id` | Directly mapped from the `ep_rule_id` field when `event_type` is `Firewall`.  
`event_type` | `event.idm.read_only_udm.metadata.product_event_type` | Directly mapped from the `event_type` CEF field.  
`failed_updates` | `event.idm.read_only_udm.additional.fields[<N>].key`: `failed_updates`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `failed_updates` | Directly mapped from the `failed_updates` field.  
`file_md5` | `event.idm.read_only_udm.source_file.hash_md5` | Directly mapped from the `file_md5` field when `event_type` is `TE Event`.  
`file_name` | `event.idm.read_only_udm.source_file.file_name` | Directly mapped from the `file_name` field when `event_type` is `TE Event`.  
`file_sha1` | `event.idm.read_only_udm.source_file.hash_sha1` | Directly mapped from the `file_sha1` field when `event_type` is `TE Event`.  
`file_sha256` | `event.idm.read_only_udm.source_file.hash_sha256` | Directly mapped from the `file_sha256` field when `event_type` is `TE Event`.  
`host_type` | `event.idm.read_only_udm.principal.asset.type` | Mapped from the `host_type` field. `Desktop` is converted to `WORKSTATION`, then the value is uppercased.  
`ifdir` | `event.idm.read_only_udm.network.direction` | Directly mapped from the `ifdir` field and uppercased when `event_type` is `Firewall`.  
`installed_products` | `event.idm.read_only_udm.principal.asset.software.name` | Directly mapped from the `installed_products` field.  
`is_scanned` | `sec_res.detection_fields[<N>].key`: `is_scanned`  
`sec_res.detection_fields[<N>].value`: Value of `is_scanned` | Directly mapped from the `is_scanned` field.  
`local_time` | `event.idm.read_only_udm.additional.fields[<N>].key`: `local_time`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `local_time` | Directly mapped from the `local_time` field.  
`log_type` | `event.idm.read_only_udm.metadata.log_type` | Directly mapped from the `log_type` field.  
`loguid` | `event.idm.read_only_udm.metadata.product_log_id` | Directly mapped from the `loguid` field.  
`machine_guid` | `event.idm.read_only_udm.principal.asset.product_object_id` | Directly mapped from the `machine_guid` field.  
`media_authorized` | `event.idm.read_only_udm.additional.fields[<N>].key`: `media_authorized`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `media_authorized` | Directly mapped from the `media_authorized` field.  
`media_class_id` | `event.idm.read_only_udm.additional.fields[<N>].key`: `media_class_id`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `media_class_id` | Directly mapped from the `media_class_id` field.  
`media_description` | `event.idm.read_only_udm.additional.fields[<N>].key`: `media_description`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `media_description` | Directly mapped from the `media_description` field.  
`media_encrypted` | `event.idm.read_only_udm.additional.fields[<N>].key`: `media_encrypted`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `media_encrypted` | Directly mapped from the `media_encrypted` field.  
`media_manufacturer` | `event.idm.read_only_udm.additional.fields[<N>].key`: `media_manufacturer`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `media_manufacturer` | Directly mapped from the `media_manufacturer` field.  
`media_type` | `event.idm.read_only_udm.additional.fields[<N>].key`: `media_type`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `media_type` | Directly mapped from the `media_type` field.  
`msg` | `event.idm.read_only_udm.metadata.description` | Directly mapped from the `msg` CEF field.  
`origin` | `event.idm.read_only_udm.about.ip` | Directly mapped from the `origin` CEF field.  
`os_name` | `event.idm.read_only_udm.additional.fields[<N>].key`: `os_name`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `os_name` | Directly mapped from the `os_name` field.  
`os_version` | `event.idm.read_only_udm.principal.asset.platform_software.platform_version` | Directly mapped from the `os_version` field.  
`policy_date` | `event.idm.read_only_udm.additional.fields[<N>].key`: `policy_date`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `policy_date` | Directly mapped from the `policy_date` field.  
`policy_guid` | `event.idm.read_only_udm.principal.resource.product_object_id` | Directly mapped from the `policy_guid` field.  
`policy_name` | `event.idm.read_only_udm.principal.resource.name` | Directly mapped from the `policy_name` field.  
`policy_number` | `event.idm.read_only_udm.principal.resource.product_object_id` | Directly mapped from the `policy_number` field.  
`policy_type` | `event.idm.read_only_udm.additional.fields[<N>].key`: `policy_type`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `policy_type` | Directly mapped from the `policy_type` field.  
`policy_version` | `event.idm.read_only_udm.additional.fields[<N>].key`: `policy_version`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `policy_version` | Directly mapped from the `policy_version` field.  
`product` | `event.idm.read_only_udm.metadata.product_name` | Directly mapped from the `product` CEF field.  
`proto` | `event.idm.read_only_udm.network.protocol` | Directly mapped from the `proto` field when `event_type` is `Firewall`.  
`reading_data_access` | `event.idm.read_only_udm.additional.fields[<N>].key`: `reading_data_access`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `reading_data_access` | Directly mapped from the `reading_data_access` field.  
`requestClientApplication` | `event.idm.read_only_udm.network.http.user_agent` | Directly mapped from the `requestClientApplication` field.  
`result` | `event.idm.read_only_udm.security_result.summary` | Directly mapped from the `result` field.  
`rt` | `event.idm.read_only_udm.metadata.event_timestamp.seconds` | Mapped from the `rt` field, divided by 1000, and the integer part is taken as seconds.  
`rule_name` | `event.idm.read_only_udm.firewall.firewall_rule` | Directly mapped from the `rule_name` field when `event_type` is `Firewall`.  
`s_port` | `event.idm.read_only_udm.network.client.port` | Directly mapped from the `s_port` field when `event_type` is `Firewall`.  
`sequencenum` | `event.idm.read_only_udm.additional.fields[<N>].key`: `sequencenum`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `sequencenum` | Directly mapped from the `sequencenum` field.  
`service` | `event.idm.read_only_udm.network.target.port` | Directly mapped from the `service` field when `event_type` is `Firewall`.  
`severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from the `severity` field and converted to UDM severity values (CRITICAL, HIGH, MEDIUM, LOW, INFO).  
`shost` | `event.idm.read_only_udm.principal.hostname` | Directly mapped from the `shost` CEF field.  
`sig_ver` | `event.idm.read_only_udm.additional.fields[<N>].key`: `sig_ver`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `sig_ver` | Directly mapped from the `sig_ver` field.  
`src` | `event.idm.read_only_udm.principal.ip` | Directly mapped from the `src` CEF field.  
`src_machine_name` | `event.idm.read_only_udm.principal.hostname` | Directly mapped from the `src_machine_name` field when `event_type` is empty.  
`subject` | `event.idm.read_only_udm.task.task_name` | Directly mapped from the `subject` field when `event_type` is empty.  
`suser` | `event.idm.read_only_udm.principal.user.user_display_name` | Directly mapped from the `suser` CEF field.  
`time` | `event.idm.read_only_udm.metadata.event_timestamp.seconds` | Directly mapped from the `time` field and converted to Unix epoch seconds.  
`user_name` | `event.idm.read_only_udm.principal.user.email_addresses` | Directly mapped from the `user_name` CEF field.  
`user_sid` | `event.idm.read_only_udm.principal.user.windows_sid` | Directly mapped from the `user_sid` field.  
`version` | `event.idm.read_only_udm.additional.fields[<N>].key`: `version`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `version` | Directly mapped from the `version` field.  
`writing_data_access` | `event.idm.read_only_udm.additional.fields[<N>].key`: `writing_data_access`  
`event.idm.read_only_udm.additional.fields[<N>].value.string_value`: Value of `writing_data_access` | Directly mapped from the `writing_data_access` field.  
_N/A_ | `event.idm.read_only_udm.metadata.event_type` | Set to `GENERIC_EVENT` if none of `principal.ip`, `principal.hostname`, or `principal.mac` are present in the raw log, otherwise set to `STATUS_UPDATE`.  
_N/A_ | `event.idm.read_only_udm.metadata.vendor_name` | Constant value: `Check Point`.  
_N/A_ | `event.idm.read_only_udm.metadata.log_type` | Constant value: `CHECKPOINT_EDR`.  
_N/A_ | `event.idm.read_only_udm.principal.asset.platform_software.platform` | Set to `WINDOWS` if `os_name` contains `WINDOWS` or `Windows`.  
_N/A_ | `event.idm.read_only_udm.network.http.user_agent` | Set to `Check Point Endpoint Security Client` if `requestClientApplication` is present.  
_N/A_ | `event.edr.data_source` | Constant value: `CHECKPOINT_SANDBLAST` when `message` doesn't contain `CEF`.  
`operation` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`administrator` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`client_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`objectname` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`objecttype` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`Name` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`guid1` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`guid2` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`guid3` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`guid4` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`exclusionName1` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`exclusionName4` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`action` | `event.idm.read_only_udm.security_result_action` | Mapped from changelog  
`session_uid` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`origin` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`Icon` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`flags` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`originsicname` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`advanced_changes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sendtotrackerasadvancedauditlog` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ExclusionName` | `event.idm.read_only_udm.principal.file.full_path` | Mapped from changelog  
`id` | `event.idm.read_only_udm.about.resource.product_object_id` | Mapped from changelog  
`program_file` | `event.idm.read_only_udm.about.file.full_path` | Mapped from changelog  
`exclusionName2` | `event.idm.read_only_udm.security_result.about.url` | Mapped from changelog  
`exclusionName3` | `event.idm.read_only_udm.security_result.about.file.full_path` | Mapped from changelog  
`auth` | `event.idm.read_only_udm.about.url` | Mapped from changelog  
`uid` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`src_machine_name` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`src_user_name` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`src` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`dst` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`process_exe_path` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`appi_name` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`matched_category` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`reason` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`protection_name` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`protection_type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`usercheck_incident_uid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tenant_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`exclusion_engine_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`exclusion_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`virtual_groups` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`client_name` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`client_ip` | `event.edr.network.target_ip` | Mapped from changelog  
`origin` | `event.edr.network.target_ip` | Mapped from changelog  
`subject` | `event.edr.task.task_name` | Mapped from changelog  
`host_name` | `event.edr.client.hostname` | Mapped from changelog  
`ifdir` | `event.edr.network.direction` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/checkpoint-edr-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
