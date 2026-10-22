---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/umbrella-dns-changelog/
title: Change log for UMBRELLA_DNS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:29.234634+00:00
---

# Change log for UMBRELLA_DNS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/umbrella-dns-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for UMBRELLA_DNS

Date | Changes  
---|---  
2026-03-17 |  Enhancement:  
\- Added a grok pattern on `identity` to extract `intermediary_ip` and `intermediary_port`.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `intermediary_ip` log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.port`: Newly mapped `intermediary_port` log field with `event.idm.read_only_udm.intermediary.port` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `_blocked_categories` (key: `blocked_categories`), `column14` (key: `rule_id`), `column15` (key: `destination_countries`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-12-17 |  Enhancement:  
\- event.idm.read_only_udm.about.resource.attribute.labels: Removed mapping of `query_name` from `event.idm.read_only_udm.about.resource.attribute.labels` UDM field which was previously mapped to deprecated field `about.labels` and is now mapped to `additional.fields` since that is a more appropriate field.   
2025-11-19 |  Enhancement:  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `identities`, and `identity` log fields to `event.idm.read_only_udm.principal.asset.hostname` UDM field.   
2025-11-14 |  Enhancement:  
\- event.idm.read_only_udm.about.labels: Removed mapping of `query_name` from `event.idm.read_only_udm.about.labels` UDM field as the UDM field is deprecated.  
\- event.idm.read_only_udm.about.resource.attribute.labels: Mapped `query_name` raw log field to `event.idm.read_only_udm.about.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `datachannel_id` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added conditional check when the `message` raw log field is CSV.   
2025-10-23 |  Enhancement:  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname: Newly mapped `policy_hostname` raw log field (from column 2) with `event.idm.read_only_udm.principal.hostname` UDM field and `event.idm.read_only_udm.principal.asset.hostname` UDM field when `column11` is `Networks` and `column12` is similar to `Sites` and `column2` not similar to `LAN`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `tags` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-10-09 |  Enhancement:  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `column14` log field to `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `column16`, `column11` log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added a new Grok pattern to parse `event.idm.read_only_udm.principal.user.email_addresses` UDM field correctly.   
2025-09-03 |  Enhancement:  
\- Added gsub to remove the trailing dot for `event.idm.read_only_udm.network.dns.questions.name` UDM field.  
\- event.idm.read_only_udm.network.dns.questions.name: Newly mapped `q_name` raw log field to `event.idm.read_only_udm.network.dns.questions.name` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `tapp` raw log field to `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `app` raw log field to `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `user_email` raw log field to `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.principal.url: Newly mapped `purl` raw log field to `event.idm.read_only_udm.principal.url` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `user` raw log field to `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `rule_id` raw log field to `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `dns_return_message` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `displayname` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `pip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `pip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `tip` raw log field to `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `tip` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `c_details` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `c_details2` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `c_details3` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `c_details4` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `c_details5` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `c_details6` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `c_details7` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `c_details8` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `c_details9` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.   
2025-08-26 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` : Newly mapped `column4` raw log field to `event.idm.read_only_udm.principal.hostname` UDM field and `event.idm.read_only_udm.principal.asset.hostname` UDM field and set `has_principal_ip_host` to `true`.  
\- Added a new mapping from the raw field `column5` to an intermediate field named `identity` and then mapped to `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name` : Newly mapped `column3` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.   
2025-08-22 |  \- event.idm.read_only_udm.principal.user.user_display_name: Newly Mapped `username` raw log field to `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly Mapped `email` raw log field to `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
when column4 does not have IP and column5 and column3 have IP then below mapping follows :  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `column3` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `column3` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly Mapped `column4` raw log field to `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly Mapped `column5` raw log field to `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly Mapped `column5` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.port: Newly Mapped `column6` raw log field to `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column7` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `column8` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly Mapped `column1` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
when column16 and column17 have IP then below mapping follows :  
\- event.idm.read_only_udm.principal.location.name: Newly Mapped `column4` raw log field to `event.idm.read_only_udm.principal.location.name` UDM field.  
\- event.idm.read_only_udm.principal.location.city: Newly Mapped `column12` raw log field to `event.idm.read_only_udm.principal.location.city` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly Mapped `column5` raw log field to `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `column16` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `column16` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly Mapped `column17` raw log field to `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly Mapped `column17` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly Mapped `column18` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `column20` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column22` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column23` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column24` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column25` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column26` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column27` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column28` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
when column5 and column6 have IP then below mapping follows :  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly Mapped `column1` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.namespace: Newly Mapped `column2` raw log field to `event.idm.read_only_udm.principal.namespace` UDM field.  
\- event.idm.read_only_udm.target.namespace: Newly Mapped `column3` raw log field to `event.idm.read_only_udm.target.namespace` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly Mapped `column4` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `column5` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `column5` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly Mapped `column6` raw log field to `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly Mapped `column6` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly Mapped `column7` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `column9` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column11` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column12` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column13` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column14` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column15` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column16` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly Mapped `column19` raw log field to `event.idm.read_only_udm.security_result.rule_id` UDM field.  
when column4 does not have IP and column14 and column15 have IP,which are the part of csvData (sub string of the message) then below mapping follows :  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly Mapped `column1` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly Mapped `column2` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.location.city: Newly Mapped `column11` raw log field to `event.idm.read_only_udm.principal.location.city` UDM field.  
\- event.idm.read_only_udm.principal.location.name: Newly Mapped `column12` raw log field to `event.idm.read_only_udm.principal.location.name` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `c_pip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `c_pip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly Mapped `c_tip` raw log field to `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly Mapped `c_tip` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly Mapped `column16` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `column18` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column19` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column20` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column21` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column22` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column23` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column24` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column25` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column26` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column27` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
when column4 does not have IP and column10 and column11 have IP then below mapping follows :  
\- event.idm.read_only_udm.metadata.product_event_type: Newly Mapped `column2` raw log field to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly Mapped `column8` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `column10_ip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `column10_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly Mapped `column11_ip` raw log field to `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly Mapped `column11_ip` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly Mapped `column12` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `column14` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column16` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column17` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column18` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column19` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column20` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column21` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
when column8 and column9 have IP then below mapping follows :  
\- event.idm.read_only_udm.metadata.product_event_type: Newly Mapped `column2` raw log field to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `column8_ip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `column8_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly Mapped `column9_ip` raw log field to `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly Mapped `column9_ip` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly Mapped `column10` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `column12` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column13` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column14` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column15` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column16` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column18` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column19` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column20` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column21` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
when column7 and column8 have IP then below mapping follows :  
\- event.idm.read_only_udm.metadata.product_event_type: Newly Mapped `column2` raw log field to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `column7` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `column7` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly Mapped `column8` raw log field to `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly Mapped `column8` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly Mapped `column9` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `column11` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column13` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column14` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column16` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column17` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column18` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
when column6 and column7 have IP then below mapping follows :  
\- event.idm.read_only_udm.metadata.product_event_type: Newly Mapped `column2` raw log field to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `column6` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `column6` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly Mapped `column7` raw log field to `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly Mapped `column7` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly Mapped `column8` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `column10` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column12` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column13` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column14` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column15` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column16` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column17` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column19` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column20` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
when column7 have IP and column3 have email then below mapping follows :  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly Mapped `column3` raw log field to `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `column7` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `column7` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column4` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column5` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `column6` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
when column4 contains `create` word and column5 have IP then below mapping follows :  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `column5` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `column5` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly Mapped `column3` raw log field to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly Mapped `userid` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.   
2025-01-08 |  Enhancement:  
\- Added a new GROK pattern to parse SYSLOG data.  
\- Added a new Grok pattern for the fields `responsecode` and `_internalip`  
2024-05-28 |  Enhancement:  
\- Mapped `dns_record_type` to `additional.fields`.   
2024-03-05 |  Bug-Fix:  
\- Added a new Grok pattern to check if `column3` is having `internal_ip` and `internal_port`.  
\- Added support for Network Tunnel CSV logs.  
\- Mapped `rule_id` to `security_result.rule_id`.  
\- Mapped `dstport` to `target.port`.  
\- Mapped `srcPort` to `principal.port`.  
\- Mapped `_internalip` to `principal.ip`.  
\- Mapped `dstip` to `target.ip`.  
\- Mapped `direction` to `network.direction`.  
\- Mapped `tunnel_name` to `additional.fields`.  
\- Mapped `tunnel_type` to `metadata.product_event_type`.  
\- Mapped `origin_id` to `metadata.product_log_id`.  
\- Mapped `received_bytes` to `network.received_bytes`.  
\- Aligned mappings for `principal.ip` and `principal.asset.ip`.  
\- Aligned mappings for `target.ip` and `target.asset.ip`.   
2023-11-07 |  Enhancement:  
\- Mapped `first_name` to `principal.user.first_name` when `identityType` is `AD Users`.  
\- Mapped `last_name` to `principal.user.last_name` when `identityType` is `AD Users`.  
\- Added JSON mapping for `_identity_types` to support new pattern of `identity` value in logs.   
2023-09-29 |  Enhancement:  
\- Mapped `returncode` to `network.dns.response_code`.  
\- Mapped `querytype` to `network.dns.question.type`.  
\- Mapped `type` to `additional.fields`.  
\- Mapped `categories` to `security_result.category_details`.  
\- Mapped `verdict` to `security_result.action` and `security_result.action_details`.  
\- Mapped `amp.disposition` to `security_result.detection_fields`.  
\- Mapped `amp.malware` to `security_result.detection_fields`.  
\- Mapped `amp.score` to `security_result.detection_fields`.  
\- Mapped `policy.rulesetid` to `security_result.detection_fields`.  
\- Mapped `requestsize` to `network.sent_bytes`.  
\- Mapped `responsesize` to `network.received_bytes`.  
\- Mapped `fileName` to `target.file.names`.  
\- Mapped `responsefilename` to `network.http.method`.  
\- Mapped `statuscode` to `network.http.response_code`  
\- Mapped `tenantcontrols`, `securityoverridden`, and `forwardingmethod` to `additional.fields`.   
2022-05-17 |  Enhancement-Added conditional checks for `security_result.action`.   
2022-04-13 |  Enhancement: Parsed IP logs And Proxy Logs which were dropped earlier.   
2022-03-23 |  Enhancement-Added new field mapping.  
DNS Lookup Type mapped to labels.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
