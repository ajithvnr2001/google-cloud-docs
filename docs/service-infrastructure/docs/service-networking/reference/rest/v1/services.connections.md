---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections
title: REST Resource: services.connections \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:36.889734+00:00
---

# REST Resource: services.connections  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  REST Resource: services.connections Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Connection
    * JSON representation
  * Methods



## Resource: Connection

Represents a private connection resource. A private connection is implemented as a VPC Network Peering connection between a service producer's VPC network and a service consumer's VPC network.

JSON representation  
---  
      
    
    {
      "network": string,
      "reservedPeeringRanges": [
        string
      ],
      "peering": string,
      "service": string
    }  
  
Fields  
---  
`network` |  `string` Required. The name of the service consumer's VPC network that's connected to the service producer network, in the following format: `projects/{project}/global/networks/{network}`. `{project}` is a project number, such as in `12345` that includes the VPC service consumer's VPC network. `{network}` is the name of the service consumer's VPC network.  
`reservedPeeringRanges[]` |  `string` The name of one or more allocated IP address ranges for this service producer of type `PEERING`. Note that invoking connections.create method with a different range when connection is already established will not modify already provisioned service producer subnetworks. If connections.create method is invoked repeatedly to reconnect when peering connection had been disconnected on the consumer side, leaving this field empty will restore previously allocated IP ranges.  
`peering` |  `string` Output only. The name of the VPC Network Peering connection that was created by the service producer.  
`service` |  `string` Output only. The name of the peering service that's associated with this connection, in the following format: `services/{service name}`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections/create)`

|  Creates a private connection that establishes a VPC Network Peering connection to a VPC network in the service producer's organization.  
  
### `[deleteConnection](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections/deleteConnection)`

|  Deletes a private service access connection.  
  
### `[list](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections/list)`

|  List the private connections that are configured in a service consumer's VPC network.  
  
### `[patch](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections/patch)`

|  Updates the allocated ranges that are assigned to a connection.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-10 UTC."],[],[]] 
