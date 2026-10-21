---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/broadcom-ssl-va/
title: Collect Broadcom SSL Visibility Appliance logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:06:50.377936+00:00
---

# Collect Broadcom SSL Visibility Appliance logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/broadcom-ssl-va/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Broadcom SSL Visibility Appliance logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Broadcom SSL Visibility Appliance logs to Google Security Operations using the Bindplane agent.

Broadcom SSL Visibility Appliance provides SSL/TLS traffic inspection and generates syslog messages for session events, policy actions, and TLS connection details. The parser extracts fields using grok patterns and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Broadcom SSL Visibility Appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Broadcom SSL Visibility Appliance



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**
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

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/broadcom_ssl_va:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: BROADCOM_SSL_VA
                raw_log_field: body
        
        service:
            pipelines:
                logs/broadcom_ssl_va_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/broadcom_ssl_va
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
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
             




## Configure syslog for Broadcom SSL Visibility Appliance

  1. Sign in to the **SSL Visibility Appliance** Web UI.
  2. Go to **Platform Management > Remote Logging**.
  3. Click **Add**.
  4. Provide the following configuration details: 
     * **Host** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number (default **514**).
     * **Protocol** : Select **UDP**.
     * **Facility** : Select a syslog facility (for example, `local0`).
     * **Log Set** : Select **Session and Appliance Logs**.
  5. Click **Save** (the server entry will show **Connected** after the first heartbeat).



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
action | security_result.action_details | The value of this field is assigned to `security_result.action_details`.  
ciphersuite | network.tls.cipher | The value of this field is assigned to `network.tls.cipher`.  
data |  | This field is used for extracting other fields but not directly mapped to the UDM.  
destip | target.ip | The value of this field is assigned to `target.ip`.  
destport | target.port | The value of this field is converted to integer and assigned to `target.port`.  
hostname | principal.hostname | The value of this field is assigned to `principal.hostname`.  
pid | principal.process.pid | The value of this field is assigned to `principal.process.pid`.  
prodlogid | metadata.product_log_id | The value of this field is assigned to `metadata.product_log_id`.  
rule | security_result.rule_id | The value of this field is assigned to `security_result.rule_id`.  
segment_id | about.labels.value | The value of this field is assigned to `about.labels.value` where `about.labels.key` is `segment_id`.  
srcip | principal.ip | The value of this field is assigned to `principal.ip`.  
srcPort | principal.port | The value of this field is converted to integer and assigned to `principal.port`.  
status | security_result.action | The value of this field determines the value of `security_result.action`. If it contains `Success`, the value is set to `ALLOW`, otherwise `BLOCK`.  
timestamp | metadata.event_timestamp.seconds | The value of this field is parsed to a timestamp and the seconds part is assigned to `metadata.event_timestamp.seconds`.  
tlsversion | network.tls.version | The value of this field is assigned to `network.tls.version`.  
| about.resource.attribute.labels.key | The value of this field is set to `Flag list`.  
| about.resource.attribute.labels.value | The value of this field is taken from the `flag_list` field after undergoing some transformations.  
| metadata.event_type | The value of this field is set to `NETWORK_CONNECTION` if both `srcip` and `destip` fields are not empty.  
| metadata.log_type | The value of this field is set to `BROADCOM_SSL_VA`.  
| metadata.product_name | The value of this field is set to `SSL Visibility`.  
| metadata.vendor_name | The value of this field is set to `Broadcom`.  
| security_result.category | The value of this field is set to `SOFTWARE_MALICIOUS`.  
| target.application | The value of this field is set to `ssldata`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/broadcom-ssl-va-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
