---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-email-security/
title: Collect Cisco Secure Email Gateway (formerly Email Security Appliance) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:56:52.739578+00:00
---

# Collect Cisco Secure Email Gateway (formerly Email Security Appliance) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-email-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Secure Email Gateway (formerly Email Security Appliance) logs

**Parser Version:** 12.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Secure Email Gateway (formerly known as Email Security Appliance) logs to Google Security Operations using Bindplane.

The parser extracts fields from Cisco Secure Email Gateway syslog, key-value, and JSON formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Cisco Secure Email Gateway web interface



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

  * Locate the configuration file on your operating system as follows:

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
            chronicle/chronicle_w_labels:
                compression: gzip
                creds_file_path: '/path/to/ingestion-authentication-file.json'
                customer_id: 'YOUR_CUSTOMER_ID'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: 'CISCO_EMAIL_SECURITY'
                raw_log_field: body
                ingestion_labels:
        
        service:
            pipelines:
                logs/source0__chronicle_w_labels-0:
                    receivers:
                        - tcplog
                    exporters:
                        - chronicle/chronicle_w_labels
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `tcplog`: Use `udplog` for UDP syslog or `tcplog` for TCP syslog
    * `0.0.0.0`: IP address to listen on (`0.0.0.0` to listen on all interfaces)
    * `514`: Port number to listen on (standard syslog port)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `YOUR_CUSTOMER_ID`: Customer ID from the Get customer ID section
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `log_type`: Log type exactly as it appears in Google SecOps (`CISCO_EMAIL_SECURITY`)



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
         




## Configure syslog forwarding on Cisco Secure Email Gateway

  1. Sign in to the **Cisco Secure Email Gateway** web interface.
  2. Go to **System Administration > Log Subscriptions**.
  3. Click **Add Log Subscription**.
  4. Provide the following configuration details: 
     * **Log Type** : Select the log type to forward (for example, **Consolidated Event Logs** , **Mail Logs** , **Text Mail Logs**).
     * **Name** : Enter a descriptive name (for example, `Google-SecOps-Syslog`).
     * **Retrieval Method** : Select **Syslog Push**.
     * **Hostname** : Enter the IP address of the Bindplane agent host.
     * **Protocol** : Select **TCP**.
     * **Port** : Enter `514`.
     * **Facility** : Select **LOG_MAIL** (or your preferred facility).
  5. Click **Submit**.
  6. Repeat steps 3-5 for each additional log type to forward. Recommended log types: 
     * **Consolidated Event Logs**
     * **Text Mail Logs**
     * **Anti-Spam Logs**
     * **Antivirus Logs**
     * **AMP Engine Logs**
     * **Content Filter Logs**
  7. Click **Commit Changes** to apply the configuration.
  8. Verify syslog messages are being sent by checking the Bindplane agent logs.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
acl_decision_tag | read_only_udm.security_result.detection_fields.value | Directly mapped if not empty, "-", or "NONE". Key is "ACL Decision Tag".  
access_or_decryption_policy_group | read_only_udm.security_result.detection_fields.value | Directly mapped if not empty, "-", or "NONE". Key is "AccessOrDecryptionPolicyGroup".  
act | read_only_udm.security_result.action_details | Directly mapped.  
authenticated_user | read_only_udm.principal.user.userid | Directly mapped if not empty, "-", or "NONE".  
cache_hierarchy_retrieval | read_only_udm.security_result.detection_fields.value | Directly mapped if not empty, "-", or "NONE". Key is "Cache Hierarchy Retrieval".  
cipher | read_only_udm.network.tls.cipher | Directly mapped.  
country | read_only_udm.principal.location.country_or_region | Directly mapped.  
data_security_policy_group | read_only_udm.security_result.detection_fields.value | Directly mapped if not empty, "-", or "NONE". Key is "DataSecurityPolicyGroup".  
description | read_only_udm.metadata.description | Directly mapped for syslog messages. For CEF messages, it becomes the overall product description. Various grok patterns extract specific descriptions based on the product_event. Some descriptions are modified by gsub to remove leading/trailing spaces and colons.  
deviceDirection | read_only_udm.network.direction | If '0', maps to 'INBOUND'. If '1', maps to 'OUTBOUND'. Used to determine which TLS cipher and protocol to map directly and which to map as labels.  
deviceExternalId | read_only_udm.principal.asset.asset_id | Mapped as "Device ID:".  
domain | read_only_udm.target.administrative_domain | Directly mapped from JSON logs.  
domain_age | read_only_udm.security_result.about.labels.value | Directly mapped. Key is "YoungestDomainAge".  
duser | read_only_udm.target.user.email_addresses, read_only_udm.network.email.to | If contains ";", split into multiple email addresses and map each to both UDM fields. Otherwise, directly map to both UDM fields if a valid email address. Also used to populate network_to if it's empty.  
dvc | read_only_udm.target.ip | Directly mapped.  
entries.collection_time.nanos, entries.collection_time.seconds | read_only_udm.metadata.event_timestamp.nanos, read_only_udm.metadata.event_timestamp.seconds | Used to construct the event timestamp.  
env-from | read_only_udm.additional.fields.value.string_value | Directly mapped. Key is "Env-From".  
ESAAttachmentDetails | read_only_udm.security_result.about.file.full_path, read_only_udm.security_result.about.file.sha256 | Parsed to extract file names and SHA256 hashes. Multiple files and hashes can be extracted.  
ESADCID | read_only_udm.security_result.about.labels.value | Directly mapped. Key is "ESADCID".  
ESAFriendlyFrom | read_only_udm.principal.user.user_display_name, read_only_udm.network.email.from | Parsed to extract the display name and email address.  
ESAHeloDomain | read_only_udm.intermediary.administrative_domain | Directly mapped.  
ESAHeloIP | read_only_udm.intermediary.ip | Directly mapped.  
ESAICID | read_only_udm.security_result.about.labels.value | Directly mapped. Key is "ESAICID".  
ESAMailFlowPolicy | read_only_udm.security_result.rule_name | Directly mapped.  
ESAMID | read_only_udm.security_result.about.labels.value | Directly mapped. Key is "ESAMID".  
ESAReplyTo | read_only_udm.network.email.reply_to | Directly mapped if a valid email address. Also used to populate network_to.  
ESASDRDomainAge | read_only_udm.security_result.about.labels.value | Directly mapped. Key is "ESASDRDomainAge".  
ESASenderGroup | read_only_udm.principal.group.group_display_name | Directly mapped.  
ESAStatus | read_only_udm.security_result.about.labels.value | Directly mapped. Key is "ESAStatus".  
ESATLSInCipher | read_only_udm.network.tls.cipher or read_only_udm.security_result.about.labels.value | Mapped directly to cipher if deviceDirection is '0'. Otherwise, mapped as a label with key "ESATLSInCipher".  
ESATLSInProtocol | read_only_udm.network.tls.version or read_only_udm.security_result.about.labels.value | TLS version extracted and mapped directly if deviceDirection is '0'. Otherwise, mapped as a label with key "ESATLSInProtocol".  
ESATLSOutCipher | read_only_udm.network.tls.cipher or read_only_udm.security_result.about.labels.value | Mapped directly to cipher if deviceDirection is '1'. Otherwise, mapped as a label with key "ESATLSOutCipher".  
ESATLSOutProtocol | read_only_udm.network.tls.version or read_only_udm.security_result.about.labels.value | TLS version extracted and mapped directly if deviceDirection is '1'. Otherwise, mapped as a label with key "ESATLSOutProtocol".  
ESAURLDetails | read_only_udm.target.url | Parsed to extract URLs. Only the first URL is mapped because the field is not repeated.  
external_dlp_policy_group | read_only_udm.security_result.detection_fields.value | Directly mapped if not empty, "-", or "NONE". Key is "ExternalDlpPolicyGroup".  
ExternalMsgID | read_only_udm.security_result.about.labels.value | Directly mapped after removing single quotes and angle brackets. Key is "ExternalMsgID".  
from | read_only_udm.network.email.from | Directly mapped if a valid email address. Also used to populate network_from.  
host.hostname | read_only_udm.principal.hostname or read_only_udm.intermediary.hostname | Mapped to principal hostname if host field is invalid. Also mapped to intermediary hostname.  
host.ip | read_only_udm.principal.ip or read_only_udm.intermediary.ip | Mapped to principal IP if ip field is not set in JSON logs. Also mapped to intermediary IP.  
hostname | read_only_udm.target.hostname | Directly mapped.  
http_method | read_only_udm.network.http.method | Directly mapped.  
http_response_code | read_only_udm.network.http.response_code | Directly mapped and converted to integer.  
identity_policy_group | read_only_udm.security_result.detection_fields.value | Directly mapped if not empty, "-", or "NONE". Key is "IdentityPolicyGroup".  
ip | read_only_udm.principal.ip | Directly mapped. Overwritten by source_ip if present.  
kv_msg | Various | Parsed using kv filter. Pre-processing includes replacing spaces before keys with "#" and swapping csLabel values.  
log_type | read_only_udm.metadata.log_type | Hardcoded to "CISCO_EMAIL_SECURITY".  
loglevel | read_only_udm.security_result.severity, read_only_udm.security_result.action | Used to determine severity and action. "Info", "", "Debug", "Trace" map to "INFORMATIONAL" and "ALLOW". "Warning" maps to "MEDIUM" and "ALLOW". "High" maps to "HIGH" and "BLOCK". "Critical" and "Alert" map to "CRITICAL", "BLOCK".  
mail_id | read_only_udm.network.email.mail_id | Directly mapped from JSON logs.  
mailto | read_only_udm.target.user.email_addresses, read_only_udm.network.email.to | Directly mapped to both UDM fields if a valid email address.  
MailPolicy | read_only_udm.security_result.about.labels.value | Directly mapped. Key is "MailPolicy".  
message | Various | Parsed as JSON if possible. Otherwise, processed as a syslog message.  
message_id | read_only_udm.network.email.mail_id | Directly mapped. Also used to populate network_data.  
msg | read_only_udm.network.email.subject | Directly mapped after UTF-8 decoding and removing carriage returns, newlines, and extra quotes. Also used to populate network_data.  
msg1 | Various | Parsed using kv filter. Used to extract Hostname, helo, env-from, and reply-to.  
outbound_malware_scanning_policy_group | read_only_udm.security_result.detection_fields.value | Directly mapped if not empty, "-", or "NONE". Key is "DataSecurityPolicyGroup".  
port | read_only_udm.target.port | Directly mapped and converted to integer.  
principalMail | read_only_udm.principal.user.email_addresses | Directly mapped.  
principalUrl | read_only_udm.principal.url | Directly mapped.  
product_event | read_only_udm.metadata.product_event_type | Directly mapped. Used to determine which grok patterns to apply. Leading "%" characters are removed. "amp" is replaced with "SIEM_AMPenginelogs".  
product_version | read_only_udm.metadata.product_version | Directly mapped.  
protocol | read_only_udm.network.tls.version | Directly mapped.  
received_bytes | read_only_udm.network.received_bytes | Directly mapped and converted to unsigned integer.  
reply-to | read_only_udm.additional.fields.value.string_value | Directly mapped. Key is "Reply-To".  
reputation | read_only_udm.security_result.confidence_details | Directly mapped.  
request_method_uri | read_only_udm.target.url | Directly mapped.  
result_code | read_only_udm.security_result.detection_fields.value | Directly mapped. Key is "Result Code".  
routing_policy_group | read_only_udm.security_result.detection_fields.value | Directly mapped if not empty, "-", or "NONE". Key is "RoutingPolicyGroup".  
rule | read_only_udm.security_result.detection_fields.value | Directly mapped. Key is "Matched Condition".  
SDRThreatCategory | read_only_udm.security_result.threat_name | Directly mapped if not empty or "N/A".  
SenderCountry | read_only_udm.principal.location.country_or_region | Directly mapped.  
senderGroup | read_only_udm.principal.group.group_display_name | Directly mapped.  
security_description | read_only_udm.security_result.description | Directly mapped.  
security_email | read_only_udm.security_result.about.email or read_only_udm.principal.hostname | Mapped to email if a valid email address. Otherwise, mapped to hostname after extracting with grok.  
source | read_only_udm.network.ip_protocol | If contains "tcp", maps to "TCP".  
sourceAddress | read_only_udm.principal.ip | Directly mapped.  
sourceHostName | read_only_udm.principal.administrative_domain | Directly mapped if not "unknown".  
source_ip | read_only_udm.principal.ip | Directly mapped. Overwrites ip if present.  
Subject | read_only_udm.network.email.subject | Directly mapped after removing trailing periods. Also used to populate network_data.  
suser | read_only_udm.principal.user.email_addresses, read_only_udm.network.email.bounce_address | Directly mapped to both UDM fields if a valid email address.  
target_ip | read_only_udm.target.ip | Directly mapped.  
to | read_only_udm.network.email.to | Directly mapped if a valid email address. Also used to populate network_to.  
total_bytes | read_only_udm.network.sent_bytes | Directly mapped and converted to unsigned integer.  
trackerHeader | read_only_udm.additional.fields.value.string_value | Directly mapped. Key is "Tracker Header".  
ts, ts1, year | read_only_udm.metadata.event_timestamp.seconds | Used to construct the event timestamp. ts1 and year are combined if ts1 is present. Various formats are supported, with and without the year. If the year is not present, the current year is used. Hardcoded to "Cisco". Hardcoded to "Cisco Email Security". Defaults to "ALLOW". Set to "BLOCK" based on loglevel or description. Defaults to "INBOUND" if application_protocol is present. Set based on deviceDirection for CEF messages. Determined based on a combination of fields including network_from, network_to, target_ip, ip, description, event_type, principal_host, Hostname, user_id, and sourceAddress. Defaults to "GENERIC_EVENT". Set to "SMTP" if application_protocol is "SMTP" or "smtp", or if target_ip and ip are present. Set to "AUTHTYPE_UNSPECIFIED" if login_status and user_id are present in sshd logs. Set to true if loglevel is "Critical" or "Alert".  
`deviceInboundInterface` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dvc` | `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
`ESAHeloIP` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`startTime` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`endTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`deviceDirection` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ESAOFVerdict` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ESADLPVerdict` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ESAMFVerdict` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ESATLSOutConnStatus` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`host` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`host` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`ts_year` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`start` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`src` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`src` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`shost` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`shost` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`ESAMailFlowPolicy` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`ESAAMPVerdict` | `event.idm.read_only_udm.metadata.additional.fields` | Mapped from changelog  
`ESAASVerdict` | `event.idm.read_only_udm.metadata.additional.fields` | Mapped from changelog  
`ESAAVVerdict` | `event.idm.read_only_udm.metadata.additional.fields` | Mapped from changelog  
`ESACFVerdict` | `event.idm.read_only_udm.metadata.additional.fields` | Mapped from changelog  
`ESAGMVerdict` | `event.idm.read_only_udm.metadata.additional.fields` | Mapped from changelog  
`deviceOutboundInterface` | `event.idm.read_only_udm.metadata.additional.fields` | Mapped from changelog  
`end` | `event.idm.read_only_udm.metadata.additional.fields` | Mapped from changelog  
`ESAMsgSize` | `event.idm.read_only_udm.metadata.additional.fields` | Mapped from changelog  
`cfp1Label` | `event.idm.read_only_udm.metadata.additional.fields` | Mapped from changelog  
`cfp1` | `event.idm.read_only_udm.metadata.additional.fields` | Mapped from changelog  
`urls" and "WbrsScore` | `security_result.detection_fields` | Mapped from changelog  
`message_id2` | `network.email.mail_id` | Mapped from changelog  
`injection_connection_id` | `network.session_id` | Mapped from changelog  
`address_clean` | `network.email.to` | Mapped from changelog  
`receiver` | `network.email.to` | Mapped from changelog  
`inner_message` | `metadata.description` | Mapped from changelog  
`host_msg` | `intermediary.ip` | Mapped from changelog  
`host_msg` | `principal.hostname` | Mapped from changelog  
`attack` | `security_result.category_details` | Mapped from changelog  
`from_user` | `principal.user.user_display_name` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-email-security-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
