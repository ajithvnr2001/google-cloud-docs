---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.clusterconfig-class
title: Class protos.google.cloud.dataproc.v1.ClusterConfig (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:37.190090+00:00
---

# Class protos.google.cloud.dataproc.v1.ClusterConfig (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.clusterconfig-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataproc.v1.ClusterConfig (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.8.0  6.7.0  6.6.0  5.13.0  5.12.0  5.10.0  5.9.0  5.7.0  5.5.0  5.4.0  4.5.0  4.3.1  4.1.1  3.2.0  3.1.0  3.0.0  2.5.0  2.4.4 

Represents a ClusterConfig.

## Implements

[protos.google.cloud.dataproc.v1.IClusterConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iclusterconfig)

## Package

[@google-cloud/dataproc](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataproc.v1.IClusterConfig);

Constructs a new ClusterConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IClusterConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iclusterconfig)`   
Properties to set  
  
## Properties 

### autoscalingConfig
    
    
    public autoscalingConfig?: (google.cloud.dataproc.v1.IAutoscalingConfig|null);

ClusterConfig autoscalingConfig.

### auxiliaryNodeGroups
    
    
    public auxiliaryNodeGroups: google.cloud.dataproc.v1.IAuxiliaryNodeGroup[];

ClusterConfig auxiliaryNodeGroups.

### clusterTier
    
    
    public clusterTier: (google.cloud.dataproc.v1.ClusterConfig.ClusterTier|keyof typeof google.cloud.dataproc.v1.ClusterConfig.ClusterTier);

ClusterConfig clusterTier.

### clusterType
    
    
    public clusterType: (google.cloud.dataproc.v1.ClusterConfig.ClusterType|keyof typeof google.cloud.dataproc.v1.ClusterConfig.ClusterType);

ClusterConfig clusterType.

### configBucket
    
    
    public configBucket: string;

ClusterConfig configBucket.

### dataprocMetricConfig
    
    
    public dataprocMetricConfig?: (google.cloud.dataproc.v1.IDataprocMetricConfig|null);

ClusterConfig dataprocMetricConfig.

### encryptionConfig
    
    
    public encryptionConfig?: (google.cloud.dataproc.v1.IEncryptionConfig|null);

ClusterConfig encryptionConfig.

### endpointConfig
    
    
    public endpointConfig?: (google.cloud.dataproc.v1.IEndpointConfig|null);

ClusterConfig endpointConfig.

### engine
    
    
    public engine: (google.cloud.dataproc.v1.ClusterConfig.Engine|keyof typeof google.cloud.dataproc.v1.ClusterConfig.Engine);

ClusterConfig engine.

### gceClusterConfig
    
    
    public gceClusterConfig?: (google.cloud.dataproc.v1.IGceClusterConfig|null);

ClusterConfig gceClusterConfig.

### initializationActions
    
    
    public initializationActions: google.cloud.dataproc.v1.INodeInitializationAction[];

ClusterConfig initializationActions.

### lifecycleConfig
    
    
    public lifecycleConfig?: (google.cloud.dataproc.v1.ILifecycleConfig|null);

ClusterConfig lifecycleConfig.

### masterConfig
    
    
    public masterConfig?: (google.cloud.dataproc.v1.IInstanceGroupConfig|null);

ClusterConfig masterConfig.

### metastoreConfig
    
    
    public metastoreConfig?: (google.cloud.dataproc.v1.IMetastoreConfig|null);

ClusterConfig metastoreConfig.

### secondaryWorkerConfig
    
    
    public secondaryWorkerConfig?: (google.cloud.dataproc.v1.IInstanceGroupConfig|null);

ClusterConfig secondaryWorkerConfig.

### securityConfig
    
    
    public securityConfig?: (google.cloud.dataproc.v1.ISecurityConfig|null);

ClusterConfig securityConfig.

### softwareConfig
    
    
    public softwareConfig?: (google.cloud.dataproc.v1.ISoftwareConfig|null);

ClusterConfig softwareConfig.

### tempBucket
    
    
    public tempBucket: string;

ClusterConfig tempBucket.

### workerConfig
    
    
    public workerConfig?: (google.cloud.dataproc.v1.IInstanceGroupConfig|null);

ClusterConfig workerConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataproc.v1.IClusterConfig): google.cloud.dataproc.v1.ClusterConfig;

Creates a new ClusterConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IClusterConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iclusterconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ClusterConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.clusterconfig-class)` | ClusterConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataproc.v1.ClusterConfig;

Decodes a ClusterConfig message from the specified reader or buffer.

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
`[ClusterConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.clusterconfig-class)` | ClusterConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataproc.v1.ClusterConfig;

Decodes a ClusterConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ClusterConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.clusterconfig-class)` | ClusterConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataproc.v1.IClusterConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ClusterConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IClusterConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iclusterconfig)`   
ClusterConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataproc.v1.IClusterConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ClusterConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IClusterConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iclusterconfig)`   
ClusterConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataproc.v1.ClusterConfig;

Creates a ClusterConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ClusterConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.clusterconfig-class)` | ClusterConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ClusterConfig

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

Converts this ClusterConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataproc.v1.ClusterConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ClusterConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ClusterConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.clusterconfig-class)`   
ClusterConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ClusterConfig message.

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
