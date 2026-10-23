---
url: https://docs.cloud.google.com/monitoring/api/metrics_istio/
title: Istio metrics \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:09.050531+00:00
---

# Istio metrics  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/metrics_istio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Istio metrics Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Monitoring collects the metric types from Cloud Service Mesh and Istio on Google Kubernetes Engine services listed in this document.

## About the tables of metrics

The tables of metrics provide formatted versions of the publicly available [metric descriptors](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor). This section provides additional information to help you interpret and use these descriptors.

  * For a general explanation of the entries in the tables, including information about values like `DELTA` and `GAUGE`, see [Metric types](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types).

To chart or monitor metric types with values of type `STRING`, you must use Monitoring Query Language (MQL), and you must convert the value into a numeric value. For information about MQL string-conversion methods, see [`String`](https://docs.cloud.google.com/monitoring/mql/reference#string-group).

  * For information about the units used in the metric lists, see the [`unit` field](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor.FIELDS.unit) in the `MetricDescriptor` reference.

  * For information about statements of the form “Sampled every _x_ seconds” and “After sampling, data is not visible for up to _y_ seconds”, see [Additional information: metadata](https://docs.cloud.google.com/monitoring/api/metrics#metadata).

  * The resource-hierarchy level tells you if the metric is written at the project, organization, or folder level(s). When the level is not specified in the metric descriptor, the metric writes at the project level by default.



  * For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).


  * For information about the meaning of launch stages such as `GA` (General Availability) and `BETA` (Preview), see [Product launch stages](https://cloud.google.com/products#product-launch-stages).



## Istio metrics

Metrics from [Istio for Google Cloud](https://cloud.google.com/learn/what-is-istio).

The following list was last generated at 2026-10-14 20:24:33 UTC. For more information about this process, see [ About the lists](https://docs.cloud.google.com/monitoring/api/metrics#generated).

### istio

Metrics from [Istio](https://istio.io/docs). Launch stages of these metrics: ALPHA BETA

The "metric type" strings in this table must be prefixed with `istio.io/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`control/config_convergence_latencies` ALPHA ** _(project)_**   
Config Convergence Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[istio_control_plane](https://docs.cloud.google.com/monitoring/api/resources#tag_istio_control_plane)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of latencies between config change and a proxy receiving all required configuration. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`revision`: Revision of the control plane instance that is being monitored.   
`control_plane_version`: Version (build tag) of the control plane instance that is being monitored.   
`control/config_event_count` ALPHA ** _(project)_**   
Config Event Count   
`DELTA`, `INT64`, `1`   
**[istio_control_plane](https://docs.cloud.google.com/monitoring/api/resources#tag_istio_control_plane)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Number of registry event count of resources watched by Istio control plane. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`revision`: Revision of the control plane instance that is being monitored.   
`control_plane_version`: Version (build tag) of the control plane instance that is being monitored.   
`operation`: Operation on the resources, possible values are "ADD", "UPDATE", "UPDATESAME", and "DELETE".   
`type`: Type of resource watched by Istio control plane, e.g. "DestinationRule", "VirtualService", "ServiceEntry".   
`control/config_push_count` ALPHA ** _(project)_**   
Config Push Count   
`DELTA`, `INT64`, `1`   
**[istio_control_plane](https://docs.cloud.google.com/monitoring/api/resources#tag_istio_control_plane)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Number of control plane config pushes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`revision`: Revision of the control plane instance that is being monitored.   
`control_plane_version`: Version (build tag) of the control plane instance that is being monitored.   
`success`: (BOOL) Result of the config push.   
`type`: Istio proxy XDS resource type, possible values are "CDS", "EDS", "LDS", and "RDS".   
`control/config_validation_count` ALPHA ** _(project)_**   
Config Validation Count   
`DELTA`, `INT64`, `1`   
**[istio_control_plane](https://docs.cloud.google.com/monitoring/api/resources#tag_istio_control_plane)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Number of control plane validation events. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`revision`: Revision of the control plane instance that is being monitored.   
`control_plane_version`: Version (build tag) of the control plane instance that is being monitored.   
`success`: (BOOL) Result of the configuration validation.   
`type`: Type of Istio configuration resource that being validated.   
`control/connected_clusters` ALPHA ** _(project)_**   
Connected Clusters   
`GAUGE`, `INT64`, `1`   
**[istio_control_plane](https://docs.cloud.google.com/monitoring/api/resources#tag_istio_control_plane)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Number of clusters managed by this control plane instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`revision`: Revision of the control plane instance that is being monitored.   
`control_plane_version`: Version (build tag) of the control plane instance that is being monitored.   
`cluster_type`: Type of cluster managed: [ "local", "remote" ]   
`control/proxy_clients` ALPHA ** _(project)_**   
Proxy Clients   
`GAUGE`, `INT64`, `1`   
**[istio_control_plane](https://docs.cloud.google.com/monitoring/api/resources#tag_istio_control_plane)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Number of proxy endpoints connected to this control plane instance. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`revision`: Revision of the control plane instance that is being monitored.   
`control_plane_version`: Version (build tag) of the control plane instance that is being monitored.   
`proxy_version`: Version of the connected proxy.   
`control/rejected_config_count` ALPHA ** _(project)_**   
Rejected Config Count   
`DELTA`, `INT64`, `1`   
**[istio_control_plane](https://docs.cloud.google.com/monitoring/api/resources#tag_istio_control_plane)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Number of invalid configurations rejected by proxy. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`revision`: Revision of the control plane instance that is being monitored.   
`control_plane_version`: Version (build tag) of the control plane instance that is being monitored.   
`type`: Istio proxy XDS resource type, possible values are "CDS", "EDS", "LDS", and "RDS".   
`control/sidecar_injection_count` ALPHA ** _(project)_**   
Sidecar Injection Count   
`DELTA`, `INT64`, `1`   
**[istio_control_plane](https://docs.cloud.google.com/monitoring/api/resources#tag_istio_control_plane)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Number of sidecar injection request count to control plane. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`revision`: Revision of the control plane instance that is being monitored.   
`control_plane_version`: Version (build tag) of the control plane instance that is being monitored.   
`success`: (BOOL) Result of sidecar injection operation.   
`service/client/connection_close_count` BETA ** _(project)_**   
Client Connection Close Count   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Cumulative number of connection close events handled by the client._   
`request_protocol`: Protocol of the request or connection (e.g. HTTP, gRPC, TCP).   
`service_authentication_policy`: Determines if Istio was used to secure communications between services and how. Currently supported values: "NONE", "MUTUAL_TLS".   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`destination_service_name`: Name of destination service.   
`destination_service_namespace`: Namespace of destination service.   
`destination_port`: (INT64) Port of the destination service.   
`source_principal`: Principal of the source workload instance.   
`source_workload_name`: Name of the source workload.   
`source_workload_namespace`: Namespace of the source workload.   
`source_owner`: Owner of the source workload instance (e.g. k8s Deployment).   
`destination_principal`: Principal of the destination workload instance.   
`destination_workload_name`: Name of the destination workload.   
`destination_workload_namespace`: Namespace of the destination workload.   
`destination_owner`: Owner of the destination workload instance (e.g. k8s Deployment).   
`source_canonical_service_name`: The canonical service name of the source workload instance.   
`destination_canonical_service_name`: The canonical service name of the destination workload instance.   
`source_canonical_service_namespace`: The canonical service namespace of the source workload instance.   
`destination_canonical_service_namespace`: The canonical service namespace of the destination workload instance.   
`source_canonical_revision`: The canonical service revision of the source workload instance.   
`destination_canonical_revision`: The canonical service revision of the destination workload instance.   
`proxy_version`: Version of the proxy.   
`service/client/connection_open_count` BETA ** _(project)_**   
Client Connection Open Count   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Cumulative number of connection open events handled by the client._   
`request_protocol`: Protocol of the request or connection (e.g. HTTP, gRPC, TCP).   
`service_authentication_policy`: Determines if Istio was used to secure communications between services and how. Currently supported values: "NONE", "MUTUAL_TLS".   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`destination_service_name`: Name of destination service.   
`destination_service_namespace`: Namespace of destination service.   
`destination_port`: (INT64) Port of the destination service.   
`source_principal`: Principal of the source workload instance.   
`source_workload_name`: Name of the source workload.   
`source_workload_namespace`: Namespace of the source workload.   
`source_owner`: Owner of the source workload instance (e.g. k8s Deployment).   
`destination_principal`: Principal of the destination workload instance.   
`destination_workload_name`: Name of the destination workload.   
`destination_workload_namespace`: Namespace of the destination workload.   
`destination_owner`: Owner of the destination workload instance (e.g. k8s Deployment).   
`source_canonical_service_name`: The canonical service name of the source workload instance.   
`destination_canonical_service_name`: The canonical service name of the destination workload instance.   
`source_canonical_service_namespace`: The canonical service namespace of the source workload instance.   
`destination_canonical_service_namespace`: The canonical service namespace of the destination workload instance.   
`source_canonical_revision`: The canonical service revision of the source workload instance.   
`destination_canonical_revision`: The canonical service revision of the destination workload instance.   
`proxy_version`: Version of the proxy.   
`service/client/received_bytes_count` BETA ** _(project)_**   
Client Received Bytes Count   
`CUMULATIVE`, `INT64`, `By`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Cumulative number of bytes received by the service as a client through connections._   
`request_protocol`: Protocol of the request or connection (e.g. HTTP, gRPC, TCP).   
`service_authentication_policy`: Determines if Istio was used to secure communications between services and how. Currently supported values: "NONE", "MUTUAL_TLS".   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`destination_service_name`: Name of destination service.   
`destination_service_namespace`: Namespace of destination service.   
`destination_port`: (INT64) Port of the destination service.   
`source_principal`: Principal of the source workload instance.   
`source_workload_name`: Name of the source workload.   
`source_workload_namespace`: Namespace of the source workload.   
`source_owner`: Owner of the source workload instance (e.g. k8s Deployment).   
`destination_principal`: Principal of the destination workload instance.   
`destination_workload_name`: Name of the destination workload.   
`destination_workload_namespace`: Namespace of the destination workload.   
`destination_owner`: Owner of the destination workload instance (e.g. k8s Deployment).   
`source_canonical_service_name`: The canonical service name of the source workload instance.   
`destination_canonical_service_name`: The canonical service name of the destination workload instance.   
`source_canonical_service_namespace`: The canonical service namespace of the source workload instance.   
`destination_canonical_service_namespace`: The canonical service namespace of the destination workload instance.   
`source_canonical_revision`: The canonical service revision of the source workload instance.   
`destination_canonical_revision`: The canonical service revision of the destination workload instance.   
`proxy_version`: Version of the proxy.   
`service/client/request_bytes` BETA ** _(project)_**   
Client Request Bytes   
`DELTA`, `DISTRIBUTION`, `By`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Distribution of outgoing request sizes from the service in bytes._   
`request_protocol`: Protocol of the request or connection (e.g. HTTP, gRPC, TCP).   
`service_authentication_policy`: Determines if Istio was used to secure communications between services and how. Currently supported values: "NONE", "MUTUAL_TLS".   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`destination_service_name`: Name of destination service.   
`destination_service_namespace`: Namespace of destination service.   
`destination_port`: (INT64) Port of the destination service.   
`source_principal`: Principal of the source workload instance.   
`source_workload_name`: Name of the source workload.   
`source_workload_namespace`: Namespace of the source workload.   
`source_owner`: Owner of the source workload instance (e.g. k8s Deployment).   
`destination_principal`: Principal of the destination workload instance.   
`destination_workload_name`: Name of the destination workload.   
`destination_workload_namespace`: Namespace of the destination workload.   
`destination_owner`: Owner of the destination workload instance (e.g. k8s Deployment).   
`source_canonical_service_name`: The canonical service name of the source workload instance.   
`destination_canonical_service_name`: The canonical service name of the destination workload instance.   
`source_canonical_service_namespace`: The canonical service namespace of the source workload instance.   
`destination_canonical_service_namespace`: The canonical service namespace of the destination workload instance.   
`source_canonical_revision`: The canonical service revision of the source workload instance.   
`destination_canonical_revision`: The canonical service revision of the destination workload instance.   
`proxy_version`: Version of the proxy.   
`request_operation`: Unique string used to identify the API method (if available) or HTTP Method.   
`api_version`: Version of the API.   
`response_code`: (INT64) Response code of the request according to protocol.   
`api_name`: Name of the API.   
`service/client/request_count` BETA ** _(project)_**   
Client Request Count   
`DELTA`, `INT64`, `1`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[istio_canonical_service](https://docs.cloud.google.com/monitoring/api/resources#tag_istio_canonical_service)**   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Number of requests sent by the service. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`request_protocol`: Protocol of the request or connection (e.g. HTTP, gRPC, TCP).   
`service_authentication_policy`: Determines if Istio was used to secure communications between services and how. Currently supported values: "NONE", "MUTUAL_TLS".   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`destination_service_name`: Name of destination service.   
`destination_service_namespace`: Namespace of destination service.   
`destination_port`: (INT64) Port of the destination service.   
`source_principal`: Principal of the source workload instance.   
`source_workload_name`: Name of the source workload.   
`source_workload_namespace`: Namespace of the source workload.   
`source_owner`: Owner of the source workload instance (e.g. k8s Deployment).   
`destination_principal`: Principal of the destination workload instance.   
`destination_workload_name`: Name of the destination workload.   
`destination_workload_namespace`: Namespace of the destination workload.   
`destination_owner`: Owner of the destination workload instance (e.g. k8s Deployment).   
`source_canonical_service_name`: The canonical service name of the source workload instance.   
`destination_canonical_service_name`: The canonical service name of the destination workload instance.   
`source_canonical_service_namespace`: The canonical service namespace of the source workload instance.   
`destination_canonical_service_namespace`: The canonical service namespace of the destination workload instance.   
`source_canonical_revision`: The canonical service revision of the source workload instance.   
`destination_canonical_revision`: The canonical service revision of the destination workload instance.   
`proxy_version`: Version of the proxy.   
`request_operation`: Unique string used to identify the API method (if available) or HTTP Method.   
`api_version`: Version of the API.   
`response_code`: (INT64) Response code of the request according to protocol.   
`api_name`: Name of the API.   
`service/client/response_bytes` BETA ** _(project)_**   
Client Response Bytes   
`DELTA`, `DISTRIBUTION`, `By`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Distribution of response sizes received by the service in bytes._   
`request_protocol`: Protocol of the request or connection (e.g. HTTP, gRPC, TCP).   
`service_authentication_policy`: Determines if Istio was used to secure communications between services and how. Currently supported values: "NONE", "MUTUAL_TLS".   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`destination_service_name`: Name of destination service.   
`destination_service_namespace`: Namespace of destination service.   
`destination_port`: (INT64) Port of the destination service.   
`source_principal`: Principal of the source workload instance.   
`source_workload_name`: Name of the source workload.   
`source_workload_namespace`: Namespace of the source workload.   
`source_owner`: Owner of the source workload instance (e.g. k8s Deployment).   
`destination_principal`: Principal of the destination workload instance.   
`destination_workload_name`: Name of the destination workload.   
`destination_workload_namespace`: Namespace of the destination workload.   
`destination_owner`: Owner of the destination workload instance (e.g. k8s Deployment).   
`source_canonical_service_name`: The canonical service name of the source workload instance.   
`destination_canonical_service_name`: The canonical service name of the destination workload instance.   
`source_canonical_service_namespace`: The canonical service namespace of the source workload instance.   
`destination_canonical_service_namespace`: The canonical service namespace of the destination workload instance.   
`source_canonical_revision`: The canonical service revision of the source workload instance.   
`destination_canonical_revision`: The canonical service revision of the destination workload instance.   
`proxy_version`: Version of the proxy.   
`request_operation`: Unique string used to identify the API method (if available) or HTTP Method.   
`api_version`: Version of the API.   
`response_code`: (INT64) Response code of the request according to protocol.   
`api_name`: Name of the API.   
`service/client/roundtrip_latencies` BETA ** _(project)_**   
Client Roundtrip Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[istio_canonical_service](https://docs.cloud.google.com/monitoring/api/resources#tag_istio_canonical_service)**   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Distribution of outgoing request round trip latency from the service. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`request_protocol`: Protocol of the request or connection (e.g. HTTP, gRPC, TCP).   
`service_authentication_policy`: Determines if Istio was used to secure communications between services and how. Currently supported values: "NONE", "MUTUAL_TLS".   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`destination_service_name`: Name of destination service.   
`destination_service_namespace`: Namespace of destination service.   
`destination_port`: (INT64) Port of the destination service.   
`source_principal`: Principal of the source workload instance.   
`source_workload_name`: Name of the source workload.   
`source_workload_namespace`: Namespace of the source workload.   
`source_owner`: Owner of the source workload instance (e.g. k8s Deployment).   
`destination_principal`: Principal of the destination workload instance.   
`destination_workload_name`: Name of the destination workload.   
`destination_workload_namespace`: Namespace of the destination workload.   
`destination_owner`: Owner of the destination workload instance (e.g. k8s Deployment).   
`source_canonical_service_name`: The canonical service name of the source workload instance.   
`destination_canonical_service_name`: The canonical service name of the destination workload instance.   
`source_canonical_service_namespace`: The canonical service namespace of the source workload instance.   
`destination_canonical_service_namespace`: The canonical service namespace of the destination workload instance.   
`source_canonical_revision`: The canonical service revision of the source workload instance.   
`destination_canonical_revision`: The canonical service revision of the destination workload instance.   
`proxy_version`: Version of the proxy.   
`request_operation`: Unique string used to identify the API method (if available) or HTTP Method.   
`api_version`: Version of the API.   
`response_code`: (INT64) Response code of the request according to protocol.   
`api_name`: Name of the API.   
`service/client/sent_bytes_count` BETA ** _(project)_**   
Client Sent Bytes Count   
`CUMULATIVE`, `INT64`, `By`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_pod](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod)** |  _Cumulative number of bytes sent by the service as a client through connections._   
`request_protocol`: Protocol of the request or connection (e.g. HTTP, gRPC, TCP).   
`service_authentication_policy`: Determines if Istio was used to secure communications between services and how. Currently supported values: "NONE", "MUTUAL_TLS".   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`destination_service_name`: Name of destination service.   
`destination_service_namespace`: Namespace of destination service.   
`destination_port`: (INT64) Port of the destination service.   
`source_principal`: Principal of the source workload instance.   
`source_workload_name`: Name of the source workload.   
`source_workload_namespace`: Namespace of the source workload.   
`source_owner`: Owner of the source workload instance (e.g. k8s Deployment).   
`destination_principal`: Principal of the destination workload instance.   
`destination_workload_name`: Name of the destination workload.   
`destination_workload_namespace`: Namespace of the destination workload.   
`destination_owner`: Owner of the destination workload instance (e.g. k8s Deployment).   
`source_canonical_service_name`: The canonical service name of the source workload instance.   
`destination_canonical_service_name`: The canonical service name of the destination workload instance.   
`source_canonical_service_namespace`: The canonical service namespace of the source workload instance.   
`destination_canonical_service_namespace`: The canonical service namespace of the destination workload instance.   
`source_canonical_revision`: The canonical service revision of the source workload instance.   
`destination_canonical_revision`: The canonical service revision of the destination workload instance.   
`proxy_version`: Version of the proxy.   
`service/server/connection_close_count` BETA ** _(project)_**   
Server Connection Close Count   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Cumulative number of connection close events handled by the server._   
`request_protocol`: Protocol of the request or connection (e.g. HTTP, gRPC, TCP).   
`service_authentication_policy`: Determines if Istio was used to secure communications between services and how. Currently supported values: "NONE", "MUTUAL_TLS".   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`destination_service_name`: Name of destination service.   
`destination_service_namespace`: Namespace of destination service.   
`destination_port`: (INT64) Port of the destination service.   
`source_principal`: Principal of the source workload instance.   
`source_workload_name`: Name of the source workload.   
`source_workload_namespace`: Namespace of the source workload.   
`source_owner`: Owner of the source workload instance (e.g. k8s Deployment).   
`destination_principal`: Principal of the destination workload instance.   
`destination_workload_name`: Name of the destination workload.   
`destination_workload_namespace`: Namespace of the destination workload.   
`destination_owner`: Owner of the destination workload instance (e.g. k8s Deployment).   
`source_canonical_service_name`: The canonical service name of the source workload instance.   
`destination_canonical_service_name`: The canonical service name of the destination workload instance.   
`source_canonical_service_namespace`: The canonical service namespace of the source workload instance.   
`destination_canonical_service_namespace`: The canonical service namespace of the destination workload instance.   
`source_canonical_revision`: The canonical service revision of the source workload instance.   
`destination_canonical_revision`: The canonical service revision of the destination workload instance.   
`proxy_version`: Version of the proxy.   
`service/server/connection_open_count` BETA ** _(project)_**   
Server Connection Open Count   
`CUMULATIVE`, `INT64`, `1`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Cumulative number of connection open events handled by the server._   
`request_protocol`: Protocol of the request or connection (e.g. HTTP, gRPC, TCP).   
`service_authentication_policy`: Determines if Istio was used to secure communications between services and how. Currently supported values: "NONE", "MUTUAL_TLS".   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`destination_service_name`: Name of destination service.   
`destination_service_namespace`: Namespace of destination service.   
`destination_port`: (INT64) Port of the destination service.   
`source_principal`: Principal of the source workload instance.   
`source_workload_name`: Name of the source workload.   
`source_workload_namespace`: Namespace of the source workload.   
`source_owner`: Owner of the source workload instance (e.g. k8s Deployment).   
`destination_principal`: Principal of the destination workload instance.   
`destination_workload_name`: Name of the destination workload.   
`destination_workload_namespace`: Namespace of the destination workload.   
`destination_owner`: Owner of the destination workload instance (e.g. k8s Deployment).   
`source_canonical_service_name`: The canonical service name of the source workload instance.   
`destination_canonical_service_name`: The canonical service name of the destination workload instance.   
`source_canonical_service_namespace`: The canonical service namespace of the source workload instance.   
`destination_canonical_service_namespace`: The canonical service namespace of the destination workload instance.   
`source_canonical_revision`: The canonical service revision of the source workload instance.   
`destination_canonical_revision`: The canonical service revision of the destination workload instance.   
`proxy_version`: Version of the proxy.   
`service/server/received_bytes_count` BETA ** _(project)_**   
Server Received Bytes Count   
`CUMULATIVE`, `INT64`, `By`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Cumulative number of bytes received by the service as a server through connections._   
`request_protocol`: Protocol of the request or connection (e.g. HTTP, gRPC, TCP).   
`service_authentication_policy`: Determines if Istio was used to secure communications between services and how. Currently supported values: "NONE", "MUTUAL_TLS".   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`destination_service_name`: Name of destination service.   
`destination_service_namespace`: Namespace of destination service.   
`destination_port`: (INT64) Port of the destination service.   
`source_principal`: Principal of the source workload instance.   
`source_workload_name`: Name of the source workload.   
`source_workload_namespace`: Namespace of the source workload.   
`source_owner`: Owner of the source workload instance (e.g. k8s Deployment).   
`destination_principal`: Principal of the destination workload instance.   
`destination_workload_name`: Name of the destination workload.   
`destination_workload_namespace`: Namespace of the destination workload.   
`destination_owner`: Owner of the destination workload instance (e.g. k8s Deployment).   
`source_canonical_service_name`: The canonical service name of the source workload instance.   
`destination_canonical_service_name`: The canonical service name of the destination workload instance.   
`source_canonical_service_namespace`: The canonical service namespace of the source workload instance.   
`destination_canonical_service_namespace`: The canonical service namespace of the destination workload instance.   
`source_canonical_revision`: The canonical service revision of the source workload instance.   
`destination_canonical_revision`: The canonical service revision of the destination workload instance.   
`proxy_version`: Version of the proxy.   
`service/server/request_bytes` BETA ** _(project)_**   
Server Request Bytes   
`DELTA`, `DISTRIBUTION`, `By`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[istio_canonical_service](https://docs.cloud.google.com/monitoring/api/resources#tag_istio_canonical_service)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of incoming request sizes received by the service in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`request_protocol`: Protocol of the request or connection (e.g. HTTP, gRPC, TCP).   
`service_authentication_policy`: Determines if Istio was used to secure communications between services and how. Currently supported values: "NONE", "MUTUAL_TLS".   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`destination_service_name`: Name of destination service.   
`destination_service_namespace`: Namespace of destination service.   
`destination_port`: (INT64) Port of the destination service.   
`source_principal`: Principal of the source workload instance.   
`source_workload_name`: Name of the source workload.   
`source_workload_namespace`: Namespace of the source workload.   
`source_owner`: Owner of the source workload instance (e.g. k8s Deployment).   
`destination_principal`: Principal of the destination workload instance.   
`destination_workload_name`: Name of the destination workload.   
`destination_workload_namespace`: Namespace of the destination workload.   
`destination_owner`: Owner of the destination workload instance (e.g. k8s Deployment).   
`source_canonical_service_name`: The canonical service name of the source workload instance.   
`destination_canonical_service_name`: The canonical service name of the destination workload instance.   
`source_canonical_service_namespace`: The canonical service namespace of the source workload instance.   
`destination_canonical_service_namespace`: The canonical service namespace of the destination workload instance.   
`source_canonical_revision`: The canonical service revision of the source workload instance.   
`destination_canonical_revision`: The canonical service revision of the destination workload instance.   
`proxy_version`: Version of the proxy.   
`request_operation`: Unique string used to identify the API method (if available) or HTTP Method.   
`api_version`: Version of the API.   
`response_code`: (INT64) Response code of the request according to protocol.   
`api_name`: Name of the API.   
`service/server/request_count` BETA ** _(project)_**   
Server Request Count   
`DELTA`, `INT64`, `1`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[istio_canonical_service](https://docs.cloud.google.com/monitoring/api/resources#tag_istio_canonical_service)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Number of requests received by the service. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`request_protocol`: Protocol of the request or connection (e.g. HTTP, gRPC, TCP).   
`service_authentication_policy`: Determines if Istio was used to secure communications between services and how. Currently supported values: "NONE", "MUTUAL_TLS".   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`destination_service_name`: Name of destination service.   
`destination_service_namespace`: Namespace of destination service.   
`destination_port`: (INT64) Port of the destination service.   
`source_principal`: Principal of the source workload instance.   
`source_workload_name`: Name of the source workload.   
`source_workload_namespace`: Namespace of the source workload.   
`source_owner`: Owner of the source workload instance (e.g. k8s Deployment).   
`destination_principal`: Principal of the destination workload instance.   
`destination_workload_name`: Name of the destination workload.   
`destination_workload_namespace`: Namespace of the destination workload.   
`destination_owner`: Owner of the destination workload instance (e.g. k8s Deployment).   
`source_canonical_service_name`: The canonical service name of the source workload instance.   
`destination_canonical_service_name`: The canonical service name of the destination workload instance.   
`source_canonical_service_namespace`: The canonical service namespace of the source workload instance.   
`destination_canonical_service_namespace`: The canonical service namespace of the destination workload instance.   
`source_canonical_revision`: The canonical service revision of the source workload instance.   
`destination_canonical_revision`: The canonical service revision of the destination workload instance.   
`proxy_version`: Version of the proxy.   
`request_operation`: Unique string used to identify the API method (if available) or HTTP Method.   
`api_version`: Version of the API.   
`response_code`: (INT64) Response code of the request according to protocol.   
`api_name`: Name of the API.   
`service/server/response_bytes` BETA ** _(project)_**   
Server Response Bytes   
`DELTA`, `DISTRIBUTION`, `By`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[istio_canonical_service](https://docs.cloud.google.com/monitoring/api/resources#tag_istio_canonical_service)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of response sizes sent by the service in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`request_protocol`: Protocol of the request or connection (e.g. HTTP, gRPC, TCP).   
`service_authentication_policy`: Determines if Istio was used to secure communications between services and how. Currently supported values: "NONE", "MUTUAL_TLS".   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`destination_service_name`: Name of destination service.   
`destination_service_namespace`: Namespace of destination service.   
`destination_port`: (INT64) Port of the destination service.   
`source_principal`: Principal of the source workload instance.   
`source_workload_name`: Name of the source workload.   
`source_workload_namespace`: Namespace of the source workload.   
`source_owner`: Owner of the source workload instance (e.g. k8s Deployment).   
`destination_principal`: Principal of the destination workload instance.   
`destination_workload_name`: Name of the destination workload.   
`destination_workload_namespace`: Namespace of the destination workload.   
`destination_owner`: Owner of the destination workload instance (e.g. k8s Deployment).   
`source_canonical_service_name`: The canonical service name of the source workload instance.   
`destination_canonical_service_name`: The canonical service name of the destination workload instance.   
`source_canonical_service_namespace`: The canonical service namespace of the source workload instance.   
`destination_canonical_service_namespace`: The canonical service namespace of the destination workload instance.   
`source_canonical_revision`: The canonical service revision of the source workload instance.   
`destination_canonical_revision`: The canonical service revision of the destination workload instance.   
`proxy_version`: Version of the proxy.   
`request_operation`: Unique string used to identify the API method (if available) or HTTP Method.   
`api_version`: Version of the API.   
`response_code`: (INT64) Response code of the request according to protocol.   
`api_name`: Name of the API.   
`service/server/response_latencies` BETA ** _(project)_**   
Server Response Latencies   
`DELTA`, `DISTRIBUTION`, `ms`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[istio_canonical_service](https://docs.cloud.google.com/monitoring/api/resources#tag_istio_canonical_service)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Distribution of service response latency for incoming requests. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`request_protocol`: Protocol of the request or connection (e.g. HTTP, gRPC, TCP).   
`service_authentication_policy`: Determines if Istio was used to secure communications between services and how. Currently supported values: "NONE", "MUTUAL_TLS".   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`destination_service_name`: Name of destination service.   
`destination_service_namespace`: Namespace of destination service.   
`destination_port`: (INT64) Port of the destination service.   
`source_principal`: Principal of the source workload instance.   
`source_workload_name`: Name of the source workload.   
`source_workload_namespace`: Namespace of the source workload.   
`source_owner`: Owner of the source workload instance (e.g. k8s Deployment).   
`destination_principal`: Principal of the destination workload instance.   
`destination_workload_name`: Name of the destination workload.   
`destination_workload_namespace`: Namespace of the destination workload.   
`destination_owner`: Owner of the destination workload instance (e.g. k8s Deployment).   
`source_canonical_service_name`: The canonical service name of the source workload instance.   
`destination_canonical_service_name`: The canonical service name of the destination workload instance.   
`source_canonical_service_namespace`: The canonical service namespace of the source workload instance.   
`destination_canonical_service_namespace`: The canonical service namespace of the destination workload instance.   
`source_canonical_revision`: The canonical service revision of the source workload instance.   
`destination_canonical_revision`: The canonical service revision of the destination workload instance.   
`proxy_version`: Version of the proxy.   
`request_operation`: Unique string used to identify the API method (if available) or HTTP Method.   
`api_version`: Version of the API.   
`response_code`: (INT64) Response code of the request according to protocol.   
`api_name`: Name of the API.   
`service/server/sent_bytes_count` BETA ** _(project)_**   
Server Sent Bytes Count   
`CUMULATIVE`, `INT64`, `By`   
**[cloud_run_revision](https://docs.cloud.google.com/monitoring/api/resources#tag_cloud_run_revision)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)**   
**[k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container)** |  _Cumulative number of bytes sent by the service as a server through connections._   
`request_protocol`: Protocol of the request or connection (e.g. HTTP, gRPC, TCP).   
`service_authentication_policy`: Determines if Istio was used to secure communications between services and how. Currently supported values: "NONE", "MUTUAL_TLS".   
`mesh_uid`: Unique identifier for the mesh that is being monitored.   
`destination_service_name`: Name of destination service.   
`destination_service_namespace`: Namespace of destination service.   
`destination_port`: (INT64) Port of the destination service.   
`source_principal`: Principal of the source workload instance.   
`source_workload_name`: Name of the source workload.   
`source_workload_namespace`: Namespace of the source workload.   
`source_owner`: Owner of the source workload instance (e.g. k8s Deployment).   
`destination_principal`: Principal of the destination workload instance.   
`destination_workload_name`: Name of the destination workload.   
`destination_workload_namespace`: Namespace of the destination workload.   
`destination_owner`: Owner of the destination workload instance (e.g. k8s Deployment).   
`source_canonical_service_name`: The canonical service name of the source workload instance.   
`destination_canonical_service_name`: The canonical service name of the destination workload instance.   
`source_canonical_service_namespace`: The canonical service namespace of the source workload instance.   
`destination_canonical_service_namespace`: The canonical service namespace of the destination workload instance.   
`source_canonical_revision`: The canonical service revision of the source workload instance.   
`destination_canonical_revision`: The canonical service revision of the destination workload instance.   
`proxy_version`: Version of the proxy.   
  
Generated at 2026-10-14 20:24:33 UTC.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
