---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-central/
title: Collect Aruba Central logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:00:57.123652+00:00
---

# Collect Aruba Central logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-central/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Aruba Central logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document shows how to ingest HPE Aruba Networking Central logs to Google SecOps using the Bindplane agent. The parser extracts fields from Aruba Central syslog formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It sets default metadata values for the event source and type.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the **Aruba Central Management** console



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where the Bindplane agent will be installed.



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the Configuration File:

     * Locate the `config.yaml` file. Typically, it's in the `/etc/bindplane-agent/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             # Replace the port and IP address as required
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: <customer_id>
             endpoint: malachiteingestion-pa.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'ARUBA_CENTRAL'
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/source0__chronicle_w_labels-0:
               receivers:
                 - udplog
               exporters:
                 - chronicle/chronicle_w_labels
         

     * Replace the port and IP address as required in your infrastructure.
     * Replace `<customer_id>` with the actual Customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the file path where the authentication file was saved in Step 1.



## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure Syslog on Aruba Central

  1. Sign in to **Aruba Central** web UI.
  2. From the dashboard, locate a **group** that contains the **devices** you want to configure, or set the filter to **All Devices** for global settings. 
  3. Click the device or group you want to configure. 
  4. Go to **Configuration > System > Logging**. 
  5. Locate the **Syslog Servers** section and click the **+** button. 
     * **Server Name** : Enter a unique and descriptive name. 
     * **Server IP** : Enter the Bindplane agent IP address.
     * **Server Port** : Enter the Bindplane agent port number. 
     * **Logging Format** : Select Syslog. 
     * **Category and Facility** : Select the categories and facilities for which you want to send logs. 
     * **Logging Level** : Select **Informational**.
  6. Click **Save Settings**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`additional_amm` | `additional.fields` | Merged  
`additional_nid` | `additional.fields` | Merged  
`additional_setting_id` | `additional.fields` | Merged  
`additional_webhook` | `additional.fields` | Merged  
`dev_type_label` | `additional.fields` | Merged  
`operation_label` | `additional.fields` | Merged  
`datetime` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`timestamp` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`event_type` | `metadata.event_type` | Directly mapped  
`alert_type` | `metadata.product_event_type` | Directly mapped  
`event_data` | `metadata.product_event_type` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`details.__base_url` | `metadata.url_back_to_product` | Directly mapped  
`network_ssid` | `network.session_id` | Directly mapped  
`app` | `principal.application` | Directly mapped  
`cluster_hostname` | `principal.asset.hostname` | Directly mapped  
`host` | `principal.asset.hostname` | Directly mapped  
`princ_mac` | `principal.asset.mac` | Merged  
`details.group_name` | `principal.group.group_display_name` | Directly mapped  
`details.group` | `principal.group.product_object_id` | Directly mapped  
`cluster_hostname` | `principal.hostname` | Directly mapped  
`host` | `principal.hostname` | Directly mapped  
`princ_mac` | `principal.mac` | Merged  
`pid` | `principal.process.pid` | Directly mapped  
`cid` | `principal.user.product_object_id` | Directly mapped  
`details.user` | `principal.user.userid` | Directly mapped  
`device_id` | `principal.user.userid` | Directly mapped  
`labels` | `security_result.about.labels` | Merged  
`description` | `security_result.description` | Directly mapped  
`state_label` | `security_result.detection_fields` | Merged  
`severity` | `security_result.severity` | Mapped values (5 total, e.g. `"LOG_INFO", "LOG_DEBUG"` → `LOW`, `LOG_WARN` → `MEDIUM`, `LOG_...  
`details.config_change` | `security_result.summary` | Directly mapped  
`target_mac` | `target.asset.mac` | Merged  
`target_mac` | `target.mac` | Merged  
`alert_type` | `target.resource.type` | Mapped: `DEVICE_CONFIG_CHANGE_DETECTED` → `DEVICE`  
`target_userid` | `target.user.userid` | Directly mapped  
`userid` | `target.user.userid` | Directly mapped  
N/A | `metadata.product_name` | Constant: `ARUBA_CENTRAL`  
N/A | `metadata.vendor_name` | Constant: `ARUBA CENTRAL`  
N/A | `security_result.severity` | Constant: `LOW`  
N/A | `target.resource.type` | Constant: `DEVICE`  
`nid" , "setting_id" , "details.dev_type" , "webhook" and "operation` | `additional.fields` | Mapped from changelog  
`details.labels` | `security_result.about.labels` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-central-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
