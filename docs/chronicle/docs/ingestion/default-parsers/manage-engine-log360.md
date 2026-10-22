---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/manage-engine-log360/
title: Collect ManageEngine Log360 logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:00.569433+00:00
---

# Collect ManageEngine Log360 logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/manage-engine-log360/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ManageEngine Log360 logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest ManageEngine Log360 logs to Google Security Operations using Bindplane.

ManageEngine Log360 is a unified SIEM and log management solution that collects, monitors, and analyzes logs from multiple sources across your environment. It generates aggregated security event and compliance audit logs. Log360 includes a built-in Syslog Forwarder feature in its EventLog Analyzer component that supports multiple output formats including RFC 5424, RFC 3164, JSON, and custom templates.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and ManageEngine Log360
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to ManageEngine Log360 with administrator permissions
  * ManageEngine Log360 installed and configured to collect logs from your environment



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
          tcplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/log360:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: MANAGE_ENGINE_LOG360
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/log360_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/log360
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `tcplog`: The receiver type based on protocol: 
      * `udplog` for UDP syslog
      * `tcplog` for TCP syslog
    * `0.0.0.0`: IP address to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Specific IP address to listen on one interface
    * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)
  * **Exporter configuration:**

    * `log360`: Descriptive name for the exporter
    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `MANAGE_ENGINE_LOG360`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `log360_to_chronicle`: Descriptive name for the pipeline



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/log360:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: MANAGE_ENGINE_LOG360
            raw_log_field: body
            ingestion_labels:
              env: production
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

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
         




## Configure ManageEngine Log360 syslog forwarding

  1. Sign in to the **ManageEngine Log360** console as an administrator.
  2. Navigate to **Settings > Admin Settings > Integrations > Log Forwarding**.
  3. Click **Add New Profile**.
  4. Configure the forwarding profile with the following settings:

Setting | Value  
---|---  
**Forwarder Name** | Enter a descriptive name (for example, `Chronicle-Bindplane`)  
**Destination Server** | Enter the IP address of the Bindplane agent host  
**Protocol** | Select **TCP** or **UDP** to match the Bindplane receiver type  
**Port** | Enter the port matching the Bindplane agent receiver configuration (for example, `514`)  
  5. Click **Customize** to select the log format. Available formats include:

     * **Rawlog** : Forwards the original log as received
     * **JSON** : Forwards logs in structured JSON format
     * **RFC 5424** : Standard syslog format with structured data support
     * **RFC 5424 With Structured Data** : Extended RFC 5424 format
     * **RFC 3164** : Legacy BSD syslog format
     * **Custom** : Define a custom syslog format template
  6. Under **Select Devices** , add the devices whose logs you want to forward.

  7. Select the forwarding criteria:

     * **All logs** : Forwards all incoming logs from the selected devices
     * **Exclude** : Filters out logs matching specified rules
     * **Forward Only** : Forwards only logs matching specified rules
  8. Click **Save**.

**Note:** EventLog Analyzer supports up to 5 forwarding profiles. Each profile can forward to a different destination server.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
authentication_package | additional.fields | Merged with label object created from authentication_package  
Logon_type | extensions.auth.mechanism | Set to "NETWORK" if Logon_type == '3'; "BATCH" if '4'; "SERVICE" if '5'; "NETWORK_CLEAR_TEXT" if '8'; "NEW_CREDENTIALS" if '9'; "REMOTE_INTERACTIVE" if '10'; "CACHED_INTERACTIVE" if '11'; "MECHANISM_OTHER" if not empty  
user | intermediary.hostname | Value copied directly  
msg | metadata.description | Value copied directly  
user_present, principal_present | metadata.event_type | Set to "USER_RESOURCE_ACCESS" if user_present == "true"; "STATUS_UPDATE" if principal_present == "true"; else "GENERIC_EVENT"  
eventid | metadata.product_event_type | Value copied directly  
principal_domain | principal.administrative_domain | Value copied directly  
source_ip | principal.asset.ip | Extracted using IP grok pattern, merged if valid  
source_ip | principal.ip | Extracted using IP grok pattern, merged if valid  
source_port | principal.port | Value copied directly, converted to integer  
creator_process_name | principal.process.file.full_path | Value copied directly  
process_id | principal.process.pid | Value copied directly if not in [""," -"]  
logon_guid | principal.resource.product_object_id | Value copied directly  
principal_account_name | principal.user.userid | Value copied directly  
principal_security_id | principal.user.windows_sid | Value copied directly if matches Windows SID regex  
channel, principal_logon_id, impersonation_level, restricted_admin_mode, virtual_account, elevated_token, event_in_sequence, logon_process, transited_services, key_length | security_result.detection_fields | Merged with label objects created from each field  
summary | security_result.description | Value copied directly  
event | src.asset.software.vendor_name | Value copied directly  
target_domain | target.administrative_domain | Value copied directly if not in [""," -"]  
target_account_name | target.user.userid | Value copied directly if not in [""," -"]  
target_security_id | target.user.windows_sid | Value copied directly if matches Windows SID regex  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/manage-engine-log360-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
