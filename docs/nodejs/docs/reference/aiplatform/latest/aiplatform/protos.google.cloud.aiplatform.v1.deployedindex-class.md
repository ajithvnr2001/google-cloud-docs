---
url: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.deployedindex-class
title: Class protos.google.cloud.aiplatform.v1.DeployedIndex (7.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:32.423925+00:00
---

# Class protos.google.cloud.aiplatform.v1.DeployedIndex (7.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.deployedindex-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.aiplatform.v1.DeployedIndex (7.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.4.1 (latest)  7.3.0  6.10.0  6.9.0  6.8.1  6.6.0  6.4.0  6.3.0  6.2.0  6.1.0  6.0.0  5.14.0  5.13.0  3.15.0  3.13.0  3.11.0  3.10.1  3.9.0  3.7.0  3.6.0  3.4.0  3.3.0  3.0.0  2.12.0  2.11.0  2.10.0  2.7.0  2.6.1  2.5.0  2.3.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.11.0  1.7.2 

Represents a DeployedIndex.

## Implements

[protos.google.cloud.aiplatform.v1.IDeployedIndex](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideployedindex)

## Package

[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.aiplatform.v1.IDeployedIndex);

Constructs a new DeployedIndex.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeployedIndex](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideployedindex)`   
Properties to set  
  
## Properties 

### automaticResources
    
    
    public automaticResources?: (google.cloud.aiplatform.v1.IAutomaticResources|null);

DeployedIndex automaticResources.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

DeployedIndex createTime.

### dedicatedResources
    
    
    public dedicatedResources?: (google.cloud.aiplatform.v1.IDedicatedResources|null);

DeployedIndex dedicatedResources.

### deployedIndexAuthConfig
    
    
    public deployedIndexAuthConfig?: (google.cloud.aiplatform.v1.IDeployedIndexAuthConfig|null);

DeployedIndex deployedIndexAuthConfig.

### deploymentGroup
    
    
    public deploymentGroup: string;

DeployedIndex deploymentGroup.

### deploymentTier
    
    
    public deploymentTier: (google.cloud.aiplatform.v1.DeployedIndex.DeploymentTier|keyof typeof google.cloud.aiplatform.v1.DeployedIndex.DeploymentTier);

DeployedIndex deploymentTier.

### displayName
    
    
    public displayName: string;

DeployedIndex displayName.

### enableAccessLogging
    
    
    public enableAccessLogging: boolean;

DeployedIndex enableAccessLogging.

### enableDatapointUpsertLogging
    
    
    public enableDatapointUpsertLogging: boolean;

DeployedIndex enableDatapointUpsertLogging.

### id
    
    
    public id: string;

DeployedIndex id.

### index
    
    
    public index: string;

DeployedIndex index.

### indexSyncTime
    
    
    public indexSyncTime?: (google.protobuf.ITimestamp|null);

DeployedIndex indexSyncTime.

### privateEndpoints
    
    
    public privateEndpoints?: (google.cloud.aiplatform.v1.IIndexPrivateEndpoints|null);

DeployedIndex privateEndpoints.

### pscAutomationConfigs
    
    
    public pscAutomationConfigs: google.cloud.aiplatform.v1.IPSCAutomationConfig[];

DeployedIndex pscAutomationConfigs.

### reservedIpRanges
    
    
    public reservedIpRanges: string[];

DeployedIndex reservedIpRanges.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.aiplatform.v1.IDeployedIndex): google.cloud.aiplatform.v1.DeployedIndex;

Creates a new DeployedIndex instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeployedIndex](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideployedindex)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DeployedIndex](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.deployedindex-class)` | DeployedIndex instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.aiplatform.v1.DeployedIndex;

Decodes a DeployedIndex message from the specified reader or buffer.

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
`[DeployedIndex](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.deployedindex-class)` | DeployedIndex  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.aiplatform.v1.DeployedIndex;

Decodes a DeployedIndex message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DeployedIndex](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.deployedindex-class)` | DeployedIndex  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.aiplatform.v1.IDeployedIndex, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeployedIndex message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeployedIndex](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideployedindex)`   
DeployedIndex message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.aiplatform.v1.IDeployedIndex, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeployedIndex message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeployedIndex](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideployedindex)`   
DeployedIndex message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.aiplatform.v1.DeployedIndex;

Creates a DeployedIndex message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DeployedIndex](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.deployedindex-class)` | DeployedIndex  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DeployedIndex

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

Converts this DeployedIndex to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.aiplatform.v1.DeployedIndex, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DeployedIndex message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DeployedIndex](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.deployedindex-class)`   
DeployedIndex  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DeployedIndex message.

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
