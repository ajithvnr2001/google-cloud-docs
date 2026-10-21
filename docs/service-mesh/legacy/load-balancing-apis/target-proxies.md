---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/target-proxies/
title: Target proxies for Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:02.521100+00:00
---

# Target proxies for Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/target-proxies/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Target proxies for Cloud Service Mesh

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

This document applies only to Cloud Service Mesh with the load balancing APIs. We strongly recommend that you use the [service routing APIs](https://docs.cloud.google.com/service-mesh/docs/service-routing/service-routing-overview) to deploy Cloud Service Mesh.

When you configure Cloud Service Mesh, one of the resources that you configure is the target proxy. In the context of Cloud Service Mesh, target proxies serve two primary purposes:

  * Defining the protocol that Cloud Service Mesh clients use when they open a connection to the backends or endpoints associated with a service.

  * Working with forwarding rules and URL maps to create a routing rule map. The routing rule map provides additional capabilities, such as routing rules, depending on the type of target proxy. Invalid selections are either hidden in the user interface or rejected by the API.


**Note:** To configure target TCP proxies, you can only use the Google Cloud CLI or the API.

## Target proxy types and request protocols

Cloud Service Mesh generates different configurations for its clients based on the type of target proxy that you configure. When you configure a target proxy type, the Cloud Service Mesh client uses a specific request protocol.

Target proxy | Request protocol  
---|---  
HTTPS | Clients initiate HTTPS connections  
HTTP | Clients initiate HTTP connections  
gRPC | Clients initiate gRPC connections  
TCP | Clients initiate TCP connections  
  
You aren't restricted to choosing only one type. For example, your application might want to use HTTP when addressing some services but use TCP when addressing other services. For such a use case, you need to create both a target HTTP proxy and a target TCP proxy.

## Valid resource combinations in a routing rule map

To avoid misconfigurations, Cloud Service Mesh only lets you create routing rule maps that look like the following:

  * Forwarding rule > global target HTTPS proxy > URL map > one or more backend services
  * Forwarding rule > global target HTTP proxy > URL map > one or more backend services
  * Forwarding rule > global target gRPC proxy > URL map > one or more backend services
  * Forwarding rule > global target TCP proxy > one backend service

**Note:** Health checks and backends are not shown in the preceding list.

If you're using the Google Cloud console to set up a target HTTP proxy, the target proxy is set up implicitly as part of your routing rule map configuration. TCP proxy setup is not yet supported in the Google Cloud console.

If you're using the Google Cloud CLI or the APIs, you need to configure the target proxy explicitly.

**Note:** Target proxies are also used for [certain Google Cloud load balancers](https://docs.cloud.google.com/load-balancing/docs/target-proxies). This page only discusses target proxies in the context of Cloud Service Mesh.

## Traffic handling

The following sections describe ways to handle traffic depending on the type of target proxy that you use.

### Using a target HTTP or HTTPS proxy

When you configure HTTP- or HTTPS-based services, each service instance generally has an Envoy proxy deployed alongside it. Cloud Service Mesh configures this Envoy proxy. It is part of your service mesh data plane and handles traffic as follows.

The Envoy proxy receives the outbound request. It then compares the request's destination IP address and port to the IP address and port configured in each forwarding rule that references a target HTTP or HTTPS proxy. If a match is found, the Envoy proxy evaluates the request according to the target proxy's corresponding URL map.

### Using a target TCP proxy

When you configure TCP-based services, each service instance generally has an Envoy proxy deployed alongside it. Cloud Service Mesh configures this Envoy proxy. It is part of your service mesh data plane and handles traffic as follows.

The Envoy proxy receives the outbound request. It then compares the request's destination IP address and port to the IP address and port configured in each forwarding rule that references a target TCP proxy. Each forwarding rule routes TCP traffic to a target proxy that points to a default backend service. The backend service specifies a health check and determines the appropriate backend.

### Using a target gRPC proxy

When you configure gRPC-based services, your service instances generally don't have Envoy proxies deployed alongside them. Instead, Cloud Service Mesh configures the gRPC library. The library is part of your service mesh data plane and handles traffic as follows.

The gRPC library compares the `hostname[:port]` specified in the URI to the host rules in all URL maps that a target gRPC proxy references. If a match is found, the gRPC library evaluates the request according to the path rules associated with the matching host rule.

## Target proxy resources

To add, delete, list, and get information about target proxies, you can use the REST API or the gcloud CLI.

In addition, to get information about a target proxy, you can use the following `gcloud` commands:
    
    
    gcloud compute [target-http-proxies | target-tcp-proxies | target-grpc-proxies] list
    
    
    
    gcloud compute [target-http-proxies | target-tcp-proxies | target-grpc-proxies] describe TARGET_PROXY_NAME
    

### APIs

For descriptions of the properties and methods available to you when working with target proxies through the [REST API](https://docs.cloud.google.com/compute/docs/reference/rest/v1), see the following resources that Cloud Service Mesh supports:

  * [TargetHttpsProxies](https://docs.cloud.google.com/compute/docs/reference/v1/targetHttpsProxies)
  * [TargetHttpProxies](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpProxies)
  * [TargetTcpProxies](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetTcpProxies)
  * [TargetGrpcProxies](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetGrpcProxies)



### gcloud CLI

For the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/compute), see the following resources:

  * [target-https-proxies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies)
  * [target-http-proxies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies)
  * [target-tcp-proxies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies)
  * [target-grpc-proxies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-grpc-proxies)



## What's next

  * To learn more about Cloud Service Mesh, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).
  * To deploy Cloud Service Mesh, see the [Guide to Cloud Service Mesh deployment documentation](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/deploy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
