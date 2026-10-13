---
url: https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/multi-cluster-mesh-failover/
title: Set up Multi-Cluster Mesh Failover \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:01:57.646446+00:00
---

# Set up Multi-Cluster Mesh Failover  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/multi-cluster-mesh-failover/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up Multi-Cluster Mesh Failover

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). **Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms#off-gcp). **Caution:** Managed Cloud Service Mesh using the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must [modernize](https://docs.cloud.google.com/service-mesh/docs/modernization) all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` control plane implementation. 

This page shows you how to design and implement a high-availability traffic routing strategy using Cloud Service Mesh in a multi-cluster environment. The following table describes the expected behavior:

Cluster State | Traffic Behavior  
---|---  
Both clusters healthy | 50% traffic to Cluster A, 50% to B  
Cluster A becomes unavailable | 100% traffic to Cluster B  
Cluster A recovers | Automatically restores 50/50 split  
**Important:** This setup only applies for Managed Cloud Service Mesh with the `ISTIOD` control plane implementation, and in-cluster Cloud Service Mesh.

## Prerequisites

As a starting point, this guide assumes that you have already:

  * Created two GKE clusters [registered to the same fleet host project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#register_a_new_cluster) in two different regions configured for Cloud Service Mesh.
  * [Set up a multi-cluster mesh on Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/gke-install-multi-cluster).
  * Istio control plane installed and configured in both clusters.
  * `istio-ingressgateway` deployed and exposed in at least one cluster (Cluster A).
  * `hello-world` application deployed in both clusters with sidecar injection enabled.



This lab uses the following regions:

  * **Cluster A:** `europe-west1`
  * **Cluster B:** `us-central1`



## Set up multi-cluster mesh failover

  1. Deploy and apply the public ingress gateway using the sample manifest from the [Cloud Service Mesh repository](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages/tree/main/samples/gateways):
         
         cat <<EOF> istio-ingressgateway.yaml
         apiVersion: networking.istio.io/v1alpha3
         kind: Gateway
         metadata:
           name: public-gateway
           namespace: default
         spec:
           selector:
             istio: ingressgateway
           servers:
           - port:
               number: 80
               name: http
               protocol: HTTP
             hosts:
             - '*'
         EOF
         
         kubectl apply -f istio-ingressgateway.yaml
         

This gateway exposes the `hello-world` service externally.

  2. Create and apply a `VirtualService` in Cluster A to route traffic to the `hello-world` service:
         
         cat <<EOF> virtual-service.yaml
         apiVersion: networking.istio.io/v1beta1
         kind: VirtualService
         metadata:
           name: hello-world
           namespace: default
         spec:
           hosts:
           - '*'
           gateways:
           - public-gateway
           http:
           - route:
             - destination:
                 host: hello-world.default.svc.cluster.local
         EOF
         
         kubectl apply -f virtual-service.yaml
         

This configuration forwards HTTP requests from the gateway to the service.

  3. Configure and apply a `DestinationRule` for locality-based failover
         
         cat <<EOF> destination-rule.yaml
         apiVersion: networking.istio.io/v1alpha3
         kind: DestinationRule
         metadata:
           name: hello-world
           namespace: default
         spec:
           host: hello-world.default.svc.cluster.local
           trafficPolicy:
             connectionPool:
               http:
                 http2MaxRequests: 100
             outlierDetection:
               consecutive5xxErrors: 1
               interval: 1s
               baseEjectionTime: 30s
               maxEjectionPercent: 100
             loadBalancer:
               localityLbSetting:
                 enabled: true
                 distribute:
                 - from: europe-west1
                   to:
                     europe-west1: 50
                     us-central1: 50
                 - from: us-central1
                   to:
                     us-central1: 50
                     europe-west1: 50
         EOF
         
         kubectl apply -f destination-rule.yaml
         




Note the following:

  * The **localityLbSetting** under the **DestinationRule** enables even traffic split and automatic failover.
  * **maxEjectionPercent** allows Istio to failover all traffic if every endpoint in a locality is unhealthy.
  * **distribute:** ensures an even 50/50 split between the clusters, based on the source cluster's region.
  * **failover:** is implicitly handled when one locality becomes unavailable — Istio routes 100% of traffic to the healthy region.
  * **outlierDetection:** ejects failing endpoints after minimal error thresholds.

**Warning:** When configuring subsets within a `VirtualService`, these settings take precedence over the automatic failover logic. If a specific subset lacks healthy pods, the service mesh won't automatically redirect traffic to another locality. Instead, the mesh continues to route traffic according to the defined weights, which can result in request failures if the target version or subset becomes unavailable 

## Validate

You can now validate this behavior by:

  1. Sending requests through the Ingress Gateway in Cluster A.
  2. Scaling down `hello-world` pods in `europe-west1` to 0.
  3. Observing traffic failover to `us-central1`.
  4. Scaling pods back up in `europe-west1` and verifying traffic split resumes.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
