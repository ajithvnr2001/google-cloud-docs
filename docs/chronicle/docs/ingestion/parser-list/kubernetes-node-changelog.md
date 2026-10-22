---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kubernetes-node-changelog/
title: Change log for KUBERNETES_NODE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:43.577543+00:00
---

# Change log for KUBERNETES_NODE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kubernetes-node-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for KUBERNETES_NODE

Date | Changes  
---|---  
2026-06-18 |  \- additional.fields[x_forwarded_for]: Newly mapped `jsonPayload.x_forwarded_for`, `x_forwarded_for` and `jsonPayload.httpRequest.x_forwarded_for` raw log fields with `additional.fields[x_forwarded_for]` UDM field.  
\- additional.fields[downstream_local_address]: Newly mapped `jsonPayload.downstream_local_address`, `jsonPayload.httpRequest.downstream_local_address` and `downstream_local_address` raw log fields with `additional.fields[downstream_local_address]` UDM field.   
2026-05-21 |  \- principal.ip: Newly mapped `jsonPayload.x_forwarded_for` raw log field with `principal.ip` UDM field.  
\- network.http.method: Corrected the mapping of `jsonPayload.method` to populate `network.http.method` instead of `additional.fields[method]`.   
2026-02-10 |  Added support for the following fields for the resource type `k8s_container`.  
\- additional.fields[actionI18nKey]: Newly mapped `jsonPayload.auditType.actionI18nKey` raw log field with `additional.fields[actionI18nKey]` UDM field for the resource type `k8s_container`.  
\- additional.fields[level]: Newly mapped `jsonPayload.auditType.level` raw log field with `additional.fields[level]` UDM field for the resource type `k8s_container`.  
\- additional.fields[action]: Newly mapped `jsonPayload.auditType.action` raw log field with `additional.fields[action]` UDM field for the resource type `k8s_container`.  
\- additional.fields[area]: Newly mapped `jsonPayload.auditType.area` raw log field with `additional.fields[area]` UDM field for the resource type `k8s_container`.  
\- additional.fields[date]: Newly mapped `jsonPayload.auditType.date` raw log field with `additional.fields[date]` UDM field for the resource type `k8s_container`.  
\- target.url: Newly mapped `jsonPayload.system` raw log field with `target.url` UDM field for the resource type `k8s_container`.  
\- principal.ip: Newly mapped `jsonPayload.source` raw log field with `principal.ip` UDM field for the resource type `k8s_container`.  
\- security_result.detection_fields[affected_object_%{index}_type]: Newly mapped `jsonPayload.affectedObjects.type` raw log field with `security_result.detection_fields[affected_object_%{index}_type]` UDM field for the resource type `k8s_container`.  
\- security_result.detection_fields[affected_object_%{index}_name]: Newly mapped `jsonPayload.affectedObjects.name` raw log field with `security_result.detection_fields[affected_object_%{index}_name]` UDM field for the resource type `k8s_container`.  
\- security_result.category_details: Newly mapped `jsonPayload.auditType.category` raw log field with `security_result.category_details` UDM field for the resource type `k8s_container`.  
\- security_result.category_details: Newly mapped `jsonPayload.auditType.categoryI18nKey` raw log field with `security_result.category_details` UDM field for the resource type `k8s_container`.   
2026-01-16 |  \- metadata.event_type: `metadata.event_type` is now set to `RESOURCE_CREATION` instead of `USER_RESOURCE_CREATION` when the `methodName` raw log is equal to `google.container.v1.ClusterManager.CreateNodePool`, `io.k8s.authorization.v1.subjectaccessreviews.create`, `google.monitoring.v3.MetricService.CreateServiceTimeSeries` or `google.container.v1beta1.ClusterManager.CreateCluster`.  
\- metadata.event_type: `metadata.event_type` is now set to `RESOURCE_DELETION` instead of `USER_RESOURCE_DELETION` when the `methodName` raw log is `google.container.v1.ClusterManager.DeleteCluster`.  
\- metadata.event_type: `metadata.event_type` is now set to `RESOURCE_READ` instead of `SCAN_UNCATEGORIZED` when the `methodName` raw log is `io.k8s.node.v1.runtimeclasses.watch`.  
\- metadata.event_type: `metadata.event_type` is now set to `RESOURCE_WRITTEN` instead of `USER_RESOURCE_UPDATE_CONTENT` when the `methodName` raw log is equal to `io.k8s.coordination.v1.leases.update`, or `io.k8s.authorization.rbac.v1.clusterrolebindings.patch`.   
2025-12-29 |  Modified the mapping logic for the following fields for the resource type `k8s_container` in order to introduce more accurate mappings.  
\- network.received_bytes: Modified logic to map `jsonPayload.bytes_received` raw log field with `network.received_bytes` UDM field for the resource type `k8s_container`.  
\- network.tls.client.server_name: Newly mapped jsonPayload.requested_server_name raw log field with network.tls.client.server_name UDM field if the raw log field labels.destination_service_host is present in the log.  
\- network.tls.client.server_name: Removed mapping of jsonPayload.requested_server_name from network.tls.client.server_name UDM field if the raw log field labels.destination_service_host is not present in the log.  
\- target.hostname: Mapped jsonPayload.requested_server_name raw log field with target.hostname UDM field if the raw log field labels.destination_service_host is not present in the log.   
2025-12-02 |  Added support for the following fields for the resource type `k8s_container`.  
\- additional.fields[caller]: Newly mapped `jsonPayload.caller` raw log field with `additional.fields[caller]` UDM field for the resource type `k8s_container`.  
\- metadata.description: Newly mapped `jsonPayload.msg` raw log field with `metadata.description` UDM field for the resource type `k8s_container`.  
\- about.resource.name: Newly mapped `jsonPayload.json.repo` raw log field with `about.resource.name` UDM field for the resource type `k8s_container`.  
\- about.resource.attributes.labels: Newly mapped `jsonPayload.json.pull` raw log field with `about.resource.attributes.labels` UDM field for the resource type `k8s_container`.   
2025-11-26 |  Added support for the following fields for the resource type `k8s_container`.  
\- metadata.event_type: Removed mapping of value `GENERIC_EVENT` from `metadata.event_type` UDM field and mapped the value `NETWORK_HTTP` instead if the raw log field `jsonPayload.protocol` contains the value `HTTP` and the required UDM fields for event validation are mapped for the resource type `k8s_container`.  
\- metadata.event_type: Newly mapped value `NETWORK_CONNECTION` with `metadata.event_type` UDM field if the required UDM fields for event validation are mapped for the resource type `k8s_container`.  
\- `principal.ip`: Newly mapped `jsonPayload.x_forwarded_for` raw log field with `principal.ip` UDM field for the resource type `k8s_container`.  
\- principal.ip: Newly mapped `ip_address` extracted from the `jsonPayload.downstream_remote_address` raw log field with `principal.ip` UDM field for the resource type `k8s_container`.  
\- principal.port: Newly mapped `port` extracted from the `jsonPayload.downstream_remote_address` raw log field with `principal.port` UDM field if the UDM field `principal.port` is not already mapped for the resource type `k8s_container`.  
\- additional.fields[downstream_remote_address]: Newly mapped `jsonPayload.downstream_remote_address` raw log field with `additional.fields[downstream_remote_address]` UDM field if the UDM field `principal.port` is already mapped for the resource type `k8s_container`.  
\- intermediary.ip: Newly mapped `ip_address` extracted from the `jsonPayload.downstream_local_address` raw log field with `intermediary.ip` UDM field for the resource type `k8s_container`.  
\- intermediary.port: Newly mapped `port` extracted from the `jsonPayload.downstream_local_address` raw log field with `intermediary.port` UDM field for the resource type `k8s_container`.  
\- target.ip: Newly mapped `ip_address` extracted from the `jsonPayload.upstream_host` raw log field with `target.ip` UDM field for the resource type `k8s_container`.  
\- target.port: Newly mapped `port` extracted from the `jsonPayload.upstream_host` raw log field with `target.port` UDM field if the UDM field `target.port` is not already mapped for the resource type `k8s_container`.  
\- additional.fields[upstream_host]: Newly mapped `jsonPayload.upstream_host` raw log field with `additional.fields[upstream_host]` UDM field if the UDM field `target.port` is already mapped for the resource type `k8s_container`.  
\- `network.http.response_code` \- Newly mapped `jsonPayload.response_code` raw log field with `network.http.response_code` UDM field if the raw log field `jsonPayload.status` is empty for the resource type `k8s_container`.  
\- network.session_duration: Newly mapped `jsonPayload.duration` raw log field with `network.session_duration` UDM field for the resource type `k8s_container`.  
\- network.received_bytes: Newly mapped `jsonPayload.received_bytes` raw log field with `network.received_bytes` UDM field for the resource type `k8s_container` if the UDM field `network.received_bytes` is not already mapped for the resource type `k8s_container`.  
\- security_result.detection_fields[response_flags]: Newly mapped `jsonPayload.response_flags` raw log field with `security_result.detection_fields[response_flags]` UDM field if the UDM field `network.received_bytes` is already mapped for the resource type `k8s_container`.  
\- target.resource_ancestors.name: Newly mapped `jsonPayload.upstream_cluster` raw log field with `target.resource_ancestors.name` UDM field for the resource type `k8s_container`.  
\- target.resource_ancestors.resource_type: Newly mapped value `CLUSTER` with `target.resource_ancestors.resource_type` UDM field if the raw log field `jsonPayload.upstream_cluster` is not empty for the resource type `k8s_container`.  
\- network.http.user_agent: Newly mapped `jsonPayload.user_agent` raw log field with `network.http.user_agent` UDM field if the raw log field `jsonPayload.http_user_agent` is empty for the resource type `k8s_container`.  
\- additional.fields[user_agent]: Newly mapped `jsonPayload.user_agent` raw log field with `additional.fields[user_agent]` UDM field if the raw log field `jsonPayload.http_user_agent` is not empty for the resource type `k8s_container`.  
\- network.application_protocol: Newly mapped value `HTTP` with `network.application_protocol` UDM field if the raw log field `jsonPayload.server_protocol` is empty and `jsonPayload.protocol` contains the value `HTTP` for the resource type `k8s_container`.  
\- additional.fields[protocol]: Newly mapped `jsonPayload.protocol` raw log field with `additional.fields[protocol]` UDM field if the raw log field `jsonPayload.server_protocol` is not empty for the resource type `k8s_container`.  
\- `network.tls.client.server_name`: Newly mapped `jsonPayload.requested_server_name` raw log field with `network.tls.client.server_name` UDM field for the resource type `k8s_container`.  
\- network.http.method: Newly mapped `jsonPayload.method` raw log field with `network.http.method` UDM field if UDM field `network.http.method` is not already mapped for the resource type `k8s_container`.  
\- `additional.fields[method]`: Newly mapped `jsonPayload.method` raw log field with `additional.fields[method]` UDM field if UDM field `network.http.method` is already mapped for the resource type `k8s_container`.  
\- additional.fields[response_code]: Newly mapped `jsonPayload.response_code` raw log field with `additional.fields[response_code]` UDM field if the raw log field `jsonPayload.status` is not empty for the resource type `k8s_container`.  
\- additional.fields[upstream_local_address]: Newly mapped `jsonPayload.upstream_local_address` raw log field with `additional.fields[upstream_local_address]` UDM field for the resource type `k8s_container`.  
\- additional.fields[start_time]: Newly mapped `jsonPayload.start_time` raw log field with `additional.fields[start_time]` UDM field for the resource type `k8s_container`.  
\- `additional.fields[response_code_details]`: Newly mapped `jsonPayload.response_code_details` raw log field with `additional.fields[response_code_details]` UDM field for the resource type `k8s_container`.  
\- `additional.fields[upstream_service_time]`: Newly mapped `jsonPayload.upstream_service_time` raw log field with `additional.fields[upstream_service_time]` UDM field for the resource type `k8s_container`.  
\- additional.fields[route_name]: Newly mapped `jsonPayload.route_name` raw log field with `additional.fields[route_name]` UDM field for the resource type `k8s_container`.   
2025-08-20 |  target.namespace: Removed mapping of `resource.labels.namespace_name` from `target.namespace` UDM field and mapped to `additional.fields` in order to prevent the feed namespace from being overwritten by the prebuilt parser.  
target.namespace: Removed mapping of `protoPayload.request.metadata.namespace` from `target.namespace` UDM field and mapped to `additional.fields` for the k8s_cluster `resource.type` in order to prevent the feed namespace from being overwritten by the prebuilt parser.  
target.namespace: Removed mapping of `labels.destination_namespace` from `target.namespace` for the UDM field and mapped to `additional.fields` for the k8s_container `resource.type` in order to prevent the feed namespace from being overwritten by the prebuilt parser.  
principal.namespace: Removed mapping of `labels.source_namespace` from `principal.namespace` for the UDM field and mapped to `additional.fields` for the k8s_container `resource.type` in order to prevent the feed namespace from being overwritten by the prebuilt parser.  
principal.namespace: Removed mapping of `jsonPayload.src.namespace` from `principal.namespace` for the UDM field and mapped to `additional.fields` for the k8s_node `resource.type` in order to prevent the feed namespace from being overwritten by the prebuilt parser.  
principal.namespace: Removed mapping of `jsonPayload.src.pod_namespace` from `principal.namespace` for the UDM field and mapped to `additional.fields` for the k8s_node `resource.type` in order to prevent the feed namespace from being overwritten by the prebuilt parser.  
target.namespace: Removed mapping of `jsonPayload.dest.pod_namespace` from `target.namespace` for the UDM field and mapped to `additional.fields` for the k8s_node `resource.type` in order to prevent the feed namespace from being overwritten by the prebuilt parser.  
target.namespace: Removed mapping of `jsonPayload.dest.namespace` from `target.namespace` for the UDM field and mapped to `additional.fields` for the k8s_node `resource.type` in order to prevent the feed namespace from being overwritten by the prebuilt parser.   
2025-07-29 |  `generic_node`: Added support for the event `generic_node` and relevant corresponding raw log fields.   
2024-10-11 |  Added Support jsonPayload.authority and jsonPayload.path to Kubernetes default parser.   
2024-05-22 |  Updated parser to map `security_result.action` UDM field conditionally.   
2024-05-01 |  Added additional mappings for deprecated `noun.labels`.   
2024-04-24 |  Added empty check for `role.description` and `protoPayload.request.roleRef.name` field.   
2024-01-03 |  Added support of additional UDM fields for NGINX logs based on the `textPayload` field.   
2023-12-13 |  Added mapping for additional raw log fields.   
2023-11-29 |  Added mapping for vulnerability fields.  
Aligned `principal/target.hostname` and `principal/target.asset.hostname` mapping.   
2023-08-16 |  Modify the parser to support dynamic labels.  
Added support to parse the log field `jsonPayload.httpRequest.x-forwarded-for`.   
2023-06-28 |  Promoted KUBERNETES_NODE parser to default.  
For the field mapping reference, see [https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kubernetes-node>Collect Kubernetes Node logs](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/<code).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
