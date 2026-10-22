---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netskope-webproxy-changelog/
title: Change log for NETSKOPE_WEBPROXY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:38.823612+00:00
---

# Change log for NETSKOPE_WEBPROXY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netskope-webproxy-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for NETSKOPE_WEBPROXY

Date | Changes  
---|---  
2026-08-25 |   
2026-08-07 |   
2026-07-31 |   
2026-06-05 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `x_c_hostname` from `event.idm.read_only_udm.additional.fields` UDM field to map it to more appropriate UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Mapped `x_c_hostname` log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Removed mapping of `cs-host` and `cs_host` from `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields to map it to more appropriate UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `cs-host` and `cs_host` log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Removed mapping of `cs-dns` and `cs_dns` from `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields to map it to more appropriate UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `cs-dns` and `cs_dns` log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Removed GROK patterns previously used for parsing CSV logs as these are now processed by a CSV filter.   
2026-05-19 |  Enhancement:  
\- Removed Grok patterns for web transaction logs and parsed these as CSV.  
\- Added support for transaction logs.  
\- `event.idm.read_only_udm.principal.file.size`: Removed mapping of `x_rs_file_size` from `event.idm.read_only_udm.principal.file.size` UDM field to map it to more appropriate UDM field.  
\- `event.idm.read_only_udm.principal.process.file.size`: Mapped `x_rs_file_size` raw log field with `event.idm.read_only_udm.principal.process.file.size` UDM field.  
\- `event.idm.read_only_udm.additional`: Removed mapping of `x_rs_file_type` from `event.idm.read_only_udm.additional` UDM field to map it to more appropriate UDM field.  
\- `event.idm.read_only_udm.principal.process.file.mime_type`: Mapped `x_rs_file_type` raw log field with `event.idm.read_only_udm.principal.process.file.mime_type` UDM field.  
\- Added a grok pattern on `prin_port` to extract `prin_port_check`  
\- Added a grok pattern on `x_rs_file_size` to extract `x_rs_file_size_int`  
\- Added a grok pattern on `uri_port` to extract `uri_port`  
\- `event.idm.read_only_udm.network.tls.server.certificate.not_before`: Newly mapped `x_r_cert_start` raw log field with `event.idm.read_only_udm.network.tls.server.certificate.not_before` UDM field.  
\- `event.idm.read_only_udm.network.tls.server.certificate.not_after`: Newly mapped `x_r_cert_end` raw log field with `event.idm.read_only_udm.network.tls.server.certificate.not_after` UDM field.  
\- `event.idm.read_only_udm.additional`: Newly mapped `x_tenant_id`, `x_r_country`, `x_r_latitude`, `x_r_longitude`, `x_r_location` , `x_r_region`, `x_r_zipcode`, `x_c_authz_source`, `x_cs_app_instance_tags`, `x_cs_ssl_malformed_ssl` , `x_cs_access_proxy`, `x_c_local_timestamp` raw log fields with `event.idm.read_only_udm.additional` UDM field.  
\- Added a check to drop logs if `message` starts with `_id,`.   
2026-04-21 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip`: Removed mapping of `s_ip` from `event.idm.read_only_udm.principal.ip` UDM field to map it to more appropriate UDM field.  
\- `event.idm.read_only_udm.target.ip`: Mapped `s_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.md5`: Removed mapping of `file_md5` from `event.idm.read_only_udm.principal.process.file.md5` UDM field to map it to more appropriate UDM field.  
\- `event.idm.read_only_udm.principal.file.md5`: Mapped `file_md5` raw log field with `event.idm.read_only_udm.principal.file.md5` UDM field.  
\- `event.idm.read_only_udm.principal.resource.id`: Removed mapping of `device_sn` from `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Mapped `device_sn` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- Added support for a new log format for alert events where `column2` is `Client` and `column6` is `yes`.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `act_user`, `from_user`, and `userkey` raw log fields with `event.idm.read_only_udm.principal.user.email_addresses` UDM field if these are valid email addresses.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `act_user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `cs_app` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.network.email.bcc`: Newly mapped `bcc` raw log field with `event.idm.read_only_udm.network.email.bcc` UDM field.  
\- `event.idm.read_only_udm.network.email.cc`: Newly mapped `cc` raw log field with `event.idm.read_only_udm.network.email.cc` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `source_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `process_path` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.names`: Newly mapped `process_name` raw log field with `event.idm.read_only_udm.principal.process.file.names` UDM field.  
\- `event.idm.read_only_udm.principal.file.full_path`: Newly mapped `file_path` raw log field with `event.idm.read_only_udm.principal.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.file.mime_type`: Newly mapped `src_file_type` raw log field with `event.idm.read_only_udm.principal.file.mime_type` UDM field.  
\- `event.idm.read_only_udm.principal.file.sha256`: Newly mapped `src_sha256` raw log field with `event.idm.read_only_udm.principal.file.sha256` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.sha256`: Newly mapped `x_rs_file_sha256` raw log field with `event.idm.read_only_udm.principal.process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.target.file.names`: Newly mapped `destination_file_name` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `x_cs_timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.location.city`: Newly mapped `dst_location` raw log field with `event.idm.read_only_udm.target.location.city` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `assignee` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `connection_id` and `network_session_id` raw log fields with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `policy` and `policy_name` raw log fields with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `action_data` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.principal.platform`: If `x_c_os` or `os` contains `Windows`, `MAC`, or `LINUX` (case-insensitive), updated the value of `event.idm.read_only_udm.principal.platform` to `WINDOWS`, `MAC`, or `LINUX` respectively.  
\- `event.idm.read_only_udm.security_result.action`: If `action_data` is `allow`, updated the value of `event.idm.read_only_udm.security_result.action` to `ALLOW`.  
\- `event.idm.read_only_udm.security_result.action`: If `action_data` is one of `block`, `restrictToView`, `disableDownload`, `restrictAccess`, or `delete`, updated the value of `event.idm.read_only_udm.security_result.action` to `BLOCK`.  
\- `event.idm.read_only_udm.security_result.action`: If `action_data` is one of `alert`, `bypass`, `quarantine`, `legalHold`, `useralert`, `Detection`, or `expireLink`, updated the value of `event.idm.read_only_udm.security_result.action` to `QUARANTINE`.  
\- `event.idm.read_only_udm.security_result.severity`: If `severity` contains `high`, updated the value of `event.idm.read_only_udm.security_result.severity` to `HIGH`.  
\- `event.idm.read_only_udm.security_result.severity`: If `severity` contains `medium`, updated the value of `event.idm.read_only_udm.security_result.severity` to `MEDIUM`.  
\- `event.idm.read_only_udm.security_result.severity`: If `severity` contains `low`, updated the value of `event.idm.read_only_udm.security_result.severity` to `LOW`.  
\- `event.idm.read_only_udm.security_result.severity`: If `severity` contains `critical`, updated the value of `event.idm.read_only_udm.security_result.severity` to `CRITICAL`.  
\- `event.idm.read_only_udm.security_result.severity`: If `severity` contains `info`, updated the value of `event.idm.read_only_udm.security_result.severity` to `INFORMATIONAL`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column2` (key: `access_method`), `column5` (key: `activity`), `column6` (key: `alert`), `column7` (key: `alert_name`), `column8` (key: `alert_type`), `column10` (key: `app-gdpr-level`), `column11` (key: `app_session_id`), `column12` (key: `appact`), `column14` (key: `appsuite`), `column15` (key: `audit_type`), `column18` (key: `browser_session_id`), `column24` (key: `cloud_provider`), `column26` (key: `conn_duration`), `column27` (key: `conn_endtime`), `column28` (key: `conn_starttime`), `column30` (key: `connection_type`), `column32` (key: `destination_file_directory`), `column35` (key: `device`), `column36` (key: `device_classification`), `column37` (key: `dinsid`), `column76` (key: `filepath`), `column82` (key: `instance`), `column83` (key: `instance_id`), `column137` (key: `shared_with`), `column138` (key: `site`), `column139` (key: `smtp_to`), `column140` (key: `spet`), `column141` (key: `spst`), `column109` (key: `page`), `column196` (key: `violation`), `column197` (key: `account_id`), `column198` (key: `account_name`), `column199` (key: `acked`), `column200` (key: `alert_id`), `column201` (key: `alert_source`), `column202` (key: `breach_date`), `column203` (key: `breach_id`), `column204` (key: `breach_score`), `column205` (key: `detection_engine`), `column206` (key: `dlp_fingerprint_match`), `column207` (key: `dlp_rule_score`), `column208` (key: `email_title`), `column209` (key: `event_uuid`), `column210` (key: `file_category`), `column211` (key: `file_cls_encrypted`), `column212` (key: `file_exposure`), `column213` (key: `file_id`), `column214` (key: `filename`), `column215` (key: `iaas_remediated`), `column216` (key: `iaas_remediated_by`), `column217` (key: `iaas_remediated_on`), `column218` (key: `iaas_remediation_action`), `column219` (key: `instance_name`), `column220` (key: `loc`), `column221` (key: `local_md5`), `column222` (key: `local_sha1`), `column223` (key: `local_sha256`), `column224` (key: `mal_id`), `column225` (key: `mal_type`), `column226` (key: `malware_id`), `column227` (key: `malware_severity`), `column228` (key: `malware_type`), `column229` (key: `message_id`), `column230` (key: `modified_date`), `column231` (key: `pop_id`), `column232` (key: `redirect_url`), `column233` (key: `region_id`), `column234` (key: `region_name`), `column235` (key: `resource_category`), `column236` (key: `resource_group`), `column237` (key: `risk_level_id`), `column238` (key: `sa_profile_name`), `column239` (key: `sa_rule_name`), `column240` (key: `sa_rule_severity`), `column241` (key: `sender`), `column242` (key: `severity_id`), `column243` (key: `severity_level`), `column244` (key: `shared_credential_user`), `column245` (key: `shared_domains`), `column246` (key: `sharedType`), `column247` (key: `smtp_status`), `column248` (key: `subject`), `column249` (key: `suppression_count`), `column250` (key: `tss_license`), `column251` (key: `two_factor_auth`), `column252` (key: `usergroup`), `column253` (key: `watchlist_name`), `column254` (key: `web_url`), `column13` (key: `appcategory`), `column31` (key: `custom_attr`), `column86` (key: `location`), `column90` (key: `md5`), `column91` (key: `mime_type`), and `column113` (key: `policy_action`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-04-20 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.ip`: Removed mapping of `column57 (x-cs-dst-ip)` from `event.idm.read_only_udm.intermediary.ip` UDM field as the field represents the destination IP.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Mapped `column57 (x-cs-dst-ip)` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm..read_only_udm.intermediary.port`: Removed mapping of `column58 (x-cs-dst-port)` from `event.idm.read_only_udm.intermediary.port` UDM field as the field represents the destination port.  
\- `event.idm.read_only_udm.target.port`: Mapped `column58 (x-cs-dst-port)` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `column66 (x-cs-src-ip)` from `event.idm.read_only_udm.additional.fields` UDM field to introduce more specific UDM mapping for the raw log field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Mapped `column66 (x-cs-src-ip)` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.nat_ip`: Removed mapping of `column67 (x-cs-src-ip-egress)` from `event.idm.read_only_udm.principal.nat_ip` UDM field as the field represents the public IP address that is used by client device.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`:Mapped `column67 (x-cs-src-ip-egress)` from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.nat_port`: Removed mapping of `column68 (x-cs-src-port)` from `event.idm.read_only_udm.principal.nat_port` UDM field as the field represents the source port of the client.  
\- `event.idm.read_only_udm.principal.port`: Mapped `column68 (x-cs-src-port)` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.md5`: Removed mapping of `column108 (x-rs-file-md5)` from `event.idm.read_only_udm.principal.process.file.md5` UDM field as the field represents the MD5 Hash of the object transferred to/from the remote server.  
\- `event.idm.read_only_udm.principal.file.md5`: Mapped `column108 (x-rs-file-md5)` raw log field with `event.idm.read_only_udm.principal.file.md5` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `column6 (cs-host)` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column11 (cs-uri-query)`, `column34 (x-category)`, `column35 (x-category-id)`, `column36 (x-client-ssl-err)`, `column37 (x-cs-access-method)`, `column40 (x-cs-app-category)`, `column46 (x-cs-app-instance-tag)`, `column47 (x-cs-app-object-id)`, `column50 (x-cs-app-suite)`, `column52 (x-cs-app-to-user)`, `column53 (x-cs-connect-host)`, `column54 (x-cs-connect-port)`, `column56 (x-cs-domain-fronted-sni)`, `column71 (x-cs-ssl-engine-action-reason)`, `column78 (x-cs-tunnel-id)`, `column79 (x-cs-uri-path)`, `column89 (x-policy-justification-reason)`, `column90 (x-policy-justification-type)`, `column107 (x-rs-file-language)`, `column119 (x-s-zipcode)`, `column120 (x-sc-notification-name)`, `column121 (x-server-ssl-err)`, `column124 (x-sr-headers-name)`, `column125 (x-sr-headers-value)` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `column14 (cs-username)` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field if it is not a valid email address.  
\- `event.idm.read_only_udm.principal.browser.browser_type`: Newly mapped `column23 (x-c-browser)` raw log field with `event.idm.read_only_udm.principal.browser.browser_type` UDM field.  
\- `event.idm.read_only_udm.principal.browser.browser_version`: Newly mapped `column24 (x-c-browser-version)` raw log field with `event.idm.read_only_udm.principal.browser.browser_version` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `column28 (x-c-local-time)`, `column84 (x-other-category-id)`, `column88 (x-policy-dst-ip)`, `column92 (x-policy-src-ip)`, `column123 (x-sr-dst-port)`, `column144 (x-ssl-policy-src-ip)` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.platform`: Newly mapped `column31 (x-c-os)` raw log field with `event.idm.read_only_udm.principal.platform` UDM field.  
\- Changed the key name of mapping of `column33 (x-c-zipcode)` to `event.idm.read_only_udm.additional.fields` from `Postal Code` to `x-c-zipcode`.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `column38 (x-cs-app)` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_address`: Newly mapped `column43 (x-cs-app-from-user)` raw log field with `event.idm.read_only_udm.principal.user.email_address` UDM field if it is a valid email address.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `column43 (x-cs-app-from-user)` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field if it is not a valid email address.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `column44 (x-cs-app-instance-id)` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `column45 (x-cs-app-instance-name)` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `column55 (x-cs-connect-user-agent)` raw log field with `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `column60 (x-cs-ip-connect-xff)`, `column61 (x-cs-ip-xff)`, `column81 (x-cs-userip)` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `column63 (x-cs-session-id)` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.network.tls.cipher`: Newly mapped `column69 (x-cs-ssl-cipher)` raw log field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `column75 (x-cs-ssl-version)` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- `event.idm.read_only_udm.principal.file.sha256`: Newly mapped `column109 (x-rs-file-sha256)` raw log field with `event.idm.read_only_udm.principal.file.sha256` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `column126 (x-sr-src-ip)` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.port`: Newly mapped `column127 (x-sr-src-port)` raw log field with `event.idm.read_only_udm.intermediary.port` UDM field.   
2026-04-13 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.action` and `event.idm.read_only_udm.security_result.action_details`: Removed mapping of `column70 (x-cs-ssl-engine-action)` from `event.idm.read_only_udm.security_result.action` and `event.idm.read_only_udm.security_result.action_details` UDM field to introduce more accurate UDM mappings for the raw log field.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `column70 (x-cs-ssl-engine-action)` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Corrected parsing logic of `column8` raw log field to prevent IP addresses from referral URLs from being incorrectly mapped as target IP.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column19 (sc-content-type)`, `column26 (x-c-device)`, `column39 (x-cs-app-activity)`, `column41 (x-cs-app-cci)`, `column42 (x-cs-app-ccl)`, `column51 (x-cs-app-tags)`, `column64 (x-cs-site)`, `column48 (x-cs-app-object-name)`, `column49 (x-cs-app-object-type)`, `column106 (x-rs-file-category)`, `column111 (x-rs-file-type)`, `column9 (cs-uri)`, `column4 (cs-content-type)` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `column38 (x-cs-app)` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.md5`: Newly mapped `column108 (x-rs-file-md5)` raw log field with `event.idm.read_only_udm.principal.process.file.md5` UDM field.  
\- `event.idm.read_only_udm.principal.file.size`: Newly mapped `column110 (x-rs-file-size)` raw log field with `event.idm.read_only_udm.principal.file.size` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `column85 (x-policy-action)` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `column20 (http_response_code)` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.   
2026-04-01 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_log_id`: Removed mapping of `column1 (bytes)` from `event.idm.read_only_udm.metadata.product_log_id` UDM field because the field represents sum of client bytes plus server bytes.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `column1 (bytes)` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Removed mapping of `column3 (cs-bytes)` from `event.idm.read_only_udm.principal.port` UDM field because the field represents bytes received from the client.  
\- `event.idm.read_only_udm.network.sent_bytes`: Mapped `column3 (cs-bytes)` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Removed mapping of `column18 (sc-bytes)` from `event.idm.read_only_udm.network.sent_bytes` UDM field because the field represents bytes received from the server.  
\- `event.idm.read_only_udm.network.received_bytes`: Mapped `column18 (sc-bytes)` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Removed mapping of `column22 (time-taken)` from `event.idm.read_only_udm.network.received_bytes` UDM field because the field represents delta between the request processing started and the full response was received.  
\- `event.idm.read_only_udm.network.session_duration`: Mapped `column22 (time-taken)` raw log field with `event.idm.read_only_udm.network.session_duration` UDM field.  
\- `event.idm.read_only_udm.target.location.region_latitude`: Removed mapping of `column27 (x-c-latitude)` from `event.idm.read_only_udm.target.location.region_latitude` UDM field because the field represents latitude of the client.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.latitude`: Mapped `column27 (x-c-latitude)` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.latitude` UDM field.  
\- `event.idm.read_only_udm.target.location.region_longitude`: Removed mapping of `column30 (x-c-longitude)` from `event.idm.read_only_udm.target.location.region_longitude` UDM field because the field represents longitude of the client.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.longitude`: Mapped `column30 (x-c-longitude)` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.longitude` UDM field.  
\- `event.idm.read_only_udm.target.location.state`: Removed mapping of `column32 (x-c-region)` from `event.idm.read_only_udm.target.location.state` UDM field because the field represents state of the client.  
\- `event.idm.read_only_udm.principal.location.state`: Mapped `column32 (x-c-region)` raw log field with `event.idm.read_only_udm.principal.location.state` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Removed mapping of `column57 (x-cs-dst-ip)` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field because the field represents the destination IP of the client to proxy session.  
\- `event.idm.read_only_udm.intermediary.ip`: Mapped `column57 (x-cs-dst-ip)` raw log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.file.md5`: Removed mapping of `column74 (x-cs-ssl-ja3)` from `event.idm.read_only_udm.target.file.md5` UDM field because the field represents the fingerprints the way the Client communicates over TLS.  
\- `event.idm.read_only_udm.network.tls.client.ja3`: Mapped `column74 (x-cs-ssl-ja3)` raw log field with `event.idm.read_only_udm.network.tls.client.ja3` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.latitude`: Removed mapping of `column115 (x-s-latitude)` from `event.idm.read_only_udm.principal.location.region_coordinates.latitude` UDM field because the field represents latitude of the server.  
\- `event.idm.read_only_udm.target.location.region_coordinates.latitude`: Mapped `column115 (x-s-latitude)` raw log field with `event.idm.read_only_udm.target.location.region_coordinates.latitude` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.longitude`: Removed mapping of `column117 (x-s-longitude)` from `event.idm.read_only_udm.principal.location.region_coordinates.longitude` UDM field because the field represents longitude of the server.  
\- `event.idm.read_only_udm.target.location.region_coordinates.longitude`: Mapped `column117 (x-s-longitude)` raw log field with `event.idm.read_only_udm.target.location.region_coordinates.longitude` UDM field.  
\- `event.idm.read_only_udm.principal.location.state`: Removed mapping of `column118 (x-s-region)` from `event.idm.read_only_udm.principal.location.state` UDM field as the field represents state of the server.  
\- `event.idm.read_only_udm.target.location.state`: Mapped `column118 (x-s-region)` raw log field with `event.idm.read_only_udm.target.location.state` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `column7 (method)` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `column12 (app_protocol)` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `column13 (network_http_user_agent)` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `column17 (server_ip)` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.port`: Newly mapped `column58 (intermediary_port)` raw log field with `event.idm.read_only_udm.intermediary.port` UDM field.  
\- `event.idm.read_only_udm.network.tls.client.server_name`: Newly mapped `column65 (x-cs-sni)` raw log field with `event.idm.read_only_udm.network.tls.client.server_name` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `column70 (engine_action)` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `column70 (engine_action)` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `column76 (generated_timestamp)` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `column80 (x-cs-url)` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `column83 (other_categories)` and `column139 (x-ssl-policy-categories)` raw log fields with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `column85 (x-policy-action)` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `column91 (x-policy-name)` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.network.tls.server.certificate.issuer`: Newly mapped `column96 (x-r-cert-issuer-cn)` raw log field with `event.idm.read_only_udm.network.tls.server.certificate.issuer` UDM field.  
\- `event.idm.read_only_udm.network.tls.server.certificate.subject`: Newly mapped `column102 (x-r-cert-subject-cn)` raw log field with `event.idm.read_only_udm.network.tls.server.certificate.subject` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `column112 (x-s-country)` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.network.tls.server.ja3s`: Newly mapped `column133 (x-sr-ssl-ja3s)` raw log field with `event.idm.read_only_udm.network.tls.server.ja3s` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `column136 (x-ssl-bypass)` and `column143 (x-ssl-policy-name)` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `column137 (x-ssl-bypass-reason)` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `column146 (x-type)` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column62 (x-cs-page-id)`, `column63 (x-cs-session-id)`, `column66 (x-cs-src-ip)`, `column72 (x-cs-ssl-fronting-error)`, `column73 (x-cs-ssl-handshake-error)`, `column77 (x-cs-traffic-type)`, `column82 (x-error)`, `column86 (x-policy-dst-host)`, `column87 (x-policy-dst-host-source)`, `column94 (x-r-cert-expired)`, `column95 (x-r-cert-incomplete-chain)`, `column97 (x-r-cert-mismatch)`, `column98 (x-r-cert-revocation-check)`, `column99 (x-r-cert-revoked)`, `column100 (x-r-cert-self-signed)`, `column103 (x-r-cert-untrusted-root)`, `column104 (x-r-cert-valid)`, `column105 (x-request-id)`, `column113 (x-s-custom-signing-ca-error)`, `column114 (x-s-dp-name)`, `column122 (x-sr-dst-ip)`, `column128 (x-sr-ssl-cipher)`, `column129 (x-sr-ssl-client-certificate-error)`, `column130 (x-sr-ssl-engine-action)`, `column131 (x-sr-ssl-engine-action-reason)`, `column132 (x-sr-ssl-handshake-error)`, `column134 (x-sr-ssl-malformed-ssl)`, `column135 (x-sr-ssl-version)`, `column138 (x-ssl-policy-action)`, `column140 (x-ssl-policy-dst-host)`, `column141 (x-ssl-policy-dst-host-source)`, `column142 (x-ssl-policy-dst-ip)` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `column8 (cs-referer)` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `column16 (http_response_code)` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.network.tls.server.certificate.not_before`: Newly mapped `column101 (x-r-cert-startdate)` raw log field with `event.idm.read_only_udm.network.tls.server.certificate.not_before` UDM field.  
\- `event.idm.read_only_udm.network.tls.server.certificate.not_after`: Newly mapped `column93 (x-r-cert-enddate)` raw log field with `event.idm.read_only_udm.network.tls.server.certificate.not_after` UDM field.   
2026-03-09 |  Enhancement:  
\- Added support for new format of CSV logs.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `column2` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `cs_dns` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `cs_host` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `cs_method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `cs_referer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `cs_uri_scheme` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `cs-username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `sc-status` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `rs-status` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `s-ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `sc-bytes` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `x-c-country` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `x-c-location` raw log field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.principal.platform`: If `x-c-os` is `Windows`, updated the value of `event.idm.read_only_udm.principal.platform` to `WINDOWS`.  
\- `event.idm.read_only_udm.principal.platform`: If `x-c-os` is `MAC`, updated the value of `event.idm.read_only_udm.principal.platform` to `MAC`.  
\- `event.idm.read_only_udm.principal.platform`: If `x-c-os` is `LINUX`, updated the value of `event.idm.read_only_udm.principal.platform` to `LINUX`.  
\- `event.idm.read_only_udm.principal.location.state`: Newly mapped `x-c-region` raw log field with `event.idm.read_only_udm.principal.location.state` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `column49` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `x_cs_dst_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `x-cs-session-id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `column56` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `column57` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `x-cs-src-port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.network.tls.client.ja3`: Newly mapped `x-cs-ssl-ja3` raw log field with `event.idm.read_only_udm.network.tls.client.ja3` UDM field.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `x-cs-ssl-version` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `column71` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `x-policy-action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: If `x-policy-action` is `ALLOW`, updated the value of `event.idm.read_only_udm.security_result.action` to `ALLOW`.  
\- `event.idm.read_only_udm.security_result.action`: If `x-policy-action` is `BLOCK`, updated the value of `event.idm.read_only_udm.security_result.action` to `BLOCK`.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `x-policy-name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `x-ssl-policy-name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.network.tls.server.certificate.subject`: Newly mapped `x-r-cert-subject-cn` raw log field with `event.idm.read_only_udm.network.tls.server.certificate.subject` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.sha256`: Newly mapped `x-rs-file-sha256` raw log field with `event.idm.read_only_udm.principal.process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.principal.file.size`: Newly mapped `x-rs-file-size` raw log field with `event.idm.read_only_udm.principal.file.size` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `x-s-country` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.location.name`: Newly mapped `x-s-location` raw log field with `event.idm.read_only_udm.target.location.name` UDM field.  
\- `event.idm.read_only_udm.network.tls.server.ja3s`: Newly mapped `x-sr-ssl-ja3s` raw log field with `event.idm.read_only_udm.network.tls.server.ja3s` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `x_cs_connect_host` (key: `x_cs_connect_host`), `x_cs_connect_port` (key: `x_cs_connect_port`), `x_cs_connect_user_agent` (key: `x_cs_connect_user_agent`), `x_cs_ip_xff` (key: `x_cs_ip_xff`), `x-policy-justification-type` (key: `x-policy-justification-type`), `x-sr-src-port` (key: `x-sr-src-port`), `cs-uri-port` (key: `cs-uri-port`), `cs_uri` (key: `cs_uri`), `cs_uri_query` (key: `cs_uri_query`), `time_taken` (key: `time_taken`), `x-category` (key: `x-category`), `x-cs-access-method` (key: `x-cs-access-method`), `x-cs-app` (key: `x-cs-app`), `x-cs-app-activity` (key: `x-cs-app-activity`), `x-cs-app-category` (key: `x-cs-app-category`), `x-cs-app-cci` (key: `x-cs-app-cci`), `x-cs-app-ccl` (key: `x-cs-app-ccl`), `x-cs-page-id` (key: `x-cs-page-id`), `x-cs-site` (key: `x-cs-site`), `x-cs-traffic-type` (key: `x-cs-traffic-type`), `x-cs-uri-path` (key: `x-cs-uri-path`), `x-error` (key: `x-error`), `x-request-id` (key: `x-request-id`), `x-s-dp-name` (key: `x-s-dp-name`), `x-sc-notification-name` (key: `x-sc-notification-name`), `x-transaction-id` (key: `x-transaction-id`), `x-type` (key: `x-type`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `x-cs-http-version` (key: `x-cs-http-version`), `x-cs-ssl-engine-action` (key: `x-cs-ssl-engine-action`), `x-cs-ssl-engine-action-reason` (key: `x-cs-ssl-engine-action-reason`), `x-cs-ssl-fronting-error` (key: `x-cs-ssl-fronting-error`), `x-cs-ssl-handshake-error` (key: `x-cs-ssl-handshake-error`), `x-cs-userip` (key: `x-cs-userip`), `x-policy-dst-host` (key: `x-policy-dst-host`), `x-policy-dst-host-source` (key: `x-policy-dst-host-source`), `x-policy-dst-ip` (key: `x-policy-dst-ip`), `x-policy-src-ip` (key: `x-policy-src-ip`), `x-sr-ssl-engine-action` (key: `x-sr-ssl-engine-action`), `x-sr-ssl-engine-action-reason` (key: `x-sr-ssl-engine-action-reason`), `x-ssl-policy-action` (key: `x-ssl-policy-action`), `x-ssl-policy-dst-host` (key: `x-ssl-policy-dst-host`), `x-ssl-policy-dst-host-source` (key: `x-ssl-policy-dst-host-source`), `x-ssl-policy-dst-ip` (key: `x-ssl-policy-dst-ip`), `x-ssl-policy-src-ip` (key: `x-ssl-policy-src-ip`), `x-ssl-bypass-reason` (key: `SSL BYPASS REASON`) raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added a condition to drop logs which are CSV headers.   
2026-01-12 |  Enhancement:  
\- Added grok pattern to parse unparsed logs.  
\- The conditional logic for mapping event.idm.read_only_udm.target.hostname and event.idm.read_only_udm.target.asset.hostname was updated. The mapping from cs_dns now occurs only if its length is 255 characters.  
\- If the length of the cs_host raw log field is 255 characters or more, then it will map to mapped to event.idm.read_only_udm.additional.fields instead of event.idm.read_only_udm.target.hostname.   
2025-12-19 |  Enhancement:  
\- Added a grok pattern to parse unparsed log.  
\- event.idm.read_only_udm.network.sent_bytes: Changed mapping for event.idm.read_only_udm.network.sent_bytes from %{sent_bytes} to the validated %{sent_bytes_check} field.  
\- event.idm.read_only_udm.principal.nat_port: Changed mapping for event.idm.read_only_udm.principal.nat_port from %{p_port} to the validated %{p_port_check} field.  
\- event.idm.read_only_udm.principal.file.size: Changed mapping for event.idm.read_only_udm.principal.file.size from %{x_rs_file_size} to the validated %{x_rs_file_size_int} field.  
\- event.idm.read_only_udm.target.ip, event.idm.read_only_udm.target.asset.ip: Changed mapping to use the validated valid_ip field which is derived from x_cs_dst_ip.  
\- Added conditional check for c_ip, x_cs_src_ip: Added logic to use x_cs_src_ip as a fallback for c_ip, which is used to populate event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.target.ip.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `x_policy_name`, `bytes`, `x_s_dp_name` and `rs_status` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-12-11 |  Enhancement:  
\- Added CSV as a supported format.   
2025-11-21 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `postal_code`, `internal_category`, `accessMethod`, `postal_code_num` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `log_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.network.application_protocol_version: Newly mapped `http_version` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `int2`, `sc-bytes`, `server_bytes`, `bytes_received` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `sent_bytes`, `int3`, `cs-bytes`, `client_bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.network.session_duration.seconds: Newly mapped `int1` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `prin_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `prin_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.location.city: Newly mapped `city` raw log field with `event.idm.read_only_udm.principal.location.city` UDM field.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `location` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.principal.location.region_coordinates.latitude: Newly mapped `src_latitude` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.latitude` UDM field.  
\- event.idm.read_only_udm.principal.location.region_coordinates.longitude: Newly mapped `src_longitude` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.longitude` UDM field.  
\- event.idm.read_only_udm.principal.location.region_coordinates.latitude: Newly mapped `latitude_region` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.latitude` UDM field.  
\- event.idm.read_only_udm.principal.location.region_coordinates.longitude: Newly mapped `longitude_region` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.longitude` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `p_application` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.principal.location.state: Newly mapped `state` raw log field with `event.idm.read_only_udm.principal.location.state` UDM field.  
\- event.idm.read_only_udm.target.location.state: Newly mapped `state_location` raw log field with `event.idm.read_only_udm.target.location.state` UDM field.  
\- event.idm.read_only_udm.principal.nat_ip: Newly mapped `t_ip` raw log field with `event.idm.read_only_udm.principal.nat_ip` UDM field.  
\- event.idm.read_only_udm.principal.nat_port: Newly mapped `p_port` raw log field with `event.idm.read_only_udm.principal.nat_port` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `prin_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.principal.process.file.sha256: Newly mapped `x-rs-file-sha256` raw log field with `event.idm.read_only_udm.principal.process.file.sha256` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `target_host` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `target_ip`, `tar_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `target_ip`, `tar_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `target_host` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.location.city: Newly mapped `location_name` raw log field with `event.idm.read_only_udm.target.location.city` UDM field.  
\- event.idm.read_only_udm.target.location.region_coordinates.latitude: Newly mapped `dst_latitude` raw log field with `event.idm.read_only_udm.target.location.region_coordinates.latitude` UDM field.  
\- event.idm.read_only_udm.target.location.region_coordinates.longitude: Newly mapped `dst_longitude` raw log field with `event.idm.read_only_udm.target.location.region_coordinates.longitude` UDM field.  
\- event.idm.read_only_udm.target.location.region_latitude: Newly mapped `latitude` raw log field with `event.idm.read_only_udm.target.location.region_latitude` UDM field.  
\- event.idm.read_only_udm.target.location.region_longitude: Newly mapped `longitude` raw log field with `event.idm.read_only_udm.target.location.region_longitude` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `network_id` raw log field to `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `summary_res` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `target_port`, `dstport` raw log field with `event.idm.read_only_udm.target.port` UDM field.   
2025-09-29 |  Enhancement:  
\- Added grok patterns to parse unparsed logs.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped x_c_nsclient_version field with event.idm.read_only_udm.metadata.product_version UDM field.  
\- event.idm.read_only_udm.principal.platform_version: Newly mapped x_c_os_version field with event.idm.read_only_udm.principal.platform_version UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped x_cs_process field with event.idm.read_only_udm.principal.process.file.full_path UDM field.  
\- event.idm.read_only_udm.principal.process.parent_process.file.full_path: Newly mapped x_cs_parent_process field with event.idm.read_only_udm.principal.process.parent_process.file.full_path UDM field.  
\- event.idm.read_only_udm.principal.platform_version: Newly mapped os_version field with event.idm.read_only_udm.principal.platform_version UDM field.  
\- event.idm.read_only_udm.principal.process.parent_process.pid: Newly mapped x_cs_ppid field with event.idm.read_only_udm.principal.process.parent_process.pid UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped x_cs_pid field with event.idm.read_only_udm.principal.process.pid UDM field.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped x_c_device_uid field with a device_uid: prefix and event.idm.read_only_udm.principal.asset.asset_id UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped rs_bytes, x_action, x_action_reason, x_c_authn_user, x_c_authn_source, x_c_authn_surrogate, x_c_authn_surrogate_status, x_c_authz_groups, x_c_authz_ou, x_cs_xau, x_cs_connect_xau, x_c_user_confidence_index, x_c_hostname, x_c_os_family, x_c_nsclient_client_profile, x_c_nsclient_steering_profile, x_c_device_classification, x_cs_nsclient_tunnel_type, x_tp_result, x_tp_engine, x_tp_malware_name, x_tp_severity, x_sr_forward_dest, x_ssl_policy_issuer, x_eip_policy_name, x_eip_policy_footprint, x_policy_categories, x_c_timezone, and x_support field with event.idm.read_only_udm.additional.fields UDM field.   
2025-08-13 |  Enhancement:  
\- Added GROK pattern to parse unparsed logs.  
\- Modified mapping of `src_region` from using rename and now using replace to map the src_region raw log field.  
\- Modified mapping of `src_location` from using rename and now using replace to map the src_location raw log field.  
\- Modified mapping of request_method from using rename and now using replace to map the request_method raw log field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp` raw log field with event.idm.read_only_udm.metadata.event_timestamp UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `src_ip_1` raw log field to event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip.  
\- event.idm.read_only_udm.principal.port: Newly mapped `src_port_1` raw log field to event.idm.read_only_udm.principal.port.  
\- event.idm.read_only_udm.principal.port: Newly mapped `source_port` raw log field to event.idm.read_only_udm.principal.port.  
\- event.idm.read_only_udm.target.ip: Newly mapped `dst_ip_1` raw log field to event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip.  
\- event.idm.read_only_udm.target.port: Newly mapped `dst_port_1` raw log field to event.idm.read_only_udm.target.port.  
\- event.idm.read_only_udm.target.port: Newly mapped `server_port` raw log field to event.idm.read_only_udm.target.port.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `origin_ip` raw log field to event.idm.read_only_udm.intermediary.ip and event.idm.read_only_udm.intermediary.asset.ip.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `internal_ip` raw log field to event.idm.read_only_udm.intermediary.ip and event.idm.read_only_udm.intermediary.asset.ip.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `user_email` raw log field to event.idm.read_only_udm.principal.user.email_addresses.  
\- event.idm.read_only_udm.principal.application: Newly mapped `client_type` raw log field to event.idm.read_only_udm.principal.application.  
\- event.idm.read_only_udm.principal.location.region_coordinates.latitude: Newly mapped `latitude_1` raw log field to event.idm.read_only_udm.principal.location.region_coordinates.latitude.  
\- event.idm.read_only_udm.principal.location.region_coordinates.latitude: Newly mapped `latitude` raw log field to event.idm.read_only_udm.principal.location.region_coordinates.latitude.  
\- event.idm.read_only_udm.principal.location.region_coordinates.longitude: Newly mapped `longitude_1` raw log field to event.idm.read_only_udm.principal.location.region_coordinates.longitude.  
\- event.idm.read_only_udm.principal.location.region_coordinates.longitude: Newly mapped `longitude` raw log field to event.idm.read_only_udm.principal.location.region_coordinates.longitude.  
\- event.idm.read_only_udm.principal.location.city: Newly mapped `city` raw log field to event.idm.read_only_udm.principal.location.city.  
\- event.idm.read_only_udm.principal.location.state: Newly mapped `state` raw log field to event.idm.read_only_udm.principal.location.state.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `http_transaction` raw log field to event.idm.read_only_udm.network.http.method.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `ssl_error` raw log field to event.idm.read_only_udm.security_result.summary.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `id` raw log field to event.idm.read_only_udm.metadata.product_log_id.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `status` raw log field to event.idm.read_only_udm.security_result.action.  
\- event.idm.read_only_udm.network.tls.version: Newly mapped `TLS_version` raw log field to event.idm.read_only_udm.network.tls.version.  
\- event.idm.read_only_udm.network.tls.cipher: Newly mapped `cipher` raw log field to event.idm.read_only_udm.network.tls.cipher.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `id1`, `id2`, `id3`, `id4`, `id5`, `error_message`, `Sni`, `decrypt`, `server_name`, raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `category`, `category1`, `category2`, `category3`, `category4`, `category5`,`categories`, `codes`, `status1`, `status2`, `status3`, `status4`, `server_name2`, `client_ssl` raw log field to event.idm.read_only_udm.security_result.detection_fields.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `zip_code` raw log field to event.idm.read_only_udm.principal.resource.attribute.labels.   
2025-07-23 |  Enhancement:  
\- Added grok patterns to parse unparsed logs.  
\- Consolidated all mapping for event.idm.read_only_udm.additional.fields, event.idm.read_only_udm.security_result.detection_fields, and event.idm.read_only_udm.principal.resource.attribute.labels in for loop.   
2025-05-22 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `_id` and `product_id` raw log fields with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `referer` and `cs_referer` raw log fields with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `organization_unit` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user_id` and `cs_username` raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `useragent` and `cs_user_agent` raw log fields with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `useragent` and `cs_user_agent` raw log fields with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `session_duration` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `os_version` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.principal.platform`: Newly mapped `os` and `x_c_os` raw log fields with `event.idm.read_only_udm.principal.platform` UDM field.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `ur_normalized` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `browser_session_id`, `network_session_id` and `x_cs_session_id` raw log fields with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_id`: Newly mapped `malware_id` raw log field with `event.idm.read_only_udm..threat_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `src_location`, `src_zipcode` and `src_geoip_src` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `ip_protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.principal.file.size`: Newly mapped `file_size` and `x_rs_file_size` raw log fields with `event.idm.read_only_udm.principal.file.size` UDM field.  
\- `event.idm.read_only_udm.target.file.mime_type`: Newly mapped `file_type` raw log field with `event.idm.read_only_udm.target.file.mime_type` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `srcip`, `s_ip`, `c_ip` and `x_cs_src_ip` raw log fields with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `srcip`, `s_ip`, `c_ip` and `x_cs_src_ip` raw log fields with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `srcport` and `x_cs_src_port` raw log fields with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.md5`: Newly mapped `file_md5` and `x_rs_file_md5` raw log fields with `event.idm.read_only_udm.principal.process.file.md5` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `computer_name` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `computer_name` and `cs_dns` and `cs_host` raw log fields with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.resource.type`: Newly mapped `device` raw log field with `event.idm.read_only_udm.principal.resource.type` UDM field.  
\- `event.idm.read_only_udm.principal.resource.resource_subtype`: Newly mapped `device` raw log field with `event.idm.read_only_udm.principal.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.principal.resource.id`: Newly mapped `device_sn` raw log field with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `src_region` and `x_c_location` raw log fields with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `src_country` and `x_c_country` raw log fields with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.latitude`: Newly mapped `src_latitude` and `x_c_latitude` raw log fields with `event.idm.read_only_udm.principal.location.region_coordinates.latitude` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.longitude`: Newly mapped `src_longitude` and `x_c_longitude` raw log fields with `event.idm.read_only_udm.principal.location.region_coordinates.longitude` UDM field.  
\- `event.idm.read_only_udm.target.location.region_coordinates.latitude`: Newly mapped `dst_latitude` and `x_s_latitude` raw log fields with `event.idm.read_only_udm.target.location.region_coordinates.latitude` UDM field.  
\- `event.idm.read_only_udm.target.location.region_coordinates.longitude`: Newly mapped `dst_longitude` and `x_s_longitude` raw log fields with `event.idm.read_only_udm.target.location.region_coordinates.longitude` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `destination_file_path` and `dlp_file` raw log fields with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.file.sha256`: Newly mapped `sha256` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- `event.idm.read_only_udm.target.file.md5`: Newly mapped `md5` raw log field with `event.idm.read_only_udm.target.file.md5` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `dst_country` and `x_s_country` raw log fields with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.location.state`: Newly mapped `x_s_region` raw log field with `event.idm.read_only_udm.target.location.state` UDM field.  
\- `event.idm.read_only_udm.target.location.name`: Newly mapped `dst_region` and `x_s_location` raw log fields with `event.idm.read_only_udm.target.location.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `dst_zipcode` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `dsthost`, `dstip` and `x_cs_dst_ip` raw log fields with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dsthost`, `dstip` and `x_cs_dst_ip` raw log fields with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dstport` and `x_cs_dst_port` raw log fields with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `cci`, `alert_type`, `x_other_category_id`, `x_cs_userip`, `x_ssl_bypass`, `x_cs_ssl_fronting_error`, `x_cs_ssl_handshake_error`, `x_sr_ssl_handshake_error`, `x_sr_ssl_client_certificate_error`, `x_sr_ssl_malformed_ssl`, `x_s_custom_signing_ca_error`, `x_cs_ssl_engine_action`, `x_cs_ssl_engine_action_reason`, `x_sr_ssl_engine_action`, `x_sr_ssl_engine_action_reason`, `x_ssl_policy_src_ip`, `x_ssl_policy_dst_ip`, `x_ssl_policy_dst_host`, `x_ssl_policy_dst_host_source`, `x_ssl_policy_action`, `x_sr_ssl_version`, `x_sr_ssl_cipher`, `x_cs_src_ip_egress`, `x_policy_src_ip`, `x_policy_dst_ip`, `x_policy_dst_host`, `x_policy_dst_host_source`, `x_policy_justification_type`, `x_policy_justification_reason`, `x_sc_notification_name`, `x_cs_http_version`, `x_sr_dst_ip`, and `x_sr_dst_port` raw log fields with `event.idm.read_only_udm..detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.confidence_details`: Newly mapped `ccl` raw log field with `event.idm.read_only_udm..confidence_details` UDM field.  
\- `event.idm.read_only_udm.security_result.confidence`: Newly mapped `ccl` raw log field with `event.idm.read_only_udm..confidence` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_type`: Newly mapped `dlp_profile_name` raw log field with `event.idm.read_only_udm..rule_type` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `policy_name`, `dlp_fingerprint_classification`, `dlp_fingerprint_match`, `dlp_fingerprint_score`, `dlp_rule_score`, `dlp_unique_count`, `acked`, `app_session_id`, `x_type`, `x_transaction_id`, `x_client_ssl_err`, `x_cs_domain_fronted_sni`, `x_cs_tunnel_id`, `x_request_id`, `x_s_zipcode`, `x_c_zipcode`, `x_c_browser`, `x_c_browser_version`, `x_c_device`, `x_cs_site`, `x_cs_page_id`, `x_cs_traffic_type`, `x_category_id`, `x_category`, `x_r_cert_valid`, `x_r_cert_expired`, `x_r_cert_untrusted_root`, `x_r_cert_incomplete_chain`, `x_r_cert_self_signed`, `x_r_cert_revoked`, `x_rs_file_type`, `x_rs_file_category`, `x_rs_file_language`, `x_r_cert_revocation_check`, `x_cs_app_category`, `x_cs_app_cci`, `x_cs_app_ccl`, `x_cs_app_tags`, `x_cs_app_suite`, `x_cs_app_instance_id`, `x_cs_app_instance_name`, `x_cs_app_instance_tag`, `x_cs_app_activity`, `x_cs_app_from_user`, `x_cs_app_to_user`, `x_cs_app_object_type`, `x_cs_app_object_name`, `x_cs_app_object_id`, `x_cs_uri_path`, `x_r_cert_mismatch`, `x_cs_access_method`, `cs_uri`, `cs_uri_port`, `cs_uri_query`, `cs_content_type` and `sc_content_type` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `app` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.auth_details`: Newly mapped `access_method` raw log field with `event.idm.read_only_udm.extensions.auth.auth_details` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `action` and `x_policy_action` raw log fields with `event.idm.read_only_udm..action` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `alert_name` and `x_ssl_policy_name` raw log fields with `event.idm.read_only_udm..rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm..severity` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `activity` raw log field with `event.idm.read_only_udm..description` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `appcategory` and `x_ssl_policy_categories` and `x_other_category` raw log fields with `event.idm.read_only_udm..category_details` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `server_bytes` and `sc_bytes` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `client_bytes` and `cs_bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_packets`: Newly mapped `client_packets` raw log field with `event.idm.read_only_udm.network.sent_packets` UDM field.  
\- `event.idm.read_only_udm.network.received_packets`: Newly mapped `server_packets` raw log field with `event.idm.read_only_udm.network.received_packets` UDM field.   
2025-05-09 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- Added a new Grok pattern in order to parse `temp_data` raw log field.  
\- Added `null` check condition for `hostname` and `url` raw log fields.  
\- Added a new `regex` pattern for `sha256` raw log field.   
2025-03-03 |  Enhancement:  
\- Mapped `x-rs-file-md5` to `principal.process.file.md5`.  
\- Mapped `x-rs-file-size` to `principal.file.size`.   
2024-06-21 |  Enhancement:  
\- Added Grok to support a new log format.   
2024-06-04 |  Enhancement:  
\- Added Grok to handle unparsed logs.  
\- Mapped `url` to `target.url`.  
\- Mapped `appSessionId` to `network.session_id`.  
\- Mapped `page` to `network.http.referral_url`.  
\- Mapped `appcategory` to `security_result.category_details`.  
\- Mapped `clientBytes` to `network.sent_bytes`.  
\- Mapped `serverBytes` to `network.received_bytes`.  
\- Mapped `ccl` to `security_result.confidence_details`.  
\- Mapped `IncidentID`, `applicationType`, `browser`, and `cci` to `security_result.detection_fields`.   
2024-04-22 |  Enhancement:  
\- Mapped `x-cs-app-ccl`,`x-cs-app-instance-id`,`x-cs-app-tags` ,`x-cs-app-instance-name` ,`x-cs-app-instance-tag`, `x-cs-app-to-user`,`x-cs-app-object-id` and `x-cs-app-from-user` to `additional.fields`.   
2024-02-26 |  Enhancement:  
\- Changed mapping of `cs-bytes` from `network.received_bytes` to `network.sent_bytes`.  
\- Changed mapping of `sc-bytes` from `network.sent_bytes` to `network.received_bytes`.  
\- Mapped `x-cs-app-object-name` to `additional.fields`.  
\- Mapped `x-cs-app-from-user` to `principal.user.email_addresses`.   
2023-12-22 |  Enhancement:  
\- If `cs-dns` value is `null`, changed `cs-host` mapping from `principal.hostname` to `target.hostname`.  
\- Changed `cs-dns` mapping from `principal.hostname` to `target.hostname`.  
\- If `sc-status` value is `null`, mapped `rs-status` to `network.http.response_code`.  
\- Mapped `x-cs-app` to `principal.application`.  
\- Mapped `x-cs-src-ip-egress` to `principal.ip`.   
2023-12-08 |  Enhancement:  
\- Added on_error check to parse the failing logs.  
\- Set `metadata.vendor_name` to `Netskope` and `metadata.product_name` to `Netskope Webproxy`.  
\- Added conditional check for `src_region`, `src_country`, `src_location`, `dst_region`, `dst_country`, `dst_location` before mapping.   
2023-10-09 |  Enhancement:  
\- Mapped `dvchost` to `target.hostname` if `target.hostname` is not present.  
\- Added a null check prior mapping `requestClientApplication`.   
2023-09-12 |  Enhancement:  
\- Mapped `x-cs-dst-ip` to `target.ip`.  
\- Mapped `x-cs-src-ip` to `principal.ip`.  
\- Mapped `x-cs-src-port` to `principal.port`.  
\- Mapped `x-cs-dst-port` to `target.port`.  
\- Added on_error check for date filter.  
\- Added conditional checks before mapping `metadata.event_type`.   
2023-08-28 |  Enhancement:  
\- Mapped `cs-uri` to `additional.fields`.  
\- Mapped `cs-uri-port` to `additional.fields`.  
\- Mapped `x-s-zipcode` to `additional.fields`.  
\- Mapped `x-c-zipcode` to `additional.fields`.  
\- Mapped `x-cs-site` to `additional.fields`.  
\- Mapped `x-category` to `additional.fields`.  
\- Mapped `x-sr-ssl-version` to `security_result.detection_fields`.  
\- Mapped `x-sr-ssl-cipher` to `security_result.detection_fields`.  
\- Mapped `x-cs-src-ip-egress` to `security_result.detection_fields`.  
\- Mapped `x-cs-userip` to `security_result.detection_fields`.  
\- Mapped `x-cs-url` to `target.url`.  
\- Mapped `x-cs-uri-path` to `additional.fields`.  
\- Mapped `x-cs-app-cci` to `additional.fields`.  
\- Mapped `x-cs-app-object-type` to `additional.fields`.  
\- Mapped `x-rs-file-type` to `additional.fields`.  
\- Mapped `x-rs-file-category` to `additional.fields`.   
2023-08-17 |  Enhancement:  
\- Added support for new JSON type log format.   
2023-06-22 |  Enhancement:  
\- Added support for new SYSLOG+JSON type log format.   
2023-05-30 |  Enhancement:  
\- Mapped `duser` to `target.user.email_addresses`.  
\- Mapped `requestClientApplication` to `network.http.parsed_user_agent`.   
2023-02-03 |  Enhancement:  
\- Mapped `Domain` to `principal.administrative_domain`.   
2023-01-09 |  Enhancement:  
\- Added conditional checks for mapping different event_type based on required parameters present.  
\- Parsed different formats of `rt`.   
2022-04-06 |  Enhancement-Added mappings for new fields  
md5, mwDetectionEngine, mwProfile, mwType mapped to udm.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
