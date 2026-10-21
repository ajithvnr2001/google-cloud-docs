---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-pix-firewall/
title: Collect Cisco PIX logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:57:05.134924+00:00
---

# Collect Cisco PIX logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-pix-firewall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco PIX logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco PIX logs to Google Security Operations using Bindplane. The parser extracts fields from the firewall syslog messages using regular expressions (grok patterns) and conditional logic. It then maps these extracted fields to the Unified Data Model (UDM), categorizing events as network connections, status updates, or generic events based on the presence of source and destination IP addresses.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows 2016 or later, or a Linux host with `systemd`
  * If running behind a proxy, ensure firewall [ports](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) are open
  * Privileged access to the **Cisco PIX Firewall** appliance



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
                 log_type: 'CISCO_PIX_FIREWALL'
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
                log_type: 'CISCO_PIX_FIREWALL'
                raw_log_field: body
                ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in **Linux** , run the following command:
        
        sudo systemctl restart bindplane-agent
        

  * To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
        
        net stop BindPlaneAgent && net start BindPlaneAgent
        




## Configure Syslog on Cisco PIX Firewall

  1. Sign in to your Cisco PIX appliance using SSH or a console connection.
  2. Enter the following for **privileged** mode:
         
         enable
         

  3. Enter the following command for configuration mode:
         
         conf t
         

  4. Enter the following commands to enable logging and timestamp:
         
         logging on
         logging timestamp
         

  5. Enter the following command to configure log level:
         
         logging trap information
         

  6. Enter the following command to configure syslog information:
         
         logging host <interface> <bindplane_IP_address>
         

     * Change `<interface>` to the interface that has access to your Bindplane agent.
     * Change `<bindplane_IP_address>` to your actual Bindplane agent IP address.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
datetime | metadata.event_timestamp.seconds | Convert the extracted timestamp to epoch seconds  
datetime | metadata.event_timestamp.nanos | Convert the extracted timestamp to epoch nanoseconds  
descrip | metadata.description | Directly mapped from the extracted `descrip` field  
observer_ip | observer.ip | Directly mapped from the extracted `observer_ip` field  
proto | network.ip_protocol | Directly mapped from the extracted `proto` field after converting to uppercase. Only mapped if the value is one of `UDP`, `TCP`, or `ICMP`.  
src_ip | principal.ip | Directly mapped from the extracted `src_ip` field  
src_port | principal.port | Directly mapped from the extracted `src_port` field after converting to integer  
facility | principal.resource.type | Directly mapped from the extracted `facility` field  
action | security_result.action_details | Directly mapped from the extracted `action` field  
severity_level | security_result.severity | Mapped based on the value of `severity_level`:   
\- 7, 6: INFORMATIONAL   
\- 5: LOW   
\- 4: MEDIUM   
\- 3: ERROR   
\- 2: HIGH   
\- Otherwise: CRITICAL  
dest_ip | target.ip | Directly mapped from the extracted `dest_ip` field  
dest_port | target.port | Directly mapped from the extracted `dest_port` field after converting to integer  
direction | network.direction | Mapped to `INBOUND` if the `direction` field is `inbound`  
| metadata.event_timestamp.seconds | Value taken from the top level 'create_time.seconds' field  
| metadata.event_timestamp.nanos | Value taken from the top level 'create_time.nanos' field  
| metadata.event_type | Determined based on the presence of src_ip and dest_ip:   
\- Both present: NETWORK_CONNECTION   
\- Only src_ip present: STATUS_UPDATE   
\- Otherwise: GENERIC_EVENT  
| metadata.product_event_type | Concatenation of `facility`, `-`, `severity_level`, `-`, and `mnemonic` fields.  
| metadata.product_name | Hardcoded value: `CISCO_FWSM`  
| metadata.vendor_name | Hardcoded value: `CISCO`  
| security_result.action | Mapped to `BLOCK` if the `action` field is one of `Deny`, `Teardown`, `denied`, or `Denied`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-pix-firewall-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
