---
url: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featurestoreonlineservingservice-class
title: Class protos.google.cloud.aiplatform.v1beta1.FeaturestoreOnlineServingService (7.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:55.804750+00:00
---

# Class protos.google.cloud.aiplatform.v1beta1.FeaturestoreOnlineServingService (7.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featurestoreonlineservingservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.aiplatform.v1beta1.FeaturestoreOnlineServingService (7.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.4.1 (latest)  7.3.0  6.10.0  6.9.0  6.8.1  6.6.0  6.4.0  6.3.0  6.2.0  6.1.0  6.0.0  5.14.0  5.13.0  3.15.0  3.13.0  3.11.0  3.10.1  3.9.0  3.7.0  3.6.0  3.4.0  3.3.0  3.0.0  2.12.0  2.11.0  2.10.0  2.7.0  2.6.1  2.5.0  2.3.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.11.0  1.7.2 

Represents a FeaturestoreOnlineServingService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.aiplatform.v1beta1.FeaturestoreOnlineServingService

## Package

[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new FeaturestoreOnlineServingService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): FeaturestoreOnlineServingService;

Creates new FeaturestoreOnlineServingService service using the specified rpc implementation.

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
`[FeaturestoreOnlineServingService](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.featurestoreonlineservingservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### readFeatureValues(request, callback)
    
    
    public readFeatureValues(request: google.cloud.aiplatform.v1beta1.IReadFeatureValuesRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreOnlineServingService.ReadFeatureValuesCallback): void;

Calls ReadFeatureValues.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadFeatureValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadfeaturevaluesrequest)`   
ReadFeatureValuesRequest message or plain object  
`callback` |  `[ReadFeatureValuesCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ReadFeatureValuesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### readFeatureValues(request)
    
    
    public readFeatureValues(request: google.cloud.aiplatform.v1beta1.IReadFeatureValuesRequest): Promise<google.cloud.aiplatform.v1beta1.ReadFeatureValuesResponse>;

Calls ReadFeatureValues.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IReadFeatureValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ireadfeaturevaluesrequest)`   
ReadFeatureValuesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.ReadFeatureValuesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.readfeaturevaluesresponse-class)>` | Promise  
  
### streamingReadFeatureValues(request, callback)
    
    
    public streamingReadFeatureValues(request: google.cloud.aiplatform.v1beta1.IStreamingReadFeatureValuesRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreOnlineServingService.StreamingReadFeatureValuesCallback): void;

Calls StreamingReadFeatureValues.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStreamingReadFeatureValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istreamingreadfeaturevaluesrequest)`   
StreamingReadFeatureValuesRequest message or plain object  
`callback` |  `[StreamingReadFeatureValuesCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ReadFeatureValuesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### streamingReadFeatureValues(request)
    
    
    public streamingReadFeatureValues(request: google.cloud.aiplatform.v1beta1.IStreamingReadFeatureValuesRequest): Promise<google.cloud.aiplatform.v1beta1.ReadFeatureValuesResponse>;

Calls StreamingReadFeatureValues.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IStreamingReadFeatureValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istreamingreadfeaturevaluesrequest)`   
StreamingReadFeatureValuesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.ReadFeatureValuesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.readfeaturevaluesresponse-class)>` | Promise  
  
### writeFeatureValues(request, callback)
    
    
    public writeFeatureValues(request: google.cloud.aiplatform.v1beta1.IWriteFeatureValuesRequest, callback: google.cloud.aiplatform.v1beta1.FeaturestoreOnlineServingService.WriteFeatureValuesCallback): void;

Calls WriteFeatureValues.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IWriteFeatureValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritefeaturevaluesrequest)`   
WriteFeatureValuesRequest message or plain object  
`callback` |  `[WriteFeatureValuesCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and WriteFeatureValuesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### writeFeatureValues(request)
    
    
    public writeFeatureValues(request: google.cloud.aiplatform.v1beta1.IWriteFeatureValuesRequest): Promise<google.cloud.aiplatform.v1beta1.WriteFeatureValuesResponse>;

Calls WriteFeatureValues.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IWriteFeatureValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iwritefeaturevaluesrequest)`   
WriteFeatureValuesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1beta1.WriteFeatureValuesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.writefeaturevaluesresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
