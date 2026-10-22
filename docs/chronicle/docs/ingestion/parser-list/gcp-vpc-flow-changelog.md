---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-vpc-flow-changelog/
title: Change log for GCP_VPC_FLOW \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:49.255849+00:00
---

# Change log for GCP_VPC_FLOW  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-vpc-flow-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GCP_VPC_FLOW

Date | Changes  
---|---  
2026-09-25 |  Enhancement:  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Removed mapping of `src_instance.vm_name` from `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field if `jsonPayload.reporter` is `SRC`.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Mapped `src_instance.vm_name` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.location.city`: Removed mapping of `jsonPayload.dest_location.city` from `event.idm.read_only_udm.principal.location.city` UDM field as it is related to target location.  
\- `event.idm.read_only_udm.target.location.city`: Mapped `jsonPayload.dest_location.city` raw log field with `event.idm.read_only_udm.target.location.city` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Removed mapping of `jsonPayload.dest_location.country` from `event.idm.read_only_udm.principal.location.country_or_region` UDM field as it is related to target location.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Mapped `jsonPayload.dest_location.country` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.location.state`: Removed mapping of `jsonPayload.dest_location.region` from `event.idm.read_only_udm.principal.location.state` UDM field as it is related to target location field.  
\- `event.idm.read_only_udm.target.location.state`: Mapped `jsonPayload.dest_location.region` raw log field with `event.idm.read_only_udm.target.location.state` UDM field.  
\- `event.idm.read_only_udm.target.location.name`: Removed mapping of `jsonPayload.src_instance.region` from `event.idm.read_only_udm.target.location.name` UDM field as it is related to principal related field.  
\- `event.idm.read_only_udm.principal.location.name`: Mapped `jsonPayload.src_instance.region` raw log field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.target.namespace`: Removed mapping of `jsonPayload.src_vpc.project_id` from `event.idm.read_only_udm.target.namespace` UDM field as it is related to principal related field.  
\- `event.idm.read_only_udm.principal.namespace`: Mapped `jsonPayload.src_vpc.project_id` raw log field with `event.idm.read_only_udm.principal.namespace` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Removed mapping of `resource.labels.subnetwork_id` from `event.idm.read_only_udm.target.user.attribute.labels` UDM field as it is related to target related fields.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `jsonPayload.dest_instance.project_id`, `jsonPayload.dest_instance.zone` from `event.idm.read_only_udm.additional.fields` UDM field as it is related to target related fields.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `jsonPayload.dest_vpc.subnetwork_name`, `jsonPayload.dest_vpc.subnetwork_region` from `event.idm.read_only_udm.security_result.detection_fields` UDM field as it is related to target related fields.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `resource.labels.subnetwork_id`, `jsonPayload.dest_instance.project_id`, `jsonPayload.dest_instance.zone`, `jsonPayload.dest_vpc.subnetwork_name`, `jsonPayload.dest_vpc.subnetwork_region`, `jsonPayload.dest_gateway.interconnect_name`, `jsonPayload.dest_gateway.interconnect_project_number`, `jsonPayload.dest_gateway.location`, `jsonPayload.dest_gateway.name`, `jsonPayload.dest_gateway.project_id`, `jsonPayload.dest_gateway.type`, `jsonPayload.dest_gateway.vpc.project_id`, `jsonPayload.dest_gateway.vpc.vpc_name` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `jsonPayload.dest_instance.vm_name` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `jsonPayload.src_instance.project_id`, `jsonPayload.src_instance.zone`, `jsonPayload.src_vpc.subnetwork_name`, `jsonPayload.src_vpc.subnetwork_region`, `jsonPayload.src_instance.managed_instance_group.name`, `jsonPayload.src_instance.managed_instance_group.zone`, `jsonPayload.src_instance.managed_instance_group.region` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `jsonPayload.round_trip_time.median_msec`, `jsonPayload.one_way_network_latencies.median_msec`, `jsonPayload.one_way_network_latency_jitter.median_msec` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.direction`: If `jsonPayload.reporter` is `SRC`, updated the value of `event.idm.read_only_udm.network.direction` to `OUTBOUND`.   
2026-09-02 |  Enhancement:  
\- Removed redundant `grok` block for parsing `jsonPayload.end_time` to timestamp processing and directly parsed it using the `date` filter.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `jsonPayload.bytes_sent` (when value is `0`), `jsonPayload.load_balancing.backend_service_name`, `jsonPayload.load_balancing.backend_service_project_id`, `jsonPayload.load_balancing.forwarding_rule_name`, `jsonPayload.load_balancing.forwarding_rule_project_id`, `jsonPayload.load_balancing.reporter`, `jsonPayload.load_balancing.scheme`, `jsonPayload.load_balancing.type`, `jsonPayload.load_balancing.vpc.project_id`, `jsonPayload.load_balancing.vpc.vpc_name`, `jsonPayload.reporter`, `jsonPayload.dest_instance.project_id`, `jsonPayload.dest_instance.zone` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `jsonPayload.dest_vpc.subnetwork_name`, `jsonPayload.dest_vpc.subnetwork_region` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `resource.labels.subnetwork_name` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `jsonPayload.start_time` raw log field to `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.   
2025-07-31 |  Enhancement -  
\- Refactor the code to swap the values of principal.* and target.* fields (ip, asset.ip, port) when network.direction == `INBOUND` and jsonPayload.reporter == `DEST`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `jsonPayload.rtt_msec` raw log field with `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `jsonPayload.src_google_service.type` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `jsonPayload.dest_gke_details.service.service_name`,`jsonPayload.dest_gke_details.service.service_namespace` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Added a conditional checks of `jsonPayload.reporter` not equals to `DEST`.  
\- event1.idm.read_only_udm.target.ip, event1.idm.read_only_udm.target.asset.ip: Newly mapped `principal.ip` field with `event1.idm.read_only_udm.target.ip` and `event1.idm.read_only_udm.target.asset.ip` if `network.direction` is `INBOUND` and `jsonPayload.reporter` is `DEST`.  
\- event1.idm.read_only_udm.principal.ip, event1.idm.read_only_udm.principal.asset.ip: Newly mapped `target.ip` field with `event1.idm.read_only_udm.principal.ip` and `event1.idm.read_only_udm.principal.asset.ip` if `network.direction` is `INBOUND` and `jsonPayload.reporter` is `DEST`.  
\- event1.idm.read_only_udm.target.port : Newly mapped `principal.port` field with `event1.idm.read_only_udm.target.port` if `network.direction` is `INBOUND` and `jsonPayload.reporter` is `DEST`.  
\- event1.idm.read_only_udm.principal.port: Newly mapped `target.port` field with `event1.idm.read_only_udm.principal.port` if `network.direction` is `INBOUND` and `jsonPayload.reporter` is `DEST`.  
\- event1.idm.read_only_udm.target.ip, event1.idm.read_only_udm.target.asset.ip: Newly mapped `target.ip` field with `event1.idm.read_only_udm.target.ip` and `event1.idm.read_only_udm.target.asset.ip` if `network.direction` is `OUTBOUND` and `jsonPayload.reporter` is `DEST`.  
\- event1.idm.read_only_udm.principal.ip, event1.idm.read_only_udm.principal.asset.ip: Newly mapped `principal.ip` field with `event1.idm.read_only_udm.principal.ip` and `event1.idm.read_only_udm.principal.asset.ip` if `network.direction` is `OUTBOUND` and `jsonPayload.reporter` is `DEST`.  
\- event1.idm.read_only_udm.target.port : Newly mapped `target.port` field with `event1.idm.read_only_udm.target.port` if `network.direction` is `OUTBOUND` and `jsonPayload.reporter` is `DEST`.  
\- event1.idm.read_only_udm.principal.port: Newly mapped `principal.port` field with `event1.idm.read_only_udm.principal.port` if `network.direction` is `OUTBOUND` and `jsonPayload.reporter` is `DEST`.   
2024-10-24 |  Enhancement -  
\- Interchanged mapping of `principal.ip`, `principal.port` with `target.ip` and `target.port` respectively.   
2024-03-15 |  Enhancement -  
\- Mapped `jsonPayload.src_gke_details.pod.pod_namespace`, `jsonPayload.src_gke_details.pod.pod_name`,  
`jsonPayload.src_gke_details.cluster.cluster_name`, `jsonPayload.src_gke_details.cluster.cluster_location` to `principal.resource.attribute.labels`.  
\- Mapped `jsonPayload.dest_gke_details.pod.pod_namespace`, `jsonPayload.dest_gke_details.pod.pod_name`,  
`jsonPayload.dest_gke_details.cluster.cluster_name`, `jsonPayload.dest_gke_details.cluster.cluster_location` to `target.resource.attribute.labels`.   
2023-05-23 |  Enhancement -  
\- Mapped `metadata.event_type` to `USER_RESOURCE_ACCESS` when field `logName` does not contain `vpc_flows`.  
\- Mapped `timestamp` to `events.timestamp`.  
\- Mapped `textPayload`, `labels.tunnel_id` to `additional.fields`.  
\- Mapped `resource.labels.region` to `target.location.country_or_region`.  
\- Added null checks for various fields wherever required.   
2023-04-10 |  Enhancement -  
\- Set `target.resource.attribute.cloud.environment` to `GOOGLE_CLOUD_PLATFORM`.  
\- Set `target.resource.name` to the full resource name value.   
2022-07-22 |  Enhancement:  
\- Mapped `resource.labels.location` to `principal.location.name`.  
\- Mapped `resource.labels.subnetwork_id` to `target.user.attribute.labels`.  
\- Mapped `logName` to `security_result.category_details`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
