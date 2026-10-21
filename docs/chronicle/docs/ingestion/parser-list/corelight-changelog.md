---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/corelight-changelog/
title: Change log for CORELIGHT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:01:03.460980+00:00
---

# Change log for CORELIGHT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/corelight-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CORELIGHT

Date | Changes  
---|---  
2026-10-06 |  \- `corelight_ml_results`: Added support for the event `corelight_ml_results` and relevant corresponding raw log fields.  
\- `net_perf`: Added support for the event `net_perf` and relevant corresponding raw log fields.  
\- `yara`: Added support for the event `yara` and relevant corresponding raw log fields.   
2026-06-01 |  \- `asset_classification`: Added support for the event `asset_classification` and relevant corresponding raw log fields.   
2026-05-15 |  \- `network.application_protocol`: Added new `TELNET`, `SFTP`, `IMAP`, `POP3`, and `IRC` enums to the `network.application_protocol` UDM field.   
2026-05-04 |  Additional Fields Mapping:  
\- Newly mapped `uid` and `uids` raw log field with `metadata.ingestion_labels[uid]` UDM field.  
\- Newly mapped `user_agents` and `user_agent` raw fields for `http`, `http_red`, `http2`, `http_agg` log types with `about.network.http.user_agent` UDM field.  
\- Newly mapped `subject` raw field for `ssl`, `ssl_agg` and `ssl_red` log types with `network.tls.server.certificate.subject` UDM field.  
\- Newly mapped `mime_type` and `mime_types` raw fields for `files`, `files_red` and `files_agg` log types with `about.file.mime_type` UDM field.  
\- Newly mapped `certificate.issuer` raw field for `files`, `files_red` and `files_agg` log types with `about.labels[certificate_issuer]` UDM field.  
Update Field Mapping - change the UDM field:  
\- Updated mapping of `service` from `about.labels[service]` to `about.namespace` UDM field for `conn`, `conn_red`, `conn_long` and `conn_agg` log types.  
Update Field Mapping - change value only:  
\- Updated value of `metadata.event_type` UDM field from `NETWORK_UNCATEGORIZED` to `NETWORK_CONNECTION` for `ntp` log type.  
Other Updates:  
\- Added mapping of `network.application_protocol` UDM field for log types whose `_path` raw log field value exists in `application_protocol` enum values set.  
\- Updated enum values list for `network.application_protocol`.  
\- Improved precision of `network.session_duration` up to nanoseconds.   
2026-02-12 |  Additional Events Parsing:  
\- AWS VPC logs: Added support for the event `AWS VPC logs` and relevant corresponding raw log fields.  
Update Field Mapping - change the UDM field:  
\- `network.session_id`: Removed mapping of `session_handle`, `call_id`, `session_id`, `trans_id`, and `flow_id` from `network.session_id` UDM field.  
\- `about.labels`: Mapped `session_handle` raw log field with `about.labels[session_handle]` UDM field.  
\- `about.labels`: Mapped `call_id` raw log field with `about.labels[call_id]` UDM field.  
\- `about.labels`: Mapped `session_id` raw log field with `about.labels[session_id]` UDM field.  
\- `metadata.product_log_id`: Mapped `trans_id` raw log field with `metadata.product_log_id` UDM field.  
\- `about.labels`: Mapped `flow_id` raw log field with `about.labels[flow_id]` UDM field.   
2025-11-25 |  \- security_result.detection_fields: Removed unintended mapping of `host_key` raw log field from `security_result.detection_fields` UDM field for `SSH` log name.  
\- Enhanced the `inferences` raw log field mapping for the `VPN` log name.   
2025-10-30 |  \- Added support for `analyzer`, `anomaly`, `ssdp`, `telnet`, `websocket`, `first_seen` events and corresponding raw log fields.  
\- Enhanced the Corelight parser. Please find the updated field mapping delta in the [Corelight Secops document](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/corelight).   
2025-07-29 |  \- `conn_agg`: Added support for the event `conn_agg` and relevant corresponding raw log fields.  
\- `dns_agg`: Added support for the event `dns_agg` and relevant corresponding raw log fields.  
\- `files_agg`: Added support for the event `files_agg` and relevant corresponding raw log fields.  
\- `http_agg`: Added support for the event `http_agg` and relevant corresponding raw log fields.  
\- `ssl_agg`: Added support for the event `ssl_agg` and relevant corresponding raw log fields.  
\- `weird_agg`: Added support for the event `weird_agg` and relevant corresponding raw log fields.  
\- Handled `extracted` raw log field for files_red event.   
2025-04-23 |  Modified the static value of `security_result.summary` UDM field from `Providioned` to `Provisioned` for the event `ssh`.   
2025-04-08 |  Updated principal.hostname mapped as per the new event_type validation.   
2024-09-20 |  Added support for new fields of these log types(v27.12): [conn_red, ldap, known_remotes, weird, suricata_corelight, stun_nat, ssl_red, ftp, smb_files, s7comm, dce_rpc, syslog, ldap_search, smtp_links, http, bacnet, kerberos, tds_rpc, dpd, tds, http_red, irc, http2, known_domains, conn, intel, mqtt_connect, profinet_dce_rpc, known_certs, rfb, x509, tunnel, mqtt_subscribe, snmp, socks, ipsec, ntlm, ssl, modbus, corelight_burst, profinet_debug, tds_sql_batch, stun, sip, dnp3, profinet, smb_mapping, known_devices, radius, wireguard, conn_long, x509_red, vpn, dns, mysql, known_services, rdp, notice, ntp, enip, dga, weird_red, known_names, ssh, smtp, files, known_hosts, dns_red, mqtt_publish, cip, local_subnets_dj, known_users, icmp_specific_tunnels]   
2024-08-23 |  Modifying severity based on raw rule.   
2024-07-26 |  Added support for new fields of updated schema of suricata_corelight.   
2024-06-19 |  Extracted the key and value based on the delimiter and mapped it accordingly.   
2024-05-01 |  Added support for mapping of base64 decoded value of `payload` and `packet` fields into `about.labels`.   
2024-02-26 |  Added support for mapping of `_write_ts` and `extracted` fields.   
2024-02-14 |  Update the mapping for `network.dns.response` UDM field.   
2023-12-13 |  Added support for updated suricata, corelight_metrics_*, intel  
log type and validation for `entity_type`.   
2023-11-29 |  Aligned `principal/target.hostname` and `principal/target.asset.hostname` mapping.   
2023-10-04 |  Added mapping for `network.tls.certificate.md5`, `network.tls.certificate.sha1`, and `network.tls.certificate.sha256`.   
2023-06-13 |  Enhanced existing parser.   
2023-06-09 |  Mapped `assigned_addr` to `network.dhcp.ciaddr`.   
2022-04-23 |  Added normalization for Suricata Eve alerts.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
