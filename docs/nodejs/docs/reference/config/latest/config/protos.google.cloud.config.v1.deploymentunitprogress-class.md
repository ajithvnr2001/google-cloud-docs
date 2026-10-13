---
url: https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.deploymentunitprogress-class
title: Class protos.google.cloud.config.v1.DeploymentUnitProgress (0.15.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:53.601391+00:00
---

# Class protos.google.cloud.config.v1.DeploymentUnitProgress (0.15.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.deploymentunitprogress-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.config.v1.DeploymentUnitProgress (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.14.0  0.12.0  0.7.0  0.5.0  0.2.0  0.1.1 

Represents a DeploymentUnitProgress.

## Implements

[protos.google.cloud.config.v1.IDeploymentUnitProgress](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideploymentunitprogress)

## Package

[@google-cloud/config](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.config.v1.IDeploymentUnitProgress);

Constructs a new DeploymentUnitProgress.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeploymentUnitProgress](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideploymentunitprogress)`   
Properties to set  
  
## Properties 

### deployment
    
    
    public deployment: string;

DeploymentUnitProgress deployment.

### deploymentOperationSummary
    
    
    public deploymentOperationSummary?: (google.cloud.config.v1.IDeploymentOperationSummary|null);

DeploymentUnitProgress deploymentOperationSummary.

### error
    
    
    public error?: (google.rpc.IStatus|null);

DeploymentUnitProgress error.

### intent
    
    
    public intent: (google.cloud.config.v1.DeploymentUnitProgress.Intent|keyof typeof google.cloud.config.v1.DeploymentUnitProgress.Intent);

DeploymentUnitProgress intent.

### state
    
    
    public state: (google.cloud.config.v1.DeploymentUnitProgress.State|keyof typeof google.cloud.config.v1.DeploymentUnitProgress.State);

DeploymentUnitProgress state.

### stateDescription
    
    
    public stateDescription: string;

DeploymentUnitProgress stateDescription.

### unitId
    
    
    public unitId: string;

DeploymentUnitProgress unitId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.config.v1.IDeploymentUnitProgress): google.cloud.config.v1.DeploymentUnitProgress;

Creates a new DeploymentUnitProgress instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeploymentUnitProgress](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideploymentunitprogress)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentUnitProgress](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.deploymentunitprogress-class)` | DeploymentUnitProgress instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.config.v1.DeploymentUnitProgress;

Decodes a DeploymentUnitProgress message from the specified reader or buffer.

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
`[DeploymentUnitProgress](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.deploymentunitprogress-class)` | DeploymentUnitProgress  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.config.v1.DeploymentUnitProgress;

Decodes a DeploymentUnitProgress message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentUnitProgress](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.deploymentunitprogress-class)` | DeploymentUnitProgress  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.config.v1.IDeploymentUnitProgress, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeploymentUnitProgress message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeploymentUnitProgress](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideploymentunitprogress)`   
DeploymentUnitProgress message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.config.v1.IDeploymentUnitProgress, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeploymentUnitProgress message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeploymentUnitProgress](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideploymentunitprogress)`   
DeploymentUnitProgress message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.config.v1.DeploymentUnitProgress;

Creates a DeploymentUnitProgress message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentUnitProgress](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.deploymentunitprogress-class)` | DeploymentUnitProgress  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DeploymentUnitProgress

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

Converts this DeploymentUnitProgress to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.config.v1.DeploymentUnitProgress, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DeploymentUnitProgress message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DeploymentUnitProgress](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.deploymentunitprogress-class)`   
DeploymentUnitProgress  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DeploymentUnitProgress message.

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
