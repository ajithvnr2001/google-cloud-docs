---
url: https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.apptopology-class
title: Class protos.google.cloud.apptopology.v1.AppTopology (0.3.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:01:00.509255+00:00
---

# Class protos.google.cloud.apptopology.v1.AppTopology (0.3.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.apptopology-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apptopology.v1.AppTopology (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.0 (latest)  0.1.0 

Represents an AppTopology

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.apptopology.v1.AppTopology

## Package

[@google-cloud/apptopology](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AppTopology service.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
  
## Methods 

### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AppTopology;

Creates new AppTopology service using the specified rpc implementation.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
**Returns**  
---  
**Type** | **Description**  
`[AppTopology](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.apptopology-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### generateDiscoveredResourcesTopology(request, callback)
    
    
    public generateDiscoveredResourcesTopology(request: google.cloud.apptopology.v1.IGenerateDiscoveredResourcesTopologyRequest, callback: google.cloud.apptopology.v1.AppTopology.GenerateDiscoveredResourcesTopologyCallback): void;

Calls GenerateDiscoveredResourcesTopology.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateDiscoveredResourcesTopologyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.igeneratediscoveredresourcestopologyrequest)`   
GenerateDiscoveredResourcesTopologyRequest message or plain object  
`callback` |  `[GenerateDiscoveredResourcesTopologyCallback](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateDiscoveredResourcesTopologyResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateDiscoveredResourcesTopology(request)
    
    
    public generateDiscoveredResourcesTopology(request: google.cloud.apptopology.v1.IGenerateDiscoveredResourcesTopologyRequest): Promise<google.cloud.apptopology.v1.GenerateDiscoveredResourcesTopologyResponse>;

Calls GenerateDiscoveredResourcesTopology.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateDiscoveredResourcesTopologyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.igeneratediscoveredresourcestopologyrequest)`   
GenerateDiscoveredResourcesTopologyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apptopology.v1.GenerateDiscoveredResourcesTopologyResponse](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.generatediscoveredresourcestopologyresponse)>` | Promise  
  
### getDomain(request, callback)
    
    
    public getDomain(request: google.cloud.apptopology.v1.IGetDomainRequest, callback: google.cloud.apptopology.v1.AppTopology.GetDomainCallback): void;

Calls GetDomain.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDomainRequest](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.igetdomainrequest)`   
GetDomainRequest message or plain object  
`callback` |  `[GetDomainCallback](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/overview.html)`   
Node-style callback called with the error, if any, and Domain  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDomain(request)
    
    
    public getDomain(request: google.cloud.apptopology.v1.IGetDomainRequest): Promise<google.cloud.apptopology.v1.Domain>;

Calls GetDomain.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDomainRequest](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.igetdomainrequest)`   
GetDomainRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apptopology.v1.Domain](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.domain)>` | Promise  
  
### getSchema(request, callback)
    
    
    public getSchema(request: google.cloud.apptopology.v1.IGetSchemaRequest, callback: google.cloud.apptopology.v1.AppTopology.GetSchemaCallback): void;

Calls GetSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSchemaRequest](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.igetschemarequest)`   
GetSchemaRequest message or plain object  
`callback` |  `[GetSchemaCallback](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/overview.html)`   
Node-style callback called with the error, if any, and Schema  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSchema(request)
    
    
    public getSchema(request: google.cloud.apptopology.v1.IGetSchemaRequest): Promise<google.cloud.apptopology.v1.Schema>;

Calls GetSchema.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSchemaRequest](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.igetschemarequest)`   
GetSchemaRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apptopology.v1.Schema](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.schema)>` | Promise  
  
### listDomains(request, callback)
    
    
    public listDomains(request: google.cloud.apptopology.v1.IListDomainsRequest, callback: google.cloud.apptopology.v1.AppTopology.ListDomainsCallback): void;

Calls ListDomains.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDomainsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.ilistdomainsrequest)`   
ListDomainsRequest message or plain object  
`callback` |  `[ListDomainsCallback](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDomainsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDomains(request)
    
    
    public listDomains(request: google.cloud.apptopology.v1.IListDomainsRequest): Promise<google.cloud.apptopology.v1.ListDomainsResponse>;

Calls ListDomains.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDomainsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.ilistdomainsrequest)`   
ListDomainsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apptopology.v1.ListDomainsResponse](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.listdomainsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
