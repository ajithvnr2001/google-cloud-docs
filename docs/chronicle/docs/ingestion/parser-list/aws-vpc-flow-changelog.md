---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-vpc-flow-changelog/
title: Change log for AWS_VPC_FLOW \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:37:09.236827+00:00
---

# Change log for AWS_VPC_FLOW  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-vpc-flow-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_VPC_FLOW

Date | Changes  
---|---  
2026-06-05 |  Enhancement:  
\- Parser overhaul version to make it more efficient and increase fields coverage. You can see the full list of changes in the parser documentation page `https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-vpc-flow`.   
2026-05-18 |  Enhancement:  
\- Added new grok patterns to parse SYSLOG format logs.  
\- event.idm.read_only_udm.network.sent_bytes: Removed mapping of `bytes` from `event.idm.read_only_udm.network.sent_bytes` as the same data is already and more appropriately captured by the `event.idm.read_only_udm.network.received_bytes` field.  
\- event.idm.read_only_udm.network.dhcp.flags: Removed mapping of `tcp_flags` from `event.idm.read_only_udm.network.dhcp.flags` as TCP flags are not applicable to the DHCP protocol.  
\- event.idm.read_only_udm.additional.fields: Removed mapping of `protocol` raw log field with `event.idm.read_only_udm.additional.fields` UDM field as this information is already correctly and semantically mapped to `event.idm.read_only_udm.network.direction`.  
\- event.idm.read_only_udm.about.resource.attribute.labels: Mapped `flow_direction` raw log field with event.idm.read_only_udm.about.resource.attribute.labels UDM field.  
\- event.idm.read_only_udm.additional.fields: Mapped `tcp_flags` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.   
2026-03-02 |  Enhancement:  
\- Added a new grok pattern in order to parse the logs with SYSLOG format.  
\- Added a conditional check for `tcp_flags`.  
\- `event.idm.read_only_udm.principal.cloud.availability_zone`: Removed mapping of `tgw_src_az_id_zone`,`Az_id`,`az_id` from `event.idm.read_only_udm.principal.cloud.availability_zone` UDM field. As it is a deprecated field.  
\- `event.idm.read_only_udm.principal.location.name`: Mapped `tgw_src_az_id_zone`,`Az_id`,`az_id` raw log field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.principal.cloud.vpc.id`: Removed mapping of `Vpc_id`,`vpcID`,`tgw_src_vpc_id` from `event.idm.read_only_udm.principal.cloud.vpc.id` UDM field. As it is a deprecated field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `Vpc_id`,`vpcID`,`tgw_src_vpc_id` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.cloud.vpc.id`: Removed mapping of `tgw_dst_vpc_id` from `event.idm.read_only_udm.target.cloud.vpc.id` UDM field. As it is a deprecated field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `tgw_dst_vpc_id` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2025-11-14 |  Enhancement:  
\- Added a new Grok pattern to parse a new pattern of logs.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `interface_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `src_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dst_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `direction` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dst_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `region` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `DeviceType` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.   
2025-11-13 |  Enhancement:  
\- Added a new Grok pattern to parse a new pattern of logs.   
2025-10-15 |  Enhancement:  
\- Added Grok patterns to parse the logs.  
\- Added a conditional check `pkt_dstaddr_ip` is not equal to `dstaddr` before mapping `pkt_dstaddr_ip` to `intermediary.ip`.  
\- Added a conditional check `pkt_srcaddr_ip` is not equal to `srcaddr` before mapping `pkt_srcaddr_ip` to `intermediary.ip`.   
2025-09-03 |  Enhancement:  
\- Added Grok patterns to parse the unparsed logs.  
\- event.idm.read_only_udm.principal.cloud.availability_zone: Mapped `tgw_src_az_id_zone` raw log field with `event.idm.read_only_udm.principal.cloud.availability_zone` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.cloud.availability_zone: Mapped `tgw_dst_az_id_zone` raw log field with `event.idm.read_only_udm.target.resource.attribute.cloud.availability_zone` UDM field.   
2025-06-25 |  Enhancement:  
\- Added Grok patterns to parse the unparsed logs.  
\- event.idm.read_only_udm.about.resource.attribute.labels: Removed mapping of `interfaceId` from `event.idm.read_only_udm.about.resource.attribute.labels` UDM field because `interfaceId` is associated with the user's unique identifier.  
\- event.idm.read_only_udm.principal.user.product_object_id: Mapped `interfaceId` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Removed mapping of `vpcID` from `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field because `vpcID` represents the unique identifier for a Virtual Private Cloud.  
\- event.idm.read_only_udm.principal.cloud.vpc.id: Mapped `vpcID` raw log field with `event.idm.read_only_udm.principal.cloud.vpc.id` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels: Removed mapping of `subnetID` from `event.idm.read_only_udm.about.resource.attribute.labels` UDM field because `subnetID` is a unique identifier within a specific network or cloud environment.  
\- event.idm.read_only_udm.principal.asset_id: Mapped `subnetID` raw log field with `event.idm.read_only_udm.principal.asset_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Removed mapping of `packets` and `pckts` from `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.sent_packets: Mapped `packets` and `pckts` raw log field with `event.idm.read_only_udm.network.sent_packets` UDM field because it is the number of network packets sent during a communication event.  
\- event.idm.read_only_udm.additional.fields: Removed mapping of `bytes` from `event.idm.read_only_udm.additional.fields` UDM field as it is already getting mapped in `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.network.direction: Newly mapped `flow_direction` raw log field with `event.idm.read_only_udm.network.direction` UDM field as INBOUND when `flow_direction` is `ingress` and as OUTBOUND when `flow_direction` is `egress`.  
\- event.idm.read_only_udm.about.resource.attribute.labels: Removed mapping of `Tcp_flags` from `event.idm.read_only_udm.about.resource.attribute.labels` UDM field because 'Tcp_flags. describes network protocol details, not attributes of a separate resource entity.  
\- event.idm.read_only_udm.network.dhcp.flags: Mapped `Tcp_flags` raw log field with `event.idm.read_only_udm.network.dhcp.flags` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels: Removed mapping of `traffic_path` from `event.idm.read_only_udm.about.resource.attribute.labels` UDM field because it represents a general, unstructured detail not fitting a specific UDM entity or attribute..  
\- event.idm.read_only_udm.additional.fields: Mapped `traffic_path` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-06-06 |  Enhancement:  
\- event.idm.read_only_udm.about.resource.attribute.labels: Removed mapping of `traffic_path` from `event.idm.read_only_udm.about.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Mapped `traffic_path` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Removed mapping of `tgw_src_eni` and `tgw_src_subnet_id` from `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.user.product_object_id: Mapped `tgw_src_eni` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field  
\- event.idm.read_only_udm.target.resource.attribute.labels: Removed mapping of `tgw_dst_eni` and `tgw_dst_subnet_id` from `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.user.product_object_id: Mapped `tgw_dst_eni` raw log field with `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.asset_id: Mapped `tgw_src_subnet_id` raw log field with `event.idm.read_only_udm.principal.asset_id` UDM field  
\- event.idm.read_only_udm.target.asset_id: Mapped `tgw_dst_subnet_id` raw log field with `event.idm.read_only_udm.target.asset_id` UDM field.  
\- event.idm.read_only_udm.principal.resource.product_object_id: Removed mapping of `tgw_src_vpc_id` from `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.cloud.vpc.id: Mapped `tgw_src_vpc_id` raw log field with `event.idm.read_only_udm.principal.cloud.vpc.id` UDM field  
\- event.idm.read_only_udm.target.resource.product_object_id: Removed mapping of `tgw_dst_vpc_id` from `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.cloud.vpc.id: Mapped `tgw_dst_vpc_id` raw log field with `event.idm.read_only_udm.target.cloud.vpc.id` UDM field  
\- If `tcp_flags` is equal to `tcp-flags` then mapped `tcp_flags` to `additional.fields` UDM field else map `tcp_flags` to `event.idm.read_only_udm.network.dhcp.flags`.   
2025-05-22 |  Enhancement:  
\- Modified the Grok patterns to parse the `vpcID` raw log field.  
\- Removed the Grok pattern where `vpcID` is equal to null.  
\- Added Grok patterns to parse the raw logs.  
\- Added gsub replace `\\n` with "".  
\- Added a conditional check if `srcaddr`, `dstaddr`, `srcport` and `protocol` not equals to null or `-` .  
\- Added a conditional check if `protocol` not equals to null or `-` before mapping `UNKNOWN_IP_PROTOCOL` to `event.idm.read_only_udm.network.ip_protocol`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `action` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-04-29 |  Enhancement:  
\- Added a Grok pattern to parse `vpcID` raw log field.   
2025-04-22 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `Start` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `start_time_dt` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `Start_time_dt` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `start_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `start` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-03-07 |  Enhancement:  
\- Modified a Grok pattern to parse droped logs.  
\- Added gsub to remove the extra part from Region field.   
2025-02-14 |  Enhancement:  
\- Added a fix to map `interfaceId` to `about.resource.attribute.labels`.   
2025-02-05 |  Enhancement:  
\- If `flow_direction` is `ingress` then mapped `packets` to `network.received_packets`.  
\- If `flow_direction` is `ingress` then mapped `traffic.packets` to `network.received_packets`.  
\- If `flow_direction` is `ingress` then mapped `Traffic.Packets` to `network.received_packets`.  
\- If `flow_direction` is `ingress` then mapped `byt` to `network.received_bytes`.  
\- If `flow_direction` is `ingress` then mapped `Traffic.Bytes` to `network.received_bytes`.  
\- If `flow_direction` is `ingress` then mapped `bytes` to `network.received_bytes`.  
\- If `flow_direction` is `egress` then mapped `packets` to `network.sent_packets`.  
\- If `flow_direction` is `egress` then mapped `traffic.packets` to `network.sent_packets`.  
\- If `flow_direction` is `egress` then mapped `Traffic.Packets` to `network.sent_packets`.  
\- If `flow_direction` is `egress` then mapped `byt` to `network.sent_bytes`.  
\- If `flow_direction` is `egress` then mapped `Traffic.Bytes` to `network.sent_bytes`.  
\- If `flow_direction` is `egress` then mapped `bytes` to `network.sent_bytes`.   
2025-01-31 |  Enhancement:  
\- Changed mappings of `Instance_id`, `instance_id` and `InstanceID` from `principal.cloud.project.id` to `principal.resource_ancestors.product_object_id`.  
\- Changed mappings of `Vpc_id` and `vpcID` from `principal.cloud.vpc.id` to `principal.resource.attribute.labels`.   
2025-01-13 |  Enhancement:  
\- Added a new Grok pattern to parse the unparsed logs.   
2024-12-27 |  Enhancement:  
\- Added a Grok pattern to parse logs in proper format.  
\- Mapped `protocol_code` to `additional.fields`.   
2024-12-20 |  Enhancement:  
\- Added a Grok pattern to parse the unparsed logs.   
2024-12-05 |  Enhancement:  
\- Added Grok patterns to parse the unparsed logs.  
\- Mapped `tgw-id`, `tgw-attachment-id`, `tgw-pair-attachment-id`, `packets-lost-no-route`, `packets-lost-blackhole`, `packets-lost-mtu-exceeded`, `packets-lost-ttl-expired`, `packets`, `start-time`, `end-time`, and `bytes` to `additional.fields`.  
\- Mapped `resource_type` to `principal.resource.resource_type`.  
\- Mapped `tgw_src_vpc_account_id` to `principal.user.userid`.  
\- Mapped `tgw_dst_vpc_account_id` to `target.user.userid`.  
\- Mapped `tgw_src_eni` and `tgw-src-az-id` to `principal.resource.attribute.labels`.  
\- Mapped `tgw-dst-eni` and `tgw-dst-az-id` to `target.resource.attribute.labels`.  
\- Mapped `tgw-src-subnet-id` to `principal.resource.attribute.labels`.  
\- Mapped `tgw-dst-subnet-id` to `target.resource.attribute.labels`.  
\- Mapped `tgw_src_vpc_id` to `principal.resource.product_object_id`.  
\- Mapped `tgw_dst_vpc_id` to `target.resource.product_object_id`.  
\- Mapped `type`, `flow_direction`, and `instance_id` to `about.resource.attribute.labels`.   
2024-10-30 |  Enhancement:  
\- Mapped `Metadata.Product.version` to `metadata.product_version`.  
\- Mapped `cloud.zone` to `target.resource.attribute.cloud.availability_zone`.  
\- Mapped `cloud.provider` to `target.resource.attribute.cloud.environment`.  
\- Mapped `src_endpoint.port` to `principal.port`.  
\- Mapped `src_endpoint.ip` to `principal.ip`.  
\- Mapped `dst_endpoint.port` to `target.port`.  
\- Mapped `dst_endpoint.ip` to `target.ip`.  
\- Mapped `metadata.product.feature.name`, `metadata.profiles`, `metadata.version`, `cloud.account.uid`, `cloud.region`, `src_endpoint.interface_uid`, `src_endpoint.vpc_uid`, `src_endpoint.instance_uid`, `src_endpoint.subnet_uid` to `additional.fields`.  
\- Mapped `dst_endpoint.interface_uid`, `dst_endpoint.vpc_uid`, `dst_endpoint.instance_uid`, and `dst_endpoint.subnet_uid` to `additional.fields`.  
\- Mapped `connection_info.protocol_num` to `network.ip_protocol`.  
\- Mapped `connection_info.direction` to `network.direction`.  
\- Mapped `severity_id` to `security_result.severity`.  
\- Mapped `category_name` to `security_result.category_details`.  
\- Mapped `activity_name` to `metadata.product_event_type`.   
2024-10-01 |  Enhancement:  
\- Added support for new unparsed logs of type AWS_VPC_FLOW.   
2024-07-31 |  Enhancement:  
\- Added support for JSON format logs.   
2023-04-06 |  Enhancement - Mapped `metadata.event_type` to `GENERIC_EVENT` where both `srcaddr` and `dstaddr` is not present.   
2022-10-18 |  Enhancement - Modified mapping for the value of following fields from `additional.fields` to `about.resource.attribute.labels` :  
\- `interfaceId` , `packets` , `SubnetID` , `logStatus` ,`tcp_flags` ,`traffic_path` ,`start_time` ,`end_time`, `sublocation_id`,`sublocation_type` ,`pkt_dst_aws_service` ,`pkt_src_aws_service`.  
\- Added grok pattern to parse logs in which `destination_port` might not be present.   
2022-07-07 |  Enhancement - The newly ingested SYSLOG format logs have been parsed and handled using proper grok pattern.   
2022-05-30 |  Enhancement - Modified the grok pattern to avoid incorrect mapping of UDM fields.  
Mapped `start_time`, `end_time`, `traffic_path`, `sublocation_id`, `sublocation_type`, `pkt_dst_aws_service` and `pkt_src_aws_service` to `additional.fields`.  
Added a new grok pattern to parse the logs of different format.  
Mapped `flow_direction` to `network.direction`.  
Mapped `az_id` to `principal.cloud.availability_zone`.  
Mapped `pkt_srcaddr`, `pkt_dstaddr` to `intermediary.ip`.   
2022-05-05 |  Enhancement - Updated mapping for the field `accountId` from `principal.user.userid` to `metadata.product_log_id`.  
Mapped the field `version` to `metadata.product_version`.  
Mapped the field `end` to `metadata.ingested_timestamp`.  
Mapped `action` to `security_result.action` and `security_result.action_details`.  
Mapped the field `interfaceId`, `packets`, `SubnetID`, `logStatus`, `tcp_flags` to `additional.fields`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
