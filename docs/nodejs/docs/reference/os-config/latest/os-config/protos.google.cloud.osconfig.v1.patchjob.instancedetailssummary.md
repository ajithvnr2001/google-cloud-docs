---
url: https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.patchjob.instancedetailssummary
title: Class protos.google.cloud.osconfig.v1.PatchJob.InstanceDetailsSummary (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:36.823084+00:00
---

# Class protos.google.cloud.osconfig.v1.PatchJob.InstanceDetailsSummary (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.patchjob.instancedetailssummary

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.osconfig.v1.PatchJob.InstanceDetailsSummary (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  4.0.1  2.2.2  2.1.2  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.6 

Represents an InstanceDetailsSummary.

## Implements

[protos.google.cloud.osconfig.v1.PatchJob.IInstanceDetailsSummary](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.patchjob.iinstancedetailssummary)

## Package

[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.osconfig.v1.PatchJob.IInstanceDetailsSummary);

Constructs a new InstanceDetailsSummary.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInstanceDetailsSummary](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.patchjob.iinstancedetailssummary)`   
Properties to set  
  
## Properties 

### ackedInstanceCount
    
    
    public ackedInstanceCount: (number|Long|string);

InstanceDetailsSummary ackedInstanceCount.

### applyingPatchesInstanceCount
    
    
    public applyingPatchesInstanceCount: (number|Long|string);

InstanceDetailsSummary applyingPatchesInstanceCount.

### downloadingPatchesInstanceCount
    
    
    public downloadingPatchesInstanceCount: (number|Long|string);

InstanceDetailsSummary downloadingPatchesInstanceCount.

### failedInstanceCount
    
    
    public failedInstanceCount: (number|Long|string);

InstanceDetailsSummary failedInstanceCount.

### inactiveInstanceCount
    
    
    public inactiveInstanceCount: (number|Long|string);

InstanceDetailsSummary inactiveInstanceCount.

### noAgentDetectedInstanceCount
    
    
    public noAgentDetectedInstanceCount: (number|Long|string);

InstanceDetailsSummary noAgentDetectedInstanceCount.

### notifiedInstanceCount
    
    
    public notifiedInstanceCount: (number|Long|string);

InstanceDetailsSummary notifiedInstanceCount.

### pendingInstanceCount
    
    
    public pendingInstanceCount: (number|Long|string);

InstanceDetailsSummary pendingInstanceCount.

### postPatchStepInstanceCount
    
    
    public postPatchStepInstanceCount: (number|Long|string);

InstanceDetailsSummary postPatchStepInstanceCount.

### prePatchStepInstanceCount
    
    
    public prePatchStepInstanceCount: (number|Long|string);

InstanceDetailsSummary prePatchStepInstanceCount.

### rebootingInstanceCount
    
    
    public rebootingInstanceCount: (number|Long|string);

InstanceDetailsSummary rebootingInstanceCount.

### startedInstanceCount
    
    
    public startedInstanceCount: (number|Long|string);

InstanceDetailsSummary startedInstanceCount.

### succeededInstanceCount
    
    
    public succeededInstanceCount: (number|Long|string);

InstanceDetailsSummary succeededInstanceCount.

### succeededRebootRequiredInstanceCount
    
    
    public succeededRebootRequiredInstanceCount: (number|Long|string);

InstanceDetailsSummary succeededRebootRequiredInstanceCount.

### timedOutInstanceCount
    
    
    public timedOutInstanceCount: (number|Long|string);

InstanceDetailsSummary timedOutInstanceCount.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.osconfig.v1.PatchJob.IInstanceDetailsSummary): google.cloud.osconfig.v1.PatchJob.InstanceDetailsSummary;

Creates a new InstanceDetailsSummary instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInstanceDetailsSummary](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.patchjob.iinstancedetailssummary)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[InstanceDetailsSummary](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.patchjob.instancedetailssummary)` | InstanceDetailsSummary instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.osconfig.v1.PatchJob.InstanceDetailsSummary;

Decodes an InstanceDetailsSummary message from the specified reader or buffer.

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
`[InstanceDetailsSummary](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.patchjob.instancedetailssummary)` | InstanceDetailsSummary  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.osconfig.v1.PatchJob.InstanceDetailsSummary;

Decodes an InstanceDetailsSummary message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[InstanceDetailsSummary](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.patchjob.instancedetailssummary)` | InstanceDetailsSummary  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.osconfig.v1.PatchJob.IInstanceDetailsSummary, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified InstanceDetailsSummary message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInstanceDetailsSummary](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.patchjob.iinstancedetailssummary)`   
InstanceDetailsSummary message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.osconfig.v1.PatchJob.IInstanceDetailsSummary, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified InstanceDetailsSummary message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInstanceDetailsSummary](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.patchjob.iinstancedetailssummary)`   
InstanceDetailsSummary message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.osconfig.v1.PatchJob.InstanceDetailsSummary;

Creates an InstanceDetailsSummary message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[InstanceDetailsSummary](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.patchjob.instancedetailssummary)` | InstanceDetailsSummary  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for InstanceDetailsSummary

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

Converts this InstanceDetailsSummary to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.osconfig.v1.PatchJob.InstanceDetailsSummary, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an InstanceDetailsSummary message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[InstanceDetailsSummary](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1.patchjob.instancedetailssummary)`   
InstanceDetailsSummary  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an InstanceDetailsSummary message.

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
