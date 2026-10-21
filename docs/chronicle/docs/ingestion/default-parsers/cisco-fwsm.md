---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-fwsm/
title: Collect Cisco Firewall Service Module (FWSM) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:28.991530+00:00
---

# Collect Cisco Firewall Service Module (FWSM) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-fwsm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Firewall Service Module (FWSM) logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Firewall Service Module (FWSM) logs to Google Security Operations using Bindplane. The parser first extracts common fields like timestamps, IP addresses, and event descriptions from the appliance syslog messages using Grok patterns. Then, it maps the extracted information to the standardized Unified Data Model (UDM) schema, converting data types, renaming fields, and enriching the output with security-related classifications based on specific values and keywords.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance
  * Windows 2016 or later, or a Linux host with `systemd`
  * If running behind a proxy, ensure firewall [ports](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) are open
  * Privileged access to the **Cisco FWSM** appliance



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

## Configure the Bindpolane agent to ingest Syslog and send to Google SecOps

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
                 log_type: 'CISCO_FWSM'
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
                log_type: 'CISCO_FWSM'
                raw_log_field: body
                ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in **Linux** , run the following command:
        
        sudo systemctl restart bindplane-agent
        

  * To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
        
        net stop BindPlaneAgent && net start BindPlaneAgent
        




## Configure Syslog on Cisco FWSM

  1. Sign in to Cisco FWSM using SSH or a console connection.
  2. Configure logging:
         
         logging on
         

  3. Configure the logging level:
         
         logging trap <level>
         

     * Change the logging trap level to **6** (informational).
  4. Configure the syslog settings:
         
         logging host [interface] bindplane_ip_address udp[/bindplane_port]
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
1.1.1.1 | observer.ip | Extracted from the log message using grok pattern.  
2.2.2.2 | principal.ip  
target.ip | Extracted from the log message using grok pattern. The destination IP is mapped to either principal.ip or target.ip based on the direction of the connection. When `dst outside` it will be mapped to principal.ip, otherwise to target.ip.  
3.3.3.3 | principal.ip  
target.ip | Extracted from the log message using grok pattern. The source IP is mapped to either principal.ip or target.ip based on the direction of the connection. When `dst outside` it will be mapped to principal.ip, otherwise to target.ip.  
Apr 3 10:35:40 |  | This timestamp is not captured in the UDM.  
Apr 3 10:44:38 |  | This timestamp is not captured in the UDM.  
Apr 3 11:20:34 |  | This timestamp is not captured in the UDM.  
Apr 3 11:20:38 |  | This timestamp is not captured in the UDM.  
Apr 29 16:09:44 |  | This timestamp is not captured in the UDM.  
Deny | security_result.action_details | Extracted from the log message using grok pattern.  
Denied | security_result.action_details | Extracted from the log message using grok pattern.  
FWSM-3-106011 | metadata.product_event_type | Extracted from the log message using grok pattern.  
FWSM-3-313001 | metadata.product_event_type | Extracted from the log message using grok pattern.  
FWSM-4-106023 | metadata.product_event_type | Extracted from the log message using grok pattern.  
FWSM-4-302010 | metadata.product_event_type | Extracted from the log message using grok pattern.  
FWSM-4-302016 | metadata.product_event_type | Extracted from the log message using grok pattern.  
ICMP | network.ip_protocol | Extracted from the log message using grok pattern and converted to uppercase.  
TCP | network.ip_protocol | Extracted from the log message using grok pattern and converted to uppercase.  
Teardown | security_result.action_details | Extracted from the log message using grok pattern.  
UDP | network.ip_protocol | Extracted from the log message using grok pattern and converted to uppercase.  
111 | target.port | Extracted from the log message using grok pattern and converted to integer. When `dst outside` it will be mapped to principal.port, otherwise to target.port.  
17608 | principal.port | Extracted from the log message using grok pattern and converted to integer. When `dst outside` it will be mapped to principal.port, otherwise to target.port.  
3000 | principal.port | Extracted from the log message using grok pattern and converted to integer. When `dst outside` it will be mapped to principal.port, otherwise to target.port.  
33103 | target.port | Extracted from the log message using grok pattern and converted to integer. When `dst outside` it will be mapped to principal.port, otherwise to target.port.  
514 | principal.port  
target.port | Extracted from the log message using grok pattern and converted to integer. When `dst outside` it will be mapped to principal.port, otherwise to target.port.  
| metadata.description | The entire `descrip` field from the raw log is mapped to this field.  
| metadata.event_timestamp | The timestamp from the batch object is used as the event timestamp.  
| metadata.event_type | Determined based on the presence of source and destination IPs:   
\- NETWORK_CONNECTION: both source and destination IPs are present.   
\- STATUS_UPDATE: only source IP is present.   
\- GENERIC_EVENT: neither source nor destination IP is present.  
| metadata.product_name | Hardcoded to `CISCO_FWSM`.  
| metadata.vendor_name | Hardcoded to `CISCO`.  
| principal.resource.type | Mapped from the `facility` field extracted from the log message.  
| security_result.action | Set to `BLOCK` if the `action` field is one of `Deny`, `Teardown`, `denied`, or `Denied`.  
| security_result.severity | Determined based on the `severity_level` field:   
\- 7, 6: INFORMATIONAL   
\- 5: LOW   
\- 4: MEDIUM   
\- 3: ERROR   
\- 2: HIGH   
\- other: CRITICAL  
| network.direction | Mapped from the `direction` field extracted from the log message. If `direction` field is `inbound`, this field will be set to `INBOUND`.  
`tls_version` | `event.idm.read_only_udm.network.tls.version` | Mapped from changelog  
`packet_size` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`threshold` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-fwsm-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
