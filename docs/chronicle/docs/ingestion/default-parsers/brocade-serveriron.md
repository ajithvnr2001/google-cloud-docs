---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/brocade-serveriron/
title: Collect Brocade ServerIron ADX logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:28.629662+00:00
---

# Collect Brocade ServerIron ADX logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/brocade-serveriron/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Brocade ServerIron ADX logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Brocade ServerIron ADX logs to Google Security Operations using the Bindplane agent.

Brocade ServerIron ADX is an application delivery controller that generates syslog messages for authentication, load balancing, network events, and system activity. The parser extracts fields using grok patterns and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Brocade ServerIron ADX device
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Brocade ServerIron ADX CLI



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
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/brocade_serveriron:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: BROCADE_SERVERIRON
            raw_log_field: body
        
        service:
          pipelines:
            logs/brocade_serveriron_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/brocade_serveriron
        




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
          chronicle/brocade_serveriron:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: BROCADE_SERVERIRON
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
           
           ```bash
           sudo systemctl status observiq-otel-collector
           ```
           

    2. Check logs for errors:
           
           ```bash
           sudo journalctl -u observiq-otel-collector -f
           ```
           

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
             




## Configure syslog export from Brocade ServerIron ADX

  1. Sign in to the ADX device and enter global configuration mode:
         
         enable
         configure terminal
         

  2. Enable syslog logging:
         
         logging on
         

  3. Specify the IP address and port of the syslog server (Bindplane):
         
         logging host <syslog-server-ip> udp port 514
         

  4. Optional: Set the syslog facility (`local0` to `local7`):
         
         logging facility local0
         

  5. Define the minimum severity level of logs to send to the syslog server:
         
         logging trap <severity-level>
         

  6. Save the configuration:
         
         write memory
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`%{GREEDYDATA}` | `metadata.description` | The %{GREEDYDATA} field is mapped to metadata.description when it matches the "-- %{GREEDYDATA} --" pattern.  
`%{GREEDYDATA:auth_result}` | `security_result.description` | The %{GREEDYDATA:auth_result} field is concatenated with the %{GREEDYDATA:desc} field to form the security_result.description when %{GREEDYDATA:desc} is present.  
`%{GREEDYDATA:desc}` | `security_result.description` | The %{GREEDYDATA:desc} field is used to populate the security_result.description field. It can be concatenated with other fields depending on the raw log format.  
`%{GREEDYDATA:login_to}` | `security_result.description` | The %{GREEDYDATA:login_to} field is concatenated with the %{GREEDYDATA:desc} field to form the security_result.description when %{GREEDYDATA:desc} is present.  
`%{GREEDYDATA:user}` | `target.user.userid` | The %{GREEDYDATA:user} field is mapped to target.user.userid.  
`%{HOST:principal_host}` | `principal.hostname` | The %{HOST:principal_host} field is mapped to principal.hostname.  
`%{HOST:target_host}` | `target.hostname` | The %{HOST:target_host} field is mapped to target.hostname.  
`%{INT:http_port}` | `additional.fields.value.string_value` | The %{INT:http_port} field is mapped to additional.fields.value.string_value with key "HTTP Port".  
`%{INT:target_port}` | `target.port` | The %{INT:target_port} field is mapped to target.port and converted to an integer.  
`%{INT:telnet_port}` | `additional.fields.value.string_value` | The %{INT:telnet_port} field is mapped to additional.fields.value.string_value with key "Telnet Port".  
`%{INT:tftp_port}` | `additional.fields.value.string_value` | The %{INT:tftp_port} field is mapped to additional.fields.value.string_value with key "TFTP Port".  
`%{IP:principal_ip}` | `principal.ip` | The %{IP:principal_ip} field is mapped to principal.ip.  
`%{IP:target_ip}` | `target.ip` | The %{IP:target_ip} field is mapped to target.ip.  
`%{IPV4:principal_ip}` | `principal.ip` | The %{IPV4:principal_ip} field is mapped to principal.ip.  
`%{IPV4:target_ip}` | `target.ip` | The %{IPV4:target_ip} field is mapped to target.ip.  
`%{MAC:principal_mac}` | `principal.mac` | The %{MAC:principal_mac} field is mapped to principal.mac after converting it to the format [0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}.  
`%{USERNAME:target_host}` | `target.hostname` | The %{USERNAME:target_host} field is mapped to target.hostname.  
`%{USERNAME:user}` | `target.user.userid` | The %{USERNAME:user} field is mapped to target.user.userid.  
`%{WORD:auth_result}` | `security_result.description` | The %{WORD:auth_result} field is concatenated with the %{GREEDYDATA:desc} field to form the security_result.description when %{GREEDYDATA:desc} is present.  
`%{WORD:proto}` | `network.application_protocol` | The %{WORD:proto} field is mapped to network.application_protocol when its value is 'SSH'.  
`timestamp` | `metadata.event_timestamp` | The timestamp field is parsed from the raw log data using a grok pattern and converted to a timestamp object.  
| `extensions.auth.type` | The value is set to "MACHINE" if the proto field is not empty and the auth_action field is either "logout" or "login".  
| `metadata.description` | The field is populated with the value of the "metadata_description" field if it's not empty.  
| `metadata.event_type` | The field is populated based on the values of other fields using conditional logic:- STATUS_STARTUP: if target_port_status is "up".- STATUS_SHUTDOWN: if target_port_status is "down".- USER_LOGOUT: if proto is not empty and auth_action is "logout".- USER_LOGIN: if proto is not empty and auth_action is "login".- STATUS_UPDATE: if metadata_description matches "state changed".- GENERIC_EVENT: if none of the preceding conditions are met.  
| `metadata.log_type` | The value is hardcoded to "BROCADE_SERVERIRON".  
| `metadata.product_name` | The value is hardcoded to "ServerIron".  
| `metadata.vendor_name` | The value is hardcoded to "Brocade".  
| `security_result.action` | The value is set to "BLOCK" if the desc field contains "fail", or the auth_result field contains "fail" or "rejected".  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
