---
url: https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.operationstep-class
title: Class protos.google.cloud.hypercomputecluster.v1.OperationStep (0.5.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:43.083721+00:00
---

# Class protos.google.cloud.hypercomputecluster.v1.OperationStep (0.5.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.operationstep-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.hypercomputecluster.v1.OperationStep (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.2.0  0.1.0 

Represents an OperationStep.

## Implements

[protos.google.cloud.hypercomputecluster.v1.IOperationStep](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.ioperationstep)

## Package

[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.hypercomputecluster.v1.IOperationStep);

Constructs a new OperationStep.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOperationStep](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.ioperationstep)`   
Properties to set  
  
## Properties 

### checkClusterHealth
    
    
    public checkClusterHealth?: (google.cloud.hypercomputecluster.v1.ICheckClusterHealth|null);

OperationStep checkClusterHealth.

### createFilestoreInstance
    
    
    public createFilestoreInstance?: (google.cloud.hypercomputecluster.v1.ICreateFilestoreInstance|null);

OperationStep createFilestoreInstance.

### createLoginNode
    
    
    public createLoginNode?: (google.cloud.hypercomputecluster.v1.ICreateLoginNode|null);

OperationStep createLoginNode.

### createLustreInstance
    
    
    public createLustreInstance?: (google.cloud.hypercomputecluster.v1.ICreateLustreInstance|null);

OperationStep createLustreInstance.

### createNetwork
    
    
    public createNetwork?: (google.cloud.hypercomputecluster.v1.ICreateNetwork|null);

OperationStep createNetwork.

### createNodeset
    
    
    public createNodeset?: (google.cloud.hypercomputecluster.v1.ICreateNodeset|null);

OperationStep createNodeset.

### createOrchestrator
    
    
    public createOrchestrator?: (google.cloud.hypercomputecluster.v1.ICreateOrchestrator|null);

OperationStep createOrchestrator.

### createPartition
    
    
    public createPartition?: (google.cloud.hypercomputecluster.v1.ICreatePartition|null);

OperationStep createPartition.

### createPrivateServiceAccess
    
    
    public createPrivateServiceAccess?: (google.cloud.hypercomputecluster.v1.ICreatePrivateServiceAccess|null);

OperationStep createPrivateServiceAccess.

### createStorageBucket
    
    
    public createStorageBucket?: (google.cloud.hypercomputecluster.v1.ICreateStorageBucket|null);

OperationStep createStorageBucket.

### deleteFilestoreInstance
    
    
    public deleteFilestoreInstance?: (google.cloud.hypercomputecluster.v1.IDeleteFilestoreInstance|null);

OperationStep deleteFilestoreInstance.

### deleteLoginNode
    
    
    public deleteLoginNode?: (google.cloud.hypercomputecluster.v1.IDeleteLoginNode|null);

OperationStep deleteLoginNode.

### deleteLustreInstance
    
    
    public deleteLustreInstance?: (google.cloud.hypercomputecluster.v1.IDeleteLustreInstance|null);

OperationStep deleteLustreInstance.

### deleteNetwork
    
    
    public deleteNetwork?: (google.cloud.hypercomputecluster.v1.IDeleteNetwork|null);

OperationStep deleteNetwork.

### deleteNodeset
    
    
    public deleteNodeset?: (google.cloud.hypercomputecluster.v1.IDeleteNodeset|null);

OperationStep deleteNodeset.

### deleteOrchestrator
    
    
    public deleteOrchestrator?: (google.cloud.hypercomputecluster.v1.IDeleteOrchestrator|null);

OperationStep deleteOrchestrator.

### deletePartition
    
    
    public deletePartition?: (google.cloud.hypercomputecluster.v1.IDeletePartition|null);

OperationStep deletePartition.

### deletePrivateServiceAccess
    
    
    public deletePrivateServiceAccess?: (google.cloud.hypercomputecluster.v1.IDeletePrivateServiceAccess|null);

OperationStep deletePrivateServiceAccess.

### deleteStorageBucket
    
    
    public deleteStorageBucket?: (google.cloud.hypercomputecluster.v1.IDeleteStorageBucket|null);

OperationStep deleteStorageBucket.

### state
    
    
    public state: (google.cloud.hypercomputecluster.v1.OperationStep.State|keyof typeof google.cloud.hypercomputecluster.v1.OperationStep.State);

OperationStep state.

### type
    
    
    public type?: ("createNetwork"|"createPrivateServiceAccess"|"createFilestoreInstance"|"createStorageBucket"|"createLustreInstance"|"createOrchestrator"|"createNodeset"|"createPartition"|"createLoginNode"|"checkClusterHealth"|"updateOrchestrator"|"updateNodeset"|"updatePartition"|"updateLoginNode"|"deleteOrchestrator"|"deleteNodeset"|"deletePartition"|"deleteLoginNode"|"deleteFilestoreInstance"|"deleteStorageBucket"|"deleteLustreInstance"|"deletePrivateServiceAccess"|"deleteNetwork");

OperationStep type.

### updateLoginNode
    
    
    public updateLoginNode?: (google.cloud.hypercomputecluster.v1.IUpdateLoginNode|null);

OperationStep updateLoginNode.

### updateNodeset
    
    
    public updateNodeset?: (google.cloud.hypercomputecluster.v1.IUpdateNodeset|null);

OperationStep updateNodeset.

### updateOrchestrator
    
    
    public updateOrchestrator?: (google.cloud.hypercomputecluster.v1.IUpdateOrchestrator|null);

OperationStep updateOrchestrator.

### updatePartition
    
    
    public updatePartition?: (google.cloud.hypercomputecluster.v1.IUpdatePartition|null);

OperationStep updatePartition.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.hypercomputecluster.v1.IOperationStep): google.cloud.hypercomputecluster.v1.OperationStep;

Creates a new OperationStep instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOperationStep](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.ioperationstep)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[OperationStep](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.operationstep-class)` | OperationStep instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.hypercomputecluster.v1.OperationStep;

Decodes an OperationStep message from the specified reader or buffer.

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
`[OperationStep](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.operationstep-class)` | OperationStep  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.hypercomputecluster.v1.OperationStep;

Decodes an OperationStep message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[OperationStep](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.operationstep-class)` | OperationStep  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.hypercomputecluster.v1.IOperationStep, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OperationStep message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOperationStep](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.ioperationstep)`   
OperationStep message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.hypercomputecluster.v1.IOperationStep, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OperationStep message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOperationStep](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.ioperationstep)`   
OperationStep message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.hypercomputecluster.v1.OperationStep;

Creates an OperationStep message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[OperationStep](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.operationstep-class)` | OperationStep  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for OperationStep

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

Converts this OperationStep to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.hypercomputecluster.v1.OperationStep, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an OperationStep message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[OperationStep](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.operationstep-class)`   
OperationStep  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an OperationStep message.

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
