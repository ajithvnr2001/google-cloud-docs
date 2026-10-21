---
url: https://docs.cloud.google.com/service-mesh/v1.29/docs/gateway/reference/
title: Reference \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:42.625644+00:00
---

# Reference  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.29/docs/gateway/reference/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.29/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Reference

This page describes the Gateway and Vendor extension resources.

## API Resources

With Gateway for Mesh an xRoute typically uses a Kubernetes Service as the [`parentRef`](https://gateway-api.sigs.k8s.io/geps/gep-1426/#api). When used this way, the parent Service becomes the "service frontend" for the client to call where the service gets an automatically allocated DNS name (`name.namespace.svc.cluster.local`) and IP address (`ClusterIP`). A proxyless gRPC client then uses the channel URI to access the service at

`xds:///SERVICE_NAME.NAMESPACE_NAME.svc.cluster.local:${PORT}`

### HTTPRoute

The HTTPRoute API specification, a key component of the Kubernetes Gateway API, defines a resource for routing HTTP traffic within Kubernetes. It allows users to specify fine-grained routing rules for HTTP traffic - based on attributes like hostnames, paths, headers, and methods, determine how requests are directed within the cluster. HTTPRoute can also be attached to Gateways, which act as entry points for traffic into the cluster.

For more information, see [HTTPRoute](https://gateway-api.sigs.k8s.io/api-types/httproute/).

### GRPCRoute

The GRPCRoute API specification is part of the Kubernetes Gateway API and defines a resource for routing gRPC traffic within a Kubernetes cluster. It lets users specify how gRPC requests should be matched and directed to backend services based on criteria like hostnames, gRPC methods, and headers. You can also attach GRPCRoutes to Gateways which act as entry points for traffic into the cluster. This specification enables fine-grained control over gRPC traffic routing, making it a valuable tool for managing gRPC-based applications in Kubernetes.

For more information, see [GRPCRoute](https://gateway-api.sigs.k8s.io/api-types/grpcroute/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
