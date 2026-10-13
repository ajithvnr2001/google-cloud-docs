---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.effectivevpcflowlogsconfig-class
title: Class protos.google.cloud.networkmanagement.v1.EffectiveVpcFlowLogsConfig (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:17.160118+00:00
---

# Class protos.google.cloud.networkmanagement.v1.EffectiveVpcFlowLogsConfig (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.effectivevpcflowlogsconfig-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networkmanagement.v1.EffectiveVpcFlowLogsConfig (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.2.0  4.2.0  3.11.0  3.10.0  3.9.0  3.7.0  3.3.0  3.0.0  2.4.2  2.3.1  2.2.0  1.1.2  1.0.2 

Represents an EffectiveVpcFlowLogsConfig.

## Implements

[protos.google.cloud.networkmanagement.v1.IEffectiveVpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.ieffectivevpcflowlogsconfig)

## Package

[@google-cloud/network-management](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.networkmanagement.v1.IEffectiveVpcFlowLogsConfig);

Constructs a new EffectiveVpcFlowLogsConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEffectiveVpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.ieffectivevpcflowlogsconfig)`   
Properties to set  
  
## Properties 

### aggregationInterval
    
    
    public aggregationInterval?: (google.cloud.networkmanagement.v1.VpcFlowLogsConfig.AggregationInterval|keyof typeof google.cloud.networkmanagement.v1.VpcFlowLogsConfig.AggregationInterval|null);

EffectiveVpcFlowLogsConfig aggregationInterval.

### crossProjectMetadata
    
    
    public crossProjectMetadata?: (google.cloud.networkmanagement.v1.VpcFlowLogsConfig.CrossProjectMetadata|keyof typeof google.cloud.networkmanagement.v1.VpcFlowLogsConfig.CrossProjectMetadata|null);

EffectiveVpcFlowLogsConfig crossProjectMetadata.

### filterExpr
    
    
    public filterExpr?: (string|null);

EffectiveVpcFlowLogsConfig filterExpr.

### flowSampling
    
    
    public flowSampling?: (number|null);

EffectiveVpcFlowLogsConfig flowSampling.

### interconnectAttachment
    
    
    public interconnectAttachment?: (string|null);

EffectiveVpcFlowLogsConfig interconnectAttachment.

### metadata
    
    
    public metadata?: (google.cloud.networkmanagement.v1.VpcFlowLogsConfig.Metadata|keyof typeof google.cloud.networkmanagement.v1.VpcFlowLogsConfig.Metadata|null);

EffectiveVpcFlowLogsConfig metadata.

### metadataFields
    
    
    public metadataFields: string[];

EffectiveVpcFlowLogsConfig metadataFields.

### name
    
    
    public name: string;

EffectiveVpcFlowLogsConfig name.

### network
    
    
    public network?: (string|null);

EffectiveVpcFlowLogsConfig network.

### scope
    
    
    public scope?: (google.cloud.networkmanagement.v1.EffectiveVpcFlowLogsConfig.Scope|keyof typeof google.cloud.networkmanagement.v1.EffectiveVpcFlowLogsConfig.Scope|null);

EffectiveVpcFlowLogsConfig scope.

### state
    
    
    public state?: (google.cloud.networkmanagement.v1.VpcFlowLogsConfig.State|keyof typeof google.cloud.networkmanagement.v1.VpcFlowLogsConfig.State|null);

EffectiveVpcFlowLogsConfig state.

### subnet
    
    
    public subnet?: (string|null);

EffectiveVpcFlowLogsConfig subnet.

### targetResource
    
    
    public targetResource?: ("network"|"subnet"|"interconnectAttachment"|"vpnTunnel");

EffectiveVpcFlowLogsConfig targetResource.

### vpnTunnel
    
    
    public vpnTunnel?: (string|null);

EffectiveVpcFlowLogsConfig vpnTunnel.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.networkmanagement.v1.IEffectiveVpcFlowLogsConfig): google.cloud.networkmanagement.v1.EffectiveVpcFlowLogsConfig;

Creates a new EffectiveVpcFlowLogsConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEffectiveVpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.ieffectivevpcflowlogsconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[EffectiveVpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.effectivevpcflowlogsconfig-class)` | EffectiveVpcFlowLogsConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.networkmanagement.v1.EffectiveVpcFlowLogsConfig;

Decodes an EffectiveVpcFlowLogsConfig message from the specified reader or buffer.

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
`[EffectiveVpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.effectivevpcflowlogsconfig-class)` | EffectiveVpcFlowLogsConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.networkmanagement.v1.EffectiveVpcFlowLogsConfig;

Decodes an EffectiveVpcFlowLogsConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[EffectiveVpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.effectivevpcflowlogsconfig-class)` | EffectiveVpcFlowLogsConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.networkmanagement.v1.IEffectiveVpcFlowLogsConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EffectiveVpcFlowLogsConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEffectiveVpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.ieffectivevpcflowlogsconfig)`   
EffectiveVpcFlowLogsConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.networkmanagement.v1.IEffectiveVpcFlowLogsConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EffectiveVpcFlowLogsConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEffectiveVpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.ieffectivevpcflowlogsconfig)`   
EffectiveVpcFlowLogsConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.networkmanagement.v1.EffectiveVpcFlowLogsConfig;

Creates an EffectiveVpcFlowLogsConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[EffectiveVpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.effectivevpcflowlogsconfig-class)` | EffectiveVpcFlowLogsConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for EffectiveVpcFlowLogsConfig

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

Converts this EffectiveVpcFlowLogsConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.networkmanagement.v1.EffectiveVpcFlowLogsConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an EffectiveVpcFlowLogsConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[EffectiveVpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.effectivevpcflowlogsconfig-class)`   
EffectiveVpcFlowLogsConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an EffectiveVpcFlowLogsConfig message.

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
