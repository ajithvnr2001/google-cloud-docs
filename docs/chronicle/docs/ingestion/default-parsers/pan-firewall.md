---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-firewall/
title: Collect Palo Alto Networks firewall logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:46.576944+00:00
---

# Collect Palo Alto Networks firewall logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-firewall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Palo Alto Networks firewall logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how to configure Google Security Operations to ingest logs from Palo Alto Networks using two primary deployment methods.

Select the following section that matches your architecture:

  * Palo Alto Networks Firewall
    * Description: Collects logs directly from PAN-OS firewalls.
    * Ingestion method: Logs are sent using syslog to a Google SecOps forwarder or a Bindplane agent. Because the Google SecOps forwarder is deprecated, use the Bindplane agent for log forwarding.
    * Supported formats: CSV, CEF, and LEEF.
  * Palo Alto Networks Firewall Strata Logging Service
    * Description: Collects logs from the cloud-based Strata Logging Service.
    * Ingestion method: Logs are forwarded directly to Google SecOps using an HTTPS webhook. No local forwarder is required for this method.
    * Supported formats: JSON Array.



## Palo Alto Networks Firewall

### Overview

This document describes how you can configure syslog and a Google SecOps forwarder to collect Palo Alto Networks firewall logs. This document also explains how Palo Alto Networks firewall log fields map to Google SecOps Unified Data Model (UDM) fields. For an overview about Google SecOps data ingestion, see [Data ingestion to Google SecOps](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow.md). An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the PAN_FIREWALL ingestion label.

### Before you begin

  * Ensure that the Palo Alto Networks firewall product is properly deployed and configured. For detailed setup instructions, refer to the [PAN-OS Documentation](https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/getting-started).
  * To understand the components deployed to collect Palo Alto Networks firewall logs, review the deployment architecture. Each customer deployment might differ from this representation and might be more complex. The following diagram shows how you can configure syslog on a Palo Alto Networks firewall and install a Google SecOps forwarder on a Linux server to forward log data to Google SecOps. The parser supports logs written in the following data formats: Comma Separated Values (CSV), Common Event Format (CEF), and Log Event Extended Format (LEEF).

![Deployment architecture](https://docs.cloud.google.com/static/chronicle/docs/ingestion/default-parsers/images/parser-pan-firewall-architecture.svg)

  * Verify the log formats and PAN-OS versions that the Google SecOps parser supports. The following table lists the log formats and the corresponding PAN-OS versions that the Google SecOps parser supports:

**Log format** | **PAN-OS version**  
---|---  
CSV  | 10.1.3   
CEF  | 10.0.0   
LEEF  | 9.1.0   
  * Verify the Palo Alto Networks firewall log types that the Google SecOps parser supports. The Google SecOps parser supports the following Palo Alto Networks firewall log types:

    * Traffic
    * Threat
    * WildFire submissions
    * Tunnel inspection
    * Config
    * System
    * HIP match
    * IP-Tag
    * User-ID
    * Decryption
    * Authentication
    * URL filtering
    * Data filtering
    * GlobalProtect
    * Correlation
    * GTP
    * SCTP
    * Audit

For more information about the Palo Alto Networks firewall log types, see [PAN-OS log types](https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/monitoring/view-and-manage-logs/log-types-and-severity-levels.html).

  * Ensure that all systems in the deployment architecture are configured in the UTC time zone.

  * Before you use the Palo Alto Networks firewall parser, review the [changes in field mappings between the previous parser and the current Palo Alto Networks firewall parser](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/field-maps/pan-firewall-map-changes). As part of the migration, ensure that the rules, searches, dashboards, or other processes that depend on the original fields use the updated fields.

For example, in the previous parser version, the `category` log field is mapped to the `security_result.description` UDM field. In the current Palo Alto Networks firewall parser, the `category` log field is mapped to the `security_result.category_details` UDM field. If you migrate to the current Palo Alto Networks firewall parser and use the `category` field in your rules, you need to modify the rules to use the `security_result.category_details` UDM field of the current parser.




### Configure syslog and the Google Security Operations forwarder

To configure syslog and the Google SecOps forwarder, complete the following steps:

  1. To monitor CSV logs, configure the syslog server profile. For more information, see [Configure the syslog server profile](https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/monitoring/use-syslog-for-monitoring/configure-syslog-monitoring.html). When you configure the syslog server profile, specify "Default" as the custom log format.
  2. To monitor CEF logs, configure the Palo Alto Networks firewall to forward CEF logs. For more information, [download the PAN-OS CEF Integration guide PDF](https://docs.paloaltonetworks.com/content/dam/techdocs/en_US/pdf/cef/pan-os-10-0-cef-configuration-guide.pdf) and see the "Configuration of Palo Alto Networks NGFW to output CEF events" section.
  3. To monitor LEEF logs, configure the syslog server profile. For more information, see [Custom log forwarding in LEEF format](https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClEcCAK).
  4. Configure the Google SecOps forwarder to send logs to Google Security Operations. For more information, see [Installing and configuring the forwarder on Linux](https://docs.cloud.google.com/chronicle/docs/install/forwarder-linux.md). The following is an example of a Google SecOps forwarder configuration:
         
         - syslog:
               common:
                 enabled: true
                 data_type: PAN_FIREWALL
                 batch_n_seconds: 10
                 batch_n_bytes: 1048576
               tcp_address: 0.0.0.0:10518
               connection_timeout_sec: 60
         




### Configure syslog forwarding on PAN Firewall

#### Create a syslog server profile

  1. Sign in to the **Palo Alto Networks Firewall Management Console**.
  2. Go to **Device** > **Server Profiles** > **Syslog**.
  3. Click **Add** to create a new server profile.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps BindPlane`).
     * **Location** : Select the virtual system (vsys) or **Shared** where this profile will be available.
  5. Click **Servers** > **Add** to configure the syslog server.
  6. Provide the following server configuration details: 
     * **Name** : Enter a descriptive name for the server (for example, `BindPlane Agent`).
     * **Syslog Server** : Enter the BindPlane Agent IP address.
     * **Transport** : Select **UDP** or **TCP** , depending on your BindPlane Agent configuration (UDP is default).
     * **Port** : Enter the BindPlane Agent port number (for example, `514`).
     * **Format** : Select **BSD** (default) or **IETF** , depending on your requirements.
     * **Facility** : Select **LOG_USER** (default) or another facility as needed.
  7. Click **OK** to save the syslog server profile.



#### Optional: Configure custom log format for CEF or LEEF

If you need CEF (Common Event Format) or LEEF (Log Event Extended Format) logs instead of CSV:

  1. In the Syslog Server Profile, select the **Custom Log Format** tab.
  2. Configure the custom log format for each log type (Config, System, Threat, Traffic, URL, Data, WildFire, Tunnel, Authentication, User-ID, HIP Match).
  3. For CEF format configuration, refer to the [Palo Alto Networks CEF Configuration Guide](https://docs.paloaltonetworks.com/resources/cef).
  4. Click **OK** to save the configuration.

**Note:** Palo Alto Networks recommends PAN-OS 8.0.3 or later for CEF custom log formats.

#### Create a log forwarding profile

  1. Go to **Objects** > **Log Forwarding**.
  2. Click **Add** to create a new log forwarding profile.
  3. Provide the following configuration details: 
     * **Name** : Enter a profile name (for example, `Google SecOps Forwarding`). If you want the firewall to automatically assign this profile to new security rules and zones, name it `default`.
  4. For each log type you want to forward (Traffic, Threat, WildFire Submission, URL Filtering, Data Filtering, Tunnel, Authentication), configure the following: 
     * Click **Add** in the respective log type section.
     * **Syslog** : Select the syslog server profile you created (for example, `Google SecOps BindPlane`).
     * **Log Severity** : Select the severity levels to forward (for example, **All**).
  5. Click **OK** to save the log forwarding profile.



#### Apply log forwarding profile to security policies

  1. Go to **Policies** > **Security**.
  2. Select the security rule(s) for which you want to enable log forwarding.
  3. Click the rule to edit it.
  4. Go to the **Actions** tab.
  5. In the **Log Forwarding** menu, select the log forwarding profile you created (for example, `Google SecOps Forwarding`).
  6. Click **OK** to save the security policy configuration.



#### Configure log settings for system logs

  1. Go to **Device** > **Log Settings**.
  2. For each log type (System, Configuration, User-ID, HIP Match, Global Protect, IP-Tag, SCTP) and severity level, select the syslog server profile you created.
  3. Click **OK** to save the log settings.



#### Commit the changes

  1. Click **Commit** at the top of the firewall web interface.
  2. Wait for the commit to complete successfully.
  3. Verify that logs are being sent to the Bindplane agent by checking the Google SecOps console for incoming Palo Alto Networks firewall logs.



### Forward Logs to Google SecOps using Bindplane agent

  1. Install and set up a **Linux Virtual Machine**.
  2. Install and configure the Bindplane agent on Linux to forward logs to Google SecOps. For more information about how to install and configure the Bindplane agent, see [the Bindplane agent installation and configuration instructions](https://bindplane.com/docs/getting-started/quickstart-guide).



If you encounter issues when you create feeds, contact [Google SecOps support](https://docs.cloud.google.com/chronicle/docs/support).

### Supported log formats

The Palo Alto Networks firewall parser supports logs in LEEF,CEF and CSV format.

### Supported sample logs

  * LEEF
        
        <14>Jan 22 02:20:19 device_host LEEF:1.0|Palo Alto Networks|PAN-OS Syslog Integration|10.2.12-h4|Microsoft MSOFFICE(52033)|ReceiveTime=2025/01/22 02:20:18|SerialNumber=01250100xxxx|cat=THREAT|Subtype=wildfire|devTime=Jan 22 2025 08:20:18 GMT|src=198.50.100.1|dst=198.50.100.2|srcPostNAT=198.50.100.3|dstPostNAT=198.50.100.4|RuleName=AZURE-US-NEW-CNF_Inbound_To_Azure-ALLOW|usrName=|SourceUser=|DestinationUser=|Application=smtp-base|VirtualSystem=vsys1|SourceZone=McD-Global-Zone|DestinationZone=Azure-Zone|IngressInterface=ae1.111|EgressInterface=ae2.409|LogForwardingProfile=Default-Traffic-Logging|SessionID=35331795|RepeatCount=1|srcPort=21578|dstPort=25|srcPostNATPort=0|dstPostNATPort=0|Flags=0x2000|proto=tcp|action=allow|Miscellaneous=\"......3...................xls\"|ThreatID=Microsoft MSOFFICE(52033)|URLCategory=malicious|sev=4|Severity=high|Direction=client-to-server|sequence=7462614601465681755|ActionFlags=0x8000000000000000|SourceLocation=198.50.100.1-198.50.100.255|DestinationLocation=United States|ContentType=|PCAP_ID=0|FileDigest=0ea04c99bf188c2e4207f60f92ca7c6f5088c7943ee63f45c50032bbd2bf7ea9|Cloud=demo.com|URLIndex=1|RequestMethod=|FileType=ms-office|Sender=sender@ab.myownpersonaldomain.com|Subject=\"............:.................................................................................-.........(Name)-2025-01-22...............:Y107202501220005, ............:........................, ...............:.........\"|Recipient=abc@demo.myownpersonaldomain.com|ReportID=117022282776|DeviceGroupHierarchyL1=143|DeviceGroupHierarchyL2=144|DeviceGroupHierarchyL3=39|DeviceGroupHierarchyL4=0|vSrcName=|DeviceName=device_host|SrcUUID=|DstUUID=|TunnelID=0|MonitorTag=|ParentSessionID=0|ParentStartTime=|TunnelType=N/A|ThreatCategory=N/A|ContentVer=WildFire-0
        

  * CEF
        
        14>1 2024-04-04T16:21:56+02:00 FW-PERIMETRAL-AVG-01 - - - - CEF:0|Palo Alto Networks|PAN-OS|10.1.10-h2|end|TRAFFIC|1|src=198.51.100.1 dst=198.51.100.2 srcTranslatedAddress=198.51.100.3 dstTranslatedAddress=198.51.100.4 rule=FW_USER_NATS2_APP suser= duser= app=bittorrent vs=vsys1 sz=INSIDE dz=EXTERNAL InboundInterface=ae2.2266 OutboundInterface=ae1 lp=log_forwarding sid=2935823 cnt=1 spt=6881 dpt=51413 srcTranslatedPort=0 dstTranslatedPort=0 flags=0x7a proto=udp act=allow tbytes=475 in=150 out=325 pkt=2 pktReceived=1 pktSent=1 start=Apr 04 2024 14:21:56 GMT stime=1206 urlcat=any externalId=externalId reason=aged-out DGl1=11 DGl2=161 DGl3=0 DGl4=0 VsysName=STONESOFT dvchost=FW-PERIMETRAL-AVG-01 cat=from-policy ActionFlags=0x8000000000000000 srcUUID= dstUUID= TunnelID=0 MonitorTag= ParentSessionID=0 ParentStartTime= TunnelType=N/A SCTPAssocID=0 SCTPChunks=0 SCTPChunkSent=0 SCTPChunksRcv=0 RuleUUID=746c3eb6-3d51-4679-8438-bd0e00e170a8 HTTP2Con=0 LinkChange=0 PolicyID= LinkDetail= SDWANCluster= SDWANDevice= SDWANClustype= SDWANSite= DynamicUsrgrp= XFFIP= srcDevCat= srcDevProf= srcDevModel= srcDevVendor= srcDevOS= srcDevOSv= srcHostname= srcMac= dstDevCat= dstDevProf= dstDevModel= dstDevVendor= dstDevOS= dstDevOSv= dstHostname= dstMac= ContainerName= PODNamespace= PODName= srcEDL= dstEDL= GPHostID= EPSerial= srcDAG= dstDAG= HASessionOwner= TimeHighRes=2024-04-04T16:21:56.250+02:00 ASServiceType= ASServiceDiff="
        

  * CSV
        
        1,2021/10/24 15:30:07,,CONFIG,0,2561,2021/10/24 15:30:07,198.51.100.0,,set,admin,Web,Succeeded, network virtual-router  VR1,,VR1  { ecmp { algorithm { ip-modulo ; } } protocol { bgp { routing-options { graceful-restart { enable yes; } } enable no; } rip { enable no; } ospf { enable no; } ospfv3 { enable no; } } routing-table { ip { static-route { vr1-log  { path-monitor { enable no; failure-condition any; hold-time 2; } nexthop { ip-address 198.51.100.0; } bfd { profile None; } interface ethernet1/1; metric 10; destination 0.0.0.0/0; route-table { unicast ; } } } } } interface [ ethernet1/1 ethernet1/2 ]; } ,7022390503849066572,0x0,0,0,0,0,,PA-VM,0,
        




### Field mapping reference: Logs fields to UDM fields

This section explains how the parser maps Palo Alto Networks firewall log fields to Google SecOps UDM event fields for each log type. The Google SecOps label key refers to the name of the key mapped to Labels.key UDM field.

For example, in the case of the "Virtual System" field, the field name is "cs3" in CEF format and is "VirtualSystem" in LEEF format. The UDM field "about.labels.key" contains the value "vsys" and the UDM field "about.labels.value" contains the value of that field. Some of the CEF or LEEF field names do not have a name corresponding to the CSV field names. In such cases, if you add your own variable name in custom log format in the syslog profile, the parser does not map it to the UDM field.

Refer to the following sections for mapping reference of each log type:

  * System
  * Config
  * Threat/wildfire
  * Traffic
  * User ID
  * HIP match
  * IP tag
  * Decryption
  * Tunnel
  * Authentication
  * URL
  * Data
  * GlobalProtect
  * Correlation
  * GTP
  * SCTP
  * Audit

**Deprecated:**

The following `labels` fields for UDM nouns are deprecated: `about.labels`, `intermediary.labels`, `observer.labels`, `principal.labels`, `src.labels`, `security_result.about.labels`, and `target.labels`. For existing parsers, in addition to these UDM fields, the logs fields are also mapped to key/value `additional.fields` UDM fields. For new parsers, the key/value settings in `additional.fields` UDM fields are used instead of the deprecated `labels` UDM fields. We recommend that you update the existing rules to use the key/value settings in the `additional.fields` UDM fields instead of the deprecated `labels` UDM fields.

### System

The following table lists the log fields of the system log type and their corresponding UDM fields.

CSV field | CEF field | LEEF field | Google Security Operations label key | UDM field  
---|---|---|---|---  
Receive Time (receive_time or cef-formatted-receive_time)  | rt  | devTime  |  | metadata.collected_timestamp,  metadata.event_timestamp (if "Generate Time" is absent)   
Serial Number (serial)  | deviceExternalId  | SerialNumber  |  | target.asset.hardware.serial_number  
intermediary.asset.hardware.serial_number   
Type (type)  | type (Header)  | cat  |  | metadata.product_event_type is set to "%{type} - %{subtype}".   
Threat/Content Type (subtype)  | subtype (Header)  | Subtype  |  | metadata.product_event_type is set to "%{type} - %{subtype}".   
Generated Time (time_generated or cef-formatted-time_generated)  |  |  |  | metadata.event_timestamp   
Virtual System (vsys)  | cs3  | VirtualSystem  | vsys  | target.asset.attribute.labels.key/value  
intermediary.asset.attribute.labels.key/value   
Event ID (eventid)  | cat  |  | eventid  | additional.fields.key and additional.fields.value.string_value   
Object (object)  | fname  | Filename  | object  | target.resource.name   
Module (module)  | flexString2  | Module  | module  | additional.fields.key and additional.fields.value.string_value   
Severity (severity)  | $number-of-severity(header)  | Severity  |  | security_result.severity and security_result.severity_details   
Description (opaque)  | msg  | msg  |  | metadata.description   
| principal_user_userid (This field is extracted from the msg field)  |  |  | principal.user.userid   
| principal_ip3 (This field is extracted from the msg field)  |  |  | principal.ip   
| Reason (This field is extracted from the msg field)  |  |  | security_result.description   
| server_address (This field is extracted from the msg field.)  |  |  | target.ip   
| server_profile (This field is extracted from the msg field.)  |  |  | additional.fields.key and additional.fields.value.string_value   
Sequence Number (seqno)  | externalId  | sequence  |  | metadata.product_log_id   
Action Flags (actionflags)  | PanOSActionFlags  | ActionFlags  | actionflags  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_1 to dg_hier_level_4)  | PanOSDGl1  | DeviceGroupHierarchyL1  | dg_hier_level_1  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_2)  | PanOSDGl2  | DeviceGroupHierarchyL2  | dg_hier_level_2  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_3)  | PanOSDGl3  | DeviceGroupHierarchyL3  | dg_hier_level_3  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_4)  | PanOSDGl4  | DeviceGroupHierarchyL4  | dg_hier_level_4  | additional.fields.key and additional.fields.value.string_value   
Virtual System Name (vsys_name)  | PanOSVsysName  | vSrcName  |  | target.asset.attribute.labels.key/value  
intermediary.asset.attribute.labels.key/value   
Device Name (device_name)  | dvchost  | DeviceName  |  | target.hostname  
intermediary.hostname   
High Resolution Timestamp (high_res_timestamp)  | PanOSTimeGeneratedHighResolution  |  |  | additional.fields.key and additional.fields.value.string_value   
  
### Config

The following table lists the log fields of the config log type and their corresponding UDM fields.

CSV field | CEF field | LEEF field | Google Security Operations label key | UDM field  
---|---|---|---|---  
Receive Time (receive_time or cef-formatted-receive_time)  | rt  | devTime  |  | metadata.collected_timestamp,  metadata.event_timestamp (if "Generate Time" is absent)   
Serial Number (serial)  | deviceExternalId  | SerialNumber  |  | target.asset.hardware.serial_number  
intermediary.asset.hardware.serial_number   
Type (type)  | type (Header)  | cat  |  | metadata.product_event_type   
Threat/Content Type (subtype)  | subtype (Header)  |  |  | metadata.product_event_type   
Generated Time (time_generated or cef-formatted-time_generated)  |  |  |  | metadata.event_timestamp   
Host (host)  | shost  | src  |  | principal.ip/hostname   
Virtual System (vsys)  | cs3  | VirtualSystem  | vsys  | target.asset.attribute.labels.key/value  
intermediary.asset.attribute.labels.key/value   
Command (cmd)  | act  | msg  | cmd  | principal.process.command_line   
Admin (admin)  | duser  | usrName  |  | principal.user.userid   
Client (client)  | destinationServiceName  | client  |  | principal.application   
Result (result)  | Signature ID (Header)(reason)  | Result  |  | security_result.summary   
Configuration Path (path)  | msg  | ConfigurationPath  |  | principal.process.command_line   
Before Change Detail (before_change_detail)  | cs1  | BeforeChangeDetail  | before_change_detail  | target.resource.attribute.labels.key/value   
After Change Detail (after_change_detail)  | cs2  | AfterChangeDetail  | after_change_detail  | target.resource.attribute.labels.key/value   
Sequence Number (seqno)  | externalId  | sequence  |  | metadata.product_log_id   
Action Flags (actionflags)  | PanOSActionFlags  | ActionFlags  | actionflags  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_1 to dg_hier_level_4)  | PanOSDGl1  | DeviceGroupHierarchyL1  | dg_hier_level_1  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_2)  | PanOSDGl2  | DeviceGroupHierarchyL2  | dg_hier_level_2  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_3)  | PanOSDGl3  | DeviceGroupHierarchyL3  | dg_hier_level_3  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_4)  | PanOSDGl4  | DeviceGroupHierarchyL4  | dg_hier_level_4  | additional.fields.key and additional.fields.value.string_value   
Virtual System Name (vsys_name)  | PanOSVsysName  | vSrcName  |  | target.asset.attribute.labels.key/value  
intermediary.asset.attribute.labels.key/value   
Device Name (device_name)  | dvchost  | DeviceName  |  | target.hostname  
intermediary.hostname   
Device Group (dg_id)  | PanOSFWDeviceGroup  |  | dg_id  | target.asset.attribute.labels.key/value   
Audit Comment (comment)  | PanOSPolicyAuditComment  |  | comment  | additional.fields.key and additional.fields.value.string_value   
High Resolution Timestamp (high_res_timestamp)  |  |  |  | additional.fields.key and additional.fields.value.string_value   
Severity (severity)  | number-of-severity(header)  |  |  | security_result.severity and security_result.severity_details   
  
### Threat/WildFire

The following table lists the log fields of the Threat/WildFire log type and their corresponding UDM fields.

CSV field | CEF field | LEEF field | Google Security Operations label key | UDM field  
---|---|---|---|---  
Receive Time (receive_time or cef-formatted-receive_time)  | rt  | devTime  |  | metadata.collected_timestamp,  metadata.event_timestamp (if "Generate Time" is absent)   
Serial Number (serial #)  | deviceExternalId  | SerialNumber  |  | intermediary.asset.hardware.serial_number   
Type (type)  | type (Header)  | cat  |  | metadata.product_event_type   
Threat/Content Type (subtype)  | cat/subtype (Header)  | Subtype  |  | metadata.product_event_type   
Generate Time (time_generated or cef-formatted-time_generated)  |  |  |  | metadata.event_timestamp   
Source address (src)  | src  | src  |  | principal.ip   
Destination address (dst)  | dst  | dst  |  | target.ip   
NAT Source IP (natsrc)  | sourceTranslatedAddress  | srcPostNAT  |  | principal.nat_ip   
NAT Destination IP (natdst)  | destinationTranslatedAddress  | dstPostNAT  |  | target.nat_ip   
Rule Name (rule)  | cs1  | RuleName  |  | security_result.rule_name   
Source User (srcuser)  | suser  | SourceUser / usrName  |  | principal.user.userid   
Destination User (dstuser)  | duser  | DestinationUser  |  | target.user.userid   
Application (app)  | app  | Application  |  | target.application   
Virtual System (vsys)  | cs3  | VirtualSystem  | vsys  | intermediary.asset.attribute.labels.key/value   
Source Zone (from)  | cs4  | SourceZone  | from  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Destination Zone (to)  | cs5  | DestinationZone  | to  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Inbound Interface (inbound_if)  | deviceInboundInterface  | IngressInterface  | inbound_if  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Outbound Interface (outbound_if)  | deviceOutboundInterface  | EgressInterface  | outbound_if  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Log Action (logset)  | cs6  | LogForwardingProfile  | logset  | additional.fields.key and additional.fields.value.string_value   
Session ID (sessionid)  | cn1  | SessionID  |  | network.session_id   
Repeat Count (repeatcnt)  | cnt  | RepeatCount  | repeatcnt  | additional.fields.key and additional.fields.value.string_value   
Source Port (sport)  | spt  | srcPort  |  | principal.port   
Destination Port (dport)  | dpt  | dstPort  |  | target.port   
NAT Source Port (natsport)  | sourceTranslatedPort  | srcPostNATPort  |  | principal.nat_port   
NAT Destination Port (natdport)  | destinationTranslatedPort  | dstPostNATPort  |  | target.nat_port   
Flags (flags)  | flexString1  | Flags  | flags  | additional.fields.key and additional.fields.value.string_value   
IP Protocol (proto)  | proto  | proto  |  | network.ip_protocol   
Action (action)  | act  | action  |  | security_result.action_details  security_result.action   
URL/Filename (misc)  | request  | Miscellaneous  |  | target.file.names (if subtype is 'file', 'virus', 'wildfire-virus', or 'wildfire' then `misc` field is mapped to target.file.names) target.url (if subtype is 'url' then `misc` field is mapped to target.url and target.hostname)  
Threat/Content Name (threatid)  | cat  | ThreatID  |  | security_result.threat_name   
Category (category)  | cs2  | URLCategory  |  | security_result.category_details   
Severity (severity)  | number-of-severity(header)  | Severity  |  | security_result.severity and security_result.severity_details   
Direction (direction)  | flexString2  | Direction  |  | network.direction   
Sequence Number (seqno)  | externalId  | sequence  |  | metadata.product_log_id   
Action Flags (actionflags)  | PanOSActionFlags  | ActionFlags  | actionflags  | additional.fields.key and additional.fields.value.string_value   
Source Country (srcloc)  |  | SourceLocation  |  | principal.location.country_or_region   
Destination Country (dstloc)  |  | DestinationLocation  |  | target.location.country_or_region   
Content Type (contenttype)  |  | ContentType  | contenttype  | additional.fields.key and additional.fields.value.string_value   
PCAP ID (pcap_id)  | fileId  | PCAP_ID  | pcap_id  | additional.fields.key and additional.fields.value.string_value   
File Digest (filedigest)  | fileHash  | FileDigest  |  | target.file.sha1/md5/sha256   
Cloud (cloud)  | filePath  | Cloud  | cloud  | additional.fields.key and additional.fields.value.string_value   
URL Index (url_idx)  |  | URLIndex  | url_idx  | additional.fields.key and additional.fields.value.string_value   
User Agent (user_agent)  |  |  |  | network.http.user_agent   
File Type (filetype)  | fileType  | FileType  |  | target.file.mime_type   
X-Forwarded-For (xff)  |  |  |  | principal.ip   
Referer (referer)  |  |  |  | network.http.referral_url   
Sender (sender)  | suid  | Sender  |  | network.email.from   
Subject (subject)  | msg  | Subject  |  | network.email.subject   
Recipient (recipient)  | duid  | Recipient  |  | network.email.to   
Report ID (reportid)  | oldFileId  | ReportID  | reportid  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_1 to dg_hier_level_4)  | PanOSDGl1  | DeviceGroupHierarchyL1  | dg_hier_level_1  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_2)  | PanOSDGl2  | DeviceGroupHierarchyL2  | dg_hier_level_2  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_3)  | PanOSDGl3  | DeviceGroupHierarchyL3  | dg_hier_level_3  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_4)  | PanOSDGl4  | DeviceGroupHierarchyL4  | dg_hier_level_4  | additional.fields.key and additional.fields.value.string_value   
Virtual System Name (vsys_name)  | PanOSVsysName  | vSrcName  |  | intermediary.asset.attribute.labels.key/value   
Device Name (device_name)  | dvchost  | DeviceName  |  | intermediary.hostname intermediary.asset.hostname target.hostname target.asset.hostname  
Source VM UUID (src_uuid)  | PanOSSrcUUID  | SrcUUID  |  | principal.asset.product_object_id   
Destination VM UUID (dst_uuid)  | PanOSDstUUID  | DstUUID  |  | target.asset.product_object_id   
HTTP Method (http_method)  |  | RequestMethod  |  | network.http.method   
Tunnel ID/IMSI (tunnel_id/imsi)  | PanOSTunnelID  | TunnelID  | tunnel_id/imsi  | additional.fields.key and additional.fields.value.string_value   
Monitor Tag/IMEI (monitortag/imei)  | PanOSMonitorTag  | MonitorTag  | monitortag/imei  | additional.fields.key and additional.fields.value.string_value   
Parent Session ID (parent_session_id)  | PanOSParentSessionID  | ParentSessionID  | parent_session_id  | network.parent_session_id   
Parent Session Start Time (parent_start_time)  | PanOSParentStartTime  | ParentStartTime  | parent_start_time  | additional.fields.key and additional.fields.value.string_value   
Tunnel Type (tunnel)  | PanOSTunnelType  | TunnelType  | tunnel  | additional.fields.key and additional.fields.value.string_value   
Threat Category (thr_category)  | PanOSThreatCategory  | ThreatCategory  | thr_category  | security_result.detection_fields.key/value   
Content Version (contentver)  | PanOSContentVer  | ContentVer  | contentver  | additional.fields.key and additional.fields.value.string_value   
SCTP Association ID (assoc_id)  | PanOSAssocID  |  | assoc_id  | additional.fields.key and additional.fields.value.string_value   
Payload Protocol ID (ppid)  | PanOSPPID  |  | ppid  | additional.fields.key and additional.fields.value.string_value   
HTTP Headers (http_headers)  | PanOSHTTPHeader  |  | http_headers  | target.url.last_http_response_headers   
URL Category List (url_category_list)  | PanOSURLCatList  |  | url_category_list  | additional.fields.key and additional.fields.value.string_value   
Rule UUID (rule_uuid)  | PanOSRuleUUID  |  |  | security_result.rule_id   
HTTP/2 Connection (http2_connection)  | PanOSHTTP2Con  |  | http2_connection  | network.application_protocol_version   
Dynamic User Group Name (dynusergroup_name)  | PanDynamicUsrgrp  |  | dynusergroup_name  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
XFF Address (xff_ip)  | PanXFFIP  |  |  | principal.ip   
Source Device Category (src_category)  | PanSrcDeviceCat  |  | src_category  | principal.asset.category   
Source Device Profile (src_profile)  | PanSrcDeviceProf  |  | src_profile  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Source Device Model (src_model)  | PanSrcDeviceModel  |  | src_model  | principal.asset.hardware.model   
Source Device Vendor (src_vendor)  | PanSrcDeviceVendor  |  | src_vendor  | principal.asset.hardware.manufacturer   
Source Device OS Family (src_osfamily)  | PanSrcDeviceOS  |  | src_osfamily  | principal.platform   
Source Device OS Version (src_osversion)  | PanSrcDeviceOSv  |  |  | principal.platform_version   
Source Hostname (src_host)  | PanSrcHostname  |  |  | principal.hostname   
Source MAC Address (src_mac)  | PanSrcMac  |  |  | principal.mac   
Destination Device Category (dst_category)  | PanDstDeviceCat  |  | dst_category  | target.asset.category   
Destination Device Profile (dst_profile)  | PanDstDeviceProf  |  | dst_profile  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Destination Device Model (dst_model)  | PanDstDeviceModel  |  | dst_model  | target.asset.hardware.model   
Destination Device Vendor (dst_vendor)  | PanDstDeviceVendor  |  | dst_vendor  | target.asset.hardware.manufacturer   
Destination Device OS Family (dst_osfamily)  | PanDstDeviceOS  |  | dst_osfamily  | target.platform   
Destination Device OS Version (dst_osversion)  | PanDstDeviceOSv  |  |  | target.platform_version   
Destination Hostname (dst_host)  | PanDstHostname  |  |  | target.hostname   
Destination MAC Address (dst_mac)  | PanDstMac  |  |  | target.mac   
Container ID (container_id)  | PanContainerName  |  | container_id  | intermediary.resource.product_object_id   
POD Namespace (pod_namespace)  | PanPODNamespace  |  | pod_namespace  | target.resource.attribute.labels.key/value   
POD Name (pod_name)  | PanPODName  |  | pod_name  | target.resource.name   
Source External Dynamic List (src_edl)  | PanSrcEDL  |  | src_edl  | additional.fields.key and additional.fields.value.string_value   
Destination External Dynamic List (dst_edl)  | PanDstEDL  |  | dst_edl  | additional.fields.key and additional.fields.value.string_value   
Host ID (hostid)  | PanGPHostID  |  | hostid  | principal.asset.asset_id   
User Device Serial Number (serialnumber)  | PanEPSerial  |  |  | principal.asset.hardware.serial_number   
Domain EDL (domain_edl)  | PanDomainEDL  |  | domain_edl  | additional.fields.key and additional.fields.value.string_value   
Source Dynamic Address Group (src_dag)  | PanSrcDAG  |  |  | principal.group.group_display_name   
Destination Dynamic Address Group (dst_dag)  | PanDstDAG  |  |  | target.group.group_display_name   
Partial Hash (partial_hash)  | PanPartialHash  |  | partial_hash  | additional.fields.key and additional.fields.value.string_value   
High Resolution Timestamp (high_res timestamp)  | PanTimeHighRes  |  | high_res timestamp  | additional.fields.key and additional.fields.value.string_value   
Reason (reason)  | PanReasonFilteringAction  |  | reason  | security_result.summary   
Justification (justification)  | PanJustification  |  | justification  | additional.fields.key and additional.fields.value.string_value   
A Slice Service Type (nssai_sst)  | PanASServiceType  |  | nssai_sst  | additional.fields.key and additional.fields.value.string_value   
Application Subcategory (subcategory_of_app)  |  |  | subcategory_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Category (category_of_app)  |  |  | category_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Technology (technology_of_app)  |  |  | technology_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Risk (risk_of_app)  |  |  | risk_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Characteristic (characteristic_of_app)  |  |  | characteristic_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Container (container_of_app)  |  |  | container_of_app  | additional.fields.key and additional.fields.value.string_value   
Application SaaS (is_saas_of_app)  |  |  | is_saas_of_app  | additional.fields.key and additional.fields.value.string_value   
Tunneled Application (tunneled_app)  |  |  |  | additional.fields.key and additional.fields.value.string_value   
Flow Type (flow_type)  |  |  |  | additional.fields.key and additional.fields.value.string_value   
Cluster Name (cluster_name)  |  |  |  | intermediary.resource.name   
Application Sanctioned State (sanctioned_state_of_app)  |  |  | sanctioned_state_of_app  | additional.fields.key and additional.fields.value.string_value   
  
### Traffic

The following table lists the log fields of the traffic log type and their corresponding UDM fields.

CSV field | CEF field | LEEF field | Google Security Operations label key | UDM field  
---|---|---|---|---  
Receive Time (receive_time or cef-formatted-receive_time)  | rt  | devTime  |  | metadata.collected_timestamp,  metadata.event_timestamp (if "Generate Time" is absent)   
Serial Number (serial)  | deviceExternalId  | SerialNumber  |  | intermediary.asset.hardware.serial_number   
Type (type)  | type (Header)  | cat/Type  |  | metadata.product_event_type   
Threat/Content Type (subtype)  | subtype (Header)  | Subtype  |  | metadata.product_event_type   
Generated Time (time_generated or cef-formatted-time_generated)  | start  |  |  | metadata.event_timestamp   
Source Address (src)  | src  | src  |  | principal.ip   
Destination Address (dst)  | dst  | dst  |  | target.ip   
NAT Source IP (natsrc)  | sourceTranslatedAddress  | srcPostNAT  |  | principal.nat_ip   
NAT Destination IP (natdst)  | destinationTranslatedAddress  | dstPostNAT  |  | target.nat_ip   
Rule Name (rule)  | cs1  | RuleName  |  | security_result.rule_name   
Source User (srcuser)  | suser  | SourceUser  |  | principal.user.userid   
Destination User (dstuser)  | duser  | DestinationUser  |  | target.user.userid   
Application (app)  | app  | Application  |  | target.application   
Virtual System (vsys)  | cs3  | VirtualSystem  | vsys  | intermediary.asset.attribute.labels.key/value   
Source Zone (from)  | cs4  | SourceZone  | from  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Destination Zone (to)  | cs5  | DestinationZone  | to  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Inbound Interface (inbound_if)  | deviceInboundInterface  | IngressInterface  | inbound_if  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Outbound Interface (outbound_if)  | deviceOutboundInterface  | EgressInterface  | outbound_if  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Log Action (logset)  | cs6  | LogForwardingProfile  | logset  | additional.fields.key and additional.fields.value.string_value   
Session ID (sessionid)  | cn1  | SessionID  |  | network.session_id   
Repeat Count (repeatcnt)  | cnt  | RepeatCount  | repeatcnt  | additional.fields.key and additional.fields.value.string_value   
Source Port (sport)  | spt  | srcPort  |  | principal.port   
Destination Port (dport)  | dpt  | dstPort  |  | target.port   
NAT Source Port (natsport)  | sourceTranslatedPort  | srcPostNATPort  |  | principal.nat_port   
NAT Destination Port (natdport)  | destinationTranslatedPort  | dstPostNATPort  |  | target.nat_port   
Flags (flags)  | flexString1  | Flags  | flags  | additional.fields.key and additional.fields.value.string_value   
IP Protocol (proto)  | proto  | proto  |  | network.ip_protocol   
Action (action)  | act  | action  |  | security_result.action_details  security_result.action   
Bytes (bytes)  | flexNumber1  | totalBytes  | bytes  | additional.fields.key and additional.fields.value.string_value   
Bytes Sent (bytes_sent)  | in  | srcBytes  |  | network.sent_bytes   
Bytes Received (bytes_received)  | out  | dstBytes  |  | network.received_bytes   
Packets (packets)  | cn2  | totalPackets  | packets  | additional.fields.key and additional.fields.value.string_value   
Start Time (start)  |  | StartTime  | start  | additional.fields.key and additional.fields.value.string_value   
Elapsed Time (elapsed)  | cn3  | ElapsedTime  | elapsed  | network.session_duration.seconds   
Category (category)  | cs2  | URLCategory  |  | security_result.category / security_result.category_details   
Sequence Number (seqno)  | externalId  | sequence  |  | metadata.product_log_id   
Action Flags (actionflags)  | PanOSActionFlags  | ActionFlags  | actionflags  | additional.fields.key and additional.fields.value.string_value   
Source Country (srcloc)  |  | SourceLocation  |  | principal.location.country_or_region   
Destination Country (dstloc)  |  | DestinationLocation  |  | target.location.country_or_region   
Packets Sent (pkts_sent)  | PanOSPacketsSent  | srcPackets  | pkts_sent  | network.sent_packets   
Packets Received (pkts_received)  | PanOSPacketsReceived  | dstPackets  | pkts_received  | network.received_packets   
Session End Reason (session_end_reason)  | reason  | SessionEndReason  |  | security_result.summary   
Device Group Hierarchy1 (dg_hier_level_1 to dg_hier_level_4)  | PanOSDGl1  | DeviceGroupHierarchyL1  | dg_hier_level_1  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy2 (dg_hier_level_2)  | PanOSDGl2  | DeviceGroupHierarchyL2  | dg_hier_level_2  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy3 (dg_hier_level_3)  | PanOSDGl3  | DeviceGroupHierarchyL3  | dg_hier_level_3  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_4)  | PanOSDGl4  | DeviceGroupHierarchyL4  | dg_hier_level_4  | additional.fields.key and additional.fields.value.string_value   
Virtual System Name (vsys_name)  | PanOSVsysName  | vSrcName  |  | intermediary.asset.attribute.labels.key/value   
Device Name (device_name)  | dvchost  | DeviceName  |  | intermediary.hostname intermediary.asset.hostname  
Action Source (action_source)  | cat  | ActionSource  | action_source  | additional.fields.key and additional.fields.value.string_value   
Source VM UUID (src_uuid)  | PanOSSrcUUID  | SrcUUID  |  | principal.asset.product_object_id   
Destination VM UUID (dst_uuid)  | PanOSDstUUID  | DstUUID  |  | target.asset.product_object_id   
Tunnel ID/IMSI (tunnelid/imsi)  | PanOSTunnelID  | TunnelID  | tunnelid/imsi  | additional.fields.key and additional.fields.value.string_value   
Monitor Tag/IMEI (monitortag/imei)  | PanOSMonitorTag  | MonitorTag  | monitortag/imei  | additional.fields.key and additional.fields.value.string_value   
Parent Session ID (parent_session_id)  | PanOSParentSessionID  | ParentSessionID  | parent_session_id  | network.parent_session_id   
Parent Start Time (parent_start_time)  | PanOSParentStartTime  | ParentStartTime  | parent_start_time  | additional.fields.key and additional.fields.value.string_value   
Tunnel Type (tunnel)  | PanOSTunnelType  | TunnelType  | tunnel  | additional.fields.key and additional.fields.value.string_value   
SCTP Association ID (assoc_id)  | PanOSSCTPAssocID  |  | assoc_id  | additional.fields.key and additional.fields.value.string_value   
SCTP Chunks (chunks)  | PanOSSCTPChunks  |  | chunks  | additional.fields.key and additional.fields.value.string_value   
SCTP Chunks Sent (chunks_sent)  | PanOSSCTPChunkSent  |  | chunks_sent  | additional.fields.key and additional.fields.value.string_value   
SCTP Chunks Received (chunks_received)  | PanOSSCTPChunksRcv  |  | chunks_received  | additional.fields.key and additional.fields.value.string_value   
Rule UUID (rule_uuid)  | PanOSRuleUUID  |  |  | security_result.rule_id   
HTTP/2 Connection (http2_connection)  | PanOSHTTP2Con  |  | http2_connection  | network.application_protocol_version   
App Flap Count (link_change_count)  | PanLinkChange  |  | link_change_count  | additional.fields.key and additional.fields.value.string_value   
Policy ID (policy_id)  | PanPolicyID  |  | policy_id  | additional.fields.key and additional.fields.value.string_value   
Link Switches (link_switches)  | PanLinkDetail  |  | link_switches  | additional.fields.key and additional.fields.value.string_value   
SD-WAN Cluster (sdwan_cluster)  | PanSDWANCluster  |  | sdwan_cluster  | additional.fields.key and additional.fields.value.string_value   
SD-WAN Device Type (sdwan_device_type)  | PanSDWANDevice  |  | sdwan_device_type  | additional.fields.key and additional.fields.value.string_value   
SD-WAN Cluster Type (sdwan_cluster_type)  | PanSDWANClustype  |  | sdwan_cluster_type  | additional.fields.key and additional.fields.value.string_value   
SD-WAN Site (sdwan_site)  | PanSDWANSite  |  | sdwan_site  | additional.fields.key and additional.fields.value.string_value   
Dynamic User Group Name (dynusergroup_name)  | PanDynamicUsrgrp  |  | dynusergroup_name  | additional.fields.key and additional.fields.value.string_value   
XFF Address (xff_ip)  | PanXFFIP  |  |  | principal.ip   
Source Device Category (src_category)  | PanSrcDeviceCat  |  | src_category  | principal.asset.category   
Source Device Profile (src_profile)  | PanSrcDeviceProf  |  | src_profile  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Source Device Model (src_model)  | PanSrcDeviceModel  |  | src_model  | principal.asset.hardware.model   
Source Device Vendor (src_vendor)  | PanSrcDeviceVendor  |  | src_vendor  | principal.asset.hardware.manufacturer   
Source Device OS Family (src_osfamily)  | PanSrcDeviceOS  |  |  | principal.platform   
Source Device OS Version (src_osversion)  | PanSrcDeviceOSv  |  |  | principal.asset.software.version   
Source Hostname (src_host)  | PanSrcHostname  |  |  | principal.hostname   
Source MAC Address (src_mac)  | PanSrcMac  |  |  | principal.mac   
Destination Device Category (dst_category)  | PanDstDeviceCat  |  | dst_category  | target.asset.category   
Destination Device Profile (dst_profile)  | PanDstDeviceProf  |  | dst_profile  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Destination Device Model (dst_model)  | PanDstDeviceModel  |  | dst_model  | target.asset.hardware.model   
Destination Device Vendor (dst_vendor)  | PanDstDeviceVendor  |  | dst_vendor  | target.asset.hardware.manufacturer   
Destination Device OS Family (dst_osfamily)  | PanDstDeviceOS  |  | dst_osfamily  | target.platform   
Destination Device OS Version (dst_osversion)  | PanDstDeviceOSv  |  |  | target.platform_version   
Destination Hostname (dst_host)  | PanDstHostname  |  |  | target.hostname   
Destination MAC Address (dst_mac)  | PanDstMac  |  |  | target.mac   
Container ID (container_id)  | PanContainerName  |  | container_id  | intermediary.resource.product_object_id   
POD Namespace (pod_namespace)  | PanPODNamespace  |  | pod_namespace  | target.resource.attribute.labels.key/value   
POD Name (pod_name)  | PanPODName  |  | pod_name  | target.resource.name   
Source External Dynamic List (src_edl)  | PanSrcEDL  |  | src_edl  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Destination External Dynamic List (dst_edl)  | PanDstEDL  |  | dst_edl  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Host ID (hostid)  | PanGPHostID  |  | hostid  | principal.asset.asset_id   
User Device Serial Number (serialnumber)  | PanEPSerial  |  |  | principal.asset.hardware.serial_number   
Source Dynamic Address Group (src_dag)  | PanSrcDAG  |  |  | principal.group.group_display_name   
Destination Dynamic Address Group (dst_dag)  | PanDstDAG  |  |  | target.group.group_display_name   
Session Owner (session_owner)  | PanHASessionOwner  |  | session_owner  | additional.fields.key and additional.fields.value.string_value   
High Resolution Timestamp (high_res_timestamp)  | PanTimeHighRes  |  |  | additional.fields.key and additional.fields.value.string_value   
A Slice Service Type (nsdsai_sst)  | PanASServiceType  |  | nsdsai_sst  | additional.fields.key and additional.fields.value.string_value   
A Slice Differentiator (nsdsai_sd)  | PanASServiceDiff  |  | nsdsai_sd  | additional.fields.key and additional.fields.value.string_value   
Application Subcategory (subcategory_of_app)  |  |  | subcategory_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Category (category_of_app)  |  |  | category_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Technology (technology_of_app)  |  |  | technology_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Risk (risk_of_app)  |  |  |  | security_result.severity   
Application Characteristic (characteristic_of_app)  |  |  | characteristic_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Container (container_of_app)  |  |  | container_of_app  | additional.fields.key and additional.fields.value.string_value   
Application SaaS (is_saas_of_app)  |  |  | is_saas_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Sanctioned State (sanctioned_state_of_app)  |  |  | sanctioned_state_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Subcategory (subcategory_of_app)  |  |  | subcategory_of_app1  | additional.fields.key and additional.fields.value.string_value   
Severity (severity)  | number-of-severity(header)  |  |  | security_result.severity and security_result.severity_details   
  
### User-ID

The following table lists the log fields of the user-id log type and their corresponding UDM fields.

CSV field | CEF field | LEEF field | Google Security Operations label key | UDM field  
---|---|---|---|---  
Receive Time (receive_time or cef-formatted-receive_time)  | rt  | devTime  |  | metadata.collected_timestamp,  metadata.event_timestamp (if "Generate Time" is absent)   
Serial Number (serial)  | deviceExternalId  | SerialNumber  |  | intermediary.asset.hardware.serial_number   
Type (type)  | type (Header)  | cat  |  | metadata.product_event_type   
Threat/Content Type (subtype)  | subtype (Header)  | Subtype  |  | metadata.product_event_type   
Generated Time (time_generated or cef-formatted-time_generated)  |  |  |  | metadata.event_timestamp   
Virtual System (vsys)  | cs3  | VirtualSystem  | vsys  | intermediary.asset.attribute.labels.key/value   
Source IP (ip)  | src  | src  |  | principal.ip   
User (user)  | duser  | usrName  |  | target.user.userid  target.administrative_domain  target.user.email_addresses   
Data Source Name (datasourcename)  | cs4  | DataSourceName  | datasourcename  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Event ID (eventid)  |  | EventID  | eventid  | additional.fields.key and additional.fields.value.string_value   
Repeat Count (repeatcnt)  | cnt  | RepeatCount  | repeatcnt  | additional.fields.key and additional.fields.value.string_value   
Time Out Threshold (timeout)  | cn3  | TimeoutThreshold  | timeout  | additional.fields.key and additional.fields.value.string_value   
Source Port (beginport)  | spt  | srcPort  |  | principal.port   
Destination Port (endport)  | dpt  | dstPort  |  | target.port   
Data Source (datasource)  | cs5  | DataSource  | datasource  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Data Source Type (datasourcetype)  | cs6  | DataSourceType  | datasourcetype  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Sequence Number (seqno)  | externalId  | sequence  |  | metadata.product_log_id   
Action Flags (actionflags)  | PanOSActionFlags  | ActionFlags  | actionflags  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_1)  | PanOSDGl1  | DeviceGroupHierarchyL1  | dg_hier_level_1  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_2)  | PanOSDGl2  | DeviceGroupHierarchyL2  | dg_hier_level_2  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_3)  | PanOSDGl3  | DeviceGroupHierarchyL3  | dg_hier_level_3  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_4)  | PanOSDGl4  | DeviceGroupHierarchyL4  | dg_hier_level_4  | additional.fields.key and additional.fields.value.string_value   
Virtual System Name (vsys_name)  | PanOSVsysName  | vSrcName  |  | intermediary.asset.attribute.labels.key/value   
Device Name (device_name)  | dvchost  | DeviceName  |  | intermediary.hostname   
Virtual System ID (vsys_id)  | cn2  | VirtualSystemID  |  | intermediary.resource.product_object_id   
Factor Type (factortype)  | cs1  | FactorType  | factortype  | additional.fields.key and additional.fields.value.string_value   
Factor Completion Time (factorcompletiontime)  | end  | FactorCompletionTime  | factorcompletiontime  | additional.fields.key and additional.fields.value.string_value   
Factor Number (factorno)  | cn1  | FactorNumber  | factorno  | additional.fields.key and additional.fields.value.string_value   
User Group Flags (ugflags)  | PanOSUGFlags  |  | ugflags  | additional.fields.key and additional.fields.value.string_value   
User by Source (userbysource)  | PanOSUserBySource  |  |  | additional.fields,  target.user.userid (if "duser" is absent)   
High Resolution Timestamp (high_res timestamp)  | PanOSTimeGeneratedHighResolution  |  |  | additional.fields.key and additional.fields.value.string_value   
Origin Data Source (origindatasource)  |  |  |  | additional.fields.key and additional.fields.value.string_value   
Cluster Name (cluster_name)  |  |  |  | principal.resource.name   
Severity (severity)  | number-of-severity(header)  |  |  | security_result.severity and security_result.severity_details   
  
### HIP match

The following table lists the log fields of the HIP match log type and their corresponding UDM fields.

CSV field | CEF field | LEEF field | Google Security Operations label key | UDM field  
---|---|---|---|---  
Receive Time (receive_time or cef-formatted-receive_time)  | rt  | devTime  |  | metadata.collected_timestamp,  metadata.event_timestamp (if "Generate Time" is absent)   
Serial Number (serial)  | deviceExternalId  | SerialNumber  |  | target.asset.hardware.serial_number  
intermediary.asset.hardware.serial_number   
Type (type)  | type (Header)  | cat  |  | metadata.product_event_type   
Threat/Content Type (subtype)  | subtype (Header)  | Subtype  |  |   
Generated Time (time_generated or cef-formatted-time_generated)  | start  | startTime  |  | metadata.event_timestamp   
Source User (srcuser)  | suser  | usrName  |  | principal.user.userid   
Virtual System (vsys)  | cs3  | VirtualSystem  | vsys  | target.asset.attribute.labels.key/value  
intermediary.asset.attribute.labels.key/value   
Machine Name (machinename)  | shost  | identHostName  |  | principal.hostname   
Operating System (os)  | cs2  | OS  |  | principal.asset.platform_software.platform   
Source Address (src)  | src  | identsrc  |  | principal.ip   
HIP (matchname)  | cat  | HIP  | matchname  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Repeat Count (repeatcnt)  | cnt  | RepeatCount  | repeatcnt  | additional.fields.key and additional.fields.value.string_value   
HIP Type (matchtype)  | Device Event Class ID (Header)  | HIPType  | matchtype  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Sequence Number (seqno)  | externalId  | sequence  |  | metadata.product_log_id   
Action Flags (actionflags)  | PanOSActionFlags  | ActionFlags  | actionflags  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_1)  | PanOSDGl1  | DeviceGroupHierarchyL1  | dg_hier_level_1  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_2)  | PanOSDGl2  | DeviceGroupHierarchyL2  | dg_hier_level_2  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_3)  | PanOSDGl3  | DeviceGroupHierarchyL3  | dg_hier_level_3  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_4)  | PanOSDGl4  | DeviceGroupHierarchyL4  | dg_hier_level_4  | additional.fields.key and additional.fields.value.string_value   
Virtual System Name (vsys_name)  | PanOSVsysName  | vSrcName  |  | target.asset.attribute.labels.key/value  
intermediary.asset.attribute.labels.key/value   
Device Name (device_name)  | dvchost  | DeviceName  |  | target.hostname  
intermediary.hostname   
Virtual System ID (vsys_id)  | cn2  | VirtualSystemID  |  | target.resource.product_object_id  
intermediary.resource.product_object_id   
IPv6 System Address (srcipv6)  | c6a2  | srcipv6  |  | principal.asset.ip   
Host ID (hostid)  | PanOSHostID  |  |  | principal.asset.asset_id   
User Device Serial Number (serialnumber)  | PanOSEndpointSerialNumber  |  |  | principal.asset.hardware.serial_number   
Device MAC Address (mac)  | PanOSEndpointMac  |  |  | principal.asset.mac   
High Resolution Timestamp (high_res_timestamp)  | PanOSTimeGeneratedHighResolution  |  |  | additional.fields.key and additional.fields.value.string_value   
Cluster Name (cluster_name)  |  |  |  | principal.resource.name   
Severity (severity)  | number-of-severity(header)  |  |  | security_result.severity and security_result.severity_details   
  
### IP tag

The following table lists the log fields of the IP tag log type and their corresponding UDM fields.

CSV field | CEF field | LEEF field | Google Security Operations label key | UDM field  
---|---|---|---|---  
Receive Time (receive_time or cef-formatted-receive_time)  | rt  | devTime  |  | metadata.collected_timestamp,  metadata.event_timestamp (if "Generate Time" is absent)   
Serial Number (serial)  | deviceExternalId  | SerialNumber  |  | target.asset.hardware.serial_number  
intermediary.asset.hardware.serial_number   
Type (type)  | type (Header)  | cat  |  | metadata.product_event_type   
Threat/Content Type (subtype)  | subtype (Header)  | Subtype  |  | metadata.product_event_type   
Generated Time (time_generated or cef-formatted-time_generated)  |  | GenerateTime  |  | metadata.event_timestamp   
Virtual System (vsys)  | cs3  | VirtualSystem  | vsys  | target.asset.attribute.labels.key/value  
intermediary.asset.attribute.labels.key/value   
Source IP (ip)  | src  | src  |  | principal.ip   
Tag Name (tag_name)  | PanOSTagName  | TagName  | tag_name  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Event ID (event_id)  | PanOSEventID  | EventID  | event_id  | additional.fields.key and additional.fields.value.string_value   
Repeat Count (repeatcnt)  | cnt  | RepeatCount  | repeatcnt  | additional.fields.key and additional.fields.value.string_value   
Timeout (timeout)  | PanOSTimeout  | TimeoutThreshold  | timeout  | additional.fields.key and additional.fields.value.string_value   
Data Source Name (datasourcename)  | PanOSDataSourceName  | DataSourceName  | datasourcename  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Data Source Type (datasource_type)  | PanOSDataSourceType  | DataSource  | datasource_type  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Data Source Subtype (datasource_subtype)  | PanOSDataSourceSubType  | DataSourceType  | datasource_subtype  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Sequence Number (seqno)  | externalId  | sequence  |  | metadata.product_log_id   
Action Flags (actionflags)  | PanOSActionFlags  | ActionFlags  | actionflags  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_1)  | PanOSDGl1  | DeviceGroupHierarchyL1  | dg_hier_level_1  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_2)  | PanOSDGl2  | DeviceGroupHierarchyL2  | dg_hier_level_2  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_3)  | PanOSDGl3  | DeviceGroupHierarchyL3  | dg_hier_level_3  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_4)  | PanOSDGl4  | DeviceGroupHierarchyL4  | dg_hier_level_4  | additional.fields.key and additional.fields.value.string_value   
Virtual System Name (vsys_name)  | PanOsVsysName  | vSrcName  |  | target.asset.attribute.labels.key/value  
intermediary.asset.attribute.labels.key/value   
Device Name (device_name)  | dvchost  | DeviceName  |  | target.hostname  
intermediary.hostname   
Virtual System ID (vsys_id)  | cn2  | VirtualSystemID  |  | target.resource.product_object_id  
intermediary.resource.product_object_id   
High Resolution Timestamp (high_res timestamp)  | PanOSTimeGeneratedHighResolution  |  |  | additional.fields.key and additional.fields.value.string_value   
Severity (severity)  | number-of-severity(header)  |  |  | security_result.severity and security_result.severity_details   
Cluster Name (cluster_name)  |  |  |  | principal.resource.name   
  
### Decryption

The following table lists the log fields of the decryption log type and their corresponding UDM fields.

CSV field | CEF field | LEEF field | Google Security Operations label key | UDM field  
---|---|---|---|---  
Receive Time (receive_time or cef-formatted-receive_time)  | rt  |  |  | metadata.collected_timestamp,  metadata.event_timestamp (if "Generate Time" is absent)   
Serial Number (serial)  | PanOSDeviceSN  |  |  | intermediary.asset.hardware.serial_number   
Type (type)  | type (Header)  |  |  | metadata.product_event_type   
Threat/Content Type (subtype)  | subtype (Header)  |  |  | metadata.product_event_type   
Config Version (config_ver)  | PanOSConfigVersion  |  | config_ver  | additional.fields.key and additional.fields.value.string_value   
Generate Time (time_generated)  | PanOSLogTimeStamp  |  |  | metadata.event_timestamp   
Source Address (src)  | src  |  |  | principal.ip   
Destination Address (dst)  | dst  |  |  | target.ip   
NAT Source IP (natsrc)  | sourceTranslatedAddress  |  |  | principa.nat_ip   
NAT Destination IP (natdst)  | destinationTranslatedAddress  |  |  | target.nat_ip   
Rule (rule)  | cs1  |  |  | security_result.rule_name   
Source User (srcuser)  | suser  |  |  | principal.user.userid   
Destination User (dstuser)  | duser  |  |  | target.user.userid   
Application (app)  | app  |  |  | network.application_protocol   
Virtual System (vsys)  | cs3  |  | vsys  | intermediary.asset.attribute.labels.key/value   
Source Zone (from)  | cs4  |  | from  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Destination Zone (to)  | cs5  |  | to  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Inbound Interface (inbound_if)  | deviceInboundInterface  |  | inbound_if  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Outbound Interface (outbound_if)  | deviceOutboundInterface  |  | outbound_if  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Log Action (logset)  | cs6  |  | logset  | additional.fields.key and additional.fields.value.string_value   
Time Logged (time_received)  | PanOSTimeReceivedManagementPlane  |  |  | \-   
Session ID (sessionid)  | cn1  |  |  | network.session_id   
Repeat Count (repeatcnt)  | PanOSCountOfRepeats/RepeatCount  |  | repeatcnt  | additional.fields.key and additional.fields.value.string_value   
Source Port (sport)  | spt  |  |  | principal.port   
Destination Port (dport)  | dpt  |  |  | target.port   
NAT Source Port (natsport)  | sourceTranslatedPort  |  |  | principal.nat_port   
NAT Destination Port (natdport)  | destinationTranslatedPort  |  |  | target.nat_port   
Flags (flags)  | flexString1  |  | flags  | additional.fields.key and additional.fields.value.string_value   
IP Protocol (proto)  | proto  |  |  | network.ip_protocol   
Action (action)  | act  |  |  | security_result.action_details  security_result.action   
Tunnel (tunnel)  | PanOSTunnel  |  | tunnel  | additional.fields.key and additional.fields.value.string_value   
Source VM UUID (src_uuid)  | PanOSSourceUUID  |  |  | principal.asset.product_object_id   
Destination VM UUID (dst_uuid)  | PanOSDestinationUUID  |  |  | target.asset.product_object_id   
UUID for rule (rule_uuid)  | PanOSRuleUUID  |  |  | security_result.rule_id   
Stage for Client to Firewall (hs_stage_c2f)  | PanOSClientToFirewall  |  | hs_stage_c2f  | additional.fields.key and additional.fields.value.string_value   
Stage for Firewall to Server (hs_stage_f2s)  | PanOSFirewallToServer  |  | hs_stage_f2s  | additional.fields.key and additional.fields.value.string_value   
TLS Version (tls_version)  | PanOSTLSVersion  |  |  | network.tls.version   
Key Exchange Algorithm (tls_keyxchg)  | PanOSTLSKeyExchange  |  | tls_keyxchg  | additional.fields.key and additional.fields.value.string_value   
Encryption Algorithm (tls_enc)  | PanOSTLSEncryptionAlgorithm  |  | tls_enc  | additional.fields.key and additional.fields.value.string_value   
Hash Algorithm (tls_auth)  | PanOSTLSAuth  |  | tls_auth  | additional.fields.key and additional.fields.value.string_value   
Policy Name (policy_name)  | PanOSPolicyName  |  | policy_name  | additional.fields.key and additional.fields.value.string_value   
Elliptic Curve (ec_curve)  | PanOSEllipticCurve  |  |  | network.tls.curve   
Error Index (err_index)  | PanOSErrorIndex  |  | err_index  | additional.fields.key and additional.fields.value.string_value   
Root Status (root_status)  | PanOSRootStatus  |  | root_status  | additional.fields.key and additional.fields.value.string_value   
Chain Status (chain_status)  | PanOSChainStatus  |  | chain_status  | additional.fields.key and additional.fields.value.string_value   
Proxy Type (proxy_type)  | PanOSProxyType  |  | proxy_type  | additional.fields.key and additional.fields.value.string_value   
Certificate Serial Number (cert_serial)  | PanOSCertificateSerial  |  |  | network.tls.server.certificate.serial   
Certificate Fingerprint (fingerprint)  | PanOSFingerprint  |  |  | network.tls.server.certificate.md5/sha1/sha256   
Certificate Start Date (notbefore)  | PanOSTimeNotBefore  |  |  | network.tls.server.certificate.not_before   
Certificate End Date (notafter)  | PanOSTimeNotAfter  |  |  | network.tls.server.certificate.not_after   
Certificate Version (cert_ver)  | PanOSCertificateVersion  |  |  | network.tls.server.certificate.version   
Certificate Size (cert_size)  | PanOSCertificateSize  |  | cert_size  | additional.fields.key and additional.fields.value.string_value   
Common Name Length (cn_len)  | PanOSCommonNameLength  |  | cn_len  | additional.fields.key and additional.fields.value.string_value   
Issuer Common Name Length (issuer_len)  | PanOSIssuerNameLength  |  | issuer_len  | additional.fields.key and additional.fields.value.string_value   
Root Common Name Length (rootcn_len)  | PanOSRootCNLength  |  | rootcn_len  | additional.fields.key and additional.fields.value.string_value   
SNI Length (sni_len)  | PanOSSNILength  |  | sni_len  | additional.fields.key and additional.fields.value.string_value   
Certificate Flags (cert_flags)  | PanOSCertificateFlags  |  | cert_flags  | additional.fields.key and additional.fields.value.string_value   
Subject Common Name (cn)  | PanOSCommonName  |  | cn  | additional.fields.key and additional.fields.value.string_value   
Issuer Common Name (issuer_cn)  | PanOSIssuerCommonName  |  |  | network.tls.server.certificate.issuer   
Root Common Name (root_cn)  | PanOSRootCommonName  |  | root_cn  | additional.fields.key and additional.fields.value.string_value   
Server Name Indication  (sni)  |  |  |  | network.tls.client.server_name   
Error (error)  | PanOSErrorMessage  |  | error  | additional.fields.key and additional.fields.value.string_value   
Container ID (container_id)  | PanOSContainerID  |  | container_id  | intermediary.resource.product_object_id   
POD Namespace (pod_namespace)  | PanOSContainerNameSpace  |  | pod_namespace  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
POD Name (pod_name)  | PanOSContainerName  |  | pod_name  | target.resource.name   
Source External Dynamic List (src_edl)  | PanOSSourceEDL  |  | src_edl  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Destination External Dynamic List (dst_edl)  | PanOSDestinationEDL  |  | dst_edl  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Source Dynamic Address Group (src_dag)  | PanOSSourceDynamicAddressGroup  |  |  | principal.group.group_display_name   
Destination Dynamic Address Group (dst_dag)  | PanOSDestinationDynamicAddressGroup  |  |  | target.group.group_display_name   
High Resolution Timestamp (high_res_timestamp)  | PanOSTimeGeneratedHighResolution  |  |  | additional.fields.key and additional.fields.value.string_value   
Source Device Category (src_category)  | PanOSSourceDeviceCategory  |  | src_category  | principal.asset.category   
Source Device Profile (src_profile)  | PanOSSourceDeviceProfile  |  | src_profile  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Source Device Model (src_model)  | PanOSSourceDeviceModel  |  | src_model  | principal.asset.hardware.model   
Source Device Vendor (src_vendor)  | PanOSSourceDeviceVendor  |  | src_vendor  | principal.asset.hardware.manufacturer   
Source Device OS Family (src_osfamily)  | PanOSSourceDeviceOSFamily  |  |  | principal.platform   
Source Device OS Version (src_osversion)  | PanOSSourceDeviceOSVersion  |  |  | principal.platform_version   
Source Hostname (src_host)  | PanOSSourceDeviceHost  |  |  | principal.hostname   
Source MAC Address (src_mac)  | PanOSSourceDeviceMac  |  |  | principal.mac   
Destination Device Category (dst_category)  | PanOSDestinationDeviceCategory  |  | dst_category  | target.asset.category   
Destination Device Profile (dst_profile)  | PanOSDestinationDeviceProfile  |  | dst_profile  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Destination Device Model (dst_model)  | PanOSDestinationDeviceModel  |  | dst_model  | target.asset.hardware.model   
Destination Device Vendor (dst_vendor)  | PanOSDestinationDeviceVendor  |  | dst_vendor  | target.asset.hardware.manufacturer   
Destination Device OS Family (dst_osfamily)  | PanOSDestinationDeviceOSFamily  |  | dst_osfamily  | target.platform   
Destination Device OS Version (dst_osversion)  | PanOSDestinationDeviceOSVersion  |  |  | target.platform_version   
Destination Hostname (dst_host)  | PanOSDestinationDeviceHost  |  |  | target.hostname   
Destination MAC Address (dst_mac)  | PanOSDestinationDeviceMac  |  |  | target.mac   
Sequence Number (seqno)  | PanOSLogTypeSeqNo  |  |  | metadata.product_log_id   
Action Flags (actionflags)  | PanOSActionFlags  |  | actionflags  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_1)  |  | DeviceGroupHierarchyL1  | dg_hier_level_1  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_2)  |  | DeviceGroupHierarchyL2  | dg_hier_level_2  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_3)  |  | DeviceGroupHierarchyL3  | dg_hier_level_3  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_4)  |  | DeviceGroupHierarchyL4  | dg_hier_level_4  | additional.fields.key and additional.fields.value.string_value   
Virtual System Name (vsys_name)  |  |  |  | intermediary.asset.attribute.labels.key/value   
Device Name (device_name)  |  |  |  | intermediary.hostname   
Virtual System ID (vsys_id)  |  |  |  | intermediary.resource.product_object_id   
Application Subcategory (subcategory_of_app)  |  |  | subcategory_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Category (category_of_app)  |  |  | category_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Technology (technology_of_app)  |  |  | technology_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Risk (risk_of_app)  |  |  |  | security_result.severity   
Application Characteristic (characteristic_of_app)  |  |  | characteristic_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Container (container_of_app)  |  |  | container_of_app  | additional.fields.key and additional.fields.value.string_value   
Application SaaS (is_saas_of_app)  |  |  | is_saas_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Sanctioned State (sanctioned_state_of_app)  |  |  | sanctioned_state_of_app  | additional.fields.key and additional.fields.value.string_value   
Severity (severity)  | number-of-severity(header)  |  |  | security_result.severity and security_result.severity_details   
  
### Tunnel

The following table lists the log fields of the tunnel log type and their corresponding UDM fields.

CSV field | CEF field | LEEF field | Google Security Operations label key | UDM field  
---|---|---|---|---  
Receive Time (receive_time or cef-formatted-receive_time)  | rt  | devTime  |  | metadata.collected_timestamp,  metadata.event_timestamp (if "Generate Time" is absent)   
Serial Number (serial)  | deviceExternalId  | SerialNumber  |  | intermediary.asset.hardware.serial_number   
Type (type)  | type (Header)  | cat  |  | metadata.product_event_type   
Threat/Content Type (subtype)  | subtype (Header)  | Subtype  |  | metadata.product_event_type   
Generated Time (time_generated or cef-formatted-time_generated)  |  |  |  | metadata.event_timestamp   
Source Address (src)  | src  | src  |  | principal.ip   
Destination Address (dst)  | dst  | dst  |  | target.ip   
NAT Source IP (natsrc)  | sourceTranslatedAddress  | srcPostNAT  |  | principal.nat_ip   
NAT Destination IP (natdst)  | destinationTranslatedAddress  | dstPostNAT  |  | target.nat_ip   
Rule Name (rule)  | cs1  | RuleName  |  | security_result.rule_name   
Source User (srcuser)  | suser  | SourceUser / usrName  |  | principal.user.userid   
Destination User (dstuser)  | duser  | DestinationUser  |  | target.user.userid   
Application (app)  | app  | Application  |  | network.application_protocol   
Virtual System (vsys)  | cs3  | VirtualSystem  | vsys  | intermediary.asset.attribute.labels.key/value   
Source Zone (from)  | cs4  | SourceZone  | from  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Destination Zone (to)  | cs5  | DestinationZone  | to  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Inbound Interface (inbound_if)  | deviceInboundInterface  | IngressInterface  | inbound_if  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Outbound Interface (outbound_if)  | deviceOutboundInterface  | EgressInterface  | outbound_if  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Log Action (logset)  | cs6  | LogForwardingProfile  | logset  | additional.fields.key and additional.fields.value.string_value   
Session ID (sessionid)  | cn1  | SessionID  |  | network.session_id   
Repeat Count (repeatcnt)  | cnt  | RepeatCount  | repeatcnt  | additional.fields.key and additional.fields.value.string_value   
Source Port (sport)  | spt  | srcPort  |  | principal.port   
Destination Port (dport)  | dpt  | dstPort  |  | target.port   
NAT Source Port (natsport)  | sourceTranslatedPort  | srcPostNATPort  |  | principal.nat_port   
NAT Destination Port (natdport)  | destinationTranslatedPort  | dstPostNATPort  |  | target.nat_port   
Flags (flags)  | flexString1  | Flags  | flags  | additional.fields.key and additional.fields.value.string_value   
IP Protocol (proto)  | proto  | proto  |  | network.ip_protocol   
Action (action)  | act  | action  |  | security_result.action_details  security_result.action   
Severity (severity)  | number-of-severity(header)  |  |  | security_result.severity and security_result.severity_details   
Sequence Number (seqno)  | externalId  | sequence  |  | metadata.product_log_id   
Action Flags (actionflags)  | PanOSActionFlags  | ActionFlags  | actionflags  | additional.fields.key and additional.fields.value.string_value   
Source Location (srcloc)  |  |  |  | principal.location.country_or_region   
Destination Location (dstloc)  |  |  |  | target.location.country_or_region   
Device Group Hierarchy (dg_hier_level_1)  | PanOSDGl1  | DeviceGroupHierarchyL1  | dg_hier_level_1  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_2)  | PanOSDGl2  | DeviceGroupHierarchyL2  | dg_hier_level_2  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_3)  | PanOSDGl3  | DeviceGroupHierarchyL3  | dg_hier_level_3  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_4)  | PanOSDGl4  | DeviceGroupHierarchyL4  | dg_hier_level_4  | additional.fields.key and additional.fields.value.string_value   
Virtual System Name (vsys_name)  | PanOSVsysName  | vSrcName  |  | intermediary.asset.attribute.labels.key/value   
Device Name (device_name)  | dvchost  | DeviceName  |  | intermediary.hostname   
Tunnel ID (tunnelid)  | PanOSTunnelID  | TunnelID  | tunnelid  | additional.fields.key and additional.fields.value.string_value   
Monitor Tag (monitortag)  | PanOSMonitorTag  | MonitorTag  | monitortag  | additional.fields.key and additional.fields.value.string_value   
Parent Session ID (parent_session_id)  | PanOSParentSessionID  | ParentSessionID  | parent_session_id  | network.parent_session_id   
Parent Start Time (parent_start_time)  | PanOSParentStartTime  | ParentStartTime  | parent_start_time  | additional.fields.key and additional.fields.value.string_value   
Tunnel Type (tunnel)  | cs2  | TunnelType  | tunnel  | additional.fields.key and additional.fields.value.string_value   
Bytes (bytes)  | flexNumber1  | totalBytes  | bytes  | additional.fields.key and additional.fields.value.string_value   
Bytes Sent (bytes_sent)  | in  | srcBytes  |  | network.sent_bytes   
Bytes Received (bytes_received)  | out  | dstBytes  |  | network.received_bytes   
Packets (packets)  | cn2  | totalPackets  | packets  | additional.fields.key and additional.fields.value.string_value   
Packets Sent (pkts_sent)  | PanOSPacketsSent  | srcPackets  | pkts_sent  | network.sent_packets   
Packets Received (pkts_received)  | PanOSPacketsReceived  | dstPackets  | pkts_received  | network.received_packets   
Maximum Encapsulation (max_encap)  | flexNumber2  | MaximumEncapsulation  | max_encap  | additional.fields.key and additional.fields.value.string_value   
Unknown Protocol (unknown_proto)  | cfp1  | UnknownProtocol  | unknown_proto  | additional.fields.key and additional.fields.value.string_value   
Strict Checking (strict_check)  | cfp2  | StrictChecking  | strict_check  | additional.fields.key and additional.fields.value.string_value   
Tunnel Fragment (tunnel_fragment)  | PanOSTunnelFragment  | TunnelFragment  | tunnel_fragment  | additional.fields.key and additional.fields.value.string_value   
Sessions Created (sessions_created)  | cfp3  | SessionsCreated  | sessions_created  | additional.fields.key and additional.fields.value.string_value   
Sessions Closed (sessions_closed)  | cfp4  | SessionsClosed  | sessions_closed  | additional.fields.key and additional.fields.value.string_value   
Session End Reason (session_end_reason)  | reason  | SessionEndReason  |  | security_result.summary   
Action Source (action_source)  | cat  | ActionSource  | action_source  | additional.fields.key and additional.fields.value.string_value   
Start Time (start)  |  | startTime  | start  | additional.fields.key and additional.fields.value.string_value   
Elapsed Time (elapsed)  | cn3  | ElapsedTime  | elapsed  | network.session_duration.seconds   
Tunnel Inspection Rule (tunnel_insp_rule)  | PanOSTunneInspectionRule  |  |  | security_result.rule_name = "Tunnel Inspection Rule: %{PanOSTunnelInspectionRule}"   
Remote User IP (remote_user_ip)  | PanOSRmtUserIP  |  |  | principal.ip   
Remote User ID (remote_user_id)  | PanOSRmtUserID  |  | remote_user_id  | principal.user.userid   
Security Rule UUID (rule_uuid)  | PanOSRuleUUID  |  |  | security_result.rule_id   
PCAP ID (pcap_id)  | PanOSPcapID  |  | pcap_id  | additional.fields.key and additional.fields.value.string_value   
Dynamic User Group Name (dynusergroup_name)  | PanDynamicUsrgrp  |  |  | principal.group.group_display_name   
Source External Dynamic List (src_edl)  | PanOSSourceEDL  |  | src_edl  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Destination External Dynamic List (dst_edl)  | PanOSDestinationEDL  |  | dst_edl  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
High Resolution Timestamp (high_res timestamp)  | PanOSTimeGeneratedHighResolution  |  |  | additional.fields.key and additional.fields.value.string_value   
A Slice Differentiator (nssai_sd)  |  |  | nssai_sd  | additional.fields.key and additional.fields.value.string_value   
A Slice Service Type (nssai_sd)  |  |  | nssai_sd1  | additional.fields.key and additional.fields.value.string_value   
PDU Session ID (pdu_session_id)  |  |  | pdu_session_id  | additional.fields.key and additional.fields.value.string_value   
Application Subcategory (subcategory_of_app)  |  |  | subcategory_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Category (category_of_app)  |  |  | category_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Technology (technology_of_app)  |  |  | technology_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Risk (risk_of_app)  |  |  | risk_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Characteristic (characteristic_of_app)  |  |  | characteristic_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Container (container_of_app)  |  |  | container_of_app  | additional.fields.key and additional.fields.value.string_value   
Application SaaS (is_saas_of_app)  |  |  | is_saas_of_app  | additional.fields.key and additional.fields.value.string_value   
Tunneled Application (tunneled_app)  |  |  |  | additional.fields.key and additional.fields.value.string_value   
Offloaded (offloaded)  |  |  |  | additional.fields.key and additional.fields.value.string_value   
Flow Type (flow_type)  |  |  |  | additional.fields.key and additional.fields.value.string_value   
Cluster Name (cluster_name)  |  |  |  |  principal.resource.name  
Application Sanctioned State (sanctioned_state_of_app)  |  |  | sanctioned_state_of_app  | additional.fields.key and additional.fields.value.string_value   
  
### Authentication

The following table lists the log fields of the authentication log type and their corresponding UDM fields.

CSV field | CEF field | LEEF field | Google Security Operations label key | UDM field  
---|---|---|---|---  
Receive Time (receive_time or cef-formatted-receive_time)  | rt  | devTime  |  | metadata.collected_timestamp,  metadata.event_timestamp (if "Generate Time" is absent)   
Serial Number (serial)  | deviceExternalId  | SerialNumber  |  | intermediary.asset.hardware.serial_number   
Type (type)  | type (Header)  | cat  |  | metadata.product_event_type   
Threat/Content Type (subtype)  | subtype (Header)  | Subtype  |  | metadata.product_event_type   
Generated Time (time_generated or cef-formatted-time_generated)  |  |  |  | metadata.event_timestamp   
Virtual System (vsys)  | cs3  | VirtualSystem  | vsys  | intermediary.asset.attribute.labels.key/value   
Source IP (ip)  | src  | src  |  | principal.ip   
User (user)  | duser  | usrName  |  | target.user.userid   
Normalize User (normalize_user)  | cs2  | NormalizeUser  |  | target.user.user_display_name   
Object (object)  | fname  | ObjectName  | object  | target.resource.name   
Authentication Policy (authpolicy)  | cs4  | AuthPolicy  | authpolicy  | additional.fields.key and additional.fields.value.string_value   
Repeat Count (repeatcnt)  | cnt  | RepeatCount  | repeatcnt  | additional.fields.key and additional.fields.value.string_value   
Authentication ID (authid)  | cn2  | AuthenticationID  | authid  | additional.fields.key and additional.fields.value.string_value   
Vendor (vendor)  | flexString2  | Vendor  | vendor  | additional.fields.key and additional.fields.value.string_value   
Log Action (logset)  | cs6  | LogForwardingProfile  | logset  | additional.fields.key and additional.fields.value.string_value   
Server Profile (serverprofile)  | cs1  | ServerProfile  | serverprofile  | additional.fields.key and additional.fields.value.string_value   
Description (desc)  | PanOSDesc  | AdditionalAuthInfo  |  | security_result.description   
Client Type (clienttype)  | cs5  | ClientType  | clienttype  | additional.fields.key and additional.fields.value.string_value   
Event Type (event)  | msg  | msg  |  | extensions.auth.auth_details   
Factor Number (factorno)  | cn1  | FactorNumber  | factorno  | additional.fields.key and additional.fields.value.string_value   
Sequence Number (seqno)  | externalId  | sequence  |  | metadata.product_log_id   
Action Flags (actionflags)  | PanOSActionFlags  | ActionFlags  | actionflags  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_1)  | PanOSDGl1  | DeviceGroupHierarchyL1  | dg_hier_level_1  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_2)  | PanOSDGl2  | DeviceGroupHierarchyL2  | dg_hier_level_2  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_3)  | PanOSDGl3  | DeviceGroupHierarchyL3  | dg_hier_level_3  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_4)  | PanOSDGl4  | DeviceGroupHierarchyL4  | dg_hier_level_4  | additional.fields.key and additional.fields.value.string_value   
Virtual System Name (vsys_name)  | PanOSVsysName  | vSrcName  |  | intermediary.asset.attribute.labels.key/value   
Device Name (device_name)  | dvchost  | DeviceName  |  | intermediary.hostname   
Virtual System ID (vsys_id)  |  |  |  | intermediary.resource.product_object_id   
Authentication Protocol (authproto)  |  |  | authproto  | additional.fields.key and additional.fields.value.string_value   
UUID for rule (rule_uuid)  | PanOSRuleUUID/RuleUUID  |  |  | security_result.rule_id   
High Resolution Timestamp (high_res _timestamp)  | PanOSTimeGeneratedHighResolution  |  |  | additional.fields.key and additional.fields.value.string_value   
Source Device Category (src_category)  | PanOSSourceDeviceCategory  |  | src_category  | principal.asset.category   
Source Device Profile (src_profile)  | PanOSSourceDeviceProfile  |  | src_profile  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Source Device Model (src_model)  | PanOSSourceDeviceModel  |  | src_model  | principal.asset.hardware.model   
Source Device Vendor (src_vendor)  | PanOSSourceDeviceVendor  |  | src_vendor  | principal.asset.hardware.manufacturer   
Source Device OS Family (src_osfamily)  | PanOSSourceDeviceOSFamily  |  |  | principal.platform  
Source Device OS Version (src_osversion)  | PanOSSourceDeviceOSVersion  |  |  | principal.platform_version   
Source Hostname (src_host)  | PanOSSourceHostname  |  |  | principal.hostname   
Source MAC Address (src_mac)  | PanOSSourceMac  |  |  | principal.asset.mac   
Region (region)  | PanOSTrafficOriginRegion  |  |  | principal.location.country_or_region   
User Agent (user_agent)  | PanOSHTTPUserAgent  |  |  | network.http.user_agent   
Session ID(sessionid)  | PanOSTrafficSessionID  |  |  | network.session_id   
Severity (severity)  | number-of-severity(header)  |  |  | security_result.severity and security_result.severity_details   
Cluster Name (cluster_name)  |  |  |  | principal.resource.name   
  
### URL

The following table lists the log fields of the URL log type and their corresponding UDM fields.

CSV field | CEF field | LEEF field | Google Security Operations label key | UDM field  
---|---|---|---|---  
Receive Time (cef-formatted-receive_time)  | rt  | devTime  |  | metadata.collected_timestamp,  metadata.event_timestamp (if "Generate Time" is absent)   
Serial # (serial)  | deviceExternalId  | SerialNumber  |  | intermediary.asset.hardware.serial_number   
Type (type)  | type (Header)  | cat  |  | metadata.product_event_type   
Threat/Content Type (subtype)  | subtype (Header)  | Subtype  |  | metadata.product_event_type   
Generate Time  |  |  |  | metadata.event_timestamp   
Source address (src)  | src  | src  |  | principal.ip   
Destination address (dst)  | dst  | dst  |  | target.ip   
NAT Source IP (natsrc)  | sourceTranslatedAddress  | srcPostNAT  |  | principal.nat_ip   
NAT Destination IP (natdst)  | destinationTranslatedAddress  | dstPostNAT  |  | target.nat_ip   
Rule (rule)  | cs1  | RuleName  |  | security_result.rule_name   
Source User (srcuser)  | suser  | SourceUser  |  | principal.user.userid   
Destination User (dstuser)  | duser  | DestinationUser  |  | target.user.userid   
Application (app)  | app  | Application  |  | network.application_protocol   
Virtual System (vsys)  | cs3  | VirtualSystem  | vsys  | intermediary.asset.attribute.labels.key/value   
Source Zone (from)  | cs4  | SourceZone  | from  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Destination Zone (to)  | cs5  | DestinationZone  | to  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Inbound Interface (inbound_if)  | deviceInboundInterface  | IngressInterface  | inbound_if  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Outbound Interface (outbound_if)  | deviceOutboundInterface  | EgressInterface  | outbound_if  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Log Action (logset)  | cs6  | LogForwardingProfile  | logset  | additional.fields.key and additional.fields.value.string_value   
Time Logged  |  |  | time_logged  | additional.fields.key and additional.fields.value.string_value   
Session ID (sessionid)  | cn1  | SessionID  |  | network.session_id   
Repeat Count (repeatcnt)  | cnt  | RepeatCount  | repeatcnt  | additional.fields.key and additional.fields.value.string_value   
Source Port (sport)  | spt  | srcPort  |  | principal.port   
Destination Port (dport)  | dpt  | dstPort  |  | target.port   
NAT Source Port (natsport)  | sourceTranslatedPort  | srcPostNATPort  |  | principal.nat_port   
NAT Destination Port (natdport)  | destinationTranslatedPort  | dstPostNATPort  |  | target.nat_port   
Flags (flags)  | flexString1  | Flags  | flags  | additional.fields.key and additional.fields.value.string_value   
IP Protocol (proto)  | proto  | proto  |  | network.ip_protocol   
Action (action)  | act  | action  |  | security_result.action_details  security_result.action   
URL/Filename (misc)  |  | Miscellaneous  |  | target.file.names  target.url   
Threat/Content Name (threatid)  | cat  | ThreatID  |  | security_result.threat_id   
Category (category)  | cs2  | URLCategory  | category  | security_result.category_details   
Severity (severity)  | number-of-severity (Header)  | Severity  |  | security_result.severity  security_result.severity_details   
Direction (direction)  | flexString2  | Direction  |  | network.direction   
Sequence Number (seqno)  | externalId  | sequence  |  | metadata.product_log_id   
Action Flags (actionflags)  | PanOSActionFlags  | ActionFlags  | actionflags  | additional.fields.key and additional.fields.value.string_value   
Source Country (srcloc)  |  | SourceLocation  |  | principal.location.country_or_region   
Destination Country (dstloc)  |  | DestinationLocation  |  | target.location.country_or_region   
contenttype (contenttype)  | requestContext  | ContentType  | contenttype  | additional.fields.key and additional.fields.value.string_value   
pcap_id (pcap_id)  | fileId  | PCAP_ID  | pcap_id  | additional.fields.key and additional.fields.value.string_value   
filedigest (filedigest)  |  | FileDigest  |  | target.file.sha1/md5/sha256   
cloud (cloud)  |  | Cloud  | cloud  | additional.fields.key and additional.fields.value.string_value   
url_idx (url_idx)  |  | URLIndex  | url_idx  | additional.fields.key and additional.fields.value.string_value   
user_agent (user_agent)  | requestClientApplication  | UserAgent  |  | network.http.user_agent   
filetype (filetype)  |  |  |  | target.file.mime_type   
xff (xff)  | PanOSXForwarderfor  | identSrc  | xff  | principal.ip   
referer (referer)  | PanOSReferer  | Referer  |  | network.http.referral_url   
sender (sender)  |  |  |  | network.email.from   
subject (subject)  |  | Subject  |  | network.email.subject   
recipient (recipient)  |  |  |  | network.email.to   
reportid (reportid)  |  |  | reportid  | additional.fields.key and additional.fields.value.string_value   
DG Hierarchy Level 1 (dg_hier_level_1)  | PanOSDGl1  | DeviceGroupHierarchyL1  | dg_hier_level_1  | additional.fields.key and additional.fields.value.string_value   
DG Hierarchy Level 2 (dg_hier_level_2)  | PanOSDGl2  | DeviceGroupHierarchyL2  | dg_hier_level_2  | additional.fields.key and additional.fields.value.string_value   
DG Hierarchy Level 3 (dg_hier_level_3)  | PanOSDGl3  | DeviceGroupHierarchyL3  | dg_hier_level_3  | additional.fields.key and additional.fields.value.string_value   
DG Hierarchy Level 4 (dg_hier_level_4)  | PanOSDGl4  | DeviceGroupHierarchyL4  | dg_hier_level_4  | additional.fields.key and additional.fields.value.string_value   
Virtual System Name (vsys_name)  | PanOSVsysName  | vSrcName  |  | intermediary.asset.attribute.labels.key/value   
Device Name (device_name)  | dvchost  | DeviceName  |  | intermediary.hostname   
file_url (file_url)  |  |  |  | target.url   
Source VM UUID (src_uuid)  |  | SrcUUID  |  | principal.asset.product_object_id   
Destination VM UUID (dst_uuid)  |  | DstUUID  |  | target.asset.product_object_id   
http_method (http_method)  | requestMethod  | RequestMethod  |  | network.http.method   
Tunnel ID/IMSI (tunnelid)  | PanOSTunnelID  | TunnelID  | tunnelid  | additional.fields.key and additional.fields.value.string_value   
Monitor Tag/IMEI (monitortag)  | PanOSMonitorTag  | MonitorTag  | monitortag  | additional.fields.key and additional.fields.value.string_value   
Parent Session ID (parent_session_id)  | PanOSParentSessionID  | ParentSessionID  | parent_session_id  | network.parent_session_id   
Parent Session Start Time (parent_start_time)  | PanOSParentStartTime  | ParentStartTime  | parent_start_time  | additional.fields.key and additional.fields.value.string_value   
Tunnel (tunnel)  | PanOSTunnelType  | TunnelType  | tunnel  | additional.fields.key and additional.fields.value.string_value   
thr_category (thr_category)  | PanOSThreatCategory  | ThreatCategory  | thr_category  | security_result.detection_fields.key/value   
contentver (contentver)  | PanOSContentVer  | ContentVer  | contentver  | additional.fields.key and additional.fields.value.string_value   
sig_flags (sig_flags)  |  |  | sig_flags  | additional.fields.key and additional.fields.value.string_value   
SCTP Association ID (assoc_id)  | PanOSAssocID  |  | assoc_id  | additional.fields.key and additional.fields.value.string_value   
Payload Protocol ID (ppid)  | PanOSPPID  |  | ppid  | additional.fields.key and additional.fields.value.string_value   
http_headers (http_headers)  | PanOSHTTPHeader  |  | http_headers  | target.url.last_http_response_headers   
URL Category List (url_category_list)  | PanOSURLCatList  |  | url_category_list  | additional.fields.key and additional.fields.value.string_value   
UUID for rule (rule_uuid)  | PanOSRuleUUID  |  | rule_uuid  | security_result.rule_id   
HTTP/2 Connection (http2_connection)  | PanOSHTTP2Con  |  | http2_connection  | network.application_protocol_version   
dynusergroup_name (dynusergroup_name)  | PanDynamicUsrgrp  |  | dynusergroup_name  | additional.fields.key and additional.fields.value.string_value   
XFF address (xff_ip)  | PanXFFIP  |  |  | principal.ip   
Source Device Category (src_category)  | PanSrcDeviceCat  |  | src_category  | principal.asset.category   
Source Device Profile (src_profile)  | PanSrcDeviceProf  |  | src_profile  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Source Device Model (src_model)  | PanSrcDeviceModel  |  | src_model  | principal.asset.hardware.model   
Source Device Vendor (src_vendor)  | PanSrcDeviceVendor  |  | src_vendor  | principal.asset.hardware.manufacturer   
Source Device OS Family (src_osfamily)  | PanSrcDeviceOS  |  |  | principal.platform   
Source Device OS Version (src_osversion)  | PanSrcDeviceOSv  |  |  | principal.platform_version   
Source Hostname (src_host)  | PanSrcHostname  |  | src_host  | principal.hostname   
Source Mac Address (src_mac)  | PanSrcMac  |  |  | principal.mac   
Destination Device Category (dst_category)  | PanDstDeviceCat  |  | dst_category  | target.asset.category   
Destination Device Profile (dst_profile)  | PanDstDeviceProf  |  | dst_profile  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Destination Device Model (dst_model)  | PanDstDeviceModel  |  | dst_model  | target.asset.hardware.model   
Destination Device Vendor (dst_vendor)  | PanDstDeviceVendor  |  | dst_vendor  | target.asset.hardware.manufacturer   
Destination Device OS Family (dst_osfamily)  | PanDstDeviceOS  |  |  | target.platform   
Destination Device OS Version (dst_osversion)  | PanDstDeviceOSv  |  |  | target.platform_version   
Destination Hostname (dst_host)  | PanPODNamespace  |  |  | target.hostname   
Destination Mac Address (dst_mac)  | PanDstMac  |  |  | target.mac   
Container ID (container_id)  | PanContainerName  |  | container_id  | intermediary.resource.product_object_id   
POD Namespace (pod_namespace)  | PanPODNamespace  |  | pod_namespace  | target.resource.attribute.labels.key/value   
POD Name (pod_name)  | PanPODName  |  | pod_name  | target.resource.name   
Source External Dynamic List (src_edl)  | PanSrcEDL  |  | src_edl  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Destination External Dynamic List (dst_edl)  | PanDstEDL  |  | dst_edl  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Host ID (hostid)  | PanGPHostID  |  | hostid  | principal.asset.asset_id   
Serial Number (serialnumber)  | PanEPSerial  |  |  | principal.asset.hardware.serial_number   
domain_edl (domain_edl)  | PanDomainEDL  |  | domain_edl  | additional.fields.key and additional.fields.value.string_value   
Source Dynamic Address Group (src_dag)  | PanSrcDAG  |  |  | principal.group.group_display_name   
Destination Dynamic Address Group (dst_dag)  | PanDstDAG  |  |  | target.group.group_display_name   
partial_hash (partial_hash)  | PanPartialHash  |  | partial_hash  | additional.fields.key and additional.fields.value.string_value   
High Res Timestamp (high_res_timestamp)  | PanTimeHighRes  |  |  | additional.fields.key and additional.fields.value.string_value   
Reason (reason)  | PanReasonFilteringAction  |  | reason  | security_result.summary   
justification (justification)  | PanJustification  |  | justification  | additional.fields.key and additional.fields.value.string_value   
nssai_sst (nssai_sst)  | PanASServiceType  |  | nssai_sst  | additional.fields.key and additional.fields.value.string_value   
Subcategory of app (subcategory_of_app)  |  |  | subcategory_of_app  | additional.fields.key and additional.fields.value.string_value   
Category of app (category_of_app)  |  |  | category_of_app  | additional.fields.key and additional.fields.value.string_value   
Technology of app (technology_of_app)  |  |  | technology_of_app  | additional.fields.key and additional.fields.value.string_value   
Risk of app (risk_of_app)  |  |  | risk_of_app  | additional.fields.key and additional.fields.value.string_value   
Characteristic of app (characteristic_of_app)  |  |  | characteristic_of_app  | additional.fields.key and additional.fields.value.string_value   
Container of app (container_of_app)  |  |  | container_of_app  | additional.fields.key and additional.fields.value.string_value   
Tunneled app (tunneled_app)  |  |  | tunneled_app  | additional.fields.key and additional.fields.value.string_value   
SaaS of app (is_saas_of_app)  |  |  | is_saas_of_app  | additional.fields.key and additional.fields.value.string_value   
Sanctioned State of app (sanctioned_state_of_app)  |  |  | sanctioned_state_of_app  | additional.fields.key and additional.fields.value.string_value   
Cloud Report ID (cloud_reportid)  |  |  |  | additional.fields.key and additional.fields.value.string_value   
Cluster Name (cluster_name)  |  |  |  |  principal.resource.name  
Flow Type (flow_type)  |  |  |  | additional.fields.key and additional.fields.value.string_value   
  
### Data

The following table lists the log fields of the data log type and their corresponding UDM fields.

CSV field | CEF field | LEEF field | Google Security Operations label key | UDM field  
---|---|---|---|---  
Receive Time (cef-formatted-receive_time)  | rt  | devTime  |  | metadata.collected_timestamp,  metadata.event_timestamp (if "Generate Time" is absent)   
Serial # (serial)  | deviceExternalId  | SerialNumber  |  | intermediary.asset.hardware.serial_number   
Type (type)  | type (Header)  | cat  |  | metadata.product_event_type   
Threat/Content Type (subtype)  | subtype (Header)  | Subtype  |  | metadata.product_event_type   
Generate Time  |  |  |  | metadata.event_timestamp   
Source address (src)  | src  | src  |  | principal.ip   
Destination address (dst)  | dst  | dst  |  | target.ip   
NAT Source IP (natsrc)  | sourceTranslatedAddress  | srcPostNAT  |  | principal.nat_ip   
NAT Destination IP (natdst)  | destinationTranslatedAddress  | dstPostNAT  |  | target.nat_ip   
Rule (rule)  | cs1  | RuleName  |  | security_result.rule_name   
Source User (srcuser)  | suser  | SourceUser  |  | principal.user.userid   
Destination User (dstuser)  | duser  | DestinationUser  |  | target.user.userid   
Application (app)  | app  | Application  |  | network.application_protocol   
Virtual System (vsys)  | cs3  | VirtualSystem  | vsys  | intermediary.asset.attribute.labels.key/value   
Source Zone (from)  | cs4  | SourceZone  | from  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Destination Zone (to)  | cs5  | DestinationZone  | to  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Inbound Interface (inbound_if)  | deviceInboundInterface  | IngressInterface  | inbound_if  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Outbound Interface (outbound_if)  | deviceOutboundInterface  | EgressInterface  | outbound_if  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Log Action (logset)  | cs6  | LogForwardingProfile  | logset  | additional.fields.key and additional.fields.value.string_value   
Time Logged  |  |  | time_logged  | additional.fields.key and additional.fields.value.string_value   
Session ID (sessionid)  | cn1  | SessionID  |  | network.session_id   
Repeat Count (repeatcnt)  | cnt  | RepeatCount  | repeatcnt  | additional.fields.key and additional.fields.value.string_value   
Source Port (sport)  | spt  | srcPort  |  | principal.port   
Destination Port (dport)  | dpt  | dstPort  |  | target.port   
NAT Source Port (natsport)  | sourceTranslatedPort  | srcPostNATPort  |  | principal.nat_port   
NAT Destination Port (natdport)  | destinationTranslatedPort  | dstPostNATPort  |  | target.nat_port   
Flags (flags)  | flexString1  | Flags  | flags  | additional.fields.key and additional.fields.value.string_value   
IP Protocol (proto)  | proto  | proto  |  | network.ip_protocol   
Action (action)  | act  | action  |  | security_result.action_details  security_result.action   
URL/Filename (misc)  |  | Miscellaneous  |  | target.file.names  target.url   
Threat/Content Name (threatid)  | cat  | ThreatID  |  | security_result.threat_id   
Category (category)  | cs2  | URLCategory  | category  | security_result.category_details   
Severity (severity)  | number-of-severity (Header)  | Severity  |  | security_result.severity  security_result.severity_details   
Direction (direction)  | flexString2  | Direction  |  | network.direction   
Sequence Number (seqno)  | externalId  | sequence  |  | metadata.product_log_id   
Action Flags (actionflags)  | PanOSActionFlags  | ActionFlags  | actionflags  | additional.fields.key and additional.fields.value.string_value   
Source Country (srcloc)  |  | SourceLocation  |  | principal.location.country_or_region   
Destination Country (dstloc)  |  | DestinationLocation  |  | target.location.country_or_region   
contenttype (contenttype)  |  | ContentType  | contenttype  | additional.fields.key and additional.fields.value.string_value   
pcap_id (pcap_id)  | fileId  | PCAP_ID  | pcap_id  | additional.fields.key and additional.fields.value.string_value   
filedigest (filedigest)  |  | FileDigest  |  | target.file.sha1/md5/sha256   
cloud (cloud)  |  | Cloud  | cloud  | additional.fields.key and additional.fields.value.string_value   
url_idx (url_idx)  |  | URLIndex  | url_idx  | additional.fields.key and additional.fields.value.string_value   
user_agent (user_agent)  |  |  |  | network.http.user_agent   
filetype (filetype)  |  |  |  | target.file.mime_type   
xff (xff)  |  |  | xff  | principal.ip   
referer (referer)  |  |  |  | network.http.referral_url   
sender (sender)  |  |  |  | network.email.from   
subject (subject)  |  | Subject  |  | network.email.subject   
recipient (recipient)  |  |  |  | network.email.to   
reportid (reportid)  |  |  | reportid  | additional.fields.key and additional.fields.value.string_value   
DG Hierarchy Level 1 (dg_hier_level_1)  | PanOSDGl1  | DeviceGroupHierarchyL1  | dg_hier_level_1  | additional.fields.key and additional.fields.value.string_value   
DG Hierarchy Level 2 (dg_hier_level_2)  | PanOSDGl2  | DeviceGroupHierarchyL2  | dg_hier_level_2  | additional.fields.key and additional.fields.value.string_value   
DG Hierarchy Level 3 (dg_hier_level_3)  | PanOSDGl3  | DeviceGroupHierarchyL3  | dg_hier_level_3  | additional.fields.key and additional.fields.value.string_value   
DG Hierarchy Level 4 (dg_hier_level_4)  | PanOSDGl4  | DeviceGroupHierarchyL4  | dg_hier_level_4  | additional.fields.key and additional.fields.value.string_value   
Virtual System Name (vsys_name)  | PanOSVsysName  | vSrcName  |  | intermediary.asset.attribute.labels.key/value   
Device Name (device_name)  | dvchost  | DeviceName  |  | intermediary.hostname   
file_url (file_url)  |  |  |  | target.url   
Source VM UUID (src_uuid)  |  | SrcUUID  |  | principal.asset.product_object_id   
Destination VM UUID (dst_uuid)  |  | DstUUID  |  | target.asset.product_object_id   
http_method (http_method)  |  | RequestMethod  |  | network.http.method   
Tunnel ID/IMSI (tunnelid)  | PanOSTunnelID  | TunnelID  | tunnelid  | additional.fields.key and additional.fields.value.string_value   
Monitor Tag/IMEI (monitortag)  | PanOSMonitorTag  | MonitorTag  | monitortag  | additional.fields.key and additional.fields.value.string_value   
Parent Session ID (parent_session_id)  | PanOSParentSessionID  | ParentSessionID  | parent_session_id  | network.parent_session_id   
Parent Session Start Time (parent_start_time)  | PanOSParentStartTime  | ParentStartTime  | parent_start_time  | additional.fields.key and additional.fields.value.string_value   
Tunnel (tunnel)  | PanOSTunnelType  | TunnelType  | tunnel  | additional.fields.key and additional.fields.value.string_value   
thr_category (thr_category)  | PanOSThreatCategory  | ThreatCategory  | thr_category  | security_result.detection_fields.key/value   
contentver (contentver)  | PanOSContentVer  | ContentVer  | contentver  | additional.fields.key and additional.fields.value.string_value   
sig_flags (sig_flags)  |  |  | sig_flags  | additional.fields.key and additional.fields.value.string_value   
SCTP Association ID (assoc_id)  | PanOSAssocID  |  | assoc_id  | additional.fields.key and additional.fields.value.string_value   
Payload Protocol ID (ppid)  | PanOSPPID  |  | ppid  | additional.fields.key and additional.fields.value.string_value   
http_headers (http_headers)  | PanOSHTTPHeader  |  | http_headers  | target.url.last_http_response_headers   
URL Category List (url_category_list)  |  |  | url_category_list  | additional.fields.key and additional.fields.value.string_value   
UUID for rule (rule_uuid)  | PanOSRuleUUID  |  | rule_uuid  | security_result.rule_id   
HTTP/2 Connection (http2_connection)  |  |  | http2_connection  | network.application_protocol_version   
dynusergroup_name (dynusergroup_name)  |  |  | dynusergroup_name  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
XFF address (xff_ip)  |  |  |  | principal.ip   
Source Device Category (src_category)  |  |  | src_category  | principal.asset.category   
Source Device Profile (src_profile)  |  |  | src_profile  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Source Device Model (src_model)  |  |  | src_model  | principal.asset.hardware.model   
Source Device Vendor (src_vendor)  |  |  | src_vendor  | principal.asset.hardware.manufacturer   
Source Device OS Family (src_osfamily)  |  |  |  | principal.platform   
Source Device OS Version (src_osversion)  |  |  |  | principal.platform_version   
Source Hostname (src_host)  |  |  | src_host  | principal.hostname   
Source Mac Address (src_mac)  |  |  |  | principal.mac   
Destination Device Category (dst_category)  |  |  | dst_category  | target.asset.category   
Destination Device Profile (dst_profile)  |  |  | dst_profile  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Destination Device Model (dst_model)  |  |  | dst_model  | target.asset.hardware.model   
Destination Device Vendor (dst_vendor)  |  |  | dst_vendor  | target.asset.hardware.manufacturer   
Destination Device OS Family (dst_osfamily)  |  |  |  | target.platform   
Destination Device OS Version (dst_osversion)  |  |  |  | target.platform_version   
Destination Hostname (dst_host)  |  |  |  | target.hostname   
Destination Mac Address (dst_mac)  |  |  |  | target.mac   
Container ID (container_id)  |  |  | container_id  | intermediary.resource.product_object_id   
POD Namespace (pod_namespace)  |  |  | pod_namespace  | target.resource.attribute.labels.key/value   
POD Name (pod_name)  |  |  | pod_name  | target.resource.name   
Source External Dynamic List (src_edl)  |  |  | src_edl  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Destination External Dynamic List (dst_edl)  |  |  | dst_edl  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Host ID (hostid)  |  |  | hostid  | principal.asset.asset_id   
Serial Number (serialnumber)  |  |  |  | principal.asset.hardware.serial_number   
domain_edl (domain_edl)  |  |  | domain_edl  | additional.fields.key and additional.fields.value.string_value   
Source Dynamic Address Group (src_dag)  |  |  |  | principal.group.group_display_name   
Destination Dynamic Address Group (dst_dag)  |  |  |  | target.group.group_display_name   
partial_hash (partial_hash)  |  |  | partial_hash  | additional.fields.key and additional.fields.value.string_value   
High Res Timestamp (high_res_timestamp)  |  |  |  | additional.fields.key and additional.fields.value.string_value   
Reason (reason)  |  |  | reason  | security_result.summary   
justification (justification)  |  |  | justification  | additional.fields.key and additional.fields.value.string_value   
nssai_sst (nssai_sst)  |  |  | nssai_sst  | additional.fields.key and additional.fields.value.string_value   
Subcategory of app (subcategory_of_app)  |  |  | subcategory_of_app  | additional.fields.key and additional.fields.value.string_value   
Category of app (category_of_app)  |  |  | category_of_app  | additional.fields.key and additional.fields.value.string_value   
Technology of app (technology_of_app)  |  |  | technology_of_app  | additional.fields.key and additional.fields.value.string_value   
Risk of app (risk_of_app)  |  |  | risk_of_app  | additional.fields.key and additional.fields.value.string_value   
Characteristic of app (characteristic_of_app)  |  |  | characteristic_of_app  | additional.fields.key and additional.fields.value.string_value   
Container of app (container_of_app)  |  |  | container_of_app  | additional.fields.key and additional.fields.value.string_value   
Tunneled app (tunneled_app)  |  |  | tunneled_app  | additional.fields.key and additional.fields.value.string_value   
SaaS of app (is_saas_of_app)  |  |  | is_saas_of_app  | additional.fields.key and additional.fields.value.string_value   
Sanctioned State of app (sanctioned_state_of_app)  |  |  | sanctioned_state_of_app  | additional.fields.key and additional.fields.value.string_value   
Cloud Report ID (cloud_reportid)  |  |  |  | additional.fields.key and additional.fields.value.string_value   
Cluster Name (cluster_name)  |  |  |  | principal.resource.name   
Flow Type (flow_type)  |  |  |  | additional.fields.key and additional.fields.value.string_value   
  
### GlobalProtect

The following table lists the log fields of the GlobalProtect log type and their corresponding UDM fields.

CSV field | CEF field | LEEF field | Google Security Operations label key | UDM field  
---|---|---|---|---  
Receive Time (receive_time)  | rt  |  | received_time  | metadata.event_timestamp   
Serial # (serial)  | PanOSDeviceSN  |  | intermediary_asset_hardware_serial_number  | intermediary.asset.hardware.serial_number   
Type (type)  | type (Header)  |  |  | metadata.product_event_type   
Threat/Content Type (subtype)  | subtype (Header)  | Subtype  |  | metadata.product_event_type   
Generate Time (time_generated)  | PanOSLogTimeStamp  |  | generated_timestamp  | metadata.event_timestamp   
Virtual System (vsys)  | PanOSVirtualSystem  |  | vsys  | intermediary.asset.attribute.labels.key/value   
Event ID (eventid)  | PanOSEventID  |  | event_id  | additional.fields.key and additional.fields.value.string_value   
Stage (stage)  | PanOSStage  |  | stage  | additional.fields.key and additional.fields.value.string_value   
Authentication Method (auth_method)  | PanOSAuthMethod  |  | extension_auth_auth_details  | extensions.auth.auth_details   
Tunnel Type (tunnel_type)  | PanOSTunnelType  |  | tunnel  | additional.fields.key and additional.fields.value.string_value   
Source User (srcuser)  | PanOSSourceUserName  |  | src_user  | principal.user.email_address  principal.user.userid  principal.administrative_domain   
Source Region (srcregion)  | PanOSSourceRegion  |  | src_region  | principal.location.country_or_region   
Machine Name (machinename)  | PanOSEndpointDeviceName  |  | machine_name  | principal.hostname   
Public IP (public_ip)  | PanOSPublicIPv4  |  |  | principal.nat_ip   
Public IPv6 (public_ipv6)  | PanOSPublicIPv6  |  |  | principal.nat_ip   
Private IP (private_ip)  | PanOSPrivateIPv4  |  |  | principal.ip   
Private IPv6 (private_ipv6)  | PanOSPrivateIPv6  |  |  | principal.ip   
Host ID (hostid)  | PanOSHostID  |  | hostid  | principal.asset.asset_id   
Serial Number (serialnumber)  | PanOSDeviceSN  |  |  | principal.asset.hardware.serial_number   
Client Version (client_ver)  | PanOSGlobalProtectClientVersion  |  | client_ver  | additional.fields.key and additional.fields.value.string_value   
Client OS (client_os)  | PanOSEndpointOSType  |  |  | principal.platform   
Client OS Version (client_os_ver)  | PanOSEndpointOSVersion  |  |  | principal.platform_version   
Repeat Count (repeatcnt)  | PanOSCountOfRepeats  |  | repeatcnt  | additional.fields.key and additional.fields.value.string_value   
Reason (reason)  | PanOSQuarantineReason  |  |  | security_result.summary   
Error (error)  | PanOSConnectionError  |  | error  | security_result.description   
Description (opaque)  | PanOSDescription  |  |  | security_result.description   
Status (status)  | PanOSEventStatus  |  | status  | additional.fields.key and additional.fields.value.string_value   
Location (location)  | PanOSGPGatewayLocation  |  |  | target.location.country_or_region   
Login Duration (login_duration)  | PanOSLoginDuration  |  |  | network.session_duration   
Connect Method (connect_method)  | PanOSConnectionMethod  |  | connect_method  | additional.fields.key and additional.fields.value.string_value   
Error Code (error_code)  | PanOSConnectionErrorID  |  | error_code  | additional.fields.key and additional.fields.value.string_value   
Portal (portal)  | PanOSPortal  |  | portal  | additional.fields.key and additional.fields.value.string_value   
Sequence Number (seqno)  | PanOSSequenceNo  |  |  | metadata.product_log_id   
Action Flags (actionflags)  | PanOSActionFlags  |  | actionflags  | additional.fields.key and additional.fields.value.string_value   
High Resolution Timestamp (high_res_timestamp)  | PanOSTimeGeneratedHighResolution  |  |  | additional.fields.key and additional.fields.value.string_value   
Gateway Selection Method (selection_type)  | PanOSGatewaySelectionType  |  | selection_type  | additional.fields.key and additional.fields.value.string_value   
SSL Response Time (response_time)  | PanOSSSLResponseTime  |  | response_time  | additional.fields.key and additional.fields.value.string_value   
Gateway Priority (priority)  | PanOSGatewayPriority  |  | priority  | additional.fields.key and additional.fields.value.string_value   
Attempted Gateways (attempted_gateways)  | PanOSAttemptedGateways  |  | attempted_gateways  | additional.fields.key and additional.fields.value.string_value   
Gateway Name (gateway)  | PanOSAttemptedGateways  |  | gateway  | target.resource.name   
Device Group Hierarchy (dg_hier_level_1)  |  |  | dg_hier_level_1  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_2)  |  |  | dg_hier_level_2  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_3)  |  |  | dg_hier_level_3  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy (dg_hier_level_4)  |  |  | dg_hier_level_4  | additional.fields.key and additional.fields.value.string_value   
Virtual System Name (vsys_name)  |  |  |  | intermediary.asset.attribute.labels.key/value   
Device Name (device_name)  |  |  |  | intermediary.hostname   
Virtual System ID (vsys_id)  |  |  |  | intermediary.resource.product_object_id   
Severity (severity)  | number-of-severity(header)  |  |  | security_result.severity and security_result.severity_details   
Cluster Name (cluster_name)  |  |  |  | principal.resource.name   
  
### Correlation

The following table lists the log fields of the Correlation log type and their corresponding UDM fields.

CSV field | CEF field | LEEF field | Google Security Operations label key | UDM field  
---|---|---|---|---  
Generated Time (time_generated or cef-formatted-time_generated)  |  | startTime  | generated_timestamp  | metadata.event_timestamp   
Source Address (src)  |  | src  |  | principal.ip   
Source User (srcuser)  |  | SourceUser / usrName  |  | principal.user.userid   
Virtual System (vsys)  |  | VirtualSystem  | vsys  | intermediary.asset.attribute.labels.key/value   
Category (category)  |  |  |  | security_result.category_details   
Severity (severity)  |  | Severity  |  | security_result.severity and security_result.severity_details   
Device Group Hierarchy Level 1  |  | DeviceGroupHierarchyL1  |  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy Level 2  |  | DeviceGroupHierarchyL2  |  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy Level 3  |  | DeviceGroupHierarchyL3  |  | additional.fields.key and additional.fields.value.string_value   
Device Group Hierarchy Level 4  |  | DeviceGroupHierarchyL4  |  | additional.fields.key and additional.fields.value.string_value   
Virtual System Name (vsys_name)  |  | vSrcName  |  | intermediary.asset.attribute.labels.key/value   
Device Name (device_name)  |  | DeviceName  |  | intermediary.hostname intermediary.asset.hostname target.hostname target.asset.hostname  
Virtual System ID (vsys_id)  |  | VirtualSystemID  |  | intermediary.resource.product_object_id   
Object Name (objectname)  |  | ObjectName  |  | target.resource.name   
Object ID (object_id)  |  | ObjectID  |  | target.resource.product_object_id   
Evidence (evidence)  |  | msg  |  | security_result.summary   
  
### GTP

The following table lists the log fields of the gtp log type and their corresponding UDM fields.

CSV field | CEF field | LEEF field | Google Security Operations label key | UDM field  
---|---|---|---|---  
Receive Time (receive_time or cef-formatted-receive_time)  |  |  |  | metadata.collected_timestamp,  metadata.event_timestamp (if "Generate Time" is absent)   
Serial Number (serial)  |  |  |  | intermediary.asset.hardware.serial_number   
Type (type)  |  |  |  | metadata.product_event_type   
Threat/Content Type (subtype)  |  |  |  | metadata.product_event_type   
Generated Time (time_generated or cef-formatted-time_generated)  |  |  |  | metadata.event_timestamp   
Source Address (src)  |  |  |  | principal.ip   
Destination Address (dst)  |  |  |  | target.ip   
Rule Name (rule)  |  |  |  | security_result.rule_name   
Application (app)  |  |  |  | network.application_protocol   
Virtual System (vsys)  |  |  | vsys  | intermediary.asset.attribute.labels.key/value   
Source Zone (from)  |  |  | from  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Destination Zone (to)  |  |  | to  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Inbound Interface (inbound_if)  |  |  | inbound_if  | principal.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Outbound Interface (outbound_if)  |  |  | outbound_if  | target.resource.attribute.labels.key/value additional.fields.key and additional.fields.value.string_value  
Log Action (logset)  |  |  | logset  | additional.fields.key and additional.fields.value.string_value   
Session ID (sessionid)  |  |  |  | network.session_id   
Source Port (sport)  |  |  |  | principal.port   
Destination Port (dport)  |  |  |  | target.port   
IP Protocol (proto)  |  |  |  | network.ip_protocol   
Action (action)  |  |  |  | security_result.action_details  security_result.action   
GTP Event Type (event_type)  |  |  | gtp_event_type  | additional.fields.key and additional.fields.value.string_value   
MSISDN (msisdn)  |  |  | msisdn  | additional.fields.key and additional.fields.value.string_value   
Access Point Name (apn)  |  |  | apn  | additional.fields.key and additional.fields.value.string_value   
Radio Access Technology (rat)  |  |  | rat  | additional.fields.key and additional.fields.value.string_value   
GTP Message Type (msg_type)  |  |  | gtp_msg_type  | additional.fields.key and additional.fields.value.string_value   
End IP Address (end_ip_adr)  |  |  |  | principal.ip   
Tunnel Endpoint Identifier1 (teid1)  |  |  | teid1  | additional.fields.key and additional.fields.value.string_value   
Tunnel Endpoint Identifier2 (teid2)  |  |  | teid2  | additional.fields.key and additional.fields.value.string_value   
GTP Interface (gtp_interface)  |  |  | gtp_interface  | additional.fields.key and additional.fields.value.string_value   
GTP Cause (cause_code)  |  |  | gtp_cause_code  | additional.fields.key and additional.fields.value.string_value   
Severity (severity)  |  |  |  | security_result.severity and security_result.severity_details   
Serving Network MCC (mcc)  |  |  | mcc  | additional.fields.key and additional.fields.value.string_value   
Serving Network MNC (mnc)  |  |  | mnc  | additional.fields.key and additional.fields.value.string_value   
Area Code (area_code)  |  |  | area_code  | additional.fields.key and additional.fields.value.string_value   
Cell ID (cell_id)  |  |  | cell_id  | additional.fields.key and additional.fields.value.string_value   
GTP Event Code (event_code)  |  |  | event_code  | additional.fields.key and additional.fields.value.string_value   
Source Location (srcloc)  |  |  |  | principal.location.country_or_region   
Destination Location (dstloc)  |  |  |  | target.location.country_or_region   
Tunnel ID/IMSI (imsi)  |  |  | tunnelid  | additional.fields.key and additional.fields.value.string_value   
Monitor Tag/IMEI (imei)  |  |  | monitortag  | additional.fields.key and additional.fields.value.string_value   
Start Time (start)  |  |  | start  | additional.fields.key and additional.fields.value.string_value   
Elapsed Time (elapsed)  |  |  |  | network.session_duration.seconds   
Tunnel Inspection RuleTunnel (tunnel_insp_rule)  |  |  | tunnel_insp_rule  | security_result.detection_fields.key/value   
Remote User IP (remote_user_ip)  |  |  |  | principal.ip   
Remote User ID (remote_user_id)  |  |  | remote_user_id  | principal.user.userid   
UUID for rule (rule_uuid)  |  |  |  | security_result.rule_id   
PCAP ID (pcap_id)  |  |  | pcap_id  | additional.fields.key and additional.fields.value.string_value   
High Resolution Timestamp (high_res_timestamp)  |  |  |  | additional.fields.key and additional.fields.value.string_value   
A Slice Service Type (nsdsai_sst)  |  |  | nsdsai_sst  | additional.fields.key and additional.fields.value.string_value   
A Slice Differentiator (nsdsai_sd)  |  |  | nsdsai_sd  | additional.fields.key and additional.fields.value.string_value   
Application Subcategory (subcategory_of_app)  |  |  | subcategory_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Category (category_of_app)  |  |  | category_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Technology (technology_of_app)  |  |  | technology_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Risk (risk_of_app)  |  |  | risk_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Characteristic (characteristic_of_app)  |  |  | characteristic_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Container (container_of_app)  |  |  | container_of_app  | additional.fields.key and additional.fields.value.string_value   
Application SaaS (is_saas_of_app)  |  |  | is_saas_of_app  | additional.fields.key and additional.fields.value.string_value   
Application Sanctioned State (sanctioned_state_of_app)  |  |  | sanctioned_state_of_app  | additional.fields.key and additional.fields.value.string_value   
  
### SCTP

CSV field | CEF field | LEEF field | Google Security Operations label key | UDM field  
---|---|---|---|---  
Receive Time (receive_time or cef-formatted-receive_time) |  |  | receive_time or cef-formatted-receive_time | metadata.collected_timestamp  
Serial Number (serial) |  |  | serial | intermediary.asset.hardware.serial_number  
Type (type) |  |  | type | metadata.product_event_type  
Generated Time (time_generated or cef-formatted-time_generated) |  |  | time_generated or cef-formatted-time_generated | metadata.event_timestamp  
Source Address (src) |  |  | src | principal.ip  
Destination Address (dst) |  |  | dst | target.ip  
Rule Name (rule) |  |  | rule | security_result.rule_name  
Source Zone (from) |  |  | from | additional.fields.key and additional.fields.value.string_value  
Destination Zone (to) |  |  | to | additional.fields.key and additional.fields.value.string_value  
Inbound Interface (inbound_if) |  |  | inbound_if | additional.fields.key and additional.fields.value.string_value  
Outbound Interface (outbound_if) |  |  | outbound_if | additional.fields.key and additional.fields.value.string_value  
Log Action (logset) |  |  | logset | additional.fields.key and additional.fields.value.string_value  
Session ID (sessionid) |  |  | sessionid | network.session_id  
Repeat Count (repeatcnt) |  |  | repeatcnt | additional.fields.key and additional.fields.value.string_value  
Source Port (sport) |  |  | sport | principal.port  
Destination Port (dport) |  |  | dport | target.port  
IP Protocol (proto) |  |  | proto | network.ip_protocol (enum)  
Action (action) |  |  | action | security_result.action_details  
security_result.action  
Device Group Hierarchy (dg_hier_level_1 to dg_hier_level_4) |  |  | dg_hier_level_1 to dg_hier_level_4 | additional.fields.key and additional.fields.value.string_value  
Device Name (device_name) |  |  | device_name | intermediary.hostname  
Sequence Number (seqno) |  |  | seqno | metadata.product_log_id  
SCTP Association ID (assoc_id) |  |  | assoc_id | additional.fields.key and additional.fields.value.string_value  
Payload Protocol ID (ppid) |  |  | ppid | additional.fields.key and additional.fields.value.string_value  
Severity (severity) |  |  | severity | security_result.severity and security_result.severity_details  
SCTP Chunk Type (sctp_chunk_type) |  |  | sctp_chunk_type | additional.fields.key and additional.fields.value.string_value  
SCTP Event Type (sctp_event_type) |  |  | sctp_event_type | additional.fields.key and additional.fields.value.string_value  
SCTP Verification Tag 1 (verif_tag_1) |  |  | verif_tag_1 | additional.fields.key and additional.fields.value.string_value  
SCTP Verification Tag 2 (verif_tag_2) |  |  | verif_tag_2 | additional.fields.key and additional.fields.value.string_value  
SCTP Cause Code (sctp_cause_code) |  |  | sctp_cause_code | additional.fields.key and additional.fields.value.string_value  
Diameter App ID (diam_app_id) |  |  | diam_app_id | additional.fields.key and additional.fields.value.string_value  
Diameter Command Code (diam_cmd_code) |  |  | diam_cmd_code | additional.fields.key and additional.fields.value.string_value  
Diameter AVP Code (diam_avp_code) |  |  | diam_avp_code | additional.fields.key and additional.fields.value.string_value  
SCTP Stream ID (stream_id) |  |  | stream_id | additional.fields.key and additional.fields.value.string_value  
SCTP Association End Reason (assoc_end_reason) |  |  | assoc_end_reason | additional.fields.key and additional.fields.value.string_value  
Op Code (op_code) |  |  | op_code | additional.fields.key and additional.fields.value.string_value  
SCCP Calling Party SSN (sccp_calling_ssn) |  |  | sccp_calling_ssn | additional.fields.key and additional.fields.value.string_value  
SCCP Calling Party Global Title (sccp_calling_gt) |  |  | sccp_calling_gt | additional.fields.key and additional.fields.value.string_value  
SCTP Filter (sctp_filter) |  |  | sctp_filter | additional.fields.key and additional.fields.value.string_value  
SCTP Chunks (chunks) |  |  | chunks | additional.fields.key and additional.fields.value.string_value  
SCTP Chunks Sent (chunks_sent) |  |  | chunks_sent | additional.fields.key and additional.fields.value.string_value  
SCTP Chunks Received (chunks_received) |  |  | chunks_received | additional.fields.key and additional.fields.value.string_value  
Packets (packets) |  |  | packets | additional.fields.key and additional.fields.value.string_value  
UUID for rule (rule_uuid) |  |  | rule_uuid | security_result.rule_id  
Virtual System (vsys) |  |  | vsys | intermediary.asset.attribute.labels.key/value  
Virtual System Name (vsys_name) |  |  | vsys_name | intermediary.asset.attribute.labels.key/value  
Packets Sent (pkts_sent) |  |  | pkts_sent | network.sent_packets  
Packets Received (pkts_received) |  |  | pkts_received | network.received_packets  
  
### Audit

CSV field | CEF field | LEEF field | Google Security Operations label key | UDM field  
---|---|---|---|---  
Generate Time |  |  |  | metadata.event_timestamp  
Type |  |  |  | metadata.product_event_type  
Content Type (subtype) |  |  |  | metadata.product_event_type  
Event ID |  |  |  | additional.fields.key and additional.fields.value.string_value  
Object |  |  |  | principal.user.userid  
Description |  |  |  | metadata.description  
Status |  |  |  | additional.fields.key and additional.fields.value.string_value  
Serial Number |  |  |  | intermediary.asset.hardware.serial_number  
  
### Field mapping reference: Log types to UDM event type

The following table lists the Palo Alto Networks firewall log types and their corresponding UDM event types. 

**Log type** | **UDM event type**  
---|---  
Traffic  | NETWORK_CONNECTION   
Threat  | NETWORK_CONNECTION   
URL Filtering  | NETWORK_CONNECTION   
WildFire  | SCAN_UNCATEGORIZED  WildFire submissions logs are a subtype of Threat log type and use the same syslog format.   
Data Filtering  | NETWORK_UNCATEGORIZED   
Globalprotect  | USER_LOGIN/USER_LOGOUT/USER_RESOURCE_ACCESS  If Event ID (eventid) log field contains value either "auth" or "login" or Stage (stage) log field contains value "login", then USER_LOGIN is set. If Event ID (eventid) log field contains value "logout" or Stage (stage) log field contains value "logout", then USER_LOGOUT is set.  If Event ID (eventid) or Stage (stage) log fields contains any other value, then USER_RESOURCE_ACCESS is set.   
Tunnel  | NETWORK_CONNECTION   
GTP  | NETWORK_CONNECTION   
Config  | SETTING_MODIFICATION/SETTING_CREATION/SETTING_DELETION/SETTING_UNCATEGORIZED  The value of the "Command (cmd)" field determines the UDM event type mapping. If the cmd field value is add or clone, SETTING_CREATION is set.  If the cmd field value is delete, SETTING_DELETION is set. If the cmd field value is edit, move, rename, set, or commit, SETTING_MODIFICATION is set. If the cmd field value does not contain any values, then SETTING_UNCATEGORIZED is set.   
System  |  If the subtype value is "dhcp", then NETWORK_DHCP is set. If the subtype value is "auth", then USER_LOGIN is set.  If the description value is "logged in", then USER_LOGIN is set.  If the description value is "logged out", then USER_LOGOUT is set.  For other values of the subtype, GENERIC_EVENT is set.   
HIP Match  | NETWORK_CONNECTION   
IP Tag  | GENERIC_EVENT   
User-ID  | USER_LOGIN/USER_LOGOUT/USER_UNCATEGORIZED  If subtype value is "login", then USER_LOGIN is set. If subtype value is "logout", then USER_LOGOUT is set.  If subtype does not contain any value, then USER_UNCATEGORIZED is set.   
Decryption  | NETWORK_CONNECTION   
Authentication  | STATUS_UNCATEGORIZED   
SCTP  | NETWORK_CONNECTION   
Audit  | GENERIC_EVENT   
CORRELATION  | GENERIC_EVENT   
  
## Palo Alto Networks Firewall Strata Logging Service

### Overview

Palo Alto Networks Strata Logging Service provides cloud-based, centralized log storage and aggregation for your on-premises and virtual (private cloud and public cloud) firewalls, for Prisma Access, and for cloud-delivered services such as Cortex XDR. Strata Logging Service is secure, resilient, and fault-tolerant, and it helps ensure that your logging data is up-to-date and available when you need it. Strata Logging Service provides a scalable logging infrastructure that alleviates the need to plan and deploy Log Collectors to meet your log retention needs. If you already have on-premises Log Collectors, then Strata Logging Service can complement your existing setup to expand operational capacity as your business grows, or to meet the capacity needs for new locations. With this service, Palo Alto Networks manages the ongoing maintenance and monitoring of the logging infrastructure.

This section describes how to configure Palo Alto Networks Next-Generation Firewalls (NGFW) to generate logs, forward them to Strata Logging Service, and deliver logs to Google SecOps using an HTTPS webhook.

The following table describes the supported platforms, management modes, PAN-OS versions, and destination settings for this deployment:

Category | Supported configurations  
---|---  
Firewall platforms |  All Palo Alto Networks NGFW platforms:

  * **Physical hardware** : PA-400, PA-800, PA-3200, PA-5200, and PA-7000 Series
  * **VM-Series** : virtual firewall on VMware, AWS, Azure, Google Cloud, KVM, and Hyper-V
  * **CN-Series** : containerized firewall for Kubernetes environments

  
Management mode | 

  * **Standalone** : firewall managed directly using the PAN-OS web UI or CLI
  * **Panorama-managed** : centrally managed using a Panorama appliance or Panorama in the cloud

  
PAN-OS version |  PAN-OS 10.0 and later (11.x recommended)  
Google SecOps destination |  Google SecOps using Strata Logging Service HTTPS Log Forwarding (JSON Array formats)  
  
### Before you begin

Before you configure log forwarding through Strata Logging Service, verify the following prerequisites:

  * Verify the log formats and PAN-OS versions that the Strata Logging Service parser supports. The following table lists the log formats and the corresponding PAN-OS versions that the Strata Logging Service parser supports:

Log format | PAN-OS version  
---|---  
JSON Array | 10.0 and later  
  * Verify the Palo Alto Networks firewall log types that the Google SecOps parser supports. The Google SecOps parser supports the following Palo Alto Networks firewall log types:

    * Traffic
    * Threat
    * Tunnel inspection
    * System
    * HIP match
    * IP-Tag
    * User-ID
    * Decryption
    * Authentication
    * URL filtering
    * GlobalProtect
    * SCTP
    * Audit
  * **PAN-OS version** : Install PAN-OS 10.0 or later on all firewall platforms (PA-Series, VM-Series, and CN-Series). For general firewall setup instructions, see the [PAN-OS Administrator's Guide](https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/getting-started) and [Strata Logging Service deployment prerequisites](https://docs.paloaltonetworks.com/strata-logging-service/activation-and-onboarding/planning).

  * **Strata Logging Service license** : Ensure that the `PAN-LGS-DL` license is active on the same Customer Support Portal (CSP) account as the firewall.

  * **Cloud Logging enabled on all platforms** : On every firewall, go to **Device** > **Setup** > **Management** > **Cloud Logging** , select **Enable Cloud Logging** , and select your **Region**. This setting is required for VM-Series (PAVM), CN-Series, and physical firewalls.

**Note:** After you deploy a VM-Series (PAVM) firewall, go to **Device** > **Setup** > **Management** > **Cloud Logging** and enable **Cloud Logging** before proceeding. The firewall won't send logs to Strata Logging Service until you explicitly enable this setting.
  * **Network and firewall access** : Ensure that the firewall management interface can reach the following fully qualified domain names (FQDNs) on TCP port 443 without SSL decryption:

    * `api.paloaltonetworks.com`
    * `apitrusted.paloaltonetworks.com`
    * `certificate.paloaltonetworks.com`
    * `certificatetrusted.paloaltonetworks.com`
    * `lic.lc.prod.us.cs.paloaltonetworks.com`
  * **Administrator credentials** : Ensure that you have the `Superuser` or `device-admin` role on the firewall and access to the [Strata Hub console](https://stratacloudmanager.paloaltonetworks.com/).

  * **Google SecOps webhook URL** : Obtain the region-specific HTTPS endpoint URL from your Google SecOps instance (see Step 2: Configure the HTTPS forwarding profile).

  * **SSL/TLS certificate** : Obtain a valid CA certificate for the HTTPS webhook. Publicly trusted certificate authorities (CAs), such as GlobalSign and DigiCert, are pre-trusted by Strata Logging Service. If you use a self-signed or private CA certificate, then you must upload it manually.

  * **Panorama plugin (if Panorama-managed)** : Install Cloud Services Plugin 2.x or later on Panorama.




### Architecture overview

Log ingestion through Strata Logging Service follows a three-stage pipeline from your PAN-OS firewalls to Google SecOps:

  1. **PAN-OS NGFW** (PA-Series, VM-Series, or CN-Series) forwards logs over Cloud Logging (TLS on TCP port 443).
  2. **Strata Logging Service** (https://stratacloudmanager.paloaltonetworks.com/) normalizes, indexes, and stores logs in regional cloud storage.
  3. **Google SecOps** (`chronicle.googleapis.com` region-specific endpoint) receives GZIP-compressed JSON Array payloads from Strata Logging Service over an HTTPS webhook.



The following table describes each stage of the log forwarding architecture:

Stage | Component | Transport | Description  
---|---|---|---  
Phase 1 |  **PAN-OS NGFW** (PA-Series, VM-Series, CN-Series; standalone or Panorama-managed) | Cloud Logging (TLS on TCP port 443) |  The firewall generates various types of logs. A **Log Forwarding Profile** is assigned to Security Policy rules to activate log forwarding. Cloud Logging must be explicitly enabled on each firewall.  
Phase 2 |  **Strata Logging Service** (`(https://stratacloudmanager.paloaltonetworks.com/)`, regional cloud storage) | Cloud storage (indexed and normalized) |  Palo Alto Networks cloud-native logging infrastructure receives logs from all onboarded firewalls, and normalizes and indexes them. This service provides the **Log Forwarding** application to push logs outbound to external platforms, and supports up to 200 destinations per instance.  
Phase 3 |  **Google SecOps** (`chronicle.googleapis.com`, region-specific URL) | HTTPS webhook, JSON Array (GZIP-compressed) |  Strata Log Forwarding pushes logs to Google SecOps using HTTPS POST. An SSL/TLS certificate and **Basic Authorization** credentials help secure the connection. The Google SecOps URL must match your Strata Logging Service region.  
  
### Phase 1: Generate logs on the PAN-OS firewall

To configure your PAN-OS firewall to generate and forward security and system logs, complete the following steps:

  1. Go to **Device** > **Log Settings**. Confirm that **System** , **Configuration** , and **HIP Match** logs are active with appropriate severity levels (minimum **Informational** for **System** logs). PAN-OS generates these system-level logs automatically without requiring an additional profile.
  2. Go to **Objects** > **Log Forwarding** > **Add** to create a log forwarding profile. Define the log types to forward: **Traffic** , **Threat** , **WildFire** , **URL Filtering** , and **Auth**. Assign a server profile (**Syslog** or **HTTP**) and configure filters if required.
  3. Go to **Policies** > **Security** , edit each rule, and select the **Actions** tab. Select your **Log Forwarding** profile, and select **Log at Session End** (and optionally **Log at Session Start**). Click **OK** , and then click **Commit**.



For more information, see the following Palo Alto Networks resources:

  * [Configure log forwarding on PAN-OS](https://docs.paloaltonetworks.com/ngfw/administration/monitoring/configure-log-forwarding)
  * [Configure a log forwarding profile](https://docs.paloaltonetworks.com/network-security/security-policy/administration/objects/log-forwarding/configure-a-log-forwarding-profile-pm)
  * [Configure syslog monitoring](https://docs.paloaltonetworks.com/ngfw/administration/monitoring/use-syslog-for-monitoring/configure-syslog-monitoring)



### Phase 2: Onboard and forward logs to Strata

To activate Strata Logging Service, onboard your firewalls, and verify log delivery, complete the following steps:

  1. Sign in to the [Strata Hub console](https://stratacloudmanager.paloaltonetworks.com/) and activate your `PAN-LGS-DL` license. Select your **CSP Account** , **Tenant/TSG** , and the **Region** where logs will be stored.
  2. On each firewall (including PA-Series, VM-Series, and CN-Series), go to **Device** > **Setup** > **Management** > **Cloud Logging** :

     1. Select **Enable Cloud Logging**.
     2. Select the **Region** that matches your Strata Logging Service instance.
     3. Optional: To send log copies to both Strata Logging Service and on-premises Panorama, select **Enable Duplicate Logging**.
     4. Click **OK** , and then click **Commit**.
**Note:** In PAN-OS versions earlier than 10.1, this setting might appear as **Cortex Data Lake** or **Logging Service**. For CN-Series firewalls, go to the **Cloud Logging** pane in Panorama, select **Enable Cloud Logging** , and click **Commit & Push**.
  3. Verify connectivity between the firewall and Strata Logging Service:

     1. Go to **Device** > **Setup** > **Management** > **Cloud Logging** , and click **Show Status**. Confirm that the status displays **Connected**.
     2. Open **Strata Log Viewer** in the Strata Hub console to confirm that logs are arriving.
     3. To verify connectivity from the PAN-OS CLI, run the following command:
            
            show logging-status
            

  4. Optional: To capture DNS queries, HTTP user-agent strings, and session metadata (required for Cortex XSIAM and IoT Security), in the **Cloud Logging** settings, select **Enable Enhanced Application Logging**.


**Warning:** Don't enable SSL/TLS decryption for traffic destined to Strata Logging Service FQDNs. Strata Logging Service uses mutual TLS authentication; enabling decryption breaks the connection and stops log delivery.

For more information, see the following Palo Alto Networks resources:

  * [Onboard firewalls to Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service/activation-and-onboarding/onboard-overview)
  * [Start sending logs to Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service/activation-and-onboarding/start-sending-logs)
  * [Strata Logging Service deployment prerequisites and planning](https://docs.paloaltonetworks.com/strata-logging-service/activation-and-onboarding/planning)
  * [Guide to onboard and ingest logs from firewalls to Strata](https://live.paloaltonetworks.com/t5/community-blogs/guide-to-onboard-and-ingest-logs-from-firewalls-to-strata/ba-p/1233567)



### Phase 3: Configure an HTTPS webhook to forward logs

To forward logs from Strata Logging Service to Google SecOps using an HTTPS webhook, complete the following steps.

**Note:** A valid CA certificate must be in place before you can save or test the HTTPS webhook. Strata Logging Service uses this certificate to authenticate your HTTPS receiver (server authentication). Publicly trusted CAs, such as GlobalSign and DigiCert, are trusted by default and don't require an upload. If you use a self-signed or private PKI CA, then upload the CA certificate file using **Upload CA Certificate**.

#### Step 1: Configure a Google SecOps pipeline with the Unroll processor

To split Palo Alto Networks Strata Logging Service JSON Array logs into individual log events using the **Unroll** processor, complete the following steps:

  1. Create a [webhook feed](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#setup-webhook) for the **Palo Alto Networks Firewall** (`PAN_FIREWALL`) log type. Generate the webhook URL using the following format:
         
         ENDPOINT_URL?key=API_KEY&secret=SECRET
         

  2. Create a [Google SecOps data processing pipeline](https://docs.cloud.google.com/chronicle/docs/ingestion/data-processing-pipeline) and [add a stream](https://docs.cloud.google.com/chronicle/docs/ingestion/data-processing-pipeline#configure_streams) using the webhook feed that you created.

  3. Add a **Parse JSON** processor to parse the raw JSON payload (this is a [requirement](https://docs.cloud.google.com/chronicle/docs/ingestion/data-processing-pipeline#configure-processors) for the **Unroll** processor).

  4. Add an **Unroll** processor to split the JSON Array logs into individual log events, and then save and activate the pipeline.




#### Step 2: Configure the HTTPS forwarding profile

  1. To create an HTTPS forwarding profile, sign in to the [Strata Hub console](https://stratacloudmanager.paloaltonetworks.com/), open your Strata Logging Service instance, and go to **Log Forwarding** > **Add**.
  2. Configure the profile name and Google SecOps URL:

     * **Profile Name** : Enter a descriptive name (for example, `PAVM-Chronicle-HTTPS`). The **Profile Type** is preset to **Log Forwarding**.
     * **URL** : Enter the region-specific Google SecOps HTTPS webhook URL (beginning with `https://` on default port `443` in the format `ENDPOINT_URL?key=API_KEY&secret=SECRET`) that matches your Strata Logging Service region, as shown in the following table.

For more information, see [Set up a SIEM webhook](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#setup-webhook).

Strata Logging Service region | Google SecOps ingestion URL  
---|---  
US | `https://chronicle.googleapis.com`  
Europe | `https://europe-chronicle.googleapis.com`  
Asia | `https://asia-southeast1-chronicle.googleapis.com`  



#### Step 3: Configure server authentication

In the **Server Authentication** section, configure the SSL/TLS certificate for your HTTPS endpoint:

  1. If you use a self-signed or private CA, then drag the CA certificate file or click **Upload CA Certificate**. If you use a publicly trusted CA (for example, GlobalSign), then default public roots are already trusted and no upload is required. Click **Delete** only if you need to replace an existing certificate.
  2. Verify that the **Certificate Details** match your endpoint's CA. Ensure that your HTTPS receiver presents a TLS certificate signed by this CA; if the certificate chain doesn't match, then the **Test Connection** step fails.



You can download the root certificates from the **Root CAs** section on the [Google Trust Services repository](https://pki.goog/repository/) page.

The following table shows example certificate details displayed in the **Server Authentication** section:

Certificate field | Example value  
---|---  
Common name | `GlobalSign Root CA`  
Expires on | `1/28/2028`  
Issued by | `GlobalSign Root CA`  
Purpose | Server authentication (verifies the TLS certificate of your HTTPS receiver)  
  
#### Step 4: Configure client authentication and client authorization

Client authentication lets Google SecOps verify that incoming requests originate from Strata Logging Service. Client authorization provides the credentials that Strata Logging Service uses when calling your Google SecOps endpoint.

In the **Client Authorization** section, configure the following fields:

  * **Type** : Select **Basic Authorization**.
  * **Username** : Enter a placeholder value, such as `test`. The Google SecOps HTTPS endpoint doesn't require a username.
  * **Password** : Enter a placeholder value, such as `test`. The Google SecOps HTTPS endpoint doesn't require a password.



The following table describes the client authorization configuration for Google SecOps:

Authorization type | When to use | Configuration for Google SecOps  
---|---|---  
Basic Authorization | HTTPS receiver requires username and password credentials | Enter a placeholder value, such as `test`, for both the username and password because the Google SecOps HTTPS endpoint doesn't require these credentials  
  
#### Step 5: Test the connection and save

  1. Click **Test Connection** at the bottom of the **Client Authorization** section. Strata Logging Service sends a test payload to your Google SecOps HTTPS endpoint: 
     * **Success** : The status indicates that the connection succeeded. Click **Next**.
     * **Failure** : Verify the CA certificate match, confirm that the Google SecOps URL matches your region, check your credentials, and ensure that the endpoint accepts GZIP-compressed JSON Array payloads.
  2. After **Test Connection** succeeds, click **Next**.
  3. In the **Payload Format** list, select **Array JSON**.
  4. Select the log types to forward to Google SecOps:

     * **Traffic logs** (`action = deny` is recommended for high-value alerts)
     * **Threat logs** (`severity >= High`)
     * **WildFire logs**
     * **System and Auth logs** (`severity = Critical`)
  5. Click **Save**. Generate a test event on the firewall (for example, access a blocked URL) and verify that the event appears in the Google SecOps console within 1 to 5 minutes.




For more information, see the following Palo Alto Networks resources:

  * [Forward logs to an HTTPS server](https://docs.paloaltonetworks.com/strata-logging-service/administration/forward-logs/forward-logs-to-an-https-server)
  * [Forward logs from Strata Logging Service](https://docs.paloaltonetworks.com/strata-logging-service/administration/forward-logs)
  * [Forward logs to a Syslog server](https://docs.paloaltonetworks.com/strata-logging-service/administration/forward-logs/forward-logs-to-syslog-server)
  * [Server certificate validation](https://docs.paloaltonetworks.com/strata-logging-service/administration/forward-logs/server-certificate-validation)
  * [Log Forwarding API release notes](https://pan.dev/cdl/docs/logforwarding/release-notes/relnotes)
  * [Strata Logging Service log reference](https://docs.paloaltonetworks.com/strata-logging-service/log-reference)
  * [Strata Logging Service administration overview](https://docs.paloaltonetworks.com/strata-logging-service/administration/overview)



### Supported log formats

The Palo Alto Networks Strata Logging Service firewall parser supports logs in JSON and JSON Array formats.

### Supported sample logs

The following sample logs show the supported Strata Logging Service formats:

  * JSON Array
        
        [{  "TimeReceived": "2026-06-23T10:20:00.000000Z",  "DeviceSN": "023201024129",  "LogType": "TRAFFIC",  "Subtype": "end",  "ConfigVersion": "11.2",  "TimeGenerated": "2026-06-23T10:19:50.000000Z",  "SourceAddress": "198.51.100.0",  "DestinationAddress": "198.51.100.1",  "NATSource": "198.51.100.2",  "NATDestination": "198.51.100.1",  "Rule": "PAMGMT_INTERNET_RULE",  "SourceUser": null,  "DestinationUser": null,  "Application": "dns-base",  "VirtualLocation": "vsys1",  "FromZone": "Vlan-Zone",  "ToZone": "outside",  "InboundInterface": "ethernet1/6.20",  "OutboundInterface": "ethernet1/5",  "LogSetting": "IoT Security Default Profile",  "SessionID": 141475,  "RepeatCount": 1,  "SourcePort": 47343,  "DestinationPort": 53,  "NATSourcePort": 35449,  "NATDestinationPort": 53,  "Protocol": "udp",  "Action": "allow",  "Bytes": 354,  "BytesSent": 149,  "BytesReceived": 205,  "PacketsTotal": 2,  "SessionStartTime": "2026-06-23T10:19:22.000000Z",  "SessionDuration": 1,  "URLCategory": "any",  "SequenceNo": 7650419021796487925,  "SourceLocation": "198.51.100.3-198.51.100.4",  "DestinationLocation": "US",  "PacketsSent": 1,  "PacketsReceived": 1,  "SessionEndReason": "aged-out",  "DGHierarchyLevel1": 0,  "DGHierarchyLevel2": 0,  "DGHierarchyLevel3": 0,  "DGHierarchyLevel4": 0,  "VirtualSystemName": "",  "DeviceName": "PA-450",  "ActionSource": "from-policy",  "SourceUUID": null,  "DestinationUUID": null,  "IMSI": 0,  "IMEI": null,  "ParentSessionID": 0,  "ParentStarttime": "1970-01-01T00:00:00.000000Z",  "Tunnel": "N/A",  "EndpointAssociationID": 0,  "ChunksTotal": 0,  "ChunksSent": 0,  "ChunksReceived": 0,  "RuleUUID": "29222f63-8656-476f-b70e-6ec3332ff5fe",  "HTTP2Connection": 0,  "LinkChangeCount": 0,  "SDWANPolicyName": null,  "LinkSwitches": null,  "SDWANCluster": null,  "SDWANDeviceType": null,  "SDWANClusterType": null,  "SDWANSite": null,  "DynamicUserGroupName": null,  "X-Forwarded-ForIP": "",  "SourceDeviceCategory": null,  "SourceDeviceProfile": null,  "SourceDeviceModel": null,  "SourceDeviceVendor": null,  "SourceDeviceOSFamily": null,  "SourceDeviceOSVersion": null,  "SourceDeviceHost": null,  "SourceDeviceMac": null,  "DestinationDeviceCategory": null,  "DestinationDeviceProfile": null,  "DestinationDeviceModel": null,  "DestinationDeviceVendor": null,  "DestinationDeviceOSFamily": null,  "DestinationDeviceOSVersion": null,  "DestinationDeviceHost": null,  "DestinationDeviceMac": null,  "ContainerID": null,  "ContainerNameSpace": null,  "ContainerName": null,  "SourceEDL": null,  "DestinationEDL": null,  "GPHostID": null,  "EndpointSerialNumber": null,  "SourceDynamicAddressGroup": null,  "DestinationDynamicAddressGroup": null,  "HASessionOwner": null,  "TimeGeneratedHighResolution": "2026-06-23T10:19:51.048000Z",  "NSSAINetworkSliceType": null,  "NSSAINetworkSliceDifferentiator": null},{  "TimeReceived": "2026-06-23T10:20:00.000000Z",  "DeviceSN": "023201024129",  "LogType": "TRAFFIC",  "Subtype": "end",  "ConfigVersion": "11.2",  "TimeGenerated": "2026-06-23T10:19:51.000000Z",  "SourceAddress": "198.51.100.0",  "DestinationAddress": "198.51.100.1",  "NATSource": "198.51.100.5",  "NATDestination": "198.51.100.1",  "Rule": "PAMGMT_INTERNET_RULE",  "SourceUser": null,  "DestinationUser": null,  "Application": "dns-base",  "VirtualLocation": "vsys1",  "FromZone": "Vlan-Zone",  "ToZone": "outside",  "InboundInterface": "ethernet1/6.20",  "OutboundInterface": "ethernet1/8",  "LogSetting": "IoT Security Default Profile",  "SessionID": 195791,  "RepeatCount": 1,  "SourcePort": 53359,  "DestinationPort": 53,  "NATSourcePort": 51905,  "NATDestinationPort": 53,  "Protocol": "udp",  "Action": "allow",  "Bytes": 278,  "BytesSent": 133,  "BytesReceived": 145,  "PacketsTotal": 2,  "SessionStartTime": "2026-06-23T10:19:22.000000Z",  "SessionDuration": 1,  "URLCategory": "any",  "SequenceNo": 7650419021796487926,  "SourceLocation": "198.51.100.3-198.51.100.4",  "DestinationLocation": "US",  "PacketsSent": 1,  "PacketsReceived": 1,  "SessionEndReason": "aged-out",  "DGHierarchyLevel1": 0,  "DGHierarchyLevel2": 0,  "DGHierarchyLevel3": 0,  "DGHierarchyLevel4": 0,  "VirtualSystemName": "",  "DeviceName": "PA-450",  "ActionSource": "from-policy",  "SourceUUID": null,  "DestinationUUID": null,  "IMSI": 0,  "IMEI": null,  "ParentSessionID": 0,  "ParentStarttime": "1970-01-01T00:00:00.000000Z",  "Tunnel": "N/A",  "EndpointAssociationID": 0,  "ChunksTotal": 0,  "ChunksSent": 0,  "ChunksReceived": 0,  "RuleUUID": "29222f63-8656-476f-b70e-6ec3332ff5fe",  "HTTP2Connection": 0,  "LinkChangeCount": 0,  "SDWANPolicyName": null,  "LinkSwitches": null,  "SDWANCluster": null,  "SDWANDeviceType": null,  "SDWANClusterType": null,  "SDWANSite": null,  "DynamicUserGroupName": null,  "X-Forwarded-ForIP": "",  "SourceDeviceCategory": null,  "SourceDeviceProfile": null,  "SourceDeviceModel": null,  "SourceDeviceVendor": null,  "SourceDeviceOSFamily": null,  "SourceDeviceOSVersion": null,  "SourceDeviceHost": null,  "SourceDeviceMac": null,  "DestinationDeviceCategory": null,  "DestinationDeviceProfile": null,  "DestinationDeviceModel": null,  "DestinationDeviceVendor": null,  "DestinationDeviceOSFamily": null,  "DestinationDeviceOSVersion": null,  "DestinationDeviceHost": null,  "DestinationDeviceMac": null,  "ContainerID": null,  "ContainerNameSpace": null,  "ContainerName": null,  "SourceEDL": null,  "DestinationEDL": null,  "GPHostID": null,  "EndpointSerialNumber": null,  "SourceDynamicAddressGroup": null,  "DestinationDynamicAddressGroup": null,  "HASessionOwner": null,  "TimeGeneratedHighResolution": "2026-06-23T10:19:51.048000Z",  "NSSAINetworkSliceType": null,  "NSSAINetworkSliceDifferentiator": null},{  "TimeReceived": "2026-06-23T10:20:00.000000Z",  "DeviceSN": "023201024129",  "LogType": "TRAFFIC",  "Subtype": "end",  "ConfigVersion": "11.2",  "TimeGenerated": "2026-06-23T10:19:51.000000Z",  "SourceAddress": "198.51.100.6",  "DestinationAddress": "198.51.100.1",  "NATSource": "198.51.100.2",  "NATDestination": "198.51.100.1",  "Rule": "PAMGMT_INTERNET_RULE",  "SourceUser": null,  "DestinationUser": null,  "Application": "dns-base",  "VirtualLocation": "vsys1",  "FromZone": "Vlan-Zone",  "ToZone": "outside",  "InboundInterface": "ethernet1/6.20",  "OutboundInterface": "ethernet1/5",  "LogSetting": "IoT Security Default Profile",  "SessionID": 262531,  "RepeatCount": 1,  "SourcePort": 56168,  "DestinationPort": 53,  "NATSourcePort": 32784,  "NATDestinationPort": 53,  "Protocol": "udp",  "Action": "allow",  "Bytes": 351,  "BytesSent": 149,  "BytesReceived": 202,  "PacketsTotal": 2,  "SessionStartTime": "2026-06-23T10:19:23.000000Z",  "SessionDuration": 0,  "URLCategory": "any",  "SequenceNo": 7650419021796487928,  "SourceLocation": "198.51.100.3-198.51.100.4",  "DestinationLocation": "US",  "PacketsSent": 1,  "PacketsReceived": 1,  "SessionEndReason": "aged-out",  "DGHierarchyLevel1": 0,  "DGHierarchyLevel2": 0,  "DGHierarchyLevel3": 0,  "DGHierarchyLevel4": 0,  "VirtualSystemName": "",  "DeviceName": "PA-450",  "ActionSource": "from-policy",  "SourceUUID": null,  "DestinationUUID": null,  "IMSI": 0,  "IMEI": null,  "ParentSessionID": 0,  "ParentStarttime": "1970-01-01T00:00:00.000000Z",  "Tunnel": "N/A",  "EndpointAssociationID": 0,  "ChunksTotal": 0,  "ChunksSent": 0,  "ChunksReceived": 0,  "RuleUUID": "29222f63-8656-476f-b70e-6ec3332ff5fe",  "HTTP2Connection": 0,  "LinkChangeCount": 0,  "SDWANPolicyName": null,  "LinkSwitches": null,  "SDWANCluster": null,  "SDWANDeviceType": null,  "SDWANClusterType": null,  "SDWANSite": null,  "DynamicUserGroupName": null,  "X-Forwarded-ForIP": "",  "SourceDeviceCategory": null,  "SourceDeviceProfile": null,  "SourceDeviceModel": null,  "SourceDeviceVendor": null,  "SourceDeviceOSFamily": null,  "SourceDeviceOSVersion": null,  "SourceDeviceHost": null,  "SourceDeviceMac": null,  "DestinationDeviceCategory": null,  "DestinationDeviceProfile": null,  "DestinationDeviceModel": null,  "DestinationDeviceVendor": null,  "DestinationDeviceOSFamily": null,  "DestinationDeviceOSVersion": null,  "DestinationDeviceHost": null,  "DestinationDeviceMac": null,  "ContainerID": null,  "ContainerNameSpace": null,  "ContainerName": null,  "SourceEDL": null,  "DestinationEDL": null,  "GPHostID": null,  "EndpointSerialNumber": null,  "SourceDynamicAddressGroup": null,  "DestinationDynamicAddressGroup": null,  "HASessionOwner": null,  "TimeGeneratedHighResolution": "2026-06-23T10:19:51.048000Z",  "NSSAINetworkSliceType": null,  "NSSAINetworkSliceDifferentiator": null},{  "TimeReceived": "2026-06-23T10:20:00.000000Z",  "DeviceSN": "023201024129",  "LogType": "TRAFFIC",  "Subtype": "end",  "ConfigVersion": "11.2",  "TimeGenerated": "2026-06-23T10:19:53.000000Z",  "SourceAddress": "198.51.100.0",  "DestinationAddress": "198.51.100.1",  "NATSource": "198.51.100.2",  "NATDestination": "198.51.100.1",  "Rule": "PAMGMT_INTERNET_RULE",  "SourceUser": null,  "DestinationUser": null,  "Application": "dns-base",  "VirtualLocation": "vsys1",  "FromZone": "Vlan-Zone",  "ToZone": "outside",  "InboundInterface": "ethernet1/6.20",  "OutboundInterface": "ethernet1/5",  "LogSetting": "IoT Security Default Profile",  "SessionID": 76996,  "RepeatCount": 1,  "SourcePort": 49024,  "DestinationPort": 53,  "NATSourcePort": 9559,  "NATDestinationPort": 53,  "Protocol": "udp",  "Action": "allow",  "Bytes": 342,  "BytesSent": 145,  "BytesReceived": 197,  "PacketsTotal": 2,  "SessionStartTime": "2026-06-23T10:19:24.000000Z",  "SessionDuration": 1,  "URLCategory": "any",  "SequenceNo": 7650419021796489539,  "SourceLocation": "198.51.100.3-198.51.100.4",  "DestinationLocation": "US",  "PacketsSent": 1,  "PacketsReceived": 1,  "SessionEndReason": "aged-out",  "DGHierarchyLevel1": 0,  "DGHierarchyLevel2": 0,  "DGHierarchyLevel3": 0,  "DGHierarchyLevel4": 0,  "VirtualSystemName": "",  "DeviceName": "PA-450",  "ActionSource": "from-policy",  "SourceUUID": null,  "DestinationUUID": null,  "IMSI": 0,  "IMEI": null,  "ParentSessionID": 0,  "ParentStarttime": "1970-01-01T00:00:00.000000Z",  "Tunnel": "N/A",  "EndpointAssociationID": 0,  "ChunksTotal": 0,  "ChunksSent": 0,  "ChunksReceived": 0,  "RuleUUID": "29222f63-8656-476f-b70e-6ec3332ff5fe",  "HTTP2Connection": 0,  "LinkChangeCount": 0,  "SDWANPolicyName": null,  "LinkSwitches": null,  "SDWANCluster": null,  "SDWANDeviceType": null,  "SDWANClusterType": null,  "SDWANSite": null,  "DynamicUserGroupName": null,  "X-Forwarded-ForIP": "",  "SourceDeviceCategory": null,  "SourceDeviceProfile": null,  "SourceDeviceModel": null,  "SourceDeviceVendor": null,  "SourceDeviceOSFamily": null,  "SourceDeviceOSVersion": null,  "SourceDeviceHost": null,  "SourceDeviceMac": null,  "DestinationDeviceCategory": null,  "DestinationDeviceProfile": null,  "DestinationDeviceModel": null,  "DestinationDeviceVendor": null,  "DestinationDeviceOSFamily": null,  "DestinationDeviceOSVersion": null,  "DestinationDeviceHost": null,  "DestinationDeviceMac": null,  "ContainerID": null,  "ContainerNameSpace": null,  "ContainerName": null,  "SourceEDL": null,  "DestinationEDL": null,  "GPHostID": null,  "EndpointSerialNumber": null,  "SourceDynamicAddressGroup": null,  "DestinationDynamicAddressGroup": null,  "HASessionOwner": null,  "TimeGeneratedHighResolution": "2026-06-23T10:19:53.080000Z",  "NSSAINetworkSliceType": null,  "NSSAINetworkSliceDifferentiator": null},{  "TimeReceived": "2026-06-23T10:20:00.000000Z",  "DeviceSN": "023201024129",  "LogType": "TRAFFIC",  "Subtype": "end",  "ConfigVersion": "11.2",  "TimeGenerated": "2026-06-23T10:19:53.000000Z",  "SourceAddress": "198.51.100.0",  "DestinationAddress": "198.51.100.1",  "NATSource": "198.51.100.5",  "NATDestination": "198.51.100.1",  "Rule": "PAMGMT_INTERNET_RULE",  "SourceUser": null,  "DestinationUser": null,  "Application": "dns-base",  "VirtualLocation": "vsys1",  "FromZone": "Vlan-Zone",  "ToZone": "outside",  "InboundInterface": "ethernet1/6.20",  "OutboundInterface": "ethernet1/8",  "LogSetting": "IoT Security Default Profile",  "SessionID": 117181,  "RepeatCount": 1,  "SourcePort": 43566,  "DestinationPort": 53,  "NATSourcePort": 37003,  "NATDestinationPort": 53,  "Protocol": "udp",  "Action": "allow",  "Bytes": 348,  "BytesSent": 148,  "BytesReceived": 200,  "PacketsTotal": 2,  "SessionStartTime": "2026-06-23T10:19:24.000000Z",  "SessionDuration": 1,  "URLCategory": "any",  "SequenceNo": 7650419021796489538,  "SourceLocation": "198.51.100.3-198.51.100.4",  "DestinationLocation": "US",  "PacketsSent": 1,  "PacketsReceived": 1,  "SessionEndReason": "aged-out",  "DGHierarchyLevel1": 0,  "DGHierarchyLevel2": 0,  "DGHierarchyLevel3": 0,  "DGHierarchyLevel4": 0,  "VirtualSystemName": "",  "DeviceName": "PA-450",  "ActionSource": "from-policy",  "SourceUUID": null,  "DestinationUUID": null,  "IMSI": 0,  "IMEI": null,  "ParentSessionID": 0,  "ParentStarttime": "1970-01-01T00:00:00.000000Z",  "Tunnel": "N/A",  "EndpointAssociationID": 0,  "ChunksTotal": 0,  "ChunksSent": 0,  "ChunksReceived": 0,  "RuleUUID": "29222f63-8656-476f-b70e-6ec3332ff5fe",  "HTTP2Connection": 0,  "LinkChangeCount": 0,  "SDWANPolicyName": null,  "LinkSwitches": null,  "SDWANCluster": null,  "SDWANDeviceType": null,  "SDWANClusterType": null,  "SDWANSite": null,  "DynamicUserGroupName": null,  "X-Forwarded-ForIP": "",  "SourceDeviceCategory": null,  "SourceDeviceProfile": null,  "SourceDeviceModel": null,  "SourceDeviceVendor": null,  "SourceDeviceOSFamily": null,  "SourceDeviceOSVersion": null,  "SourceDeviceHost": null,  "SourceDeviceMac": null,  "DestinationDeviceCategory": null,  "DestinationDeviceProfile": null,  "DestinationDeviceModel": null,  "DestinationDeviceVendor": null,  "DestinationDeviceOSFamily": null,  "DestinationDeviceOSVersion": null,  "DestinationDeviceHost": null,  "DestinationDeviceMac": null,  "ContainerID": null,  "ContainerNameSpace": null,  "ContainerName": null,  "SourceEDL": null,  "DestinationEDL": null,  "GPHostID": null,  "EndpointSerialNumber": null,  "SourceDynamicAddressGroup": null,  "DestinationDynamicAddressGroup": null,  "HASessionOwner": null,  "TimeGeneratedHighResolution": "2026-06-23T10:19:53.080000Z",  "NSSAINetworkSliceType": null,  "NSSAINetworkSliceDifferentiator": null}]
        




### Field mapping reference: Logs fields to UDM fields

This section explains how the parser maps Palo Alto Networks Strata Logging Service firewall log fields to Google SecOps UDM event fields for each log type.

See the following sections for the mapping reference of each log type:

  * System
  * Threat
  * Traffic
  * User ID
  * HIP match
  * IP tag
  * Decryption
  * Tunnel
  * Authentication
  * URL
  * GlobalProtect
  * SCTP
  * Audit



### System

The following table lists the log fields of the System log type and their corresponding UDM fields.

Log field | UDM mapping  
---|---  
AgentContentVersion | additional.fields.key/value.string_value  
AgentDataCollectionStatus | target.resource.attribute.labels  
AgentID | target.resource.attribute.labels  
AgentIsolationStatus | target.resource.attribute.labels  
AgentStatus | target.resource.attribute.labels  
AgentVersion | target.asset.software.version  
ConfigVersion | additional.fields.key/value.string_value  
TenantID | metadata.product_deployment_id  
DeviceGroup | target.group.product_object_id  
DGHierarchyLevel1 | additional.fields.key/value.string_value  
DGHierarchyLevel2 | additional.fields.key/value.string_value  
DGHierarchyLevel3 | additional.fields.key/value.string_value  
DGHierarchyLevel4 | additional.fields.key/value.string_value  
EndpointCPUArchitecture | target.asset.hardware.cpu_platform  
EndpointDeviceDomain | target.asset.administrative_domain  
EndpointDeviceName | target.asset.hostname  
EndpointIPaddress | target.asset.ip  
VDIEndpoint | target.asset.attribute.labels  
EndpointOSType | additional.fields.key/value.string_value  
EndpointOSVersion | target.platform_version  
AgentTimeZoneOffset | additional.fields.key/value.string_value  
EndpointUserDomain | additional.fields.key/value.string_value  
EndpointUserName | target.user.user_display_name  
EndpointUserUUID | target.user.userid  
EventComponent | additional.fields.key/value.string_value  
EventDescription | metadata.description  
EventName | additional.fields.key/value.string_value  
EventTime | metadata.event_timestamp  
IsDuplicateLog | additional.fields.key/value.string_value  
LogExported | additional.fields.key/value.string_value  
LogForwarded | additional.fields.key/value.string_value  
IsPrismaNetwork | additional.fields.key/value.string_value  
IsPrismaUsers | additional.fields.key/value.string_value  
LogCategory | security_result.category_details  
LogSource | target.resource.attribute.labels  
LogSourceGroupID | target.resource.attribute.labels  
LogSourceID | target.resource.attribute.labels  
LogSourceName | target.resource.attribute.labels  
LogSourceTimeZoneOffset | additional.fields.key/value.string_value  
LogTime | metadata.collected_timestamp  
LogType | additional.fields.key/value.string_value  
PanoramaSN | observer.asset.hardware.serial_number  
PlatformType | additional.fields.key/value.string_value  
SequenceNo | metadata.product_log_id  
Severity | security_result.severity  
Subtype | metadata.product_event_type  
Template | target.resource.attribute.labels  
TimeGeneratedHighResolution | additional.fields.key/value.string_value  
VendorName | additional.fields.key/value.string_value  
VendorSeverity | security_result.severity_details  
VirtualLocation | target.asset.attribute.labels  
VirtualSystemID | target.resource.product_object_id  
VirtualSystemName | target.asset.attribute.labels  
  
### Threat

The following table lists the log fields of the Threat log type and their corresponding UDM fields.

Log field | UDM mapping  
---|---  
Action | security_result.action  
Application | target.application  
ApplicationCategory | additional.fields.key/value.string_value  
ApplicationSubcategory | additional.fields.key/value.string_value  
ApplianceOrCloud | additional.fields.key/value.string_value  
CloudHostname | additional.fields.key/value.string_value  
CloudReportID | security_result.detection_fields.key/value  
ConfigVersion | additional.fields.key/value.string_value  
ContainerID | intermediary.resource.product_object_id  
ApplicationContainer | additional.fields.key/value.string_value  
ContentVersion | additional.fields.key/value.string_value  
RepeatCount | additional.fields.key/value.string_value  
CortexDataLakeTenantID | metadata.product_deployment_id  
DestinationDeviceCategory | target.asset.category  
DestinationDeviceClass | additional.fields.key/value.string_value  
DestinationDeviceHost | target.asset.hostname  
DestinationDeviceMac | target.asset.mac  
DestinationDeviceModel | target.asset.hardware.model  
DestinationDeviceOS | additional.fields.key/value.string_value  
DestinationDeviceOSFamily | additional.fields.key/value.string_value  
DestinationDeviceOSVersion | target.platform_version  
DestinationDeviceProfile | additional.fields.key/value.string_value  
DestinationDeviceVendor | target.asset.hardware.manufacturer  
DestinationDynamicAddressGroup | target.group.group_display_name  
DestinationEDL | additional.fields.key/value.string_value  
DestinationAddress | target.ip  
DestinationLocation | target.location.country_or_region  
DestinationPort | target.port  
DestinationUser | target.user.userid  
DestinationUserDomain | target.administrative_domain  
DestinationUserName | target.user.user_display_name  
DestinationUserUUID | target.user.product_object_id  
DestinationUUID | target.resource.product_object_id  
DGHierarchyLevel1 | additional.fields.key/value.string_value  
DGHierarchyLevel2 | additional.fields.key/value.string_value  
DGHierarchyLevel3 | additional.fields.key/value.string_value  
DGHierarchyLevel4 | additional.fields.key/value.string_value  
DirectionOfAttack | security_result.detection_fields.key/value  
DomainEDL | additional.fields.key/value.string_value  
DynamicUserGroupName | additional.fields.key/value.string_value  
EndpointSerialNumber | principal.asset.hardware.serial_number  
FileName | target.file.names  
FileHash | target.file.sha1  
FileType | additional.fields.key/value.string_value  
FileURL | target.url  
FlowType | additional.fields.key/value.string_value  
FromZone | additional.fields.key/value.string_value  
HostID | principal.asset.asset_id  
HTTP2Connection | network.application_protocol_version  
HTTPMethod | network.http.method  
InboundInterface | additional.fields.key/value.string_value  
InboundInterfaceDetailsPort | additional.fields.key/value.string_value  
InboundInterfaceDetailsSlot | additional.fields.key/value.string_value  
InboundInterfaceDetailsType | additional.fields.key/value.string_value  
InboundInterfaceDetailsUnit | additional.fields.key/value.string_value  
CaptivePortal | additional.fields.key/value.string_value  
IsClienttoServer | additional.fields.key/value.string_value  
IsContainer | additional.fields.key/value.string_value  
IsDecryptMirror | additional.fields.key/value.string_value  
IsDecrypted | additional.fields.key/value.string_value  
IsDuplicateLog | additional.fields.key/value.string_value  
IsEncrypted | additional.fields.key/value.string_value  
LogExported | additional.fields.key/value.string_value  
LogForwarded | additional.fields.key/value.string_value  
IsIPV6 | additional.fields.key/value.string_value  
IsMptcpOn | additional.fields.key/value.string_value  
NAT | additional.fields.key/value.string_value  
IsNonStandardDestinationPort | additional.fields.key/value.string_value  
IsPacketCapture | additional.fields.key/value.string_value  
IsPhishing | additional.fields.key/value.string_value  
IsPrismaNetwork | additional.fields.key/value.string_value  
IsPrismaUsers | additional.fields.key/value.string_value  
IsProxy | additional.fields.key/value.string_value  
IsReconExcluded | additional.fields.key/value.string_value  
IsSaaSApplication | additional.fields.key/value.string_value  
IsServertoClient | additional.fields.key/value.string_value  
IsSourceXForwarded | additional.fields.key/value.string_value  
IsSystemReturn | additional.fields.key/value.string_value  
IsTransaction | additional.fields.key/value.string_value  
IsTunnelInspected | additional.fields.key/value.string_value  
IsURLDenied | additional.fields.key/value.string_value  
K8SClusterID | target.resource.attribute.labels  
LocalDeepLearningAnalyzed | additional.fields.key/value.string_value  
Location | observer.location.country_or_region  
LogSetting | intermediary.resource.attribute.labels  
LogSource | intermediary.resource.attribute.labels  
LogSourceGroupID | intermediary.resource.attribute.labels  
DeviceSN | intermediary.asset.hardware.serial_number  
DeviceName | intermediary.hostname  
LogSourceTimeZoneOffset | additional.fields.key/value.string_value  
TimeReceived | metadata.collected_timestamp  
LogType | additional.fields.key/value.string_value  
IMEI | additional.fields.key/value.string_value  
NATDestination | target.nat_ip  
NATDestinationPort | target.nat_port  
NATSource | principal.nat_ip  
NATSourcePort | principal.nat_port  
NonStandardDestinationPort | additional.fields.key/value.string_value  
NSSAINetworkSliceType | additional.fields.key/value.string_value  
OutboundInterface | additional.fields.key/value.string_value  
OutboundInterfaceDetailsPort | additional.fields.key/value.string_value  
OutboundInterfaceDetailsSlot | additional.fields.key/value.string_value  
OutboundInterfaceDetailsType | additional.fields.key/value.string_value  
OutboundInterfaceDetailsUnit | additional.fields.key/value.string_value  
PanoramaSN | observer.asset.hardware.serial_number  
ParentSessionID | network.parent_session_id  
ParentStarttime | additional.fields.key/value.string_value  
PartialHash | additional.fields.key/value.string_value  
PayloadProtocolID | additional.fields.key/value.string_value  
Packet | additional.fields.key/value.string_value  
PacketID | additional.fields.key/value.string_value  
PlatformType | additional.fields.key/value.string_value  
ContainerName | target.resource.name  
ContainerNameSpace | target.resource.attribute.labels  
Protocol | network.ip_protocol  
RecipientEmail | target.user.email_addresses  
ReportID | security_result.detection_fields.key/value  
ApplicationRisk | additional.fields.key/value.string_value  
Rule | security_result.rule_name  
RuleUUID | security_result.rule_id  
SanctionedStateOfApp | additional.fields.key/value.string_value  
SenderEmail | principal.user.email_addresses  
SequenceNo | metadata.product_log_id  
SessionID | network.session_id  
Severity | security_result.severity  
SigFlags | additional.fields.key/value.string_value  
SourceDeviceCategory | principal.asset.category  
SourceDeviceClass | additional.fields.key/value.string_value  
SourceDeviceHost | principal.hostname  
SourceDeviceMac | principal.asset.mac  
SourceDeviceModel | principal.asset.hardware.model  
SourceDeviceOS | additional.fields.key/value.string_value  
SourceDeviceOSFamily | additional.fields.key/value.string_value  
SourceDeviceOSVersion | principal.platform_version  
SourceDeviceProfile | additional.fields.key/value.string_value  
SourceDeviceVendor | principal.asset.hardware.manufacturer  
SourceDynamicAddressGroup | principal.group.group_display_name  
SourceEDL | additional.fields.key/value.string_value  
SourceAddress | principal.ip  
SourceLocation | principal.location.country_or_region  
SourcePort | principal.port  
SourceUser | principal.user.userid  
SourceUserDomain | principal.administrative_domain  
SourceUserName | principal.user.user_display_name  
SourceUserUUID | principal.user.product_object_id  
SourceUUID | principal.resource.product_object_id  
Subtype | metadata.product_event_type  
EmailSubject | network.email.subject  
ApplicationTechnology | additional.fields.key/value.string_value  
ThreatCategory | security_result.detection_fields.key/value.key/value  
ThreatID | security_result.threat_id  
ThreatName | security_result.threat_name  
ThreatNameFirewall | additional.fields.key/value.string_value  
TimeGenerated | metadata.event_timestamp  
TimeGeneratedHighResolution | additional.fields.key/value.string_value  
ToZone | additional.fields.key/value.string_value  
Tunnel | additional.fields.key/value.string_value  
TunneledApplication | additional.fields.key/value.string_value  
IMSI | additional.fields.key/value.string_value  
URLDomain | target.domain.name  
URLCounter | additional.fields.key/value.string_value  
Users | additional.fields.key/value.string_value  
VendorName | additional.fields.key/value.string_value  
VendorSeverity | security_result.severity_details  
Verdict | additional.fields.key/value.string_value  
VirtualLocation | intermediary.asset.attribute.labels  
VirtualSystemID | intermediary.resource.product_object_id  
VirtualSystemName | intermediary.asset.attribute.labels  
X-Forwarded-ForIP | principal.ip  
  
### Traffic

The following table lists the log fields of the Traffic log type and their corresponding UDM fields.

Log field | UDM mapping  
---|---  
Action | security_result.action  
ActionSource | additional.fields.key/value.string_value  
AIFwdError | additional.fields.key/value.string_value  
AITraffic | additional.fields.key/value.string_value  
Application | target.application  
ApplicationCategory | additional.fields.key/value.string_value  
ApplicationSubcategory | additional.fields.key/value.string_value  
BytesReceived | network.received_bytes  
BytesSent | network.sent_bytes  
Bytes | additional.fields.key/value.string_value  
ChunksReceived | additional.fields.key/value.string_value  
ChunksSent | additional.fields.key/value.string_value  
ChunksTotal | additional.fields.key/value.string_value  
ConfigVersion | additional.fields.key/value.string_value  
ContainerID | intermediary.resource.product_object_id  
ApplicationContainer | additional.fields.key/value.string_value  
RepeatCount | additional.fields.key/value.string_value  
CortexDataLakeTenantID | metadata.product_deployment_id  
DestinationDeviceCategory | target.asset.category  
DestinationDeviceClass | additional.fields.key/value.string_value  
DestinationDeviceHost | target.asset.hostname  
DestinationDeviceMac | target.asset.mac  
DestinationDeviceModel | target.asset.hardware.model  
DestinationDeviceOS | additional.fields.key/value.string_value  
DestinationDeviceOSFamily | additional.fields.key/value.string_value  
DestinationDeviceOSVersion | target.platform_version  
DestinationDeviceProfile | additional.fields.key/value.string_value  
DestinationDeviceVendor | target.asset.hardware.manufacturer  
DestinationDynamicAddressGroup | target.group.group_display_name  
DestinationEDL | additional.fields.key/value.string_value  
DestinationAddress | target.ip  
DestinationLocation | target.location.country_or_region  
DestinationPort | target.port  
DestinationUser | target.user.userid  
DestinationUserDomain | target.administrative_domain  
DestinationUserName | target.user.user_display_name  
DestinationUserUUID | target.user.product_object_id  
DestinationUUID | target.resource.product_object_id  
DGHierarchyLevel1 | additional.fields.key/value.string_value  
DGHierarchyLevel2 | additional.fields.key/value.string_value  
DGHierarchyLevel3 | additional.fields.key/value.string_value  
DGHierarchyLevel4 | additional.fields.key/value.string_value  
DynamicUserGroupName | additional.fields.key/value.string_value  
EndpointSerialNumber | principal.asset.hardware.serial_number  
EndpointAssociationID | additional.fields.key/value.string_value  
FlowType | additional.fields.key/value.string_value  
FromZone | additional.fields.key/value.string_value  
HASessionOwner | additional.fields.key/value.string_value  
GPHostID | additional.fields.key/value.string_value  
HTTP2Connection | network.application_protocol_version  
InboundInterface | additional.fields.key/value.string_value  
InboundInterfaceDetailsPort | additional.fields.key/value.string_value  
InboundInterfaceDetailsSlot | additional.fields.key/value.string_value  
InboundInterfaceDetailsType | additional.fields.key/value.string_value  
InboundInterfaceDetailsUnit | additional.fields.key/value.string_value  
CaptivePortal | additional.fields.key/value.string_value  
IsClienttoServer | additional.fields.key/value.string_value  
IsContainer | additional.fields.key/value.string_value  
IsDecryptMirror | additional.fields.key/value.string_value  
IsDecrypted | additional.fields.key/value.string_value  
IsDecryptedPayloadForward | additional.fields.key/value.string_value  
IsDecryptedLog | additional.fields.key/value.string_value  
IsDuplicateLog | additional.fields.key/value.string_value  
IsEncrypted | additional.fields.key/value.string_value  
LogExported | additional.fields.key/value.string_value  
LogForwarded | additional.fields.key/value.string_value  
IsIPV6 | additional.fields.key/value.string_value  
IsInspectionBeforeSession | additional.fields.key/value.string_value  
IsMptcpOn | additional.fields.key/value.string_value  
NAT | additional.fields.key/value.string_value  
IsNonStandardDestinationPort | additional.fields.key/value.string_value  
IsOffloaded | additional.fields.key/value.string_value  
IsPacketCapture | additional.fields.key/value.string_value  
IsPhishing | additional.fields.key/value.string_value  
IsPrismaNetwork | additional.fields.key/value.string_value  
IsPrismaUsers | additional.fields.key/value.string_value  
IsProxy | additional.fields.key/value.string_value  
IsReconExcluded | additional.fields.key/value.string_value  
IsSaaSApplication | additional.fields.key/value.string_value  
IsServertoClient | additional.fields.key/value.string_value  
IsSourceXForwarded | additional.fields.key/value.string_value  
IsSystemReturn | additional.fields.key/value.string_value  
IsTransaction | additional.fields.key/value.string_value  
IsTunnelInspected | additional.fields.key/value.string_value  
IsURLDenied | additional.fields.key/value.string_value  
K8SClusterID | target.resource.attribute.labels  
LinkChangeCount | additional.fields.key/value.string_value  
LinkSwitches | additional.fields.key/value.string_value  
Location | observer.location.country_or_region  
LogSetting | intermediary.resource.attribute.labels  
LogSource | intermediary.resource.attribute.labels  
LogSourceGroupID | intermediary.resource.attribute.labels  
DeviceSN | intermediary.asset.hardware.serial_number  
DeviceName | intermediary.hostname  
LogSourceTimeZoneOffset | additional.fields.key/value.string_value  
TimeReceived | metadata.collected_timestamp  
LogType | additional.fields.key/value.string_value  
IMEI | additional.fields.key/value.string_value  
NATDestination | target.nat_ip  
NATDestinationPort | target.nat_port  
NATSource | principal.nat_ip  
NATSourcePort | principal.nat_port  
NonStandardDestinationPort | additional.fields.key/value.string_value  
NSSAINetworkSliceType | additional.fields.key/value.string_value  
OutboundInterface | additional.fields.key/value.string_value  
OutboundInterfaceDetailsPort | additional.fields.key/value.string_value  
OutboundInterfaceDetailsSlot | additional.fields.key/value.string_value  
OutboundInterfaceDetailsType | additional.fields.key/value.string_value  
OutboundInterfaceDetailsUnit | additional.fields.key/value.string_value  
PacketsReceived | network.received_packets  
PacketsSent | network.sent_packets  
PacketsTotal | additional.fields.key/value.string_value  
PanoramaSN | observer.asset.hardware.serial_number  
ParentSessionID | network.parent_session_id  
ParentStarttime | additional.fields.key/value.string_value  
PlatformType | additional.fields.key/value.string_value  
ContainerName | target.resource.name  
ContainerNameSpace | target.resource.attribute.labels  
SDWANPolicyName | additional.fields.key/value.string_value  
Protocol | network.ip_protocol  
ApplicationRisk | additional.fields.key/value.string_value  
Rule | security_result.rule_name  
RuleUUID | security_result.rule_id  
SanctionedStateOfApp | additional.fields.key/value.string_value  
SDWANFECRatio | additional.fields.key/value.string_value  
SDWANCluster | additional.fields.key/value.string_value  
SDWANClusterType | additional.fields.key/value.string_value  
SDWANDeviceType | additional.fields.key/value.string_value  
SDWANSite | additional.fields.key/value.string_value  
SequenceNo | metadata.product_log_id  
SessionOwnerMidx | additional.fields.key/value.string_value  
SessionEndReason | security_result.summary  
SessionID | network.session_id  
SessionStartTime | additional.fields.key/value.string_value  
SessionTracker | additional.fields.key/value.string_value  
SourceDeviceCategory | principal.asset.category  
SourceDeviceClass | additional.fields.key/value.string_value  
SourceDeviceHost | principal.hostname  
SourceDeviceMac | principal.asset.mac  
SourceDeviceModel | principal.asset.hardware.model  
SourceDeviceOS | additional.fields.key/value.string_value  
SourceDeviceOSFamily | additional.fields.key/value.string_value  
SourceDeviceOSVersion | principal.platform_version  
SourceDeviceProfile | additional.fields.key/value.string_value  
SourceDeviceVendor | principal.asset.hardware.manufacturer  
SourceDynamicAddressGroup | principal.group.group_display_name  
SourceEDL | additional.fields.key/value.string_value  
SourceAddress | principal.ip  
SourceLocation | principal.location.country_or_region  
SourcePort | principal.port  
SourceUser | principal.user.userid  
SourceUserDomain | principal.administrative_domain  
SourceUserName | principal.user.user_display_name  
SourceUserUUID | principal.user.product_object_id  
SourceUUID | principal.resource.product_object_id  
Subtype | metadata.product_event_type  
ApplicationTechnology | additional.fields.key/value.string_value  
TimeGenerated | metadata.event_timestamp  
TimeGeneratedHighResolution | additional.fields.key/value.string_value  
ToZone | additional.fields.key/value.string_value  
SessionDuration | network.session_duration  
Tunnel | additional.fields.key/value.string_value  
TunneledApplication | additional.fields.key/value.string_value  
IMSI | additional.fields.key/value.string_value  
URLCategory | target.url_metadata.categories  
Users | additional.fields.key/value.string_value  
VendorName | additional.fields.key/value.string_value  
VirtualLocation | intermediary.asset.attribute.labels  
VirtualSystemID | intermediary.resource.product_object_id  
VirtualSystemName | intermediary.asset.attribute.labels  
X-Forwarded-ForIP | principal.ip  
  
### User-ID

The following table lists the log fields of the User-Id log type and their corresponding UDM fields.

Log field | UDM mapping  
---|---  
AuthFactorNo | security_result.detection_fields.key/value  
AuthenticatedUserDomain | target.user.administrative_domain  
AuthenticatedUserName | target.user.userid  
AuthenticatedUserUUID | target.user.product_object_id  
ConfigVersion | additional.fields.key/value.string_value  
CountofRepeats | additional.fields.key/value.string_value  
CortexDataLakeTenantID | metadata.product_deployment_id  
DestinationPort | target.port  
DGHierarchyLevel1 | additional.fields.key/value.string_value  
DGHierarchyLevel2 | additional.fields.key/value.string_value  
DGHierarchyLevel3 | additional.fields.key/value.string_value  
DGHierarchyLevel4 | additional.fields.key/value.string_value  
EventID | additional.fields.key/value.string_value  
IsDuplicateLog | additional.fields.key/value.string_value  
IsDuplicateUser | additional.fields.key/value.string_value  
LogExported | additional.fields.key/value.string_value  
LogForwarded | additional.fields.key/value.string_value  
IsPrismaNetworks | additional.fields.key/value.string_value  
IsPrismaUsers | additional.fields.key/value.string_value  
LogSource | intermediary.resource.attribute.labels  
LogSourceGroupID | intermediary.resource.attribute.labels  
DeviceSN | intermediary.asset.hardware.serial_number  
DeviceName | intermediary.hostname  
LogSourceTimeZoneOffset | additional.fields.key/value.string_value  
TimeReceived | metadata.collected_timestamp  
LogType | additional.fields.key/value.string_value  
MappingDataSource | additional.fields.key/value.string_value  
MappingDataSourceName | additional.fields.key/value.string_value  
MappingDataSourceType | additional.fields.key/value.string_value  
MappingTimeout | additional.fields.key/value.string_value  
MFAFactorType | additional.fields.key/value.string_value  
PanoramaSN | observer.asset.hardware.serial_number  
PlatformType | additional.fields.key/value.string_value  
SequenceNo | metadata.product_log_id  
SourceIP | principal.ip  
SourcePort | principal.port  
Subtype | metadata.product_event_type  
Tag | additional.fields.key/value.string_value  
TimeGenerated | metadata.event_timestamp  
TimeGeneratedHighResolution | additional.fields.key/value.string_value  
UGFlags | additional.fields.key/value.string_value  
User | target.user.userid  
UserGroupFound | additional.fields.key/value.string_value  
UserIdentifiedBySource | additional.fields.key/value.string_value  
VendorName | additional.fields.key/value.string_value  
VirtualLocation | intermediary.asset.attribute.labels  
VirtualSystemID | intermediary.resource.product_object_id  
VirtualSystemName | intermediary.asset.attribute.labels  
  
### HIP match

The following table lists the log fields of the HIP match log type and their corresponding UDM fields.

Log field | UDM mapping  
---|---  
ConfigVersion | additional.fields.key/value.string_value  
CountOfRepeats | additional.fields.key/value.string_value  
TenantID | metadata.product_deployment_id  
DGHierarchyLevel1 | additional.fields.key/value.string_value  
DGHierarchyLevel2 | additional.fields.key/value.string_value  
DGHierarchyLevel3 | additional.fields.key/value.string_value  
DGHierarchyLevel4 | additional.fields.key/value.string_value  
EndpointDeviceName | principal.asset.hostname  
EndpointOSType | additional.fields.key/value.string_value  
EndpointSerialNumber | principal.asset.hardware.serial_number  
HipMatchName | target.resource.attribute.labels  
HipMatchType | target.resource.attribute.labels  
HostID | principal.asset.asset_id  
IsDuplicateLog | additional.fields.key/value.string_value  
LogExported | additional.fields.key/value.string_value  
LogForwarded | additional.fields.key/value.string_value  
IsPrismaNetworks | additional.fields.key/value.string_value  
IsPrismaUsers | additional.fields.key/value.string_value  
LogSource | intermediary.resource.attribute.labels  
LogSourceGroupID | intermediary.resource.attribute.labels  
DeviceSN | target.asset.hardware.serial_number  
DeviceName | target.hostname  
LogSourceTimeZoneOffset | additional.fields.key/value.string_value  
TimeReceived | metadata.collected_timestamp  
LogType | metadata.product_event_type  
PanoramaSN | observer.asset.hardware.serial_number  
PlatformType | additional.fields.key/value.string_value  
SequenceNo | metadata.product_log_id  
Source | additional.fields.key/value.string_value  
SourceDeviceCategory | principal.asset.category  
SourceDeviceClass | additional.fields.key/value.string_value  
SourceDeviceHost | principal.hostname  
SourceDeviceMac | principal.asset.mac  
SourceDeviceModel | principal.asset.hardware.model  
SourceDeviceOS | additional.fields.key/value.string_value  
SourceDeviceOSFamily | additional.fields.key/value.string_value  
SourceDeviceOSVersion | principal.platform_version  
SourceDeviceProfile | additional.fields.key/value.string_value  
SourceDeviceVendor | principal.asset.hardware.manufacturer  
SourceIP | principal.ip  
SourceIPv6 | principal.ip  
SourceUser | principal.user.userid  
SourceUserDomain | principal.administrative_domain  
SourceUserName | principal.user.user_display_name  
SourceUserUUID | principal.user.product_object_id  
Subtype | metadata.product_event_type  
TimeGenerated | metadata.event_timestamp  
TimeGeneratedHighResolution | additional.fields.key/value.string_value  
TimestampDeviceIdentification | principal.asset.first_seen_time  
UUID | additional.fields.key/value.string_value  
VendorName | additional.fields.key/value.string_value  
VirtualLocation | target.asset.attribute.labels  
VirtualSystemID | target.resource.product_object_id  
VirtualSystemName | target.asset.attribute.labels  
  
### IP tag

The following table lists the log fields of the IP tag log type and their corresponding UDM fields.

Log field | UDM mapping  
---|---  
ConfigVersion | additional.fields.key/value.string_value  
CountOfRepeats | additional.fields.key/value.string_value  
TenantID | metadata.product_deployment_id  
DGHierarchyLevel1 | additional.fields.key/value.string_value  
DGHierarchyLevel2 | additional.fields.key/value.string_value  
DGHierarchyLevel3 | additional.fields.key/value.string_value  
DGHierarchyLevel4 | additional.fields.key/value.string_value  
EventID | additional.fields.key/value.string_value  
IPSubnetRange | network.ip_subnet_range  
IsDuplicateLog | additional.fields.key/value.string_value  
LogExported | additional.fields.key/value.string_value  
LogForwarded | additional.fields.key/value.string_value  
IsPrismaNetworks | additional.fields.key/value.string_value  
IsPrismaUsers | additional.fields.key/value.string_value  
LogSetting | target.resource.attribute.labels  
LogSource | target.resource.attribute.labels  
LogSourceGroupID | target.resource.attribute.labels  
DeviceSN | target.asset.hardware.serial_number  
DeviceName | target.hostname  
LogSourceTimeZoneOffset | additional.fields.key/value.string_value  
TimeReceived | metadata.collected_timestamp  
LogType | additional.fields.key/value.string_value  
MappingDataSource | additional.fields.key/value.string_value  
MappingDataSourceSubType | additional.fields.key/value.string_value  
MappingDataSourceType | additional.fields.key/value.string_value  
MappingTimeout | additional.fields.key/value.string_value  
PanoramaSN | observer.asset.hardware.serial_number  
PlatformType | additional.fields.key/value.string_value  
RuleMatched | security_result.rule_name  
RuleMatchedUUID | security_result.rule_id  
SequenceNo | metadata.product_log_id  
SourceIP | principal.ip  
Subtype | metadata.product_event_type  
TagName | additional.fields.key/value.string_value  
TimeGenerated | metadata.event_timestamp  
TimeGeneratedHighResolution | additional.fields.key/value.string_value  
VendorName | additional.fields.key/value.string_value  
VirtualLocation | target.asset.attribute.labels  
VirtualSystemID | target.resource.product_object_id  
VirtualSystemName | target.asset.attribute.labels  
  
### Decryption

The following table lists the log fields of the Decryption log type and their corresponding UDM fields.

Log field | UDM mapping  
---|---  
Action | security_result.action  
Application | target.application  
ApplicationCategory | additional.fields.key/value.string_value  
ApplicationSubcategory | additional.fields.key/value.string_value  
CertificateFlags | additional.fields.key/value.string_value  
CertificateSerial | network.tls.server.certificate.serial  
CertificateSize | additional.fields.key/value.string_value  
CertificateVersion | network.tls.server.certificate.version  
ChainStatus | additional.fields.key/value.string_value  
ApplicationCharacteristics | additional.fields.key/value.string_value  
ClientToFirewall | additional.fields.key/value.string_value  
CommonName | additional.fields.key/value.string_value  
CommonNameLength | additional.fields.key/value.string_value  
ContainerID | intermediary.resource.product_object_id  
ApplicationContainer | additional.fields.key/value.string_value  
Cpadding | additional.fields.key/value.string_value  
DestinationDeviceCategory | target.asset.category  
DestinationDeviceClass | additional.fields.key/value.string_value  
DestinationDeviceHost | target.asset.hostname  
DestinationDeviceMac | target.asset.mac  
DestinationDeviceModel | target.asset.hardware.model  
DestinationDeviceOS | additional.fields.key/value.string_value  
DestinationDeviceOSFamily | additional.fields.key/value.string_value  
DestinationDeviceOSVersion | target.platform_version  
DestinationDeviceProfile | additional.fields.key/value.string_value  
DestinationDeviceVendor | target.asset.hardware.manufacturer  
DestinationDynamicAddressGroup | target.group.group_display_name  
DestinationEDL | additional.fields.key/value.string_value  
DestinationAddress | target.ip  
DestinationLocation | target.location.country_or_region  
DestinationPort | target.port  
DestinationUser | target.user.userid  
DestinationUserDomain | target.administrative_domain  
DestinationUserName | target.user.user_display_name  
DestinationUserUUID | target.user.product_object_id  
DestinationUUID | target.resource.product_object_id  
Domain | target.hostname  
EllipticCurve | network.tls.curve  
ErrorIndex | additional.fields.key/value.string_value  
ErrorMessage | additional.fields.key/value.string_value  
Fingerprint | network.tls.server.certificate.md5/sha1/sha256  
FirewallToClient | additional.fields.key/value.string_value  
FromZone | additional.fields.key/value.string_value  
InboundInterface | additional.fields.key/value.string_value  
InboundInterfaceDetailsPort | additional.fields.key/value.string_value  
InboundInterfaceDetailsSlot | additional.fields.key/value.string_value  
InboundInterfaceDetailsType | additional.fields.key/value.string_value  
InboundInterfaceDetailsUnit | additional.fields.key/value.string_value  
CaptivePortal | additional.fields.key/value.string_value  
IsCertECDSA | additional.fields.key/value.string_value  
IsCertRSA | additional.fields.key/value.string_value  
IsCertCNTruncated | additional.fields.key/value.string_value  
IsClienttoServer | additional.fields.key/value.string_value  
IsContainer | additional.fields.key/value.string_value  
IsDecryptMirror | additional.fields.key/value.string_value  
IsDecrypted | additional.fields.key/value.string_value  
IsEncrypted | additional.fields.key/value.string_value  
IsForwarded | additional.fields.key/value.string_value  
IsIPV6 | additional.fields.key/value.string_value  
IsIssuerCNTruncated | additional.fields.key/value.string_value  
IsMptcpOn | additional.fields.key/value.string_value  
IsNAT | additional.fields.key/value.string_value  
IsNonStandardDestinationPort | additional.fields.key/value.string_value  
PacketCapture | additional.fields.key/value.string_value  
IsPhishing | additional.fields.key/value.string_value  
IsProxy | additional.fields.key/value.string_value  
IsReconExcluded | additional.fields.key/value.string_value  
IsResumeSession | additional.fields.key/value.string_value  
IsRootCNTruncated | additional.fields.key/value.string_value  
IsSaaSApplication | additional.fields.key/value.string_value  
IsServertoClient | additional.fields.key/value.string_value  
IsSNITruncated | additional.fields.key/value.string_value  
IsSourceXForwarded | additional.fields.key/value.string_value  
IsSystemReturn | additional.fields.key/value.string_value  
IsTransaction | additional.fields.key/value.string_value  
IsTunnelInspected | additional.fields.key/value.string_value  
IsURLDenied | additional.fields.key/value.string_value  
IssuerCommonName | network.tls.server.certificate.issuer  
IssuerNameLength | additional.fields.key/value.string_value  
DeviceSN | intermediary.asset.hardware.serial_number  
DeviceName | intermediary.hostname  
NATDestination | target.nat_ip  
NATDestinationPort | target.nat_port  
NATSource | principal.nat_ip  
NATSourcePort | principal.nat_port  
TimeNotAfter | additional.fields.key/value.string_value  
TimeNotBefore | additional.fields.key/value.string_value  
OutboundInterface | additional.fields.key/value.string_value  
OutboundInterfaceDetailsPort | additional.fields.key/value.string_value  
OutboundInterfaceDetailsSlot | additional.fields.key/value.string_value  
OutboundInterfaceDetailsType | additional.fields.key/value.string_value  
OutboundInterfaceDetailsUnit | additional.fields.key/value.string_value  
Padding | additional.fields.key/value.string_value  
Padding3 | additional.fields.key/value.string_value  
ContainerName | target.resource.name  
ContainerNameSpace | target.resource.attribute.labels  
PolicyName | additional.fields.key/value.string_value  
Protocol | network.ip_protocol  
ProxyType | additional.fields.key/value.string_value  
ApplicationRisk | additional.fields.key/value.string_value  
RootCommonName | additional.fields.key/value.string_value  
RootCNLength | additional.fields.key/value.string_value  
RootStatus | additional.fields.key/value.string_value  
Rule | security_result.rule_name  
RuleUUID | security_result.rule_id  
SanctionedStateOfApp | additional.fields.key/value.string_value  
SessionID | network.session_id  
ServerNameIndication | network.tls.client.server_name  
SNILength | additional.fields.key/value.string_value  
SourceDeviceClass | additional.fields.key/value.string_value  
SourceDeviceOS | additional.fields.key/value.string_value  
SourceDynamicAddressGroup | principal.group.group_display_name  
SourceEDL | additional.fields.key/value.string_value  
SourceAddress | principal.ip  
SourceLocation | principal.location.country_or_region  
SourcePort | principal.port  
SourceUser | principal.user.userid  
SourceUserDomain | principal.administrative_domain  
SourceUserName | principal.user.user_display_name  
SourceUserUUID | principal.user.product_object_id  
SourceUUID | principal.resource.product_object_id  
ApplicationTechnology | additional.fields.key/value.string_value  
TimeReceivedManagementPlane | additional.fields.key/value.string_value  
TLSAuth | additional.fields.key/value.string_value  
TLSEncryptionAlgorithm | additional.fields.key/value.string_value  
TLSKeyExchange | additional.fields.key/value.string_value  
TLSVersion | network.tls.version  
ToZone | additional.fields.key/value.string_value  
Tpadding | additional.fields.key/value.string_value  
Tunnel | additional.fields.key/value.string_value  
TunneledApplication | additional.fields.key/value.string_value  
Vpadding | additional.fields.key/value.string_value  
IsDuplicateLog | additional.fields.key/value.string_value  
LogExported | additional.fields.key/value.string_value  
IsPrismaNetwork | additional.fields.key/value.string_value  
IsPrismaUsers | additional.fields.key/value.string_value  
LogSetting | intermediary.resource.attribute.labels  
LogSource | intermediary.resource.attribute.labels  
LogSourceGroupID | intermediary.resource.attribute.labels  
LogSourceTimeZoneOffset | additional.fields.key/value.string_value  
TimeReceived | metadata.collected_timestamp  
LogType | additional.fields.key/value.string_value  
PanoramaSN | observer.asset.hardware.serial_number  
PlatformType | additional.fields.key/value.string_value  
SequenceNo | metadata.product_log_id  
SourceDeviceCategory | principal.asset.category  
SourceDeviceHost | principal.hostname  
SourceDeviceMac | principal.asset.mac  
SourceDeviceModel | principal.asset.hardware.model  
SourceDeviceOSFamily | additional.fields.key/value.string_value  
SourceDeviceOSVersion | principal.platform_version  
SourceDeviceProfile | additional.fields.key/value.string_value  
SourceDeviceVendor | principal.asset.hardware.manufacturer  
Subtype | metadata.product_event_type  
TimeGenerated | metadata.event_timestamp  
TimeGeneratedHighResolution | additional.fields.key/value.string_value  
VendorName | additional.fields.key/value.string_value  
VirtualLocation | intermediary.asset.attribute.labels  
VirtualSystemID | intermediary.resource.product_object_id  
VirtualSystemName | intermediary.asset.attribute.labels  
  
### Tunnel

The following table lists the log fields of the Tunnel log type and their corresponding UDM fields.

Log field | UDM mapping  
---|---  
AccessPointName | additional.fields.key/value.string_value  
Action | security_result.action  
ActionSource | additional.fields.key/value.string_value  
Application | target.application  
ApplicationCategory | additional.fields.key/value.string_value  
ApplicationSubcategory | additional.fields.key/value.string_value  
BytesReceived | network.received_bytes  
BytesSent | network.sent_bytes  
Bytes | additional.fields.key/value.string_value  
ConfigVersion | additional.fields.key/value.string_value  
ContainerID | intermediary.resource.product_object_id  
ApplicationContainer | additional.fields.key/value.string_value  
ContentVersion | additional.fields.key/value.string_value  
RepeatCount | additional.fields.key/value.string_value  
LoggingServiceID | additional.fields.key/value.string_value  
DestinationDeviceClass | additional.fields.key/value.string_value  
DestinationDeviceMac | target.asset.mac  
DestinationDeviceModel | target.asset.hardware.model  
DestinationDeviceOS | additional.fields.key/value.string_value  
DestinationDeviceVendor | target.asset.hardware.manufacturer  
DestinationDynamicAddressGroup | target.group.group_display_name  
DestinationEDL | additional.fields.key/value.string_value  
DestinationAddress | target.ip  
DestinationLocation | target.location.country_or_region  
DestinationPort | target.port  
DestinationUser | target.user.userid  
DestinationUserDomain | target.administrative_domain  
DestinationUserName | target.user.user_display_name  
DestinationUserUUID | target.user.product_object_id  
DestinationUUID | target.resource.product_object_id  
DGHierarchyLevel1 | additional.fields.key/value.string_value  
DGHierarchyLevel2 | additional.fields.key/value.string_value  
DGHierarchyLevel3 | additional.fields.key/value.string_value  
DGHierarchyLevel4 | additional.fields.key/value.string_value  
DynamicUserGroupName | additional.fields.key/value.string_value  
FromZone | additional.fields.key/value.string_value  
InboundInterface | additional.fields.key/value.string_value  
InboundInterfaceDetailsPort | additional.fields.key/value.string_value  
InboundInterfaceDetailsSlot | additional.fields.key/value.string_value  
InboundInterfaceDetailsType | additional.fields.key/value.string_value  
InboundInterfaceDetailsUnit | additional.fields.key/value.string_value  
CaptivePortal | additional.fields.key/value.string_value  
IsClienttoServer | additional.fields.key/value.string_value  
IsContainer | additional.fields.key/value.string_value  
IsDecryptMirror | additional.fields.key/value.string_value  
IsDecryptedPayloadForward | additional.fields.key/value.string_value  
IsDecryptedLog | additional.fields.key/value.string_value  
IsDuplicateLog | additional.fields.key/value.string_value  
LogExported | additional.fields.key/value.string_value  
LogForwarded | additional.fields.key/value.string_value  
IsIPV6 | additional.fields.key/value.string_value  
IsInspectionBeforeSession | additional.fields.key/value.string_value  
IsMptcpOn | additional.fields.key/value.string_value  
NAT | additional.fields.key/value.string_value  
IsNonStandardDestinationPort | additional.fields.key/value.string_value  
IsPacketCapture | additional.fields.key/value.string_value  
IsPhishing | additional.fields.key/value.string_value  
IsPrismaNetwork | additional.fields.key/value.string_value  
IsPrismaUsers | additional.fields.key/value.string_value  
IsProxy | additional.fields.key/value.string_value  
IsReconExcluded | additional.fields.key/value.string_value  
IsSaaSApplication | additional.fields.key/value.string_value  
IsServertoClient | additional.fields.key/value.string_value  
IsSourceXForwarded | additional.fields.key/value.string_value  
IsSystemReturn | additional.fields.key/value.string_value  
IsTransaction | additional.fields.key/value.string_value  
IsTunnelInspected | additional.fields.key/value.string_value  
IsURLDenied | additional.fields.key/value.string_value  
LogSetting | intermediary.resource.attribute.labels  
LogSource | intermediary.resource.attribute.labels  
LogSourceGroupID | intermediary.resource.attribute.labels  
DeviceSN | intermediary.asset.hardware.serial_number  
DeviceName | intermediary.hostname  
LogSourceTimeZoneOffset | additional.fields.key/value.string_value  
TimeReceived | metadata.collected_timestamp  
LogType | additional.fields.key/value.string_value  
MobileAreaCode | additional.fields.key/value.string_value  
MobileBaseStationCode | additional.fields.key/value.string_value  
MobileCountryCode | additional.fields.key/value.string_value  
MobileIP | additional.fields.key/value.string_value  
MobileNetworkCode | additional.fields.key/value.string_value  
MobileSubscriberISDN | additional.fields.key/value.string_value  
IMEI | additional.fields.key/value.string_value  
NATDestination | target.nat_ip  
NATDestinationPort | target.nat_port  
NATSource | principal.nat_ip  
NATSourcePort | principal.nat_port  
NonStandardDestinationPort | additional.fields.key/value.string_value  
NSSAINetworkSliceDifferentiator | additional.fields.key/value.string_value  
NSSAINetworkSliceType | additional.fields.key/value.string_value  
OutboundInterface | additional.fields.key/value.string_value  
OutboundInterfaceDetailsPort | additional.fields.key/value.string_value  
OutboundInterfaceDetailsSlot | additional.fields.key/value.string_value  
OutboundInterfaceDetailsType | additional.fields.key/value.string_value  
OutboundInterfaceDetailsUnit | additional.fields.key/value.string_value  
PacketsDroppedMax | additional.fields.key/value.string_value  
PacketsDroppedStrict | additional.fields.key/value.string_value  
PacketsDroppedTunnel | additional.fields.key/value.string_value  
PacketsDroppedProtocol | additional.fields.key/value.string_value  
PacketsReceived | network.received_packets  
PacketsSent | network.sent_packets  
PacketsTotal | additional.fields.key/value.string_value  
PanoramaSN | observer.asset.hardware.serial_number  
ParentSessionID | network.parent_session_id  
ParentStarttime | additional.fields.key/value.string_value  
ProtocolDataUnitsessionID | additional.fields.key/value.string_value  
PlatformType | additional.fields.key/value.string_value  
ContainerName | target.resource.name  
ContainerNameSpace | target.resource.attribute.labels  
Protocol | network.ip_protocol  
RadioAccessTechnology | additional.fields.key/value.string_value  
ApplicationRisk | additional.fields.key/value.string_value  
Rule | security_result.rule_name  
RuleUUID | security_result.rule_id  
SanctionedStateOfApp | additional.fields.key/value.string_value  
SequenceNo | metadata.product_log_id  
SessionOwnerMidx | additional.fields.key/value.string_value  
SessionEndReason | security_result.summary  
SessionID | network.session_id  
SessionStartTime | additional.fields.key/value.string_value  
SessionTracker | additional.fields.key/value.string_value  
Severity | security_result.severity  
SourceDeviceClass | additional.fields.key/value.string_value  
SourceDeviceMac | principal.asset.mac  
SourceDeviceModel | principal.asset.hardware.model  
SourceDeviceOS | additional.fields.key/value.string_value  
SourceDeviceVendor | principal.asset.hardware.manufacturer  
SourceDynamicAddressGroup | principal.group.group_display_name  
SourceEDL | additional.fields.key/value.string_value  
SourceAddress | principal.ip  
SourceLocation | principal.location.country_or_region  
SourcePort | principal.port  
SourceUser | principal.user.userid  
SourceUserDomain | principal.administrative_domain  
SourceUserName | principal.user.user_display_name  
SourceUserUUID | principal.user.product_object_id  
SourceUUID | principal.resource.product_object_id  
StandardPortsOfApp | additional.fields.key/value.string_value  
Subtype | metadata.product_event_type  
ApplicationTechnology | additional.fields.key/value.string_value  
TimeGenerated | metadata.event_timestamp  
TimeGeneratedHighResolution | additional.fields.key/value.string_value  
ToZone | additional.fields.key/value.string_value  
SessionDuration | network.session_duration  
Tunnel | additional.fields.key/value.string_value  
TunnelCauseCode | additional.fields.key/value.string_value  
TunnelEndpointID1 | additional.fields.key/value.string_value  
TunnelEndpointID2 | additional.fields.key/value.string_value  
TunnelEventCode | additional.fields.key/value.string_value  
TunnelEventType | additional.fields.key/value.string_value  
TunnelInspectionRule | additional.fields.key/value.string_value  
TunnelInterface | additional.fields.key/value.string_value  
TunnelMessageType | additional.fields.key/value.string_value  
TunnelRemoteIMSIID | additional.fields.key/value.string_value  
TunnelRemoteUserIP | principal.ip  
TunnelSessionsClosed | additional.fields.key/value.string_value  
TunnelSessionsCreated | additional.fields.key/value.string_value  
TunneledApplication | additional.fields.key/value.string_value  
IMSI | additional.fields.key/value.string_value  
URLCategory | target.url_metadata.categories  
Users | additional.fields.key/value.string_value  
VendorName | additional.fields.key/value.string_value  
VendorSeverity | security_result.severity_details  
VirtualLocation | intermediary.asset.attribute.labels  
VirtualSystemID | intermediary.resource.product_object_id  
VirtualSystemName | intermediary.asset.attribute.labels  
  
### Authentication

The following table lists the log fields of the Authentication log type and their corresponding UDM fields.

Log field | UDM mapping  
---|---  
AuthenticationDescription | security_result.description  
AuthEvent | metadata.description  
AuthFactorNo | security_result.detection_fields.key/value  
AuthenticationPolicy | security_result.detection_fields.key/value  
AuthenticationProtocol | additional.fields.key/value.string_value  
AuthServerProfile | additional.fields.key/value.string_value  
AuthenticatedUserDomain | target.administrative_domain  
AuthenticatedUserName | target.user.userid  
AuthenticatedUserUUID | target.user.product_object_id  
ClientType | additional.fields.key/value.string_value  
ClientTypeName | additional.fields.key/value.string_value  
CountOfRepeats | additional.fields.key/value.string_value  
CortexDataLakeTenantID | metadata.product_deployment_id  
IsPrismaNetworks | additional.fields.key/value.string_value  
Location | target.location.country_or_region  
LogSetting | intermediary.resource.attribute.labels  
LogType | additional.fields.key/value.string_value  
MFAAuthenticationID | additional.fields.key/value.string_value  
MFAVendor | additional.fields.key/value.string_value  
NormalizeUser | target.user.user_display_name  
Object | target.resource.name  
RuleMatched | security_result.rule_name  
RuleMatchedUUID | security_result.rule_id  
AuthCacheServiceRegion | additional.fields.key/value.string_value  
SessionID | network.session_id  
SourceDeviceCategory | principal.asset.category  
SourceDeviceHost | principal.hostname  
SourceDeviceMac | principal.asset.mac  
SourceDeviceModel | principal.asset.hardware.model  
SourceDeviceOSFamily | additional.fields.key/value.string_value  
SourceDeviceOSVersion | principal.platform_version  
SourceDeviceProfile | additional.fields.key/value.string_value  
SourceDeviceVendor | principal.asset.hardware.manufacturer  
SourceIP | principal.ip  
TimeGenerated | metadata.event_timestamp  
User | target.user.userid  
UserAgentString | network.http.user_agent  
IsDuplicateLog | additional.fields.key/value.string_value  
LogExported | additional.fields.key/value.string_value  
LogForwarded | additional.fields.key/value.string_value  
IsPrismaUsers | additional.fields.key/value.string_value  
LogSource | intermediary.resource.attribute.labels  
LogSourceGroupID | intermediary.resource.attribute.labels  
DeviceSN | intermediary.asset.hardware.serial_number  
DeviceName | intermediary.hostname  
LogSourceTimeZoneOffset | additional.fields.key/value.string_value  
TimeReceived | metadata.collected_timestamp  
PanoramaSN | observer.asset.hardware.serial_number  
PlatformType | additional.fields.key/value.string_value  
SequenceNo | metadata.product_log_id  
Subtype | metadata.product_event_type  
TimeGeneratedHighResolution | additional.fields.key/value.string_value  
VendorName | additional.fields.key/value.string_value  
VirtualLocation | intermediary.asset.attribute.labels  
VirtualSystemID | intermediary.resource.product_object_id  
VirtualSystemName | intermediary.asset.attribute.labels  
  
### URL

The following table lists the log fields of the URL log type and their corresponding UDM fields.

Log field | UDM mapping  
---|---  
Action | security_result.action  
Application | target.application  
ApplicationCategory | additional.fields.key/value.string_value  
ApplicationSubcategory | additional.fields.key/value.string_value  
CloudHostname | additional.fields.key/value.string_value  
CloudReportID | security_result.detection_fields.key/value  
ConfigVersion | additional.fields.key/value.string_value  
ContainerID | intermediary.resource.product_object_id  
ApplicationContainer | additional.fields.key/value.string_value  
ContentType | additional.fields.key/value.string_value  
ContentVersion | additional.fields.key/value.string_value  
RepeatCount | additional.fields.key/value.string_value  
CortexDataLakeTenantID | metadata.product_deployment_id  
DestinationDeviceCategory | target.asset.category  
DestinationDeviceClass | additional.fields.key/value.string_value  
DestinationDeviceHost | target.asset.hostname  
DestinationDeviceMac | target.asset.mac  
DestinationDeviceModel | target.asset.hardware.model  
DestinationDeviceOS | additional.fields.key/value.string_value  
DestinationDeviceOSFamily | additional.fields.key/value.string_value  
DestinationDeviceOSVersion | target.platform_version  
DestinationDeviceProfile | additional.fields.key/value.string_value  
DestinationDeviceVendor | target.asset.hardware.manufacturer  
DestinationDynamicAddressGroup | target.group.group_display_name  
DestinationEDL | additional.fields.key/value.string_value  
DestinationAddress | target.ip  
DestinationLocation | target.location.country_or_region  
DestinationPort | target.port  
DestinationUser | target.user.userid  
DestinationUserDomain | target.administrative_domain  
DestinationUserName | target.user.user_display_name  
DestinationUserUUID | target.user.product_object_id  
DestinationUUID | target.resource.product_object_id  
DGHierarchyLevel1 | additional.fields.key/value.string_value  
DGHierarchyLevel2 | additional.fields.key/value.string_value  
DGHierarchyLevel3 | additional.fields.key/value.string_value  
DGHierarchyLevel4 | additional.fields.key/value.string_value  
DirectionOfAttack | security_result.detection_fields.key/value  
DynamicUserGroupName | additional.fields.key/value.string_value  
EndpointSerialNumber | principal.asset.hardware.serial_number  
FileURL | target.url  
FlowType | additional.fields.key/value.string_value  
FromZone | additional.fields.key/value.string_value  
HostID | principal.asset.asset_id  
HTTP2Connection | network.application_protocol_version  
HTTPHeaders | additional.fields.key/value.string_value  
HTTPMethod | network.http.method  
InboundInterface | additional.fields.key/value.string_value  
InboundInterfaceDetailsPort | additional.fields.key/value.string_value  
InboundInterfaceDetailsSlot | additional.fields.key/value.string_value  
InboundInterfaceDetailsType | additional.fields.key/value.string_value  
InboundInterfaceDetailsUnit | additional.fields.key/value.string_value  
InlineMLVerdict | additional.fields.key/value.string_value  
CaptivePortal | additional.fields.key/value.string_value  
IsClienttoServer | additional.fields.key/value.string_value  
IsContainer | additional.fields.key/value.string_value  
IsDecryptMirror | additional.fields.key/value.string_value  
IsDecrypted | additional.fields.key/value.string_value  
IsDuplicateLog | additional.fields.key/value.string_value  
IsEncrypted | additional.fields.key/value.string_value  
LogExported | additional.fields.key/value.string_value  
LogForwarded | additional.fields.key/value.string_value  
IsIPV6 | additional.fields.key/value.string_value  
IsMptcpOn | additional.fields.key/value.string_value  
NAT | additional.fields.key/value.string_value  
IsNonStandardDestinationPort | additional.fields.key/value.string_value  
IsPacketCapture | additional.fields.key/value.string_value  
IsPhishing | additional.fields.key/value.string_value  
IsPrismaNetwork | additional.fields.key/value.string_value  
IsPrismaUsers | additional.fields.key/value.string_value  
IsProxy | additional.fields.key/value.string_value  
IsReconExcluded | additional.fields.key/value.string_value  
IsSaaSApplication | additional.fields.key/value.string_value  
IsServertoClient | additional.fields.key/value.string_value  
IsSourceXForwarded | additional.fields.key/value.string_value  
IsSystemReturn | additional.fields.key/value.string_value  
IsTransaction | additional.fields.key/value.string_value  
IsTunnelInspected | additional.fields.key/value.string_value  
IsURLDenied | additional.fields.key/value.string_value  
K8SClusterID | target.resource.attribute.labels  
Location | observer.location.country_or_region  
LogSetting | intermediary.resource.attribute.labels  
LogSource | intermediary.resource.attribute.labels  
LogSourceGroupID | intermediary.resource.attribute.labels  
DeviceSN | intermediary.asset.hardware.serial_number  
DeviceName | intermediary.hostname  
LogSourceTimeZoneOffset | additional.fields.key/value.string_value  
TimeReceived | metadata.collected_timestamp  
LogType | additional.fields.key/value.string_value  
IMEI | additional.fields.key/value.string_value  
NATDestination | target.nat_ip  
NATDestinationPort | target.nat_port  
NATSource | principal.nat_ip  
NATSourcePort | principal.nat_port  
NonStandardDestinationPort | additional.fields.key/value.string_value  
NSSAINetworkSliceType | additional.fields.key/value.string_value  
OutboundInterface | additional.fields.key/value.string_value  
OutboundInterfaceDetailsPort | additional.fields.key/value.string_value  
OutboundInterfaceDetailsSlot | additional.fields.key/value.string_value  
OutboundInterfaceDetailsType | additional.fields.key/value.string_value  
OutboundInterfaceDetailsUnit | additional.fields.key/value.string_value  
PanoramaSN | observer.asset.hardware.serial_number  
ParentSessionID | network.parent_session_id  
ParentStarttime | additional.fields.key/value.string_value  
Packet | additional.fields.key/value.string_value  
PacketID | additional.fields.key/value.string_value  
PlatformType | additional.fields.key/value.string_value  
ContainerName | target.resource.name  
ContainerNameSpace | target.resource.attribute.labels  
Protocol | network.ip_protocol  
Referer | network.http.referral_url  
HTTPRefererFQDN | additional.fields.key/value.string_value  
HTTPRefererPort | additional.fields.key/value.string_value  
HTTPRefererProtocol | additional.fields.key/value.string_value  
HTTPRefererURLPath | additional.fields.key/value.string_value  
ApplicationRisk | additional.fields.key/value.string_value  
Rule | security_result.rule_name  
RuleUUID | security_result.rule_id  
SanctionedStateOfApp | additional.fields.key/value.string_value  
SequenceNo | metadata.product_log_id  
SessionID | network.session_id  
Severity | security_result.severity  
SigFlags | additional.fields.key/value.string_value  
SourceDeviceCategory | principal.asset.category  
SourceDeviceClass | additional.fields.key/value.string_value  
SourceDeviceHost | principal.hostname  
SourceDeviceMac | principal.asset.mac  
SourceDeviceModel | principal.asset.hardware.model  
SourceDeviceOS | additional.fields.key/value.string_value  
SourceDeviceOSFamily | additional.fields.key/value.string_value  
SourceDeviceOSVersion | principal.platform_version  
SourceDeviceProfile | additional.fields.key/value.string_value  
SourceDeviceVendor | principal.asset.hardware.manufacturer  
SourceDynamicAddressGroup | principal.group.group_display_name  
SourceEDL | additional.fields.key/value.string_value  
SourceAddress | principal.ip  
SourceLocation | principal.location.country_or_region  
SourcePort | principal.port  
SourceUser | principal.user.userid  
SourceUserDomain | principal.administrative_domain  
SourceUserName | principal.user.user_display_name  
SourceUserUUID | principal.user.product_object_id  
SourceUUID | principal.resource.product_object_id  
Subtype | metadata.product_event_type  
ApplicationTechnology | additional.fields.key/value.string_value  
TimeGenerated | metadata.event_timestamp  
TimeGeneratedHighResolution | additional.fields.key/value.string_value  
ToZone | additional.fields.key/value.string_value  
Tunnel | additional.fields.key/value.string_value  
TunneledApplication | additional.fields.key/value.string_value  
IMSI | additional.fields.key/value.string_value  
URL | target.url_metadata.URL  
URLCategory | target.url_metadata.categories  
URLCategoryList | additional.fields.key/value.string_value  
URLDomain | target.domain.name  
URLCounter | additional.fields.key/value.string_value  
UserAgent | network.http.user_agent  
Users | additional.fields.key/value.string_value  
VendorName | additional.fields.key/value.string_value  
VendorSeverity | security_result.severity_details  
VirtualLocation | intermediary.asset.attribute.labels  
VirtualSystemID | intermediary.resource.product_object_id  
VirtualSystemName | intermediary.asset.attribute.labels  
X-Forwarded-For | additional.fields.key/value.string_value  
X-Forwarded-ForIP | principal.ip  
  
### GlobalProtect

The following table lists the log fields of the GlobalProtect log type and their corresponding UDM fields.

Log field | UDM mapping  
---|---  
AttemptedGateways | additional.fields.key/value.string_value  
AuthMethod | extensions.auth.auth_details  
ConnectionMethod | additional.fields.key/value.string_value  
ConnectionErrorID | additional.fields.key/value.string_value  
ConnectionError | additional.fields.key/value.string_value  
CountOfRepeats | additional.fields.key/value.string_value  
EndpointDeviceName | principal.asset.hostname  
GlobalProtectClientVersion | additional.fields.key/value.string_value  
EndpointOSType | additional.fields.key/value.string_value  
EndpointSN | principal.asset.hardware.serial_number  
EventIDValue | additional.fields.key/value.string_value  
Gateway | target.resource.name  
GatewayPriority | additional.fields.key/value.string_value  
GatewaySelectionType | additional.fields.key/value.string_value  
GlobalProtectGatewayLocation | target.location.country_or_region  
HostID | principal.asset.asset_id  
LogSource | intermediary.resource.attribute.labels  
LogSourceGroupID | intermediary.resource.attribute.labels  
DeviceSN | intermediary.asset.hardware.serial_number  
DeviceName | intermediary.hostname  
LoginDuration | network.session_duration  
Description | security_result.description  
Portal | target.hostname  
PrivateIPv4 | principal.ip  
PrivateIPv6 | principal.ip  
ProjectName | additional.fields.key/value.string_value  
PublicIPv4 | principal.nat_ip  
PublicIPv6 | principal.nat_ip  
QuarantineReason | security_result.summary  
SequenceNo | metadata.product_log_id  
SourceRegion | principal.location.country_or_region  
SourceUserName | principal.user.user_display_name  
SourceUserDomain | principal.administrative_domain  
SourceUserName | principal.user.user_display_name  
SourceUserUUID | principal.user.product_object_id  
SSLResponseTime | additional.fields.key/value.string_value  
Stage | additional.fields.key/value.string_value  
EventStatus | additional.fields.key/value.string_value  
LogSubtype | metadata.product_event_type  
TunnelType | additional.fields.key/value.string_value  
VirtualSystem | intermediary.asset.attribute.labels  
VirtualSystemName | intermediary.asset.attribute.labels  
EndpointOSVersion | principal.platform_version  
IsDuplicateLog | additional.fields.key/value.string_value  
LogExported | additional.fields.key/value.string_value  
LogForwarded | additional.fields.key/value.string_value  
IsPrismaNetworks | additional.fields.key/value.string_value  
IsPrismaUsers | additional.fields.key/value.string_value  
LogSourceTimeZoneOffset | additional.fields.key/value.string_value  
TimeReceived | metadata.collected_timestamp  
LogType | metadata.product_event_type  
PanoramaSN | observer.asset.hardware.serial_number  
PlatformType | additional.fields.key/value.string_value  
TimeGenerated | metadata.event_timestamp  
TimeGeneratedHighResolution | additional.fields.key/value.string_value  
VendorName | additional.fields.key/value.string_value  
VirtualSystemID | intermediary.resource.product_object_id  
  
### SCTP

The following table lists the log fields of the SCTP log type and their corresponding UDM fields.

Log field | UDM mapping  
---|---  
Action | security_result.action  
Application | target.application  
AssocationEndReason | additional.fields.key/value.string_value  
ChunksReceived | additional.fields.key/value.string_value  
ChunksSent | additional.fields.key/value.string_value  
ChunksTotal | additional.fields.key/value.string_value  
ConfigVersion | additional.fields.key/value.string_value  
ContainerID | intermediary.resource.product_object_id  
ContentVersion | additional.fields.key/value.string_value  
RepeatCount | additional.fields.key/value.string_value  
CortexDataLakeTenantID | metadata.product_deployment_id  
DestinationDeviceClass | target.asset.category  
DestinationDeviceMac | target.asset.mac  
DestinationDeviceModel | target.asset.hardware.model  
DestinationDeviceOS | additional.fields.key/value.string_value  
DestinationDeviceVendor | target.asset.hardware.manufacturer  
DestinationDynamicAddressGroup | target.group.group_display_name  
DestinationEDL | additional.fields.key/value.string_value  
DestinationIP | target.ip  
DestinationLocation | target.location.country_or_region  
DestinationPort | target.port  
DestinationUser | target.user.userid  
DestinationUserDomain | target.administrative_domain  
DestinationUserName | target.user.user_display_name  
DestinationUserUUID | target.user.product_object_id  
DestinationUUID | target.resource.product_object_id  
DGHierarchyLevel1 | additional.fields.key/value.string_value  
DGHierarchyLevel2 | additional.fields.key/value.string_value  
DGHierarchyLevel3 | additional.fields.key/value.string_value  
DGHierarchyLevel4 | additional.fields.key/value.string_value  
DiamAppID | additional.fields.key/value.string_value  
DiamAvpCode | additional.fields.key/value.string_value  
DiameterCommandCode | additional.fields.key/value.string_value  
DiameterRequestFlag | additional.fields.key/value.string_value  
DeviceName | principal.asset.hostname  
SCTPEventType | additional.fields.key/value.string_value  
FromZone | additional.fields.key/value.string_value  
InboundInterface | additional.fields.key/value.string_value  
InboundInterfaceDetailsPort | additional.fields.key/value.string_value  
InboundInterfaceDetailsSlot | additional.fields.key/value.string_value  
InboundInterfaceDetailsType | additional.fields.key/value.string_value  
InboundInterfaceDetailsUnit | additional.fields.key/value.string_value  
CaptivePortal | additional.fields.key/value.string_value  
IsClienttoServer | additional.fields.key/value.string_value  
IsContainer | additional.fields.key/value.string_value  
IsDecryptMirror | additional.fields.key/value.string_value  
IsDecryptedPayloadForward | additional.fields.key/value.string_value  
IsDecryptedLog | additional.fields.key/value.string_value  
IsDuplicateLog | additional.fields.key/value.string_value  
LogExported | additional.fields.key/value.string_value  
LogForwarded | additional.fields.key/value.string_value  
IsIPV6 | additional.fields.key/value.string_value  
IsInspectionBeforeSession | additional.fields.key/value.string_value  
IsMptcpOn | additional.fields.key/value.string_value  
NAT | additional.fields.key/value.string_value  
IsNonStandardDestinationPort | additional.fields.key/value.string_value  
IsPacketCapture | additional.fields.key/value.string_value  
IsPhishing | additional.fields.key/value.string_value  
IsPrismaNetwork | additional.fields.key/value.string_value  
IsPrismaUsers | additional.fields.key/value.string_value  
IsProxy | additional.fields.key/value.string_value  
IsReconExcluded | additional.fields.key/value.string_value  
IsServertoClient | additional.fields.key/value.string_value  
IsSourceXForwarded | additional.fields.key/value.string_value  
IsSystemReturn | additional.fields.key/value.string_value  
IsTransaction | additional.fields.key/value.string_value  
IsTunnelInspected | additional.fields.key/value.string_value  
IsURLFiltering | additional.fields.key/value.string_value  
IsWildfire | additional.fields.key/value.string_value  
LogAction | additional.fields.key/value.string_value  
LogSourceGroupID | intermediary.resource.attribute.labels  
DeviceSN | intermediary.asset.hardware.serial_number  
DeviceName | intermediary.hostname  
LogSourceTimeZoneOffset | additional.fields.key/value.string_value  
TimeReceived | metadata.collected_timestamp  
LogType | additional.fields.key/value.string_value  
MapAppCode | additional.fields.key/value.string_value  
NATDestination | target.nat_ip  
NATDestinationPort | target.nat_port  
NATSource | principal.nat_ip  
NATSourcePort | principal.nat_port  
OutboundInterface | additional.fields.key/value.string_value  
OutboundInterfaceDetailsPort | additional.fields.key/value.string_value  
OutboundInterfaceDetailsSlot | additional.fields.key/value.string_value  
OutboundInterfaceDetailsType | additional.fields.key/value.string_value  
OutboundInterfaceDetailsUnit | additional.fields.key/value.string_value  
PacketsReceived | network.received_packets  
PacketsSent | network.sent_packets  
PacketsTotal | additional.fields.key/value.string_value  
PanoramaSN | observer.asset.hardware.serial_number  
PayloadProtocolID | additional.fields.key/value.string_value  
PlatformType | additional.fields.key/value.string_value  
ContainerName | target.resource.name  
ContainerNameSpace | target.resource.attribute.labels  
Protocol | network.ip_protocol  
Rule | security_result.rule_name  
RuleUUID | security_result.rule_id  
SccpCallingGt | additional.fields.key/value.string_value  
SccpCallingSSN | additional.fields.key/value.string_value  
SctpCauseCode | additional.fields.key/value.string_value  
SctpChunkType | additional.fields.key/value.string_value  
SctpFilter | additional.fields.key/value.string_value  
SequenceNo | metadata.product_log_id  
SessionOwnerMidx | additional.fields.key/value.string_value  
SessionEndReason | security_result.summary  
SessionID | network.session_id  
SessionTracker | additional.fields.key/value.string_value  
Severity | security_result.severity  
SourceDeviceClass | additional.fields.key/value.string_value  
SourceDeviceMac | principal.asset.mac  
SourceDeviceModel | principal.asset.hardware.model  
SourceDeviceOS | additional.fields.key/value.string_value  
SourceDeviceVendor | principal.asset.hardware.manufacturer  
SourceDynamicAddressGroup | principal.group.group_display_name  
SourceEDL | additional.fields.key/value.string_value  
SourceIP | principal.ip  
SourceLocation | principal.location.country_or_region  
SourcePort | principal.port  
SourceUser | principal.user.userid  
SourceUserDomain | principal.administrative_domain  
SourceUserName | principal.user.user_display_name  
SourceUserUUID | principal.user.product_object_id  
SourceUUID | principal.resource.product_object_id  
Subtype | metadata.product_event_type  
TimeGenerated | metadata.event_timestamp  
TimeGeneratedHighResolution | additional.fields.key/value.string_value  
ToZone | additional.fields.key/value.string_value  
Tunnel | additional.fields.key/value.string_value  
VendorName | additional.fields.key/value.string_value  
VendorSeverity | security_result.severity_details  
VerificationTag1 | additional.fields.key/value.string_value  
VerificationTag2 | additional.fields.key/value.string_value  
VirtualLocation | intermediary.asset.attribute.labels  
VirtualSystemID | intermediary.resource.product_object_id  
VirtualSystemName | intermediary.asset.attribute.labels  
  
### Audit

The following table lists the log fields of the Audit log type and their corresponding UDM fields.

Log field | UDM mapping  
---|---  
EventCategory | network.http.method  
EventDescription | metadata.description  
EventDestinationURL | target.url  
EventDestinationUserUserID | target.user.userid  
DestinationVendor | additional.fields.key/value.string_value  
EventDetails | additional.fields.key/value.string_value  
EventID | metadata.product_log_id  
EventName | additional.fields.key/value.string_value  
EventResult | security_result.summary  
EventSourceUserUserID | principal.user.userid  
EventTime | metadata.event_timestamp  
LogSource | target.resource.attribute.labels  
LogSourceGroupID | target.resource.attribute.labels  
DeviceSN | target.asset.hardware.serial_number  
DeviceName | target.hostname  
TimeReceived | metadata.collected_timestamp  
LogType | additional.fields.key/value.string_value  
PlatformType | additional.fields.key/value.string_value  
Subtype | metadata.product_event_type  
TSGID | additional.fields.key/value.string_value  
Vendor | additional.fields.key/value.string_value  
VendorSeverity | security_result.severity_details  
  
### Field mapping reference: Log types to UDM event type

The following table lists the Palo Alto Networks Strata Logging Service firewall log types and their corresponding UDM event types. 

**Log type** | **UDM event type**  
---|---  
Traffic  | NETWORK_CONNECTION   
Threat  | NETWORK_CONNECTION   
URL Filtering  | NETWORK_CONNECTION   
Tunnel  | NETWORK_CONNECTION   
System  |  If the subtype value is "dhcp", then NETWORK_DHCP is set. If the subtype value is "auth", then USER_LOGIN is set.  If the description value is "logged in", then USER_LOGIN is set.  If the description value is "logged out", then USER_LOGOUT is set.  For other values of the subtype, GENERIC_EVENT is set.   
HIP Match  | NETWORK_CONNECTION   
IP Tag  | GENERIC_EVENT   
User-ID  | USER_LOGIN/USER_LOGOUT/USER_UNCATEGORIZED  If subtype value is "login", then USER_LOGIN is set. If subtype value is "logout", then USER_LOGOUT is set.  If subtype does not contain any value, then USER_UNCATEGORIZED is set.   
Decryption  | NETWORK_CONNECTION   
Authentication  | STATUS_UNCATEGORIZED   
Globalprotect  | USER_LOGIN/USER_LOGOUT/USER_RESOURCE_ACCESS  If Stage log field value is "login", then USER_LOGIN is set. If Stage log field value is "logout", then USER_LOGOUT is set.  If Stage log field has any other value, then USER_RESOURCE_ACCESS is set.   
SCTP  | NETWORK_CONNECTION   
Audit  | GENERIC_EVENT   
  
## What's next

  * [Data ingestion to Google SecOps](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow)



## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-firewall-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
