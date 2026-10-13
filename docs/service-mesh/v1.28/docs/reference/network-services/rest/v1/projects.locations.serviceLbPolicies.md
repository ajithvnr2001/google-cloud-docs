---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies
title: REST Resource: projects.locations.serviceLbPolicies \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:30.652765+00:00
---

# REST Resource: projects.locations.serviceLbPolicies  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies

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



Send feedback 

#  REST Resource: projects.locations.serviceLbPolicies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ServiceLbPolicy
    * JSON representation
  * LoadBalancingAlgorithm
  * AutoCapacityDrain
    * JSON representation
  * FailoverConfig
    * JSON representation
  * IsolationConfig
    * JSON representation
  * IsolationGranularity
  * IsolationMode
  * Methods



## Resource: ServiceLbPolicy

ServiceLbPolicy holds global load balancing and traffic distribution configuration that can be applied to a BackendService.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "description": string,
      "loadBalancingAlgorithm": enum ([LoadBalancingAlgorithm](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies#LoadBalancingAlgorithm)),
      "autoCapacityDrain": {
        object ([AutoCapacityDrain](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies#AutoCapacityDrain))
      },
      "failoverConfig": {
        object ([FailoverConfig](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies#FailoverConfig))
      },
      "isolationConfig": {
        object ([IsolationConfig](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies#IsolationConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the ServiceLbPolicy resource. It matches pattern `projects/{project}/locations/{location}/serviceLbPolicies/{service_lb_policy_name}`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this resource was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Set of label tags associated with the ServiceLbPolicy resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Optional. A free-text description of the resource. Max length 1024 characters.  
`loadBalancingAlgorithm` |  `enum (`[LoadBalancingAlgorithm](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies#LoadBalancingAlgorithm)`)` Optional. The type of load balancing algorithm to be used. The default behavior is WATERFALL_BY_REGION.  
`autoCapacityDrain` |  `object (`[AutoCapacityDrain](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies#AutoCapacityDrain)`)` Optional. Configuration to automatically move traffic away for unhealthy IG/NEG for the associated Backend Service.  
`failoverConfig` |  `object (`[FailoverConfig](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies#FailoverConfig)`)` Optional. Configuration related to health based failover.  
`isolationConfig` |  `object (`[IsolationConfig](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies#IsolationConfig)`)` Optional. Configuration to provide isolation support for the associated Backend Service.  
  
## LoadBalancingAlgorithm

The global load balancing algorithm to be used.

Enums  
---  
`LOAD_BALANCING_ALGORITHM_UNSPECIFIED` | The type of the loadbalancing algorithm is unspecified.  
`SPRAY_TO_WORLD` | Balance traffic across all backends across the world proportionally based on capacity.  
`SPRAY_TO_REGION` | Direct traffic to the nearest region with endpoints and capacity before spilling over to other regions and spread the traffic from each client to all the MIGs/NEGs in a region.  
`WATERFALL_BY_REGION` | Direct traffic to the nearest region with endpoints and capacity before spilling over to other regions. All MIGs/NEGs within a region are evenly loaded but each client might not spread the traffic to all the MIGs/NEGs in the region.  
`WATERFALL_BY_ZONE` | Attempt to keep traffic in a single zone closest to the client, before spilling over to other zones.  
  
## AutoCapacityDrain

Option to specify if an unhealthy IG/NEG should be considered for global load balancing and traffic routing.

JSON representation  
---  
      
    
    {
      "enable": boolean
    }  
  
Fields  
---  
`enable` |  `boolean` Optional. If set to 'True', an unhealthy IG/NEG will be set as drained. - An IG/NEG is considered unhealthy if less than 25% of the instances/endpoints in the IG/NEG are healthy. - This option will never result in draining more than 50% of the configured IGs/NEGs for the Backend Service.  
  
## FailoverConfig

Option to specify health based failover behavior. This is not related to Network load balancer FailoverPolicy.

JSON representation  
---  
      
    
    {
      "failoverHealthThreshold": integer
    }  
  
Fields  
---  
`failoverHealthThreshold` |  `integer` Optional. The percentage threshold that a load balancer will begin to send traffic to failover backends. If the percentage of endpoints in a MIG/NEG is smaller than this value, traffic would be sent to failover backends if possible. This field should be set to a value between 1 and 99. The default value is 50 for Global external HTTP(S) load balancer (classic) and Proxyless service mesh, and 70 for others.  
  
## IsolationConfig

Configuration to provide isolation support for the associated Backend Service.

JSON representation  
---  
      
    
    {
      "isolationGranularity": enum ([IsolationGranularity](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies#IsolationGranularity)),
      "isolationMode": enum ([IsolationMode](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies#IsolationMode))
    }  
  
Fields  
---  
`isolationGranularity` |  `enum (`[IsolationGranularity](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies#IsolationGranularity)`)` Optional. The isolation granularity of the load balancer.  
`isolationMode` |  `enum (`[IsolationMode](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies#IsolationMode)`)` Optional. The isolation mode of the load balancer.  
  
## IsolationGranularity

The granularity of this isolation restriction.

Enums  
---  
`ISOLATION_GRANULARITY_UNSPECIFIED` | No isolation is configured for the backend service. Traffic can overflow based on the load balancing algorithm.  
`REGION` | Traffic for this service will be isolated at the cloud region level.  
  
## IsolationMode

The mode of this isolation restriction, defining whether clients in a given region are allowed to reach out to another region.

Enums  
---  
`ISOLATION_MODE_UNSPECIFIED` | No isolation mode is configured for the backend service.  
`NEAREST` | Traffic will be sent to the nearest region.  
`STRICT` | Traffic will fail if no serving backends are available in the same region as the load balancer.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies/create)`

|  Creates a new ServiceLbPolicy in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies/delete)`

|  Deletes a single ServiceLbPolicy.  
  
### `[get](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies/get)`

|  Gets details of a single ServiceLbPolicy.  
  
### `[getIamPolicy](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies/list)`

|  Lists ServiceLbPolicies in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies/patch)`

|  Updates the parameters of a single ServiceLbPolicy.  
  
### `[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-28 UTC."],[],[]] 
