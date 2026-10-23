---
url: https://docs.cloud.google.com/service-mesh/v1.23/docs/managed-control-plane-overview/
title: Managed control plane for continuing customers \u00a0|\u00a0 Cloud Service Mesh v1.23 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:29.600970+00:00
---

# Managed control plane for continuing customers  |  Cloud Service Mesh v1.23  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.23/docs/managed-control-plane-overview/

You are viewing archived v1.23 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.23 ](https://docs.cloud.google.com/service-mesh/v1.23/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.23/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Managed control plane for continuing customers

This document is for you if you're a continuing Anthos Service Mesh customer using the managed control plane or in-cluster control plane. This document discusses your control plane implementation and the possible modernization of your control plane.

If you're a continuing Traffic Director customer or a new customer, you don't need to read this document. 

## Control plane overview

In service meshes, the control plane provides traffic management, proxy management when the Envoy proxy is in use, and other networking capabilities.

Anthos Service Mesh offered two control planes: a managed control plane and an in-cluster control plane. Only Envoy proxies are used as the data plane.

## New managed control plane

The new managed control plane is called the Traffic Director (TD) implementation. What does the new control plane mean for you?

One of the most significant changes from the Anthos Service Mesh product to Cloud Service Mesh is the move to a multi-tenant, global control plane.

The managed control plane used in Anthos Service Mesh is dedicated to a single cluster. Although the APIs (Istio CRDs) used for GKE are the same, and the xDS configuration sent to the sidecars is compatible with no behavioral differences, the control plane differences result in a few characteristics that are visible to you, the end user.

  * Configuration change response time. New service deployments, or changes to service policies, take slightly longer with the new control plane. 
    * The configuration pipeline performs a two-pass configuration commit for reliability purposes. The first pass performs validations to check whether the configuration is well formed. The subsequent phase propagates the configuration globally to your service deployments. To enable use of Google Cloud services, such as global cross-zonal or cross-region load balancing, centralized health checking, traffic-driven autoscaling, and managed rate limiting, the configuration is propagated to these systems and independently validated for correctness. The configuration is also stored internally in a manner that allows Google site reliability engineering to reliably and efficiently perform product operations during any production emergencies.
    * These operations provide better reliability, but they result in a config push that is slower than the latency observed by current users of Anthos Service Mesh.
    * The latency for any new Pod to fetch existing configuration is measured to be slightly better with the new control plane. The slow configuration push is for the first-time propagation of any new service created or any new policies pushed for the service. Endpoint propagation latencies are functionally similar.
  * Speed of scaling events and other changes to the endpoints. These are handled at least as quickly with the new control plane. These events include new Pods starting or stopping because of horizontal Pod autoscaling, and Pods restarting with new IP addresses because they were moved to a different node in the cluster.
  * Scaling the number of endpoints. With the new global control plane, the endpoints of the mesh are sent directly from each cluster to the control plane from across all clusters in the mesh. This is a simpler, faster, and more scalable approach than the previous managed control plane uses. In older managed control plane (dedicated control plane) model, each Istiod must communicate with every other cluster in the mesh to determine the endpoints available in every other cluster. With the global control plane, the endpoints are propagated directly to the global control plane. This results in better reliability and performance in meshes with large numbers of endpoints and allows the meshes to scale to a larger number of endpoints.



## How does the new control plane affect you?

How the new control plane affects you depends on the APIs and control plane that you are using.

  * If you are a Traffic Director user, your control plane remains the same. You don't need to read the rest of this guide. Documentation for your Cloud Service Mesh implementation is under **Configure with Google Cloud APIs**.
  * If you are an Anthos Service Mesh user, the next steps for the control plane in your existing deployment depend on whether you use the managed control plane or the in-cluster control plane. 
    * If you use the managed control plane, with some exceptions your existing fleets will be migrated to the new control plane, referred to in the Cloud Service Mesh as managed control plane (Traffic Director, or TD, implementation). Read the following section, Control plane modernization for existing meshes and fleets. If you are using a feature that isn't supported by the Traffic Director control plane implementation, you remain temporarily on the previous control plane. You should continue reading this guide.
    * If you use the in-cluster control plane, your control plane remains the same. You don't need to read the rest of this guide.
    * If you don't have a Google Cloud Organization, and you use the managed control plane on an organization-less project, you will receive the TD control plane.
  * If you are an Anthos Service Mesh customer and you are creating new fleets, you will receive the Traffic Director control plane implementation. You should continue reading this guide. 
    * You will be notified about the date when new fleets receive the TD control plane.



## Control plane modernization for existing meshes and fleets

See [managed control plane modernization](https://docs.cloud.google.com/service-mesh/v1.23/docs/modernization).

### Check control plane compatibility

Review [differences in supported features between managed control plane implementations](https://docs.cloud.google.com/service-mesh/v1.23/docs/supported-features-managed) to determine whether your current usage of Cloud Service Mesh will require changes.

## Control plane for new meshes

Starting on July 1, 2024, most existing users of the managed `istiod` control plane implementation began to receive the updated managed control plane with Google's globally available implementation - the Traffic Director (TD) control plane, in _new_ fleets.

Users whose existing usage of managed Cloud Service Mesh with the `istiod` control plane implementation was not compatible with the Traffic Director implementation without changes continued to get the `istiod` implementation until September 8, 2024.

A small number of users were further snowflaked to get continue getting the `istiod` control plane implementation in new fleets. If this applies to your organization then you received a Service Announcement.

If you onboard a new fleet to managed Cloud Service Mesh, and this fleet is not in a Google Cloud Organization or it is in a new Google Cloud Organization, then you will get the new managed control plane with the TD implementation from the Cloud Service Mesh launch date.

## What's next

  * If you're a continuing Anthos Service Mesh customer, your documentation is in the left-hand table of contents under **Configure service mesh with Istio APIs**.
  * If you're a continuing Traffic Director customer, your documentation is under **Configure service mesh with Google Cloud APIs**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
