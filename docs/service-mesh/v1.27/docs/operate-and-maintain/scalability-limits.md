---
url: https://docs.cloud.google.com/service-mesh/v1.27/docs/operate-and-maintain/scalability-limits/
title: Scaling Limits for Cloud Service Mesh on GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:39.549660+00:00
---

# Scaling Limits for Cloud Service Mesh on GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.27/docs/operate-and-maintain/scalability-limits/

You are viewing v1.27 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.27/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Scaling Limits for Cloud Service Mesh on GKE

This document describes the scaling limits of the control plane for managed Cloud Service Mesh architectures on GKE so you can make informed decisions regarding your deployments.

## Overview

The scalability of Cloud Service Mesh on GKE depends on the efficient operation of its two main components, the data plane and the control plane. This document focuses on scaling limits of the control plane. Refer to [Scalability Best Practices](https://docs.cloud.google.com/service-mesh/v1.27/docs/operate-and-maintain/scalability-best-practices) for data plane scalability best practices.

Some of the scaling limits documented are enforced by quota restrictions. Exceeding them will require quota increase requests. Others are not strictly enforced, but can lead to undefined behavior and performance if exceeded.

To understand how Istio resources are translated to Google Cloud resources, refer to the [Understanding API resources](https://docs.cloud.google.com/service-mesh/v1.27/docs/understand-api-resources) guide first.

**Note:** The limitations documented in this guide are only applicable to the `TRAFFIC_DIRECTOR` control plane implementation.

## Service scaling limits

Service scaling is limited along two dimensions

  * Per Project: A maximum of 5000 Cloud Service Mesh services are supported per Google Cloud project (with the exception of Kubernetes headless services).

  * Per Zone per Project: Since Cloud Service Mesh creates [network-endpoint groups per zone](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts) for GKE services in the cluster, the [Zonal NEG quota limits](https://docs.cloud.google.com/load-balancing/docs/negs#zonal-neg) apply to the number of services per project that can have endpoints in that zone.




Note that once Cloud Service Mesh is enabled for a particular membership (i.e GKE cluster), **all** kubernetes services in the cluster are translated to Cloud Service Mesh services, including those that target workloads without a Cloud Service Mesh sidecar. Cloud Service Mesh creates Zonal Network Endpoint Groups for all services in the GKE cluster. If the cluster is regional, network endpoint groups are created for all node pool zones in the region.

**Note:** At larger scales, configuration changes can take longer to propagate to the data plane. Latency increases with the number of configurations being changed at the same time.

### Cloud Service Mesh services versus Kubernetes services

Cloud Service Mesh services are not the same as Kubernetes services in that Cloud Service Mesh services are one service per port.

For example, this Kubernetes service is internally translated into two Cloud Service Mesh services, one for each port.
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: my-service
    spec:
      selector:
        app: my-app
      ports:
        -   port: 80
          targetPort: 80
          protocol: TCP
          name: http
        -   port: 443
          targetPort: 443
          protocol: TCP
          name: https
    

Cloud Service Mesh service usage can be tracked by looking at the usage for the [BackendService Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/global_internal_traffic_director_backend_services) in the project

### Multi-cluster deployments

When a single mesh is deployed across [workloads in different Google Cloud clusters](https://docs.cloud.google.com/service-mesh/v1.27/docs/operate-and-maintain/gke-install-multi-cluster), all Cloud Service Mesh service resources are by default replicated across all clusters. This means that a Kubernetes service deployed in a single cluster creates several Cloud Service Mesh services, one for each cluster.

### Destination rule subsets

When configuring the [Istio Destination Rule API](https://istio.io/latest/docs/reference/config/networking/destination-rule/) with subsets, each subset may result in the generation of multiple new Cloud Service Mesh services.

For example, consider the following `DestinationRule` that targets the kubernetes service defined earlier:
    
    
    apiVersion: networking.istio.io/v1alpha3
    kind: DestinationRule
    metadata:
      name: my-service-destinationrule
    spec:
      host: my-service
      subsets:
      -   name: testversion
        labels:
          version: v3
      -   name: prodversion
        labels:
          version: v2
    

New synthetic services will be created for each of the subsets defined. If the original Kubernetes service created two Cloud Service Mesh services, the `DestinationRule` will create 4 additional Cloud Service Mesh services, 2 for each subset, resulting in a total of 6 Cloud Service Mesh services.

### Multi-project deployments

When a single mesh is deployed across workloads in different Google Cloud projects, all Cloud Service Mesh service resources are created in the fleet host project. This means they are all subject to the Cloud Service Mesh scalability limitations in the fleet host project.

### Kubernetes headless services

Kubernetes headless services have a lower limit compared to regular services. Cloud Service Mesh only supports 50 headless Cloud Service Mesh services per cluster. See [the Kubernetes networking documentation](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services) for an example.

### Istio Sidecar Resources

For [Istio Sidecar API](https://istio.io/latest/docs/reference/config/networking/sidecar/), the following limits apply:

  * Sidecar without `workloadSelector`: 150 per cluster

  * Sidecar with `workloadSelector`: 20 per cluster




## Endpoint scaling limits

Endpoint scaling limits are typically per the following:

  * Cloud Service Mesh service

  * GKE cluster




### Regular Kubernetes services

[Endpoints per NEG quotas](https://docs.cloud.google.com/load-balancing/docs/quotas#endpoints_per_neg) affect the maximum number of endpoints that can belong to a single Kubernetes service.

### Kubernetes headless services

For Kubernetes headless service, Cloud Service Mesh supports not more than 36 endpoints per headless service. Refer to [the Kubernetes networking documentation](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services) for an example.

### GKE cluster limits

Cloud Service Mesh supports up to 5000 endpoints (Pod IPs) per cluster.

## Gateway scaling limit

When [using Istio Gateways](https://istio.io/latest/docs/reference/config/networking/gateway/), especially to [terminate HTTPS connections using TLS credentials in Kubernetes secrets](https://istio.io/latest/docs/tasks/traffic-management/ingress/secure-ingress/), Cloud Service Mesh supports at most the following number of pods:

  * 1500 gateway pods when using Regional GKE clusters

  * 500 gateway pods when using Zonal or Autopilot GKE clusters




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
