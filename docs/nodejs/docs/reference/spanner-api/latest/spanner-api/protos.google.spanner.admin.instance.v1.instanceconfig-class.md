---
url: https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instanceconfig-class
title: Class protos.google.spanner.admin.instance.v1.InstanceConfig (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:30.631913+00:00
---

# Class protos.google.spanner.admin.instance.v1.InstanceConfig (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instanceconfig-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.spanner.admin.instance.v1.InstanceConfig (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an InstanceConfig.

## Implements

[protos.google.spanner.admin.instance.v1.IInstanceConfig](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.iinstanceconfig)

## Package

[@google-cloud/spanner-api](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.spanner.admin.instance.v1.IInstanceConfig);

Constructs a new InstanceConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInstanceConfig](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.iinstanceconfig)`   
Properties to set  
  
## Properties 

### baseConfig
    
    
    public baseConfig: string;

InstanceConfig baseConfig.

### configType
    
    
    public configType: (google.spanner.admin.instance.v1.InstanceConfig.Type|keyof typeof google.spanner.admin.instance.v1.InstanceConfig.Type);

InstanceConfig configType.

### displayName
    
    
    public displayName: string;

InstanceConfig displayName.

### etag
    
    
    public etag: string;

InstanceConfig etag.

### freeInstanceAvailability
    
    
    public freeInstanceAvailability: (google.spanner.admin.instance.v1.InstanceConfig.FreeInstanceAvailability|keyof typeof google.spanner.admin.instance.v1.InstanceConfig.FreeInstanceAvailability);

InstanceConfig freeInstanceAvailability.

### labels
    
    
    public labels: { [k: string]: string };

InstanceConfig labels.

### leaderOptions
    
    
    public leaderOptions: string[];

InstanceConfig leaderOptions.

### name
    
    
    public name: string;

InstanceConfig name.

### optionalReplicas
    
    
    public optionalReplicas: google.spanner.admin.instance.v1.IReplicaInfo[];

InstanceConfig optionalReplicas.

### quorumType
    
    
    public quorumType: (google.spanner.admin.instance.v1.InstanceConfig.QuorumType|keyof typeof google.spanner.admin.instance.v1.InstanceConfig.QuorumType);

InstanceConfig quorumType.

### reconciling
    
    
    public reconciling: boolean;

InstanceConfig reconciling.

### replicas
    
    
    public replicas: google.spanner.admin.instance.v1.IReplicaInfo[];

InstanceConfig replicas.

### state
    
    
    public state: (google.spanner.admin.instance.v1.InstanceConfig.State|keyof typeof google.spanner.admin.instance.v1.InstanceConfig.State);

InstanceConfig state.

### storageLimitPerProcessingUnit
    
    
    public storageLimitPerProcessingUnit: (number|Long|string);

InstanceConfig storageLimitPerProcessingUnit.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.spanner.admin.instance.v1.IInstanceConfig): google.spanner.admin.instance.v1.InstanceConfig;

Creates a new InstanceConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInstanceConfig](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.iinstanceconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[InstanceConfig](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instanceconfig-class)` | InstanceConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.spanner.admin.instance.v1.InstanceConfig;

Decodes an InstanceConfig message from the specified reader or buffer.

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
`[InstanceConfig](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instanceconfig-class)` | InstanceConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.spanner.admin.instance.v1.InstanceConfig;

Decodes an InstanceConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[InstanceConfig](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instanceconfig-class)` | InstanceConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.spanner.admin.instance.v1.IInstanceConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified InstanceConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInstanceConfig](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.iinstanceconfig)`   
InstanceConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.spanner.admin.instance.v1.IInstanceConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified InstanceConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInstanceConfig](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.iinstanceconfig)`   
InstanceConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.spanner.admin.instance.v1.InstanceConfig;

Creates an InstanceConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[InstanceConfig](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instanceconfig-class)` | InstanceConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for InstanceConfig

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

Converts this InstanceConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.spanner.admin.instance.v1.InstanceConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an InstanceConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[InstanceConfig](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instanceconfig-class)`   
InstanceConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an InstanceConfig message.

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

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
