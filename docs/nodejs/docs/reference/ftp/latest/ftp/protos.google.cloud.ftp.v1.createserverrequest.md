---
url: https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.createserverrequest
title: Class protos.google.cloud.ftp.v1.CreateServerRequest (0.3.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:19.985518+00:00
---

# Class protos.google.cloud.ftp.v1.CreateServerRequest (0.3.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.createserverrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ftp.v1.CreateServerRequest (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a CreateServerRequest.

## Implements

[protos.google.cloud.ftp.v1.ICreateServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.icreateserverrequest)

## Package

[@google-cloud/ftp](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ftp.v1.ICreateServerRequest);

Constructs a new CreateServerRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.icreateserverrequest)`   
Properties to set  
  
## Properties 

### parent
    
    
    public parent: string;

CreateServerRequest parent.

### requestId
    
    
    public requestId: string;

CreateServerRequest requestId.

### server
    
    
    public server?: (google.cloud.ftp.v1.IServer|null);

CreateServerRequest server.

### serverId
    
    
    public serverId: string;

CreateServerRequest serverId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ftp.v1.ICreateServerRequest): google.cloud.ftp.v1.CreateServerRequest;

Creates a new CreateServerRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.icreateserverrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CreateServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.createserverrequest)` | CreateServerRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ftp.v1.CreateServerRequest;

Decodes a CreateServerRequest message from the specified reader or buffer.

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
`[CreateServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.createserverrequest)` | CreateServerRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ftp.v1.CreateServerRequest;

Decodes a CreateServerRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CreateServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.createserverrequest)` | CreateServerRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ftp.v1.ICreateServerRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateServerRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.icreateserverrequest)`   
CreateServerRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ftp.v1.ICreateServerRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateServerRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.icreateserverrequest)`   
CreateServerRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ftp.v1.CreateServerRequest;

Creates a CreateServerRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CreateServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.createserverrequest)` | CreateServerRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CreateServerRequest

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

Converts this CreateServerRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ftp.v1.CreateServerRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CreateServerRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CreateServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.createserverrequest)`   
CreateServerRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CreateServerRequest message.

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
