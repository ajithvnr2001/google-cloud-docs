---
url: https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.gkeinferencequickstart-class
title: Class protos.google.cloud.gkerecommender.v1.GkeInferenceQuickstart (0.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:49:06.899212+00:00
---

# Class protos.google.cloud.gkerecommender.v1.GkeInferenceQuickstart (0.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.gkeinferencequickstart-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gkerecommender.v1.GkeInferenceQuickstart (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a GkeInferenceQuickstart

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.gkerecommender.v1.GkeInferenceQuickstart

## Package

[@google-cloud/gkerecommender](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new GkeInferenceQuickstart service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): GkeInferenceQuickstart;

Creates new GkeInferenceQuickstart service using the specified rpc implementation.

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
`[GkeInferenceQuickstart](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.gkeinferencequickstart-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### fetchBenchmarkingData(request, callback)
    
    
    public fetchBenchmarkingData(request: google.cloud.gkerecommender.v1.IFetchBenchmarkingDataRequest, callback: google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchBenchmarkingDataCallback): void;

Calls FetchBenchmarkingData.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchBenchmarkingDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.ifetchbenchmarkingdatarequest)`   
FetchBenchmarkingDataRequest message or plain object  
`callback` |  `[FetchBenchmarkingDataCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/overview.html)`   
Node-style callback called with the error, if any, and FetchBenchmarkingDataResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchBenchmarkingData(request)
    
    
    public fetchBenchmarkingData(request: google.cloud.gkerecommender.v1.IFetchBenchmarkingDataRequest): Promise<google.cloud.gkerecommender.v1.FetchBenchmarkingDataResponse>;

Calls FetchBenchmarkingData.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchBenchmarkingDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.ifetchbenchmarkingdatarequest)`   
FetchBenchmarkingDataRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkerecommender.v1.FetchBenchmarkingDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.fetchbenchmarkingdataresponse)>` | Promise  
  
### fetchModels(request, callback)
    
    
    public fetchModels(request: google.cloud.gkerecommender.v1.IFetchModelsRequest, callback: google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelsCallback): void;

Calls FetchModels.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.ifetchmodelsrequest)`   
FetchModelsRequest message or plain object  
`callback` |  `[FetchModelsCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/overview.html)`   
Node-style callback called with the error, if any, and FetchModelsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchModels(request)
    
    
    public fetchModels(request: google.cloud.gkerecommender.v1.IFetchModelsRequest): Promise<google.cloud.gkerecommender.v1.FetchModelsResponse>;

Calls FetchModels.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.ifetchmodelsrequest)`   
FetchModelsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkerecommender.v1.FetchModelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.fetchmodelsresponse)>` | Promise  
  
### fetchModelServers(request, callback)
    
    
    public fetchModelServers(request: google.cloud.gkerecommender.v1.IFetchModelServersRequest, callback: google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelServersCallback): void;

Calls FetchModelServers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchModelServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.ifetchmodelserversrequest)`   
FetchModelServersRequest message or plain object  
`callback` |  `[FetchModelServersCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/overview.html)`   
Node-style callback called with the error, if any, and FetchModelServersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchModelServers(request)
    
    
    public fetchModelServers(request: google.cloud.gkerecommender.v1.IFetchModelServersRequest): Promise<google.cloud.gkerecommender.v1.FetchModelServersResponse>;

Calls FetchModelServers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchModelServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.ifetchmodelserversrequest)`   
FetchModelServersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkerecommender.v1.FetchModelServersResponse](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.fetchmodelserversresponse)>` | Promise  
  
### fetchModelServerVersions(request, callback)
    
    
    public fetchModelServerVersions(request: google.cloud.gkerecommender.v1.IFetchModelServerVersionsRequest, callback: google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelServerVersionsCallback): void;

Calls FetchModelServerVersions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchModelServerVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.ifetchmodelserverversionsrequest)`   
FetchModelServerVersionsRequest message or plain object  
`callback` |  `[FetchModelServerVersionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/overview.html)`   
Node-style callback called with the error, if any, and FetchModelServerVersionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchModelServerVersions(request)
    
    
    public fetchModelServerVersions(request: google.cloud.gkerecommender.v1.IFetchModelServerVersionsRequest): Promise<google.cloud.gkerecommender.v1.FetchModelServerVersionsResponse>;

Calls FetchModelServerVersions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchModelServerVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.ifetchmodelserverversionsrequest)`   
FetchModelServerVersionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkerecommender.v1.FetchModelServerVersionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.fetchmodelserverversionsresponse)>` | Promise  
  
### fetchProfiles(request, callback)
    
    
    public fetchProfiles(request: google.cloud.gkerecommender.v1.IFetchProfilesRequest, callback: google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchProfilesCallback): void;

Calls FetchProfiles.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchProfilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.ifetchprofilesrequest)`   
FetchProfilesRequest message or plain object  
`callback` |  `[FetchProfilesCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/overview.html)`   
Node-style callback called with the error, if any, and FetchProfilesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchProfiles(request)
    
    
    public fetchProfiles(request: google.cloud.gkerecommender.v1.IFetchProfilesRequest): Promise<google.cloud.gkerecommender.v1.FetchProfilesResponse>;

Calls FetchProfiles.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchProfilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.ifetchprofilesrequest)`   
FetchProfilesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkerecommender.v1.FetchProfilesResponse](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.fetchprofilesresponse)>` | Promise  
  
### generateOptimizedManifest(request, callback)
    
    
    public generateOptimizedManifest(request: google.cloud.gkerecommender.v1.IGenerateOptimizedManifestRequest, callback: google.cloud.gkerecommender.v1.GkeInferenceQuickstart.GenerateOptimizedManifestCallback): void;

Calls GenerateOptimizedManifest.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateOptimizedManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.igenerateoptimizedmanifestrequest)`   
GenerateOptimizedManifestRequest message or plain object  
`callback` |  `[GenerateOptimizedManifestCallback](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateOptimizedManifestResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateOptimizedManifest(request)
    
    
    public generateOptimizedManifest(request: google.cloud.gkerecommender.v1.IGenerateOptimizedManifestRequest): Promise<google.cloud.gkerecommender.v1.GenerateOptimizedManifestResponse>;

Calls GenerateOptimizedManifest.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateOptimizedManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.igenerateoptimizedmanifestrequest)`   
GenerateOptimizedManifestRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.gkerecommender.v1.GenerateOptimizedManifestResponse](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.generateoptimizedmanifestresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
