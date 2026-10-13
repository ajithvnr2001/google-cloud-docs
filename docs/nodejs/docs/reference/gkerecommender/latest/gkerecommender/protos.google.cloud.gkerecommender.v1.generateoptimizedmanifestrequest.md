---
url: https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.generateoptimizedmanifestrequest
title: Class protos.google.cloud.gkerecommender.v1.GenerateOptimizedManifestRequest (0.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:49:06.598492+00:00
---

# Class protos.google.cloud.gkerecommender.v1.GenerateOptimizedManifestRequest (0.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.generateoptimizedmanifestrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gkerecommender.v1.GenerateOptimizedManifestRequest (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a GenerateOptimizedManifestRequest.

## Implements

[protos.google.cloud.gkerecommender.v1.IGenerateOptimizedManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.igenerateoptimizedmanifestrequest)

## Package

[@google-cloud/gkerecommender](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.gkerecommender.v1.IGenerateOptimizedManifestRequest);

Constructs a new GenerateOptimizedManifestRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGenerateOptimizedManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.igenerateoptimizedmanifestrequest)`   
Properties to set  
  
## Properties 

### acceleratorType
    
    
    public acceleratorType: string;

GenerateOptimizedManifestRequest acceleratorType.

### kubernetesNamespace
    
    
    public kubernetesNamespace: string;

GenerateOptimizedManifestRequest kubernetesNamespace.

### modelServerInfo
    
    
    public modelServerInfo?: (google.cloud.gkerecommender.v1.IModelServerInfo|null);

GenerateOptimizedManifestRequest modelServerInfo.

### performanceRequirements
    
    
    public performanceRequirements?: (google.cloud.gkerecommender.v1.IPerformanceRequirements|null);

GenerateOptimizedManifestRequest performanceRequirements.

### storageConfig
    
    
    public storageConfig?: (google.cloud.gkerecommender.v1.IStorageConfig|null);

GenerateOptimizedManifestRequest storageConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.gkerecommender.v1.IGenerateOptimizedManifestRequest): google.cloud.gkerecommender.v1.GenerateOptimizedManifestRequest;

Creates a new GenerateOptimizedManifestRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGenerateOptimizedManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.igenerateoptimizedmanifestrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GenerateOptimizedManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.generateoptimizedmanifestrequest)` | GenerateOptimizedManifestRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.gkerecommender.v1.GenerateOptimizedManifestRequest;

Decodes a GenerateOptimizedManifestRequest message from the specified reader or buffer.

**Parameters**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
`length` |  `number`   
Message length if known beforehand  
**Returns**  
---  
**Type** | **Description**  
`[GenerateOptimizedManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.generateoptimizedmanifestrequest)` | GenerateOptimizedManifestRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.gkerecommender.v1.GenerateOptimizedManifestRequest;

Decodes a GenerateOptimizedManifestRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GenerateOptimizedManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.generateoptimizedmanifestrequest)` | GenerateOptimizedManifestRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.gkerecommender.v1.IGenerateOptimizedManifestRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GenerateOptimizedManifestRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGenerateOptimizedManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.igenerateoptimizedmanifestrequest)`   
GenerateOptimizedManifestRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.gkerecommender.v1.IGenerateOptimizedManifestRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GenerateOptimizedManifestRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGenerateOptimizedManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.igenerateoptimizedmanifestrequest)`   
GenerateOptimizedManifestRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.gkerecommender.v1.GenerateOptimizedManifestRequest;

Creates a GenerateOptimizedManifestRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GenerateOptimizedManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.generateoptimizedmanifestrequest)` | GenerateOptimizedManifestRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GenerateOptimizedManifestRequest

**Parameter**  
---  
**Name** | **Description**  
`typeUrlPrefix` |  `string`   
your custom typeUrlPrefix(default "type.googleapis.com")  
**Returns**  
---  
**Type** | **Description**  
`string` | The default type url  
  
### toJSON()
    
    
    public toJSON(): { [k: string]: any };

Converts this GenerateOptimizedManifestRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.gkerecommender.v1.GenerateOptimizedManifestRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GenerateOptimizedManifestRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GenerateOptimizedManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gkerecommender/latest/gkerecommender/protos.google.cloud.gkerecommender.v1.generateoptimizedmanifestrequest)`   
GenerateOptimizedManifestRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GenerateOptimizedManifestRequest message.

**Parameter**  
---  
**Name** | **Description**  
`message` |  `{ [k: string]: any }`   
Plain object to verify  
**Returns**  
---  
**Type** | **Description**  
`(string|null)` | `null` if valid, otherwise the reason why it is not  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
