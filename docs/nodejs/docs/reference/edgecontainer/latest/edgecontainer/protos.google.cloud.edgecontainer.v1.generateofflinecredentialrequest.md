---
url: https://docs.cloud.google.com/nodejs/docs/reference/edgecontainer/latest/edgecontainer/protos.google.cloud.edgecontainer.v1.generateofflinecredentialrequest
title: Class protos.google.cloud.edgecontainer.v1.GenerateOfflineCredentialRequest (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:35.658461+00:00
---

# Class protos.google.cloud.edgecontainer.v1.GenerateOfflineCredentialRequest (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/edgecontainer/latest/edgecontainer/protos.google.cloud.edgecontainer.v1.generateofflinecredentialrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.edgecontainer.v1.GenerateOfflineCredentialRequest (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.7.0  0.6.1  0.3.0 

Represents a GenerateOfflineCredentialRequest.

## Implements

[protos.google.cloud.edgecontainer.v1.IGenerateOfflineCredentialRequest](https://docs.cloud.google.com/nodejs/docs/reference/edgecontainer/latest/edgecontainer/protos.google.cloud.edgecontainer.v1.igenerateofflinecredentialrequest)

## Package

[@google-cloud/edgecontainer](https://docs.cloud.google.com/nodejs/docs/reference/edgecontainer/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.edgecontainer.v1.IGenerateOfflineCredentialRequest);

Constructs a new GenerateOfflineCredentialRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGenerateOfflineCredentialRequest](https://docs.cloud.google.com/nodejs/docs/reference/edgecontainer/latest/edgecontainer/protos.google.cloud.edgecontainer.v1.igenerateofflinecredentialrequest)`   
Properties to set  
  
## Properties 

### cluster
    
    
    public cluster: string;

GenerateOfflineCredentialRequest cluster.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.edgecontainer.v1.IGenerateOfflineCredentialRequest): google.cloud.edgecontainer.v1.GenerateOfflineCredentialRequest;

Creates a new GenerateOfflineCredentialRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGenerateOfflineCredentialRequest](https://docs.cloud.google.com/nodejs/docs/reference/edgecontainer/latest/edgecontainer/protos.google.cloud.edgecontainer.v1.igenerateofflinecredentialrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GenerateOfflineCredentialRequest](https://docs.cloud.google.com/nodejs/docs/reference/edgecontainer/latest/edgecontainer/protos.google.cloud.edgecontainer.v1.generateofflinecredentialrequest)` | GenerateOfflineCredentialRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.edgecontainer.v1.GenerateOfflineCredentialRequest;

Decodes a GenerateOfflineCredentialRequest message from the specified reader or buffer.

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
`[GenerateOfflineCredentialRequest](https://docs.cloud.google.com/nodejs/docs/reference/edgecontainer/latest/edgecontainer/protos.google.cloud.edgecontainer.v1.generateofflinecredentialrequest)` | GenerateOfflineCredentialRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.edgecontainer.v1.GenerateOfflineCredentialRequest;

Decodes a GenerateOfflineCredentialRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GenerateOfflineCredentialRequest](https://docs.cloud.google.com/nodejs/docs/reference/edgecontainer/latest/edgecontainer/protos.google.cloud.edgecontainer.v1.generateofflinecredentialrequest)` | GenerateOfflineCredentialRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.edgecontainer.v1.IGenerateOfflineCredentialRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GenerateOfflineCredentialRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGenerateOfflineCredentialRequest](https://docs.cloud.google.com/nodejs/docs/reference/edgecontainer/latest/edgecontainer/protos.google.cloud.edgecontainer.v1.igenerateofflinecredentialrequest)`   
GenerateOfflineCredentialRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.edgecontainer.v1.IGenerateOfflineCredentialRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GenerateOfflineCredentialRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGenerateOfflineCredentialRequest](https://docs.cloud.google.com/nodejs/docs/reference/edgecontainer/latest/edgecontainer/protos.google.cloud.edgecontainer.v1.igenerateofflinecredentialrequest)`   
GenerateOfflineCredentialRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.edgecontainer.v1.GenerateOfflineCredentialRequest;

Creates a GenerateOfflineCredentialRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GenerateOfflineCredentialRequest](https://docs.cloud.google.com/nodejs/docs/reference/edgecontainer/latest/edgecontainer/protos.google.cloud.edgecontainer.v1.generateofflinecredentialrequest)` | GenerateOfflineCredentialRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GenerateOfflineCredentialRequest

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

Converts this GenerateOfflineCredentialRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.edgecontainer.v1.GenerateOfflineCredentialRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GenerateOfflineCredentialRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GenerateOfflineCredentialRequest](https://docs.cloud.google.com/nodejs/docs/reference/edgecontainer/latest/edgecontainer/protos.google.cloud.edgecontainer.v1.generateofflinecredentialrequest)`   
GenerateOfflineCredentialRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GenerateOfflineCredentialRequest message.

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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
