---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vectra-stream-changelog/
title: Change log for VECTRA_STREAM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:29:31.739493+00:00
---

# Change log for VECTRA_STREAM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vectra-stream-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for VECTRA_STREAM

Date | Changes  
---|---  
2025-08-28 |  \- target.hostname: Prioritized mapping of `resp_hostname` raw log field with `target.hostname` UDM field for logs in KV format.  
\- target.asset.hostname: Prioritized mapping of `resp_hostname` raw log field with `target.asset.hostname` UDM field for logs in KV format.  
\- If `resp_hostname` raw log field contains value of IP address, then mapped `resp_hostname` raw log field with `target.ip` UDM field for logs in KV format. Else, mapped `resp_hostname` raw log field with `target.hostname` UDM field for logs in KV format.   
2025-06-03 |  \- Added Fallback parser for VECTRA_STREAM to handle log_type other than JSON.   
2025-05-15 |  \- Modify the Stream Parser to support only JSON format and modify the UDM mapping.   
2025-02-11 |  Enhancement:  
\- Mapped `eve_json.alert.signature` to `security_result.summary`.   
2025-01-28 |  Enhancement:  
\- Mapped `eve_json.alert.category` to `security_result.category_details`.  
\- Mapped `eve_json.alert.metadata.attack_target`,`eve_json.alert.metadata.deployment`,`eve_json.alert.metadata.tag`,`eve_json.alert.rev`,`eve_json.alert.signature_id`,`eve_json.app_proto`,`eve_json.direction`,`rrtype`,`tx_id`,`type`,`eve_json.flow.pkts_toclient`,`eve_json.flow.start`,`eve_json.flow_id`,`eve_json.packet`,`eve_json.packet_info.linktype`,`eve_json.payload`,`eve_json.payload_printable`,`eve_json.pkt_src`,`eve_json.proto`,`eve_json.stream`,`eve_json.tx_id`,`eve_json.vlan`,`id.ip_ver`,`local_orig`,`local_resp`,`orig_huid`,`resp_huid` and `resp_sluid` to additional.fields.  
\- Mapped `eve_json.alert.metadata.signature_severity` to `security_result.severity`.  
\- Mapped `eve_json.alert.signature` to `security_result.summary`.  
\- Mapped `eve_json.alert.gid` to `target.group.product_object_id`.  
\- Mapped `eve_json.alert.metadata.confidence` to `security_result.confidence`.  
\- Mapped `eve_json.dest_ip` and `eve_json.flow.dest_ip` to `target.ip` and `target.assest.ip`.  
\- Mapped `eve_json.dest_port` and `eve_json.flow.dest_port` to `target.port`.  
\- Mapped `rrname` to `dns.questions.name`.  
\- Mapped `eve_json.flow.bytes_toclient` to `network.sent_bytes`.  
\- Mapped `eve_json.flow.bytes_toserver` to `network.received_bytes`.  
\- Mapped `eve_json.flow.src_ip` and `eve_json.src_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `eve_json.flow.src_port` and `eve_json.src_port` to `principal.port`.   
2025-01-10 |  Enhancement:  
\- Renamed `id.orig_h`, `id.orig_p`, `id.resp_h`, `id.resp_p` to `idorig_h`, `idorig_p`, `idresp_h`, `idresp_p` respectively.  
\- Mapped `idorig_h` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `idorig_p` to `principal.port`.  
\- Mapped `resp_h` to `target.ip` and `target.assest.ip`.  
\- Mapped `resp_p` to `target.port`.   
2024-07-26 |  Enhancement:  
\- Mapped `attributes` to `additional.fields`.   
2024-06-18 |  Enhancement:  
\- Mapped `first_orig_resp_data_pkt`, `first_orig_resp_data_pkt_time`, `cookie`, `keyboard_layout`, `name`, and `query_scope` to `additional.fields`.  
\- Mapped `operation` to `security_result.action_details`.   
2024-02-26 |  Enhancement:  
\- Handled DHCP logs.   
2024-01-12 |  Enhancement:  
\- Handled invalid JSON in `rcpt_to` field.   
2023-10-15 |  Enhancement:  
\- Handled unparsed JSON logs having field `metadata_type` as `metadata_smbfiles`.  
\- Mapped `dns_server_ips` to `principal.ip`.  
\- Mapped `assigned_ip` to `network.dhcp.yiaddr`.  
\- Mapped `dhcp_server_ip` to `network.dhcp.giaddr`.  
\- Mapped `path` to `target.file.full_path`.   
2023-09-14 |  Fix -  
\- Initialized `uid`, `metadata_type`, `orig_sluid`, `intermediary`, `has_target_file`, `qclass_name` to null.  
\- Added not null check to `uid` and `metadata_type` prior to mapping to UDM.  
\- Mapped `orig_sluid` to `principal.hostname` if `orig_hostname` is null.  
\- Mapped `qclass_name` to `question.name`.  
\- Added a check to event_type `FILE_MODIFICATION` to verify that `target.file` is not null.   
2023-07-31 |  Bug-Fix-  
\- Added `on_error` check for `date` filter.   
2023-07-24 |  Bug-Fix-  
\- Added check for `UNIX` and `UNIX_MS` timestamp check before mapping `certificate.not_valid_after` to `network.tls.client.certificate.not_after`.  
\- Added check for `UNIX` and `UNIX_MS` timestamp check before mapping `certificate.not_valid_before` to `network.tls.client.certificate.not_before`.   
2022-10-27 |  Enhancement-  
Added Json support for the logs.  
Added extra grok pattern for failing logs.  
Added extra grok pattern for the `_raw` data present in some json logs.  
Added `metadata_type` conditions along with already present `log_type` conditions for json logs.  
Mapped `status_code` to `network.http.response_code`.  
Mapped `user_agent` to `network.http.user_agent`.  
Added condtions to check if the data is from json log inorder to convert the integer/float values to string for variables:  
`version_num`,`certificate.not_valid_before`,`certificate.not_valid_after`,`certificate.versio`.  
Added condtions to check if the data is from syslog inorder to convert the string values to boolean for variables:  
`AA`,`RD`,`RA`,`TC`,`established`.  
Added condition to check if `duration` is extracted from json log or syslog.  
Added grok pattern to extract `answers` as string from json logs.   
2022-10-25 |  Enhancement-Added mappings  
-common fields  
sensor_uid mapped to observer.asset_id.  
-metadata_radius  
account_session_id mapped to network.session_id.  
account_session_time mapped to network.session_duration.  
calling_station_id mapped to intermediate.asset.product_object_id.  
connect_info mapped to security_result.description.  
radius_type mapped to metadata.description.  
result mapped to security_result.summary.  
nas_identifier mapped to target.user.attribute.roles.name.  
dst_display_name mapped to target.hostname.  
dst_luid mapped to target.asset.product_object_it.  
src_display_name mapped to principal.hostname.  
src_luid mapped to principal.asset.product_object_it.  
-metadata_beacon  
beacon_type mapped to metadata.description  
beacon_uid mapped to network.session_id  
ja3 mapped to network.tls.ja3  
-metadata_httpsessioninfo  
method mapped to network.http.method.  
uri mapped to target.url.  
host mapped to target.hostname.  
referrer mapped to network.http.referral_url.  
user_agent mapped to network.http.user_agent.  
orig_mime_types mapped to principal.file.mime_type.  
resp_mime_types mapped to target.file.mime_type.  
status_code mapped to network.http.response_code.  
status_msg mapped to security_result.summary.  
proxied mapped to principal.ip.  
host_multihomed mapped to additionals.key/value  
-metadata_ldap  
query mapped to principal.process.command_line.  
result mapped to security_result.description.  
result_code mapped to security_result.action_details.  
-metadata_ntlm  
hostname mapped to target.hostname.  
domain mapped to target.domain.name.  
status mapped to security_result.summary.  
success mapped to seucirty_result.action.  
-metadata_rdp  
cookie mapped to target.user.userid  
-metadata_smbfiles  
action mapped to metadata.event_type (FILE_*)  
name mapped to target.file.full_path.  
version mapped to principal.platform_version.  
-metadata_smbmapping  
path mapped to target.file.full_path.  
-metadata_ssh  
client mapped to principal.application.  
server mapped to target.application.  
cipher_alg mapped to network.tls.cipher.  
mac_alg mapped to additionals.key/value.  
compression_alg mapped to additionals.key/value.  
kex_alg mapped to additionals.key/value.  
host_key_alg mapped to additionals.key/value.  
host_key mapped to additionals.key/value.  
hassh mapped to additionals.key/value.  
hasshServer mapped to additionals.key/value.   
2022-07-22 |  Enhancement-Added mappings  
radius log type mapped to metadata.event_type=NETWORK_FLOW.  
beacon log type mapped to metadata.event_type=NETWORK_FLOW.  
httpsessioninfo log type mapped to metadata.event_type=NETWORK_NETWORK_HTTP.  
ldap log type mapped to metadata.event_type=NETWORK_USER_STATS.  
smbmapping log type mapped to metadata.event_type=NETWORK_FLOW.  
ntlm log type mapped to metadata.event_type=NETWORK_CONNECTION.  
rdp log type mapped to metadata.event_type=NETWORK_CONNECTION.  
smbfiles log type mapped to metadata.event_type=NETWORK_FTP.  
ssh log type mapped to metadata.event_type=NETWORK_CONNECTION.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
