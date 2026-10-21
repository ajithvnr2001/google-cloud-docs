---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/appian-cloud/
title: Collect Appian Cloud logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:07:09.405751+00:00
---

# Collect Appian Cloud logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/appian-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Appian Cloud logs

**Parser Version:** 4.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Appian Cloud logs to Google Security Operations using Bindplane agent.

Appian Cloud is a low-code automation platform that enables organizations to build enterprise applications and workflows. Log streaming provides audit and security event logs from your Appian Cloud environment over an IPsec VPN connection.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Professional or Signature license with Appian Cloud
  * Record of your Appian environment URL(s)
  * IPsec VPN between Appian Cloud and the environment where the Bindplane agent will be deployed



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

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
            tcplog:
                listen_address: "0.0.0.0:6514"
        
        exporters:
            chronicle/appian_cloud:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: APPIAN_CLOUD
                raw_log_field: body
        
        service:
            pipelines:
                logs/appian_to_chronicle:
                    receivers:
                        - tcplog
                    exporters:
                        - chronicle/appian_cloud
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `6514` is the recommended port for Appian Cloud log streaming
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list



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
             




## Enable log streaming for Appian Cloud

  1. Open a Support case with Appian, with the Subject **Enable Log Streaming** , and include the following details: 
     * Environment URL(s)
     * Desired network path, as an IPsec VPN
     * Bindplane agent IP address
     * Bindplane agent TCP port number (for example, **6514**)
  2. Appian Support schedules a maintenance window and deploys the configuration.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`available_heap_space_label` | `additional.fields` | Merged  
`cpu_core_count_label` | `additional.fields` | Merged  
`daemon_thread_count_label` | `additional.fields` | Merged  
`data_store_label` | `additional.fields` | Merged  
`devicetimestamp_label` | `additional.fields` | Merged  
`entity_label` | `additional.fields` | Merged  
`execute_time_label` | `additional.fields` | Merged  
`load_average_label` | `additional.fields` | Merged  
`operation_name_label` | `additional.fields` | Merged  
`operation_type_label` | `additional.fields` | Merged  
`permanent_generation_available_label` | `additional.fields` | Merged  
`permanent_generation_used_label` | `additional.fields` | Merged  
`prepare_time_label` | `additional.fields` | Merged  
`retcode_label` | `additional.fields` | Merged  
`session_count_label` | `additional.fields` | Merged  
`tenured_collection_count_label` | `additional.fields` | Merged  
`tenured_collection_time_label` | `additional.fields` | Merged  
`tenured_generation_available_label` | `additional.fields` | Merged  
`tenured_generation_usage_after_collection_label` | `additional.fields` | Merged  
`tenured_generation_used_label` | `additional.fields` | Merged  
`thread_label` | `additional.fields` | Merged  
`total_swap_space_label` | `additional.fields` | Merged  
`total_system_memory_label` | `additional.fields` | Merged  
`total_thread_count_label` | `additional.fields` | Merged  
`transform_time_label` | `additional.fields` | Merged  
`used_heap_space_label` | `additional.fields` | Merged  
`used_swap_space_label` | `additional.fields` | Merged  
`used_system_memory_label` | `additional.fields` | Merged  
`young_cllection_time_label` | `additional.fields` | Merged  
`young_collection_count_label` | `additional.fields` | Merged  
`has_principal_user` | `extensions.auth.type` | Mapped: `true` → `AUTHTYPE_UNSPECIFIED`  
`src_host` | `intermediary.hostname` | Directly mapped  
`src_ip` | `intermediary.ip` | Merged  
`time` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss`  
`event_type` | `metadata.event_type` | Directly mapped  
`device` | `metadata.product_event_type` | Directly mapped  
`product_type` | `metadata.product_event_type` | Directly mapped  
`http_method` | `network.http.method` | Directly mapped  
`useragent` | `network.http.parsed_user_agent` | Renamed/mapped  
`useragent` | `network.http.user_agent` | Directly mapped  
`connectionid` | `network.session_id` | Directly mapped  
`sessionID` | `network.session_id` | Directly mapped  
`session_id` | `network.session_id` | Directly mapped  
`domain` | `principal.administrative_domain` | Directly mapped  
`application` | `principal.application` | Directly mapped  
`host` | `principal.asset.hostname` | Directly mapped  
`hostname` | `principal.asset.hostname` | Directly mapped  
`IpAddress` | `principal.asset.ip` | Merged  
`host` | `principal.hostname` | Directly mapped  
`hostname` | `principal.hostname` | Directly mapped  
`IpAddress` | `principal.ip` | Merged  
`src_port` | `principal.port` | Directly mapped  
`process_id` | `principal.process.pid` | Directly mapped  
`url` | `principal.url` | Directly mapped  
`roles` | `principal.user.attribute.roles` | Merged  
`companyname` | `principal.user.company_name` | Directly mapped  
`email` | `principal.user.email_addresses` | Merged  
`user_id` | `principal.user.email_addresses` | Mapped: `N/A` → `user_id`  
`modified_by_uuid` | `principal.user.product_object_id` | Directly mapped  
`user` | `principal.user.product_object_id` | Directly mapped  
`modified_by_username` | `principal.user.userid` | Directly mapped  
`userId` | `principal.user.userid` | Directly mapped  
`user_id` | `principal.user.userid` | Directly mapped  
`username2` | `principal.user.userid` | Directly mapped  
`versionDetails` | `security_result.about.platform_version` | Directly mapped  
`outcome_result` | `security_result.action` | Merged  
`security_result_action` | `security_result.action` | Merged  
`act` | `security_result.action_details` | Directly mapped  
`status` | `security_result.action_details` | Directly mapped  
`sec_result_category` | `security_result.category` | Merged  
`category` | `security_result.category_details` | Merged  
`desc` | `security_result.description` | Directly mapped  
`details` | `security_result.description` | Directly mapped  
`details_label` | `security_result.detection_fields` | Merged  
`endpoint_label` | `security_result.detection_fields` | Merged  
`execution_count_label` | `security_result.detection_fields` | Merged  
`maximum_execution_time_label` | `security_result.detection_fields` | Merged  
`maximum_response_size_label` | `security_result.detection_fields` | Merged  
`maximum_response_time_label` | `security_result.detection_fields` | Merged  
`mean_execution_time_label` | `security_result.detection_fields` | Merged  
`mean_response_size_label` | `security_result.detection_fields` | Merged  
`minimum_execution_time_label` | `security_result.detection_fields` | Merged  
`minimum_response_size_label` | `security_result.detection_fields` | Merged  
`model_label` | `security_result.detection_fields` | Merged  
`rolesAllow_label` | `security_result.detection_fields` | Merged  
`sqlcmd_label` | `security_result.detection_fields` | Merged  
`status_code_1xx_count_label` | `security_result.detection_fields` | Merged  
`status_code_2xx_count_label` | `security_result.detection_fields` | Merged  
`status_code_3xx_count_label` | `security_result.detection_fields` | Merged  
`status_code_4xx_count_label` | `security_result.detection_fields` | Merged  
`status_code_5xx_count_label` | `security_result.detection_fields` | Merged  
`type_label` | `security_result.detection_fields` | Merged  
`uuid_label` | `security_result.detection_fields` | Merged  
`severity` | `security_result.severity` | Mapped: `"INFORMATIONAL","INFORMATION","INFO"` → `INFORMATIONAL`, `"WARNING", "MEDIUM"` → `M...  
`detail` | `security_result.severity_details` | Directly mapped  
`action1` | `security_result.summary` | Directly mapped  
`msg` | `security_result.summary` | Directly mapped  
`object` | `security_result.summary` | Directly mapped  
`operation_detail` | `security_result.summary` | Directly mapped  
`reason` | `security_result.summary` | Directly mapped  
`summary` | `security_result.summary` | Directly mapped  
`server_host` | `target.asset.hostname` | Directly mapped  
`tar_host` | `target.asset.hostname` | Directly mapped  
`src_ip1` | `target.asset.ip` | Merged  
`hash` | `target.file.md5` | Directly mapped  
`document_name` | `target.file.names` | Merged  
`server_host` | `target.hostname` | Directly mapped  
`tar_host` | `target.hostname` | Directly mapped  
`src_ip1` | `target.ip` | Merged  
`commandline` | `target.process.command_line` | Directly mapped  
`action_label` | `target.resource.attribute.labels` | Merged  
`environment_label` | `target.resource.attribute.labels` | Merged  
`filters_label` | `target.resource.attribute.labels` | Merged  
`new_value_label` | `target.resource.attribute.labels` | Merged  
`original_value_label` | `target.resource.attribute.labels` | Merged  
`page_group_invoved_label` | `target.resource.attribute.labels` | Merged  
`page_involved_label` | `target.resource.attribute.labels` | Merged  
`record_identifier_label` | `target.resource.attribute.labels` | Merged  
`record_type_name_label` | `target.resource.attribute.labels` | Merged  
`record_type_url_stub_label` | `target.resource.attribute.labels` | Merged  
`setting_new_value_label` | `target.resource.attribute.labels` | Merged  
`setting_old_value_label` | `target.resource.attribute.labels` | Merged  
`site_involved_label` | `target.resource.attribute.labels` | Merged  
`site_url_stub_label` | `target.resource.attribute.labels` | Merged  
`view_label` | `target.resource.attribute.labels` | Merged  
`database` | `target.resource.name` | Directly mapped  
`property` | `target.resource.name` | Directly mapped  
`record_type_name` | `target.resource.name` | Directly mapped  
`resourcename` | `target.resource.name` | Directly mapped  
`site_involved` | `target.resource.name` | Directly mapped  
`id` | `target.resource.product_object_id` | Directly mapped  
`oid` | `target.resource.product_object_id` | Directly mapped  
`queryid` | `target.resource.product_object_id` | Directly mapped  
`sessionID` | `target.resource.product_object_id` | Directly mapped  
`transactionId` | `target.resource.product_object_id` | Directly mapped  
`action` | `target.resource.resource_subtype` | Directly mapped  
`name` | `target.resource.resource_subtype` | Directly mapped  
`user_uuid` | `target.user.product_object_id` | Directly mapped  
`username1` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.log_type` | Constant: `APPIAN_CLOUD`  
N/A | `metadata.product_name` | Constant: `Cloud Platform`  
N/A | `metadata.vendor_name` | Constant: `Appian`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
`sessionID` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`transactionId` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`versionDetails` | `event.idm.read_only_udm.security_result.about.platform_version` | Mapped from changelog  
`application` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`IpAddress` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`IpAddress` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`userId` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`rolesAllow` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`userRole` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`status` | `event.idm.read_only_udm.section_result.action_details` | Mapped from changelog  
`resourcename` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`commandline` | `event.idm.read_only_udm.target.process.command_line` | Mapped from changelog  
`devicetimestamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`email` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`document_name` | `target.files.names` | Mapped from changelog  
`msg" and "reason` | `security_result.summary` | Mapped from changelog  
`original_value", "setting_new_value", "setting_old_value", and "new_value` | `target.resource.attribute.labels` | Mapped from changelog  
`page_involved", "site_involved", and "page_group_involved` | `target.resource.attribute.labels` | Mapped from changelog  
`total_thread_count", "daemon_thread_count", used_heap_space", "available_heap_space", "tenured_generation_usage_after_collection", "tenured_generation_used", "tenured_generation_available", "permanent_generation_used", and "permanent_generation_available` | `additional.fields` | Mapped from changelog  
`young_collection_count", "young_cllection_time", "tenured_collection_count", "tenured_collection_time", "cpu_core_count", "total_system_memory", "used_system_memory", "total_swap_space", "used_swap_space", "load_average", and "session_count` | `additional.fields` | Mapped from changelog  
`record_identifier", "record_type_url_stub", "view", "filters", "environment", and "site_url_stub` | `target.resource.attribute.labels` | Mapped from changelog  
`data_store", "entity", and "operation_type` | `additional.fields` | Mapped from changelog  
`operation_name", "prepare_time", "transform_time", and "execute_time` | `additional.fields` | Mapped from changelog  
`connectionid` | `network.session.id` | Mapped from changelog  
`minimum_execution_time", "execution_count", "status_code_1xx_count", "status_code_2xx_count", "status_code_3xx_count", "status_code_4xx_count", "status_code_5xx_count", "minimum_response_size", "maximum_response_time", "maximum_response_size", "mean_execution_time", and "maximum_response_size` | `security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/appian-cloud-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
