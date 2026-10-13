---
url: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.KubernetesConfig.GatewayServiceMesh
title: Class GatewayServiceMesh (2.12.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:42:56.357443+00:00
---

# Class GatewayServiceMesh (2.12.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.KubernetesConfig.GatewayServiceMesh

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GatewayServiceMesh (2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.0  2.9.0  2.8.0  2.7.1  2.6.3  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.0  1.19.1  1.18.1  1.17.3  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1  1.2.1  1.1.1  1.0.0  0.3.2  0.2.0  0.1.1 
    
    
    GatewayServiceMesh(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Information about the Kubernetes Gateway API service mesh configuration.

## Attributes  
  
---  
**Name** | **Description**  
`http_route` |  `str`   
Required. Name of the Gateway API HTTPRoute.   
`service` |  `str`   
Required. Name of the Kubernetes Service.   
`deployment` |  `str`   
Required. Name of the Kubernetes Deployment whose traffic is managed by the specified HTTPRoute and Service.   
`route_update_wait_time` |  `google.protobuf.duration_pb2.Duration`   
Optional. The time to wait for route updates to propagate. The maximum configurable time is 3 hours, in seconds format. If unspecified, there is no wait time.   
`stable_cutback_duration` |  `google.protobuf.duration_pb2.Duration`   
Optional. The amount of time to migrate traffic back from the canary Service to the original Service during the stable phase deployment. If specified, must be between 15s and 3600s. If unspecified, there is no cutback time.   
`pod_selector_label` |  `str`   
Optional. The label to use when selecting Pods for the Deployment and Service resources. This label must already be present in both resources.   
`route_destinations` |  `[google.cloud.deploy_v1.types.KubernetesConfig.GatewayServiceMesh.RouteDestinations](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.KubernetesConfig.GatewayServiceMesh.RouteDestinations)`   
Optional. Route destinations allow configuring the Gateway API HTTPRoute to be deployed to additional clusters. This option is available for multi-cluster service mesh set ups that require the route to exist in the clusters that call the service. If unspecified, the HTTPRoute will only be deployed to the Target cluster.   
  
## Classes 

### RouteDestinations
    
    
    RouteDestinations(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Information about route destinations for the Gateway API service mesh.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
