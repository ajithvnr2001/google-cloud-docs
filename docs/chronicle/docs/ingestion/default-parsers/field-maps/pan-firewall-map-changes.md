---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/field-maps/pan-firewall-map-changes/
title: Mapping changes in Palo Alto Networks firewall parser \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:39:18.384584+00:00
---

# Mapping changes in Palo Alto Networks firewall parser  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/field-maps/pan-firewall-map-changes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Mapping changes in Palo Alto Networks firewall parser

This document describes the field mapping changes made in the Palo Alto Networks firewall default parser on 2022-09-28.

Log types | Log fields | UDM mapping in previous versions | UDM mapping in default parser version 2022-09-28  
---|---|---|---  
All log types (LEEF)  | Session End Reason  | security_result.detection_fields.key/value  | security_result.summary   
All log types (LEEF)  | Bytes  | security_result.detection_fields.key/value  | about.labels.key/value   
All log types (LEEF/CSV)  | Source Zone  | security_result.detection_fields.key/value  | principal.labels.key/value   
All log types (LEEF/CSV)  | Destination Zone  | security_result.detection_fields.key/value  | target.labels.key/value   
All log types (LEEF)  | intermediary (observer_hostname)  | intermediary.hostname  | observer.hostname   
All log types (LEEF)  | action  | If "action" is "BLOCK", "event.idm.is_alert" is set to "true". If "action" is "sinkhole" and format is "LEEF", "security_result.action" is set to "ALLOW_WITH_MODIFICATION".  If "action" is "sinkhole" and format is "CSV", "security_result.action" is set to "BLOCK".  | If "action" is "BLOCK", "event.idm.is_alert" isn't set to "true"  If "action" is "sinkhole", "security_result.action" is set to "BLOCK"   
TRAFFIC  | Serial  | metadata.product_log_id  | intermediary.asset.hardware.serial_number   
TRAFFIC  | NAT Source IP  | src.ip, principal.nat_ip  | principal.nat_ip   
TRAFFIC  | NAT Destination IP  | If "natDstAddress" is not equal to "dstAddress", NAT Destination IP is mapped to "target.nat_ip" and "target.ip"  | target.nat_ip   
TRAFFIC  | Destination Zone  | security_result.detection_fields.key/value  | target.labels.key/value   
TRAFFIC  | Bytes Sent  | network.sent_bytes  | network.received_bytes   
TRAFFIC  | Bytes Received  | network.received_bytes  | network.sent_bytes   
TRAFFIC  | Elapsed Time  | network.session_duration.seconds  | about.labels.key/value   
TRAFFIC  | Category  | security_result.description  | security_result.category_details   
TRAFFIC  | Application  | CSV is set to security_result.about.application  LEEF is set to principal.application  | target.application   
THREAT  | Tunnel Type  | security_result.category_details  | about.labels.key/value   
THREAT  | Threat/Content Name  | security_result.summary  | security_result.threat_name   
THREAT  | NAT Source IP  | principal.nat_ip  src.ip  | principal.nat_ip   
THREAT  | X-Forwarded-For  | if index == 0, principal.ip  if index > 0, then, intermediary.ip  | principal.ip   
THREAT  | URL/Filename  | target.file.full_path  target.hostname  target.url  | target.file.full_path  target.url   
THREAT  | Application [all subtype except "file", "url"]  | security_result.about.application  | target.application   
THREAT  | Application [subtype "file", "url"]  | security_result.about.application  | network.application_protocol   
THREAT  | Category  | security_result.description  | security_result.category_details   
THREAT  | Threat Category  | security_result.category_details  | security_result.detection_fields   
THREAT  | HTTP Headers  | If "httpHeaders" contains "travel" or "computer-and-internet-info", it is mapped to "security_result.category_details", else it is not mapped.  | about.labels.key/value   
THREAT  | Cloud  | target.file.sha256  | about.labels.key/value   
THREAT  | Serial Number  | metadata.product_log_id  | intermediary.asset.hardware.serial_number   
THREAT  | Severity  |  If Severity is "critical" or subtype is "wildfire-virus", "wildfire", "virus", "vulnerability", "scan", or "spyware", "security_result.severity" is set to "HIGH".  If severity is "low", "security_result.severity" is set to "LOW".  If severity is "medium", "security_result.severity" is set to "MEDIUM"  If severity is "informational", "security_result.severity" is set to "INFORMATIONAL"  If severity is "high", "security_result.severity" is set to "HIGH"  If severity is "error", "security_result.severity" is set to "ERROR"  If severity is "critical", "security_result.severity" is set to "CRITICAL"  | security_result.severity_details   
THREAT (LEEF)  | URL/Filename [subtype "virus", "wildfire-virus", "wildfire", "file"]  | security_result.description  | target.file.full_path   
THREAT (LEEF)  | URL/Filename [subtype "url"]  | security_result.description  | target_url   
THREAT (LEEF)  | Threat Category  | security_result.category_details  | security_result.detection_fields.key/value   
THREAT (LEEF)  | URL/Filename [subtype all]  | "urlHostname" and "urlPath" are extracted from Miscellaneous and "urlHostname" is mapped with "target.hostname"  | Not mapped   
THREAT (LEEF)  | Application  | network.application_protocol  If Application is DNS, then  network.dns.opcode is set to 0  metadata.event_type" is set to "NETWORK_DNS"  dnsQuestion.name" is set to "%{urlHostname}"  dnsQuestion.name" is set to "%{dst}"  | If subtype is "file" or "url", map Application to network_application_protocol.   
SYSTEM  | platform_version [subtype globalprotect]  | principal.platform_version  | principal.asset.software.platform_version   
SYSTEM  | Description [subtype dhcp]  | Extracted mac using grok  principal.mac is set to "%{mac}"  "Extracted ""dhcp_client_hostname"" and mapped with network.dhcp.client_hostname and principal.hostname"  | Extracted mac using grok  network.dhcp.chaddr is set to "%{mac}"  Extracted ""dhcp_client_hostname"" and mapped with network.dhcp.client_hostname   
SYSTEM  | Device Name [subtype dhcp]  | network.dhcp.sname and intermediary.hostname  | intermediary.hostname   
SYSTEM  | Event ID, Description [subtype "url-filtering", "userid","monitoring", syslog", "general", "vpn", "satd", "panorama-check"]  | metadata.description is set to "%{Event ID}" -- "%{Description}"  | metadata.description is set to "%{Description}"   
SYSTEM  | action  | security_result.action = ALLOW or BLOCK or UNKNOWN_ACTION  if type == SYSTEM and subType = auth/globalprotect  action = ALLOW  if [Message] ~= Login Failed  action = BLOCK  | If type is SYSTEM and subType is auth/globalprotect and message contains "Login Failed", security_result.action is set to "BLOCK".  
SYSTEM  | deviceName [subtype globalprotect]  | If "Event ID" includes "globalprotectgateway-config" and deviceName is not empty then, event_type is set to RESOURCE_CREATION, deviceName is mapped to target.resource.resource_name, and target.resource.resource_type is set to ACCESS_POLICY.  | target.resource.name  target.resource.resource_type is not set   
USERID (CSV format)  | User  | principal.user.userid  principal.administrative_domain  target.user.email_addresses  | target.user.userid  target.administrative_domain  target.user.email_addresses   
USERID  | Device Name  | target.hostname  | intermediary.hostname   
USERID  | security_result.action  | IF USER_LOGIN, security_result.action is set to ALLOW  else if USER_LOGOUT, security_result.action is set to UNKNOWN_ACTION  | Not Mapped.   
USERID  | User by Source  | target.user.userid  target.user.email_addresses  | principal.user.userid  principal.administrative_domain  principal.user.email_addresses   
USERID (LEEF format)  | User  | about.user.userid  | target.user.userid   
HIPMATCH  | Host ID  | principal.mac  | principal.asset.product_object_id   
HIPMATCH  | IPv6 System Address  | src.ip  principal.nat_ip  | principal.asset.ip   
HIPMATCH  | Machine Name  | target.resource.name  resource.resource_type is set to "DEVICE"  | principal.hostname   
HIPMATCH  | Operating System  | principal.platform  | principal.asset.platform_software.platform(enum)   
HIPMATCH  | Device Name  | target.hostname  | intermediary.hostname   
HIPMATCH  | UDM EVENT TYPE  | SCAN_HOST  | STATUS_UPDATE   
HIPMATCH (LEEF)  | Source User  | about.user.userid  | principal.user.userid   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
