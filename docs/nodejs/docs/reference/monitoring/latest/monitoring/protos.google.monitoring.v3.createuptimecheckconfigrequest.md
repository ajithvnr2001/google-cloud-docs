---
url: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.createuptimecheckconfigrequest
title: Class protos.google.monitoring.v3.CreateUptimeCheckConfigRequest (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:52.418528+00:00
---

# Class protos.google.monitoring.v3.CreateUptimeCheckConfigRequest (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.createuptimecheckconfigrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.monitoring.v3.CreateUptimeCheckConfigRequest (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.4.0  5.2.0  4.0.0  3.0.4  2.3.5 

Represents a CreateUptimeCheckConfigRequest.

## Implements

[protos.google.monitoring.v3.ICreateUptimeCheckConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.icreateuptimecheckconfigrequest)

## Package

[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.monitoring.v3.ICreateUptimeCheckConfigRequest);

Constructs a new CreateUptimeCheckConfigRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateUptimeCheckConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.icreateuptimecheckconfigrequest)`   
Properties to set  
  
## Properties 

### parent
    
    
    public parent: string;

CreateUptimeCheckConfigRequest parent.

### uptimeCheckConfig
    
    
    public uptimeCheckConfig?: (google.monitoring.v3.IUptimeCheckConfig|null);

CreateUptimeCheckConfigRequest uptimeCheckConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.monitoring.v3.ICreateUptimeCheckConfigRequest): google.monitoring.v3.CreateUptimeCheckConfigRequest;

Creates a new CreateUptimeCheckConfigRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateUptimeCheckConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.icreateuptimecheckconfigrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CreateUptimeCheckConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.createuptimecheckconfigrequest)` | CreateUptimeCheckConfigRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.monitoring.v3.CreateUptimeCheckConfigRequest;

Decodes a CreateUptimeCheckConfigRequest message from the specified reader or buffer.

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
`[CreateUptimeCheckConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.createuptimecheckconfigrequest)` | CreateUptimeCheckConfigRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.monitoring.v3.CreateUptimeCheckConfigRequest;

Decodes a CreateUptimeCheckConfigRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CreateUptimeCheckConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.createuptimecheckconfigrequest)` | CreateUptimeCheckConfigRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.monitoring.v3.ICreateUptimeCheckConfigRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateUptimeCheckConfigRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateUptimeCheckConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.icreateuptimecheckconfigrequest)`   
CreateUptimeCheckConfigRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.monitoring.v3.ICreateUptimeCheckConfigRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateUptimeCheckConfigRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateUptimeCheckConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.icreateuptimecheckconfigrequest)`   
CreateUptimeCheckConfigRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.monitoring.v3.CreateUptimeCheckConfigRequest;

Creates a CreateUptimeCheckConfigRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CreateUptimeCheckConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.createuptimecheckconfigrequest)` | CreateUptimeCheckConfigRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CreateUptimeCheckConfigRequest

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

Converts this CreateUptimeCheckConfigRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.monitoring.v3.CreateUptimeCheckConfigRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CreateUptimeCheckConfigRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CreateUptimeCheckConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.createuptimecheckconfigrequest)`   
CreateUptimeCheckConfigRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CreateUptimeCheckConfigRequest message.

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
