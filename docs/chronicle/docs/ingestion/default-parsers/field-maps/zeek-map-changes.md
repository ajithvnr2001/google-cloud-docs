---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/field-maps/zeek-map-changes/
title: Mapping changes in Zeek (Bro) parser \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:45.157338+00:00
---

# Mapping changes in Zeek (Bro) parser  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/field-maps/zeek-map-changes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Mapping changes in Zeek (Bro) parser

This document describes the changes made in the Zeek (Bro) default parser on 2022-09-28.

The Zeek (Bro) default parser update on 2022-09-28 uses the logs as defined in the official Zeek documentation.

The following table lists the field mapping changes between the Zeek (Bro) parser previous versions and Zeek (Bro) default parser version 2022-09-28:

Log type | Fields | Mapping in previous version | Mapping in default parser version 2022-09-28  
---|---|---|---  
ssl  | server_name  | target.hostname  | network.tls.client.server_name   
| ja3  | network.tls.client.ja3  | Not mapped.   
| ja3s  | network.tls.server.ja3s  | Not mapped.   
|  | metadata.description is set to "SSL/TLS handshake info"  | Not mapped.   
ssh  | client  | network.tls.client.certificate.version  | principal.platform_version   
| server  | network.tls.server.certificate.version  | target.platform_version   
| host_key  | target.labels  | about.labels   
| host_key_alg  | target.labels  | about.labels   
| kex_alg  | target.labels  | about.labels   
| mac_alg  | target.labels  | about.labels   
| compression_alg  | target.labels  | about.labels   
| cipher_alg  | target.labels  | about.labels   
| auth_attempts  | target.labels  | about.labels   
| auth_success  | security_result.action  | about.labels   
| event_type  | metadata.event_type is set to "NETWORK_CONNECTION"  | metadata.event_type is set to "NETWORK_UNCATEGORIZED"   
http  |  | network.application_protocol is set to "HTTP"  | Not mapped.   
files  | received_bytes  | network.received_bytes  | target.file.size   
dhcp  | domain  | principal.administrative_domain  | target.administrative_domain   
| dhcp_info  | network.dhcp.type  |   
smb_files  | action  | metadata.description  | metadata.description" is set to "action: %{action} on: %{name}"   
|  | network.application_protocol is set to "SMB"  | Not mapped.   
kerberos  | user_name  | principal.user.userid  | Not mapped.   
| user_email  | principal.user.email_addresses  | Not mapped.   
| event_type  | metadata.event_type is set to "GENERIC_EVENT"  | metadata.event_type is set to "NETWORK_CONNECTION"   
ftp  | uid  | metadata.product_log_id  | Not mapped.   
| file_size  | principal.file.size  | src.file.size   
x509  | event_type  | metadata.event_type is set to "NETWORK_UNCATEGORIZED"  | metadata.event_type is set to "GENERIC_EVENT"   
| id  | metadata.product_log_id  | Not mapped.   
| _system_name  | principal.hostname  | Not mapped.   
smb_mapping  | path  | target.resource.name  | target.file.full_path   
|  | network.application_protocol is set to "SMB"  | Not mapped.   
nltm  |  | metadata.description is set to "NTLM"  | Not mapped.   
dce_rpc  |  | metadata.description is set to "DCE_RPC"  | Not mapped.   
|  | network.application_protocol is set to "RPC"  | Not mapped.   
tunnel  |  | metadata.description is set to "Tunnel"  | Not mapped.   
| tunnel_type  | additional.fields  | security_result.description   
| action  | additional.fields  | security_result.description   
mysql  | event_type  | metadata.event_type" is set to "NETWORK_CONNECTION"  | metadata.event_type" is set to "NETWORK_UNCATEGORIZED"   
|  | metadata.description is set to "MYSQL"  | Not mapped.   
| cmd  | additional.fields  | metadata.description   
| arg  | additional.fields  | principal.process.command_line   
| rows  | additional.fields  | security_result.description   
radius  |  | extensions.auth.type is set to "AUTHTYPE_UNSPECIFIED"  | Not mapped.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
