---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-emps/
title: Collect Trellix Email Security (formerly FireEye eMPS) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:52:31.758333+00:00
---

# Collect Trellix Email Security (formerly FireEye eMPS) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-emps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trellix Email Security (formerly FireEye eMPS) logs

**Parser Version:** 16.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Trellix Email Security (formerly known as FireEye eMPS) logs to Google Security Operations using Bindplane.

Trellix Email Security is an email security appliance that protects organizations from advanced email threats including spear phishing, malware, and targeted attacks by analyzing email content and attachments in real time.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance
  * Windows Server 2016 or later, or Linux host with systemd
  * Network connectivity between Bindplane agent and FireEye eMPS appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the FireEye eMPS appliance CLI (Admin or Operator role)
  * FireEye eMPS appliance with syslog notification capability



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agent**.
  3. Click **Download** to download the **Ingestion Authentication File**.
  4. Save the file securely on the system where Bindplane agent will be installed.

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
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         




The service should show as **active (running)**.

### Additional installation resources

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:** `/opt/observiq-otel-collector/config.yaml`
  * **Windows:** `C:\Program Files\observIQ OpenTelemetry Collector\config.yaml`



### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/fireeye_emps:
            compression: gzip
            creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: FIREEYE_EMPS
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/fireeye_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/fireeye_emps
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * The receiver is configured for UDP syslog on port 514.
    * To use a non-privileged port on Linux, change `514` to `1514` or higher.
    * To use TCP instead of UDP, replace `udplog` with `tcplog`.
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file.
    * `YOUR_CUSTOMER_ID`: Replace with your actual customer ID.
    * `endpoint`: Regional endpoint URL (e.g., `malachiteingestion-pa.googleapis.com`).
    * `log_type`: Must be exactly `FIREEYE_EMPS`.
    * `ingestion_labels`: Optional labels in YAML format.



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
         




## Configure FireEye eMPS syslog forwarding

### Access the FireEye eMPS CLI

  1. Connect to the FireEye eMPS appliance via SSH or console.
  2. Log in and enter enable mode: `hostname> enable`
  3. Enter configuration mode: `hostname# configure terminal`



### Configure syslog server

  1. Add the Bindplane agent as a syslog trap sink: `hostname(config)# fenotify rsyslog trap-sink chronicle address <BINDPLANE_IP_ADDRESS>`
  2. Set the syslog format to CEF: `hostname(config)# fenotify rsyslog trap-sink chronicle prefer message format cef`
  3. Set the syslog facility to local4 (recommended): `hostname(config)# fenotify rsyslog default facility local4`
  4. Set the delivery mode: `hostname(config)# fenotify rsyslog trap-sink chronicle message delivery per-event`
  5. Set the alert severity: `hostname(config)# fenotify rsyslog trap-sink chronicle prefer message send-as alert`
  6. Set the protocol: `hostname(config)# fenotify rsyslog trap-sink chronicle protocol udp`
  7. Set the port: `hostname(config)# fenotify rsyslog trap-sink chronicle port 514`



### Enable syslog notifications

  1. Enable rsyslog notifications globally: `hostname(config)# fenotify rsyslog enable`
  2. Enable global notifications: `hostname(config)# fenotify enable`
  3. Enable specific alert types:
         
         hostname(config)# fenotify rsyslog alert malware-object enable
         hostname(config)# fenotify rsyslog alert malware-callback enable
         hostname(config)# fenotify rsyslog alert infection-match enable
         hostname(config)# fenotify rsyslog alert domain-match enable
         

  4. Verify configuration: `hostname(config)# show fenotify alerts`

  5. Save and exit:
         
         hostname(config)# write memory
         hostname(config)# exit
         hostname# exit
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
| about.asset.asset_id | Concatenated from device_vendor, device_product, and deviceExternalId  
about | about | Merged from about_token  
about.file.full_path | about.file.full_path | Value copied directly  
about.file.sha256 | about.file.sha256 | Value copied directly  
about.file.size | about.file.size | Value copied directly  
about.hostname | about.hostname | Value copied directly  
about.ip | about.ip | Merged from ips array  
about.mac | about.mac | Value from dvcmac if valid MAC, else from mac_address  
about.nat_ip | about.nat_ip | Value copied directly from deviceTranslatedAddress  
about.process.command_line | about.process.command_line | Value from Subject if not empty, else Emne, else Path  
about.process.file.full_path | about.process.file.full_path | Value copied directly  
about.process.pid | about.process.pid | Value copied directly  
about.resource.attribute.permissions | about.resource.attribute.permissions | Value copied directly from permissions  
additional | additional | Renamed directly  
additional_cfp1 | additional.fields | Merged into additional fields  
additional_cfp2 | additional.fields | Merged into additional fields  
additional_cfp3 | additional.fields | Merged into additional fields  
additional_cfp4 | additional.fields | Merged into additional fields  
additional_cn1 | additional.fields | Merged into additional fields  
additional_cn2 | additional.fields | Merged into additional fields  
additional_cn3 | additional.fields | Merged into additional fields  
additional_cs1 | additional.fields | Merged into additional fields  
additional_cs2 | additional.fields | Merged into additional fields  
additional_cs3 | additional.fields | Merged into additional fields  
additional_cs4 | additional.fields | Merged into additional fields  
additional_cs5 | additional.fields | Merged into additional fields  
additional_cs6 | additional.fields | Merged into additional fields  
additional_cs7 | additional.fields | Merged into additional fields  
additional_devicePayloadId | additional.fields | Merged into additional fields  
additional_eventId | additional.fields | Merged into additional fields  
additional_fname | additional.fields | Merged into additional fields  
additional_flexString1 | additional.fields | Merged into additional fields  
additional_flexString2 | additional.fields | Merged into additional fields  
app_protocol_output | network.application_protocol | Value copied directly  
cs1Label, cs1 | additional.fields | Key from cs1Label, value from cs1  
cs2Label, cs2 | additional.fields | Key from cs2Label, value from cs2  
cs3Label, cs3 | additional.fields | Key from cs3Label, value from cs3  
cs4Label, cs4 | additional.fields | Key from cs4Label, value from cs4  
cs5Label, cs5 | additional.fields | Key from cs5Label, value from cs5  
cs6Label, cs6 | additional.fields | Key from cs6Label, value from cs6  
cs7Label, cs7 | additional.fields | Key from cs7Label, value from cs7  
cfp1Label, cfp1 | additional.fields | Key from cfp1Label, value from cfp1  
cfp2Label, cfp2 | additional.fields | Key from cfp2Label, value from cfp2  
cfp3Label, cfp3 | additional.fields | Key from cfp3Label, value from cfp3  
cfp4Label, cfp4 | additional.fields | Key from cfp4Label, value from cfp4  
cn1Label, cn1 | additional.fields | Key from cn1Label, value from cn1  
cn2Label, cn2 | additional.fields | Key from cn2Label, value from cn2  
cn3Label, cn3 | additional.fields | Key from cn3Label, value from cn3  
customer_label | security_result.detection_fields | Merged into detection fields  
destination_translated_address | target.nat_ip | Value copied directly  
device_name_not_present, Enhetsnavn | principal.hostname | Value from Device_name if not empty, else Enhetsnavn  
deviceExternalId | about.asset.asset_id | Part of concatenation  
devicePayloadId | additional.fields | Key as devicePayloadId, value copied  
deviceTranslatedAddress | about.nat_ip | Value copied directly  
device_vendor | about.asset.asset_id | Part of concatenation  
device_product | about.asset.asset_id | Part of concatenation  
device_version | metadata.product_version | Value copied directly  
device_event_class_id, event_name | metadata.product_event_type | Concatenated as [%{device_event_class_id}] - %{event_name} if both present, else device_event_class_id or event_name  
device_process_name | about.process.command_line | Value copied directly  
device_vendor | metadata.vendor_name | Value copied directly  
device_product | metadata.product_name | Value copied directly  
dhost | target.hostname | Value copied directly  
dmac | target.mac | Value copied directly  
dntdom | target.administrative_domain | Value copied directly  
dpid | target.process.pid | Value copied directly  
dproc | target.process.command_line | Value copied directly  
dst | target.asset.ip | Value copied directly  
dst_ip | target.ip | Value copied directly  
duid | target.user.userid | Value from temp_duid after grok extraction  
duser | target.user.user_display_name | Value copied directly  
dvchost | about.hostname | Value copied directly  
deviceNtDomain | about.administrative_domain | Value copied directly  
dvcmac | about.mac | Value from dvcmac if valid MAC  
dvc_mac | about.mac | Value from dvc_mac if valid MAC  
eventId | additional.fields | Key as eventId, value copied  
eventid | additional.fields | Key as eventId, value from eventid  
externalId | metadata.product_log_id | Value copied directly  
externalID_value | metadata.product_log_id | Value copied directly  
file_full_path | metadata.event_type | Set to PROCESS_UNCATEGORIZED if file_full_path not empty  
fileHash | about.file.sha256 | Value copied directly if not hash, else about.file.full_path  
filePath | about.file.full_path | Value copied directly  
fileType | about.file.mime_type | Value copied directly  
flexString1Label, flexString1 | additional.fields | Key from flexString1Label, value from flexString1  
flexString2Label, flexString2 | additional.fields | Key from flexString2Label, value from flexString2  
fname | additional.fields | Key as fname, value copied  
Generated | metadata.event_timestamp | Converted using date match yyyy-MM-ddTHH:mm:ss  
Generert | metadata.event_timestamp | Converted using date match yyyy-MM-ddTHH:mm:ss  
Group_name | principal.group.group_display_name | Value copied directly  
Gruppenavn | principal.group.group_display_name | Value from Gruppenavn if Group_name empty  
infection_channel_label | security_result.detection_fields | Merged into detection fields  
in | network.received_bytes | Converted to uinteger if not 0  
IPv6_Address | target.ip | Merged if not "-"  
ipv6 | target.ip | Merged if not "-"  
mac | principal.mac | Value copied directly  
mac_address | target.mac | Value copied directly  
mac_address | about.mac | Value from mac_address  
metadata | metadata | Renamed directly  
msg | metadata.description | Value copied directly  
msg_data_2 | security_result.description | Value copied directly  
mottatt_not_present, Mottatt | metadata.collected_timestamp | Converted using date match yyyy-MM-ddTHH:mm:ss  
network | network | Renamed directly  
oldFilePath | src.file.full_path | Value copied directly  
oldFileSize | src.file.size | Converted to uinteger  
old_permissions | src.resource.attribute.permissions | Value copied directly  
operasjon_label | security_result.detection_fields | Merged into detection fields  
operation_label | security_result.detection_fields | Merged into detection fields  
out | network.sent_bytes | Converted to uinteger if not 0  
permission_label | security_result.detection_fields | Merged into detection fields  
permissions | about.resource.attribute.permissions | Value copied directly  
principal | principal | Renamed directly  
principal_ip | principal.ip | Value copied directly  
principal_role | principal.user.attribute.roles | Merged into roles  
protocol_number_src | network.ip_protocol | Value copied directly  
Received | metadata.collected_timestamp | Converted using date match yyyy-MM-ddTHH:mm:ss  
reason | security_result.summary | Value copied directly  
request | target.url | Value copied directly  
requestClientApplication | network.http.user_agent | Value copied directly  
requestMethod | network.http.method | Value copied directly  
resource_Type_label | target.resource.attribute.labels | Merged into labels  
rt | @timestamp | Converted using various date formats and timezone adjustments  
security_result | security_result | Merged directly  
security_result_token | security_result | Merged directly  
severity | security_result.severity | Set to LOW if in [0,1,2,3,LOW]; MEDIUM if in [4,5,6,MEDIUM,SUBSTANTIAL,INFO]; HIGH if in [7,8,HIGH,SEVERE]; CRITICAL if in [9,10,VERY-HIGH,CRITICAL]  
shost | principal.hostname | Value copied directly if not IP, else principal.ip  
shost | principal.ip | Value copied directly if IP  
shost_present | principal.machine_id_present | Set to true  
smac | principal.mac | Value copied directly after formatting  
sntdom | principal.administrative_domain | Value copied directly  
sourceDnsDomain | target.asset.hostname, target.hostname | Value from sourceDnsDomain via grok to tar_host  
sourceServiceName | principal.application | Value copied directly  
sourceTranslatedAddress | principal.nat_ip | Value copied directly  
sourceTranslatedPort | principal.nat_port | Converted to integer  
spid | principal.process.pid | Value copied directly  
sproc | principal.process.command_line | Value copied directly  
spt | principal.port | Converted to integer if not 0 or {srcPort}  
src | principal.asset.ip | Value copied directly  
src_ip | principal.ip | Value copied directly  
srcaddr | principal.ip | Value copied directly  
spyware_Grayware_Type_label | security_result.detection_fields | Merged into detection fields  
suser | principal.user.user_display_name | Value copied directly if not starts with {  
suid | principal.user.userid | Value copied directly  
target | target | Renamed directly  
target_ip | target.ip | Value copied directly  
target_role | target.user.attribute.roles | Merged into roles  
temp_data |  | Used in grok patterns  
temp_dhost | target.hostname | Value copied directly  
temp_duser | target.user.user_display_name | Value copied directly  
temp_duid | target.user.userid | Value from temp_duid after grok  
threat_probability_label | security_result.detection_fields | Merged into detection fields  
tillatelse_label | security_result.detection_fields | Merged into detection fields  
type_label | security_result.detection_fields | Merged into detection fields  
User | target.user.userid | Value copied directly  
Bruker | target.user.userid | Value from Bruker if User empty  
username | principal.user.userid | Value copied directly  
Virus_Malware_Name | security_result.threat_name | Value from Virus_Malware_Name if Spyware empty  
Spyware | security_result.threat_name | Value copied directly  
Unknown_Threat | security_result.threat_name | Value from Unknown_Threat if Virus_Malware_Name empty  
_hash | about.file.sha256 | Value copied directly  
_message | security_result.description | Value copied directly if not invalid  
_metadata.customer | security_result.detection_fields | Key as Customer, value copied  
_metadata.proxy.address | principal.hostname, principal.asset.hostname | Value copied directly  
_metadata.source.address | principal.hostname, principal.asset.hostname | Value copied directly  
_metadata.source.port | principal.port | Converted to integer  
_metadata.source.type | security_result.detection_fields | Key as Type, value copied  
_metadata.timestamp.producer_process | metadata.event_timestamp | Converted using date match yyyy-MM-ddTHH:mm:ss.SSSZ  
act | security_result.action_details | Value copied directly  
act | security_result.action | Set to ALLOW if act in [accept, notified] or outcome REDIRECTED_USER_MAY_PROCEED or categoryOutcome Success or cs2 Allow; BLOCK if act deny/blocked or outcome BLOCKED or categoryOutcome Failure or cs2 Denied; FAIL if outcome Failure  
action | security_result.action | Value copied directly  
app | app_protocol_src | Value copied directly  
app_protocol_src | network.application_protocol | Value from app_protocol_src after uppercase and mapping  
categoryOutcome | security_result.action | Part of conditional for action  
cs2 | security_result.action | Part of conditional for action  
cs5 | additional.fields | Key from cs5Label, value from cs5  
cs7 | additional.fields | Key from cs7Label, value from cs7  
destinationTranslatedAddress | target.nat_ip | Value copied directly  
destinationTranslatedPort | target.nat_port | Converted to integer  
deviceDirection | network.direction | Set to INBOUND if 0, OUTBOUND if 1  
device_event_class_id | metadata.product_event_type | Part of concatenation  
duid | target.user.userid | Value from temp_duid after grok  
dvcmac | about.mac | Value from dvcmac after formatting  
event_name | metadata.product_event_type | Part of concatenation  
event_name | metadata.event_type | Set to SCAN_UNCATEGORIZED if in [LogSpyware, LogPredictiveMachineLearning]  
fileHash | about.file.sha256 | Value copied directly if hash, else about.file.full_path  
Mottatt | metadata.collected_timestamp | Converted using date match yyyy-MM-ddTHH:mm:ss  
outcome | security_result.action | Part of conditional for action  
port | principal.port | Converted to integer  
protocol_number_src | network.ip_protocol | Value from protocol_number_src after mapping  
proto | protocol_number_src | Value copied directly  
severity | security_result.severity | Mapped based on value ranges  
shost | principal.hostname | Value copied directly if not IP  
act | security_result.action | Set based on conditional logic  
app_protocol_src | network.application_protocol | Mapped from app_protocol_src  
protocol_number_src | network.ip_protocol | Mapped from protocol_number_src  
Virus_Malware_Name | security_result.threat_name | Value from Virus_Malware_Name if  
`flexString2` | `event.idm.read_only_udm.network.email.subject` | Mapped from changelog  
`version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`device_product` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs1` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`cs4` | `event.idm.read_only_udm.metadata.url_back_to_product` | Mapped from changelog  
`suser` | `event.idm.read_only_udm.network.email.from` | Mapped from changelog  
`duser` | `event.idm.read_only_udm.network.email.to` | Mapped from changelog  
`fname` | `event.idm.read_only_udm.target.file.names` | Mapped from changelog  
`fileHash` | `event.idm.read_only_udm.target.file.md5` | Mapped from changelog  
`flexString1` | `event.idm.read_only_udm.about.file.sha256` | Mapped from changelog  
`observer_application` | `event.idm.read_only_udm.observer.application` | Mapped from changelog  
`syslog_severity_label` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`start` | `event.idm.read_only_udm.security_result.first_discovered_time` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-emps-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
