---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/cloud-run-api-reference/
title: Cloud Run API reference \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:37.129205+00:00
---

# Cloud Run API reference  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/cloud-run-api-reference/

You are viewing v1.28 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.28/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Run API reference

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview).

This page provides a reference for the APIs that are used to configure Cloud Service Mesh for Cloud Run workloads.

## Cloud Run API

### v1 API

Cloud Service Mesh is enabled using a [Revision level annotation](https://docs.cloud.google.com/run/docs/reference/yaml/v1). The value of this annotation is the backing mesh name of the Cloud Service Mesh Istio cluster.

Annotation | Value  
---|---  
run.googleapis.com/mesh | projects/PROJECT/locations/global/meshes/MESH  
  
### v2 API

Cloud Service Mesh is enabled using the `serviceMesh` field in the [`Service` resource](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#Service)

## Cloud Service Mesh Istio API

### VirtualService API

Field Name | Type | Field Description  
---|---|---  
gateways | String [] | If the gateways include an "external-mesh" then the virtual service applies to only non-GKE workloads.   
  
If "mesh" is specified along with "external-mesh", the virtual service will apply to both non-GKE and GKE workloads.  
  
exportTo | string | Considering that non-GKE workloads have no concept of a namespace, "external-mesh" virtual services will ignore the exportTo field.  
  
However, they will continue to work for virtual services that have "mesh" or gateways will continue to work as expected for GKE workloads.  
httpRoute.HTTPMatchRequest.SourceLabels | map | Will be ignored for "external-mesh" virtual services.  
However, they will continue to work for virtual services that have "mesh" or gateways will continue to work as expected for GKE workloads.  
httpRoute.HTTPMatchRequest.SourceNamespace | string | Will be ignored for "external-mesh" virtual services.  
  
However, they will continue to work for virtual services that have "mesh" or gateways will continue to work as expected for GKE workloads.  
httpRoute.HTTPMatchRequest.Gateways | string[] | Will be ignored for "external-mesh" virtual services.  
  
However, they will continue to work for virtual services that have "mesh" or gateways will continue to work as expected for GKE workloads.  
tls | tlsRoute[] | Will be ignored for "external-mesh" virtual services.  
  
However, they will continue to work for virtual services that have "mesh" or gateways will continue to work as expected for GKE workloads.  
tcp  | tcpRoute[] | Will be ignored for external-mesh virtual service.  
  
However, they will continue to work for virtual services that have "mesh" or gateways will continue to work as expected for GKE workloads.  
  
### Istio Auto MTLS and Secure Naming

Currently, Cloud Service Mesh supports Automatic Istio MutualTLS and Secure Naming for requests between GKE Services.

For Preview, non-GKE workloads communicating with GKE workloads/services will not use Istio Auto MTLS nor Secure Naming. The traffic will be in plain text. Make sure that GKE Services have a permissive MTLS policy (which is the Istio API default) which accepts MTLS traffic from GKE workloads and plain text from non-GKE workloads.

Use the following command to check if PeerAuthentication is in permissive mode:
    
    
    # list PeerAuthentication resources in a namespace
    # If no PeerAuthentication resource exists in the namespace, 
    # then it's PERMISSIVE mode (Istio API default)
    kubectl get PeerAuthentication -n $NAMESPACE
    
    # for each of the above run the following command
    kubectl get PeerAuthentication $PEER-AUTHN -n $NAMESPACE
    
    # Expected Output is as follows:
    # MTLS Mode must be PERMISSIVE.
    # If the output says STRICT, then please update the policy to PERMISSIVE.
    apiVersion: security.istio.io/v1
    kind: PeerAuthentication
    metadata:
      name: $PEER-AUTHN
      namespace: $NAMESPACE
    spec:
      mtls:
        mode: PERMISSIVE
    

### MeshConfig Telemetry

Cloud Service Mesh supports MeshConfig telemetry API to enable and disable Cloud Logging and Cloud Monitoring for GKE workloads. This will work similarly for non-GKE workloads as well.

### Destination Rule

For Preview, `DestinationRule` targeting the "external-mesh" virtual services will be supported except following fields: `trafficPolicy.tls`

### Sidecar API

Sidecar API will not be applicable to non-GKE workloads. Non-GKE workloads will be able to see all the virtual services scoped to "external-mesh" without being filtered by any Sidecar visibility rules.

### Security API - Authorization Policy, Request Authentication Policy

These will not apply to non-GKE workloads which act as Clients sending outbound traffic. They will continue to apply GKE workloads that receive inbound traffic.

### GCPBackend API

**Note:** This is a Kubernetes Custom Resource.**Field Name** | **Type** | **Field Description**  
---|---|---  
GCPBackend | struct | Schema for the GCPBackend resource.  
TypeMeta | metav1.TypeMeta | Embedded struct for storing metadata information like kind and API version.  
ObjectMeta | metav1.ObjectMeta | Embedded struct for storing metadata information like name, namespace, labels, annotations, etc.  
Spec | GCPBackendSpec | Specification for the GCPBackend resource, defining its desired state.  
GCPBackendSpec | struct | Defines the desired state of the GRPCRoute.  
CloudRun | *CloudRunBackend | Defines a backend running in CloudRun (optional).  
CloudRunBackend | struct | Identifies a service running on Cloud Run.  
Service | string | CloudRun service name. Must be between 1 and 49 characters, follow a specific pattern, and consist only of lowercase letters, hyphens, and numbers.  
Regions | []Region | Regions of the CloudRun service. Exactly one region must be provided.  
Project | string | Project ID of the CloudRun service. Defaults to the same project as the GKE cluster. Must be between 6 and 30 characters and follow a specific pattern. Currently, Cloud Run Service and the GKE Cluster must be in the same project.  
GCPBackendList | struct | Contains a list of GCPBackends.  
Items | []*GCPBackend | Array of GCPBackend pointers representing the list of GCPBackend resources.  
ListMeta | metav1.ListMeta | Embedded struct for storing list metadata information like resource version and continue token for pagination.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
