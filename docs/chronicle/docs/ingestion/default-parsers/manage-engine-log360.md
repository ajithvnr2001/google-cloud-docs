---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/manage-engine-log360/
title: Collect ManageEngine Log360 logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:10:47.554343+00:00
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
        
        sudo systemctl status observiq-otel-collector
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            tcplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/log360:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
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
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `MANAGE_ENGINE_LOG360`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `log360_to_chronicle`: Descriptive name for the pipeline



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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
