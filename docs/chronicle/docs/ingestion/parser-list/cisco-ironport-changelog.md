---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-ironport-changelog/
title: Change log for CISCO_IRONPORT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:44:56.096793+00:00
---

# Change log for CISCO_IRONPORT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-ironport-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_IRONPORT

Date | Changes  
---|---  
2026-09-23 |  Enhancement:  
\- Modified grok patterns to parse hostname and extract `interface_data`, `target_host` correctly.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `interface_data` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-06-15 |  Enhancement:  
\- Renamed grok variable from `from` to `Message_id` and `email_domain` for better naming convention.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `internal_id` from `event.idm.read_only_udm.additional.fields` UDM field as it's a duplicate mapping.  
\- `event.idm.read_only_udm.network.email.from`: Removed mapping of `from` raw log field from `event.idm.read_only_udm.network.email.from` UDM field as it was incorrectly capturing `Message-ID` components instead of a sender email address.  
\- `event.idm.read_only_udm.intermediary.administrative_domain`: Newly mapped `email_domain` raw log field to `event.idm.read_only_udm.intermediary.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `rid`, `smtp_response_code`, `kb_sec`, `Message_id`, and `sys_priority` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added a new grok pattern to parse the new `SYSLOG` format logs.   
2026-06-05 |  Enhancement:  
\- Added support for new format of SYSLOG + CSV logs.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `sc_body_size`, `sc_location`, `x_proxy_instance_id`, `x_spoofed_ip`, `x_http_rewrite_profile_name`, `x_id_shared`, `x_wbrs_threat_reason`, `syslog_severity`, `log_date`, `log_time` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-11-13 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `web_category` raw log field to `event.idm.read_only_udm.security_result.category_details`.  
\- Added support for new format of logs with trailing CSV data.  
\- Modified grok patterns to support additional variations of the Access Log format.  
\- Updated the severity detection regex to include `Warning`.   
2025-10-27 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.risk_score`: Newly mapped `column2` raw log field(s) with `event.idm.read_only_udm.security_result.risk_score` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `column20` raw log field(s) with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `column23` raw log field(s) with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- Added a CSV filter to parse W3C log format fields from the csv_msg field.   
2025-10-21 |  Enhancement:  
\- `event.idm.read_only_udm.network.tls.cipher`: Newly mapped `ESATLSInCipher` raw log field to `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- `event.idm.read_only_udm.intermediary.administrative_domain`: Newly mapped `ESAHeloDomain` raw log field to `event.idm.read_only_udm.intermediary.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `principal_host` raw log field to `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `principal_host` raw log field to `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `internal_id`, `ESAMsgSize`, `ESAHeloIP`, `mailfrom.result`, `mailfrom.sender`, `helo.result`, `ESATLSInConnStatus`, `ESATLSOutConnStatus`, `ESATLSOutProtocol`, `Sender_Maturity` raw log field(s) to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `helo.sender` raw log field to `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- Added grok patterns to `msg1` thus additional Events support for logs having metadata.event_type `GENERIC_EVENT`.   
2025-08-28 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `ESACFVerdict`, `deviceInboundInterface` and `ESAMailFlowPolicy` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.intermediary.application: Newly mapped `syslog_program` raw log field to `event.idm.read_only_udm.intermediary.application`.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `target_user` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `target_url` raw log field to `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `src_ip` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip: Newly mapped `target_ip` raw log field to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.hostname and event.idm.read_only_udm.target.asset.hostname: Newly mapped `target_host` raw log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `start`, `end` and `interaction_mode` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `email` raw log field to `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `cs_username` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.   
2025-08-20 |  Enhancement:  
\- Added grok pattern to remove port from url.   
2025-08-06 |  Enhancement:  
\- Replaced `cs_url` with `request_method_uri` in grok patterns to map it with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.network.referral_url : Removed mapping of `cs_url` from `event.idm.read_only_udm.network.referral_url` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.target.url : Removed mapping of `cs_url` from `event.idm.read_only_udm.target.url` UDM field in order to introduce a more accurate mapping for the raw log field.   
2025-07-14 |  Enhancement:  
\- Added support for Syslog of CEF format.  
\- Added gsub to replace `'` with `"` in `ESAAttachmentDetails` and `ESASPFVerdict` raw log field.  
\- event.idm.read_only_udm.about.file.full_path: Newly mapped `file_name` raw log field with `event.idm.read_only_udm.about.file.full_path` UDM field.  
\- event.idm.read_only_udm.about.file.sha256: Newly mapped `AMP.fileHash` raw log field with `event.idm.read_only_udm.about.file.sha256` UDM field.  
\- event.idm.read_only_udm.about.url: Newly mapped `ESAURLDetails` raw log field with `event.idm.read_only_udm.about.url` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `ESASenderGroup`, `ESAAMPVerdict`, `ESAASVerdict`, `ESAAVVerdict`, `Verdict` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `column2` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `column3` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `column1` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.network.email.from: Newly mapped `mailfrom.sender` raw log field with `event.idm.read_only_udm.network.email.from` UDM field.  
\- Added null condition check for `msg1` raw log field before mapping it to `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ESAAttachmentDetails`, `result`, `ESADCID`, `ESAICID`, `ESAMID`, `content_type`, `elapsed_time` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Remove redundant code for additional fields mapping.  
\- Remove redundant code for `security_result.detection_fields` mapping.   
2025-07-08 |  Enhancement:  
\- Added Grok patterns to `msg1` data field to parse it following fields.  
\- Added a Grok pattern for `dst_ip1` data field to parse it following IP address correctly.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `sc_bytes`, `uritype`, `proto`, `vendorid`, `varianttype`, and `uriidvalue` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.url` : Newly mapped `cs_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent` : Newly mapped `cs_user_agent` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- When `c_ip` is mapped to `event.idm.read_only_udm.principal.ip` UDM field then set `has_principal_ip` to `true`.  
\- When `s_ip` is mapped to `event.idm.read_only_udm.target.ip` UDM field then set `has_target_ip` to `true`.  
\- When `s_computerName` is mapped to `event.idm.read_only_udm.target.hostname` then set `has_target` to `true`.   
2025-06-18 |  Enhancement:  
\- Added a Grok pattern to parse new type of SYSLOG logs.  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname: Removed mapping of `hostname` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.intermediary.hostname and event.idm.read_only_udm.intermediary.asset.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM fields.  
\- event.idm.read_only_udm.target.port: Newly mapped `dst_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `useragent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `response_code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.   
2025-06-06 |  Enhancement:  
\- Modified the Grok pattern to parse `s_hostname` value properly from `x_hierarchy_origin` raw log field.  
\- event.idm.read_only_udm.additional.fields: Removed mapping of `cs_x_forwarded_for` from `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Mapped `cs_x_forwarded_for` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.   
2025-05-28 |  Enhancement:  
\- Added grok patterns to parse new pattern of syslog logs.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `target_host` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.about.hostname: Newly mapped `about_hostname` raw log field with `event.idm.read_only_udm.about.hostname` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `cs_user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `cs_method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `cs_url` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Added Grok pattern to match IP address then mapped `c_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `c_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `cs_username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.target.ip, event.idm.read_only_udm.target.asset.ip: Added Grok pattern to match IP address then mapped `s_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `s_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `session_time`, `x_webcat_code_full`, `x_result_code`, `cs_version`, `cs_x_forwarded_for`, `cs_mime_type`, `cs_referer`, `x_req_dvs_scanverdict`, `x_sophos_file_name`, `x_elapsed_time`, `s_hierarchy`, `cs_auth_group`, `cs_bytes`, `cs_uri`, `x_acltag`, `x_ids_verdict`, `x_resp_dvs_canverdict`, `x_resp_dvs_threat_name`, `x_resp_dvs_verdictname`, `user_type`, `x_suspect_user_agent`, `x_wbrs_threat_type`,`x_webcat_req_code_abbr`, `x_webroot_scanverdict`, `x_webroot_threat_name`, `x_webroot_trace_id`, `x_webroot_trr`, `x_webcat_resp_code_abbr`, `x_wbrs_score`, `x_sophos_virus_name`, `x_sophos_scanverdict`,`x_sophos_scanerror`, `x_mcafee_av_virustype`, `x_mcafee_av_virusname`, `x_mcafee_av_scanerror`,`x_req_dvs_verdictname`,`x_mcafee_av_scanverdict`, `x_mcafee_filename`,`x_mcafee_av_detecttype`, `x_icap_server`,`x_avc_behaviour`,`x_app_type`,`x_app`,`x_amp_verdict`,`x_amp_upload_indicator`,`x_amp_sha`,`x_amp_score`, `x_amp_malware_name`, `x_amp_filename`, `sc_result_code_denial` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added gsub to remove `\\"` from `x_mcafee_av_virustype`, `x_webcat_resp_code_abbr` and `x_wbrs_threat_type` raw log fields.  
\- event.idm.read_only_udm.about: Merged `about` raw log field with `event.idm.read_only_udm.about` UDM field.   
2025-03-18 |  Enhancement:  
\- Modified Grok patterns to parse `hostname` to `principal.hostname` field.  
\- Mapped the `hostname` to `principal.hostname` properly ,previously processName was getting mapped to `principal.hostname` field.  
\- Mapped `processName` to `principal.process.file.full_path`.  
\- Added a grok checker to extract the Ip address properly.   
2025-02-26 |  Enhancement:  
\- Added support for syslog logs.   
2025-01-31 |  Enhancement:  
\- Added support for SYSLOG logs.   
2024-10-16 |  Enhancement:  
\- Mapped `res` to `security_result.action_details`.  
\- Mapped `dkim` to `security_result.summary`.  
\- Mapped `email` to `principal.user.email_addresses`.   
2024-09-19 |  Enhancement:  
\- Mapped `subject` to `additional.fields`.  
\- Mapped `antivirus` to `security_result.detection_fields`.  
\- Mapped `threat_level` to `security_result.detection_fields`.  
\- Mapped `threat_category` to `security_result.detection_fields`.  
\- Mapped `suspected_domain` to `security_result.detection_fields`.   
2024-06-11 |  Enhancement:  
\- Added Grok patterns to parse new format unparsed logs.   
2024-02-07 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
