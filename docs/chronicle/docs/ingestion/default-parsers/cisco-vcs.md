---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-vcs/
title: Collect Cisco VCS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:59.950360+00:00
---

# Collect Cisco VCS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-vcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco VCS logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco VCS (Video Communication Service), (controlled through ExpressWay) logs to Google Security Operations using Bindplane. The parser extracts fields from the syslog messages, normalizes them into a Unified Data Model (UDM), and categorizes the event type based on extracted details like IP addresses, ports, and actions. It handles various log formats, extracts key-value pairs, and maps severity levels to standardized values for security analysis. 

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance
  * A Windows 2016 or later, or a Linux host with `systemd`
  * If running behind a proxy, firewall [ports](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) are open
  * Privileged access to the **Cisco ExpressWay**



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

For additional installation options, consult the [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file: 
     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
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
                 customer_id: <customer_id>
                 endpoint: chronicle.googleapis.com
                 # Add optional ingestion labels for better organization
                 log_type: 'CISCO_VCS'
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
     * Replace `<customer_id>` with the actual customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the path where the service account key file (Option 1) was saved in the Get Google SecOps credentials for the Bindplane agent section.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
            chronicle/chronicle_w_labels:
                compression: gzip
                # Adjust the path to the credentials file you downloaded in Step 1
                creds_file_path: '/path/to/ingestion-authentication-file.json'
                # Replace with your actual customer ID from Step 2
                customer_id: <customer_id>
                endpoint: malachiteingestion-pa.googleapis.com
                # Add optional ingestion labels for better organization
                log_type: 'CISCO_VCS'
                raw_log_field: body
                ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in **Linux** , run the following command:
        
        sudo systemctl restart bindplane-agent
        

  * To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
        
        net stop BindPlaneAgent && net start BindPlaneAgent
        




## Configure Syslog for Cisco ExpressWay

  1. Sign in to the **Cisco ExpressWay** web UI.
  2. Go to **Maintenance > Logging**.
  3. Enter the Bindplane agent IP addresses as the **Remote syslog server**.
  4. Click **Options**.
  5. Provide the following configuration details: 
     * **Transport** : Select **UDP**.
     * **Port** : Enter the Bindplane agent port number.
     * **Message Format** : Select **BSD** , the other possible option is **IETF**.
     * **Filter by Severity** : Select **Informational**.
  6. Click **Save**.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
Action | read_only_udm.security_result.action_details | The value of `Action` field from the raw log.  
Code | read_only_udm.network.http.response_code | The value of `Code` field from the raw log, converted to integer. Used when `Response-code` is not present.  
Detail | read_only_udm.security_result.description | The value of `Detail` field from the raw log.  
Dst-ip | read_only_udm.target.ip | The value of `Dst-ip` field from the raw log. Used when `Action` is not `Received`.  
Dst-port | read_only_udm.target.port | The value of `Dst-port` field from the raw log, converted to integer. Used when `Action` is not `Received`.  
Event | read_only_udm.metadata.product_event_type | The value of `Event` field from the raw log.  
Level | read_only_udm.security_result.severity_details | The value of `Level` field from the raw log.  
Level | read_only_udm.security_result.severity | Mapped based on the value of `Level` field from the raw log:   
\- `9`, `10`, `VERY-HIGH`: CRITICAL   
\- `error`, `warning`, `7`, `8`, `HIGH`: HIGH   
\- `notice`, `4`, `5`, `6`, `MEDIUM`: MEDIUM   
\- `information`, `info`, `0`, `1`, `2`, `3`, `LOW`: LOW  
Local-ip | read_only_udm.principal.ip | The value of `Local-ip` field from the raw log. Used when `Action` is not `Received`.  
Local-ip | read_only_udm.target.ip | The value of `Local-ip` field from the raw log. Used when `Action` is `Received`.  
Local-port | read_only_udm.principal.port | The value of `Local-port` field from the raw log, converted to integer. Used when `Action` is not `Received`.  
Local-port | read_only_udm.target.port | The value of `Local-port` field from the raw log, converted to integer. Used when `Action` is `Received`.  
Method | read_only_udm.network.http.method | The value of `Method` field from the raw log.  
Module | read_only_udm.additional.fields.value.string_value | The value of `Module` field from the raw log.  
Node | read_only_udm.additional.fields.value.string_value | The value of `Node` field from the raw log.  
Protocol | read_only_udm.network.ip_protocol | The value of `Protocol` field from the raw log, parsed and mapped to the corresponding IP protocol name using the `parse_ip_protocol.include` logic.  
Response-code | read_only_udm.network.http.response_code | The value of `Response-code` field from the raw log, converted to integer.  
Src-ip | read_only_udm.principal.ip | The value of `Src-ip` field from the raw log. Used when `Action` is `Received`.  
Src-ip | read_only_udm.principal.ip | The value of `Src-ip` field from the raw log. Used when `Action` is not `Received` and `Local-ip` is not present.  
Src-port | read_only_udm.principal.port | The value of `Src-port` field from the raw log, converted to integer. Used when `Action` is `Received`.  
Src-port | read_only_udm.principal.port | The value of `Src-port` field from the raw log, converted to integer. Used when `Action` is not `Received` and `Local-port` is not present.  
application | read_only_udm.target.application | The value of `application` field from the raw log.  
description | read_only_udm.security_result.description | The value of `description` field from the raw log.  
inner_msg | read_only_udm.security_result.description | The value of `inner_msg` field from the raw log. Used when `inner_msg_grok_failure` occurs.  
principal_hostname | read_only_udm.principal.hostname | The value of `principal_hostname` field from the raw log.  
timestamp | read_only_udm.metadata.event_timestamp.seconds | The epoch timestamp extracted from the `timestamp` field in the raw log.  
timestamp | read_only_udm.events.timestamp.seconds | The epoch timestamp extracted from the `timestamp` field in the raw log.  
| read_only_udm.additional.fields.key | Hardcoded value: `Module`, `Node`  
| read_only_udm.metadata.log_type | Hardcoded value: `CISCO_VCS`  
| read_only_udm.metadata.product_name | Hardcoded value: `CISCO VCS`  
| read_only_udm.metadata.vendor_name | Hardcoded value: `CISCO VCS`  
| read_only_udm.metadata.event_type | Determined based on the values of `Action`, `Src-ip`, `principal_hostname`, `Local-ip`, and `Dst-ip` fields:   
\- `NETWORK_CONNECTION`: if either (`Action` is `Received` and `Local-ip` is present) or (`Action` is not `Received` and `Dst-ip` is present)   
\- `STATUS_UPDATE`: otherwise  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-vcs-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
