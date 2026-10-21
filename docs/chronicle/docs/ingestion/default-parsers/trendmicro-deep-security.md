---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-deep-security/
title: Collect Trend Micro Deep Security logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:00:37.765099+00:00
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



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Collection Agent**.
  3. Download the **Ingestion Authentication File**. 
     * Save the file securely on the system where Bindplane will be installed.



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
                 compression: gzip
                 creds_file_path: '/path/to/ingestion-authentication-file.json'
                 customer_id: '<CUSTOMER_ID>'
                 endpoint: malachiteingestion-pa.googleapis.com
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
  * Replace `<CUSTOMER_ID>` with the actual customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the path where the authentication file was saved.



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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
