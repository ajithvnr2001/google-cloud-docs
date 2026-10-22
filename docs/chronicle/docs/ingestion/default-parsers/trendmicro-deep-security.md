---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-deep-security/
title: Collect Trend Micro Deep Security logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:35.362686+00:00
---

# Collect Trend Micro Deep Security logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-deep-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trend Micro Deep Security logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Trend Micro Deep Security logs to Google Security Operations using Bindplane. Trend Micro Deep Security is a server security platform that provides anti-malware, IPS, firewall, integrity monitoring, log inspection, and application control for physical, virtual, and cloud workloads. Deep Security is consolidating under the Trend Vision One platform, but the Deep Security Manager continues to generate syslog events for all protection modules.

For more information, see [Collect Trend Micro Deep Security logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-deep-security).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Trend Micro Deep Security Manager web console with administrator or auditor role.
  * Deep Security Manager 20.0 or later.



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
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "[https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi](https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi)" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         




### Additional installation resources

  * For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

**Note:** Trend Micro Deep Security uses TCP for syslog forwarding to ensure reliable delivery of security events. The Bindplane agent must be configured with a `tcplog` receiver.

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it is in the `/opt/observiq-otel-collector/config.yaml` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           tcplog:
             listen_address: "0.0.0.0:1514"
         
         exporters:
           chronicle/trendmicro_ds:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             customer_id: '<CUSTOMER_ID>'
             endpoint: chronicle.googleapis.com
             log_type: TRENDMICRO_DEEP_SECURITY
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/trendmicro_ds_to_chronicle:
               receivers:
                 - tcplog
               exporters:
                 - chronicle/trendmicro_ds
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * Replace `<CUSTOMER_ID>` with the actual customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the path where the service account key file (Option 1) was saved.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/trendmicro_ds:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: TRENDMICRO_DEEP_SECURITY
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in Windows, you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure syslog forwarding on Trend Micro Deep Security

### Configure syslog settings in Deep Security Manager

  1. Sign in to the **Trend Micro Deep Security Manager** web console.
  2. Go to **Administration > System Settings > Event Forwarding**.
  3. In the **SIEM** section, select **Forward Events to a remote computer (via Syslog)**.
  4. Click **Edit** next to the syslog configuration.

  5. Provide the following configuration details:

     * **Server Name** : Enter the IP address of the Bindplane agent host.
     * **Server Port** : Enter `1514` (or your configured port).
     * **Transport** : Select **TCP**.
     * **Event Format** : Select **Common Event Format (CEF)**.
**Note:** CEF format is recommended for optimal parsing with Google SecOps.
  6. Click **OK** to save the syslog server configuration.




### Select event types to forward

  1. In the **Event Forwarding** tab, configure which event types to forward:

     * **Anti-Malware Events** : Select **Forward Anti-Malware Events to Syslog**.
     * **Web Reputation Events** : Select **Forward Web Reputation Events to Syslog**.
     * **Firewall Events** : Select **Forward Firewall Events to Syslog**.
     * **Intrusion Prevention Events** : Select **Forward Intrusion Prevention Events to Syslog**.
     * **Integrity Monitoring Events** : Select **Forward Integrity Monitoring Events to Syslog**.
     * **Log Inspection Events** : Select **Forward Log Inspection Events to Syslog**.
     * **Application Control Events** : Select **Forward Application Control Events to Syslog**.
     * **System Events** : Select **Forward System Events to Syslog**.
  2. Click **Save**.




### Configure policy-level syslog (optional)

If you need to configure syslog forwarding for specific policies:

  1. Go to **Policies**.
  2. Double-click the policy you want to configure.
  3. Go to **Settings > Event Forwarding**.

  4. For each protection module, you can override the global syslog settings:

     * Select **Inherit** to use the global setting.
     * Select **Yes** to enable syslog forwarding for the specific policy.
     * Select **No** to disable syslog forwarding for the specific policy.
  5. Click **Save**.




### Verify syslog forwarding

  1. In the **Deep Security Manager** , go to **Events & Reports > Events**.
  2. Verify that security events are being generated.
  3. Check the Bindplane agent logs to confirm that syslog messages are being received on the TCP listener:
         
         sudo journalctl -u observiq-otel-collector -f
         




For more information, see [Trend Micro Deep Security syslog documentation](https://help.deepsecurity.trendmicro.com/20_0/on-premise/event-syslog.html).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`dvc` | `about.ip` | Merged  
`aggregation_type_label` | `additional.fields` | Merged  
`cn1Label` | `additional.fields` | Mapped: `Host ID` → `cn1_label`  
`cn1_label` | `additional.fields` | Merged  
`fileInCompressedFile_label` | `additional.fields` | Merged  
`repeat_count_label` | `additional.fields` | Merged  
`cef_host` | `intermediary.hostname` | Directly mapped  
`hostname` | `intermediary.hostname` | Directly mapped  
`cef_host` | `intermediary.ip` | Merged  
`hostname` | `intermediary.ip` | Merged  
`desc` | `metadata.description` | Directly mapped  
`timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_HTTP`, `true` → `STATUS_UPDATE`  
`TrendMicroDsTenant` | `metadata.product_deployment_id` | Directly mapped  
`event_id` | `metadata.product_event_type` | Directly mapped  
`log_type` | `metadata.product_name` | Directly mapped  
`product_version` | `metadata.product_version` | Directly mapped  
`organization` | `metadata.vendor_name` | Directly mapped  
`proto` | `network.ip_protocol` | Mapped: `ICMPv6` → `ICMP`  
`in` | `network.received_bytes` | Renamed/mapped  
`out` | `network.sent_bytes` | Renamed/mapped  
`dvchost` | `principal.asset.hostname` | Directly mapped  
`shost` | `principal.asset.hostname` | Directly mapped  
`src` | `principal.asset.ip` | Merged  
`dvchost` | `principal.hostname` | Directly mapped  
`shost` | `principal.hostname` | Directly mapped  
`src` | `principal.ip` | Merged  
`smac` | `principal.mac` | Merged  
`srcMAC` | `principal.mac` | Merged  
`spt` | `principal.port` | Directly mapped  
`srcPort` | `principal.port` | Directly mapped  
`TrendMicroDsProcessPid` | `principal.process.pid` | Directly mapped  
`suser` | `principal.user.user_display_name` | Directly mapped  
`suid` | `principal.user.userid` | Directly mapped  
`usrName` | `principal.user.userid` | Directly mapped  
`action` | `security_result.action` | Merged  
`act` | `security_result.action_details` | Directly mapped  
`result` | `security_result.action_details` | Directly mapped  
`cat` | `security_result.category_details` | Merged  
`msg` | `security_result.description` | Directly mapped  
`TrendMicroDsPacketData_label` | `security_result.detection_fields` | Merged  
`behaviour_type_field` | `security_result.detection_fields` | Merged  
`cn3_label` | `security_result.detection_fields` | Merged  
`count_label` | `security_result.detection_fields` | Merged  
`cs1_label` | `security_result.detection_fields` | Merged  
`cs2_label` | `security_result.detection_fields` | Merged  
`cs3_label` | `security_result.detection_fields` | Merged  
`cs4_label` | `security_result.detection_fields` | Merged  
`cs5_label` | `security_result.detection_fields` | Merged  
`cs6_label` | `security_result.detection_fields` | Merged  
`cs7_label` | `security_result.detection_fields` | Merged  
`frame_type_field` | `security_result.detection_fields` | Merged  
`malware_target` | `security_result.detection_fields` | Merged  
`process_label` | `security_result.detection_fields` | Merged  
`target_type` | `security_result.detection_fields` | Merged  
`tenant_field` | `security_result.detection_fields` | Merged  
`tenant_id_field` | `security_result.detection_fields` | Merged  
`sev` | `security_result.severity` | Mapped: `"0", "1", "2", "3", "LOW"` → `LOW`, `"4", "5", "6", "MEDIUM"` → `MEDIUM`, `"7", "8"...  
`sev` | `security_result.severity_details` | Directly mapped  
`name` | `security_result.summary` | Directly mapped  
`result` | `security_result.summary` | Directly mapped  
`event_name` | `security_result.threat_name` | Directly mapped  
`organization` | `target.administrative_domain` | Directly mapped  
`cef_host` | `target.asset.hostname` | Directly mapped  
`hostname` | `target.asset.hostname` | Directly mapped  
`target` | `target.asset.hostname` | Directly mapped  
`dst` | `target.asset.ip` | Merged  
`filePath` | `target.file.full_path` | Directly mapped  
`cs3` | `target.file.md5` | Directly mapped  
`TrendMicroDsFileSHA1` | `target.file.sha1` | Directly mapped  
`cs2` | `target.file.sha1` | Directly mapped  
`fileHash` | `target.file.sha256` | Directly mapped  
`cn2` | `target.file.size` | Renamed/mapped  
`fsize` | `target.file.size` | Renamed/mapped  
`cef_host` | `target.hostname` | Directly mapped  
`hostname` | `target.hostname` | Directly mapped  
`target` | `target.hostname` | Directly mapped  
`dst` | `target.ip` | Merged  
`dmac` | `target.mac` | Merged  
`dstMAC` | `target.mac` | Merged  
`dpt` | `target.port` | Directly mapped  
`dstPort` | `target.port` | Directly mapped  
`duser` | `target.user.user_display_name` | Directly mapped  
N/A | `metadata.event_type` | Constant: `NETWORK_HTTP`  
N/A | `network.ip_protocol` | Constant: `ICMP`  
N/A | `security_result.severity` | Constant: `LOW`  
`cs4" , "TrendMicroDsPacketData" and "cn3` | `security_result.detection_fields` | Mapped from changelog  
`cn1` | `principal.asset_id` | Mapped from changelog  
`security_result.action` | `BLOCK` | Mapped from changelog  
`cef_host" and "hostname` | `intermediary.ip` | Mapped from changelog  
`TrendMicroDsMalwareTarget","TrendMicroDsProcess", "TrendMicroDsMalwareTargetCount","TrendMicroDsMalwareTargetType" and "TrendMicroDsBehaviorType` | `security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-deep-security-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
