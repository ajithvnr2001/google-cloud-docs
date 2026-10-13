---
url: https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceBindings
title: REST Resource: projects.locations.serviceBindings \u00a0|\u00a0 Cloud Service Mesh v1.26 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:58.616981+00:00
---

# REST Resource: projects.locations.serviceBindings  |  Cloud Service Mesh v1.26  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceBindings

You are viewing archived v1.26 Service Mesh documentation.

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
  * [ v1.26 ](https://docs.cloud.google.com/service-mesh/v1.26/docs)



Send feedback 

#  REST Resource: projects.locations.serviceBindings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ServiceBinding
    * JSON representation
  * Methods



## Resource: ServiceBinding

ServiceBinding can be used to: - Bind a Service Directory Service to be used in a BackendService resource. This feature will be deprecated soon. - Bind a Private Service Connect producer service to be used in consumer Cloud Service Mesh or Application Load Balancers.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "createTime": string,
      "updateTime": string,
      "service": string,
      "serviceId": string,
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the ServiceBinding resource. It matches pattern `projects/*/locations/*/serviceBindings/<service_binding_name>`.  
`description` |  `string` Optional. A free-text description of the resource. Max length 1024 characters.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`service` |  `string` Optional. The full Service Directory Service name of the format `projects/*/locations/*/namespaces/*/services/*`. This field is for Service Directory integration which will be deprecated soon.  
`serviceId` |  `string` Output only. The unique identifier of the Service Directory Service against which the ServiceBinding resource is validated. This is populated when the Service Binding resource is used in another resource (like Backend Service). This is of the UUID4 format. This field is for Service Directory integration which will be deprecated soon.  
`labels` |  `map (key: string, value: string)` Optional. Set of label tags associated with the ServiceBinding resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceBindings/create)`

|  Creates a new ServiceBinding in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceBindings/delete)`

|  Deletes a single ServiceBinding.  
  
### `[get](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceBindings/get)`

|  Gets details of a single ServiceBinding.  
  
### `[list](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceBindings/list)`

|  Lists ServiceBinding in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-23 UTC."],[],[]] 
