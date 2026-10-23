---
url: https://docs.cloud.google.com/service-mesh/v1.24/docs/migrate/modernization-configuration-updates/
title: Configuration updates for modernization \u00a0|\u00a0 Cloud Service Mesh v1.24 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:10.975464+00:00
---

# Configuration updates for modernization  |  Cloud Service Mesh v1.24  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.24/docs/migrate/modernization-configuration-updates/

You are viewing archived v1.24 Service Mesh documentation.

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
  * [ v1.24 ](https://docs.cloud.google.com/service-mesh/v1.24/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configuration updates for modernization

This document describes configuration updates you may need to make to your managed Cloud Service Mesh before modernizing your mesh to the `TRAFFIC_DIRECTOR` control plane from the `ISTIOD` control plane.

For more information on the modernization workflow, see the [Managed control plane modernization](https://docs.cloud.google.com/service-mesh/v1.24/docs/modernization) page.

## Migrate from Istio secrets to multicluster_mode

Multi-cluster secrets are not supported when a cluster is using the `TRAFFIC_DIRECTOR` control plane. This document describes how you can modernize from using Istio multi-cluster secrets to using `multicluster_mode`.

### Istio secrets versus declarative API overview

[Open source istio multi-cluster](https://istio.io/latest/docs/setup/install/multicluster/) endpoint discovery works by using `istioctl` or other tools to create a [Kubernetes Secret](https://kubernetes.io/docs/concepts/configuration/secret/) in a cluster. This secret allows a cluster to load balance traffic to another cluster in the mesh. The `ISTIOD` control plane then reads this secret and begins routing traffic to that other cluster.

Cloud Service Mesh has a [declarative API](https://docs.cloud.google.com/service-mesh/v1.24/docs/operate-and-maintain/multi-cluster#endpoint-discovery-declarative-api) to control multi-cluster traffic instead of directly creating Istio secrets. This API treats Istio secrets as an implementation detail and is more reliable than creating Istio secrets manually. Future Cloud Service Mesh features will depend on the declarative API, and you won't be able to use those new features with Istio secrets directly. The declarative API is the only supported path forward.

If you are using Istio Secrets, migrate to using the declarative API as soon as possible. Note that the `multicluster_mode` setting directs each cluster to direct traffic to every other cluster in the mesh. Using secrets allows a more flexible configuration, letting you configure for each cluster which other cluster it should direct traffic to in the mesh. For a full list of the differences between the supported features of the declarative API and Istio secrets, see [Supported features using Istio APIs](https://docs.cloud.google.com/service-mesh/v1.24/docs/supported-features-managed#multi-cluster_deployment).

**Important:** With the declarative API, an entire cluster is opted into endpoint discovery at a time. This means that every cluster with `multicluster_mode=connected` will discover endpoints for every other cluster in the fleet that also has `multicluster_mode=connected`. 

### Migrate from Istio secrets to declarative API

If you provisioned Cloud Service Mesh using automatic management with the [fleet feature API](https://docs.cloud.google.com/service-mesh/v1.24/docs/onboarding/provision-control-plane), you don't need to follow these instructions. These steps only apply if you onboarded using `asmcli --managed`.

Note, this process changes secrets that point to a cluster. During this process, the endpoints are removed and then re-added. In between the endpoints being removed and added, the traffic will briefly revert to routing locally instead of load balancing to other clusters. For more information, see the [GitHub issue](https://github.com/istio/istio/issues/36365).

To move from using Istio secrets to the declarative API, follow these steps. Execute these steps at the same time or in close succession:

  1. Enable the declarative API for each cluster in the fleet where you want to enable multi cluster endpoint discovery by setting `multicluster_mode=connected`. Note that you need to explicitly set `multicluster_mode=disconnected` if you don't want the cluster to be discoverable.

Use the following command to opt in a cluster for multi cluster endpoint discovery:
         
         kubectl patch configmap/asm-options -n istio-system --type merge -p '{"data":{"multicluster_mode":"connected"}}'
         

Use the following command to opt a cluster out of endpoint discovery:
         
         kubectl patch configmap/asm-options -n istio-system --type merge -p '{"data":{"multicluster_mode":"disconnected"}}'
         

  2. Delete old secrets.

After setting `multicluster_mode=connected` on your clusters, each cluster will have a new secret generated for every other cluster that also has `multicluster_mode=connected` set. The secret is placed in the istio-system namespace and have the following format:
         
         istio-remote-secret-projects-PROJECT_NAME-locations-LOCATION-memberships-MEMBERSHIPS
         

Each secret will also have the label `istio.io/owned-by: mesh.googleapis.com` applied.

Once the new secrets are created, you can delete any secrets manually created with `istioctl create-remote-secret`:
         
         kubectl delete secret SECRET_NAME -n istio-system
         




Once migrated, check your request metrics to make sure they're routed as expected.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
