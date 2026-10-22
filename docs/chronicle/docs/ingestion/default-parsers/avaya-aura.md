---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/avaya-aura/
title: Collect Avaya Aura logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:07.642494+00:00
---

# Collect Avaya Aura logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/avaya-aura/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Avaya Aura logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Avaya Aura logs to Google Security Operations using the Bindplane agent.

Avaya Aura is a unified communications platform that generates syslog messages for user login/logout events, system configuration changes, and security events. The parser extracts fields from syslog messages using grok patterns and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Avaya Aura system
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Avaya Aura



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
          chronicle/avaya_aura:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: AVAYA_AURA
            raw_log_field: body
        
        service:
          pipelines:
            logs/avaya_aura_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/avaya_aura
        




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
          chronicle/avaya_aura:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: AVAYA_AURA
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
             




## Configure syslog in Avaya Aura

  1. Sign in to the **Avaya Aura** console.
  2. Go to **EM > System Configuration > Logging Settings > Syslog**.
  3. Enable **SYSLOG Delivery of Logs**.
  4. Click **Add**.
  5. Provide the following configuration details: 
     * **Server Address** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent listening port.
  6. Click **Save**.
  7. Click **Confirm**.
  8. **Restart** Avaya Aura.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
data{}.@timestamp | metadata.event_timestamp | The event timestamp is parsed from the data field using the grok pattern and assigned to the event_timestamp field in the metadata section of the UDM.  
data{}.host | principal.hostname | The host value is extracted from the data field using the grok pattern and assigned to the hostname field within the principal section of the UDM.  
data{}.portal | security_result.about.resource.attribute.labels.value | The portal value is extracted from the data field using the grok pattern and assigned as the value of the `Portal` label within the about.resource.attribute.labels section of the security_result in the UDM.  
data{}.prod_log_id | metadata.product_log_id | The prod_log_id value is extracted from the data field using the grok pattern and assigned to the product_log_id field in the metadata section of the UDM.  
data{}.sec_cat | security_result.category_details | The sec_cat value is extracted from the data field using the grok pattern and assigned to the category_details field within the security_result section of the UDM.  
data{}.sec_desc | security_result.description | The sec_desc value is extracted from the data field using the grok pattern and assigned to the description field within the security_result section of the UDM.  
data{}.severity | security_result.severity | The severity value is extracted from the data field using the grok pattern. If the severity is `warn`, `fatal`, or `error` (case-insensitive), it is mapped to `HIGH` in the security_result.severity field of the UDM. Otherwise, if the severity is `info` (case-insensitive), it is mapped to `LOW`.  
data{}.summary | security_result.summary | The summary value is extracted from the data field using the grok pattern and assigned to the summary field within the security_result section of the UDM.  
data{}.user_id | target.user.userid | The user_id value is extracted from the data field using the grok pattern and assigned to the userid field within the target.user section of the UDM.  
| extensions.auth.type | The auth.type field is set to `AUTHTYPE_UNSPECIFIED` if the event_name field contains `log(in|on)` or `logoff` (case-insensitive), or if the summary field contains `login` or `logoff` (case-insensitive) and the user_id field is not empty.  
| metadata.description | The description field is populated with the value of the desc field if it is not empty.  
| metadata.event_type | The event_type field is determined based on the following logic: - If the event_name field contains `log(in|on)` or the summary field contains `login` (case-insensitive) and the user_id field is not empty, the event_type is set to `USER_LOGIN`. - If the event_name field contains `logoff` or the summary field contains `logoff` (case-insensitive) and the user_id field is not empty, the event_type is set to `USER_LOGOUT`. - If the has_principal field is `true`, the event_type is set to `STATUS_UPDATE`. - Otherwise, the event_type remains as `GENERIC_EVENT` (default value).  
| metadata.log_type | The log_type is hardcoded to `AVAYA_AURA`.  
| metadata.product_event_type | The product_event_type field is populated with the value of the event_name field if it is not empty.  
| metadata.product_name | The product_name is hardcoded to `AVAYA AURA`.  
| metadata.vendor_name | The vendor_name is hardcoded to `AVAYA AURA`.  
| security_result.action | The action field within the security_result section is set based on the following logic: - If the summary field contains `fail` or `failed` (case-insensitive), the action is set to `BLOCK`. - If the summary field contains `success` (case-insensitive), the action is set to `ALLOW`.  
| security_result.severity_details | The severity_details field is populated with the value of the severity_details field if it is not empty.  
timestamp.nanos | metadata.event_timestamp.nanos | The nanos value from the timestamp field is directly mapped to the nanos field within the event_timestamp section of the metadata in the UDM.  
timestamp.seconds | metadata.event_timestamp.seconds | The seconds value from the timestamp field is directly mapped to the seconds field within the event_timestamp section of the metadata in the UDM.  
`time` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`src_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`dst_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`dst_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`process_pid` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`principal_application` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`network_protocol` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`application_protocol_version` | `event.idm.read_only_udm.network.application_protocol_version` | Mapped from changelog  
`community_id` | `event.idm.read_only_udm.network.community_id` | Mapped from changelog  
`security_description` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`device_uptime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cmg_trap_subsystem` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cmg_trap_onboard` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cmg_trap_location` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog_priority` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/avaya-aura-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
