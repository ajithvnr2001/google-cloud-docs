---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akeyless-vault/
title: Collect Akeyless Vault logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:28:32.443208+00:00
---

# Collect Akeyless Vault logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akeyless-vault/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Akeyless Vault logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Akeyless Vault logs to Google Security Operations using Bindplane.

Akeyless Vault is a cloud-native secrets management platform that provides centralized access to credentials, certificates, and encryption keys. It uses a patented Distributed Fragments Cryptography (DFC) technology that ensures secrets are never stored in a single location, providing zero-knowledge security across hybrid and multi-cloud environments.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and Akeyless Gateway
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Akeyless Gateway web UI with administrator permissions



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.

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
        
        sudo nano /status observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/akeyless_vault:
                compression: gzip
                creds_file_path: '<PLACEHOLDER_CREDS_FILE_PATH>'
                customer_id: '<PLACEHOLDER_CUSTOMER_ID>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: AKEYLESS_VAULT
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/akeyless_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/akeyless_vault
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `udplog`: UDP syslog receiver for Akeyless Gateway log forwarding
    * `0.0.0.0:514`: IP address and port to listen on. Replace the port as required in your infrastructure
  * **Exporter configuration:**

    * `<PLACEHOLDER_CREDS_FILE_PATH>`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<PLACEHOLDER_CUSTOMER_ID>`: Google SecOps customer ID
    * `malachiteingestion-pa.googleapis.com`: Regional endpoint URL. Replace with the appropriate endpoint for your region: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list



### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

To restart the Bindplane agent in Linux: 

  1. Run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. Verify the service is running:
         
         sudo systemctl status observiq-otel-collector
         

  3. Check logs for errors:
         
         sudo journalctl -u observiq-otel-collector -f
         




To restart the Bindplane agent in Windows:

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
         




## Configure syslog forwarding in Akeyless Vault

  1. Sign in to your **Akeyless Gateway** web UI.
  2. Go to **Log Forwarding**.
  3. Select the **Enable** checkbox.
  4. Choose the log format - select **JSON**.
  5. In the **Audit Log Server** field, enter `https://audit.akeyless.io/`.
  6. From the **Log Service** dropdown list, select **Syslog**.
  7. Provide the following configuration details: 
     * **Syslog Network** : Select the network protocol used by the Bindplane agent (for example, **UDP**).
     * **Syslog Host** : Enter the hostname or IP address of the Bindplane agent host (for example, `192.168.1.100:514`).
     * **Syslog Tag** : (Optional) Enter the tag for audit logs. The default value is `audit-export`.
     * **Syslog Formatter** : Select **Text** or **CEF**.
     * **TLS** : (Optional) Select the **TLS** checkbox and upload the **TLS Certificate** of your log server if TLS encryption is required.
  8. Click **Save Changes**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`access_id` | `metadata.product_log_id` | Directly mapped from `access_id` field. If not present, extracted from the message field using regex.  
`account_id` | `target.user.userid` | Directly mapped from `account_id` field.  
`action` | `security_result.action_details` | Directly mapped from `action` field.  
`component` | `target.resource.name` | Directly mapped from `component` field.  
`duration` | `network.session_duration.seconds` | Directly mapped from `duration` field and converted to integer.  
`remote_addr` | `principal.ip` | Extracted from `remote_addr` field, split by comma and added to the `principal.ip` array.  
`request_parameters.access_type` | `target.resource.attribute.labels` (key: `access_type`) | Directly mapped from `request_parameters.access_type` field. If not present, extracted from the message field using regex.  
`request_parameters.comment` | `target.resource.attribute.labels` (key: `comment`) | Directly mapped from `request_parameters.comment` field.  
`request_parameters.operation` | `target.resource.attribute.labels` (key: `operation`) | Directly mapped from `request_parameters.operation` field.  
`request_parameters.product` | `target.resource.attribute.labels` (key: `product`) | Directly mapped from `request_parameters.product` field. If not present, extracted from the message field using regex.  
`request_parameters.token_id` | `target.resource.attribute.labels` (key: `token_id`) | Directly mapped from `request_parameters.token_id` field.  
`request_parameters.transaction_type` | `target.resource.attribute.labels` (key: `transaction_type`) | Directly mapped from `request_parameters.transaction_type` field and converted to string. If not present, extracted from the message field using regex.  
`request_parameters.unique_id` | `target.resource.attribute.labels` (key: `unique_id`) | Directly mapped from `request_parameters.unique_id` field. If not present, extracted from the message field using regex.  
`request_parameters.universal_identity_rotate_type` | `target.resource.attribute.labels` (key: `universal_identity_rotate_type`) | Directly mapped from `request_parameters.universal_identity_rotate_type` field.  
`request_parameters.user_agent` | `target.resource.attribute.labels` (key: `user_agent`) | Directly mapped from `request_parameters.user_agent` field.  
`severity` | `security_result.severity` | Mapped from `severity` field: `Info` to `INFORMATIONAL`, `Error` to `ERROR`, `Warning` to `MEDIUM`, otherwise `UNKNOWN_SEVERITY`.  
`status` | `network.http.response_code` | Directly mapped from `status` field and converted to integer.  
`timestamp` | `metadata.event_timestamp` | Directly mapped from the log entry timestamp field.  
N/A | `metadata.log_type` | Hardcoded to `AKEYLESS_VAULT`.  
N/A | `metadata.event_type` | Set to `STATUS_UPDATE` if IP is present, otherwise defaults to `GENERIC_EVENT`.  
N/A | `metadata.vendor_name` | Extracted from the message field using CEF regex pattern.  
N/A | `metadata.product_name` | Extracted from the message field using CEF regex pattern.  
N/A | `metadata.product_version` | Extracted from the message field using CEF regex pattern.  
N/A | `metadata.product_event_type` | Extracted from the message field using syslog header regex pattern.  
N/A | `target.namespace` | Extracted from the message field using regex.  
`action` | `network.http.method` | Mapped from `action` field: `get` to `GET`, `put` and `Authentication` to `PUT`, `post` to `POST`, `delete` to `DELETE`.  
`remote_addr` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`syslog_hostname` | `event.idm.read_only_udm.observer.hostname` | Mapped from changelog  
`process_name` | `event.idm.read_only_udm.observer.application` | Mapped from changelog  
`pid` | `event.idm.read_only_udm.observer.process.pid` | Mapped from changelog  
`severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`request_parameters.unique_id` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`item_type` | `event.idm.read_only_udm.target.resource.resource_subtype` | Mapped from changelog  
`request_parameters.session_id` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`duration_in_ms` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`request_parameters.source` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`request_parameters.item_accessibility` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`remote_addr array` | `principal.ip` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akeyless-vault-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
