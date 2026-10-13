---
url: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awsnodeconfig
title: Class protos.google.cloud.gkemulticloud.v1.AwsNodeConfig (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:41.610282+00:00
---

# Class protos.google.cloud.gkemulticloud.v1.AwsNodeConfig (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awsnodeconfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gkemulticloud.v1.AwsNodeConfig (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.4.0  2.3.0  2.1.0  2.0.1  1.5.0  1.1.0  0.3.2  0.1.4 

Represents an AwsNodeConfig.

## Implements

[protos.google.cloud.gkemulticloud.v1.IAwsNodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iawsnodeconfig)

## Package

[@google-cloud/gkemulticloud](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.gkemulticloud.v1.IAwsNodeConfig);

Constructs a new AwsNodeConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAwsNodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iawsnodeconfig)`   
Properties to set  
  
## Properties 

### autoscalingMetricsCollection
    
    
    public autoscalingMetricsCollection?: (google.cloud.gkemulticloud.v1.IAwsAutoscalingGroupMetricsCollection|null);

AwsNodeConfig autoscalingMetricsCollection.

### configEncryption
    
    
    public configEncryption?: (google.cloud.gkemulticloud.v1.IAwsConfigEncryption|null);

AwsNodeConfig configEncryption.

### iamInstanceProfile
    
    
    public iamInstanceProfile: string;

AwsNodeConfig iamInstanceProfile.

### imageType
    
    
    public imageType: string;

AwsNodeConfig imageType.

### instancePlacement
    
    
    public instancePlacement?: (google.cloud.gkemulticloud.v1.IAwsInstancePlacement|null);

AwsNodeConfig instancePlacement.

### instanceType
    
    
    public instanceType: string;

AwsNodeConfig instanceType.

### labels
    
    
    public labels: { [k: string]: string };

AwsNodeConfig labels.

### proxyConfig
    
    
    public proxyConfig?: (google.cloud.gkemulticloud.v1.IAwsProxyConfig|null);

AwsNodeConfig proxyConfig.

### rootVolume
    
    
    public rootVolume?: (google.cloud.gkemulticloud.v1.IAwsVolumeTemplate|null);

AwsNodeConfig rootVolume.

### securityGroupIds
    
    
    public securityGroupIds: string[];

AwsNodeConfig securityGroupIds.

### spotConfig
    
    
    public spotConfig?: (google.cloud.gkemulticloud.v1.ISpotConfig|null);

AwsNodeConfig spotConfig.

### sshConfig
    
    
    public sshConfig?: (google.cloud.gkemulticloud.v1.IAwsSshConfig|null);

AwsNodeConfig sshConfig.

### tags
    
    
    public tags: { [k: string]: string };

AwsNodeConfig tags.

### taints
    
    
    public taints: google.cloud.gkemulticloud.v1.INodeTaint[];

AwsNodeConfig taints.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.gkemulticloud.v1.IAwsNodeConfig): google.cloud.gkemulticloud.v1.AwsNodeConfig;

Creates a new AwsNodeConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAwsNodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iawsnodeconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AwsNodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awsnodeconfig)` | AwsNodeConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.gkemulticloud.v1.AwsNodeConfig;

Decodes an AwsNodeConfig message from the specified reader or buffer.

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
`[AwsNodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awsnodeconfig)` | AwsNodeConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.gkemulticloud.v1.AwsNodeConfig;

Decodes an AwsNodeConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AwsNodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awsnodeconfig)` | AwsNodeConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.gkemulticloud.v1.IAwsNodeConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AwsNodeConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAwsNodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iawsnodeconfig)`   
AwsNodeConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.gkemulticloud.v1.IAwsNodeConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AwsNodeConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAwsNodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iawsnodeconfig)`   
AwsNodeConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.gkemulticloud.v1.AwsNodeConfig;

Creates an AwsNodeConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AwsNodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awsnodeconfig)` | AwsNodeConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AwsNodeConfig

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

Converts this AwsNodeConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.gkemulticloud.v1.AwsNodeConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AwsNodeConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AwsNodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awsnodeconfig)`   
AwsNodeConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AwsNodeConfig message.

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
