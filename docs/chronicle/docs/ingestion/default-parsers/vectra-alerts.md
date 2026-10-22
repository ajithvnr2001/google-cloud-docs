---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vectra-alerts/
title: Collect Vectra Alerts logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:21.131685+00:00
---

# Collect Vectra Alerts logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vectra-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Vectra Alerts logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Vectra Alerts logs to Google Security Operations using the [Vectra SIEM Connector](https://github.com/vectranetworks/siem-connector) and Bindplane.

**Note:** The Vectra SIEM Connector is designed for **RUX (Respond UX)** deployments using the cloud-based Vectra AI Platform. It pulls alert data from the Vectra REST API and forwards it as syslog to a local collector. For QUX (Quadrant UX) deployments using a brain appliance, detection alerts can be sent directly via syslog — see the [Collect Vectra Detect logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vectra-detect) guide.

Vectra AI is a network detection and response platform that generates security alerts for threat detections across cloud, data center, and IoT environments. The platform uses AI-driven behavioral analysis to identify hidden cyberattacks in real time.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Vectra AI platform
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Vectra AI platform with administrator permissions



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

  * Linux:
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * Windows:
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/vectra_alerts:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: VECTRA_ALERTS
            raw_log_field: body
        
        service:
          pipelines:
            logs/vectra_alerts_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/vectra_alerts
        




### Configuration parameters

  * Replace the following placeholders:

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
          chronicle/vectra_alerts:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: VECTRA_ALERTS
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux:

    1. Run the following command:
           
           sudo systemctl restart observiq-otel-collector
           

    2. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    3. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           

  * To restart the Bindplane agent in Windows:

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
           




## Configure Vectra Alerts syslog forwarding

Deploy the [Vectra SIEM Connector](https://github.com/vectranetworks/siem-connector) to forward alert data to the Bindplane agent.

  1. Deploy the Vectra SIEM Connector (available as a Docker container or standalone application).
  2. Configure the connector with your Vectra AI Platform URL (for example, `https://your-tenant.vectra.ai`) and API credentials.
  3. Set the output destination to syslog with the following parameters: 
     * **Syslog Server** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514` (or the port configured in the Bindplane agent).
     * **Protocol** : Select **UDP** (matching the Bindplane receiver configuration).
  4. Select the event categories to forward: 
     * Detections
     * Audits
     * Health events
  5. Start the connector and verify that alert logs are being forwarded by checking the Bindplane agent logs.

**Note:** The connector polls the Vectra API on schedule, transforms events to syslog-compliant format, and sends them to the Bindplane agent over the configured protocol.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
assigned_date | additional.fields.assigned_date_label | Set label with key "Assigned Date" and value from assigned_date  
assigned_to | additional.fields.assigned_to_label | Set label with key "Assigned To" and value from assigned_to  
c_score | additional.fields.c_score_label | Set label with key "c_score" and value from c_score  
category | security_result.category_details | Value copied directly  
certainty | additional.fields.certainty_label | Set label with key "Certainty" and value from certainty  
created_timestamp | metadata.event_timestamp | Converted using format yyyy-MM-ddTHH:mm:ssZ  
custom_detection | additional.fields.custom_detection_label | Set label with key "Custom Detection" and value from custom_detection  
data_source.connection_id | security_result.detection_fields.connection_id_label | Set label with key "Connection ID" and value from data_source.connection_id  
data_source.connection_name | security_result.detection_fields.connection_name_label | Set label with key "Connection Name" and value from data_source.connection_name  
data_source.type | security_result.detection_fields.data_source_type_label | Set label with key "Data Source Type" and value from data_source.type  
description | metadata.description | Value copied directly  
detection | additional.fields.detection_label | Set label with key "Detection" and value from detection  
detection_category | additional.fields.detection_category_label | Set label with key "Detection Category" and value from detection_category  
detection_type | additional.fields.detection_type_label | Set label with key "Detection Type" and value from detection_type  
detection_url | principal.url | Value copied directly  
filtered_by_ai | additional.fields.filtered_by_ai_label | Set label with key "Filtered By AI" and value from filtered_by_ai  
filtered_by_rule | additional.fields.filtered_by_rule_label | Set label with key "Filtered By Rule" and value from filtered_by_rule  
filtered_by_user | additional.fields.filtered_by_user_label | Set label with key "Filtered By User" and value from filtered_by_user  
first_timestamp | additional.fields.first_timestamp_label | Set label with key "First Timestamp" and value from first_timestamp  
gd_first_timestamp | security_result.detection_fields.gd_first_timestamp_label | Set label with key "first_timestamp" and value from gd_first_timestamp  
gd_grouping_field | security_result.detection_fields.gd_grouping_field_label | Set label with key "grouping_field" and value from gd_grouping_field  
gd_last_timestamp | security_result.detection_fields.gd_last_timestamp_label | Set label with key "group_details_last_timestamp" and value from gd_last_timestamp  
gd_uuid | security_result.detection_fields.gd_uuid_label | Set label with key "gd_uuid" and value from gd_uuid  
grp_description | security_result.detection_fields.grp_description_label | Set label with key "grp_description" and value from grp_description  
grp_id | security_result.detection_fields.grp_id_label | Set label with key "grp_id" and value from grp_id  
grp_last_modified | security_result.detection_fields.grp_last_modified_label | Set label with key "grp_last_modified" and value from grp_last_modified  
grp_last_modified_by | security_result.detection_fields.grp_last_modified_by_label | Set label with key "grp_last_modified_by" and value from grp_last_modified_by  
grp_name | security_result.detection_fields.grp_name_label | Set label with key "grp_name" and value from grp_name  
grp_type | security_result.detection_fields.grp_type_label | Set label with key "grp_type" and value from grp_type  
id | metadata.product_log_id | Value copied directly  
intermediary | intermediary | Value copied directly  
is_custom_model | additional.fields.is_custom_model_label | Set label with key "is_custom_model" and value from is_custom_model  
is_marked_custom | additional.fields.is_marked_custom_label | Set label with key "is_marked_custom" and value from is_marked_custom  
is_targeting_key_asset | additional.fields.is_targeting_key_asset_label | Set label with key "is_targeting_key_asset" and value from is_targeting_key_asset  
is_triaged | additional.fields.is_triaged_label | Set label with key "is_triaged" and value from is_triaged  
last_timestamp | additional.fields.last_timestamp_label | Set label with key "last_timestamp" and value from last_timestamp  
note | additional.fields.note_label | Set label with key "note" and value from note  
note_modified_by | additional.fields.note_modified_by_label | Set label with key "note_modified_by" and value from note_modified_by  
note_modified_timestamp | additional.fields.note_modified_timestamp_label | Set label with key "note_modified_timestamp" and value from note_modified_timestamp  
notes | additional.fields.notes_label | Set label with key "notes" and value from notes  
principal | principal | Value copied directly  
security_result | security_result | Value copied directly  
sensor | additional.fields.sensor_label | Set label with key "sensor" and value from sensor  
sensor_name | additional.fields.sensor_name_label | Set label with key "sensor_name" and value from sensor_name  
src | src | Value copied directly  
src_account | additional.fields.src_account_label | Set label with key "src_account" and value from src_account  
src_host.certainty | additional.fields.src_certainty_label | Set label with key "src_host_certainty" and value from src_host.certainty  
src_host.id | principal.user.userid | Value copied directly  
gd_src_host_ip, src_ip, src_host.ip | principal.ip | Merged from gd_src_host_ip, src_ip, src_host.ip; last merge wins  
src_ip, src_host.ip | principal.asset.ip | Merged from src_ip, src_host.ip; last merge wins  
src_host.is_key_asset | additional.fields.src_host_is_key_asset_label | Set label with key "src_host_is_key_asset" and value from src_host.is_key_asset  
src_host.name | principal.hostname | Value copied directly  
src_host.threat | additional.fields.src_host_threat_label | Set label with key "src_host_threat" and value from src_host.threat  
src_host.url | src.url | Value copied directly  
src_host_group_description | security_result.detection_fields.src_host_group_description_label | Set label with key "src_host_group_description" and value from src_host_group_description  
src_host_group_id | security_result.detection_fields.src_host_group_id_label | Set label with key "src_host_group_id" and value from src_host_group_id  
src_host_group_last_modified | security_result.detection_fields.src_host_group_last_modified_label | Set label with key "src_host_group_last_modified" and value from src_host_group_last_modified  
src_host_group_last_modified_by | security_result.detection_fields.src_host_group_last_modified_by_label | Set label with key "src_host_group_last_modified_by" and value from src_host_group_last_modified_by  
src_host_group_name | security_result.detection_fields.src_host_group_name_label | Set label with key "src_host_group_name" and value from src_host_group_name  
src_host_group_type | security_result.detection_fields.src_host_group_type_label | Set label with key "src_host_group_type" and value from src_host_group_type  
state | security_result.detection_fields.state_label | Set label with key "state" and value from state  
summary.num_attempts | additional.fields.num_attempts_label | Set label with key "num_attempts" and value from summary.num_attempts  
target | target | Value copied directly  
dst_host_ip, dst_ip1 | target.ip | Merged from dst_host_ip, dst_ip1; last merge wins  
tags | additional.fields.tags_label | Set label with key "tags" and value from tags  
t_score | additional.fields.t_score_label | Set label with key "t_score" and value from t_score  
targets_key_asset | additional.fields.targets_key_asset_label | Set label with key "targets_key_asset" and value from targets_key_asset  
threat | security_result.detection_fields.threat_label | Set label with key "threat" and value from threat  
triage_rule_id | security_result.rule_id | Value copied directly  
type | additional.fields.type_label | Set label with key "type" and value from type  
url | metadata.url_back_to_product | Value copied directly  
uuid1 | security_result.detection_fields.uuid_label | Set label with key "uuid" and value from uuid1  
dst_host_id | security_result.detection_fields.dst_host_id_label | Set label with key "dst_host_id" and value from dst_host_id  
dst_host_name | security_result.detection_fields.dst_host_name_label | Set label with key "dst_host_name" and value from dst_host_name  
dst_port1 | security_result.detection_fields.dst_port_label | Set label with key "dst_port" and value from dst_port1  
dst_last_timestamp | security_result.detection_fields.dst_last_timestamp_label | Set label with key "dst_last_timestamp" and value from dst_last_timestamp  
| metadata.event_type | Set to "NETWORK_CONNECTION" if has_principal == "true" and has_target == "true", else "USER_UNCATEGORIZED" if has_user == "true", else "STATUS_UPDATE" if has_principal == "true", else "GENERIC_EVENT"  
| metadata.product_name | Set to "Vectra Alerts"  
| metadata.vendor_name | Set to "Vectra Alerts"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vectra-alerts-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
