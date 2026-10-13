---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WeightedBackendServiceOrBuilder
title: Interface WeightedBackendServiceOrBuilder (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:42.923375+00:00
---

# Interface WeightedBackendServiceOrBuilder (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WeightedBackendServiceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface WeightedBackendServiceOrBuilder (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public interface WeightedBackendServiceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBackendService()
    
    
    public abstract String getBackendService()

The full or partial URL to the default BackendService resource. Before forwarding the request to backendService, the load balancer applies any relevant headerActions specified as part of thisbackendServiceWeight.

`optional string backend_service = 306946058;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The backendService.  
  
### getBackendServiceBytes()
    
    
    public abstract ByteString getBackendServiceBytes()

The full or partial URL to the default BackendService resource. Before forwarding the request to backendService, the load balancer applies any relevant headerActions specified as part of thisbackendServiceWeight.

`optional string backend_service = 306946058;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for backendService.  
  
### getHeaderAction()
    
    
    public abstract HttpHeaderAction getHeaderAction()

Specifies changes to request and response headers that need to take effect for the selected backendService.

headerAction specified here take effect beforeheaderAction in the enclosing HttpRouteRule,PathMatcher and UrlMap.

headerAction is not supported for load balancers that have their loadBalancingScheme set to EXTERNAL.

Not supported when the URL map is bound to a target gRPC proxy that has validateForProxyless field set to true.

`optional .google.cloud.compute.v1.HttpHeaderAction header_action = 328077352;`

**Returns**  
---  
**Type** | **Description**  
`[HttpHeaderAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HttpHeaderAction)` | The headerAction.  
  
### getHeaderActionOrBuilder()
    
    
    public abstract HttpHeaderActionOrBuilder getHeaderActionOrBuilder()

Specifies changes to request and response headers that need to take effect for the selected backendService.

headerAction specified here take effect beforeheaderAction in the enclosing HttpRouteRule,PathMatcher and UrlMap.

headerAction is not supported for load balancers that have their loadBalancingScheme set to EXTERNAL.

Not supported when the URL map is bound to a target gRPC proxy that has validateForProxyless field set to true.

`optional .google.cloud.compute.v1.HttpHeaderAction header_action = 328077352;`

**Returns**  
---  
**Type** | **Description**  
`[HttpHeaderActionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HttpHeaderActionOrBuilder)` |   
  
### getWeight()
    
    
    public abstract int getWeight()

Specifies the fraction of traffic sent to a backend service, computed asweight / (sum of all weightedBackendService weights in routeAction).

The selection of a backend service is determined only for new traffic. Once a user's request has been directed to a backend service, subsequent requests are sent to the same backend service as determined by the backend service's session affinity policy. Don't configure session affinity if you're using weighted traffic splitting. If you do, the weighted traffic splitting configuration takes precedence.

The value must be from 0 to 1000.

`optional uint32 weight = 282149496;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The weight.  
  
### hasBackendService()
    
    
    public abstract boolean hasBackendService()

The full or partial URL to the default BackendService resource. Before forwarding the request to backendService, the load balancer applies any relevant headerActions specified as part of thisbackendServiceWeight.

`optional string backend_service = 306946058;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the backendService field is set.  
  
### hasHeaderAction()
    
    
    public abstract boolean hasHeaderAction()

Specifies changes to request and response headers that need to take effect for the selected backendService.

headerAction specified here take effect beforeheaderAction in the enclosing HttpRouteRule,PathMatcher and UrlMap.

headerAction is not supported for load balancers that have their loadBalancingScheme set to EXTERNAL.

Not supported when the URL map is bound to a target gRPC proxy that has validateForProxyless field set to true.

`optional .google.cloud.compute.v1.HttpHeaderAction header_action = 328077352;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the headerAction field is set.  
  
### hasWeight()
    
    
    public abstract boolean hasWeight()

Specifies the fraction of traffic sent to a backend service, computed asweight / (sum of all weightedBackendService weights in routeAction).

The selection of a backend service is determined only for new traffic. Once a user's request has been directed to a backend service, subsequent requests are sent to the same backend service as determined by the backend service's session affinity policy. Don't configure session affinity if you're using weighted traffic splitting. If you do, the weighted traffic splitting configuration takes precedence.

The value must be from 0 to 1000.

`optional uint32 weight = 282149496;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the weight field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
