---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.createagentrequest
title: Class protos.google.cloud.ces.v1.CreateAgentRequest (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:05.368830+00:00
---

# Class protos.google.cloud.ces.v1.CreateAgentRequest (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.createagentrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ces.v1.CreateAgentRequest (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Represents a CreateAgentRequest.

## Implements

[protos.google.cloud.ces.v1.ICreateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreateagentrequest)

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ces.v1.ICreateAgentRequest);

Constructs a new CreateAgentRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreateagentrequest)`   
Properties to set  
  
## Properties 

### agent
    
    
    public agent?: (google.cloud.ces.v1.IAgent|null);

CreateAgentRequest agent.

### agentId
    
    
    public agentId: string;

CreateAgentRequest agentId.

### parent
    
    
    public parent: string;

CreateAgentRequest parent.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ces.v1.ICreateAgentRequest): google.cloud.ces.v1.CreateAgentRequest;

Creates a new CreateAgentRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreateagentrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CreateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.createagentrequest)` | CreateAgentRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ces.v1.CreateAgentRequest;

Decodes a CreateAgentRequest message from the specified reader or buffer.

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
`[CreateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.createagentrequest)` | CreateAgentRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ces.v1.CreateAgentRequest;

Decodes a CreateAgentRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CreateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.createagentrequest)` | CreateAgentRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ces.v1.ICreateAgentRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateAgentRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreateagentrequest)`   
CreateAgentRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ces.v1.ICreateAgentRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateAgentRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreateagentrequest)`   
CreateAgentRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ces.v1.CreateAgentRequest;

Creates a CreateAgentRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CreateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.createagentrequest)` | CreateAgentRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CreateAgentRequest

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

Converts this CreateAgentRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ces.v1.CreateAgentRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CreateAgentRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CreateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.createagentrequest)`   
CreateAgentRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CreateAgentRequest message.

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
