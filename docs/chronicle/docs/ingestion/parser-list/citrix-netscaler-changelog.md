---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/citrix-netscaler-changelog/
title: Change log for CITRIX_NETSCALER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:28.933856+00:00
---

# Change log for CITRIX_NETSCALER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/citrix-netscaler-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CITRIX_NETSCALER

Date | Changes  
---|---  
2026-09-30 |  Enhancement:  
\- Added grok pattern to parse new format of syslogs.  
\- Added support for new format of timestamp for `event_timestamp`.   
2026-05-27 |  Enhancement:  
\- Modified the grok pattern on `HOST` raw log field to extract target hostname data.  
\- `event.idm.read_only_udm.target.url`: If `URL` does not start with `https://`, updated the value of `event.idm.read_only_udm.target.url` UDM field to be prepended with `https://`.   
2026-05-22 |  Enhancement:  
\- `event.idm.read_only_udm.principal.nat_ip and event.idm.read_only_udm.principal.asset.nat_ip`: Newly mapped `NAT_IPv4`, `NAT_IPv6` raw log fields with `event.idm.read_only_udm.principal.nat_ip` and `event.idm.read_only_udm.principal.asset.nat_ip` UDM field.   
2026-05-08 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `URL` from `event.idm.read_only_udm.additional.fields` UDM field when the `URL` field contains a properly formed URL scheme.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `url_value` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `host_port` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-05-07 |  Enhancement:  
\- Modified a grok pattern to parse the new raw logs.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `region` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.nat_ip` and `event.idm.read_only_udm.principal.asset.nat_ip`: Newly mapped `NAT_IP` raw log field with `event.idm.read_only_udm.principal.nat_ip` and `event.idm.read_only_udm.principal.asset.nat_ip` UDM fields.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `USER` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If user data is present, mapped `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `URL` raw log field with `event.idm.read_only_udm.additional.fields` UDM field when `URL` field is not a valid url.   
2026-04-16 |  Enhancement:  
\- Modified a grok pattern to extract `syslog_priority`.  
\- Added support for kv parsing in syslogs.  
\- Added a grok pattern on `desc` to extract `msg_id`, `proxy_action`, `key_value_data`  
\- `event.idm.read_only_udm.target.url`: Newly mapped `URL` raw log field with `event.idm.read_only_udm.target.url` UDM.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `proxy_action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `SRC_IP` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `HOST` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `url_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `User-Agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `User-Agent` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Newly mapped `PROXY_IP` raw log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `proxy_action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `Method` raw log field with `event.idm.read_only_udm.network.http.method`.   
2026-03-31 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Removed mapping of `v_ip` from `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields. Since the `v_ip` represents the NetScaler vServer logging the event, it functions as an `observer` rather than a network intermediary device.  
\- `event.idm.read_only_udm.observer.ip` and `event.idm.read_only_udm.observer.asset.ip`: Mapped `v_ip` raw log field with `event.idm.read_only_udm.observer.ip` and `event.idm.read_only_udm.observer.asset.ip` UDM fields to correctly model the NetScaler vServer as the entity observing and reporting the event.  
\- `event.idm.read_only_udm.intermediary.port`: Removed mapping of `v_port` from `event.idm.read_only_udm.intermediary.port` UDM field, consistent with the `v_ip` reclassification to the `observer` role.  
\- `event.idm.read_only_udm.observer.port`: Mapped `v_port` raw log field with `event.idm.read_only_udm.observer.port` UDM field, associating the port with the observing NetScaler vServer.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Removed mapping of `gwip` from `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields. Since the Gateway IP (`gwip`) represents the NetScaler component logging the event, its role is that of an `observer`, not an intermediary.  
\- `event.idm.read_only_udm.observer.ip`: Mapped `gwip` raw log field with `event.idm.read_only_udm.observer.ip` and `event.idm.read_only_udm.observer.asset.ip` UDM fields, as this accurately reflects the NetScaler Gateway's role as the device observing and reporting the event.  
\- `event.idm.read_only_udm.intermediary.port`: Removed mapping of `gwport` from `event.idm.read_only_udm.intermediary.port` UDM field, consistent with the `gwip` reclassification to the `observer` role.  
\- `event.idm.read_only_udm.observer.port`: Mapped `gwport` raw log field with `event.idm.read_only_udm.observer.port` UDM field, associating the port with the observing NetScaler Gateway.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `Username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.   
2026-02-24 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname`: Removed mapping of `VPNfqdn` from `event.idm.read_only_udm.principal.hostname` UDM field by modifying the grok pattern in `citrix_netscaler.include` file in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `VPNfqdn` from `event.idm.read_only_udm.principal.asset.hostname` UDM field by modifying the grok pattern in `citrix_netscaler.include` file in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.target.hostname` : Newly mapped `VPNfqdn` raw log field with `event.idm.read_only_udm.target.hostname` UDM field when `VPNfqdn` is not an IP, as `VPNfqdn` holds the hostname used to access the backend resource.  
\- `event.idm.read_only_udm.target.asset.hostname` : Newly mapped `VPNfqdn` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field when `VPNfqdn` is not an IP, as `VPNfqdn` holds the hostname used to access the backend resource.  
\- `event.idm.read_only_udm.target.ip` : Newly mapped `VPNfqdn` raw log field with `event.idm.read_only_udm.target.ip` UDM field when `VPNfqdn` contains an IP address, as `VPNfqdn` holds the hostname used to access the backend resource.  
\- `event.idm.read_only_udm.target.asset.ip` : Newly mapped `VPNfqdn` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field when `VPNfqdn` contains an IP address, as `VPNfqdn` holds the hostname used to access the backend resource.  
\- `event.idm.read_only_udm.target.ip`: Removed mapping of `Remote ip` from `event.idm.read_only_udm.target.ip` UDM field by modifying the grok pattern in `citrix_netscaler.include` file in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.target.asset.ip`: Removed mapping of `Remote ip` from `event.idm.read_only_udm.target.asset.ip` UDM field by modifying a Grok pattern in `citrix_netscaler.include` file in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `Remote ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field. This change was implemented by modifying a Grok pattern on `message` to extract `Remote ip` into `principal_ip` variable, because `Remote ip` represents the client machine initiating the connection.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `Remote ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field. This change was implemented by modifying a Grok pattern on `message` to extract `Remote ip` into `principal_ip` variable, because `Remote ip` represents the client machine initiating the connection.  
\- `event.idm.read_only_udm.target.port`: Removed mapping of `Remote ip` from `event.idm.read_only_udm.target.port` UDM field by modifying the grok pattern in `citrix_netscaler.include` file in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `Remote ip` raw log field with `event.idm.read_only_udm.principal.port` UDM field. This change was implemented by modifying a Grok pattern on `message` to extract `Remote ip` into `principal_port` variable, because `Remote ip` represents the client machine initiating the connection.  
\- `event.idm.read_only_udm.principal.ip` : Removed mapping of `BackendIP` from `event.idm.read_only_udm.principal.ip` UDM field by modifying a Grok pattern.  
\- `event.idm.read_only_udm.principal.asset.ip`: Removed mapping of `BackendIP` from `event.idm.read_only_udm.principal.asset.ip` UDM field by modifying the grok pattern in `citrix_netscaler.include` file in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.target.ip` : Newly mapped `BackendIP` raw log field with `event.idm.read_only_udm.target.ip` UDM field. This change was implemented by modifying a Grok pattern on `message` to extract `BackendIP` into `target_ip` variable, because `BackendIP` represents the internal application server being accessed.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `BackendIP` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field. This change was implemented by modifying a Grok pattern on `message` to extract `BackendIP` into `target_ip` variable, because `BackendIP` represents the internal application server being accessed.  
\- `event.idm.read_only_udm.principal.port`: Removed mapping of `BackendIP` from `event.idm.read_only_udm.principal.port` UDM field by modifying the grok pattern in `citrix_netscaler.include` file in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `BackendIP` raw log field with `event.idm.read_only_udm.target.port` UDM field. This change was implemented by modifying a Grok pattern on `message` to extract `BackendIP` into `target_port` variable, because `BackendIP` represents the internal application server being accessed.  
\- Added a Grok pattern to parse the `message` field to extract `userId`, `sess_seq`, `description`, `func`, and `msg1`.  
\- Added a conditional check on `VPNfqdn` to map to either hostname or IP fields in the target UDM field.   
2026-02-05 |  Enhancement:  
\- Newly added grok pattern for the `desc` raw log field in the `citrix_netscaler.include` file to extract `principal_ip`, `principal_port`, and `type`, `description` raw log fields. Mapped these raw log fields to event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.port, and event.idm.read_only_udm.security_result.detection_fields, `event.idm.read_only_udm.metadata.description` respective UDM fields.   
2026-01-26 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.ip`: The raw field `Vserver` is no longer mapped to `event.idm.read_only_udm.intermediary.ip` when the `Vserver` field has the same value as the `Destination` field.  
\- `event.idm.read_only_udm.intermediary.port`: The raw field `Vserver` is no longer mapped to `event.idm.read_only_udm.intermediary.port` when the `Vserver` field has the same value as the `Destination` field.   
2025-11-25 |  Enhancement:  
\- Parser overhaul version to make it more efficient and increase fields coverage. You can see the full list of changes in the parser documentation page https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-netscaler .   
2025-11-21 |  Enhancement:  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `ICAUUID` raw log field to `event.idm.read_only_udm.network.session_id` UDM field in citrix_netscaler.include file.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `ip_protocol` raw log field to `event.idm.read_only_udm.network.ip_protocol` UDM field in citrix_netscaler.include file.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Protocol` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field in citrix_netscaler.include file.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `event_id` raw log field to `event.idm.read_only_udm.additional.fields` UDM field in citrix_netscaler.include file.  
\- Updated condition to set event_type to NETWORK_CONNECTION. The new condition is if `principal_ip` was not null and `Remote_ip` was not null or `Remote_ip` was not null and `principal_hostname` was not null.  
\- Enhanced Grok patterns to support additional log variations for fields `message_data` and `desc`.   
2025-10-17 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `ts` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `policy` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `interface`, `context`, and `event_subtype` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- The description for message_type CONN_DELINK is now set to `TCP connection is delinked`.   
2025-09-18 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip`: Removed mapping of `Nat_ip` from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field since `event.idm.read_only_udm.principal.nat_ip` is more appropriate field for mapping.  
\- `event.idm.read_only_udm.principal.nat_ip`: Newly mapped `Nat_ip` raw log field with `event.idm.read_only_udm.principal.nat_ip` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Removed mapping of v_ip from event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip` UDM field since `event.idm.read_only_udm.intermediary.ip` is more appropriate field for mapping.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped v_ip raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Removed mapping of `v_port` from `event.idm.read_only_udm.target.resource.attribute.labels` UDM field since `event.idm.read_only_udm.intermediary.resource.attribute.labels` is more appropriate field for mapping.  
\- `event.idm.read_only_udm.intermediary.port`: Newly mapped `v_port` raw log field with `event.idm.read_only_udm.intermediary.port` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `event_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-08-19 |  Enhancement:  
\- Added a new grok pattern to `desc` field to parse the logs.  
\- Modified grok patterns to add principal_port and target_port to the overwrite list from `Source`, `Destination` and `message_type` fields.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped source_hostname raw log field to event.idm.read_only_udm.principal.hostname.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped source_hostname raw log field to event.idm.read_only_udm.principal.asset.hostname.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped user_email raw log field to event.idm.read_only_udm.principal.user.email_addresses.  
\- event.idm.read_only_udm.principal.ip: Newly mapped remote_ip raw log field to event.idm.read_only_udm.principal.ip.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped remote_ip raw log field to event.idm.read_only_udm.principal.asset.ip.  
\- event.idm.read_only_udm.principal.port: Newly mapped remote_port raw log field to event.idm.read_only_udm.principal.port.  
\- event.idm.read_only_udm.target.ip: Newly mapped Vserver_ip and client_fip raw log fields to event.idm.read_only_udm.target.ip.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped Vserver_ip and client_fip raw log fields to event.idm.read_only_udm.target.asset.ip.  
\- event.idm.read_only_udm.target.port: Newly mapped Vserver_port and client_fport raw log fields to event.idm.read_only_udm.target.port.  
\- event.idm.read_only_udm.target.url: Newly mapped http_uri raw log field to event.idm.read_only_udm.target.url.  
\- event.idm.read_only_udm.network.http.method: Newly mapped http_method raw log field to event.idm.read_only_udm.network.http.method.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped protocol raw log field to event.idm.read_only_udm.network.ip_protocol.  
\- event.idm.read_only_udm.network.session_id: Newly mapped ica_uuid raw log field to event.idm.read_only_udm.network.session_id.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped message_content raw log field to event.idm.read_only_udm.security_result.summary.  
\- event.idm.read_only_udm.additional.fields: Newly mapped log_type, log_category, source_file, source_line, and sta_ticket raw log fields to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped log_action and cgp_tag raw log fields to event.idm.read_only_udm.security_result.detection_fields.   
2025-08-18 |  Enhancement:  
\- event.idm.read_only_udm.network.tls.cipher: Newly mapped CipherSuite raw log field with event.idm.read_only_udm.network.tls.cipher UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped Session raw log field with event.idm.read_only_udm.additional.fields UDM field.  
\- Added conditional check for ClientIP, VserverServiceIP, ServerIP to validate for valid IP addresses before mapping.  
\- Mapping from the ClientVersion field has been moved to a common logic block to cover more event types.  
\- The logic was updated to remove quotes from the Reason field before it is mapped.  
\- The event_type for SSL_HANDSHAKE_FAILURE events has been updated from STATUS_UPDATE to NETWORK_CONNECTION if VserverServiceIP and ClientIP are present.   
2025-07-30 |  Enhancement:  
\- Added a new grok pattern to parse the logs.  
\- event.idm.read_only_udm.additional.fields: Newly mapped log_data raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped spcb_id raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.extensions.auth.type: Newly mapped sso_status raw log field to event.idm.read_only_udm.extensions.auth.type.  
\- event.idm.read_only_udm.metadata.description: Newly mapped sso_status raw log field to event.idm.read_only_udm.metadata.description.  
\- event.idm.read_only_udm.metadata.id: Newly mapped id raw log field to event.idm.read_only_udm.metadata.id.  
\- event.idm.read_only_udm.network.http.method: Newly mapped http_method raw log field to event.idm.read_only_udm.network.http.method.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped Browser_type raw log field to event.idm.read_only_udm.network.http.user_agent and event.idm.read_only_udm.network.http.parsed_user_agent.  
\- event.idm.read_only_udm.network.session_duration.seconds: Newly mapped handshake_time raw log field to event.idm.read_only_udm.network.session_duration.seconds.  
\- event.idm.read_only_udm.network.tls.cipher: Newly mapped cipher_suite raw log field to event.idm.read_only_udm.network.tls.cipher.  
\- event.idm.read_only_udm.network.tls.version: Newly mapped client_version raw log field to event.idm.read_only_udm.network.tls.version.  
\- event.idm.read_only_udm.principal.ip: Newly mapped client_ip raw log field to event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip.  
\- event.idm.read_only_udm.principal.port: Newly mapped client_port raw log field to event.idm.read_only_udm.principal.port.  
\- event.idm.read_only_udm.security_result.description: Newly mapped session_type raw log field to event.idm.read_only_udm.security_result.description.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped event_type raw log field to event.idm.read_only_udm.security_result.summary.  
\- event.idm.read_only_udm.target.hostname: Newly mapped hostname_1 raw log field to event.idm.read_only_udm.target.hostname and event.idm.read_only_udm.target.asset.hostname.  
\- event.idm.read_only_udm.target.ip: Newly mapped vserver_ip raw log field to event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip.  
\- event.idm.read_only_udm.target.port: Newly mapped vserver_port raw log field to event.idm.read_only_udm.target.port.  
\- event.idm.read_only_udm.target.url: Newly mapped target_url raw log field to event.idm.read_only_udm.target.url.  
\- event.idm.read_only_udm.target.user.group_identifiers: Newly mapped user_group raw log field to event.idm.read_only_udm.target.user.group_identifiers.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped username raw log field to event.idm.read_only_udm.target.user.userid.  
\- event.idm.read_only_udm.target.ip: Newly mapped target_ip raw log field to event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip.  
\- event.idm.read_only_udm.target.port: Newly mapped target_port raw log field to event.idm.read_only_udm.target.port.   
2025-07-15 |  Enhancement:  
\- Modified Grok pattern to avoid parsing incorrect value to `event.idm.read_only_udm.principal.user.userid` raw log field.   
2025-07-01 |  Enhancement:  
\- Changes made in the include file :  
\- Added gsub to replace `Delink Time` with `delinkTime` on `message_data` field.  
\- Added grok pattern to extract ip address and port number from `NatIP` and `Vserver` raw log field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `Nat_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field for `CONN_DELINK` message types.  
\- event.idm.read_only_udm.principal.nat_port: Newly mapped `Nat_port` raw log field with `event.idm.read_only_udm.principal.nat_port` UDM field for `CONN_DELINK` message types.  
\- event.idm.read_only_udm.target.ip, event.idm.read_only_udm.target.asset.ip: Newly mapped `v_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field for `CONN_DELINK` message types.  
\- event.idm.read_only_udm.target.port: Newly mapped `v_port` raw log field with `event.idm.read_only_udm.target.port` UDM field for `CONN_DELINK` message types.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `delinkTime` raw log field with `event.idm.read_only_udm.additional.fields` UDM field for `CONN_DELINK` message types.   
2025-06-19 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field for `LOGIN` and `LOGOUT` message types.   
2025-04-14 |  Enhancement:  
\- Removed drop statement on kv failure to parse logs with non-utf characters.   
2025-04-03 |  Enhancement:  
\- Added a condition check before mapping `User` to `principal.user.userid`.  
\- Added a condition check before mapping `Command` to `target.process.command_line`.  
\- Added a condition to check if `has_prin_hostname` is `true` before setting the event_type to `PROCESS_UNCATEGORIZED`.  
\- Added a condition check if `User` is not equal to null before mapping `event_type` to `USER_UNCATEGORIZED`.   
2025-02-26 |  Enhancement:  
\- Changed mapping for `ClientIP` from `target.ip` to `principal.ip`.  
\- Mapped `intermediary_ip` to `intermediary.ip`.  
\- Removed invalid `target.user.userid` mappings for `SSLVPN Message` logs.  
\- Changed `metadata.event_type` from `USER_UNCATEGORIZED` to `PROCESS_UNCATEGORIZED` for `CMD_EXECUTED` logs.  
\- Changed `metadata.event_type` from `GENERIC_EVENT` to `USER_LOGIN` When `message_data` is `SSO: cached credentials`.  
\- Changed `metadata.event_type` from `NETWORK_CONNECTION` to `USER_LOGIN` for `REMOVE_SESSION_DEBUG` logs.  
\- Mapped `Remote_ip` to `target.ip`.  
\- Mapped `Username` to `principal.user.userid`.   
2025-02-25 |  Enhancement:  
\- Added a new Grok pattern to parse the logs.  
\- Mapped `Nat_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `VserverIP` to `src.ip`.  
\- Mapped `VserverPort` to `src.port`.  
\- Mapped `Start_time` to `sec_result.first_discovered_time`.  
\- Mapped `End_time` to `sec_result.last_discovered_time`.  
\- Mapped `target_port` to `target.port`.   
2025-02-24 |  Enhancement:  
\- Modified the Grok pattern to parse `intermediary.hostname`.   
2025-02-13 |  Enhancement:  
\- If the feature is `AAA` and the message type is `LOGIN_FAILED`, then `security_result.action` is mapped to `BLOCK`.  
\- If the feature is `SSLVPN` and the message type is `LOGIN`, then `security_result.action` is mapped to `ALLOW`.  
\- Mapped `User` to `target.user.userid` for `AAATM - LOGIN and LOGOUT` logs.   
2025-02-05 |  Enhancement:  
\- Added a Grok pattern to parse the logs.  
\- Mapped `prin_ip` to `principal.ip and principal.asset.ip`.  
\- Mapped `user_prin` to `principal.user.userid`.  
\- Mapped `SPCBId` to `security_result.detection_fields`  
\- Mapped `login_count` to `security_result.detection_fields`.  
\- Mapped `ica_conn_owner_refmask` to `security_result.detection_fields`.  
\- Mapped `session_id` to `network.session_id`.  
\- Mapped `sso_flags` to `security_result.detection_fields`.  
\- Mapped `copied_nsb` to `security_result.detection_fields`.  
\- Mapped `trans id` to `security_result.detection_fields`.   
2025-01-30 |  Enhancement:  
\- Added a Grok pattern to parse the log.  
\- Mapped `src` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `spt` to `principal.port`.  
\- Mapped `method` to `network.http.method`.  
\- Mapped `request` to `principal.url`.  
\- Mapped `msg` to `metadata.description`.  
\- Mapped `geolocation` to `principal.location.city`.  
\- Mapped `cn1` to `additional.fields`.  
\- Mapped `cn2` to `additional.fields`.  
\- Mapped `cs1` to `additional.fields`.  
\- Mapped `cs2` to `additional.fields`.  
\- Mapped `cs4` to `additional.fields`.  
\- Mapped `cs5` to `additional.fields`.  
\- Mapped `cs6` to `additional.fields`.  
\- Mapped `act` to `security_result.detection_fields`.   
2025-01-20 |  Enhancement:  
\- Added a Grok pattern to support new pattern of syslog logs.   
2025-01-16 |  Enhancement:  
\- Added the Grok pattern to support new format of syslog logs.  
\- Mapped `Client_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `ip_x` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `caseId` to `additional.fields`.  
\- Mapped `summ` to `security_result.summary`.  
\- Mapped `User` to `principal.user.userid`.  
\- Mapped `SessionId` to `network.session_id`.   
2025-01-14 |  Enhancement:  
\- Added conditional check for `principal_ip` and `target_ip`.  
\- Defined `session_guid`.   
2025-01-09 |  Enhancement:  
\- Modified the Grok pattern to support new format of syslog logs.  
\- When `principal_ip` and `target_ip` is then mapped `event_type` to NETWORK_CONNECTION.   
2025-01-02 |  Enhancement:  
\- Modified the Grok pattern to support new format of syslog logs.   
2024-12-19 |  Enhancement:  
\- Added support for new format of syslog logs.   
2024-12-05 |  Enhancement:  
\- Added support for new format of syslog logs.   
2024-11-21 |  Enhancement:  
\- Added support to parse new format of syslog logs.   
2024-11-07 |  Enhancement:  
\- Mapped `SubjectName` to null.  
\- Added support to parse logs where `message_type` is `REMOVE_SESSION_DEBUG`.  
\- Mapped `Errmsg` to `metadata.description`.  
\- Mapped `Sessionid` to `network.session_id`.  
\- Mapped `User` to `principal.user.userid`.  
\- Mapped `Client_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `Vserver_ip` to `target.ip` and `target.asset.ip`.   
2024-10-15 |  Enhancement:  
\- When `message_type` is equal to `LOGIN` then mapped `user_name` and `user` to `target.user.userid`.  
\- When `message_type` is equal to `LOGIN_FAILED` then mapped `User` to `principal.user.userid`.   
2024-10-11 |  Enhancement:  
\- Added `gsub` to parse the unparsed syslogs.   
2024-09-25 |  Enhancement:  
\- Added support to parse the new format of unparsed syslogs.   
2024-09-05 |  Enhancement:  
\- Mapped `VserverServiceIP` field to `target.ip` UDM field.  
\- Mapped `VserverServicePort` field to `target.port` UDM field.  
\- Mapped `ClientVersion` field to `network.tls.version_protocol` UDM field.  
\- Mapped `CipherSuite` field to `network.tls.cipher` UDM field.   
2024-08-14 |  Enhancement:  
\- Added a Grok pattern to extract `hostname` and mapped it to `intermediary.hostname`.  
\- Added a Grok pattern to extract `userid` and added conditional checks before mapping it to `target.user.userid`.   
2024-08-12 |  Enhancement:  
\- Added a Grok pattern to extract `userid` and mapped it to `principal.user.userid`.  
\- Added a Grok pattern to extract `principal_ip` and mapped it to `principal.ip`.  
\- Added a Grok pattern to extract `target_ip` and mapped it to `target.ip`.  
\- Added a Grok pattern to extract `principal_hostname` and mapped it to `principal.hostname`.  
\- Added a Grok pattern to extract `target_hostname` and mapped it to `target.hostname`.  
\- Modified the Grok pattern to parse `Authentication details`, `userid` and `error message`.  
\- Mapped `Authentication details` to `security_result.description`, `userid` to `principal.user.userid`, and `error message` to `security_result.detection_fields`  
2024-07-02 |  Enhancement:  
\- Modified a Grok pattern to parse dropped logs.  
\- Mapped the `Client_IP` to `additional.fields`.   
2024-05-21 |  Enhancement:  
\- Modified a Grok pattern to parse dropped logs.   
2024-05-20 |  Enhancement:  
\- Added new Grok pattern to parse unparsed logs.   
2024-05-08 |  Enhancement:  
\- Updated mapping of the duration information from `security_results` to `network.session_duration`.   
2024-04-29 |  Enhancement:  
\- Added conditional check for `Browser_type` and mapped it to `network.http.parsed_user_agent`.  
\- Added conditional check for `userId` and `user_email`.  
\- Mapped `Browser` to `network.http.parsed_user_agent`.   
2024-02-23 |  Enhancement:  
\- Updated Grok pattern to parse hostname as expected in the UDM field.   
2024-01-25 |  Enhancement:  
\- Added new Grok patterns to parse logs where `message_type` is `Message`, `NONHTTP_RESOURCEACCESS_DENIED`, `UDPFLOWSTAT`, and `EXTRACTED_GROUPS`.  
\- Added support to parse logs where `feature` is `GUI` and `EVENT`.  
\- Mapped `principal_port` to `principal.port`.  
\- Mapped `ClientIP` to `principal.asset.ip`.  
\- Mapped `principal_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `target_ip` to `target.ip` and `target.asset.ip`.  
\- Mapped `target_port` to `target.port`.  
\- Mapped `description` to `metadata.description`.  
\- Mapped `type`, `aaa_trans_id`, `pcb_trans_id`, `pcb_state`, `pcb_label`, `trans_id`, `authPolicyLen`, `login_attempts`, `PromptLen`, `partitionLen`, `cmdPolicyLen`, and `ssh_pubkey_len` to `security_result.detection_fields`.  
\- Mapped `principal_hostname` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `hostname` to `intermediary.asset.hostname`.  
\- Mapped `hostname` to `observer.asset.hostname`.  
\- Mapped `cip`, `ServerIP`, `VIP`, `VserverServiceIP`, and `Remote_ip` to `target.asset.ip`.  
\- When `message_type` is `Message`, then mapped `User` to `principal.user.userid`.  
\- When `principal_ip` and `target_ip` is present, then set `metadata.event_type` to `NETWORK_CONNECTION`.  
\- When `Client_ip` and `target_ip` is present, then set `metadata.event_type` to `NETWORK_CONNECTION`.  
\- When `message_type` is `NONHTTP_RESOURCEACCESS_DENIED` and `UDPFLOWSTAT`, then set `metadata.event_type` to `USER_STATS`.  
\- When `message_type` is `Message` and `User` is present, then set `metadata.event_type` to `USER_UNCATEGORIZED`.  
\- When `principal_ip` is present, then set `metadata.event_type` to `STATUS_UPDATE`.   
2023-11-26 |  Enhancement-  
\- Added new Grok patterns to parse logs where `message_type` is `Message`.   
2023-07-21 |  Enhancement - Updated the parser to correctly parse the logs containing feature - `CLI`.   
2022-09-26 |  Enhancement - Migrated custom parsers to default parser.   
2022-06-09 |  Enhancement- Added requested mappings:  
-Mapped `startTime`, `endTime`, `Duration` to `security_result.detection_fields`.  
-Updated the parser to parse the logs containing message_type - `CHANNEL_UPDATE`, `NETWORK_UPDATE`, `AAATM Message`.   
2022-05-09 |  Bug-fix - Updated the parser to correctly parse the logs containing message_type - `TCPCONNSTAT`.  
-Updated the grok to include the full domain name in `principal.administrative_domain`.  
-Parsed the logs failing during Validation API testing.   
2022-04-27 |  Enhancement- Added requested mappings  
-Mapped intermediary.hostname field  
-Parsed Api failed logs   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
