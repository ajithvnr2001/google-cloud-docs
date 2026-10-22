---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/huawei-switch/
title: Collect Huawei Switch logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:21.037370+00:00
---

# Collect Huawei Switch logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/huawei-switch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Huawei Switch logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Huawei Switch logs to Google Security Operations using the Bindplane agent.

Huawei enterprise network switches generate syslog messages for interface events, authentication, spanning tree, and configuration changes. The logs follow standard syslog format and capture principal and target network attributes, user identity, process metadata, and security result details.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Huawei switch
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Huawei switch management interface (CLI or web)



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
          chronicle/huawei_switch:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: HUAWEI_SWITCH
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/huawei_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/huawei_switch
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `udplog`: The receiver type based on protocol: 
      * `udplog` for UDP syslog
      * `tcplog` for TCP syslog
    * `0.0.0.0`: IP address to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Specific IP address to listen on one interface
    * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)
  * **Exporter configuration:**

    * `huawei_switch`: Descriptive name for the exporter
    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `HUAWEI_SWITCH`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `huawei_to_chronicle`: Descriptive name for the pipeline



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/huawei_switch:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: HUAWEI_SWITCH
            raw_log_field: body
            ingestion_labels:
              env: production
        


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
             




## Configure Huawei Switch syslog forwarding

  1. Connect to the Huawei switch via SSH or console.
  2. Enter the system view:
         
         system-view
         

  3. Enable the information center if not already enabled:
         
         info-center enable
         

  4. Configure the syslog host to point to the Bindplane agent:
         
         info-center loghost <BINDPLANE_AGENT_IP>
         

     * Replace `<BINDPLANE_AGENT_IP>` with the IP address of the Bindplane agent host.
  5. (Optional) Set the facility and severity level:
         
         info-center loghost <BINDPLANE_AGENT_IP> facility local7 level informational
         

  6. Commit the configuration:
         
         commit
         

  7. Verify the configuration:
         
         display info-center
         

  8. Verify that syslog messages are being received by checking the Bindplane agent logs.

**Note:** Huawei switches send syslog over UDP port 514 by default. Adjust the severity level based on the log detail you require. Use `level debugging` for maximum verbosity during troubleshooting.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`AuthenticationMethod_label` | `additional.fields` | Merged  
`Command_label` | `additional.fields` | Merged  
`DeviceType_label` | `additional.fields` | Merged  
`Flapping_port_1_label` | `additional.fields` | Merged  
`Flapping_port_label` | `additional.fields` | Merged  
`InfoID_label` | `additional.fields` | Merged  
`Interface_label` | `additional.fields` | Merged  
`Task_label` | `additional.fields` | Merged  
`VLANID_label` | `additional.fields` | Merged  
`accept_label` | `additional.fields` | Merged  
`alarmID_label` | `additional.fields` | Merged  
`assistant_name_label` | `additional.fields` | Merged  
`body_label` | `additional.fields` | Merged  
`clearType_label` | `additional.fields` | Merged  
`content_type_label` | `additional.fields` | Merged  
`event_identifier_label` | `additional.fields` | Merged  
`facilityName_label` | `additional.fields` | Merged  
`facility_label` | `additional.fields` | Merged  
`frag_index_label` | `additional.fields` | Merged  
`original_port_label` | `additional.fields` | Merged  
`port_2_label` | `additional.fields` | Merged  
`service_flapping_port1_label` | `additional.fields` | Merged  
`service_flapping_port2_label` | `additional.fields` | Merged  
`service_original_port_label` | `additional.fields` | Merged  
`severity_label` | `additional.fields` | Merged  
`vlan_id_label` | `additional.fields` | Merged  
`has_principal` | `extensions.auth.type` | Mapped: `true` → `AUTHTYPE_UNSPECIFIED`  
`hostname` | `intermediary.hostname` | Directly mapped  
`raw_hostname` | `intermediary.hostname` | Directly mapped  
`desc` | `metadata.description` | Directly mapped  
`logfile_description` | `metadata.description` | Directly mapped  
`service_mac_description` | `metadata.description` | Directly mapped  
`temp_description` | `metadata.description` | Directly mapped  
`raw_syslog_timestamp` | `metadata.event_timestamp` | Parsed as `MMM d yyyy HH:mm:ss`  
`syslog_timestamp` | `metadata.event_timestamp` | Parsed as `MMM dd yyyy HH:mm:ss.SSS`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `USER_LOGOUT`, `true` → `STATUS_UPDATE`, `true` → `NETWORK_CONNECTION`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`cid` | `metadata.product_log_id` | Directly mapped  
`temp_cid` | `metadata.product_log_id` | Directly mapped  
`temp_service` | `metadata.product_log_id` | Directly mapped  
`UserType` | `network.application_protocol` | Mapped: `(?i)SSH` → `SSH`  
`Method` | `network.http.method` | Directly mapped  
`SessionId` | `network.session_id` | Directly mapped  
`devid` | `principal.asset.asset_id` | Directly mapped  
`SourceAddress` | `principal.asset.ip` | Merged  
`host` | `principal.asset.ip` | Mapped: `^(?:[0-9]{1,3}[.]){3}[0-9]{1,3}$` → `host`  
`Ip` | `principal.ip` | Merged  
`RemoteIp` | `principal.ip` | Merged  
`SourceAddress` | `principal.ip` | Merged  
`host` | `principal.ip` | Mapped: `^(?:[0-9]{1,3}[.]){3}[0-9]{1,3}$` → `host`  
`MacAddress` | `principal.mac` | Merged  
`mac_address` | `principal.mac` | Merged  
`cmd` | `principal.process.command_line` | Directly mapped  
`ProcessId` | `principal.process.pid` | Directly mapped  
`VpnName` | `principal.resource.name` | Directly mapped  
`temp_oid` | `principal.resource.product_object_id` | Directly mapped  
`User` | `principal.user.userid` | Directly mapped  
`UserName` | `principal.user.userid` | Directly mapped  
`Reason` | `security_result.description` | Directly mapped  
`severityName` | `security_result.severity` | Mapped: `warning` → `MEDIUM`  
`severityName` | `security_result.severity_details` | Directly mapped  
`state` | `security_result.severity_details` | Directly mapped  
`DestAddress` | `target.asset.ip` | Merged  
`DestAddress` | `target.ip` | Merged  
`Destination` | `target.ip` | Merged  
`LocalIp` | `target.ip` | Merged  
`temp_security` | `target.resource.name` | Directly mapped  
`tty_type` | `target.resource.name` | Directly mapped  
`Url` | `target.url` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `USER_LOGOUT`  
N/A | `metadata.product_name` | Constant: `HUAWEI_SWITCH`  
N/A | `metadata.vendor_name` | Constant: `HUAWEI_SWITCH`  
N/A | `network.application_protocol` | Constant: `SSH`  
N/A | `security_result.severity` | Constant: `MEDIUM`  
`UserAddress` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`LocalAddress` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`FailedReason` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`VPNInstanceName` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`event_hostname` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`desc_input` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`event_type_value` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`event_identifier_value` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`UserType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ServiceType` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`IPADDRESS` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`InterfaceName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`TrapThreshold` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`BandWidthUsage` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`UserName` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`SourceAddress` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`SourceAddress` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`DestAddress` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`DestAddress` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`Method` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`SessionId` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`Url` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`FragIndex` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Accept` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ContentType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Body` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AssistantName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`raw_syslog_timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`raw_hostname` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`mac_address` | `event.idm.read_only_udm.principal.mac` | Mapped from changelog  
`temp_oid` | `event.idm.read_only_udm.principal.resource.product_object_id` | Mapped from changelog  
`severity` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`facility` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`facilityName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`severityName` | `event.idm.read_only_udm.security_result.severity_details` | Mapped from changelog  
`severityName` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`DeviceType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog_timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`devid` | `event.idm.read_only_udm.principal.asset.asset_id` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/huawei-switch-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
