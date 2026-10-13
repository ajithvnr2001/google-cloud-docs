---
url: https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p3beta1.imageannotator-class
title: Class protos.google.cloud.vision.v1p3beta1.ImageAnnotator (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:16.046888+00:00
---

# Class protos.google.cloud.vision.v1p3beta1.ImageAnnotator (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p3beta1.imageannotator-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.vision.v1p3beta1.ImageAnnotator (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.3.5  5.2.0  4.3.2  4.2.1  4.0.3  3.1.3  3.0.1  2.4.2  2.3.8 

Represents an ImageAnnotator

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.vision.v1p3beta1.ImageAnnotator

## Package

[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ImageAnnotator service.

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

### asyncBatchAnnotateFiles(request, callback)
    
    
    public asyncBatchAnnotateFiles(request: google.cloud.vision.v1p3beta1.IAsyncBatchAnnotateFilesRequest, callback: google.cloud.vision.v1p3beta1.ImageAnnotator.AsyncBatchAnnotateFilesCallback): void;

Calls AsyncBatchAnnotateFiles.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAsyncBatchAnnotateFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p3beta1.iasyncbatchannotatefilesrequest)`   
AsyncBatchAnnotateFilesRequest message or plain object  
`callback` |  `[AsyncBatchAnnotateFilesCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### asyncBatchAnnotateFiles(request)
    
    
    public asyncBatchAnnotateFiles(request: google.cloud.vision.v1p3beta1.IAsyncBatchAnnotateFilesRequest): Promise<google.longrunning.Operation>;

Calls AsyncBatchAnnotateFiles.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAsyncBatchAnnotateFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p3beta1.iasyncbatchannotatefilesrequest)`   
AsyncBatchAnnotateFilesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.longrunning.operation)>` | Promise  
  
### batchAnnotateImages(request, callback)
    
    
    public batchAnnotateImages(request: google.cloud.vision.v1p3beta1.IBatchAnnotateImagesRequest, callback: google.cloud.vision.v1p3beta1.ImageAnnotator.BatchAnnotateImagesCallback): void;

Calls BatchAnnotateImages.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchAnnotateImagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p3beta1.ibatchannotateimagesrequest)`   
BatchAnnotateImagesRequest message or plain object  
`callback` |  `[BatchAnnotateImagesCallback](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchAnnotateImagesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchAnnotateImages(request)
    
    
    public batchAnnotateImages(request: google.cloud.vision.v1p3beta1.IBatchAnnotateImagesRequest): Promise<google.cloud.vision.v1p3beta1.BatchAnnotateImagesResponse>;

Calls BatchAnnotateImages.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchAnnotateImagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p3beta1.ibatchannotateimagesrequest)`   
BatchAnnotateImagesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vision.v1p3beta1.BatchAnnotateImagesResponse](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p3beta1.batchannotateimagesresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ImageAnnotator;

Creates new ImageAnnotator service using the specified rpc implementation.

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
`[ImageAnnotator](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/vision/protos.google.cloud.vision.v1p3beta1.imageannotator-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
