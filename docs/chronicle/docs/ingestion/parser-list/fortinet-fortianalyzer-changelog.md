---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortianalyzer-changelog/
title: Change log for FORTINET_FORTIANALYZER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:07.227897+00:00
---

# Change log for FORTINET_FORTIANALYZER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortianalyzer-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FORTINET_FORTIANALYZER

Date | Changes  
---|---  
2026-09-18 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `eventsubtype` from `event.idm.read_only_udm.additional.fields` UDM field in order to introduce more specific UDM mapping.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Mapped `eventsubtype` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Mapped `profile` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field when `policyname` and `catdesc` raw log fields are empty.   
2026-08-28 |  Enhancement:  
\- Modified a grok pattern to parse the raw log fields.  
\- Added a grok pattern on `msg` to extract `component`, `replaces`.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp_details` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.process.product_specific_process_id`: Newly mapped `operation_id` raw log field with `event.idm.read_only_udm.principal.process.product_specific_process_id` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `observer_application_pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `component` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `LayoutEx key re-assignments`, `originator_id`, `subsystem`, `operation_id`, `component_name`, `line_number`, `component`, `replaces` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-07-22 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.action` : Mapped `result` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.action` : Setting `event.idm.read_only_udm.security_result.action` to `BLOCK` when `status` is `failure`, `negotiate_error` or `failed`.   
2026-07-08 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.category_details`: Removed mapping of `msg` from `event.idm.read_only_udm.security_result.category_details` UDM field as it contains threat details.  
\- `event.idm.read_only_udm.security_result.threat_name`: Mapped `msg` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `attackid` from `event.idm.read_only_udm.additional.fields` UDM field as it contains threat id.  
\- `event.idm.read_only_udm.security_result.threat_id`: Mapped `attackid` raw log field with `event.idm.read_only_udm.security_result.threat_id` UDM field.  
\- `event.idm.read_only_udm.security_result.about.labels`: Removed mapping of `craction` from `event.idm.read_only_udm.security_result.about.labels` UDM field as the UDM field is deprecated.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `craction` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-06-30 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `devname` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields as it is a host generating event which is best fit to `observer`.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Removed mapping of `devname` from `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field as it is a host generating event which is best fit to `observer`.  
\- `event.idm.read_only_udm.observer.hostname` and `event.idm.read_only_udm.observer.asset.hostname`: Newly mapped `devname` raw log field with `event.idm.read_only_udm.observer.hostname` and `event.idm.read_only_udm.observer.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.user.userid`: Removed mapping of `user` from `event.idm.read_only_udm.principal.user.userid` UDM field as it is Remote peer `IP`.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Mapped `user` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields when `user` is an IP address.  
\- `event.idm.read_only_udm.target.user.userid`: Mapped `user` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field when `user` is not an IP address and `dstuser` raw log field is empty.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `user` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field when `user` is not an IP address and `dstuser` raw log field is not empty.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Removed mapping of `vd` from `event.idm.read_only_udm.principal.administrative_domain` UDM field as it is a host generating event which is best fit to `observer`.  
\- `event.idm.read_only_udm.observer.administrative_domain`: Newly mapped `vd` raw log field with `event.idm.read_only_udm.observer.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Removed mapping of `devid` from `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field as it is a host generating event which is best fit to `observer`.  
\- `event.idm.read_only_udm.observer.asset.asset_id`: Newly mapped `devid` raw log field with `event.idm.read_only_udm.observer.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Removed mapping of `locip` from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields when `dir` is `INBOUND` as it is a remote-initiated event.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `locip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields when `dir` is `INBOUND`.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Removed mapping of `remip` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields when `dir` is `INBOUND` as it is a remote-initiated event.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `remip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields when `dir` is `INBOUND`.  
\- `event.idm.read_only_udm.principal.port`: Removed mapping of `locport` from `event.idm.read_only_udm.principal.port` UDM field when `dir` is `INBOUND` as it is a remote-initiated event.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `locport` raw log field with `event.idm.read_only_udm.target.port` UDM field when `dir` is `INBOUND`.  
\- `event.idm.read_only_udm.target.port`: Removed mapping of `remport` from `event.idm.read_only_udm.target.port` UDM field when `dir` is `INBOUND` as it is a remote-initiated event.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `remport` raw log field with `event.idm.read_only_udm.principal.port` UDM field when `dir` is `INBOUND`.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Removed mapping of `outintf` from `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field when `dir` is `INBOUND` as it is a remote-initiated event.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `outintf` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field when `dir` is `INBOUND`.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Removed mapping of `srccountry` from `event.idm.read_only_udm.principal.location.country_or_region` UDM field when `dir` is `INBOUND` as it is a remote-initiated event.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `srccountry` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field when `dir` is `INBOUND`.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Removed mapping of `dstcountry` from `event.idm.read_only_udm.target.location.country_or_region` UDM field when `dir` is `INBOUND` as it is a remote-initiated event.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `dstcountry` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field when `dir` is `INBOUND`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `error_num`, `spi`, `seq` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `vpntunnel`, `fctuid`, `advpnsc` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-06-06 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `attack_name` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `poluuid`, `logver`, `profile`, `externalID`, `deviceInboundInterface`, `start`, `deviceOutboundInterface` raw log fields with event.idm.read_only_udm.additional.fields UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `forwardedfor_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `event_name` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `referralurl` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_id`: Newly mapped `attackid` raw log field with `event.idm.read_only_udm.security_result.threat_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `deviceSeverity` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `eventtime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2026-03-09 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.description`: Removed mapping of `msg` from `event.idm.read_only_udm.security_result.description` UDM field when `type` is `utm` and `subtype` is `ips` to map to a more appropriate UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Mapped `attack` raw log field with `event.idm.read_only_udm.security_result.description` UDM field when `type` is `utm` and `subtype` is `ips`.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `msg` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field when `type` is `utm` and `subtype` is `ips`.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `alert_sub_type` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- Added a grok pattern for message to provide support for SYSLOG+KV logs and added another grok pattern for `key_id` to extract `srcport` and `dstport` fields.  
\- Added a JSON filter to parse alert_data_details.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `Details.SourcePort` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `Details.DestinationPort` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `inter_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.observer.application`: Newly mapped `observer_application` raw log field with `event.idm.read_only_udm.observer.application` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `event_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `alert_time` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `details.Bios` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `details.HostName` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.nat_ip`: Newly mapped `details.IP` raw log field with `event.idm.read_only_udm.principal.nat_ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `agent_uuid` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `alert_name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `Details.SourceAddress` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip`: Newly mapped `Details.DestinationAddress` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `Details.Protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.security_result.about.url`: Newly mapped `ref` raw log field with `event.idm.read_only_udm.security_result.about.url` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `Details.status` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field if status is not present.  
\- `event.idm.read_only_udm.security_result.severity`: Mapped `severity` raw log field to `event.idm.read_only_udm.security_result.severity` UDM field when `crlevel` and `level` are empty.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `log_verbosity`, `root_scope_id`,`timestamp_details`,`observer_application_pid`,`Details.ConsumerScopes`, `Details.ProviderScopes` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `user_dst_location`, `user_dst_network_zone`, `user_dst_ownership` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `host_name`, `forwardedfor`, `tenant_id`, `details.AgentType`, `details.CurrentVersion`, `details.Platform`, `scope_name`, `scope_id`, `vrf_id`, `Details.user_src_app_name`, `Details.user_src_environment`, `Details.user_src_location`, `Details.user_src_network_zone`, `Details.user_src_ownership` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `severity`, `alert_text`, `attackid`, `key_id`, `individual_alert`, `summary_alert_freq`, `alert_grain`, `IsConsumerMalicious`, `IsProviderMalicious` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-02-06 |  Enhancement:  
\- `event.idm.read_only_udm.network.email.from`: Newly mapped `from` raw log field with `event.idm.read_only_udm.network.email.from` UDM field.  
\- `event.idm.read_only_udm.network.email.to`: Newly mapped `to` raw log field with `event.idm.read_only_udm.network.email.to` UDM field.  
\- `event.idm.read_only_udm.network.email.subject`: Newly mapped `subject` raw log field with `event.idm.read_only_udm.network.email.subject` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `size` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `attachment` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-12-19 |  Enhancement:  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `ipaddr` raw log field to `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `ipaddr` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `qtype` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.dns.questions.type`: Newly mapped `qtypeval` raw log field to `event.idm.read_only_udm.network.dns.questions.type` UDM field.  
\- `event.idm.read_only_udm.network.dns.questions.name`: Newly mapped `qname` raw log field to `event.idm.read_only_udm.network.dns.questions.name` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `referralurl` raw log field to `event.idm.read_only_udm.network.http.referral_url` UDM field when `type` is `utm` and `subtype` is `webfilter`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `xid` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-10-16 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.action`: Removed mapping of `action` from `event.idm.read_only_udm.security_result.action` UDM field when `action` is equal to `ip-conn` because it indicates that ip-connection is established.  
\- `event.idm.read_only_udm.security_result.action`: Mapped `action` raw log field with `event.idm.read_only_udm.security_result.action` to `ALLOW` when `action` is equal to `ip-conn` UDM field  
\- `event.idm.read_only_udm.security_result.action`: Removed mapping of `utmaction` from `event.idm.read_only_udm.security_result.action` UDM field because duplicate mapping of `security_result.action` is present.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `trandisp` with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-10-10 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `tunneltype`, `tunnelid` and `msg` raw log field to `event.idm.read_only_udm.additional.fields` with key `tunnel_type`, `tunnel_id` and `msg` respectively.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `dst_host` raw log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Removed mapping of `remip` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` for events where `logdesc` contains `SSL VPN`. This change has been done as for this particular event IP is from originating user's request.  
\- `event.idm.read_only_udm.principal.ip`: Mapped `remip` raw log field to `event.idm.read_only_udm.principal.ip` for events where `logdesc` contains `SSL VPN`. This change has been done as for this particular event IP is from originating user's request.   
2025-10-08 |  Enhancement:  
\- `event.idm.read_only_udm.target.port`: Newly mapped `remport` raw log field to `event.idm.read_only_udm.target.port`.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `locport` raw log field to `event.idm.read_only_udm.principal.port`.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `outintf` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cookies`, `init`, `mode`, `stage`, `role`, `result`, `useralt`, `xauthuser`, `xauthgroup`, `assignip`, `vpntunnel` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- Modified the logic for mapping `event.idm.read_only_udm.network.direction` to include the `dir` raw log field when determining `INBOUND` or `OUTBOUND` direction.   
2025-09-23 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `unauthuser`, `user_name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `app_protocol_src` (as `service`), `cloudaction`, `itime`, `shapingpolicyname`, `mastersrcmac`, `shapingpolicyname`, `cloudaction`, `dstdevtype`, `eventsubtype`, `pdstport`, `psrcport`, `clouduser`,`unauthusersource` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `devid`, `incidentserialno`, `poluuid` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `http_retcode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `http_method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `http_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `http_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `srcfamily` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.network.tls.cipher: Newly mapped `cipher_suite` raw log field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `policy` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `http_response_bytes` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `http_request_bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.principal.platform: Newly mapped `osname` raw log field with `event.idm.read_only_udm.principal.platform` UDM field.  
\- event.idm.read_only_udm.target.platform: Newly mapped `dstosname` raw log field with `event.idm.read_only_udm.target.platform` UDM field.  
\- event.idm.read_only_udm.network.tls.client.certificate.subject: Newly mapped `scertcname` raw log field with `event.idm.read_only_udm.network.tls.client.certificate.subject` UDM field.  
\- event.idm.read_only_udm.target.platform_version: Newly mapped `dstswversion` raw log field with `event.idm.read_only_udm.target.platform_version` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `dsthwvendor` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.file.size: Newly mapped `filesize` raw log field with `event.idm.read_only_udm.target.file.size` UDM field.  
\- event.idm.read_only_udm.network.application_protocol_version: Newly mapped `http_version` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- event.idm.read_only_udm.network.tls.server.certificate.subject: Newly mapped `x509_cert_subject` raw log field with `event.idm.read_only_udm.network.tls.server.certificate.subject` UDM field.  
\- event.idm.read_only_udm.principal.platform_version: Newly mapped `srcswversion` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- event.idm.read_only_udm.network.tls.version: Newly mapped `tlsver` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `original_src` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `http_host` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `http_refer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.   
2025-09-18 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `logver` raw log field with event.idm.read_only_udm.metadata.product_version UDM field.  
\- `event.idm.read_only_udm.principal.nat_ip`: Newly mapped `transip` raw log field with event.idm.read_only_udm.principal.nat_ip UDM field.  
\- `event.idm.read_only_udm.principal.nat_port`: Newly mapped `transport` raw log field with event.idm.read_only_udm.principal.nat_port UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `masterdstmac` raw log field with event.idm.read_only_udm.target.resource.attribute.labels UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `devid` raw log field with event.idm.read_only_udm.principal.resource.attribute.labels UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `dstreputation`, `srchwvendor`, `devtype`, `shapingpolicyid`, `shaperdropsentbyte`, `wanin`, `wanout`, `lanin`, `lanout`, `countweb`, `countapp`, `srcserver`, `dstinetsvc`, `poluuid`, `sentdelta`, `rcvddelta`, `shapersentname`, `tz` and `dstserver` raw log fields with event.idm.read_only_udm.additional.fields UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `srccountry` raw log field with event.idm.read_only_udm.additional.fields UDM field if `srccountry` is equal to `Reserved`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `dstcountry` raw log field with event.idm.read_only_udm.additional.fields UDM field if `dstcountry` is equal to `Reserved`.  
\- `event.idm.read_only.udm.security_result.action`: Removed mapping of `BLOCK` from `event.idm.read_only_udm.security_result.action` UDM field when `action` is equal to `close` because the connection is closed normally and not a blocked connection.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `ALLOW` to `event.idm.read_only_udm.security_result.action` UDM field if `action` is equal to `close`.  
\- `event.idm.read_only.udm.security_result.action`: Removed mapping of `UNKNOWN_ACTION` from `event.idm.read_only_udm.security_result.action` UDM field when `action` is equal to `client-rs` because it indicates that client reset the connection and this is a successful connection.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `ALLOW` to `event.idm.read_only_udm.security_result.action` UDM field if `action` is equal to `close`.   
2025-07-07 |  Enhancement:  
\- Corrected conditional logic to ensure the `app` field from raw logs is consistently mapped to the `target.application` UDM field when present. This resolves an issue where the mapping was previously skipped if other conditions were met.  
\- Added `on_error` handling to several mutate filters to improve parser robustness.   
2025-06-04 |  Enhancement:  
\- event.idm.read_only_udm.security_result2.rule_type: Removed mapping of `eventtype` from `event.idm.read_only_udm.security_result2.rule_type` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Mapped `eventtype` from `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result1.rule_name: Removed mapping of `catdesc` from `event.idm.read_only_udm.security_result1.rule_name` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Mapped `catdesc` from `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.security_result1.detection_fields: Removed mapping of `crscore` from `event.idm.read_only_udm.security_result1.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Mapped `crscore` from `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-05-12 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `dtype` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.   
2025-04-30 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Added support for variation of date, time and timezone format.  
\- event.idm.read_only_udm.target.asset.hostname: Newly Mapped `device_id` raw field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly Mapped `operation` raw field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly Mapped `log_id` raw field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `pri` raw field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-04-20 |  Enhancement:  
\- `SYSLOG`: Added support for `SYSLOG` format.  
\- Modified gsub pattern in order to parse the logs with `SYSLOG` Format   
2025-04-02 |  Enhancement:  
\- event.idm.read_only_udm.network.http.user_agent,event.idm.read_only_udm.network.http.parsed_user_agent:Newly mapped `agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.   
2025-02-27 |  Enhancement:  
\- Mapped `dstname` to `target.hostname` and `target.asset.hostname`.   
2025-01-31 |  Enhancement:  
\- Mapped `catdesc` to `security_result.rule_name`.  
\- Mapped `crscore` to `security_result.detection_fields`.  
\- Mapped `method` to `network.http.method`.  
\- Mapped `cat` to `security_result.rule_id`.   
2025-01-02 |  Enhancement:  
\- When `action` is `login` and `status` is `success`, then mapped `ALLOW` to `security_result.action`.  
\- When `action` is `login` and `status` is `failure`, then mapped `BLOCK` to `security_result.action`.   
2024-11-28 |  Enhancement:  
\- Mapped `filename` to `target.file.full_path`.   
2024-11-19 |  Enhancement:  
\- Mapped `dstuser` to `target.user.userid`.   
2024-11-13 |  Enhancement:  
\- Mapped `fsaverdict` to `additional.fields`.   
2024-10-28 |  Enhancement:  
\- Changed `srcinf`, `dstinf`, `srcintfrole`, and `dstintfrole` mapping from `security_result.detection_fields` to `additional.fields`.   
2024-10-16 |  Enhancement:  
\- Mapped `type`, `subtype`, and `level` to `metadata.ingestion_labels`.   
2024-10-01 |  Enhancement:  
\- Mapped `logdesc` to `metadata.description`.   
2024-09-23 |  Enhancement:  
\- Modified mapping for `devname` to `principal.resource.attribute.labels`.  
\- Mapped `srcname` to `principal.hostname` and `principal.asset.hostname`.   
2024-09-12 |  Enhancement:  
\- Added conditional checks to map the value `BLOCK` to the `security_result.action` UDM field when the `reason` value is `sslvpn_login_permission_denied`.   
2024-07-22 |  Enhancement:  
\- Added `gusb` to handle the unparsed logs.   
2024-07-04 |  Enhancement:  
\- When `msg` contains `login`, then set `event_type` to `USER_LOGIN`.   
2024-04-25 |  Enhancement:  
\- Mapped `httpmethod` to `network.http.method`.  
\- When `action` is `login`, then map `ALLOW` to `security_result.action`.  
\- When `msg` contains `logged in successfully`, then set `event_type` to `USER_LOGIN`.  
\- When `msg` contains `login failed`, then set `event_type` to `USER_LOGOUT`.   
2023-07-19 |  Bug-Fix:  
\- Added gsub to remove `\n` to parse failing logs.   
2023-05-05 |  \- Added support for logs with CEF format.   
2022-09-19 |  Newly Created Parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
