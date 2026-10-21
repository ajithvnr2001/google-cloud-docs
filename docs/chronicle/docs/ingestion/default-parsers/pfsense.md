---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pfsense/
title: Collect pfSense logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:53:15.525785+00:00
---

# Collect pfSense logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pfsense/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect pfSense logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest pfSense logs to Google Security Operations using Bindplane.

pfSense is an open-source firewall and router software distribution based on FreeBSD. It provides stateful packet filtering, VPN, traffic shaping, NAT, DHCP server, DNS forwarder, and intrusion detection capabilities, all managed through a web-based interface. The parser extracts fields from pfSense syslog formatted logs. It uses grok to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the pfSense web interface



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

## Configure Bindplane agent to ingest syslog and send to Google SecOps

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
            chronicle/chronicle_w_labels:
                compression: gzip
                creds_file_path: '/path/to/ingestion-authentication-file.json'
                customer_id: 'YOUR_CUSTOMER_ID'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: 'PFSENSE'
                raw_log_field: body
                ingestion_labels:
        
        service:
            pipelines:
                logs/source0__chronicle_w_labels-0:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/chronicle_w_labels
        




### Configuration parameters

  * Replace the following placeholders:

    * **Receiver configuration:**

      * `udplog`: Use `udplog` for UDP syslog or `tcplog` for TCP syslog
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
      * `log_type`: Log type exactly as it appears in Chronicle (`PFSENSE`)



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

      1. Press `Win+R`, type `services.msc`, and press **Enter**.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.

      4. Verify the service is running:
             
             sc query observiq-otel-collector
             

      5. Check logs for errors:
             
             type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
             




## Configure Syslog forwarding on pfSense

pfSense runs on FreeBSD and provides a web-based interface for all configuration tasks, including remote syslog forwarding.

  1. Sign in to the **pfSense** web interface.
  2. Go to **Status > System Logs > Settings**.
  3. Go to the **Remote Logging Options** section.
  4. Select **Enable Remote Logging**.
  5. Provide the following configuration details: 
     * **Source Address** : Select **Any** (or a specific interface).
     * **IP Protocol** : Select **IPv4**.
     * **Remote log servers** : Enter `BINDPLANE_IP:514` in the first available field. Replace `BINDPLANE_IP` with the IP address of the Bindplane agent host.
  6. In the **Remote Syslog Contents** section, select the log categories to forward: 
     * **System Events**
     * **Firewall Events**
     * **DNS Events** (Resolver/unbound, Forwarder/dnsmasq)
     * **DHCP Events** (DHCP service)
     * **PPP Events**
     * **Authentication Events** (Portal Auth, RADIUS)
     * **VPN Events** (IPsec, OpenVPN, L2TP)
     * **Gateway Events** (Gateway monitor)
     * **Routing Events** (Routing daemon)
     * **NTP Events**
     * **Packages** (installed packages)
  7. Click **Save**.
  8. Verify syslog messages are being sent by checking the Bindplane agent logs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
application | principal.application | The value is extracted from the log message using grok patterns. For syslog messages, the application name is typically found after the hostname and timestamp.  
command | principal.process.command_line | Extracted from the description field when the log indicates a command execution.  
description | metadata.description | The description field is mapped to the UDM metadata description, except for syslog-ng application logs where it's mapped to metadata.description. For DHCP events, the dhcp_type is prepended to the description.  
dhcp_type | metadata.product_event_type | The DHCP message type (e.g., DHCPDISCOVER, DHCPOFFER) is extracted and mapped.  
host | intermediary.hostname OR intermediary.ip | If the host value is a valid IP address, it's mapped to intermediary.ip. Otherwise, it's mapped to intermediary.hostname.  
host | principal.hostname, principal.asset.hostname | When no principal IP is present, the host is treated as the principal hostname.  
mac | principal.mac, network.dhcp.chaddr | The MAC address associated with a DHCP request is extracted and mapped.  
src_ip | principal.ip, principal.asset.ip | Extracted from specific log formats using a grok pattern.  
src_mac | principal.mac | Extracted from specific log formats using a grok pattern.  
dst_mac | target.mac | Extracted from specific log formats using a grok pattern.  
timestamp | metadata.event_timestamp | The timestamp is extracted from the log message and converted to a UDM timestamp format. The timezone information (tz) is appended to the timestamp before conversion if available.  
timestamp_no_year | metadata.event_timestamp | If a timestamp without a year is present, it's parsed, and the current year is added during the parsing process.  
user | principal.user.userid | The username associated with an event is extracted and mapped.  
column1 | security_result.rule_id | Mapped from the first CSV column if the description is in CSV format.  
column6 | security_result.rule_type | Mapped from the sixth CSV column if the description is in CSV format.  
column7 | security_result.action | Mapped from the seventh CSV column if the description is in CSV format. Converted to "BLOCK" or "ALLOW".  
column8 | network.direction | Mapped from the eighth CSV column if the description is in CSV format. Converted to "INBOUND" or "OUTBOUND".  
column13 | network.ip_protocol (if UDP or ICMP) | Mapped from the thirteenth CSV column if the description is in CSV format and the protocol is UDP or ICMP. For TCP/UDP events, it's used to create an additional field with key "Id".  
column16 | principal.ip, principal.asset.ip (if IPv6 and column9 is 6) | Mapped from the sixteenth CSV column if the description is in CSV format and column9 is 6. For TCP/UDP events, it's used for protocol identification if column9 is 4.  
column17 | target.ip, target.asset.ip (if IPv6 and not ip_failure) | Mapped from the seventeenth CSV column if the description is in CSV format, column9 is 6, and the value is a valid IP. For TCP/UDP events, it's used for protocol identification.  
column18 | principal.port (if UDP) | Mapped from the eighteenth CSV column if the description is in CSV format and the protocol is UDP. For TCP/UDP events, it's mapped to network.received_bytes.  
column19 | target.port (if UDP) | Mapped from the nineteenth CSV column if the description is in CSV format and the protocol is UDP. For DHCP events, it's mapped to network.dhcp.yiaddr. For other events, it's mapped to principal.ip, principal.asset.ip.  
column20 | additional.fields (key: "data_length") (if UDP) | Mapped from the twentieth CSV column if the description is in CSV format and the protocol is UDP. For other events, it's mapped to target.ip, target.asset.ip.  
column21 | principal.port (if TCP/UDP) | Mapped from the twenty-first CSV column if the description is in CSV format and the protocol is TCP or UDP.  
column22 | target.port (if TCP/UDP) | Mapped from the twenty-second CSV column if the description is in CSV format and the protocol is TCP or UDP.  
column23 | additional.fields (key: "data_length") (if TCP/UDP) | Mapped from the twenty-third CSV column if the description is in CSV format and the protocol is TCP or UDP.  
column24 | additional.fields (key: "tcp_flags") (if TCP) | Mapped from the twenty-fourth CSV column if the description is in CSV format and the protocol is TCP.  
column25 | additional.fields (key: "sequence_number") (if TCP/UDP) | Mapped from the twenty-fifth CSV column if the description is in CSV format and the protocol is TCP or UDP.  
column29 | additional.fields (key: "tcp_options") (if TCP) | Mapped from the twenty-ninth CSV column if the description is in CSV format and the protocol is TCP.  
compression_algo | additional.fields (key: "Compression Algorithm") | Extracted from the description field and added as an additional field.  
desc | metadata.description | Extracted from the message field and used as the description.  
principal_ip | principal.ip, principal.asset.ip | Extracted from the description field and represents the principal IP address.  
principal_username | principal.user.userid | Extracted from the description field and represents the principal username.  
status | security_result.detection_fields (key: "status") | Extracted from the description field and added as a detection field within the security result.  
target_host | target.hostname, target.asset.hostname | Extracted from the description field and represents the target hostname.  
src_port | principal.port | Extracted from the description field and represents the source port. Determined based on various log fields and parser logic. Can be NETWORK_CONNECTION, NETWORK_DHCP, STATUS_UPDATE, or GENERIC_EVENT. Hardcoded to "PFSENSE". Hardcoded to "PFSENSE". Hardcoded to "PFSENSE". Set to "DHCP" for DHCP events. Set to "BOOTREQUEST" for DHCPDISCOVER and DHCPREQUEST, and "BOOTREPLY" for DHCPOFFER and DHCPACK. Set to "DISCOVER", "REQUEST", "OFFER", or "ACK" based on the dhcp_type field.  
`pid` | `intermediary.process.pid` | Mapped from changelog  
`application` | `intermediary.application` | Mapped from changelog  
`ipv4" and "ipv6` | `principal.ip` | Mapped from changelog  
`security_result.category` | `AUTH_VIOLATION` | Mapped from changelog  
`method` | `network.http.method` | Mapped from changelog  
`referer` | `network.http.referral_url` | Mapped from changelog  
`response_code` | `network.http.response_code` | Mapped from changelog  
`user_agent` | `network.http.user_agent` | Mapped from changelog  
`sent_bytes` | `network.sent_bytes` | Mapped from changelog  
`url` | `target.url` | Mapped from changelog  
`http_version` | `additional.fields` | Mapped from changelog  
`column19" which is "source-address` | `network.dhcp.yiaddr` | Mapped from changelog  
`column17" which is "destination-address` | `target.ip` | Mapped from changelog  
`column16" which is "source-address` | `principal.ip` | Mapped from changelog  
`column12" which is "hop_limit` | `additional.fields` | Mapped from changelog  
`column13" which is "ip_protocol` | `network.ip_protocol` | Mapped from changelog  
`ttl` | `additional.fields` | Mapped from changelog  
`Offset` | `additional.fields` | Mapped from changelog  
`Data length` | `additional.fields` | Mapped from changelog  
`Length` | `additional.fields` | Mapped from changelog  
`Sequence-number` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pfsense-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
