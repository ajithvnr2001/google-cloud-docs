---
url: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.a2atask
title: Class protos.google.cloud.geminidataanalytics.v1alpha.A2ATask (0.13.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:37:51.803828+00:00
---

# Class protos.google.cloud.geminidataanalytics.v1alpha.A2ATask (0.13.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.a2atask

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.geminidataanalytics.v1alpha.A2ATask (0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.13.0  0.7.0  0.6.0  0.4.0  0.2.0 

Represents a A2ATask.

## Implements

[protos.google.cloud.geminidataanalytics.v1alpha.IA2ATask](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.ia2atask)

## Package

[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.geminidataanalytics.v1alpha.IA2ATask);

Constructs a new A2ATask.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IA2ATask](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.ia2atask)`   
Properties to set  
  
## Properties 

### artifacts
    
    
    public artifacts: google.cloud.geminidataanalytics.v1alpha.IA2AArtifact[];

A2ATask artifacts.

### contextId
    
    
    public contextId: string;

A2ATask contextId.

### history
    
    
    public history: google.cloud.geminidataanalytics.v1alpha.IA2AMessage[];

A2ATask history.

### id
    
    
    public id: string;

A2ATask id.

### metadata
    
    
    public metadata?: (google.protobuf.IStruct|null);

A2ATask metadata.

### status
    
    
    public status?: (google.cloud.geminidataanalytics.v1alpha.ITaskStatus|null);

A2ATask status.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.geminidataanalytics.v1alpha.IA2ATask): google.cloud.geminidataanalytics.v1alpha.A2ATask;

Creates a new A2ATask instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IA2ATask](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.ia2atask)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[A2ATask](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.a2atask)` | A2ATask instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.geminidataanalytics.v1alpha.A2ATask;

Decodes a A2ATask message from the specified reader or buffer.

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
`[A2ATask](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.a2atask)` | A2ATask  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.geminidataanalytics.v1alpha.A2ATask;

Decodes a A2ATask message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[A2ATask](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.a2atask)` | A2ATask  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.geminidataanalytics.v1alpha.IA2ATask, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified A2ATask message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IA2ATask](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.ia2atask)`   
A2ATask message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.geminidataanalytics.v1alpha.IA2ATask, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified A2ATask message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IA2ATask](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.ia2atask)`   
A2ATask message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.geminidataanalytics.v1alpha.A2ATask;

Creates a A2ATask message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[A2ATask](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.a2atask)` | A2ATask  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for A2ATask

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

Converts this A2ATask to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.geminidataanalytics.v1alpha.A2ATask, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a A2ATask message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[A2ATask](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1alpha.a2atask)`   
A2ATask  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a A2ATask message.

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
