---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netapp-ontap/
title: Collect NetApp ONTAP logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:18.772352+00:00
---

# Collect NetApp ONTAP logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netapp-ontap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect NetApp ONTAP logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest NetApp ONTAP logs to Google Security Operations using the Bindplane agent.

NetApp ONTAP is a storage operating system that generates syslog messages for authentication events, system status, network activity, and security-related operations. The parser extracts fields from syslog messages using regular expressions and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the NetApp ONTAP cluster
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the NetApp ONTAP cluster via SSH



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
          chronicle/netapp_ontap:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: NETAPP_ONTAP
            raw_log_field: body
        
        service:
          pipelines:
            logs/netapp_ontap_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/netapp_ontap
        




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
          chronicle/netapp_ontap:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: NETAPP_ONTAP
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
             




## Configure a syslog destination in ONTAP

  1. Access the ONTAP cluster using SSH:
         
         ssh admin@<ontap-cluster-ip>
         

     * Replace `<ontap-cluster-ip>` with the management IP of your ONTAP cluster.
  2. Check existing event filters and notifications:
         
         event filter show
         event notification show
         

  3. Create a syslog destination. Replace `<syslog-server-ip>` and `<syslog-server-port>` with your Bindplane details:
         
         event notification destination create -name syslog-ems -syslog <syslog-server-ip> -syslog-port <syslog-server-port> -syslog-transport udp-unencrypted
         

Other options for `-syslog-transport`:

     * `udp-unencrypted` (default)
     * `tcp-unencrypted`
     * `tcp-encrypted` (for TLS)
  4. Verify the syslog destination:
         
         event notification destination show
         




## Configure existing event filters

  * Link default filters to the syslog destination:
        
        event notification create -filter-name no-info-debug-events -destinations syslog-ems
        event notification create -filter-name default-trap-events -destinations syslog-ems
        




## Optional: Create and configure custom filters

  1. Authentication events filter (logins/logouts):
         
         event filter create -filter-name auth_events
         event filter rule add -filter-name auth_events -type include -message-name *login* -severity info
         event filter rule add -filter-name auth_events -type include -message-name *logout* -severity info
         

  2. Security detection fields filter:
         
         event filter create -filter-name security_fields
         event filter rule add -filter-name security_fields -type include -message-name *nmsdk_language* -severity info
         

  3. Apply each filter to the syslog destination:
         
         event notification create -filter-name auth_events -destinations syslog-ems
         event notification create -filter-name security_fields -destinations syslog-ems
         

  4. Verify notifications:
         
         event notification show
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`code` |  | Not Mapped  
`description` | `metadata.description` | Extracted from the log message using a grok pattern. Present only when the description is "Logging out" or "Logging in".  
`intermediary_host` | `intermediary.hostname` | Extracted from the log message using a grok pattern.  
`nmsdk_language` | `security_result.detection_fields.value` | Extracted from the log message using a grok pattern. This value is added as a "value" to a detection_fields object with "key" = "nmsdk_language".  
`nmsdk_platform` | `security_result.detection_fields.value` | Extracted from the log message using a grok pattern. This value is added as a "value" to a detection_fields object with "key" = "nmsdk_platform".  
`nmsdk_version` | `security_result.detection_fields.value` | Extracted from the log message using a grok pattern. This value is added as a "value" to a detection_fields object with "key" = "nmsdk_version".  
`netapp_version` | `security_result.detection_fields.value` | Extracted from the log message using a grok pattern. This value is added as a "value" to a detection_fields object with "key" = "netapp_version".  
`product_event_type` | `metadata.product_event_type` | Extracted from the log message using a grok pattern.  
`security_result.summary` | `security_result.summary` | Extracted from the log message using a grok pattern.  
`severity` | `security_result.severity` | Set to "INFORMATIONAL" if severity is "info" (case-insensitive).  
`src_ip` | `principal.ip` | Extracted from the log message using a grok pattern.  
`src_port` | `principal.port` | Extracted from the log message using a grok pattern.  
`status` | `security_result.summary` | Extracted from the log message using a grok pattern.  
`ts` | `metadata.event_timestamp.seconds` | Extracted from the log message using a grok pattern and converted to a timestamp.  
`url` | `target.url` | Extracted from the log message using a grok pattern.  
`user` | `target.user.userid` | Extracted from the log message using a grok pattern.  
| `extensions.auth.type` | Set to "AUTHTYPE_UNSPECIFIED" if description is "Logging out" or "Logging in".  
| `metadata.event_type` | Set to "USER_LOGIN" if description is "Logging in".  
| `metadata.event_type` | Set to "USER_LOGOUT" if description is "Logging out".  
| `metadata.event_type` | Set to "SCAN_UNCATEGORIZED" if description is not "Logging in" or "Logging out".  
| `metadata.log_type` | Set to "NETAPP_ONTAP".  
| `metadata.product_name` | Set to "NETAPP_ONTAP".  
| `metadata.vendor_name` | Set to "NETAPP_ONTAP".  
| `target.platform` | Set to "WINDOWS" if nmsdk_platform contains "windows" (case-insensitive).  
`accessLocation` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`accessLocation` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`deviceId` | `event.idm.read_only_udm.principal.asset_id` | Mapped from changelog  
`deviceId` | `event.idm.read_only_udm.principal.asset.asset_id` | Mapped from changelog  
`deviceName` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`deviceName` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`domain` | `event.idm.read_only_udm.principal.administarative_domain` | Mapped from changelog  
`entityName` | `event.idm.read_only_udm.target.file.names` | Mapped from changelog  
`entityPath` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`entityType` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`extension` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`entityAccessedTime` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`alertTimestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`userDisplayName` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`userId` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`volumeId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`volumeName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alertType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`attributes.dataDestructionDetectedEntityCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`attributes.changePercentage` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`severity` | `security_result.severity_details` | Mapped from changelog  
`file_extn` | `security_result.detection_fields` | Mapped from changelog  
`uid` | `metadata.product_log_id` | Mapped from changelog  
`product_name` | `principal.hostname` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netapp-ontap-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
