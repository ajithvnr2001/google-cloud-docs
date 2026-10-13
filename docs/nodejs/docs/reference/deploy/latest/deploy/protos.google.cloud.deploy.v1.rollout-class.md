---
url: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.rollout-class
title: Class protos.google.cloud.deploy.v1.Rollout (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:01:52.043322+00:00
---

# Class protos.google.cloud.deploy.v1.Rollout (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.rollout-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.deploy.v1.Rollout (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.0.1  4.4.0  4.3.0  4.0.0  3.6.0  3.5.0  3.4.0  3.1.0  3.0.0  2.5.0  2.4.1  2.3.1  2.2.2  2.1.1  1.0.0  0.2.0 

Represents a Rollout.

## Implements

[protos.google.cloud.deploy.v1.IRollout](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.irollout)

## Package

[@google-cloud/deploy](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.deploy.v1.IRollout);

Constructs a new Rollout.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRollout](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.irollout)`   
Properties to set  
  
## Properties 

### activeRepairAutomationRun
    
    
    public activeRepairAutomationRun: string;

Rollout activeRepairAutomationRun.

### annotations
    
    
    public annotations: { [k: string]: string };

Rollout annotations.

### approvalState
    
    
    public approvalState: (google.cloud.deploy.v1.Rollout.ApprovalState|keyof typeof google.cloud.deploy.v1.Rollout.ApprovalState);

Rollout approvalState.

### approveTime
    
    
    public approveTime?: (google.protobuf.ITimestamp|null);

Rollout approveTime.

### controllerRollout
    
    
    public controllerRollout: string;

Rollout controllerRollout.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Rollout createTime.

### deployEndTime
    
    
    public deployEndTime?: (google.protobuf.ITimestamp|null);

Rollout deployEndTime.

### deployFailureCause
    
    
    public deployFailureCause: (google.cloud.deploy.v1.Rollout.FailureCause|keyof typeof google.cloud.deploy.v1.Rollout.FailureCause);

Rollout deployFailureCause.

### deployingBuild
    
    
    public deployingBuild: string;

Rollout deployingBuild.

### deployStartTime
    
    
    public deployStartTime?: (google.protobuf.ITimestamp|null);

Rollout deployStartTime.

### description
    
    
    public description: string;

Rollout description.

### enqueueTime
    
    
    public enqueueTime?: (google.protobuf.ITimestamp|null);

Rollout enqueueTime.

### etag
    
    
    public etag: string;

Rollout etag.

### failureReason
    
    
    public failureReason: string;

Rollout failureReason.

### labels
    
    
    public labels: { [k: string]: string };

Rollout labels.

### metadata
    
    
    public metadata?: (google.cloud.deploy.v1.IMetadata|null);

Rollout metadata.

### name
    
    
    public name: string;

Rollout name.

### phases
    
    
    public phases: google.cloud.deploy.v1.IPhase[];

Rollout phases.

### rollbackOfRollout
    
    
    public rollbackOfRollout: string;

Rollout rollbackOfRollout.

### rolledBackByRollouts
    
    
    public rolledBackByRollouts: string[];

Rollout rolledBackByRollouts.

### state
    
    
    public state: (google.cloud.deploy.v1.Rollout.State|keyof typeof google.cloud.deploy.v1.Rollout.State);

Rollout state.

### targetId
    
    
    public targetId: string;

Rollout targetId.

### uid
    
    
    public uid: string;

Rollout uid.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.deploy.v1.IRollout): google.cloud.deploy.v1.Rollout;

Creates a new Rollout instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRollout](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.irollout)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.rollout-class)` | Rollout instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.deploy.v1.Rollout;

Decodes a Rollout message from the specified reader or buffer.

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
`[Rollout](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.rollout-class)` | Rollout  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.deploy.v1.Rollout;

Decodes a Rollout message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.rollout-class)` | Rollout  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.deploy.v1.IRollout, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Rollout message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRollout](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.irollout)`   
Rollout message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.deploy.v1.IRollout, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Rollout message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRollout](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.irollout)`   
Rollout message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.deploy.v1.Rollout;

Creates a Rollout message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.rollout-class)` | Rollout  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Rollout

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

Converts this Rollout to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.deploy.v1.Rollout, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Rollout message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Rollout](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.rollout-class)`   
Rollout  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Rollout message.

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
