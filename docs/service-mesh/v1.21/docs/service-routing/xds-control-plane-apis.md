---
url: https://docs.cloud.google.com/service-mesh/v1.21/docs/service-routing/xds-control-plane-apis/
title: xDS control plane APIs \u00a0|\u00a0 Cloud Service Mesh v1.22 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:25.149548+00:00
---

# xDS control plane APIs  |  Cloud Service Mesh v1.22  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.21/docs/service-routing/xds-control-plane-apis/

You are viewing archived v1.22 Service Mesh documentation.

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
  * [ v1.22 ](https://docs.cloud.google.com/service-mesh/v1.22/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# xDS control plane APIs

Cloud Service Mesh and its clients (Envoy proxies or proxyless gRPC libraries) use the [open source xDS API](https://www.envoyproxy.io/docs/envoy/latest/api/api) to exchange information. When you configure Cloud Service Mesh—for example, by using resources such as forwarding rules and backend services—Cloud Service Mesh converts these resources to an xDS configuration, which it shares with its clients.

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

## xDS version support

Cloud Service Mesh supports xDS v3 only.

To determine which Envoy and gRPC versions support xDS v3, see the [Envoy](https://www.envoyproxy.io/docs/envoy/latest/api/api_supported_versions) and [gRPC](https://github.com/grpc/grpc/blob/master/doc/grpc_xds_features.md) documentation.

If you are still using xDS v2, use the following instructions to migrate to xDS v3.

## Migrate from xDS v2 to xDS v3

There are two steps in the migration process:

  1. Update the Identity and Access Management (IAM) permissions granted to the service account that your clients (Envoy proxies or proxyless gRPC libraries) use when connecting to Cloud Service Mesh.
  2. Update and redeploy your applications. The specific steps vary depending on your deployment and are explained in the following sections.



### Update the service account's IAM permissions

Make sure that the service account used by your Cloud Service Mesh clients (Envoy, proxyless gRPC) has the `trafficdirector.networks.reportMetrics` and `trafficdirector.networks.getConfigs` permissions. These permissions are included in the IAM [Traffic Director Client role](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#trafficdirector.client) (`roles/trafficdirector.client`).

If you are using a custom IAM role, you can add these permissions to the custom role. After you add the permissions, you can remove the Compute Network Viewer role (`roles/compute.networkViewer`), the Compute Network Admin role (`roles/compute.networkAdmin`), or both from the service account.

We recommend that you use the Cloud Service Mesh Client role instead of the Compute Network Viewer role (`roles/compute.networkViewer`) or the Compute Network Admin role (`roles/compute.networkAdmin`). Using the Cloud Service Mesh Client role restricts the permissions granted to the service account and avoids granting overly broad permissions.

### Update your applications

After you update the IAM permissions on the service account, update your applications.

#### Envoy on Compute Engine

To update your applications on Envoy with Compute Engine, do a [rolling restart or replacement](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#starting_a_basic_rolling_update) of the managed instance groups. A version of Envoy that supports xDS v3 is automatically added to your virtual machine (VM) instances.

#### Envoy on GKE

If you use automatic Envoy injection with Google Kubernetes Engine (GKE), [re-install the sidecar injector](https://docs.cloud.google.com/service-mesh/docs/set-up-gke-pods-auto#installing_the_sidecar_injector_to_your_cluster) on the GKE clusters that you are using with Cloud Service Mesh. When a new Pod is created, an Envoy sidecar proxy that supports xDS v3 is automatically injected alongside your workload Pod.

If you use manual sidecar injection on GKE, [redeploy the sidecar proxy](https://docs.cloud.google.com/service-mesh/docs/set-up-gke-pods#injecting_a_sidecar_proxy_into_kubernetes_pods) on each of your GKE clusters.

There are two steps in the migration process:

  1. Ensure that the version of gRPC that you use supports xDS v3. For more information, see [xDS features in gRPC](https://github.com/grpc/grpc/blob/master/doc/grpc_xds_features.md).

  2. Update the bootstrap configuration by using the following steps:

     1. In the `"xds_servers"` field, add `"server_features": ["xds_v3"]` as shown in this [bootstrap file example](https://docs.cloud.google.com/service-mesh/v1.22/docs/service-routing/prepare-service-routing-envoy-proxyless#bootstrap_file).
     2. The node ID must be in the following format as shown in the previous example:
            
            "projects/PROJECT_NUMBER/networks/NETWORK_NAME/nodes/ID"
            


**Note:** Per policy, we encourage users to check for updates of the TD gRPC bootstrap generator yearly.

After you make the preceding changes to your application, build and redeploy it.

The preceding changes to the bootstrap configuration don't affect gRPC versions that don't support xDS v3. Also, if the preceding changes are not present in the bootstrap configuration, then gRPC versions that support xDS v3 use xDS v2.

For your convenience, you can use [Cloud Service Mesh gRPC bootstrap generator version 0.19.0](https://github.com/GoogleCloudPlatform/traffic-director-grpc-bootstrap/releases/tag/v0.19.0) or later to generate an xDS v3-compatible bootstrap configuration.

## Verify that Cloud Service Mesh clients are using xDS v3

To inspect the configuration that Cloud Service Mesh generates for its clients, you can use the [client status tool](https://docs.cloud.google.com/service-mesh/v1.22/docs/service-routing/client-status). This tool states whether the configuration is xDS v2 or xDS v3.

## What's next

  * To find general Cloud Service Mesh troubleshooting information, see [Troubleshoot Envoy deployments](https://docs.cloud.google.com/service-mesh/v1.22/docs/service-routing/troubleshooting).
  * To resolve configuration issues when you deploy proxyless gRPC services, see [Troubleshoot proxyless gRPC deployments](https://docs.cloud.google.com/service-mesh/v1.22/docs/service-routing/troubleshooting-proxyless).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
