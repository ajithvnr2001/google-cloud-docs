---
url: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.deploypolicyevaluationevent-class
title: Class protos.google.cloud.deploy.v1.DeployPolicyEvaluationEvent (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:01:37.074442+00:00
---

# Class protos.google.cloud.deploy.v1.DeployPolicyEvaluationEvent (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.deploypolicyevaluationevent-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.deploy.v1.DeployPolicyEvaluationEvent (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.0.1  4.4.0  4.3.0  4.0.0  3.6.0  3.5.0  3.4.0  3.1.0  3.0.0  2.5.0  2.4.1  2.3.1  2.2.2  2.1.1  1.0.0  0.2.0 

Represents a DeployPolicyEvaluationEvent.

## Implements

[protos.google.cloud.deploy.v1.IDeployPolicyEvaluationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideploypolicyevaluationevent)

## Package

[@google-cloud/deploy](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.deploy.v1.IDeployPolicyEvaluationEvent);

Constructs a new DeployPolicyEvaluationEvent.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeployPolicyEvaluationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideploypolicyevaluationevent)`   
Properties to set  
  
## Properties 

### allowed
    
    
    public allowed: boolean;

DeployPolicyEvaluationEvent allowed.

### deliveryPipeline
    
    
    public deliveryPipeline: string;

DeployPolicyEvaluationEvent deliveryPipeline.

### deployPolicy
    
    
    public deployPolicy: string;

DeployPolicyEvaluationEvent deployPolicy.

### deployPolicyUid
    
    
    public deployPolicyUid: string;

DeployPolicyEvaluationEvent deployPolicyUid.

### invoker
    
    
    public invoker: (google.cloud.deploy.v1.DeployPolicy.Invoker|keyof typeof google.cloud.deploy.v1.DeployPolicy.Invoker);

DeployPolicyEvaluationEvent invoker.

### message
    
    
    public message: string;

DeployPolicyEvaluationEvent message.

### overrides
    
    
    public overrides: google.cloud.deploy.v1.DeployPolicyEvaluationEvent.PolicyVerdictOverride[];

DeployPolicyEvaluationEvent overrides.

### pipelineUid
    
    
    public pipelineUid: string;

DeployPolicyEvaluationEvent pipelineUid.

### rule
    
    
    public rule: string;

DeployPolicyEvaluationEvent rule.

### ruleType
    
    
    public ruleType: string;

DeployPolicyEvaluationEvent ruleType.

### target
    
    
    public target: string;

DeployPolicyEvaluationEvent target.

### targetUid
    
    
    public targetUid: string;

DeployPolicyEvaluationEvent targetUid.

### verdict
    
    
    public verdict: (google.cloud.deploy.v1.DeployPolicyEvaluationEvent.PolicyVerdict|keyof typeof google.cloud.deploy.v1.DeployPolicyEvaluationEvent.PolicyVerdict);

DeployPolicyEvaluationEvent verdict.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.deploy.v1.IDeployPolicyEvaluationEvent): google.cloud.deploy.v1.DeployPolicyEvaluationEvent;

Creates a new DeployPolicyEvaluationEvent instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeployPolicyEvaluationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideploypolicyevaluationevent)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DeployPolicyEvaluationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.deploypolicyevaluationevent-class)` | DeployPolicyEvaluationEvent instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.deploy.v1.DeployPolicyEvaluationEvent;

Decodes a DeployPolicyEvaluationEvent message from the specified reader or buffer.

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
`[DeployPolicyEvaluationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.deploypolicyevaluationevent-class)` | DeployPolicyEvaluationEvent  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.deploy.v1.DeployPolicyEvaluationEvent;

Decodes a DeployPolicyEvaluationEvent message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DeployPolicyEvaluationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.deploypolicyevaluationevent-class)` | DeployPolicyEvaluationEvent  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.deploy.v1.IDeployPolicyEvaluationEvent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeployPolicyEvaluationEvent message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeployPolicyEvaluationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideploypolicyevaluationevent)`   
DeployPolicyEvaluationEvent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.deploy.v1.IDeployPolicyEvaluationEvent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeployPolicyEvaluationEvent message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeployPolicyEvaluationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ideploypolicyevaluationevent)`   
DeployPolicyEvaluationEvent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.deploy.v1.DeployPolicyEvaluationEvent;

Creates a DeployPolicyEvaluationEvent message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DeployPolicyEvaluationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.deploypolicyevaluationevent-class)` | DeployPolicyEvaluationEvent  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DeployPolicyEvaluationEvent

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

Converts this DeployPolicyEvaluationEvent to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.deploy.v1.DeployPolicyEvaluationEvent, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DeployPolicyEvaluationEvent message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DeployPolicyEvaluationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.deploypolicyevaluationevent-class)`   
DeployPolicyEvaluationEvent  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DeployPolicyEvaluationEvent message.

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
