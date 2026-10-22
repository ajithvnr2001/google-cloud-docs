---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snort-ids/
title: Collect Snort IDS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:13.868953+00:00
---

# Collect Snort IDS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snort-ids/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Snort IDS logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Snort IDS logs to Google Security Operations using the Bindplane agent.

Snort is an open-source intrusion detection and prevention system that generates syslog messages for network intrusion alerts, protocol analysis events, and traffic anomalies. The parser extracts fields from syslog-formatted and JSON-formatted logs using grok patterns and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Snort device
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Terminal access to the Snort device



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

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

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
          chronicle/snort_ids:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: SNORT_IDS
            raw_log_field: body
        
        service:
          pipelines:
            logs/snort_ids_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/snort_ids
        




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
          chronicle/snort_ids:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: SNORT_IDS
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
             




## Configure syslog export on Snort v2.x

  1. Sign in to the Snort device using terminal.
  2. Edit the following file: `/etc/snort/snort.conf`.
  3. Go to `6) Configure output plugins`.
  4. Add the following entry:
         
         # syslog output
         alert_syslog: host=<BINDPLANE_IP>:<PORT_NUMBER>, LOG_AUTH LOG_ALERT
         

     * Replace `<BINDPLANE_IP>` with the Bindplane agent IP address and `<PORT_NUMBER>` with the port number.
  5. Save the file.

  6. Start the **snort** service.

  7. Stop the **rsyslog** service.

  8. Edit the following file: `/etc/rsyslogd.conf`:
         
         # remote host is: name/ip:port
         *.* @@<BINDPLANE_IP>:<PORT_NUMBER>
         

     * Replace `<BINDPLANE_IP>` with the Bindplane agent IP address and `<PORT_NUMBER>` with the port number.
  9. Start the **rsyslog** service.




## Configure syslog export on Snort v3.1.53

  1. Sign in to the Snort device using terminal.
  2. Stop the **rsyslog** and **snort** services.
  3. Go to the Snort installation directory: `/usr/local/etc/snort/`.
  4. Edit the Snort configuration file: `snort.lua`.
  5. In the **Configure outputs** options, append the following code:
         
         alert_syslog = {
             facility = 'local3',
             level = 'info',
         }
         

  6. Save the Snort configuration file.

  7. Go to the **rsyslog** service default configuration files directory: `/etc/rsyslog.d`.

  8. Create a new file: `3-snort.conf`.

  9. To send logs over TCP or UDP, add the following configuration:
         
         local3.* @@<BINDPLANE_IP>:<PORT_NUMBER>
         

     * Replace `<BINDPLANE_IP>` with the Bindplane agent IP address and `<PORT_NUMBER>` with the port number.
  10. Save the file.

  11. Start **rsyslog** and then the **snort** service.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
agent.hostname | observer.hostname | Value taken from `agent.hostname` field in the raw log.  
agent.id | observer.asset_id | Value taken from `agent.id` field in the raw log and concatenated with `agent.type` as follows: `agent.type:agent.id`.  
agent.type | observer.application | Value taken from `agent.type` field in the raw log.  
agent.version | observer.platform_version | Value taken from `agent.version` field in the raw log.  
alert.category | security_result.category_details | Value taken from `alert.category` field in the raw log.  
alert.rev | security_result.rule_version | Value taken from `alert.rev` field in the raw log.  
alert.rule | security_result.summary | Value taken from `alert.rule` field in the raw log, with double quotes removed.  
alert.severity | security_result.severity | If `alert.severity` is greater than or equal to 4, set to `LOW`. If `alert.severity` is 2 or 3, set to `MEDIUM`. If `alert.severity` is 1, set to `HIGH`. Otherwise, set to `UNKNOWN_SEVERITY`.  
alert.signature | security_result.rule_name | Value taken from `alert.signature` field in the raw log.  
alert.signature_id | security_result.rule_id | Value taken from `alert.signature_id` field in the raw log.  
app_proto | network.application_protocol | If `app_proto` is `dns`, `smb`, or `http`, convert to uppercase and use that value. Otherwise, set to `UNKNOWN_APPLICATION_PROTOCOL`.  
category | security_result.category | If `category` is `trojan-activity`, set to `NETWORK_MALICIOUS`. If `category` is `policy-violation`, set to `POLICY_VIOLATION`. Otherwise, set to `UNKNOWN_CATEGORY`.  
classtype | security_result.rule_type | Value taken from `classtype` field in the raw log, if it's not empty or `unknown`.  
community_id | network.community_id | Value taken from `community_id` field in the raw log.  
date_log |  | Used to set the event timestamp if `time` field is empty.  
desc | metadata.description | Value taken from `desc` field in the raw log.  
dest_ip | target.ip | Value taken from `dest_ip` field in the raw log.  
dest_port | target.port | Value taken from `dest_port` field in the raw log and converted to integer.  
dstport | target.port | Value taken from `dstport` field in the raw log and converted to integer.  
file.filename | security_result.about.file.full_path | Value taken from `file.filename` field in the raw log, if it's not empty or `/`.  
file.size | security_result.about.file.size | Value taken from `file.size` field in the raw log and converted to unsigned integer.  
host.name | principal.hostname | Value taken from `host.name` field in the raw log.  
hostname | principal.hostname | Value taken from `hostname` field in the raw log.  
inter_host | intermediary.hostname | Value taken from `inter_host` field in the raw log.  
log.file.path | principal.process.file.full_path | Value taken from `log.file.path` field in the raw log.  
metadata.version | metadata.product_version | Value taken from `metadata.version` field in the raw log.  
proto | network.ip_protocol | Value taken from `proto` field in the raw log. If it's a number, it's converted to the corresponding IP protocol name using a lookup table.  
rule_name | security_result.rule_name | Value taken from `rule_name` field in the raw log.  
signature_id | security_result.rule_id | Value taken from `signature_id` field in the raw log.  
signature_rev | security_result.rule_version | Value taken from `signature_rev` field in the raw log.  
src_ip | principal.ip | Value taken from `src_ip` field in the raw log.  
src_port | principal.port | Value taken from `src_port` field in the raw log and converted to integer.  
srcport | principal.port | Value taken from `srcport` field in the raw log and converted to integer.  
time |  | Used to set the event timestamp.  
| metadata.event_type | Always set to `SCAN_NETWORK`.  
| metadata.log_type | Hardcoded to `SNORT_IDS`.  
| metadata.product_name | Hardcoded to `SNORT_IDS`.  
| metadata.vendor_name | Hardcoded to `SNORT`.  
| security_result.action | Set to `ALLOW` if `alert.action` is `allowed`, otherwise set to `UNKNOWN_ACTION`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snort-ids-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
