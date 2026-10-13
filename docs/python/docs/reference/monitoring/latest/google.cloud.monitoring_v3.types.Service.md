---
url: https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Service
title: Class Service (2.32.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:27.276589+00:00
---

# Class Service (2.32.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Service

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Service (2.32.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.32.0 (latest)  2.31.0  2.30.0  2.29.1  2.28.0  2.27.2  2.26.0  2.25.0  2.24.0  2.23.1  2.22.2  2.21.0  2.20.0  2.19.4  2.18.0  2.17.0  2.16.0  2.15.1  2.14.2  2.13.0  2.12.0  2.11.3  2.10.1  2.9.2  2.8.0  2.7.0  2.6.0  2.5.2  2.4.2  2.3.0  2.2.1  2.1.0  2.0.1  1.1.2  1.0.0  0.36.2  0.35.0  0.34.0  0.33.0  0.32.0 
    
    
    Service(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A `Service` is a discrete, autonomous, and network-accessible unit, designed to solve an individual concern (`Wikipedia <https://en.wikipedia.org/wiki/Service-orientation>`__). In Cloud Monitoring, a `Service` acts as the root resource under which operational aspects of the service are accessible.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. Resource name for this Service. The format is: :: projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]   
`display_name` |  `str`   
Name used for UI elements listing this Service.   
`custom` |  `[google.cloud.monitoring_v3.types.Service.Custom](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Service.Custom)`   
Custom service type. This field is a member of `oneof`_ `identifier`.   
`app_engine` |  `[google.cloud.monitoring_v3.types.Service.AppEngine](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Service.AppEngine)`   
Type used for App Engine services. This field is a member of `oneof`_ `identifier`.   
`cloud_endpoints` |  `[google.cloud.monitoring_v3.types.Service.CloudEndpoints](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Service.CloudEndpoints)`   
Type used for Cloud Endpoints services. This field is a member of `oneof`_ `identifier`.   
`cluster_istio` |  `[google.cloud.monitoring_v3.types.Service.ClusterIstio](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Service.ClusterIstio)`   
Type used for Istio services that live in a Kubernetes cluster. This field is a member of `oneof`_ `identifier`.   
`mesh_istio` |  `[google.cloud.monitoring_v3.types.Service.MeshIstio](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Service.MeshIstio)`   
Type used for Istio services scoped to an Istio mesh. This field is a member of `oneof`_ `identifier`.   
`istio_canonical_service` |  `[google.cloud.monitoring_v3.types.Service.IstioCanonicalService](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Service.IstioCanonicalService)`   
Type used for canonical services scoped to an Istio mesh. Metrics for Istio are `documented here   
`cloud_run` |  `[google.cloud.monitoring_v3.types.Service.CloudRun](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Service.CloudRun)`   
Type used for Cloud Run services. This field is a member of `oneof`_ `identifier`.   
`gke_namespace` |  `[google.cloud.monitoring_v3.types.Service.GkeNamespace](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Service.GkeNamespace)`   
Type used for GKE Namespaces. This field is a member of `oneof`_ `identifier`.   
`gke_workload` |  `[google.cloud.monitoring_v3.types.Service.GkeWorkload](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Service.GkeWorkload)`   
Type used for GKE Workloads. This field is a member of `oneof`_ `identifier`.   
`gke_service` |  `[google.cloud.monitoring_v3.types.Service.GkeService](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Service.GkeService)`   
Type used for GKE Services (the Kubernetes concept of a service). This field is a member of `oneof`_ `identifier`.   
`basic_service` |  `[google.cloud.monitoring_v3.types.Service.BasicService](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Service.BasicService)`   
Message that contains the service type and service labels of this service if it is a basic service. Documentation and examples `here `__.   
`telemetry` |  `[google.cloud.monitoring_v3.types.Service.Telemetry](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Service.Telemetry)`   
Configuration for how to query telemetry on a Service.   
`user_labels` |  `MutableMapping[str, str]`   
Labels which have been used to annotate the service. Label keys must start with a letter. Label keys and values may contain lowercase letters, numbers, underscores, and dashes. Label keys and values have a maximum length of 63 characters, and must be less than 128 bytes in size. Up to 64 label entries may be stored. For labels which do not have a semantic value, the empty string may be supplied for the label value.   
  
## Classes 

### AppEngine
    
    
    AppEngine(mapping=None, *, ignore_unknown_fields=False, **kwargs)

App Engine service. Learn more at <https://cloud.google.com/appengine>.

### BasicService
    
    
    BasicService(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A well-known service type, defined by its service type and service labels. Documentation and examples `here <https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#basic-svc-w-basic-sli>`__.

### CloudEndpoints
    
    
    CloudEndpoints(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Cloud Endpoints service. Learn more at <https://cloud.google.com/endpoints>.

### CloudRun
    
    
    CloudRun(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Cloud Run service. Learn more at <https://cloud.google.com/run>.

### ClusterIstio
    
    
    ClusterIstio(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Istio service scoped to a single Kubernetes cluster. Learn more at <https://istio.io>. Clusters running OSS Istio will have their services ingested as this type.

### Custom
    
    
    Custom(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Use a custom service to designate a service that you want to monitor when none of the other service types (like App Engine, Cloud Run, or a GKE type) matches your intended service.

### GkeNamespace
    
    
    GkeNamespace(mapping=None, *, ignore_unknown_fields=False, **kwargs)

GKE Namespace. The field names correspond to the resource metadata labels on monitored resources that fall under a namespace (for example, `k8s_container` or `k8s_pod`).

### GkeService
    
    
    GkeService(mapping=None, *, ignore_unknown_fields=False, **kwargs)

GKE Service. The "service" here represents a `Kubernetes service object <https://kubernetes.io/docs/concepts/services-networking/service>`**. The field names correspond to the resource labels on``k8s_service` monitored resources <https://cloud.google.com/monitoring/api/resources#tag_k8s_service>`**.

### GkeWorkload
    
    
    GkeWorkload(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A GKE Workload (Deployment, StatefulSet, etc). The field names correspond to the metadata labels on monitored resources that fall under a workload (for example, `k8s_container` or `k8s_pod`).

### IstioCanonicalService
    
    
    IstioCanonicalService(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Canonical service scoped to an Istio mesh. Anthos clusters running ASM >= 1.6.8 will have their services ingested as this type.

### MeshIstio
    
    
    MeshIstio(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Istio service scoped to an Istio mesh. Anthos clusters running ASM < 1.6.8 will have their services ingested as this type.

### Telemetry
    
    
    Telemetry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for how to query telemetry on a Service.

### UserLabelsEntry
    
    
    UserLabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
