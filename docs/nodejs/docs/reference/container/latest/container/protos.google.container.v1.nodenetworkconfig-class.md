---
url: https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.nodenetworkconfig-class
title: Class protos.google.container.v1.NodeNetworkConfig (7.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:15.330540+00:00
---

# Class protos.google.container.v1.NodeNetworkConfig (7.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.nodenetworkconfig-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.container.v1.NodeNetworkConfig (7.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.2.1 (latest)  7.1.0  6.8.0  6.7.0  6.1.0  5.19.0  5.17.0  5.15.1  5.14.0  5.10.0  5.9.0  5.8.0  5.6.0  5.5.0  5.4.1  5.1.0  4.11.0  4.10.0  4.9.0  4.7.1  4.4.0  4.3.0  4.2.0  4.1.3  3.0.0  2.6.0  2.5.0  2.4.4  2.3.2 

Represents a NodeNetworkConfig.

## Implements

[protos.google.container.v1.INodeNetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.inodenetworkconfig)

## Package

[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.container.v1.INodeNetworkConfig);

Constructs a new NodeNetworkConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INodeNetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.inodenetworkconfig)`   
Properties to set  
  
## Properties 

### acceleratorNetworkProfile
    
    
    public acceleratorNetworkProfile: string;

NodeNetworkConfig acceleratorNetworkProfile.

### additionalNodeNetworkConfigs
    
    
    public additionalNodeNetworkConfigs: google.container.v1.IAdditionalNodeNetworkConfig[];

NodeNetworkConfig additionalNodeNetworkConfigs.

### additionalPodNetworkConfigs
    
    
    public additionalPodNetworkConfigs: google.container.v1.IAdditionalPodNetworkConfig[];

NodeNetworkConfig additionalPodNetworkConfigs.

### createPodRange
    
    
    public createPodRange: boolean;

NodeNetworkConfig createPodRange.

### enablePrivateNodes
    
    
    public enablePrivateNodes?: (boolean|null);

NodeNetworkConfig enablePrivateNodes.

### networkPerformanceConfig
    
    
    public networkPerformanceConfig?: (google.container.v1.NodeNetworkConfig.INetworkPerformanceConfig|null);

NodeNetworkConfig networkPerformanceConfig.

### networkTierConfig
    
    
    public networkTierConfig?: (google.container.v1.INetworkTierConfig|null);

NodeNetworkConfig networkTierConfig.

### podCidrOverprovisionConfig
    
    
    public podCidrOverprovisionConfig?: (google.container.v1.IPodCIDROverprovisionConfig|null);

NodeNetworkConfig podCidrOverprovisionConfig.

### podIpv4CidrBlock
    
    
    public podIpv4CidrBlock: string;

NodeNetworkConfig podIpv4CidrBlock.

### podIpv4RangeUtilization
    
    
    public podIpv4RangeUtilization: number;

NodeNetworkConfig podIpv4RangeUtilization.

### podRange
    
    
    public podRange: string;

NodeNetworkConfig podRange.

### subnetwork
    
    
    public subnetwork: string;

NodeNetworkConfig subnetwork.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.container.v1.INodeNetworkConfig): google.container.v1.NodeNetworkConfig;

Creates a new NodeNetworkConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INodeNetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.inodenetworkconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[NodeNetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.nodenetworkconfig-class)` | NodeNetworkConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.container.v1.NodeNetworkConfig;

Decodes a NodeNetworkConfig message from the specified reader or buffer.

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
`[NodeNetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.nodenetworkconfig-class)` | NodeNetworkConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.container.v1.NodeNetworkConfig;

Decodes a NodeNetworkConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[NodeNetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.nodenetworkconfig-class)` | NodeNetworkConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.container.v1.INodeNetworkConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified NodeNetworkConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INodeNetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.inodenetworkconfig)`   
NodeNetworkConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.container.v1.INodeNetworkConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified NodeNetworkConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INodeNetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.inodenetworkconfig)`   
NodeNetworkConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.container.v1.NodeNetworkConfig;

Creates a NodeNetworkConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[NodeNetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.nodenetworkconfig-class)` | NodeNetworkConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for NodeNetworkConfig

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

Converts this NodeNetworkConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.container.v1.NodeNetworkConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a NodeNetworkConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[NodeNetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.nodenetworkconfig-class)`   
NodeNetworkConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a NodeNetworkConfig message.

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
