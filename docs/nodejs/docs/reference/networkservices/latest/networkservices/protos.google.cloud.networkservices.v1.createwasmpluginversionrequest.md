---
url: https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.createwasmpluginversionrequest
title: Class protos.google.cloud.networkservices.v1.CreateWasmPluginVersionRequest (0.17.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:05:28.615586+00:00
---

# Class protos.google.cloud.networkservices.v1.CreateWasmPluginVersionRequest (0.17.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.createwasmpluginversionrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networkservices.v1.CreateWasmPluginVersionRequest (0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.13.0  0.12.0  0.9.0  0.8.1  0.7.0  0.2.1 

Represents a CreateWasmPluginVersionRequest.

## Implements

[protos.google.cloud.networkservices.v1.ICreateWasmPluginVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.icreatewasmpluginversionrequest)

## Package

[@google-cloud/networkservices](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.networkservices.v1.ICreateWasmPluginVersionRequest);

Constructs a new CreateWasmPluginVersionRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateWasmPluginVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.icreatewasmpluginversionrequest)`   
Properties to set  
  
## Properties 

### parent
    
    
    public parent: string;

CreateWasmPluginVersionRequest parent.

### wasmPluginVersion
    
    
    public wasmPluginVersion?: (google.cloud.networkservices.v1.IWasmPluginVersion|null);

CreateWasmPluginVersionRequest wasmPluginVersion.

### wasmPluginVersionId
    
    
    public wasmPluginVersionId: string;

CreateWasmPluginVersionRequest wasmPluginVersionId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.networkservices.v1.ICreateWasmPluginVersionRequest): google.cloud.networkservices.v1.CreateWasmPluginVersionRequest;

Creates a new CreateWasmPluginVersionRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateWasmPluginVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.icreatewasmpluginversionrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CreateWasmPluginVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.createwasmpluginversionrequest)` | CreateWasmPluginVersionRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.networkservices.v1.CreateWasmPluginVersionRequest;

Decodes a CreateWasmPluginVersionRequest message from the specified reader or buffer.

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
`[CreateWasmPluginVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.createwasmpluginversionrequest)` | CreateWasmPluginVersionRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.networkservices.v1.CreateWasmPluginVersionRequest;

Decodes a CreateWasmPluginVersionRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CreateWasmPluginVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.createwasmpluginversionrequest)` | CreateWasmPluginVersionRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.networkservices.v1.ICreateWasmPluginVersionRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateWasmPluginVersionRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateWasmPluginVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.icreatewasmpluginversionrequest)`   
CreateWasmPluginVersionRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.networkservices.v1.ICreateWasmPluginVersionRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateWasmPluginVersionRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateWasmPluginVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.icreatewasmpluginversionrequest)`   
CreateWasmPluginVersionRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.networkservices.v1.CreateWasmPluginVersionRequest;

Creates a CreateWasmPluginVersionRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CreateWasmPluginVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.createwasmpluginversionrequest)` | CreateWasmPluginVersionRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CreateWasmPluginVersionRequest

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

Converts this CreateWasmPluginVersionRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.networkservices.v1.CreateWasmPluginVersionRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CreateWasmPluginVersionRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CreateWasmPluginVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.createwasmpluginversionrequest)`   
CreateWasmPluginVersionRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CreateWasmPluginVersionRequest message.

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
