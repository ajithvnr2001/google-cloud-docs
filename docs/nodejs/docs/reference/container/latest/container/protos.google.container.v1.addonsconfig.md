---
url: https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.addonsconfig
title: Class protos.google.container.v1.AddonsConfig (7.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:37:25.888490+00:00
---

# Class protos.google.container.v1.AddonsConfig (7.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.addonsconfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.container.v1.AddonsConfig (7.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.2.1 (latest)  7.1.0  6.8.0  6.7.0  6.1.0  5.19.0  5.17.0  5.15.1  5.14.0  5.10.0  5.9.0  5.8.0  5.6.0  5.5.0  5.4.1  5.1.0  4.11.0  4.10.0  4.9.0  4.7.1  4.4.0  4.3.0  4.2.0  4.1.3  3.0.0  2.6.0  2.5.0  2.4.4  2.3.2 

Represents an AddonsConfig.

## Implements

[protos.google.container.v1.IAddonsConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.iaddonsconfig)

## Package

[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.container.v1.IAddonsConfig);

Constructs a new AddonsConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAddonsConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.iaddonsconfig)`   
Properties to set  
  
## Properties 

### agentSandboxConfig
    
    
    public agentSandboxConfig?: (google.container.v1.IAgentSandboxConfig|null);

AddonsConfig agentSandboxConfig.

### cloudRunConfig
    
    
    public cloudRunConfig?: (google.container.v1.ICloudRunConfig|null);

AddonsConfig cloudRunConfig.

### configConnectorConfig
    
    
    public configConnectorConfig?: (google.container.v1.IConfigConnectorConfig|null);

AddonsConfig configConnectorConfig.

### dnsCacheConfig
    
    
    public dnsCacheConfig?: (google.container.v1.IDnsCacheConfig|null);

AddonsConfig dnsCacheConfig.

### gcePersistentDiskCsiDriverConfig
    
    
    public gcePersistentDiskCsiDriverConfig?: (google.container.v1.IGcePersistentDiskCsiDriverConfig|null);

AddonsConfig gcePersistentDiskCsiDriverConfig.

### gcpFilestoreCsiDriverConfig
    
    
    public gcpFilestoreCsiDriverConfig?: (google.container.v1.IGcpFilestoreCsiDriverConfig|null);

AddonsConfig gcpFilestoreCsiDriverConfig.

### gcsFuseCsiDriverConfig
    
    
    public gcsFuseCsiDriverConfig?: (google.container.v1.IGcsFuseCsiDriverConfig|null);

AddonsConfig gcsFuseCsiDriverConfig.

### gkeBackupAgentConfig
    
    
    public gkeBackupAgentConfig?: (google.container.v1.IGkeBackupAgentConfig|null);

AddonsConfig gkeBackupAgentConfig.

### highScaleCheckpointingConfig
    
    
    public highScaleCheckpointingConfig?: (google.container.v1.IHighScaleCheckpointingConfig|null);

AddonsConfig highScaleCheckpointingConfig.

### horizontalPodAutoscaling
    
    
    public horizontalPodAutoscaling?: (google.container.v1.IHorizontalPodAutoscaling|null);

AddonsConfig horizontalPodAutoscaling.

### httpLoadBalancing
    
    
    public httpLoadBalancing?: (google.container.v1.IHttpLoadBalancing|null);

AddonsConfig httpLoadBalancing.

### kubernetesDashboard
    
    
    public kubernetesDashboard?: (google.container.v1.IKubernetesDashboard|null);

AddonsConfig kubernetesDashboard.

### lustreCsiDriverConfig
    
    
    public lustreCsiDriverConfig?: (google.container.v1.ILustreCsiDriverConfig|null);

AddonsConfig lustreCsiDriverConfig.

### networkPolicyConfig
    
    
    public networkPolicyConfig?: (google.container.v1.INetworkPolicyConfig|null);

AddonsConfig networkPolicyConfig.

### nodeReadinessConfig
    
    
    public nodeReadinessConfig?: (google.container.v1.INodeReadinessConfig|null);

AddonsConfig nodeReadinessConfig.

### parallelstoreCsiDriverConfig
    
    
    public parallelstoreCsiDriverConfig?: (google.container.v1.IParallelstoreCsiDriverConfig|null);

AddonsConfig parallelstoreCsiDriverConfig.

### podSnapshotConfig
    
    
    public podSnapshotConfig?: (google.container.v1.IPodSnapshotConfig|null);

AddonsConfig podSnapshotConfig.

### rayOperatorConfig
    
    
    public rayOperatorConfig?: (google.container.v1.IRayOperatorConfig|null);

AddonsConfig rayOperatorConfig.

### sliceControllerConfig
    
    
    public sliceControllerConfig?: (google.container.v1.ISliceControllerConfig|null);

AddonsConfig sliceControllerConfig.

### slurmOperatorConfig
    
    
    public slurmOperatorConfig?: (google.container.v1.ISlurmOperatorConfig|null);

AddonsConfig slurmOperatorConfig.

### statefulHaConfig
    
    
    public statefulHaConfig?: (google.container.v1.IStatefulHAConfig|null);

AddonsConfig statefulHaConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.container.v1.IAddonsConfig): google.container.v1.AddonsConfig;

Creates a new AddonsConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAddonsConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.iaddonsconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AddonsConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.addonsconfig)` | AddonsConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.container.v1.AddonsConfig;

Decodes an AddonsConfig message from the specified reader or buffer.

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
`[AddonsConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.addonsconfig)` | AddonsConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.container.v1.AddonsConfig;

Decodes an AddonsConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AddonsConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.addonsconfig)` | AddonsConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.container.v1.IAddonsConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AddonsConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAddonsConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.iaddonsconfig)`   
AddonsConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.container.v1.IAddonsConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AddonsConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAddonsConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.iaddonsconfig)`   
AddonsConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.container.v1.AddonsConfig;

Creates an AddonsConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AddonsConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.addonsconfig)` | AddonsConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AddonsConfig

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

Converts this AddonsConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.container.v1.AddonsConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AddonsConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AddonsConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.addonsconfig)`   
AddonsConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AddonsConfig message.

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
