---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-firepower-firewall/
title: Collect Cisco Firepower NGFW logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:08.235299+00:00
---

# Collect Cisco Firepower NGFW logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-firepower-firewall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Firepower NGFW logs

**Parser Version:** 31.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Firepower NGFW logs to Google Security Operations using the Bindplane agent.

Cisco Firepower Next-Generation Firewall generates logs for network connections, intrusion events, file and malware events, and security intelligence. The parser extracts fields using grok patterns and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Cisco Firepower device
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to a Cisco Firepower device



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**
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
            chronicle/cisco_firepower_firewall:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: CISCO_FIREPOWER_FIREWALL
                raw_log_field: body
        
        service:
            pipelines:
                logs/cisco_firepower_firewall_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/cisco_firepower_firewall
        




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
             




## Configure syslog on Cisco Firepower device

  1. Sign in to the Firepower Device Manager web UI.
  2. Go to **System Settings > Logging Settings**.
  3. Switch to **Enable** the **Data Logging** toggle.
  4. Click the **+** icon under **Syslog Servers**.
  5. Click **Create new Syslog Server** (alternatively, create the Syslog Server in **Objects > Syslog Servers**).
  6. Provide the following configuration details: 
     * **IP Address** : Enter the Bindplane agent IP address.
     * **Protocol Type** : Select **UDP**.
     * **Port Number** : Enter the Bindplane agent port number.
     * Select **Data Interface** or **Management Interface**.
  7. Click **OK**.
  8. Select the newly created **Syslog server** from the list and click **OK**.
  9. Click **Severity level for filtering all events** and select **Informational** logging level from the list.
  10. Click **Save**.
  11. Click the **Deploy New Settings icon > Deploy Now**.
  12. Click **Policies** at the top of the screen.
  13. Hold the pointer over the side of the **ACP rule** and click **Edit**.
  14. Go to the **Logging** tab.
  15. Select **At End of Connection**.
  16. Open the **Select a Syslog Alert Configuration** list.
  17. Select the Bindplane **Syslog Server**.
  18. Click **OK**.
  19. Click the **Deploy New Settings icon > Deploy Now**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`target_user` | `event.idm.read_only_udm.target.userid` | Mapped from changelog  
`device_ids` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`src_ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`tar_ip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`tar_ip` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`src_nat_ip` | `event.idm.read_only_udm.principal.nat_ip` | Mapped from changelog  
`src_nat_port` | `event.idm.read_only_udm.principal.nat_port` | Mapped from changelog  
`dst_nat_ip` | `event.idm.read_only_udm.target.nat_ip` | Mapped from changelog  
`dst_nat_port` | `event.idm.read_only_udm.target.nat_port` | Mapped from changelog  
`interface` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dest_interface` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`session_id` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`protocol` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`int_IP1` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`int_IP2` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`int_IP3` | `event.idm.read_only_udm.target.nat_ip` | Mapped from changelog  
`crypto_map` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`int_IP1` | `event.idm.read_only_udm.target.nat_ip` | Mapped from changelog  
`int_IP3` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`appname` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`facility` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`proc_id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`message` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`priority` | `event.idm.read_only_udm.security_result.priority_details` | Mapped from changelog  
`process_name` | `event.idm.read_only_udm.principal.process.file.names` | Mapped from changelog  
`process_id` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`AccessControlRuleReason` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`Client` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`IPSCount` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ConnectionDuration` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ReferencedHost` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`UserAgent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`UserAgent` | `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
`event_id` | `additional.fields` | Mapped from changelog  
`path` | `principal.process.file.full_path` | Mapped from changelog  
`event_name` | `metadata.product_event_type` | Mapped from changelog  
`description` | `metadata.description` | Mapped from changelog  
`host` | `principal.hostname` | Mapped from changelog  
`srcuser` | `principal.user.userid` | Mapped from changelog  
`src_ip` | `principal.ip` | Mapped from changelog  
`src_port` | `principal.port` | Mapped from changelog  
`username2` | `target.user.userid` | Mapped from changelog  
`pwd` | `target.file.full_path` | Mapped from changelog  
`command` | `target.process.command_line` | Mapped from changelog  
`username` | `principal.user.userid` | Mapped from changelog  
`action` | `metadata.ingestion_labels` | Mapped from changelog  
`bytes_transferred` | `network.sent_bytes` | Mapped from changelog  
`HTTP_Hostname` | `target.resource.attribute.labels` | Mapped from changelog  
`HTTP_URI` | `target.resource.attribute.labels` | Mapped from changelog  
`InlineResult` | `security_result.action_details` | Mapped from changelog  
`user_id_field` | `principal.user.userid` | Mapped from changelog  
`http_method` | `network.http.method` | Mapped from changelog  
`HTTPReferer` | `network.http.referral_url` | Mapped from changelog  
`HTTPResponse` | `network.http.response_code` | Mapped from changelog  
`event_description` | `metadata.description` | Mapped from changelog  
`event_summary` | `security_result.summary` | Mapped from changelog  
`userId` | `principal.user.userid` | Mapped from changelog  
`sourceIpAddress` | `principal.ip` | Mapped from changelog  
`sourcePortOrIcmpType` | `principal.port` | Mapped from changelog  
`@computed.sensor` | `principal.hostname` | Mapped from changelog  
`@computed.user` | `principal.user.user_display_name` | Mapped from changelog  
`@computed.clientApplication` | `principal.application` | Mapped from changelog  
`@computed.ingressInterface` | `principal.asset.attribute.labels` | Mapped from changelog  
`@computed.sourceIpCountry` | `principal.location.country_or_region` | Mapped from changelog  
`destinationIpAddress` | `target.ip` | Mapped from changelog  
`destinationPortOrIcmpType` | `target.port` | Mapped from changelog  
`@computed.destinationIpCountry` | `target.location.country_or_region` | Mapped from changelog  
`ipProtocolId` | `network.ip_protocol` | Mapped from changelog  
`httpResponse` | `network.http.response_code` | Mapped from changelog  
`@computed.applicationProtocol` | `network.application_protocol` | Mapped from changelog  
`ruleId` | `security_result.rule_id` | Mapped from changelog  
`priorityId` | `security_result.priority_details` | Mapped from changelog  
`@computed.priority` | `security_result.priority` | Mapped from changelog  
`@computed.firewallPolicy` | `security_result.rule_name` | Mapped from changelog  
`@computed.message` | `security_result.threat_name` | Mapped from changelog  
`iocNumber` | `security_result.detection_fields` | Mapped from changelog  
`recordLength` | `security_result.detection_fields` | Mapped from changelog  
`@computed.recordTypeDescription` | `metadata.description` | Mapped from changelog  
`@computed.recordTypeCategory` | `metadata.product_event_type` | Mapped from changelog  
`user_name` | `principal.user.email_addresses` | Mapped from changelog  
`src_interface_name","dst_interface_name` | `metadata.ingestion_labels` | Mapped from changelog  
`category` | `security_result.threat_name` | Mapped from changelog  
`Classification` | `security_result.threat_name` | Mapped from changelog  
`DeviceUUID` | `principal.resource.id` | Mapped from changelog  
Log field | UDM mapping | Remark  
---|---|---  
`act` | `security_result.action_details` | For event IDs `313001`, `746014`.  
`Addr` | `principal.ip principal.asset.ip` | For event ID `734001`.  
`address` | `principal.ip principal.asset.ip` | For event ID `746014`.  
`action` | `metadata.ingestion_labels` | For event IDs `313001`, `746014`.  
`ap` | `metadata.ingestion_labels` |   
`api` | `metadata.ingestion_labels` |   
`Assigned Ip` | `principal.ip principal.asset.ip` | For event IDs `109201`, `109210`, `109207`.  
`assigned_ip` | `principal.ip principal.asset.ip` | For event IDs `109201`, `109210`, `109207`.  
`bytes` | `network.received_bytes` |   
`centry_addr` | `metadata.ingestion_labels` |   
`Client` | `network.http.parsed_user_agent` |   
`client_ip` | `principal.ip principal.asset.ip` |   
`COMMAND` | `principal.process.command_line` | For the `useradd` log type, which is event ID `199017`.  
`command_line` | `principal.process.command_line` |   
`connection_type` | `metadata.ingestion_labels` | For event ID `734001`.  
`ConnectionID` | `network.session_id` |   
`ConnectType` | `metadata.ingestion_labels` |   
`cribl_pipe` | `additional.fields` |   
`DE` | `metadata.ingestion_labels` |   
`desc` | `metadata.description` | For event IDs `109201`, `109210`, `109207`.  
`desc1` | `metadata.description` |   
`desc_data` | `metadata.description` |   
`description` | `metadata.description` |   
`dest_addr` | `target.ip target.asset.ip` | For event ID `602101`.  
`device_uuid` | `metadata.product_log_id` | Retrieved from JSON logs, where it indicates product ID details.  
`DeviceUUID` | `principal.resource.product_object_id` | Retrieved from syslog, which has the resource ID.  
`direction` | `network.direction` | For event ID `302020`.  
`DNSResponseType` | `network.dns.response_code` |   
`DNSSICategory` | `security_result.category_details` |   
`dpt` | `target.port` |   
`dst management IP` | `target.ip target.asset.ip` | For event ID `418001`.  
`dst management Port` | `target.port` | For event ID `418001`.  
`DstIP` | `target.ip` | For event ID `713906`.  
`dst_ip_range` | `target.network.ip_subnet_range` | For event IDs `418001`. `750001`, `750003`, `751002`, `750014`.  
`DstPort` | `target.port` | For event ID `713906`.  
`duration` | `network.session_duration.seconds` | Can be accessed in seconds.  
`euid` | `metadata.ingestion_labels` |   
`event_name` | `metadata.product_event_type` |   
`eventId` | `metadata.ingestion_labels`  
`metadata.product_event_type` |   
`exe` | `principal.process.command_line` |   
`exitcode` | `metadata.ingestion_labels` |   
`faddr` | `target.ip` (outbound)  
`principal.ip` (inbound) | For event ID `302020`.  
`fdqn` | `principal.hostname` | For event ID `746014`.  
`firewall` | `principal.ip`  
`principal.asset.ip` |   
`flag` | `metadata.ingestion_labels` | For event ID `500003`.  
`fport` | `target.port` (outbound)  
`principal.port` (inbound) | For event ID `302020`.  
`from` | `network.email.from` | For the `useradd` log type, which is event ID `199017`.  
`fromIP` | `principal.ip`  
`principal.asset.ip` | For event ID `500003`.  
`fromPort` | `principal.port` | For event ID `500003`.  
`gaddr` | `target.nat_port` (outbound)  
`principal.nat_port` (inbound) | For event ID `302020`.  
`GID` | `target.group.product_object_id` | For the `useradd` log type, which is event ID `199017`.  
`group_id` | `target.group.group_display_name` |   
`hdrlen` | `metadata.ingestion_labels` | For event ID `500003`.  
`home` | `metadata.ingestion_labels` | For the `useradd` log type, which is event ID `199017`.  
`host` | `principal.ip/hostname`  
`principal.hostname`  
`principal.asset.hostname` |   
`host_name` | `principal.hostname` |   
`HTTP_Hostname` | `target.resource.attribute.labels` |   
`HTTP_URI` | `target.resource.attribute.labels` |   
`icmp_code` | `metadata.ingestion_labels` | For event ID `313001`.  
`icmp_type` | `metadata.ingestion_labels` | For event ID `313001`.  
`interface` | `metadata.ingestion_labels` | For event ID `313004`.  
`interface_name` | `metadata.ingestion_labels` | For event IDs `313001`, `500003`.  
`intermediary_host` | `intermed.hostname`  
`intermed.asset.hostname` |   
`intermediary_ip` | `intermediary.ip` | For event ID `713906`.  
`ipp` | `principal.ip` |   
`IPReputationSICategory` | `security_result.category_details` |   
`kernel_value` | `additional.fields` |   
`laddr` | `principal.ip` (outbound)  
`target.ip` (inbound) | For event ID `302020`, and mapped based on the direction (inbound or outbound).  
`laddr` | `principal.ip`  
`principal.asset.ip` | For event ID `313004`.  
`Local` | `principal.ip`  
`principal.asset.ip` | For event IDs `750001`, `750003`, `751002`, `750014`.  
`Local_port` | `principal.port` | For event IDs `750001`, `750003`, `751002`, `750014`.  
`mailsize` | `network.sent_bytes` |   
`msgid` | `metadata.ingestion_labels` |   
`mtu_size` | `metadata.ingestion_labels` | For event ID `602101`.  
`name` | `target.user.user_display_name` | For the `useradd` log type, which is event ID `199017`.  
`NETWORK_SUSPICIOUS` | `SecCategory` (`security_result.category`) | For event ID `430001`.  
`os` | `principal.platform_version` |   
`osuser` | `principal.user.user_display_name` |   
`packet_size` | `metadata.ingestion_labels` | For event ID `602101`.  
`path` | `principal.process.file.full_path` |   
`pid` | `principal.process.pid` |   
`pktlen` | `metadata.ingestion_labels` | For event ID `500003`.  
`Policy` | `security_result.rule_labels` |   
`prin_ip` | `principal.ip`  
`principal.asset.ip` | Retrieved from `desc_data` (using the logic:  
`"desc_data" => "(?P<desc>.* %{IP:prin_ip}.*)"`).  
`prin_user` | `principal.user.userid` |   
`product` | `security_result.summary` | For event IDs `430002`, `430003`.  
`prot` | `network.ip_protocol` | For event ID `602101`.  
`Protocol` | `network.ip_protocol` | For event IDs `302020`, `313001`, `313004`, `418001`,  
`protocol` | `network.app_protocol` | For event ID `713906`.  
`protocol` | `network.ip_protocol`  
`network.application_protocol` | For when the log-field value is an application or IP protocol.  
`PWD` | `principal.process.file.full_path` | For the `useradd` log type, which is event ID `199017`.  
`reason` | `security_result.detection_fields` |   
`recipients` | `network.email.to` |   
`Remote` | `target.ip`  
`target.asset.ip` | For event IDs `750001`, `750003`, `751002`, `750014`.  
`Remote_port` | `target.port` | For event IDs `750001`, `750003`, `751002`, `750014`.  
`Revision` | `security_result.detection_fields` |   
`sec_desc` | `security_result.description` |   
`SecIntMatchingIP` | `metadata.ingestion_labels` |   
`SecRuleName` | `security_result.rule_name` | For event ID `734001`.  
`seq_num` | `security_result.detection_fields` |   
`Session` | `network.session_id` | For event IDs `109201`, `109210`, `109207`.  
`session_id` | `network.session_id` |   
`severity` | `security_result.summary` | For event IDs `430002`, `430003`.  
`shell` | `metadata.ingestion_labels` | For the `useradd` log type, which is event ID `199017`.  
`Sinkhole` | `metadata.ingestion_labels` |   
`smtpmsg` | `network.smtp.server_response` |   
`smtpstatus` | `network.http.response_code` |   
`sourceIpAddress` | `principal.ip` | For event ID `713906`.  
`source_ip` | `principal.ip`  
`principal.asset.ip` |   
`spt` | `principal.port` |   
`src management IP` | `principal.ip`  
`principal.asset.ip` | For event ID `418001`.  
`src management Port` | `principal.port` | For event ID `418001`.  
`src_addr` | `principal.ip`  
`principal.asset.ip` | For event ID `602101`.  
`src_app` | `principal.application` |   
`src_fwuser` | `principal.hostname` | For when `src_fwuser` is in the `host` format.  
`src_fwuser` | `principal.administrative_domain`  
`principal.hostname` | For when `src_fwuser` is in the `domain` or `host` format.  
`src_host` | `principal.hostname`  
`principal.asset.hostname` |   
`src_interface_name` | `metadata.ingestion_labels` |   
`SrcIP` | `principal.ip` | For event ID `713906`.  
`src_ip` | `principal.ip`  
`principal.asset.ip` |   
`src_ip_range` | `principal.network.ip_subnet_range` | For event IDs `750001`, `750003`, `751002`, `750014`.  
`src_port` | `principal.port` |   
`SrcPort` | `principal.port` | For event ID `713906`.  
`srcuser` | `principal.user.userid`  
`principal.user.user_display_name metadata.event_type` | The value for `metadata.event_type` is `USER_UNCATEGORIZED`.  
`sshd` | `principal.application` |   
`syslog_msg_id` |  | For event ID `716001`.  
`syslog_msg_text` | `security_result.description` |   
`tag` | `security_result.detection_fields` |   
`tar_ip` | `target.ip target.asset.ip` |   
`tar_port` | `target.port` |   
`TCPFlags` | `metadata.ingestion_labels` |   
`thread` | `metadata.ingestion_labels` |   
`timezoneadjustment` | `metadata.ingestion_labels` |   
`tls` | `network.smtp.is_tls` |   
`to` | `target.ip target.asset.ip` | For event ID `313004`.  
`toIP` | `target.ip target.asset.ip` | For event ID `500003`.  
`TRUE` | `is_significant` | For event ID `430001`.  
`toPort` | `target.port` | For event ID `500003`.  
`ts` | `metadate.event_timestamp` |   
`ts_year` | `metadate.event_timestamp` | For event ID `430001`.  
`tty` | `metadata.ingestion_labels` |   
`TTY` | `metadata.ingestion_labels` | For the `useradd` log type, which is event ID `199017`.  
`uid` | `metadata.ingestion_labels` |   
`UID` | `target.user.userid` | For the `useradd` log type, which is event ID `199017`.  
`URLSICategory` | `security_result.category_details` |   
`USER` | `target.user.userid` | For the `useradd` log type, which is event ID `199017`.  
`USER` | `principal.user.userid` | For all log types other than the `useradd` log type.  
`User` | `target.user.userid` | For event IDs `109201`, `109210`, `109207`, `734001`.  
`user` | `principal.user.userid` |   
`user_name` | `principal.user.email_addresses` |   
`UserAgent` | `network.http.user_agent`  
`network.http.parsed_user_agent` |   
`Username` | `principal.user.userid` | For event IDs `750001`, `750003`, `751002`, `750014`.  
`username` | `target.user.userid` |   
`username_Id` | `target.user.userid` |   
`version` | `metadata.ingestion_labels` |   
  
## UDM mapping delta reference

On November 6, 2025, Google SecOps released a new version of the Cisco Firepower NGFW parser, which includes significant changes to the mapping of Cisco Firepower NGFW log fields to UDM fields and changes to the mapping of event types.

### Log-field mapping delta

The following table lists the mapping delta for Cisco Firepower NGFW log-to-UDM fields exposed prior to November 6, 2025 and subsequently (listed in the **Old mapping** and **Current mapping** columns respectively). 

Log field | Old mapping | Current mapping  
---|---|---  
`act` | `security_result.description` | `security_result.action_details`  
`action` | `product_event_type` | `metadata.ingestion_labels`  
`DeviceUUID` | `principal.resource.id` | `principal.resource.product_object_id`  
`dpt` | `security_result.detection_fields` | `target.port`  
`flag` | `about.labels` | `metadata.ingestion_labels`  
`pid` | `principal.port` | `principal.process.pid`  
`Revision` | `security_result.about.labels` | `security_result.detection_fields`  
`spt` | `security_result.detection_fields` | `principal.port`  
`username` | `principal.user.userid` | `target.user.userid`  
  
### Event-type mapping delta

Multiple events that were classified before as generic event are now properly classified with meaningful event types.

The following table lists the delta for the handling of Cisco Firepower NGFW event types prior to November 6, 2025 and subsequently (listed in the **Old event_type** and **Current event-type** columns respectively).

Event ID from log | Old event_type | Current event_type  
---|---|---  
`113003` | `GENERIC_EVENT` | `USER_UNCATEGORIZED`  
`113009` | `GENERIC_EVENT` | `STATUS_UPDATE`  
`113010` | `GENERIC_EVENT` | `USER_LOGIN`  
`113039` | `GENERIC_EVENT` | `USER_LOGIN`  
`302020` | `STATUS_UPDATE` | `NETWORK_CONNECTION`  
`313001` | `GENERIC_EVENT` | `STATUS_UPDATE`  
`313004` | `GENERIC_EVENT` | `NETWORK_CONNECTION`  
`430002` | `NETWORK_CONNECTION` | `NETWORK_DNS`  
`430003` | `NETWORK_CONNECTION` | `NETWORK_DNS`  
`500003` | `GENERIC_EVENT` | `NETWORK_CONNECTION`  
`602101` | `STATUS_UPDATE` | `NETWORK_CONNECTION`  
`713906` | `STATUS_UPDATE` | `NETWORK_CONNECTION`  
`722051` | `GENERIC_EVENT` | `STATUS_UPDATE`  
`750003` | `STATUS_UPDATE` | `NETWORK_CONNECTION`  
`msmtp` | `STATUS_UPDATE` | `EMAIL_TRANSACTION`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-firepower-firewall-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
