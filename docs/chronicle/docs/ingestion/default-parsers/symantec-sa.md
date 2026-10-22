---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-sa/
title: Collect Symantec Security Analytics logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:17.202889+00:00
---

# Collect Symantec Security Analytics logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-sa/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Symantec Security Analytics logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Symantec Security Analytics logs to Google Security Operations using Bindplane.

Symantec Security Analytics (formerly Blue Coat) is a network forensics and packet capture platform that provides deep packet inspection, full network visibility, and threat analysis for on-premise deployments.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Symantec Security Analytics appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Symantec Security Analytics appliance with administrator permissions



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

## Configure Bindplane agent to ingest syslog and send to Google SecOps

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
          chronicle/symantec_sa:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: SYMANTEC_SA
            raw_log_field: body
        
        service:
          pipelines:
            logs/symantec_sa_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/symantec_sa
        




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
          chronicle/symantec_sa:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: SYMANTEC_SA
            raw_log_field: body
        


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
         




## Configure Symantec Security Analytics syslog forwarding

  1. Sign in to the **Symantec Security Analytics** appliance web interface.
  2. Go to **System > Alerting > Syslog**.
  3. Click **Add** to create a new syslog destination.
  4. Provide the following configuration details: 
     * **Syslog Server** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Protocol** : Select **UDP**.
     * **Facility** : Select **Local0** or your preferred facility.
  5. Select the log categories to forward (security alerts, system events, network events).
  6. Click **Save** to apply the configuration.
  7. Verify that logs are being sent by checking the Bindplane agent logs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
| additional.fields | Merged from m_label, c_label, start_time_label  
action_name | security_result.action_details | Value copied directly  
category | target.resource.type | Value copied directly  
cs4 | security_result.description | Value copied directly  
cs5 | security_result.summary | Value copied directly  
dmac | target.mac | Value copied directly  
dpt | target.port | Converted to integer  
dst | target.ip | Extracted using grok pattern as dst_ip  
dst | target.asset.ip | Extracted using grok pattern as dst_ip  
elapsed_time | security_result.detection_fields | Merged from elapsed_time_label  
end |  | Converted from epoch ms to timestamp (not used in UDM mapping)  
event_id | security_result.rule_id | Value copied directly  
event_name | metadata.product_event_type | Value copied directly  
evt | metadata.product_event_type | Value copied directly  
host | intermediary.hostname | Value copied directly  
host | intermediary.asset.hostname | Value copied directly  
id | target.resource.id | Value copied directly  
ip | principal.ip | Extracted using grok pattern as ip_address1  
ip | principal.asset.ip | Extracted using grok pattern as ip_address1  
ip_address | principal.ip | Extracted using grok pattern as ip_address2  
ip_address | principal.asset.ip | Extracted using grok pattern as ip_address2  
logmsg | metadata.description | Value copied directly  
m | additional.fields | Merged from m_label  
mac_address | principal.mac | Value copied directly  
model | target.resource.name | Value copied directly  
msgs | metadata.description | Value copied directly  
path | target.file.full_path | Value copied directly  
query_id | target.resource.attribute.labels | Merged from query_id_label  
remote_ip | target.ip | Extracted using grok pattern as r_ipaddress  
remote_ip | target.asset.ip | Extracted using grok pattern as r_ipaddress  
sequenceId | metadata.product_log_id | Value copied directly  
severity | security_result.severity_details | Value copied directly  
severity | security_result.severity | Set to LOW if in ["0","1","2","3"]; MEDIUM if in ["4","5","6"]; HIGH if in ["7","8"]; CRITICAL if in ["9","10"]; else UNKNOWN_SEVERITY  
smac | principal.mac | Value copied directly  
sn | principal.mac | Value copied directly  
spt | principal.port | Converted to integer  
src | principal.ip | Extracted using grok pattern as src_ip  
src | principal.asset.ip | Extracted using grok pattern as src_ip  
start | additional.fields | Merged from start_time_label  
ts | metadata.collected_timestamp | Converted using date match formats  
user | principal.user.userid | Value copied directly  
version | metadata.product_version | Value copied directly  
| metadata.event_type | Set to NETWORK_CONNECTION if has_principal and has_target true; STATUS_UPDATE if has_principal true and has_target false; USER_UNCATEGORIZED if has_principal_user true; else GENERIC_EVENT  
| metadata.product_name | Set to "Security Analytics Platform"  
| metadata.vendor_name | Set to "Symantec Corporation"  
`host` | `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`event_name` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`end` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`ts` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`host` | `principal.hostname` | Mapped from changelog  
`logmsg` | `metadata description` | Mapped from changelog  
`m" and "c` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-sa-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
