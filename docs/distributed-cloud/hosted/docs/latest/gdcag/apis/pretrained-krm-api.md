---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/pretrained-krm-api/
title: Pretrained API private system Kubernetes Resource Model API \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:56:44.051986+00:00
---

# Pretrained API private system Kubernetes Resource Model API  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/pretrained-krm-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Pretrained API private system Kubernetes Resource Model API Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

The pre-trained APIs are a collection of AI services that include Optical Character Recognition (OCR), Speech-to-Text, and Translation. The services are enabled and disabled using the Kubernetes Resource Model (KRM) API. The KRM API is a management API that is optionally used by the AI Platform Admin.

The purpose of this page is to provide information only.

## aiplatform.private.gdc.goog/v1

Package v1 contains API Schema definitions for the aiplatform.private.gdc.goog v1 API group

### Alerting

Alerting contains the names of the ConfigMaps that are to be processed and transformed into Observability Platform alerting CRs: MonitoringRule and LoggingRule.

_Appears in:_ \- Observability

Field | Description  
---|---  
`monitoringAlertsConfigMap` _string_ | Configmap with embedded MonitoringRule CR to fetch from Remote K8s Cluster and process by transforming into an Observability Platform MonitoringRule CR and deploy to Admin Cluster.  
`loggingAlertsConfigMap` _string_ | ConfigMap with embedded LoggingRule CR to fetch from Remote K8s Cluster and process by transforming into an Observability Platform LoggingRule CR and deploy to Admin Cluster.  
  
### AppConfig

AppConfig is the Schema for the AppConfig API. Should have one per namespace

_Appears in:_ \- AppConfigList

Field | Description  
---|---  
`apiVersion` _string_ | `aiplatform.private.gdc.goog/v1`  
`kind` _string_ | `AppConfig`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _AppConfigSpec_ |   
`status` _AppConfigStatus_ |   
  
### AppConfigList

AppConfigList contains a list of AppConfig

Field | Description  
---|---  
`apiVersion` _string_ | `aiplatform.private.gdc.goog/v1`  
`kind` _string_ | `AppConfigList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _AppConfig array_ |   
  
### AppConfigSpec

_Appears in:_ \- AppConfig

Field | Description  
---|---  
`sql` _Database_ |   
  
### AppConfigStatus

AppConfigStatus defines the observed state of AppConfig.

_Appears in:_ \- AppConfig

Field | Description  
---|---  
`ready` _boolean_ | Ready indicates whether the resource is in a ready state.  
`primaryCondition` _ResourceCondition_ | PrimaryCondition represents the primary condition of a resource. If the resource is ready, then the condition will indicate the resource is ready. Otherwise, the condition will be the primary reason why the resource is not ready.  
`resourceConditions` _ResourceCondition array_ | ResourceConditions is a collection of conditions for a resource and its subresources. It can be used to determine the overall health of a resource and its subresources.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents raw resource conditions populated from Kubernetes resources for debugging purpose.  
`database` _DatabaseInfo_ | Presents the Database subresource information.  
  
### Dashboards

Dashboards contains a list of the names of Observability Platform-dashboard-compatible configmaps to be processed.

_Appears in:_ \- Observability

Field | Description  
---|---  
`configMaps` _string array_ | ConfigMaps (with embedded Grafana dashboard json definition) to be processed; these are expected to exist in the user cluster and namespace that the AI workloads are deployed to. There should be a 1:1 mapping between the number of desired dashboards and dashboard configmaps. We assume there will be a single key in the configmap: 'data', which will house the dashboard definition json string.  
  
### Database

Database configures the relational db requirements for the target Microservice.

_Appears in:_ \- AppConfigSpec

Field | Description  
---|---  
`postgres` _PostgresConfig_ |   
  
### DatabaseInfo

DatabaseInfo defines the observed state of Database Information.

_Appears in:_ \- AppConfigStatus

Field | Description  
---|---  
`endpoint` _string_ |   
`port` _string_ |   
  
### HPAStatus

HPAStatus describes the status conditions of the HorizontalPodAutoscaler.

_Appears in:_ \- MicroserviceStatus

Field | Description  
---|---  
`statusConditions` _[HorizontalPodAutoscalerCondition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.22/#horizontalpodautoscalercondition-v2-autoscaling) array_ | Status conditions  
`currentReplicas` _integer_ | Number of current replicas managed by the HPA  
`desiredReplicas` _integer_ | Number of desired replicas managed by the HPA  
  
### Logging

Logging configures the log collection functionality for the Observability Platform on GDC air-gapped (do not enable if testing on GKE - this functionality does not apply there).

_Appears in:_ \- Observability

Field | Description  
---|---  
`enableLogCollection` _boolean_ | EnableLogCollection indicates whether or not to enable log collection via the Observability Platform.  
`staticLabels` _object (keys:string, values:string)_ | Maps to the 'additionalLabels' property of the OP LoggingTargetCR. Static labels to add to all captured log entries. Label names must not contain dashes ("-"); label values can contain dashes.  
  
### Metrics

Metrics configures how metrics of a pod will be collected.

_Appears in:_ \- Observability

Field | Description  
---|---  
`prometheus` _PrometheusMetrics_ |   
  
### Microservice

Microservice is the Schema for the services API

_Appears in:_ \- MicroserviceList

Field | Description  
---|---  
`apiVersion` _string_ | `aiplatform.private.gdc.goog/v1`  
`kind` _string_ | `Microservice`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _MicroserviceSpec_ |   
`status` _MicroserviceStatus_ |   
  
### MicroserviceList

MicroserviceList contains a list of Microservice

Field | Description  
---|---  
`apiVersion` _string_ | `aiplatform.private.gdc.goog/v1`  
`kind` _string_ | `MicroserviceList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Microservice array_ |   
  
### MicroserviceSpec

MicroserviceSpec defines the desired state of Microservice.

_Appears in:_ \- Microservice

Field | Description  
---|---  
`public` _boolean_ | Whether this Microservice is public. If true, it will have an expose DNS record as well as a public endpoint. TLS will be setup on the gateway as well automatically according to the DNS name. The DNS prefix will be the name of the Microservice in metadata.  
`enableBucketAccess` _boolean_ | Whether to provision the storage bucket related configurations to the container  
`dnsname` _string_ | DNS host name. This will be used to construct DNS host name for the Microservice in GDC environment when Microservice is public  
`autoscaling` | Autoscaling configurations.  
`observability` _Observability_ | Observability (logging, metrics, monitoring and dashboards) configuration (some of which are applicable only to GDC air-gapped configurations).  
`prerequisites` _Prerequisites_ | Prerequisites configuration.  
`template` _PodTemplateSpec_ | Template to create pods in the Microservice. The Microservice will contain stateless deployments for these pods.  
  
### PodSpec

PodSpec is a minimalist version of the core PodSpec.

_Appears in:_ \- PodTemplateSpec

Field | Description  
---|---  
`containers` _[Container](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#container-v1-core) array_ | Specifies containers. Not all attributes are supported. Ports specified from all containers will be exposed. First container (containers[0]) is considered the primary container and will be the one to be tagged with resource requests for node auto-provisioning. The rest of the containers are considered as auxiliary (e.g.,sidecars).  
`nodeSelector` _object (keys:string, values:string)_ | NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node.  
`volumes` _[Volume](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#volume-v1-core) array_ | List of volumes that will be mounted to the pods  
`initContainers` _[Container](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#container-v1-core) array_ | List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/  
`tolerations` _[Toleration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#toleration-v1-core) array_ | If specified, the pod's tolerations.  
`serviceAccount` _string_ | The pre-created Kubernetes service account that will be used by pod.  
  
### PodTemplateSpec

PodTemplateSpec is a container object for PodSpec and potentially metadata spec.

_Appears in:_ \- Microservice

Field | Description  
---|---  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _PodSpec_ |   
  
### MicroserviceStatus

MicroserviceStatus defines the observed state of Microservice.

_Appears in:_ \- Microservice

Field | Description  
---|---  
`observedGeneration` _integer_ | The generation observed by the deployment controller.  
`endpoint` _string_ | The endpoint that this Microservice is accessible from. Only populated for public services.  
`deploymentStatus` _DeploymentStatus_ | The deployment status of this Microservice.  
`hpaStatus` _HPAStatus_ | The status of the HorizontalPodAutoscaler.  
`ready` _boolean_ | Overall Microservice's readiness status  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Represents the latest available observations of a Microservice's current state.  
  
### Observability

Observability configures the various components and parameters required by the Observability Platform (on GDC air-gapped), or Metrics exposure (on GKE).

_Appears in:_ \- MicroserviceSpec

Field | Description  
---|---  
`metrics` _Metrics_ | Metrics configuration. On GKE these are only collected on the first container. On GDC air-gapped this is used in conjunction with the Observability section to configure the behavior of the Observability Platform.  
`logging` _Logging_ |   
`alerting` _Alerting_ |   
`dashboards` _Dashboards_ |   
  
### PostgresConfig

PostgresConfig defines the relevant target configuration settings for a Postgres DB.

_Appears in:_ \- Database

Field | Description  
---|---  
`version` _string_ |   
  
### Prerequisites

Prerequisites configures any prerequisites for the Microservice.

_Appears in:_ \- MicroserviceSpec

Field | Description  
---|---  
`sql` _boolean_ | SQL configuration, if required by the target workload  
  
### PrometheusMetrics

PrometheusMetrics configures the Prometheus metrics exposed by a pod.

_Appears in:_ \- Metrics

Field | Description  
---|---  
`path` _string_ | The metrics URI path to scrape metrics from. Defaults to /metrics.  
`port` _integer_ | The port to scrape metrics from. Defaults to 80.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
