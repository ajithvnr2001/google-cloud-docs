---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-esm/
title: Collect McAfee ESM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:14.270856+00:00
---

# Collect McAfee ESM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-esm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect McAfee ESM logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Trellix Enterprise Security Manager logs to Google Security Operations using the Bindplane agent.

Trellix Enterprise Security Manager (formerly McAfee ESM) is a security information and event management (SIEM) platform that provides real-time threat detection, correlation, and compliance monitoring. It collects, normalizes, and analyzes security event data from across the enterprise, enabling security teams to identify and respond to threats through centralized dashboards, advanced analytics, and automated alerting.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Trellix Enterprise Security Manager console



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
  3. Copy and save the **customer ID** from the **Organization Details** section.



## Install the Bindplane Agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows Installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux Installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional Installation Resources

  * For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane Agent to ingest Syslog and send to Google SecOps

  1. Access the Configuration File:

     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           tcplog:
             # Replace the port and IP address as required
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: YOUR_CUSTOMER_ID_HERE
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'MCAFEE_ESM'
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/source0__chronicle_w_labels-0:
               receivers:
                 - tcplog
               exporters:
                 - chronicle/chronicle_w_labels
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `YOUR_CUSTOMER_ID_HERE` with the actual Customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in Step 1.
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: YOUR_CUSTOMER_ID_HERE
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'MCAFEE_ESM'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane Agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure Trellix Enterprise Security Manager syslog forwarding

  1. Sign in to the **Trellix Enterprise Security Manager** console.
  2. Go to **System Properties > Event Forwarding**.
  3. Click **Add** to create a new event forwarding destination.
  4. In the **Name** field, enter a descriptive name (for example, `Chronicle-Bindplane`).
  5. In the **Destination** section, provide the following configuration details: 
     * **IP Address** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (or the port configured in Bindplane).
     * **Protocol** : Select **TCP**.
     * **Format** : Select **Syslog** (CEF or standard syslog format).
  6. In the **Filters** section, select the event types and severity levels to forward: 
     * Select **All Events** to forward all events, or configure specific filters.
     * Set the **Severity** threshold as needed (for example, **1-100** for all severity levels).
  7. Enable the forwarding rule by selecting the **Enabled** check-box.
  8. Click **OK** to save the configuration.
  9. Click **Apply** to activate the event forwarding.
  10. Verify that events are being forwarded by checking the **Event Forwarding** status in the ESM console.

**Note:** For more information, see the [Trellix Enterprise Security Manager documentation](https://docs.trellix.com/bundle/enterprise-security-manager-11.7.x-product-guide/page/GUID-4887B258-B40B-4150-B709-2C5B0B781B2D.html).



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`about` | `about` | Merged  
`about_token` | `about` | Merged  
`deviceNtDomain` | `about.administrative_domain` | Renamed/mapped  
`deviceExternalId` | `about.asset.asset_id` | Directly mapped  
`device_product` | `about.asset.asset_id` | Directly mapped  
`device_vendor` | `about.asset.asset_id` | Directly mapped  
`fileHash` | `about.file.full_path` | Directly mapped  
`filePath` | `about.file.full_path` | Renamed/mapped  
`_hash` | `about.file.sha256` | Renamed/mapped  
`fileHash` | `about.file.sha256` | Renamed/mapped  
`fsize` | `about.file.size` | Renamed/mapped  
`dvchost` | `about.hostname` | Renamed/mapped  
`ips` | `about.ip` | Merged  
`subjectLogonId_label` | `about.labels` | Merged  
`dvcmac` | `about.mac` | Merged  
`mac_address` | `about.mac` | Merged  
`deviceTranslatedAddress` | `about.nat_ip` | Merged  
`Emne` | `about.process.command_line` | Directly mapped  
`Path` | `about.process.command_line` | Directly mapped  
`Subject` | `about.process.command_line` | Directly mapped  
`deviceProcessName` | `about.process.command_line` | Renamed/mapped  
`dvcpid` | `about.process.pid` | Renamed/mapped  
`permissions` | `about.resource.attribute.permissions` | Merged  
`ARCH_label` | `additional.fields` | Merged  
`AUID_label` | `additional.fields` | Merged  
`EGID_label` | `additional.fields` | Merged  
`EUID_label` | `additional.fields` | Merged  
`FSGID_label` | `additional.fields` | Merged  
`FSUID_label` | `additional.fields` | Merged  
`GID_label` | `additional.fields` | Merged  
`SGID_label` | `additional.fields` | Merged  
`SUID_label` | `additional.fields` | Merged  
`SYSCALL_label` | `additional.fields` | Merged  
`UID_label` | `additional.fields` | Merged  
`additional_cfp1` | `additional.fields` | Merged  
`additional_cfp2` | `additional.fields` | Merged  
`additional_cfp3` | `additional.fields` | Merged  
`additional_cfp4` | `additional.fields` | Merged  
`additional_cn1` | `additional.fields` | Merged  
`additional_cn2` | `additional.fields` | Merged  
`additional_cn3` | `additional.fields` | Merged  
`additional_cs1` | `additional.fields` | Merged  
`additional_cs2` | `additional.fields` | Merged  
`additional_cs3` | `additional.fields` | Merged  
`additional_cs4` | `additional.fields` | Merged  
`additional_cs5` | `additional.fields` | Merged  
`additional_cs6` | `additional.fields` | Merged  
`additional_cs7` | `additional.fields` | Merged  
`additional_devicePayloadId` | `additional.fields` | Merged  
`additional_euid` | `additional.fields` | Merged  
`additional_eventId` | `additional.fields` | Merged  
`additional_flexString1` | `additional.fields` | Merged  
`additional_fname` | `additional.fields` | Merged  
`additional_logname` | `additional.fields` | Merged  
`additional_rsa_signature` | `additional.fields` | Merged  
`additional_tty` | `additional.fields` | Merged  
`arch_label` | `additional.fields` | Merged  
`attack_count_label` | `additional.fields` | Merged  
`auid_label` | `additional.fields` | Merged  
`category_label` | `additional.fields` | Merged  
`cmd_param_a0_label` | `additional.fields` | Merged  
`cmd_param_a1_label` | `additional.fields` | Merged  
`cmd_param_a2_label` | `additional.fields` | Merged  
`cmd_param_a3_label` | `additional.fields` | Merged  
`cs5_label` | `additional.fields` | Merged  
`egid_label` | `additional.fields` | Merged  
`euid_label` | `additional.fields` | Merged  
`execution_status_label` | `additional.fields` | Merged  
`exit_code_label` | `additional.fields` | Merged  
`fsgid_label` | `additional.fields` | Merged  
`fsuid_label` | `additional.fields` | Merged  
`interface_label` | `additional.fields` | Merged  
`items_label` | `additional.fields` | Merged  
`key_label` | `additional.fields` | Merged  
`node_label` | `additional.fields` | Merged  
`proctitle_label` | `additional.fields` | Merged  
`sensor_name_label` | `additional.fields` | Merged  
`severity_label` | `additional.fields` | Merged  
`sgid_label` | `additional.fields` | Merged  
`suid_label` | `additional.fields` | Merged  
`syscall_label` | `additional.fields` | Merged  
`tty_label` | `additional.fields` | Merged  
`auth_mechanism` | `extensions.auth.mechanism` | Merged  
`vuln_token` | `extensions.vulns.vulnerabilities` | Merged  
`intermediary` | `intermediary` | Merged  
`Hostname` | `intermediary.hostname` | Directly mapped  
`msg` | `metadata.description` | Directly mapped  
`event_type` | `metadata.event_type` | Directly mapped  
`log_category` | `metadata.log_type` | Directly mapped  
`device_event_class_id` | `metadata.product_event_type` | Directly mapped  
`event_name` | `metadata.product_event_type` | Directly mapped  
`log_type` | `metadata.product_event_type` | Directly mapped  
`type` | `metadata.product_event_type` | Directly mapped  
`column1` | `metadata.product_log_id` | Directly mapped  
`externalId` | `metadata.product_log_id` | Directly mapped  
`device_product` | `metadata.product_name` | Directly mapped  
`sourceName` | `metadata.product_name` | Directly mapped  
`device_version` | `metadata.product_version` | Directly mapped  
`device_vendor` | `metadata.vendor_name` | Renamed/mapped  
`app_protocol_output` | `network.application_protocol` | Directly mapped  
`requestMethod` | `network.http.method` | Renamed/mapped  
`requestClientApplication` | `network.http.user_agent` | Renamed/mapped  
`ip_protocol_out` | `network.ip_protocol` | Directly mapped  
`in` | `network.received_bytes` | Renamed/mapped  
`out` | `network.sent_bytes` | Renamed/mapped  
`ses` | `network.session_id` | Directly mapped  
`session_id` | `network.session_id` | Directly mapped  
`sntdom` | `principal.administrative_domain` | Renamed/mapped  
`sourceServiceName` | `principal.application` | Renamed/mapped  
`Group_name` | `principal.group.group_display_name` | Directly mapped  
`Gruppenavn` | `principal.group.group_display_name` | Directly mapped  
`Device_name` | `principal.hostname` | Directly mapped  
`Enhetsnavn` | `principal.hostname` | Directly mapped  
`hostname` | `principal.hostname` | Directly mapped  
`shost` | `principal.hostname` | Renamed/mapped  
`data.src_ip` | `principal.ip` | Merged  
`principal_ip` | `principal.ip` | Merged  
`shost` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`valid_src_ip` | `principal.ip` | Merged  
`data.src_mac` | `principal.mac` | Directly mapped  
`mac` | `principal.mac` | Merged  
`sourceTranslatedAddress` | `principal.nat_ip` | Merged  
`sourceTranslatedPort` | `principal.nat_port` | Renamed/mapped  
`INT:principal_port` | `principal.port` | Directly mapped  
`data.src_port` | `principal.port` | Directly mapped  
`principal_port` | `principal.port` | Renamed/mapped  
`source_port` | `principal.port` | Renamed/mapped  
`spt` | `principal.port` | Renamed/mapped  
`comm` | `principal.process.command_line` | Directly mapped  
`sproc` | `principal.process.command_line` | Renamed/mapped  
`exe` | `principal.process.file.full_path` | Directly mapped  
`ppid` | `principal.process.parent_pid` | Directly mapped  
`pid` | `principal.process.pid` | Directly mapped  
`spid` | `principal.process.pid` | Renamed/mapped  
`principal_role` | `principal.user.attribute.roles` | Merged  
`gid` | `principal.user.groupid` | Directly mapped  
`ruser` | `principal.user.user_display_name` | Directly mapped  
`suser` | `principal.user.user_display_name` | Directly mapped  
`data.UserIDSrc` | `principal.user.userid` | Directly mapped  
`suid` | `principal.user.userid` | Renamed/mapped  
`uid` | `principal.user.userid` | Directly mapped  
`user_id` | `principal.user.userid` | Directly mapped  
`data.Source_UserID` | `principal.user.windows_sid` | Directly mapped  
`security_result` | `security_result` | Merged  
`security_token` | `security_result` | Merged  
`_action` | `security_result.action` | Merged  
`Action_Taken` | `security_result.action_details` | Directly mapped  
`act` | `security_result.action_details` | Directly mapped  
`cat` | `security_result.category_details` | Merged  
`Scan_Type` | `security_result.description` | Directly mapped  
`Type` | `security_result.description` | Directly mapped  
`data.sig.name` | `security_result.description` | Directly mapped  
`msg_data_2` | `security_result.description` | Directly mapped  
`infection_channel_label` | `security_result.detection_fields` | Merged  
`operasjon_label` | `security_result.detection_fields` | Merged  
`operation_label` | `security_result.detection_fields` | Merged  
`permission_label` | `security_result.detection_fields` | Merged  
`spyware_Grayware_Type_label` | `security_result.detection_fields` | Merged  
`threat_probability_label` | `security_result.detection_fields` | Merged  
`tillatelse_label` | `security_result.detection_fields` | Merged  
`mwProfile` | `security_result.rule_name` | Directly mapped  
`Result` | `security_result.summary` | Directly mapped  
`appcategory` | `security_result.summary` | Directly mapped  
`reason` | `security_result.summary` | Renamed/mapped  
`Spyware` | `security_result.threat_name` | Directly mapped  
`Unknown_Threat` | `security_result.threat_name` | Directly mapped  
`Virus_Malware_Name` | `security_result.threat_name` | Directly mapped  
`oldFilePath` | `src.file.full_path` | Renamed/mapped  
`oldFileSize` | `src.file.size` | Renamed/mapped  
`old_permissions` | `src.resource.attribute.permissions` | Merged  
`data.DomainID` | `target.administrative_domain` | Directly mapped  
`dntdom` | `target.administrative_domain` | Renamed/mapped  
`data.AppID` | `target.application` | Directly mapped  
`destinationServiceName` | `target.application` | Renamed/mapped  
`data.Destination_Hostname` | `target.hostname` | Directly mapped  
`data.HostID` | `target.hostname` | Directly mapped  
`temp_dhost` | `target.hostname` | Directly mapped  
`IPv6_Address` | `target.ip` | Merged  
`data.dst_ip` | `target.ip` | Merged  
`dest_ip` | `target.ip` | Merged  
`dst_ip` | `target.ip` | Merged  
`data.dst_mac` | `target.mac` | Directly mapped  
`mac_address` | `target.mac` | Merged  
`destination_translated_address` | `target.nat_ip` | Merged  
`destinationTranslatedPort` | `target.nat_port` | Renamed/mapped  
`INT:target_port` | `target.port` | Directly mapped  
`data.dst_port` | `target.port` | Directly mapped  
`destination_port` | `target.port` | Renamed/mapped  
`dpt` | `target.port` | Renamed/mapped  
`target_port` | `target.port` | Renamed/mapped  
`data.Process_Name` | `target.process.command_line` | Directly mapped  
`dproc` | `target.process.command_line` | Renamed/mapped  
`File_name` | `target.process.file.full_path` | Directly mapped  
`Infected_Resource` | `target.process.file.full_path` | Directly mapped  
`Object` | `target.process.file.full_path` | Directly mapped  
`Objekt` | `target.process.file.full_path` | Directly mapped  
`data.PID` | `target.process.pid` | Directly mapped  
`dpid` | `target.process.pid` | Renamed/mapped  
`resource_Type_label` | `target.resource.attribute.labels` | Merged  
`request` | `target.url` | Directly mapped  
`target_role` | `target.user.attribute.roles` | Merged  
`CustomerName` | `target.user.user_display_name` | Directly mapped  
`temp_duser` | `target.user.user_display_name` | Directly mapped  
`username` | `target.user.user_display_name` | Directly mapped  
`Bruker` | `target.user.userid` | Directly mapped  
`User_value` | `target.user.userid` | Directly mapped  
`data.UserIDDst` | `target.user.userid` | Directly mapped  
`temp_duid` | `target.user.userid` | Directly mapped  
`data.Destination_UserID` | `target.user.windows_sid` | Directly mapped  
N/A | `about` | Constant: `about_token`  
N/A | `about.ip` | Constant: `ips`  
N/A | `about.labels` | Constant: `subjectLogonId_label`  
N/A | `about.mac` | Constant: `mac_address`  
N/A | `about.nat_ip` | Constant: `deviceTranslatedAddress`  
N/A | `about.resource.attribute.permissions` | Constant: `permissions`  
N/A | `additional.fields` | Constant: `severity_label`  
N/A | `extensions.auth.auth_details` | Constant: `UNKNOWN_AUTHENTICATION_STATUS`  
N/A | `extensions.auth.mechanism` | Constant: `auth_mechanism`  
N/A | `extensions.vulns.vulnerabilities` | Constant: `vuln_token`  
N/A | `intermediary` | Constant: `intermediary`  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.vendor_name` | Constant: `MCAFEE`  
N/A | `network.application_protocol` | Constant: `SSH`  
N/A | `network.direction` | Constant: `INBOUND`  
N/A | `principal.ip` | Constant: `src_ip`  
N/A | `principal.mac` | Constant: `mac`  
N/A | `principal.nat_ip` | Constant: `sourceTranslatedAddress`  
N/A | `principal.user.attribute.roles` | Constant: `principal_role`  
N/A | `security_result` | Constant: `security_token`  
N/A | `security_result.action` | Constant: `_action`  
N/A | `security_result.category_details` | Constant: `cat`  
N/A | `security_result.detection_fields` | Constant: `operation_label`  
N/A | `security_result.severity` | Constant: `LOW`  
N/A | `src.resource.attribute.permissions` | Constant: `old_permissions`  
N/A | `target.ip` | Constant: `dest_ip`  
N/A | `target.mac` | Constant: `mac_address`  
N/A | `target.nat_ip` | Constant: `destination_translated_address`  
N/A | `target.resource.attribute.labels` | Constant: `resource_Type_label`  
N/A | `target.user.attribute.roles` | Constant: `target_role`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
