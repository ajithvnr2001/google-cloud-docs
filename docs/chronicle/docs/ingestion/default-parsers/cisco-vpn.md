---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-vpn/
title: Collect Cisco VPN logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:22:26.635167+00:00
---

# Collect Cisco VPN logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-vpn/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco VPN logs

**Parser Version:** 22.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco ASA VPN logs to Google Security Operations using the Bindplane agent.

The parser extracts fields from Cisco ASA VPN syslog messages using grok patterns, handling both standard syslog formats and alternative message structures. It maps extracted fields to the Unified Data Model (UDM) and categorizes events based on ASA event IDs.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Cisco ASA
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Cisco ASA



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

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

  * **Linux:**
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/cisco_vpn:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: CISCO_VPN
                raw_log_field: body
        
        service:
            pipelines:
                logs/cisco_vpn_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/cisco_vpn
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list



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
             




## Configure syslog for Cisco ASA VPN

  1. Open the **Cisco ASDM**.
  2. Go to **Configuration > Features > Properties > Logging > Logging Setup**.
  3. Select the **Enable logging** checkbox to enable syslog.
  4. Select **Syslog Servers** in **Logging** and click **Add**.
  5. Enter the following configuration details in the **Add Syslog Server** window: 
     * **Interface** : Select the interface for outbound communication.
     * **IP Address** : Enter the Bindplane agent IP address.
     * **Protocol** : Select **UDP**.
     * **Port** : Enter the Bindplane agent port number.
     * Click **OK**.
  6. Select **Logging Filters** in the **logging** section.
  7. Select **Syslog Servers** and click **Edit**.
  8. Select **Informational** from the list as the **Filter on severity**.
  9. Click **OK**.
  10. Click **Apply**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`accesslist` | `target.resource.name` | Extracted from `message_info` when `eventtype` is "ASA-4-106103". Represents the name of the access list.  
`action` | `security_result.action` | Derived by the parser based on keywords in the log message (e.g., "Deny", "Reject", "Allow", "Accept"). Maps to ALLOW or BLOCK.  
`action` | `security_result.action_details` | The raw string value of the action taken (e.g., "permitted", "denied", "disconnected").  
`app_name` | `principal.application` | The name of the application used by the principal (e.g., "CLI"). Extracted from `message_details` for event ID 111008, 111009, and 111010.  
`assigned_ipv4` | N/A | Although parsed, this field is not mapped to the IDM object in the UDM.  
`assigned_ipv6` | N/A | Although parsed, this field is not mapped to the IDM object in the UDM.  
`bytes_rcv` | `network.received_bytes` | The number of bytes received in the session. Extracted from `log_mssg` for event ID 113019.  
`bytes_sent` | `network.sent_bytes` | The number of bytes sent in the session. Extracted from `log_mssg` for event ID 113019.  
`cipher` | `network.tls.cipher` | The cipher used for the SSL session. Extracted from `message_info` for eventtype 725012.  
`cisco_message_number` | `security_result.rule_name` | The Cisco message number, extracted from the `eventtype` field.  
`cisco_severity` | `security_result.severity_details` | The raw Cisco severity level, extracted from the `eventtype` field.  
`command` | N/A | Although parsed, this field is not mapped to the IDM object in the UDM.  
`cumulative_total_count.key` | `security_result.outcomes.key` | The key "cumulative_total_count" is added to the `security_result.outcomes` array.  
`cumulative_total_count.value` | `security_result.outcomes.value` | The value of the cumulative total count, extracted from `message_info`.  
`current_average_rate.key` | `security_result.outcomes.key` | The key "current_average_rate" is added to the `security_result.outcomes` array.  
`current_average_rate.value` | `security_result.outcomes.value` | The value of the current average rate, extracted from `message_info`.  
`current_burst_rate.key` | `security_result.outcomes.key` | The key "current_burst_rate" is added to the `security_result.outcomes` array.  
`current_burst_rate.value` | `security_result.outcomes.value` | The value of the current burst rate, extracted from `message_info`.  
`desc` | `metadata.description` | Description of the event, extracted from the log message. Used when a more specific description is not available.  
`description` | `metadata.description` | A more detailed description of the event, extracted from the log message when available.  
`destination_ip` | `target.ip`, `target.asset.ip` | Destination IP address, extracted from various log message formats.  
`destination_ip_port` | `target.port` or `network.application_protocol` | Destination port, extracted from various log message formats. If the extracted value is not a number, it's treated as the application protocol.  
`dst_email` | `target.user.email_addresses` or `target.user.userid` | Destination email address or userid, extracted from `message_info`. If the value matches an email format, it's added to `email_addresses`; otherwise, it's used as `userid`.  
`dst_host` | `target.hostname` | Destination hostname, extracted from `message_info`.  
`dst_ip` | `target.ip`, `target.asset.ip` | Destination IP address, extracted from the main grok pattern or other specific patterns.  
`dst_port` | `target.port` | Destination port, extracted from the main grok pattern or other specific patterns.  
`duration` | `network.session_duration` | Duration of the session, extracted from `message_details` and converted to seconds.  
`event_date` | `@timestamp` | The date and time of the event, constructed from various timestamp fields in the raw log and parsed using the `date` filter.  
`event_id` | `metadata.product_event_type` (part of) | Used in combination with `event_severity` to form the `metadata.product_event_type` field.  
`event_name` | `metadata.product_event_type` (part of) | Used in combination with `event_severity` and `event_type` to form the `metadata.product_event_type` field when available.  
`event_severity` | `metadata.product_event_type` (part of), `security_result.severity`, `is_alert`, `is_significant` | Used in combination with `event_id` or `event_name` and `event_type` to form the `metadata.product_event_type` field. Also used to derive the `security_result.severity`, `is_alert`, and `is_significant` fields.  
`event_type` | `metadata.product_event_type` (part of) | Used in combination with `event_name` and `event_severity` to form the `metadata.product_event_type` field when available.  
`eventtype` | `metadata.product_event_type`, `security_result.rule_name`, `security_result.severity_details`, `security_result.severity` | The event type string, used to derive the `metadata.product_event_type`, `security_result.rule_name`, `security_result.severity_details`, and `security_result.severity` fields.  
`fragment_id` | `security_result.about.resource.id` | ID of the IP fragment, extracted from `message_details` for event ID 209005.  
`group` | `principal.group.group_display_name`, `principal.user.group_identifiers`, `target.user.group_identifiers` | Group name, extracted from various log message formats.  
`group_name` | `principal.group.group_display_name` | Group name extracted from the `group` field when it's a hostname.  
`has_principal_ip` | N/A | Internal variable used for logic, not mapped to UDM.  
`has_target_ip` | N/A | Internal variable used for logic, not mapped to UDM.  
`hostname` | `principal.hostname`, `principal.asset.hostname` | Hostname of the principal, extracted from various log message formats.  
`hostname2` | `principal.hostname`, `principal.asset.hostname` | Hostname of the principal, extracted as a fallback when `hostname` is not available.  
`icmp_code` | N/A | Although parsed, this field is not mapped to the IDM object in the UDM.  
`icmp_dst_ip` | `target.ip`, `target.asset.ip` | Destination IP address from an ICMP error message.  
`icmp_id` | N/A | Although parsed, this field is not mapped to the IDM object in the UDM.  
`icmp_src_ip` | `principal.ip`, `principal.asset.ip` | Source IP address from an ICMP error message.  
`icmp_type` | N/A | Although parsed, this field is not mapped to the IDM object in the UDM.  
`intermediary_ip` | `principal.ip`, `principal.asset.ip` | Intermediary IP address, extracted from `message_info` for event ID 111010.  
`invalid_ip` | N/A | Internal variable used for logic, not mapped to UDM.  
`ip_1` | `principal.ip`, `principal.asset.ip` | Source IP address extracted as a fallback when source and destination IPs are the same.  
`ip_2` | `target.ip`, `target.asset.ip` | Destination IP address extracted as a fallback when source and destination IPs are the same.  
`ipprotocol` | `network.ip_protocol` | IP protocol, extracted from various log message formats and converted to uppercase.  
`issuer` | `network.tls.client.certificate.issuer` | Issuer of the peer certificate, extracted from `message_details` for event ID 717037.  
`local_proxy_ip` | `intermediary.ip` | Local proxy IP address, extracted from `message_details` for event ID 713041.  
`log_mssg` | `security_result.description`, `sr.action` | Used to populate the `security_result.description` field and to extract authentication actions.  
`login` | `security_result.summary` | Login status, extracted from `message_info`.  
`max_configured_rate.key` | `security_result.outcomes.key` | The key "max_configured_rate" is added to the `security_result.outcomes` array.  
`max_configured_rate.value` | `security_result.outcomes.value` | The value of the max configured rate, extracted from `message_info`.  
`message_details` | Various fields | The main part of the log message, containing details about the event. Parsed using various grok patterns depending on the event ID.  
`message_info` | `metadata.description` | Used to populate the `metadata.description` field when available.  
`observer` | `observer.hostname` or `observer.ip` | Observer hostname or IP address, extracted from the log message.  
`observer_ip` | `observer.ip` | Observer IP address, extracted from the `observer` field.  
`peer_type` | N/A | Although parsed, this field is not mapped to the IDM object in the UDM.  
`policy` | `target.resource.name` | Policy name, extracted from `message_details` for event ID 113003.  
`policy_name` | `target.resource.name` | Policy name, extracted from `message_details` for event IDs 113009 and 113011.  
`principal_ip` | `principal.ip`, `principal.asset.ip` | Principal IP address, extracted from `message_details` for event ID 113009.  
`privilege_level_from` | N/A | Although parsed, this field is not mapped to the IDM object in the UDM.  
`privilege_level_to` | N/A | Although parsed, this field is not mapped to the IDM object in the UDM.  
`process` | `principal.process.command_line` | Process name, extracted from `message_details` for event ID 711004.  
`protocol` | `network.ip_protocol` or `network.application_protocol` | Protocol used in the event, extracted from various log message formats. If the protocol is a standard IP protocol (ICMP, TCP, UDP, ESP), it's mapped to `network.ip_protocol`; otherwise, it's mapped to `network.application_protocol`.  
`reason` | `security_result.description` | Reason for the event, extracted from `message_details` for event ID 113016.  
`remote_proxy_ip` | `intermediary.ip` | Remote proxy IP address, extracted from `message_details` for event ID 713041.  
`retrieved_file` | `target.file.full_path` | Path to the retrieved file, extracted from `message_info`.  
`security_action` | `security_result.action` | Security action, derived by the parser based on the event context.  
`security_category` | `security_result.category` | Security category, derived by the parser based on the event context.  
`security_result.description` | `security_result.description` | Description of the security result, extracted or derived from the log message.  
`security_result.severity` | `security_result.severity` | Severity of the security result, derived from the `event_severity` field.  
`security_result.summary` | `security_result.summary` | Summary of the security result, extracted or derived from the log message.  
`sent_bytes` | `network.sent_bytes` | Number of bytes sent, extracted from `message_info`.  
`ses_id` | `network.session_id` | Session ID, extracted from `message_info`.  
`session_id` | `network.session_id` | Session ID, extracted from `message_info`.  
`sess_type` | `principal.hostname`, `principal.asset.hostname` | Session type, extracted from `log_mssg` and used as hostname when `hostname` is not available.  
`source_ip` | `principal.ip`, `principal.asset.ip` | Source IP address, extracted from various log message formats.  
`source_ip_port` | `principal.port` | Source port, extracted from various log message formats.  
`src_email` | `principal.user.email_addresses` or `principal.user.userid` | Source email address or userid, extracted from `message_info`. If the value matches an email format, it's added to `email_addresses`; otherwise, it's used as `userid`.  
`src_ip` | `principal.ip`, `principal.asset.ip` | Source IP address, extracted from the main grok pattern or other specific patterns.  
`src_port` | `principal.port` | Source port, extracted from the main grok pattern or other specific patterns.  
`src_user` | `principal.user.user_display_name` | Source user display name, extracted from `message_details` for event IDs 713049 and 713120.  
`subject` | `network.tls.client.certificate.subject` | Subject of the peer certificate, extracted from `message_details` for event ID 717037.  
`summary` | `security_result.summary` | Summary of the event, extracted from `message_details` for event ID 113016.  
`target_host` | `target.hostname` | Target hostname, extracted from `message_details` for event ID 113004.  
`target_ip` | `target.ip`, `target.asset.ip` | Target IP address, extracted from `message_details` for event ID 113004.  
`target_user` | `target.user.userid` | Target user ID, extracted from `message_details` for event ID 113003.  
`task_duration` | N/A | Although parsed, this field is not mapped to the IDM object in the UDM.  
`tcp_dst_ip` | `target.ip`, `target.asset.ip` | Destination IP address from the original TCP payload of an ICMP error message.  
`tcp_dst_port` | N/A | Although parsed, this field is not mapped to the IDM object in the UDM.  
`tcp_src_ip` | `principal.ip`, `principal.asset.ip` | Source IP address from the original TCP payload of an ICMP error message.  
`tcp_src_port` | N/A | Although parsed, this field is not mapped to the IDM object in the UDM.  
`threshold` | N/A | Although parsed, this field is not mapped to the IDM object in the UDM.  
`tls_version` | `network.tls.version` | TLS version, extracted from `message_details` for event ID 725002.  
`ts` | `@timestamp` | Timestamp of the event, parsed using the `date` filter.  
`ts_day` | `@timestamp` (part of) | Day of the month from the timestamp, used to construct the `@timestamp` field.  
`ts_month` | `@timestamp` (part of) | Month from the timestamp, used to construct the `@timestamp` field.  
`ts_time` | `@timestamp` (part of) | Time from the timestamp, used to construct the `@timestamp` field.  
`ts_year` | `@timestamp` (part of) | Year from the timestamp, used to construct the `@timestamp` field.  
`tunnel_type` | N/A | Although parsed, this field is not mapped to the IDM object in the UDM.  
`user` | `principal.user.userid`, `target.user.userid` | User ID, extracted from various log message formats.  
`user_agent` | `network.http.user_agent` | User agent string, extracted from `message_details` for event ID 722055.  
`user_attr.key` | `principal.user.attribute.labels.key` | Key of a user attribute, extracted from `message_details` for event IDs 734003 and 734001.  
`user_attr.value` | `principal.user.attribute.labels.value` | Value of a user attribute, extracted from `message_details` for event IDs 734003 and 734001.  
`userid` | `principal.user.userid` | User ID, extracted from `message_details` for event ID 106103.  
`username` | `principal.user.userid` | Username, extracted from `message_details` for event IDs 111008, 111009, 111010, and 113008.  
N/A | `metadata.vendor_name` | Hardcoded to "CISCO".  
N/A | `metadata.product_name` | Hardcoded to "ASA VPN" or "VPN".  
N/A | `metadata.event_type` | Determined by parser logic based on the presence of certain fields and event IDs. Can be GENERIC_EVENT, NETWORK_CONNECTION, STATUS_UPDATE, NETWORK_FTP, USER_LOGIN, USER_LOGOUT, NETWORK_UNCATEGORIZED, USER_UNCATEGORIZED, NETWORK_FLOW.  
N/A | `metadata.log_type` | Hardcoded to "CISCO_VPN".  
N/A | `metadata.event_timestamp` | Copied from the parsed `@timestamp` field.  
N/A | `extensions.auth.type` | Set to "VPN", "AUTHTYPE_UNSPECIFIED", or "MACHINE" depending on the event context.  
N/A | `security_result.about.resource.type` | Set to "PACKET FRAGMENT" for event ID 209005.  
N/A | `is_alert` | Set to true for high-severity events (event_severity 0 or 1).  
N/A | `is_significant` | Set to true for high-severity events (event_severity 0 or 1).  
`puser_id` | `principal.user.userid` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-vpn-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
