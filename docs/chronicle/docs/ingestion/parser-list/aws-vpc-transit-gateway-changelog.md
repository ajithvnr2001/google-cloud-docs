---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-vpc-transit-gateway-changelog/
title: Change log for AWS_VPC_TRANSIT_GATEWAY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:14:37.682445+00:00
---

# Change log for AWS_VPC_TRANSIT_GATEWAY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-vpc-transit-gateway-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_VPC_TRANSIT_GATEWAY

Date | Changes  
---|---  
2025-09-19 |  \- `event.idm.read_only_udm.principal.resource.attribute.labels`: Removed mapping of `tgw_src_subnet_id` from `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Mapped `tgw_src_subnet_id` raw log field to `event.idm.read_only_udm.principal.resource.name.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Removed mapping of `tgw_dst_subnet_id` from `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Mapped `tgw_dst_subnet_id` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Removed mapping of `tgw_src_eni` raw log field from `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Mapped `tgw_src_eni` raw log field to `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset_id`: Mapped `tgw_src_eni` raw log field to `event.idm.read_only_udm.principal.asset_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Removed mapping of `tgw_dst_eni` from `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.asset.asset_id`: Mapped `tgw_dst_eni` raw log field to `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.target.asset_id`: Mapped `tgw_dst_eni` raw log field to `event.idm.read_only_udm.target.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Removed mapping of `tgw_src_az_id` from `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Mapped `tgw_src_az_id` raw log field to `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Removed mapping of `tgw_dst_az_id` from `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Mapped `tgw_dst_az_id` raw log field to `event.idm.read_only_udm.target.location.country_or_region` UDM field if region is not null.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `tgw_src_az_id` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field if region is null.   
2025-08-19 |  \- Added a Grok pattern to parse the raw log fields for non-JSON formatted messages.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `tgw_dst_vpc_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `tgw_dst_subnet_id`, `tgw_dst_eni`, `pkt_dst_aws_service` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `srcaddr` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields and set `has_principal` to `true`.  
\- event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip: Newly mapped `dstaddr` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields and set `has_target` to `true`.  
\- event.idm.read_only_udm.principal.port: Newly mapped `srcport` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `dstport` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `protocol` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `start_time`, `type`, `packets_lost_no_route`, `packets_lost_blackhole`, `packets_lost_mtu_exceeded`, `packets_lost_ttl_expired`, `tcp_flags` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.sent_packets: Newly mapped `packets` raw log field with `event.idm.read_only_udm.network.sent_packets` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `log_status` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.network.direction: Newly mapped `flow_direction` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `end_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `pkt_src_aws_service` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Newly mapped `event_type` as `NETWORK_CONNECTION` when `has_principal` is `true` and `has_target` is `true` else if `STATUS_UPDATE` when `has_principal` is `true` and `has_target` is `false` else if `USER_RESOURCE_ACCESS` when `principal_user_present` is `true` and `target_user_present` is `true` else `GENERIC_EVENT`.   
2024-11-15 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
