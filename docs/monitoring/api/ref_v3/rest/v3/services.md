---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/
title: REST Resource: services \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:16.065345+00:00
---

# REST Resource: services  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  REST Resource: services Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Service
    * JSON representation
  * Custom
  * AppEngine
    * JSON representation
  * ClusterIstio
    * JSON representation
  * MeshIstio
    * JSON representation
  * IstioCanonicalService
    * JSON representation
  * CloudRun
    * JSON representation
  * GkeNamespace
    * JSON representation
  * GkeWorkload
    * JSON representation
  * GkeService
    * JSON representation
  * BasicService
    * JSON representation
  * Telemetry
    * JSON representation
  * Methods



## Resource: Service

A `Service` is a discrete, autonomous, and network-accessible unit, designed to solve an individual concern ([Wikipedia](https://en.wikipedia.org/wiki/Service-orientation)). In Cloud Monitoring, a `Service` acts as the root resource under which operational aspects of the service are accessible.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "basicService": {
        object ([BasicService](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#BasicService))
      },
      "telemetry": {
        object ([Telemetry](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#Telemetry))
      },
      "userLabels": {
        string: string,
        ...
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "custom": {
        object ([Custom](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#Custom))
      },
      "appEngine": {
        object ([AppEngine](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#AppEngine))
      },
      "clusterIstio": {
        object ([ClusterIstio](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#ClusterIstio))
      },
      "meshIstio": {
        object ([MeshIstio](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#MeshIstio))
      },
      "istioCanonicalService": {
        object ([IstioCanonicalService](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#IstioCanonicalService))
      },
      "cloudRun": {
        object ([CloudRun](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#CloudRun))
      },
      "gkeNamespace": {
        object ([GkeNamespace](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#GkeNamespace))
      },
      "gkeWorkload": {
        object ([GkeWorkload](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#GkeWorkload))
      },
      "gkeService": {
        object ([GkeService](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#GkeService))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Resource name for this Service. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]
      
  
`displayName` |  `string` Name used for UI elements listing this Service.  
`basicService` |  `object (`[BasicService](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#BasicService)`)` Message that contains the service type and service labels of this service if it is a basic service. Documentation and examples [here](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#basic-svc-w-basic-sli).  
`telemetry` |  `object (`[Telemetry](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#Telemetry)`)` Configuration for how to query telemetry on a Service.  
`userLabels` |  `map (key: string, value: string)` Labels which have been used to annotate the service. Label keys must start with a letter. Label keys and values may contain lowercase letters, numbers, underscores, and dashes. Label keys and values have a maximum length of 63 characters, and must be less than 128 bytes in size. Up to 64 label entries may be stored. For labels which do not have a semantic value, the empty string may be supplied for the label value.  
REQUIRED. Service-identifying atoms specifying the underlying service. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`custom` |  `object (`[Custom](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#Custom)`)` Custom service type.  
`appEngine` |  `object (`[AppEngine](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#AppEngine)`)` Type used for App Engine services.  
`clusterIstio` |  `object (`[ClusterIstio](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#ClusterIstio)`)` Type used for Istio services that live in a Kubernetes cluster.  
`meshIstio` |  `object (`[MeshIstio](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#MeshIstio)`)` Type used for Istio services scoped to an Istio mesh.  
`istioCanonicalService` |  `object (`[IstioCanonicalService](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#IstioCanonicalService)`)` Type used for canonical services scoped to an Istio mesh. Metrics for Istio are [documented here](https://istio.io/latest/docs/reference/config/metrics/)  
`cloudRun` |  `object (`[CloudRun](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#CloudRun)`)` Type used for Cloud Run services.  
`gkeNamespace` |  `object (`[GkeNamespace](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#GkeNamespace)`)` Type used for GKE Namespaces.  
`gkeWorkload` |  `object (`[GkeWorkload](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#GkeWorkload)`)` Type used for GKE Workloads.  
`gkeService` |  `object (`[GkeService](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services#GkeService)`)` Type used for GKE Services (the Kubernetes concept of a service).  
End of mutually exclusive fields.  
  
## Custom

This type has no fields.

Use a custom service to designate a service that you want to monitor when none of the other service types (like App Engine, Cloud Run, or a GKE type) matches your intended service.

## AppEngine

App Engine service. Learn more at <https://cloud.google.com/appengine>.

JSON representation  
---  
      
    
    {
      "moduleId": string
    }  
  
Fields  
---  
`moduleId` |  `string` The ID of the App Engine module underlying this service. Corresponds to the `module_id` resource label in the [`gae_app` monitored resource](https://cloud.google.com/monitoring/api/resources#tag_gae_app).  
  
## ClusterIstio

Istio service scoped to a single Kubernetes cluster. Learn more at <https://istio.io>. Clusters running OSS Istio will have their services ingested as this type.

JSON representation  
---  
      
    
    {
      "location": string,
      "clusterName": string,
      "serviceNamespace": string,
      "serviceName": string
    }  
  
Fields  
---  
`location` |  `string` The location of the Kubernetes cluster in which this Istio service is defined. Corresponds to the `location` resource label in `k8s_cluster` resources.  
`clusterName` |  `string` The name of the Kubernetes cluster in which this Istio service is defined. Corresponds to the `cluster_name` resource label in `k8s_cluster` resources.  
`serviceNamespace` |  `string` The namespace of the Istio service underlying this service. Corresponds to the `destination_service_namespace` metric label in Istio metrics.  
`serviceName` |  `string` The name of the Istio service underlying this service. Corresponds to the `destination_service_name` metric label in Istio metrics.  
  
## MeshIstio

Istio service scoped to an Istio mesh. Anthos clusters running ASM < 1.6.8 will have their services ingested as this type.

JSON representation  
---  
      
    
    {
      "meshUid": string,
      "serviceNamespace": string,
      "serviceName": string
    }  
  
Fields  
---  
`meshUid` |  `string` Identifier for the mesh in which this Istio service is defined. Corresponds to the `meshUid` metric label in Istio metrics.  
`serviceNamespace` |  `string` The namespace of the Istio service underlying this service. Corresponds to the `destination_service_namespace` metric label in Istio metrics.  
`serviceName` |  `string` The name of the Istio service underlying this service. Corresponds to the `destination_service_name` metric label in Istio metrics.  
  
## IstioCanonicalService

Canonical service scoped to an Istio mesh. Anthos clusters running ASM >= 1.6.8 will have their services ingested as this type.

JSON representation  
---  
      
    
    {
      "meshUid": string,
      "canonicalServiceNamespace": string,
      "canonicalService": string
    }  
  
Fields  
---  
`meshUid` |  `string` Identifier for the Istio mesh in which this canonical service is defined. Corresponds to the `meshUid` metric label in [Istio metrics](https://cloud.google.com/monitoring/api/metrics_istio).  
`canonicalServiceNamespace` |  `string` The namespace of the canonical service underlying this service. Corresponds to the `destination_canonical_service_namespace` metric label in [Istio metrics](https://cloud.google.com/monitoring/api/metrics_istio).  
`canonicalService` |  `string` The name of the canonical service underlying this service. Corresponds to the `destination_canonical_service_name` metric label in label in [Istio metrics](https://cloud.google.com/monitoring/api/metrics_istio).  
  
## CloudRun

Cloud Run service. Learn more at <https://cloud.google.com/run>.

JSON representation  
---  
      
    
    {
      "serviceName": string,
      "location": string
    }  
  
Fields  
---  
`serviceName` |  `string` The name of the Cloud Run service. Corresponds to the `service_name` resource label in the [`cloud_run_revision` monitored resource](https://cloud.google.com/monitoring/api/resources#tag_cloud_run_revision).  
`location` |  `string` The location the service is run. Corresponds to the `location` resource label in the [`cloud_run_revision` monitored resource](https://cloud.google.com/monitoring/api/resources#tag_cloud_run_revision).  
  
## GkeNamespace

GKE Namespace. The field names correspond to the resource metadata labels on monitored resources that fall under a namespace (for example, `k8s_container` or `k8s_pod`).

JSON representation  
---  
      
    
    {
      "projectId": string,
      "location": string,
      "clusterName": string,
      "namespaceName": string
    }  
  
Fields  
---  
`projectId` |  `string` Output only. The project this resource lives in. For legacy services migrated from the `Custom` type, this may be a distinct project from the one parenting the service itself.  
`location` |  `string` The location of the parent cluster. This may be a zone or region.  
`clusterName` |  `string` The name of the parent cluster.  
`namespaceName` |  `string` The name of this namespace.  
  
## GkeWorkload

A GKE Workload (Deployment, StatefulSet, etc). The field names correspond to the metadata labels on monitored resources that fall under a workload (for example, `k8s_container` or `k8s_pod`).

JSON representation  
---  
      
    
    {
      "projectId": string,
      "location": string,
      "clusterName": string,
      "namespaceName": string,
      "topLevelControllerType": string,
      "topLevelControllerName": string
    }  
  
Fields  
---  
`projectId` |  `string` Output only. The project this resource lives in. For legacy services migrated from the `Custom` type, this may be a distinct project from the one parenting the service itself.  
`location` |  `string` The location of the parent cluster. This may be a zone or region.  
`clusterName` |  `string` The name of the parent cluster.  
`namespaceName` |  `string` The name of the parent namespace.  
`topLevelControllerType` |  `string` The type of this workload (for example, "Deployment" or "DaemonSet")  
`topLevelControllerName` |  `string` The name of this workload.  
  
## GkeService

GKE Service. The "service" here represents a [Kubernetes service object](https://kubernetes.io/docs/concepts/services-networking/service). The field names correspond to the resource labels on [`k8s_service` monitored resources](https://cloud.google.com/monitoring/api/resources#tag_k8s_service).

JSON representation  
---  
      
    
    {
      "projectId": string,
      "location": string,
      "clusterName": string,
      "namespaceName": string,
      "serviceName": string
    }  
  
Fields  
---  
`projectId` |  `string` Output only. The project this resource lives in. For legacy services migrated from the `Custom` type, this may be a distinct project from the one parenting the service itself.  
`location` |  `string` The location of the parent cluster. This may be a zone or region.  
`clusterName` |  `string` The name of the parent cluster.  
`namespaceName` |  `string` The name of the parent namespace.  
`serviceName` |  `string` The name of this service.  
  
## BasicService

A well-known service type, defined by its service type and service labels. Documentation and examples [here](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#basic-svc-w-basic-sli).

JSON representation  
---  
      
    
    {
      "serviceType": string,
      "serviceLabels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`serviceType` |  `string` The type of service that this basic service defines, e.g. APP_ENGINE service type. Documentation and valid values [here](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#basic-svc-w-basic-sli).  
`serviceLabels` |  `map (key: string, value: string)` Labels that specify the resource that emits the monitoring data which is used for SLO reporting of this `Service`. Documentation and valid values for given service types [here](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures#basic-svc-w-basic-sli).  
  
## Telemetry

Configuration for how to query telemetry on a Service.

JSON representation  
---  
      
    
    {
      "resourceName": string
    }  
  
Fields  
---  
`resourceName` |  `string` The full name of the resource that defines this service. Formatted as described in <https://cloud.google.com/apis/design/resourceNames>.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/create)`

|  Create a `Service`.  
  
### `[delete](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/delete)`

|  Soft delete this `Service`.  
  
### `[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/get)`

|  Get the named `Service`.  
  
### `[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/list)`

|  List `Service`s for this Metrics Scope.  
  
### `[patch](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services/patch)`

|  Update this `Service`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-04 UTC."],[],[]] 
