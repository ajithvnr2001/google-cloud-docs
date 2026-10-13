---
url: https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.createinstancerequest
title: Class protos.google.cloud.alloydb.v1.CreateInstanceRequest (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:53:52.876594+00:00
---

# Class protos.google.cloud.alloydb.v1.CreateInstanceRequest (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.createinstancerequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.alloydb.v1.CreateInstanceRequest (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  1.10.1  1.9.0  1.6.0  1.4.1  1.3.0  1.2.0  0.1.1 

Represents a CreateInstanceRequest.

## Implements

[protos.google.cloud.alloydb.v1.ICreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.icreateinstancerequest)

## Package

[@google-cloud/alloydb](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.alloydb.v1.ICreateInstanceRequest);

Constructs a new CreateInstanceRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.icreateinstancerequest)`   
Properties to set  
  
## Properties 

### instance
    
    
    public instance?: (google.cloud.alloydb.v1.IInstance|null);

CreateInstanceRequest instance.

### instanceId
    
    
    public instanceId: string;

CreateInstanceRequest instanceId.

### parent
    
    
    public parent: string;

CreateInstanceRequest parent.

### requestId
    
    
    public requestId: string;

CreateInstanceRequest requestId.

### validateOnly
    
    
    public validateOnly: boolean;

CreateInstanceRequest validateOnly.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.alloydb.v1.ICreateInstanceRequest): google.cloud.alloydb.v1.CreateInstanceRequest;

Creates a new CreateInstanceRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.icreateinstancerequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.createinstancerequest)` | CreateInstanceRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.alloydb.v1.CreateInstanceRequest;

Decodes a CreateInstanceRequest message from the specified reader or buffer.

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
`[CreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.createinstancerequest)` | CreateInstanceRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.alloydb.v1.CreateInstanceRequest;

Decodes a CreateInstanceRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.createinstancerequest)` | CreateInstanceRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.alloydb.v1.ICreateInstanceRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateInstanceRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.icreateinstancerequest)`   
CreateInstanceRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.alloydb.v1.ICreateInstanceRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateInstanceRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.icreateinstancerequest)`   
CreateInstanceRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.alloydb.v1.CreateInstanceRequest;

Creates a CreateInstanceRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.createinstancerequest)` | CreateInstanceRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CreateInstanceRequest

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

Converts this CreateInstanceRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.alloydb.v1.CreateInstanceRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CreateInstanceRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CreateInstanceRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.createinstancerequest)`   
CreateInstanceRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CreateInstanceRequest message.

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
