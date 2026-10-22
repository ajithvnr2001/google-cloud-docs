---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ubiquiti-switch/
title: Collect Ubiquiti Unifi switch logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:55.129945+00:00
---

# Collect Ubiquiti Unifi switch logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ubiquiti-switch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Ubiquiti Unifi switch logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Ubiquiti Unifi switch logs to Google Security Operations using Bindplane. The parser extracts fields from the syslog messages using grok patterns, converting the raw log data into a structured format conforming to the Unified Data Model (UDM). It handles various log formats, extracts key information like timestamps, hostnames, descriptions, and network details, and enriches the data with additional context before merging it into the final UDM event.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the BindPlane agent requirements
  * Privileged access to the Ubiquiti Controller UI



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

  * For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file:

     1. Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     2. Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             # Replace the port and IP address as required
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: <CUSTOMER_ID>
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'UBIQUITI_SWITCH'
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
     * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
     * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
     * Replace `<CUSTOMER_ID>` with the actual customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the path where the service account key file (Option 1) was saved in the Get Google SecOps credentials for the Bindplane agent section.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: <CUSTOMER_ID>
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'UBIQUITI_SWITCH'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux, run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

  * To restart the Bindplane agent in Windows, you can either use the **Services** console or enter the following command:
        
        net stop observiq-otel-collector && net start observiq-otel-collector
        




## Configure Ubquiti switch to send Control Plane Syslog

  1. Sign in to the Unifi Controller UI.
  2. Open **Unifi Network**.
  3. Go to **Settings > Control Plane > Integrations tab**.
  4. Find the **Activity Logging** (Syslog) section.
  5. Enable the **SIEM Server** option.
  6. Provide the following configuration details: 
     * Click **Edit** categories and add the log categories required.
     * **Server Address** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number (**UDP** is required).
  7. Click **Apply Changes**.



## Configure Ubquiti switch to send CyberSecure Syslog

  1. Sign in to the Unifi Controller UI.
  2. Open **Unifi Network**.
  3. Go to **Settings > CyberSecure > Traffic Logging tab**.
  4. Find the **Activity Logging** (Syslog) section.
  5. Enable the **SIEM Server** option.
  6. Provide the following configuration details: 
     * Click **Edit** categories and add the log categories required.
     * **Server Address** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number (**UDP** is required).
     * Disable **Debug Logs**.
  7. Click **Apply Changes**.



## UDM Mapping Table

Log field | UDM mapping | Logic  
---|---|---  
`anomalies` | `security_result.detection_fields[].key`: "anomalies"  
`security_result.detection_fields[].value`: `anomalies` value from the log | Directly mapped from the `anomalies` field in the raw log.  
`application` | `observer.application` | Directly mapped from the `application` field in the raw log.  
`assoc_status` | `security_result.detection_fields[].key`: "assoc_status"  
`security_result.detection_fields[].value`: `assoc_status` value from the log | Directly mapped from the `assoc_status` field in the raw log.  
`asset_details` | `observer.asset.product_object_id`: Extracted using grok pattern `%{GREEDYDATA:asset_id},%{GREEDYDATA:asset_version}`  
`asset_software.version`: Extracted using grok pattern `%{GREEDYDATA:asset_id},%{GREEDYDATA:asset_version}` | The `asset_details` field is parsed using a grok pattern to extract the `asset_id` and `asset_version`.  
`asset_id` | `observer.asset.product_object_id` | Directly mapped from the extracted `asset_id` field from `asset_details`.  
`asset_version` | `observer.asset.software.version` | Directly mapped from the extracted `asset_version` field from `asset_details`.  
`bssid` | `principal.mac` | Directly mapped from the `bssid` field in the raw log.  
`description` | `metadata.description` | Directly mapped from the `description` field in the raw log.  
`device` | `metadata.product_name` | Directly mapped from the `device` field in the raw log. If `device` is not present, the value "UBIQUITI_SWITCH" is used.  
`dns_resp_seen` | `security_result.detection_fields[].key`: "dns_resp_seen"  
`security_result.detection_fields[].value`: `dns_resp_seen` value from the log | Directly mapped from the `dns_resp_seen` field in the raw log.  
`DST` | `target.ip` | Directly mapped from the `DST` field in the raw log.  
`DPT` | `principal.port` | Directly mapped from the `DPT` field in the raw log after converting it to an integer.  
`event_type` | `security_result.detection_fields[].key`: "event_type"  
`security_result.detection_fields[].value`: `event_type` value from the log | Directly mapped from the `event_type` field in the raw log.  
`host` | `principal.hostname` | Directly mapped from the `host` field in the raw log.  
`ID` | `additional.fields[].key`: "ID"  
`additional.fields[].value.string_value`: `ID` value from the log | Directly mapped from the `ID` field in the raw log.  
`IN` | `additional.fields[].key`: "IN"  
`additional.fields[].value.string_value`: `IN` value from the log | Directly mapped from the `IN` field in the raw log.  
`interface` | `additional.fields[].key`: "interface"  
`additional.fields[].value.string_value`: `interface` value from the log | Directly mapped from the `interface` field in the raw log.  
`LEN` | `additional.fields[].key`: "LEN"  
`additional.fields[].value.string_value`: `LEN` value from the log | Directly mapped from the `LEN` field in the raw log.  
`mac` | `principal.mac` | Directly mapped from the `mac` field in the raw log.  
`metadata.event_type` | `metadata.event_type` | Derived from parser logic. Set to "STATUS_SHUTDOWN" if `state` is "Down", "STATUS_STARTUP" if `state` is "Up", "STATUS_UPDATE" if `kv_msg` and `DST` are present or `principal_present` is true, and "GENERIC_EVENT" otherwise.  
`metadata.log_type` | `metadata.log_type`: "UBIQUITI_SWITCH" | Constant value set by the parser.  
`metadata.vendor_name` | `metadata.vendor_name`: "UBIQUITI" | Constant value set by the parser.  
`principal_ip` | `principal.ip` | Directly mapped from the `principal_ip` field in the raw log.  
`process_id` | `observer.process.pid` | Directly mapped from the `process_id` field in the raw log.  
`product_event_type` | `metadata.product_event_type` | Directly mapped from the `product_event_type` field in the raw log.  
`PROTO` | `network.ip_protocol` | Directly mapped from the `PROTO` field in the raw log. If `PROTO` is "ICMPv6", the value is changed to "ICMP".  
`query_1` | `target.administrative_domain` | Directly mapped from the `query_1` field in the raw log.  
`query_server_1` | `target.ip` | Directly mapped from the `query_server_1` field in the raw log.  
`radio` | `security_result.detection_fields[].key`: "radio"  
`security_result.detection_fields[].value`: `radio` value from the log | Directly mapped from the `radio` field in the raw log.  
`satisfaction_now` | `security_result.detection_fields[].key`: "satisfaction_now"  
`security_result.detection_fields[].value`: `satisfaction_now` value from the log | Directly mapped from the `satisfaction_now` field in the raw log.  
`source_port` | `principal.port` | Directly mapped from the `source_port` field in the raw log after converting it to an integer.  
`SPT` | `target.port` | Directly mapped from the `SPT` field in the raw log after converting it to an integer.  
`SRC` | `principal.ip`, `principal.hostname` | Directly mapped from the `SRC` field in the raw log.  
`sta` | `principal.mac` | Directly mapped from the `sta` field in the raw log.  
`state` | `additional.fields[].key`: "state"  
`additional.fields[].value.string_value`: `state` value from the log | Directly mapped from the `state` field in the raw log.  
`timestamp` | `metadata.event_timestamp` | Directly mapped from the `timestamp` field in the raw log after being parsed by the date filter.  
`TTL` | `additional.fields[].key`: "TTL"  
`additional.fields[].value.string_value`: `TTL` value from the log | Directly mapped from the `TTL` field in the raw log.  
`vap` | `metadata.ingestion_labels[].key`: "Vap"  
`metadata.ingestion_labels[].value`: `vap` value from the log | Directly mapped from the `vap` field in the raw log.  
`version` | `metadata.product_version` | Directly mapped from the `version` field in the raw log.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ubiquiti-switch-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
