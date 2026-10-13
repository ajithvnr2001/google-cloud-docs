---
url: https://docs.cloud.google.com/nodejs/docs/reference/notebooks/latest/notebooks/protos.google.cloud.notebooks.v1beta1.setinstancemachinetyperequest
title: Class protos.google.cloud.notebooks.v1beta1.SetInstanceMachineTypeRequest (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:50.987984+00:00
---

# Class protos.google.cloud.notebooks.v1beta1.SetInstanceMachineTypeRequest (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/notebooks/latest/notebooks/protos.google.cloud.notebooks.v1beta1.setinstancemachinetyperequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.notebooks.v1beta1.SetInstanceMachineTypeRequest (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  4.0.1  2.1.4  1.3.1  1.2.0  1.1.7 

Represents a SetInstanceMachineTypeRequest.

## Implements

[protos.google.cloud.notebooks.v1beta1.ISetInstanceMachineTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/notebooks/latest/notebooks/protos.google.cloud.notebooks.v1beta1.isetinstancemachinetyperequest)

## Package

[@google-cloud/notebooks](https://docs.cloud.google.com/nodejs/docs/reference/notebooks/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.notebooks.v1beta1.ISetInstanceMachineTypeRequest);

Constructs a new SetInstanceMachineTypeRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISetInstanceMachineTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/notebooks/latest/notebooks/protos.google.cloud.notebooks.v1beta1.isetinstancemachinetyperequest)`   
Properties to set  
  
## Properties 

### machineType
    
    
    public machineType: string;

SetInstanceMachineTypeRequest machineType.

### name
    
    
    public name: string;

SetInstanceMachineTypeRequest name.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.notebooks.v1beta1.ISetInstanceMachineTypeRequest): google.cloud.notebooks.v1beta1.SetInstanceMachineTypeRequest;

Creates a new SetInstanceMachineTypeRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISetInstanceMachineTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/notebooks/latest/notebooks/protos.google.cloud.notebooks.v1beta1.isetinstancemachinetyperequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SetInstanceMachineTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/notebooks/latest/notebooks/protos.google.cloud.notebooks.v1beta1.setinstancemachinetyperequest)` | SetInstanceMachineTypeRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.notebooks.v1beta1.SetInstanceMachineTypeRequest;

Decodes a SetInstanceMachineTypeRequest message from the specified reader or buffer.

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
`[SetInstanceMachineTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/notebooks/latest/notebooks/protos.google.cloud.notebooks.v1beta1.setinstancemachinetyperequest)` | SetInstanceMachineTypeRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.notebooks.v1beta1.SetInstanceMachineTypeRequest;

Decodes a SetInstanceMachineTypeRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SetInstanceMachineTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/notebooks/latest/notebooks/protos.google.cloud.notebooks.v1beta1.setinstancemachinetyperequest)` | SetInstanceMachineTypeRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.notebooks.v1beta1.ISetInstanceMachineTypeRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SetInstanceMachineTypeRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISetInstanceMachineTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/notebooks/latest/notebooks/protos.google.cloud.notebooks.v1beta1.isetinstancemachinetyperequest)`   
SetInstanceMachineTypeRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.notebooks.v1beta1.ISetInstanceMachineTypeRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SetInstanceMachineTypeRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISetInstanceMachineTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/notebooks/latest/notebooks/protos.google.cloud.notebooks.v1beta1.isetinstancemachinetyperequest)`   
SetInstanceMachineTypeRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.notebooks.v1beta1.SetInstanceMachineTypeRequest;

Creates a SetInstanceMachineTypeRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SetInstanceMachineTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/notebooks/latest/notebooks/protos.google.cloud.notebooks.v1beta1.setinstancemachinetyperequest)` | SetInstanceMachineTypeRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SetInstanceMachineTypeRequest

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

Converts this SetInstanceMachineTypeRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.notebooks.v1beta1.SetInstanceMachineTypeRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SetInstanceMachineTypeRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SetInstanceMachineTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/notebooks/latest/notebooks/protos.google.cloud.notebooks.v1beta1.setinstancemachinetyperequest)`   
SetInstanceMachineTypeRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SetInstanceMachineTypeRequest message.

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
