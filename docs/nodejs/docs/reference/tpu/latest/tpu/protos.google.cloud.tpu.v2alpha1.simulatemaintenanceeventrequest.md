---
url: https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2alpha1.simulatemaintenanceeventrequest
title: Class protos.google.cloud.tpu.v2alpha1.SimulateMaintenanceEventRequest (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:58:14.500577+00:00
---

# Class protos.google.cloud.tpu.v2alpha1.SimulateMaintenanceEventRequest (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2alpha1.simulatemaintenanceeventrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.tpu.v2alpha1.SimulateMaintenanceEventRequest (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  3.8.0  3.7.0  3.6.0  3.2.1  2.6.1  2.4.1  2.2.0  2.1.0  1.2.0  1.1.1  1.0.5 

Represents a SimulateMaintenanceEventRequest.

## Implements

[protos.google.cloud.tpu.v2alpha1.ISimulateMaintenanceEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2alpha1.isimulatemaintenanceeventrequest)

## Package

[@google-cloud/tpu](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.tpu.v2alpha1.ISimulateMaintenanceEventRequest);

Constructs a new SimulateMaintenanceEventRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISimulateMaintenanceEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2alpha1.isimulatemaintenanceeventrequest)`   
Properties to set  
  
## Properties 

### name
    
    
    public name: string;

SimulateMaintenanceEventRequest name.

### workerIds
    
    
    public workerIds: string[];

SimulateMaintenanceEventRequest workerIds.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.tpu.v2alpha1.ISimulateMaintenanceEventRequest): google.cloud.tpu.v2alpha1.SimulateMaintenanceEventRequest;

Creates a new SimulateMaintenanceEventRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISimulateMaintenanceEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2alpha1.isimulatemaintenanceeventrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SimulateMaintenanceEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2alpha1.simulatemaintenanceeventrequest)` | SimulateMaintenanceEventRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.tpu.v2alpha1.SimulateMaintenanceEventRequest;

Decodes a SimulateMaintenanceEventRequest message from the specified reader or buffer.

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
`[SimulateMaintenanceEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2alpha1.simulatemaintenanceeventrequest)` | SimulateMaintenanceEventRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.tpu.v2alpha1.SimulateMaintenanceEventRequest;

Decodes a SimulateMaintenanceEventRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SimulateMaintenanceEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2alpha1.simulatemaintenanceeventrequest)` | SimulateMaintenanceEventRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.tpu.v2alpha1.ISimulateMaintenanceEventRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SimulateMaintenanceEventRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISimulateMaintenanceEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2alpha1.isimulatemaintenanceeventrequest)`   
SimulateMaintenanceEventRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.tpu.v2alpha1.ISimulateMaintenanceEventRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SimulateMaintenanceEventRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISimulateMaintenanceEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2alpha1.isimulatemaintenanceeventrequest)`   
SimulateMaintenanceEventRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.tpu.v2alpha1.SimulateMaintenanceEventRequest;

Creates a SimulateMaintenanceEventRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SimulateMaintenanceEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2alpha1.simulatemaintenanceeventrequest)` | SimulateMaintenanceEventRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SimulateMaintenanceEventRequest

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

Converts this SimulateMaintenanceEventRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.tpu.v2alpha1.SimulateMaintenanceEventRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SimulateMaintenanceEventRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SimulateMaintenanceEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2alpha1.simulatemaintenanceeventrequest)`   
SimulateMaintenanceEventRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SimulateMaintenanceEventRequest message.

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
