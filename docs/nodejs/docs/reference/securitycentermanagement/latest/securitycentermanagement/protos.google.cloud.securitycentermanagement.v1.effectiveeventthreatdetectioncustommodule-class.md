---
url: https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.cloud.securitycentermanagement.v1.effectiveeventthreatdetectioncustommodule-class
title: Class protos.google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:22.543109+00:00
---

# Class protos.google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.cloud.securitycentermanagement.v1.effectiveeventthreatdetectioncustommodule-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.4.0  0.3.0  0.1.0 

Represents an EffectiveEventThreatDetectionCustomModule.

## Implements

[protos.google.cloud.securitycentermanagement.v1.IEffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.cloud.securitycentermanagement.v1.ieffectiveeventthreatdetectioncustommodule)

## Package

[@google-cloud/securitycentermanagement](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.securitycentermanagement.v1.IEffectiveEventThreatDetectionCustomModule);

Constructs a new EffectiveEventThreatDetectionCustomModule.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.cloud.securitycentermanagement.v1.ieffectiveeventthreatdetectioncustommodule)`   
Properties to set  
  
## Properties 

### config
    
    
    public config?: (google.protobuf.IStruct|null);

EffectiveEventThreatDetectionCustomModule config.

### description
    
    
    public description: string;

EffectiveEventThreatDetectionCustomModule description.

### displayName
    
    
    public displayName: string;

EffectiveEventThreatDetectionCustomModule displayName.

### enablementState
    
    
    public enablementState: (google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule.EnablementState|keyof typeof google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule.EnablementState);

EffectiveEventThreatDetectionCustomModule enablementState.

### name
    
    
    public name: string;

EffectiveEventThreatDetectionCustomModule name.

### type
    
    
    public type: string;

EffectiveEventThreatDetectionCustomModule type.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.securitycentermanagement.v1.IEffectiveEventThreatDetectionCustomModule): google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule;

Creates a new EffectiveEventThreatDetectionCustomModule instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.cloud.securitycentermanagement.v1.ieffectiveeventthreatdetectioncustommodule)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.cloud.securitycentermanagement.v1.effectiveeventthreatdetectioncustommodule-class)` | EffectiveEventThreatDetectionCustomModule instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule;

Decodes an EffectiveEventThreatDetectionCustomModule message from the specified reader or buffer.

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
`[EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.cloud.securitycentermanagement.v1.effectiveeventthreatdetectioncustommodule-class)` | EffectiveEventThreatDetectionCustomModule  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule;

Decodes an EffectiveEventThreatDetectionCustomModule message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.cloud.securitycentermanagement.v1.effectiveeventthreatdetectioncustommodule-class)` | EffectiveEventThreatDetectionCustomModule  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.securitycentermanagement.v1.IEffectiveEventThreatDetectionCustomModule, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EffectiveEventThreatDetectionCustomModule message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.cloud.securitycentermanagement.v1.ieffectiveeventthreatdetectioncustommodule)`   
EffectiveEventThreatDetectionCustomModule message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.securitycentermanagement.v1.IEffectiveEventThreatDetectionCustomModule, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EffectiveEventThreatDetectionCustomModule message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.cloud.securitycentermanagement.v1.ieffectiveeventthreatdetectioncustommodule)`   
EffectiveEventThreatDetectionCustomModule message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule;

Creates an EffectiveEventThreatDetectionCustomModule message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.cloud.securitycentermanagement.v1.effectiveeventthreatdetectioncustommodule-class)` | EffectiveEventThreatDetectionCustomModule  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for EffectiveEventThreatDetectionCustomModule

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

Converts this EffectiveEventThreatDetectionCustomModule to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an EffectiveEventThreatDetectionCustomModule message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.cloud.securitycentermanagement.v1.effectiveeventthreatdetectioncustommodule-class)`   
EffectiveEventThreatDetectionCustomModule  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an EffectiveEventThreatDetectionCustomModule message.

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
