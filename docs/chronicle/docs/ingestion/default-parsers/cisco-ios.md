---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ios/
title: Collect Cisco IOS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:24.710829+00:00
---

# Collect Cisco IOS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ios/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco IOS logs

**Parser Version:** 23.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco IOS logs to Google Security Operations using the Bindplane agent.

Cisco IOS devices generate syslog messages for system events, interface state changes, ACL matches, authentication, and routing events. The parser extracts fields using grok patterns and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Cisco IOS device
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Cisco IOS device usingng SSH or console



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
            chronicle/cisco_ios:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: CISCO_IOS
                raw_log_field: body
        
        service:
            pipelines:
                logs/cisco_ios_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/cisco_ios
        




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
           
           ```bash
           sudo systemctl status observiq-otel-collector
           ```
           

    2. Check logs for errors:
           
           ```bash
           sudo journalctl -u observiq-otel-collector -f
           ```
           

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
             




## Configure syslog on Cisco IOS device

  1. Sign in to the Cisco IOS device using SSH or a console connection.
  2. Enter privileged mode:
         
         enable
         

  3. Enter configuration mode:
         
         conf t
         

  4. Configure syslog:
         
         logging <BINDPLANE_IP>
         logging source-interface <INTERFACE>
         

     * Replace `<BINDPLANE_IP>` with the actual Bindplane agent IP address.
     * Replace `<INTERFACE>` with the actual communication interface.
  5. Configure the priority level:
         
         logging trap information
         logging console information
         

  6. Configure the syslog facility:
         
         logging facility syslog
         

  7. Save the configuration:
         
         copy running-config startup-config
         




## UDM mapping table

Log field | UDM mapping  
---|---  
`13_Protocol_Runtime_Context` | `additional.fields`  
`16_AdminWebappN` | `additional.fields`  
`16_AdminWebappT` | `additional.fields`  
`16_AdminWebappU` | `additional.fields`  
`16_BYODN` | `additional.fields`  
`16_BYODT` | `additional.fields`  
`16_BYODU` | `additional.fields`  
`16_DBListenerN` | `additional.fields`  
`16_DBListenerT` | `additional.fields`  
`16_DBListenerU` | `additional.fields`  
`16_DBServerN` | `additional.fields`  
`16_DBServerT` | `additional.fields`  
`16_DBServerU` | `additional.fields`  
`16_GuestN` | `additional.fields`  
`16_GuestT` | `additional.fields`  
`16_GuestU` | `additional.fields`  
`16_iowait` | `additional.fields`  
`16_ISEIndexingEngineN` | `additional.fields`  
`16_ISEIndexingEngineT` | `additional.fields`  
`16_ISEIndexingEngineU` | `additional.fields`  
`16_JVMN` | `additional.fields`  
`16_JVMT` | `additional.fields`  
`16_JVMU` | `additional.fields`  
`16_MessageQueueN` | `additional.fields`  
`16_MessageQueueT` | `additional.fields`  
`16_MessageQueueU` | `additional.fields`  
`16_MisservicesN` | `additional.fields`  
`16_MisservicesT` | `additional.fields`  
`16_MisservicesU` | `additional.fields`  
`16_NSFN` | `additional.fields`  
`16_NSFT` | `additional.fields`  
`16_NSFU` | `additional.fields`  
`16_ProfilerDatabaseN` | `additional.fields`  
`16_ProfilerDatabaseT` | `additional.fields`  
`16_ProfilerDatabaseU` | `additional.fields`  
`16_RMIT` | `additional.fields`  
`16_RMIU` | `additional.fields`  
`16_SyslogN` | `additional.fields`  
`16_SyslogT` | `additional.fields`  
`16_SyslogU` | `additional.fields`  
`4_ArpCache_InsertUpdate_Received` | `additional.fields`  
`4_HostName_Event_Fetch_FromAD` | `additional.fields`  
`4_Probe_Requests_Dropped` | `additional.fields`  
`4_Probe_Requests_Received` | `additional.fields`  
`AAA_ID` | `security_result.detection_fields`  
`about` | `event.idm.read_only_udm.about`  
`Acct-Session-Id` | `principal.resource.attribute.labels`  
`AcctRequest-Flags` | `security_result.summary`  
`AcctRequest-Flags` | `security_result.action`  
**Condition:**  
`[AcctRequest-Flags]` =~ "(?i)Start" or "(?i)Stop"  
`AcsSessionID` | `network.session_id`  
`Action_number` | `security_result.detection_fields`  
`address_family` | `security_result.detection_fields`  
`admin_state` | `security_result.detection_fields`  
`aid` | `security_result.detection_fields`  
`applet_statement` | `security_result.detection_fields`  
`application` | `principal.application`  
`application_name` | `principal.application`  
`arp_resp` | `additional.fields`  
`arp_src` | `principal.ip`   
`principal.asset.ip`  
`attr` | `additional.fields`  
`auditid` | `network.session_id`  
`auth_neg_dur` | `additional.fields`  
`Authen-Method` | `security_result.detection_fields`  
`Authen-Type` | `additional.fields`  
`authentication_protocol` | `security_result.detection_fields`  
`AuthenticationIdentityStore` | `additional.fields`  
`AuthenticationMethod` | `additional.fields`  
`AuthenticationStatus` | `security_result.summary`  
`AuthorizationPolicyMatchedRule` | `security_result.rule_name`  
`avg_time` | `additional.fields`  
`AVPair_priv-lvl` | `security_result.detection_fields`  
`AVPair_start_time` | `additional.fields`  
`AVPair_task_id` | `additional.fields`  
`AVPair_timezone` | `additional.fields`  
`band` | `additional.fields`  
`calledId` | `security_result.detection_fields`  
`calledId2` | `security_result.detection_fields`  
`callID` | `additional.fields`  
`Calling-Station-ID` | `additional.fields`  
`category` | `security_result.category`  
`category_number` | `security_result.detection_fields`  
`channel` | `additional.fields`  
`Chassis_data` | `additional.fields`  
`cisco_facility_2` | `security_result.detection_fields`  
`cisco_message` | `network.application_protocol`  
**Condition:**  
If `[cisco_message]` =~ "ssh" else if `[cisco_message]` =~ "HTTP"  
`cisco_mnemonic` | `security_result.rule_name`  
`cisco_severity` | `security_result.severity`  
**Condition:**  
`[cisco_severity]` == "0"  
**Additional details:**  
"`security_result.severity`" => "CRITICAL" "`security_result.severity_details`" => "System unusable"  
`cisco_severity` | `security_result.severity`  
**Condition:**  
`[cisco_severity]` == "1"  
**Additional details:**  
"`security_result.severity`" => "CRITICAL" "`security_result.severity_details`" => "Immediate action needed"  
`cisco_severity` | `security_result.severity`  
**Condition:**  
`[cisco_severity]` == "2"  
**Additional details:**  
"`security_result.severity`" => "HIGH" "`security_result.severity_details`" => "Critical condition"  
`cisco_severity` | `security_result.severity`  
**Condition:**  
`[cisco_severity]` == "3"  
**Additional details:**  
"`security_result.severity`" => "ERROR" "`security_result.severity_details`" => "Error condition"  
`cisco_severity` | `security_result.severity`  
**Condition:**  
`[cisco_severity]` == "4"  
**Additional details:**  
"`security_result.severity`" => "MEDIUM" "`security_result.severity_details`" => "Warning condition"  
`cisco_severity` | `security_result.severity`  
**Condition:**  
`[cisco_severity]` == "5"  
**Additional details:**  
"`security_result.severity`" => "LOW" "`security_result.severity_details`" => "Normal but significant condition"  
`cisco_severity` | `security_result.severity`  
**Condition:**  
`[cisco_severity]` == "6"  
**Additional details:**  
"`security_result.severity`" => "INFORMATIONAL" "`security_result.severity_details`" => "Informational message only"  
`cisco_severity` | `security_result.severity`  
**Condition:**  
`[cisco_severity]` == "7"  
**Additional details:**  
"`security_result.severity`" => "INFORMATIONAL" "`security_result.severity_details`" => "Appears during debugging only"  
`cisco_severity` | `security_result.severity` > "CRITICAL"  
`class_type` | `security_result.detection_fields`  
`client_mac` | `principal.mac`   
`principal.asset.mac`  
`ClientLatency` | `additional.fields`  
`CmdSet` | `principal.process.command_line`  
`CName` | `additional.fields`  
`code` | `additional.fields`  
`code_reference` | `additional.fields`  
`collected_timestamp` | `metadata.collected_timestamp`  
`collector_id` | `additional.fields`  
`command` | `principal.process.command_line`  
`command_code` | `additional.fields`  
`community_count` | `additional.fields`  
`ConfigVersionId` | `additional.fields`  
`context` | `additional.fields`  
`context2` | `additional.fields`  
`CPMSessionID` | `additional.fields`  
`current_state` | `security_result.detection_fields`  
`da_vendor` | `additional.fields`  
`data_value` | `additional.fields`  
`debug_file` | `principal.process.file.full_path`  
`debug_line` | `additional.fields`  
`debug_timestamp` | `security_result.detection_fields`  
`desc` | `metadata.description`  
`description` | `metadata.description`  
`DestinationIPAddress` | `target.ip`   
`target.asset.ip`  
`DestinationPort` | `target.port`  
`DetailedInfo` | `security_result.summary`  
`dev_type` | `principal.platform_version`  
`device_component` | `additional.fields`  
`Device_IP_Address` | `principal.ip`   
`principal.asset.ip`  
`device_os` | `additional.fields`  
`Device_Type` | `additional.fields`  
`DeviceType` | `principal.resource.resource_subtype`  
`DeviceType` | `principal.resource.resource_type`  
**Condition:**  
`[DeviceType]` =~ "Phone"  
`DIP` | `target.ip`   
`target.asset.ip`  
`DMac` | `target.resource.attribute.labels`  
`domain` | `principal.administrative_domain`  
`Domain` | `principal.administrative_domain`  
`dp_handle` | `additional.fields`  
`DPort` | `target.port`  
`dst_ip` | `target.ip`   
`target.asset.ip`  
`dst_mac` | `target.mac`   
`target.asset.mac`  
`dst_port` | `target.port`  
`dst_user` | `target.user.userid`  
`duration` | `additional.fields`  
`dynamic_mac` | `target.resource.attribute.labels`  
`EnableFlag` | `security_result.detection_fields`  
`ephone-1` | `principal.resource.attribute.labels`  
`essid` | `security_result.detection_fields`  
`event_id` | `additional.fields`  
`failure_reason` | `security_result.description`  
`file_path` | `principal.file.full_path`  
`first_bgp_community` | `additional.fields`  
`flapping_port_1` | `additional.fields`  
`flapping_port_2` | `additional.fields`  
`flowtype` | `security_result.detection_fields`  
`for ALG` | `additional.fields`  
`fqdn` | `security_result.detection_fields`  
`framed` | `security_result.detection_fields`  
`full_conn` | `additional.fields`  
`group` | `principal.group.group_display_name`  
`Hit cnt` | `additional.fields`  
`hmac_algorithm` | `additional.fields`  
`hostname` | `principal.hostname`   
`principal.asset.hostname`  
`hostname` (value = %PARSER-5-CFGLOG_LOGGEDCMD) | `metadata.product_event_type`  
`icmp_code` | `additional.fields`  
`icmp_type` | `additional.fields`  
`IdentityGroup` | `principal.user.group_identifiers`  
`IdentitySelectionMatchedRule` | `security_result.detection_fields`  
`IEC` | `additional.fields`  
`input intf` | `additional.fields`  
`input_interface` | `additional.fields`  
`inter_host` | `intermediary.ip`   
`intermediary.hostname`  
`interface` | `intermediary.resource.name`  
`interface_2` | `intermediary.resource.attribute.labels`  
`intermediary_host` | `intermediary.ip`   
`intermediary.hostname`  
`intermediary_ip` | `intermediary.ip`  
`internal_error` | `security_result.summary`  
`invalid_arp_count` | `additional.fields`  
`ip_ident` | `additional.fields`  
`ip_resp` | `additional.fields`  
`ip_sla_id` | `additional.fields`  
`ip_src` | `principal.ip`   
`principal.asset.ip`  
`IPSEC` | `additional.fields`  
`is_wpa` | `additional.fields`  
`IsMachineAuthentication` | `additional.fields`  
`IsMachineIdentity` | `security_result.detection_fields`  
`last_auth_ago` | `additional.fields`  
`list` | `security_result.detection_fields`  
`list_id` | `additional.fields`  
`loc_id` | `security_result.detection_fields`  
`Location` | `additional.fields`  
`logging_attribute` | `principal.resource.attribute.labels`  
`mapping-id` | `additional.fields`  
`MatchedCommandSet` | `additional.fields`  
`max_threshold` | `security_result.detection_fields`  
`message_type` | `additional.fields`  
`missed_packets` | `security_result.detection_fields`  
`Model_Name` | `additional.fields`  
`module` | `security_result.detection_fields`  
`module_id` | `security_result.detection_fields`  
`Name` | `additional.fields`  
`nas_identity` | `target.hostname`   
`target.asset.hostname`  
`nas_ip` | `target.nat_ip`  
`NAS_IP_Address` | `intermediary.ip`  
`nas_port` | `target.nat_port`  
`NAS-Identifier` | `target.resource.attribute.labels`  
`nastype` | `target.resource.attribute.labels`  
`nat_ip` | `principal.nat_ip`  
`Network_Device_Profile` | `additional.fields`  
`network_processor` | `additional.fields`  
`NetworkDeviceProfileId` | `principal.resource.product_object_id`  
`NetworkDeviceProfileName` | `principal.resource.name`  
`new_value` | `security_result.detection_fields`  
`new-state` | `security_result.detection_fields`  
`non-PATable` | `additional.fields`  
`Notification` | `additional.fields`  
`object_tracking_number` | `additional.fields`  
`offset` | `additional.fields`  
`oid` | `additional.fields`  
`oper_state` | `security_result.detection_fields`  
`peer-system-ip` | `target.ip`   
`target.asset.ip`  
`peer-type` | `additional.fields`  
`peer-vmanage-system-ip` | `target.ip`   
`target.asset.ip`  
`personality` | `principal.resource.attribute.labels`  
`pid` | `principal.process.pid`  
`PktLen` | `additional.fields`  
`Port` | `principal.resource.attribute.labels`  
`port range` | `additional.fields`  
`port_channel` | `security_result.detection_fields`  
`previous_state` | `security_result.detection_fields`  
`previous_value` | `security_result.detection_fields`  
`principal_resource` | `principal.resource.name`  
`principal_user_address` | `principal.user.attribute.labels`  
`privilege_level` | `security_result.detection_fields`  
`Privilege-Level` | `security_result.detection_fields`  
`process` | `principal.resource.attribute.labels`  
`process_name` | `target.application`  
`processing_time` | `additional.fields`  
`product_log_id` | `metadata.product_log_id`  
`prot` | `additional.fields`  
`Proto` | `additional.fields`  
`protocol` | `network.application_protocol`   
`network.ip_protocol`  
`Protocol` | `additional.fields`  
`protocol_number` | `security_result.detection_fields`  
`public-ip` | `principal.nat_ip`  
`public-port` | `principal.nat_port`  
`qfp_data` | `additional.fields`  
`radio` | `additional.fields`  
`reason` | `security_result.summary`  
`received_packets` | `network.received_bytes`  
`region` | `principal.location.country_or_region`  
`Remote-Address` | `target.ip`   
`target.asset.ip`  
`request_id` | `additional.fields`  
`RequestLatency` | `security_result.detection_fields`  
`Response` | `additional.fields`  
`result_action` | `security_result.action`  
`RSA_keypair` | `security_result.detection_fields`  
`rssi` | `additional.fields`  
`rtt` | `additional.fields`  
`sec_action` | `security_result.action`  
`security_process` | `security_result.detection_fields`  
`SelectedAccessService` | `security_result.action_details`  
`SelectedAuthenticationIdentityStores` | `security_result.detection_fields`  
`SelectedAuthorizationProfiles` | `security_result.detection_fields`  
`SelectedCommandSet` | `additional.fields`  
`SelectedShellProfile` | `additional.fields`  
`Service` | `additional.fields`  
`service` | `security_result.detection_fields`  
`Service-Argument` | `additional.fields`  
`session_id` | `network.session_id`  
`session_id2` | `security_result.detection_fields`  
`session_packet` | `network.sent_bytes`  
`severity-level` | `security_result.detection_fields`  
`SIP` | `principal.ip`   
`principal.asset.ip`  
`SMac` | `principal.resource.attribute.labels`  
`Socket` | `principal.resource.attribute.labels`  
`Software_Version` | `additional.fields`  
`source_facility` | `principal.hostname`   
`principal.asset.hostname`  
`sourced_by` | `additional.fields`  
`spi` | `security_result.detection_fields`  
`SPort` | `principal.port`  
`Src Intf` | `principal.resource.attribute.labels`  
`src_ip` | `principal.ip`   
`principal.asset.ip`   
`principal.hostname`   
`principal.asset.hostname`  
`src_ip_2` | `principal.ip`   
`principal.asset.ip`  
`src_mac` | `principal.mac`   
`principal.asset.mac`  
`src_port` | `principal.port`  
`src_user_id` | `principal.user.userid`  
`src_user_name` | `principal.user.user_display_name`  
`src_username` | `principal.user.user_display_name`  
`src-color` | `principal.resource.attribute.labels`  
`ssid` | `security_result.detection_fields`  
`state` | `security_result.detection_fields`  
`status_code` | `network.http.response_code`  
`status_msg` | `security_result.rule_name`  
`StepData_13` | `security_result.summary`  
`StepData_14` | `security_result.detection_fields`  
`StepData_15` | `security_result.detection_fields`  
`StepData_20` | `security_result.detection_fields`  
`StepData_21` | `security_result.detection_fields`  
`StepData_3` | `additional.fields`  
`StepData_4` | `security_result.detection_fields`  
`StepData_6` | `security_result.detection_fields`  
`StepData_7` | `security_result.detection_fields`  
`StepData_8` | `security_result.detection_fields`  
`StepLatency` | `additional.fields`  
`syslog_msg_category` | `additional.fields`  
`syslog_msg_id` | `additional.fields`  
`syslog_msg_level` | `additional.fields`  
`syslog_msg_source` | `additional.fields`  
`syslog_priority` | `additional.fields`  
`system-ip` | `principal.ip`   
`principal.asset.ip`  
`target_ip` | `target.ip`   
`target.asset.ip`  
`target_mac` | `target.mac`   
`target.asset.mac`  
`target_process_id` | `target.process.pid`  
`target_process_name` | `target.resource.attribute.labels`  
`target_user_address` | `target.user.attribute.labels`  
`thirdparty` | `additional.fields`  
`thread_id` | `principal.resource.attribute.labels`  
`timestamp` | `metadata.event_timestamp`  
`timestamp1` | `additional.fields`  
`tls_cipher` | `network.tls.cipher`  
`tls_client` | `network.tls.client.supported_ciphers`  
`TotalAuthenLatency` | `additional.fields`  
`tracked_object_id` | `additional.fields`  
`transport_protocol` | `additional.fields`  
`trustpoint` | `about.resource.name`  
`TS` | `additional.fields`  
`tty_number` | `additional.fields`  
`tunnel_client_endpoint` | `principal.ip`   
`principal.asset.ip`  
`Type` | `security_result.category_details`  
`uptime` | `additional.fields`  
`url` | `target.url`  
`User` | `principal.user.userid`  
`userName` | `target.user.userid`  
**Condition:**  
if (`[cisco_tag]` =~ "SEC_LOGIN-4-LOGIN_FAILED" or `[cisco_mnemonic]` =~ "LOGIN_FAILED") `[cisco_tag]` =~ "SEC_LOGIN-5-LOGIN_SUCCESS" or `[cisco_facility]` =~ "SEC_LOGIN" or `[cisco_facility]` =~ "SEC LOGIN" or `[cisco_mnemonic]`=~ "LOGIN_SUCCESS" or `[cisco_mnemonic]` =~ "SSH2_USERAUTH" or `[cisco_mnemonic]` =~ "LOGIN"  
`Username` | `principal.user.userid`  
`username_length` | `additional.fields`  
`UserType` | `additional.fields`  
`vap` | `additional.fields`  
`vlan_id` | `intermediary.resource.attribute.labels`  
`vlan_id_2` | `intermediary.resource.attribute.labels`  
`Vlan-Id` | `additional.fields`  
`VlanType` | `additional.fields`  
`vrid` | `security_result.detection_fields`  
`zone` | `additional.fields`  
`zone_pair` | `security_result.detection_fields`  
  
## Release deltas

Google SecOps released a new version of the Cisco IOS parser, which includes changes to the mapping of Parser_Name log fields to UDM fields and changes to the mapping of event types.

### Log-field mapping delta

The following table lists the mapping delta for Cisco IOS log-to-UDM fields:

Log field | Old mapping | Current mapping  
---|---|---  
`aid` | `additional.fields` | `security_result.detection_fields`  
`auditid` | `metadata.product_log_id` | `network.session_id`  
`cisco_severity` | `"security_result.severity" => "LOW"` | `"security_result.severity" => "CRITICAL"`  
`CmdSet` | `additional.fields` | `principal.process.command_line`  
`dst_user` ( value=host) | `target.user.userid` | `removed`  
`fqdn` | `principal.hostname` | `security_result.detection_fields`  
`hostname` (value = %PARSER-5-CFGLOG_LOGGEDCMD) | `principal.hostname` | `metadata.product_event_type`  
`IdentityGroup` | `additional.fields` | `principal.user.group_identifiers`  
`interface` | `intermediary.labels` | `intermediary.resource.name`  
`sequence_id` | `additional.fields` | `metadata.product_log_id`  
`User` | `target.user.userid` | `principal.user.userid`  
  
### Event-type mapping delta

**Existing event types with modifications in the conditions used:**

Event type | Conditions | Reason  
---|---|---  
`STATUS_UPDATE` | `else if`(`[principal_mid_present]` == "true" or `[has_principal]` == "true")`and [target_mid_present] == "false" {` | `To avoid setting up STATUS_UPDATE if principal.ip and target.ip both are present.`  
`USER_UNCATEGORIZED` | `else if [principal_userid_present] == "true" or [principal_display_name_present] == "true" or [target_userid_present] == "true" {` |   
  
**New event types:**

New event type | Conditions  
---|---  
`DEVICE_CONFIG_UPDATE` | `else if [principal_mid_present] == "true" and [cisco_tag] in ["PARSER-5-CFGLOG_LOGGEDCMD","SYS-5-CONFIG_I"] {`  
`USER_LOGIN` | `else if`(`[principal_userid_present]` == "true" or `[principal_display_name_present]` == "true" or `[target_userid_present]` == "true")`and [process_name] != "" and`(`[user_event]` =~ "(?i)new tcp session" or `[user_event]` =~ "(?i)created new session")`{`  
`USER_LOGIN` | `else if [target_mid_present] == "true" and [user_event] =~ "`(?i)`logging" {`  
`USER_UNCATEGORIZED` | `else if [principal_userid_present] == "true" or [target_userid_present] == "true" or [principal_mac_present] == "true" {`  
Log field | UDM mapping  
AcsSessionID | network.session_id  
AcctRequest-Flags | security_result.summary  
AcctRequest-Flags | security_result.action  
AuthenticationIdentityStore | additional.fields.key = `AuthenticationIdentityStore`, value = AuthenticationIdentityStore  
AuthenticationMethod | additional.fields.key = `AuthenticationMethod`, value = AuthenticationMethod  
AuthenticationStatus | security_result.summary  
Authen-Method | security_result.detection_fields.key = `Authen-Method`, value = Authen-Method  
Authen-Method | extensions.auth.type  
AVPair_priv-lvl | security_result.detection_fields.key = `AVPair_priv-lvl`, value = AVPair_priv-lvl  
AVPair_start_time | additional.fields.key = `AVPair_start_time`, value = AVPair_start_time  
AVPair_task_id | additional.fields.key = `AVPair_task_id`, value = AVPair_task_id  
AVPair_timezone | additional.fields.key = `AVPair_timezone`, value = AVPair_timezone  
auditid | metadata.product_log_id  
cisco_facility |   
cisco_message | metadata.description  
cisco_mnemonic | security_result.rule_name  
cisco_severity | security_result.severity  
cisco_severity | security_result.severity_details  
cisco_tag | metadata.product_event_type  
cisco_tag | metadata.event_type  
ClientLatency | additional.fields.key = `ClientLatency`, value = ClientLatency  
CmdSet | additional.fields.key = `CmdSet`, value = CmdSet  
command | principal.process.command_line  
CPMSessionID | additional.fields.key = `CPMSessionID`, value = CPMSessionID  
description | metadata.description  
DestinationIPAddress | target.asset.ip  
DestinationIPAddress | target.ip  
DestinationPort | target.port  
Device_IP_Address | principal.asset.ip  
Device_IP_Address | principal.ip  
Device_Type | additional.fields.key = `Device_Type`, value = Device_Type  
dst_ip | target.asset.ip  
dst_ip | target.ip  
dst_port | target.port  
dst_user | target.user.userid  
EnableFlag | security_result.detection_fields.key = `EnableFlag`, value = EnableFlag  
IdentityGroup | additional.fields.key = `IdentityGroup`, value = IdentityGroup  
IdentitySelectionMatchedRule | security_result.detection_fields.key = `IdentitySelectionMatchedRule`, value = IdentitySelectionMatchedRule  
intermediary_host | intermediary.hostname  
intermediary_ip | intermediary.ip  
IPSEC | additional.fields.key = `IPSEC`, value = IPSEC  
ISEPolicySetName | extensions.auth.type  
IsMachineAuthentication | additional.fields.key = `IsMachineAuthentication`, value = IsMachineAuthentication  
IsMachineIdentity | security_result.detection_fields.key = `IsMachineIdentity`, value = IsMachineIdentity  
Location | additional.fields.key = `Location`, value = Location  
MatchedCommandSet | additional.fields.key = `MatchedCommandSet`, value = MatchedCommandSet  
message |   
metadata_event_type | metadata.event_type  
Model_Name | additional.fields.key = `Model_Name`, value = Model_Name  
Name | additional.fields.key = `Name`, value = Name  
Network_Device_Profile | additional.fields.key = `Network_Device_Profile`, value = Network_Device_Profile  
NetworkDeviceGroups | additional.fields.key = `NetworkDeviceGroups`, value = NetworkDeviceGroups  
NetworkDeviceName | principal.asset.hostname  
NetworkDeviceName | principal.hostname  
NetworkDeviceProfileId | principal.resource.product_object_id  
pid | principal.process.pid  
Port | principal.resource.attribute.labels.key = `Port`, value = Port  
Privilege-Level | security_result.detection_fields.key = `Privilege-Level`, value = Privilege-Level  
product_event_type | metadata.product_event_type  
Protocol | additional.fields.key = `Protocol`, value = Protocol  
protocol | network.application_protocol  
protocol | network.ip_protocol  
reason | security_result.summary  
region | principal.location.country_or_region  
Remote-Address | target.asset.ip  
Remote-Address | target.ip  
RequestLatency | security_result.detection_fields.key = `RequestLatency`, value = RequestLatency  
Response | additional.fields.key = `Response`, value = Response  
SelectedAccessService | security_result.action_details  
SelectedAuthenticationIdentityStores | security_result.detection_fields.key = `SelectedAuthenticationIdentityStores`, value = SelectedAuthenticationIdentityStores  
SelectedCommandSet | additional.fields.key = `SelectedCommandSet`, value = SelectedCommandSet  
Service | additional.fields.key = `Service`, value = Service  
Service-Argument | additional.fields.key = `Service-Argument`, value = Service-Argument  
severity | security_result.severity  
Software_Version | additional.fields.key = `Software_Version`, value = Software_Version  
source_facility | principal.asset.hostname  
source_facility | principal.hostname  
src_ip | principal.asset.ip  
src_ip | principal.ip  
src_mac | principal.mac  
src_port | principal.port  
src_user_id | principal.user.userid  
src_user_name | principal.user.user_display_name  
Step | additional.fields.key = `Step`, value = Step  
StepData_10 | principal.asset.hostname  
StepData_10 | principal.hostname  
StepData_13 | security_result.summary  
StepData_14 | security_result.detection_fields.key = `StepData_14`, value = StepData_14  
StepData_15 | security_result.detection_fields.key = `StepData_15`, value = StepData_15  
StepData_20 | security_result.detection_fields.key = `StepData_20`, value = StepData_20  
StepData_21 | security_result.detection_fields.key = `StepData_21`, value = StepData_21  
StepData_3 | additional.fields.key = `StepData_3`, value = StepData_3  
StepData_4 | security_result.detection_fields.key = `StepData_4`, value = StepData_4  
StepData_6 | security_result.detection_fields.key = `StepData_6`, value = StepData_6  
StepData_7 | security_result.detection_fields.key = `StepData_7`, value = StepData_7  
StepData_8 | security_result.detection_fields.key = `StepData_8`, value = StepData_8  
StepData_9 | principal.user.userid  
target_host | target.asset.hostname  
target_host | target.hostname  
timestamp | metadata.event_timestamp  
TotalAuthenLatency | additional.fields.key = `TotalAuthenLatency`, value = TotalAuthenLatency  
ts | metadata.event_timestamp  
Type | security_result.category_details  
User | principal.user.userid  
UserType | additional.fields.key = `UserType`, value = UserType  
| metadata.vendor_name  
| metadata.product_name  
| metadata.log_type  
`hostname` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`  
`description` | `event.idm.read_only_udm.metadata.description`  
`application` | `event.idm.read_only_udm.principal.application`  
`userName` | `event.idm.read_only_udm.target.user.userid`  
`intermediary_host` | `event.idm.read_only_udm.intermediary.ip`  
`target_mac` | `event.idm.read_only_udm.target.mac`  
`target_mac` | `event.idm.read_only_udm.target.asset.mac`  
`fqdn` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`  
`sec_action` | `event.idm.read_only_udm.security_result.action`  
`session_packet` | `event.idm.read_only_udm.network.sent_bytes`  
`missed_packets` | `event.idm.read_only_udm.additional.fields`  
`inter_host` | `event.idm.read_only_udm.intermediary.ip`  
`target_host` | `event.idm.read_only_udm.intermediary.ip`  
`inter_host` | `event.idm.read_only_udm.intermediary.hostname`  
`tls_cipher` | `network.tls.cipher`  
`tls_client` | `network.tls.client.supported_ciphers`  
`Chassis_data` | `additional.fields`  
`extensions.auth.type` | `AUTHTYPE_UNSPECIFIED`  
`client_mac` | `principal.mac`  
`sequence_id","vap", "band", "channel", "rssi", "aid" and "radio` | `additional.fields`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-ios-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
