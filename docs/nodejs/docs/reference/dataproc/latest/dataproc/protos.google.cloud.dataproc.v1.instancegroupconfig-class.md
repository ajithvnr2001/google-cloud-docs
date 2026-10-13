---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.instancegroupconfig-class
title: Class protos.google.cloud.dataproc.v1.InstanceGroupConfig (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:47.202200+00:00
---

# Class protos.google.cloud.dataproc.v1.InstanceGroupConfig (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.instancegroupconfig-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataproc.v1.InstanceGroupConfig (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.8.0  6.7.0  6.6.0  5.13.0  5.12.0  5.10.0  5.9.0  5.7.0  5.5.0  5.4.0  4.5.0  4.3.1  4.1.1  3.2.0  3.1.0  3.0.0  2.5.0  2.4.4 

Represents an InstanceGroupConfig.

## Implements

[protos.google.cloud.dataproc.v1.IInstanceGroupConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iinstancegroupconfig)

## Package

[@google-cloud/dataproc](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataproc.v1.IInstanceGroupConfig);

Constructs a new InstanceGroupConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInstanceGroupConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iinstancegroupconfig)`   
Properties to set  
  
## Properties 

### accelerators
    
    
    public accelerators: google.cloud.dataproc.v1.IAcceleratorConfig[];

InstanceGroupConfig accelerators.

### diskConfig
    
    
    public diskConfig?: (google.cloud.dataproc.v1.IDiskConfig|null);

InstanceGroupConfig diskConfig.

### imageUri
    
    
    public imageUri: string;

InstanceGroupConfig imageUri.

### instanceFlexibilityPolicy
    
    
    public instanceFlexibilityPolicy?: (google.cloud.dataproc.v1.IInstanceFlexibilityPolicy|null);

InstanceGroupConfig instanceFlexibilityPolicy.

### instanceNames
    
    
    public instanceNames: string[];

InstanceGroupConfig instanceNames.

### instanceReferences
    
    
    public instanceReferences: google.cloud.dataproc.v1.IInstanceReference[];

InstanceGroupConfig instanceReferences.

### isPreemptible
    
    
    public isPreemptible: boolean;

InstanceGroupConfig isPreemptible.

### machineTypeUri
    
    
    public machineTypeUri: string;

InstanceGroupConfig machineTypeUri.

### managedGroupConfig
    
    
    public managedGroupConfig?: (google.cloud.dataproc.v1.IManagedGroupConfig|null);

InstanceGroupConfig managedGroupConfig.

### minCpuPlatform
    
    
    public minCpuPlatform: string;

InstanceGroupConfig minCpuPlatform.

### minNumInstances
    
    
    public minNumInstances: number;

InstanceGroupConfig minNumInstances.

### numInstances
    
    
    public numInstances: number;

InstanceGroupConfig numInstances.

### preemptibility
    
    
    public preemptibility: (google.cloud.dataproc.v1.InstanceGroupConfig.Preemptibility|keyof typeof google.cloud.dataproc.v1.InstanceGroupConfig.Preemptibility);

InstanceGroupConfig preemptibility.

### startupConfig
    
    
    public startupConfig?: (google.cloud.dataproc.v1.IStartupConfig|null);

InstanceGroupConfig startupConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataproc.v1.IInstanceGroupConfig): google.cloud.dataproc.v1.InstanceGroupConfig;

Creates a new InstanceGroupConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInstanceGroupConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iinstancegroupconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.instancegroupconfig-class)` | InstanceGroupConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataproc.v1.InstanceGroupConfig;

Decodes an InstanceGroupConfig message from the specified reader or buffer.

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
`[InstanceGroupConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.instancegroupconfig-class)` | InstanceGroupConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataproc.v1.InstanceGroupConfig;

Decodes an InstanceGroupConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.instancegroupconfig-class)` | InstanceGroupConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataproc.v1.IInstanceGroupConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified InstanceGroupConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInstanceGroupConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iinstancegroupconfig)`   
InstanceGroupConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataproc.v1.IInstanceGroupConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified InstanceGroupConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInstanceGroupConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iinstancegroupconfig)`   
InstanceGroupConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataproc.v1.InstanceGroupConfig;

Creates an InstanceGroupConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.instancegroupconfig-class)` | InstanceGroupConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for InstanceGroupConfig

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

Converts this InstanceGroupConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataproc.v1.InstanceGroupConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an InstanceGroupConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[InstanceGroupConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.instancegroupconfig-class)`   
InstanceGroupConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an InstanceGroupConfig message.

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
