---
url: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.phase-class
title: Class protos.google.cloud.deploy.v1.Phase (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:01:45.349517+00:00
---

# Class protos.google.cloud.deploy.v1.Phase (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.phase-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.deploy.v1.Phase (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.0.1  4.4.0  4.3.0  4.0.0  3.6.0  3.5.0  3.4.0  3.1.0  3.0.0  2.5.0  2.4.1  2.3.1  2.2.2  2.1.1  1.0.0  0.2.0 

Represents a Phase.

## Implements

[protos.google.cloud.deploy.v1.IPhase](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iphase)

## Package

[@google-cloud/deploy](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.deploy.v1.IPhase);

Constructs a new Phase.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPhase](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iphase)`   
Properties to set  
  
## Properties 

### childRolloutJobs
    
    
    public childRolloutJobs?: (google.cloud.deploy.v1.IChildRolloutJobs|null);

Phase childRolloutJobs.

### deploymentJobs
    
    
    public deploymentJobs?: (google.cloud.deploy.v1.IDeploymentJobs|null);

Phase deploymentJobs.

### id
    
    
    public id: string;

Phase id.

### jobs
    
    
    public jobs?: ("deploymentJobs"|"childRolloutJobs");

Phase jobs.

### skipMessage
    
    
    public skipMessage: string;

Phase skipMessage.

### state
    
    
    public state: (google.cloud.deploy.v1.Phase.State|keyof typeof google.cloud.deploy.v1.Phase.State);

Phase state.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.deploy.v1.IPhase): google.cloud.deploy.v1.Phase;

Creates a new Phase instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPhase](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iphase)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Phase](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.phase-class)` | Phase instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.deploy.v1.Phase;

Decodes a Phase message from the specified reader or buffer.

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
`[Phase](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.phase-class)` | Phase  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.deploy.v1.Phase;

Decodes a Phase message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Phase](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.phase-class)` | Phase  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.deploy.v1.IPhase, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Phase message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPhase](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iphase)`   
Phase message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.deploy.v1.IPhase, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Phase message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPhase](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iphase)`   
Phase message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.deploy.v1.Phase;

Creates a Phase message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Phase](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.phase-class)` | Phase  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Phase

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

Converts this Phase to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.deploy.v1.Phase, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Phase message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Phase](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.phase-class)`   
Phase  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Phase message.

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
