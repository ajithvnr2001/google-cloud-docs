---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-nx-changelog/
title: Change log for FIREEYE_NX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:13:33.511658+00:00
---

# Change log for FIREEYE_NX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-nx-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FIREEYE_NX

Date | Changes  
---|---  
2026-10-01 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.rule_name`: If `alert.name` is `ips-event`, mapped `alert.explanation.ips-detected.sig-name` to `event.idm.read_only_udm.security_result.rule_name`.   
2026-09-18 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `alert.explanation.malware-detected.malware.name` raw log field to `event.idm.read_only_udm.security_result.threat_name` UDM field when index is `0`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `alert.explanation.cnc-services.cnc-service.address`, `alert.explanation.cnc-services.cnc-service.port`, `alert.explanation.cnc-services.cnc-service.protocol`, `alert.explanation.cnc-services.cnc-service.sname`, `alert.explanation.cnc-services.cnc-service.type`, `alert.explanation.malware-detected.malware.name` (when index is not `0`), `alert.explanation.malware-detected.malware.application`, `alert.explanation.malware-detected.malware.http-header`, `alert.explanation.malware-detected.malware.md5sum`, `alert.explanation.malware-detected.malware.sha1`, `alert.explanation.malware-detected.malware.sha256`, `alert.explanation.malware-detected.malware.original` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-09-01 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: Removed mapping of `alert.alert-url` raw log field from `event.idm.read_only_udm.security_result.url_back_to_product` UDM field in order to introduce a more accurate `mapping` for the raw log field.  
\- `event.idm.read_only_udm.metadata.url_back_to_product`: Mapped `alert.alert-url` raw log field with `event.idm.read_only_udm.metadata.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `alert.sensor`, `alert.product`, `alert.version` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-08-20 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.summary`: Removed mapping of `event_item.name` from `event.idm.read_only_udm.security_result.summary` UDM field as `event_item.name` represents detailed description about a single step in the log rather than the main alert summary.  
\- `event.idm.read_only_udm.about.resource.attribute.labels`: Mapped `event_item.name` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `event_item.occurred`, `event_item.details.payload`, `event_item.protocol`, `event_item.id`, `event_item.sequence`, `event_item.src_port`, `event_item.dst_port` from `event.idm.read_only_udm.additional.fields` UDM field to map it to more appropriate UDM field.  
\- `event.idm.read_only_udm.about.resource.attribute.labels`: Mapped `event_item.occurred`, `event_item.details.payload`, `event_item.protocol`, `event_item.id`, `event_item.sequence`, `event_item.src_port`, `event_item.dst_port` raw log field to `event.idm.read_only_udm.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.observer.ip`: Removed mapping of `event_item.src_ip` from `event.idm.read_only_udm.observer.ip` UDM field because the observer noun is reserved for the security appliance monitoring the event, not the attacking source IP.  
\- `event.idm.read_only_udm.about.ip`: Mapped `event_item.src_ip` raw log field to `event.idm.read_only_udm.about.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `alert_tag_1` raw log field with `event.idm.read_only_udm.additional.fields` UDM field when `alert.description` is similar to `Possible Nmap`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_pri` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-08-03 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.threat_name` and `event.idm.read_only_udm.security_result.summary`: Removed the mapping of `entry.data.alert.explanation.malware-detected.malware.name` raw log field from `event.idm.read_only_udm.security_result.summary` and `event.idm.read_only_udm.security_result.threat_name` UDM fields as it's a duplicate mapping and this handles standardized threat identifiers without duplication.  
\- `event.idm.read_only_udm.security_result.rule_name`: Mapped `entry.data.alert.explanation.malware-detected.malware.name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field when `cnc-services.cnc-service.sname` is not present.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Accept` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-07-24 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection.fields`: Removed mapping of `cnc-services.cnc-service.sname` from `event.idm.read_only_udm.security_result.detection.fields` UDM field as `cnc-services.cnc-service.sname` represents the specific detection signature or rule.  
\- `event.idm.read_only_udm.security_result.rule_name`: Mapped `cnc-services.cnc-service.sname` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.   
2026-07-09 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.rule_name`: Removed mapping of `alert.name` from `event.idm.read_only_udm.security_result.rule_name` UDM field as `alert.name` represents the product's event category.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Mapped `alert.name` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `entry.data.alert.uuid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `User-Agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.tls.version_protocol`: Newly mapped `protocol_version` raw log field with `event.idm.read_only_udm.network.tls.version_protocol` UDM field.  
\- `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac`: Newly mapped `entry.data.alert.dst.mac` raw log field with `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.observer.hostname` and `event.idm.read_only_udm.observer.asset.hostname`: Newly mapped `entry.data.appliance` raw log field with `event.idm.read_only_udm.observer.hostname` and `event.idm.read_only_udm.observer.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `event_item_details_user` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `event_item_details_domain` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Added a condition to map `alert.id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field when `alert.signature_id` is not present to avoid overwriting.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `alert.explanation.cnc-services.cnc-service.host`, `alert.id`, `alert.explanation.cnc-services.cnc-service.protocol`, `alert.explanation.cnc-services.cnc-service.port`, `alert.explanation.cnc-services.cnc-service.address`, `alert.explanation.cnc-services.cnc-service.channel`, `alert.explanation.cnc-services.cnc-service.sid`, `alert.interface.mode`, `alert.interface.label`, `alert.interface.interface`, `alert.explanation.malware-detected.malware.sid`, `alert.explanation.cnc-services.cnc-service.type`, `alert.explanation.cnc-services.cnc-service.sname` and `alert.ack` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `entry.data.appliance-id`, `alert.explanation.events.occurred`, `alert.explanation.events.details.payload`, `alert.explanation.events.vlan`, `alert.explanation.events.protocol`, `alert.explanation.events.details.app_data.payload_app`, `alert.explanation.events.details.app_data.service_app`, `alert.explanation.events.details.app_data.payload_app_id`, `alert.explanation.events.details.app_data.service_app_id`, `alert.explanation.events.details.workstation`, `alert.sc-version`, `alert.src.vlan`, `msg`, `alert.attack-time`, `alert.root-infection`, `alert.sensor`, `alert.sensor-ip`, `Accept-Encoding`, `Connection`, `Accept-Language`, `Content-Type` and `spring.cloud.function.routing-expression` raw log fields with `event.idm.read_only_udm.additional.fields` UDM fields.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `Host` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2026-07-06 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `event_name` log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `device_event_class_id` log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-06-28 |  Enhancement:  
\- Added grok pattern to parse new log format.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `alert_tag_1` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.about.file.mime_type`: Newly mapped `alert.explanation.malware-detected.malware.type` raw log field with `event.idm.read_only_udm.about.file.mime_type` UDM field.  
\- `event.idm.read_only_udm.about.file.md5`: Newly mapped `alert.explanation.malware-detected.malware.md5sum` raw log field with `event.idm.read_only_udm.about.file.md5` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `alert.explanation.malware-detected.malware.submitted-at`, `alert.explanation.malware-detected.malware.executed-at`, `alert.attack-time` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `alert.explanation.malware-detected.malware.profile`, `alert.explanation.malware-detected.malware.malicious`, `alert.explanation.malware-detected.malware.original` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-05-29 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `body`, `description` raw log fields with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `alert.explanation.target-application` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.platform`: Newly mapped `alert.explanation.target-os` raw log field with `event.idm.read_only_udm.target.platform` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `alert.explanation.malware-detected.malware.content`, `alert.explanation.malware-detected.malware.stype`, `alert.explanation.malware-detected.malware.sid`, `alert.explanation.analysis`, `alert.explanation.cnc-services.cnc-service.sid`, `alert.explanation.cnc-services.cnc-service.sname`, `alert.explanation.cnc-services.cnc-service.type` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `principal_process_full_path` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `alert.explanation.protocol`, `transport` raw log fields with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.principal.hostname, event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `alert.src.host`, `attributes.net.peer.name`, `principal_hostname` raw log fields with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.about.hostname`, `event.idm.read_only_udm.about.asset.hostname`: Newly mapped `alert.explanation.cnc-services.cnc-service.address` raw log field with `event.idm.read_only_udm.about.hostname` and `event.idm.read_only_udm.about.asset.hostname` UDM fields when not an IP address.  
\- `event.idm.read_only_udm.about.ip`, `event.idm.read_only_udm.about.asset.ip`: Newly mapped `alert.explanation.cnc-services.cnc-service.address` raw log field with `event.idm.read_only_udm.about.ip` and `event.idm.read_only_udm.about.asset.ip` UDM fields when a valid IP address.  
\- `event.idm.read_only_udm.about.port`: Newly mapped `alert.explanation.cnc-services.cnc-service.port` raw log field with `event.idm.read_only_udm.about.port` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `alert.explanation.malware-detected.malware.name` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `net_host_ip_parsed` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.platform`: Newly mapped `resource_attributes.os.type` raw log field with `event.idm.read_only_udm.intermediary.platform` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `attributes.net.host.name`, `resource_attributes.host.name` raw log fields with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.port`: Newly mapped `attributes.net.host.port` raw log field with `event.idm.read_only_udm.intermediary.port` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `attributes.net.peer.port` raw log field with `event.idm.read_only_udm.principal.port` UDM field when `alert.src.port` is not a number and `event.idm.read_only_udm.principal.port` is not mapped.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `net_peer_ip_parsed` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `alert_tag`, `alert.sc-version`, `msg`, `attributes.log_type`, `rawmsg.dns.tx_id`, `rawmsg.dns.type`, `rawmsg.flow_id`, `rawmsg.iface`, `rawmsg.session_key`, `attributes.net.peer.name`, `attributes.net.peer.port`, `alert.explanation.cnc-services.cnc-service.protocol`, `alert.explanation.cnc-services.cnc-service.channel`, `alert.explanation.service`, `alert.explanation.urls` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-04-20 |  Enhancement:  
\- `event.idm.read_only_udm.about.file.full_path`: Removed mapping of `filePath` raw log field from `event.idm.read_only_udm.about.file.full_path` UDM field as `filePath` field corresponds to target details.  
\- `event.idm.read_only_udm.target.file.full_path`: Mapped `filePath` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.about.file.mime_type`: Removed mapping of `fileType` raw log field from `event.idm.read_only_udm.about.file.mime_type` UDM field as `fileType` field corresponds to target details.  
\- `event.idm.read_only_udm.target.file.mime_type`: Mapped `fileType` raw log field with `event.idm.read_only_udm.target.file.mime_type` UDM field.  
\- `event.idm.read_only_udm.about.file.size`: Removed mapping of `fsize` raw log field from `event.idm.read_only_udm.about.file.size` UDM field as `fsize` field corresponds to target details.  
\- `event.idm.read_only_udm.target.file.size`: Mapped `fsize` raw log field with `event.idm.read_only_udm.target.file.size` UDM field.  
\- `event.idm.read_only_udm.about.file.sha256`: Removed mapping of `fileHash` raw log field from `event.idm.read_only_udm.about.file.sha256` UDM field as `fileHash` field corresponds to target details.  
\- `event.idm.read_only_udm.target.file.md5`: Mapped `fileHash` raw log field with `event.idm.read_only_udm.target.file.md5` UDM field if `fileHash` is an MD5 hash.  
\- `event.idm.read_only_udm.target.file.sha256`: Mapped `fileHash` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field if `fileHash` is a SHA256 hash.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `fname` raw log field from `event.idm.read_only_udm.additional.fields` UDM field as `fname` field corresponds to target details.  
\- `event.idm.read_only_udm.target.file.names`: Mapped `fname` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `flexString1` raw log field from `event.idm.read_only_udm.additional.fields` UDM field as `flexString1` field corresponds to target details.  
\- `event.idm.read_only_udm.target.file.sha256`: Mapped `flexString1` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field if `flexString1` is a SHA256 hash.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `device_vendor` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added a grok pattern on `temp_data` to extract `Type`.   
2026-03-31 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_name`: Removed mapping of `product`, `entry.data.product`, `device_product` and `_source.alert_product` raw log fields from `event.idm.read_only_udm.metadata.product_name` UDM as we are mapping a static value (`NX`) across all events.  
\- `event.idm.read_only_udm.metadata.product_name`: Mapped `NX` static value to `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `product`, `entry.data.product`, `device_product` and `_source.alert_product` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-03-27 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `cs5` (where `cs5Label` is `cncHost`) from `event.idm.read_only_udm.additional.fields` UDM field, because this data more appropriately belongs in the specific fields within the `event.idm.read_only_udm.target` UDM noun, depending on whether `cs5` contains an IP address or a hostname.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Mapped `cs5` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields, moving it from additional fields for better UDM alignment when it represents a hostname.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Mapped `cs5` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields, as this field now correctly represents the destination Command and Control host's IP address within the target noun, rather than a generic additional field.  
\- `event.idm.read_only_udm.about.hostname`: Removed mapping of `dvchost` from `event.idm.read_only_udm.about.hostname` UDM field, because the device is better represented as an intermediary device.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Mapped `dvchost` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM fields, as this more accurately represents the device's role.  
\- `event.idm.read_only_udm.about.ip`: Removed mapping of `dvc` from `event.idm.read_only_udm.about.ip` UDM field, because the device is better represented as an intermediary device.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Mapped `dvc` raw log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields,when it is a valid IP address, as this more accurately represents the device's role.  
\- `event.idm.read_only_udm.about.mac`: Removed mapping of `dvcmac` from `event.idm.read_only_udm.about.mac` UDM field, because the device is better represented as an `event.idm.read_only_udm.intermediary` device.  
\- `event.idm.read_only_udm.intermediary.mac` and `event.idm.read_only_udm.intermediary.asset.mac`: Mapped `dvcmac` raw log field with `event.idm.read_only_udm.intermediary.mac` and `event.idm.read_only_udm.intermediary.asset.mac` UDM fields, as this more accurately represents the device's role.   
2026-03-05 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_name`: Mapping static value (`NX`) to `event.idm.read_only_udm.metadata.product_name` UDM field when `event.idm.read_only_udm.metadata.product_name` is empty.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `rawmsg.dcerpc.response_stub_data_len` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `rawmsg.dcerpc.request_stub_data_len` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `rawmsg.dcerpc.interface.uuid`, `rawmsg.dcerpc.interface.version`, and `rawmsg.dcerpc.interface.minor-version` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `rawmsg.dcerpc.request_stub_data` (key: `dcerpc_request_stub_data`), `rawmsg.dcerpc.response_stub_data` (key: `dcerpc_response_stub_data`), and `rawmsg.dcerpc.opnum` (key: `dcerpc_opnum`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-02-26 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.rule_id`: If `cn2Label` is `signatureId` or `sid`, set the value of `event.idm.read_only_udm.security_result.rule_id` with the value of `cn2` raw log field.  
\- `event.idm.read_only_udm.security_result.rule_name`: If `cs1Label` is `sname`, set the value of `event.idm.read_only_udm.security_result.rule_name` with the value of `cs1` raw log field.  
\- `event.idm.read_only_udm.target.url`: If `cs4Lablel` is `link`, set the value of `event.idm.read_only_udm.target.url` with the value of `cs4` raw log field.  
\- Added support for a nested JSON format within the raw message.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `rawmsg.timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `rawmsg.event_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `rawmsg.src_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `rawmsg.src_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `rawmsg.src_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `rawmsg.dest_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `rawmsg.dest_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `rawmsg.dest_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `rawmsg.proto` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.network.dns.id`: Newly mapped `rawmsg.dns.id` raw log field with `event.idm.read_only_udm.network.dns.id` UDM field.  
\- `event.idm.read_only_udm.network.dns.questions.name`: Newly mapped `rawmsg.dns.rrname` raw log fields with `event.idm.read_only_udm.network.dns.questions.name` UDM field.  
\- `event.idm.read_only_udm.network.dns.questions.type`: Newly mapped `rawmsg.dns.rrtype` raw log field with `event.idm.read_only_udm.network.dns.questions.type` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `rawmsg.dns.tx_id` (key: `dns_tx_id`), `rawmsg.dns.type` (key: `dns_type`), `rawmsg.flow_id` (key: `flow_id`), `rawmsg.iface` (key: `iface`), `rawmsg.session_key` (key: `session_key`), `meta_oml` (key: `meta_oml`), `cn2Lablel` (key: `signature_id`), `cn4Lablel` (key: `link`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `meta_sip4` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset_id`: Newly mapped `deviceid` raw log field with `event.idm.read_only_udm.target.asset_id` UDM field.  
\- `event.idm.read_only_udm.target.asset.asset_id`: Newly mapped `deviceid` raw log field with `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `meta_cbname` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `meta_cbname` raw log field with `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Setting the value of `event.idm.read_only_udm.network.application_protocol` to `DNS` when network DNS data is present.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `entry.data.alert.explanation.malware-detected.malware.stype` (key: `malware_stype`) raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- Setting the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_DNS` when network DNS data is present.  
\- Modified conditional logic for setting `event.idm.read_only_udm.metadata.event_type` to `SCAN_UNCATEGORIZED` and `NETWORK_CONNECTION`.   
2026-01-01 |  Enhancement:  
\- event.idm.read_only_udm.network.application_protocol: Removed mapping where event.idm.read_only_udm.network.application_protocol was set to `HTTP` based on the raw log field `message` since the logic is too broad and improperly sets application_protocol to `HTTP` based on unrelated string matches.  
\- The raw field `entry.data.alert.occurred` is now aliased to alert_occurred before being used in the date filter.  
\- The raw field `entry.data.alert.name` is now aliased to alert_name before being used for sec_category and product_event_type.  
\- event.idm.read_only_udm.metadata.event_type: If has_http is `true` and (has_principal_host is `true` or has_principal_ip is `true`) and (has_target_host is `true` or has_target_ip is `true`) OR (src is not empty and dst is not empty and has_http is `true`) OR has_http is `true`, updated to NETWORK_HTTP.  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped `HTTP` to event.idm.read_only_udm.network.application_protocol when the event type is determined to be NETWORK_HTTP.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped `product` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `alert.action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `alert.vlan`, `version` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `alert.explanation.ips-detected.action-taken`, `alert.explanation.ips-detected.signature-name`, `alert.interface.interface`, `alert.interface.label` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-12-31 |  Enhancement:  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `alert.src.port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `alert.src.ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `alert.src.mac` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `alert.dst.ip`, `event_item.dst_ip` raw log fields with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `alert.dst.port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac`: Newly mapped `alert.dst.mac` raw log field with `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `alert.signature_id`, `alert.id` raw log fields with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `alert.name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `alert.description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `appliance` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `alert.occurred` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `appliance-id`, `alert.class`, `alert.count`, `event_item.id`, `event_item.sequence`, `event_item.src_port`, `event_item.dst_port`, `event_item.details.geo_org`, `event_item.details.ratio`, `alert.src.vlan`, `alert.root-infection`, `alert.ack` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `alert.uuid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `alert.protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `alert.severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: Newly mapped `alert.alert-url` raw log field with `event.idm.read_only_udm.security_result.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `alert.category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.observer.ip`: Newly mapped `event_item.src_ip` raw log field with `event.idm.read_only_udm.observer.ip` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `event_item.details.dest_ip_resolved` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `event_item.details.duration_seconds` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `event_item.details.inbound_mb` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `event_item.details.outbound_mb` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `event_item.name` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `alert.class` is SmartVision, updated to `NETWORK_FLOW`.   
2025-08-13 |  Enhancement:  
\- Modified mutate filter to handle escaped backslashes in the cs4 field.  
\- event.idm.read_only_udm.security_result.first_discovered_time: Newly mapped `start` raw log field with event.idm.read_only_udm.security_result.first_discovered_time UDM field.  
\- event.idm.read_only_udm.security_result.last_discovered_time: Newly mapped `end` raw log field with event.idm.read_only_udm.security_result.last_discovered_time UDM field.  
\- event.idm.read_only_udm.about.mac: Added a regex validation to ensure dvc_mac values match a standard MAC address format before proceeding with parsing. This prevents invalid values from being merged into the about.mac field.  
\- Modified the conditional logic for assigning security_result.action to `ALLOW` or `BLOCK` based on the value of the `act` raw field.   
2025-06-05 |  Enhancement:  
\- Added Grok patterns to parse the unparsed logs.  
\- Added JSON block to support the new format of SYSLOG+JSON logs.  
\- `event.idm.read_only_udm.metadata.event_timestamp` \- Newly Mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM Field.  
\- `event.idm.read_only_udm.` \- Newly Mapped `event_type` raw log field with `event.idm.read_only_udm.metadata.event_type` UDM Field.  
\- `event.idm.read_only_udm.principal.user.userid` \- Newly Mapped `user_name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM Field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` \- Newly Mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM Field.  
\- `event.idm.read_only_udm.principal.user.userid` \- Newly Mapped `user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM Field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` \- Newly Mapped `dstip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM Field.  
\- `event.idm.read_only_udm.target.file.sha1` \- Newly Mapped `file_hash` raw log field with `event.idm.read_only_udm.target.file.sha1` UDM Field.  
\- `event.idm.read_only_udm.target.file.sha256` \- Newly Mapped `file_sha256` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM Field.  
\- `event.idm.read_only_udm.target.file.full_path` \- Newly Mapped `file_name` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM Field.  
\- `event.idm.read_only_udm.target.file.size` \- Newly Mapped `size` raw log field with `event.idm.read_only_udm.target.file.size` UDM Field.  
\- `event.idm.read_only_udm.principal.port` \- Newly Mapped `srcports` raw log field with `event.idm.read_only_udm.principal.port` UDM Field.  
\- `event.idm.read_only_udm.target.file.mime_type` \- Newly Mapped `file_type` raw log field with `event.idm.read_only_udm.target.file.mime_type` UDM Field.  
\- `event.idm.read_only_udm.security_result.detection_fields` \- Newly Mapped `file_id`,`ba_sid`, `reqid`, `conn_count`, `failed_conn_count`, `message_id`, `app_data.service_app_id`, `accept`,, `message_type, `app_data.client_app_id`, `attackdir`, `oversize`, `smb`, `is_icap`, `ha_is_active`, `ha_is_mirror_traffic`, `is_vxlan`, `is_websocket` and `attack_time' raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM Field.  
\- `event.idm.read_only_udm.target.port` \- Newly Mapped `dstports` raw log field with `event.idm.read_only_udm.target.port` UDM Field.  
\- `event.idm.read_only_udm.primcipal.mac` and `event.idm.read_only_udm.principal.asset.mac` \- Newly Mapped `src_mac` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM Field.  
\- `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` \- Newly Mapped `dst_mac` raw log field with `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` UDM Field.  
\- `event.idm.read_only_udm.principal.application` \- Newly Mapped `process` raw log field with `event.idm.read_only_udm.principal.application` UDM Field.  
\- `event.idm.read_only_udm.network.ip_protocol` \- Newly Mapped `protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM Field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels` \- Newly Mapped `db_action` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM Field.  
\- `event.idm.read_only_udm.principal.process.pid` \- Newly Mapped `pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM Field.  
\- `event.idm.read_only_udm.additional.fields` \- Newly Mapped `tid`, `sa_only`, `incomplete`, `clientapp`, `is_erspan`, `thread_pool`, `updated_meas_list`, `inserted_meas_list`, `insert_count`, `update_count`, `epoch_time`, `segment_date`, `request_message_id` and `ssl_decrypted` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- `event.idm.read_only_udm.target.resource.name` \- Newly Mapped `db_pool` raw log field with `event.idm.read_only_udm.target.resource.name` UDM Field.  
\- `event.idm.read_only_udm.target.resource.product_object_id` \- Newly Mapped `db_handler` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM Field.  
\- `event.idm.read_only_udm.security_result.summary` \- Newly Mapped `db_details` raw log field with `event.idm.read_only_udm.security_result.summary` UDM Field.  
\- `event.idm.read_only_udm.security_result.severity` \- Newly Mapped `log_level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM Field.  
\- `event.idm.read_only_udm.security_result.description` \- Newly Mapped `log_message` raw log field with `event.idm.read_only_udm.security_result.description` UDM Field.  
\- `event.idm.read_only_udm.target.process.command_line` \- Newly Mapped `command_line` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM Field.  
\- `event.idm.read_only_udm.network.http.method` \- Newly Mapped `http_method` raw log field with `event.idm.read_only_udm.network.http.method` UDM Field.  
\- `event.idm.read_only_udm.target.url` \- Newly Mapped `request_uri` raw log field with `event.idm.read_only_udm.target.url` UDM Field.  
\- `event.idm.read_only_udm.network.http.referral_url` \- Newly Mapped `http_referer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM Field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` \- Newly Mapped `srcip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM Field  
\- `event.idm.read_only_udm.network.http.user_agent` \- Newly Mapped `user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM Field.  
\- `event.idm.read_only_udm.target.port` \- Newly Mapped `http_port` raw log field with `event.idm.read_only_udm.target.port` UDM Field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` \- Newly Mapped `http_host' raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM Field.  
\- `event.idm.read_only_udm.network.received_bytes` \- Newly Mapped `request_length` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM Field.  
\- `event.idm.read_only_udm.network.application_protocol_version` \- Newly Mapped `http_version` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM Field.  
\- `event.idm.read_only_udm.target.process.file.full_path` \- Newly Mapped `binary_path` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM Field.  
\- `event.idm.read_only_udm.target.resource.name` \- Newly Mapped `resource_path` raw log field with `event.idm.read_only_udm.target.resource.name` UDM Field.  
\- `event.idm.read_only_udm.target.user.userid` \- Newly Mapped `target_user` raw log field with `event.idm.read_only_udm.target.user.userid` UDM Field.  
\- `event.idm.read_only_udm.security_result.action` \- Newly Mapped `log_message` raw log field when it is nearly same as `authorized` to ALLOW and `denied` to BLOCK with `event.idm.read_only_udm.security_result.action` UDM Field.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` \- Newly Mapped `incoming_peer_name` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM Field.  
\- `event.idm.read_only_udm.network.session_id` \- Newly Mapped `incoming_session_id` and `session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM Field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` \- Newly Mapped `client` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM Field.  
\- `event.idm.read_only_udm.principal.group_product_object_id` \- Newly Mapped `group_id` raw log field with `event.idm.read_only_udm.principal.group_product_object_id` UDM Field.  
\- `event.idm.read_only_udm.target.process.pid` \- Newly Mapped `target_pid` raw log field with `event.idm.read_only_udm.target.process.pid` UDM Field.   
2024-10-17 |  Enhancement:  
\- Added `gsub` for `dvcmac` to parse CEF pattern logs.   
2024-10-10 |  Enhancement:  
\- Added support for new pattern of CEF logs.   
2022-05-18 |  Enhancement - The newly ingested logs have been parsed and mapped to the following fields:  
`_source.alert.attack-time` mapped to `metadata.ingested_timestamp`.  
`_source.srcport` mapped to `principal.port`.  
`_source.srcipv4` mapped to `principal.ip`.  
`_source.mac` mapped to `principal.mac`.  
`_source.dstport` mapped to `target.port`.  
`_source.dstipv4` mapped to `target.ip`.  
`_source.dstmac` mapped to `target.mac`.  
`_source.alerturl` mapped to `metadata.url_back_to_product`.  
`_source.alert_product` mapped to `metadata.product_name`.  
`_source.alert_version` mapped to `metadata.product_version`.  
`_source.eventlog` mapped to `metadata.product_name`.  
`_source.virus` mapped to `security_result.threatname`.  
`_source.url` mapped to `target.url`.  
`_source.severity` mapped to `security_result.severity`.  
`__source.detect_rulematches` mapped to `security_result.rule_id`.  
`_source.alert_deviceid` mapped to `principal.asset.asset_id`.  
`_source.deviceid` mapped to `asset.asset_id`.  
`_source.devicename` mapped to `target.asset.attribute.labels`.  
`_source.domain` mapped to `target.hostname`.  
`entry.data.alert.mitre-mapping.code.id` mapped to `security_result.rule_id`.  
`entry.data.alert.mitre-mapping.code.name` mapped to `security_result.rule_name`.  
`entry.data.alert.dst.smtp-to` mapped to `network.email.to`.  
`entry.data.alert.severity` mapped to `security_result.severity`.  
`_source.action` mapped to `security_result.action`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
