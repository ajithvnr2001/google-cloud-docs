---
url: https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.injectfaultrequest-class
title: Class protos.google.cloud.alloydb.v1.InjectFaultRequest (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:05.073314+00:00
---

# Class protos.google.cloud.alloydb.v1.InjectFaultRequest (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.injectfaultrequest-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.alloydb.v1.InjectFaultRequest (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  1.10.1  1.9.0  1.6.0  1.4.1  1.3.0  1.2.0  0.1.1 

Represents an InjectFaultRequest.

## Implements

[protos.google.cloud.alloydb.v1.IInjectFaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.iinjectfaultrequest)

## Package

[@google-cloud/alloydb](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.alloydb.v1.IInjectFaultRequest);

Constructs a new InjectFaultRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInjectFaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.iinjectfaultrequest)`   
Properties to set  
  
## Properties 

### faultType
    
    
    public faultType: (google.cloud.alloydb.v1.InjectFaultRequest.FaultType|keyof typeof google.cloud.alloydb.v1.InjectFaultRequest.FaultType);

InjectFaultRequest faultType.

### name
    
    
    public name: string;

InjectFaultRequest name.

### requestId
    
    
    public requestId: string;

InjectFaultRequest requestId.

### validateOnly
    
    
    public validateOnly: boolean;

InjectFaultRequest validateOnly.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.alloydb.v1.IInjectFaultRequest): google.cloud.alloydb.v1.InjectFaultRequest;

Creates a new InjectFaultRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInjectFaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.iinjectfaultrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[InjectFaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.injectfaultrequest-class)` | InjectFaultRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.alloydb.v1.InjectFaultRequest;

Decodes an InjectFaultRequest message from the specified reader or buffer.

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
`[InjectFaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.injectfaultrequest-class)` | InjectFaultRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.alloydb.v1.InjectFaultRequest;

Decodes an InjectFaultRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[InjectFaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.injectfaultrequest-class)` | InjectFaultRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.alloydb.v1.IInjectFaultRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified InjectFaultRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInjectFaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.iinjectfaultrequest)`   
InjectFaultRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.alloydb.v1.IInjectFaultRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified InjectFaultRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInjectFaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.iinjectfaultrequest)`   
InjectFaultRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.alloydb.v1.InjectFaultRequest;

Creates an InjectFaultRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[InjectFaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.injectfaultrequest-class)` | InjectFaultRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for InjectFaultRequest

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

Converts this InjectFaultRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.alloydb.v1.InjectFaultRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an InjectFaultRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[InjectFaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.injectfaultrequest-class)`   
InjectFaultRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an InjectFaultRequest message.

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
