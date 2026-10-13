---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.vpcflowlogsconfig-class
title: Class protos.google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:43.835315+00:00
---

# Class protos.google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.vpcflowlogsconfig-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.2.0  4.2.0  3.11.0  3.10.0  3.9.0  3.7.0  3.3.0  3.0.0  2.4.2  2.3.1  2.2.0  1.1.2  1.0.2 

Represents a VpcFlowLogsConfig.

## Implements

[protos.google.cloud.networkmanagement.v1beta1.IVpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ivpcflowlogsconfig)

## Package

[@google-cloud/network-management](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.networkmanagement.v1beta1.IVpcFlowLogsConfig);

Constructs a new VpcFlowLogsConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IVpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ivpcflowlogsconfig)`   
Properties to set  
  
## Properties 

### aggregationInterval
    
    
    public aggregationInterval?: (google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig.AggregationInterval|keyof typeof google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig.AggregationInterval|null);

VpcFlowLogsConfig aggregationInterval.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

VpcFlowLogsConfig createTime.

### crossProjectMetadata
    
    
    public crossProjectMetadata?: (google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig.CrossProjectMetadata|keyof typeof google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig.CrossProjectMetadata|null);

VpcFlowLogsConfig crossProjectMetadata.

### description
    
    
    public description?: (string|null);

VpcFlowLogsConfig description.

### filterExpr
    
    
    public filterExpr?: (string|null);

VpcFlowLogsConfig filterExpr.

### flowSampling
    
    
    public flowSampling?: (number|null);

VpcFlowLogsConfig flowSampling.

### interconnectAttachment
    
    
    public interconnectAttachment?: (string|null);

VpcFlowLogsConfig interconnectAttachment.

### labels
    
    
    public labels: { [k: string]: string };

VpcFlowLogsConfig labels.

### metadata
    
    
    public metadata?: (google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig.Metadata|keyof typeof google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig.Metadata|null);

VpcFlowLogsConfig metadata.

### metadataFields
    
    
    public metadataFields: string[];

VpcFlowLogsConfig metadataFields.

### name
    
    
    public name: string;

VpcFlowLogsConfig name.

### network
    
    
    public network?: (string|null);

VpcFlowLogsConfig network.

### state
    
    
    public state?: (google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig.State|keyof typeof google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig.State|null);

VpcFlowLogsConfig state.

### subnet
    
    
    public subnet?: (string|null);

VpcFlowLogsConfig subnet.

### targetResource
    
    
    public targetResource?: ("network"|"subnet"|"interconnectAttachment"|"vpnTunnel");

VpcFlowLogsConfig targetResource.

### targetResourceState
    
    
    public targetResourceState?: (google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig.TargetResourceState|keyof typeof google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig.TargetResourceState|null);

VpcFlowLogsConfig targetResourceState.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

VpcFlowLogsConfig updateTime.

### vpnTunnel
    
    
    public vpnTunnel?: (string|null);

VpcFlowLogsConfig vpnTunnel.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.networkmanagement.v1beta1.IVpcFlowLogsConfig): google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig;

Creates a new VpcFlowLogsConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IVpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ivpcflowlogsconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[VpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.vpcflowlogsconfig-class)` | VpcFlowLogsConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig;

Decodes a VpcFlowLogsConfig message from the specified reader or buffer.

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
`[VpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.vpcflowlogsconfig-class)` | VpcFlowLogsConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig;

Decodes a VpcFlowLogsConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[VpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.vpcflowlogsconfig-class)` | VpcFlowLogsConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.networkmanagement.v1beta1.IVpcFlowLogsConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified VpcFlowLogsConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IVpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ivpcflowlogsconfig)`   
VpcFlowLogsConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.networkmanagement.v1beta1.IVpcFlowLogsConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified VpcFlowLogsConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IVpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.ivpcflowlogsconfig)`   
VpcFlowLogsConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig;

Creates a VpcFlowLogsConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[VpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.vpcflowlogsconfig-class)` | VpcFlowLogsConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for VpcFlowLogsConfig

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

Converts this VpcFlowLogsConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a VpcFlowLogsConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[VpcFlowLogsConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1beta1.vpcflowlogsconfig-class)`   
VpcFlowLogsConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a VpcFlowLogsConfig message.

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
