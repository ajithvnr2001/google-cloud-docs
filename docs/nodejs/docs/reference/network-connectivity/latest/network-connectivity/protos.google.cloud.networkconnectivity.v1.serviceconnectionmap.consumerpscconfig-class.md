---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.consumerpscconfig-class
title: Class protos.google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConfig (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:24.005994+00:00
---

# Class protos.google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConfig (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.consumerpscconfig-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConfig (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.6.0  4.2.0  3.6.0  3.2.0  2.3.3  2.2.0  2.1.2  1.5.0  1.4.2  1.3.0  1.2.1  1.1.6 

Represents a ConsumerPscConfig.

## Implements

[protos.google.cloud.networkconnectivity.v1.ServiceConnectionMap.IConsumerPscConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.iconsumerpscconfig)

## Package

[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.networkconnectivity.v1.ServiceConnectionMap.IConsumerPscConfig);

Constructs a new ConsumerPscConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConsumerPscConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.iconsumerpscconfig)`   
Properties to set  
  
## Properties 

### consumerInstanceProject
    
    
    public consumerInstanceProject: string;

ConsumerPscConfig consumerInstanceProject.

### disableGlobalAccess
    
    
    public disableGlobalAccess: boolean;

ConsumerPscConfig disableGlobalAccess.

### ipVersion
    
    
    public ipVersion?: (google.cloud.networkconnectivity.v1.IPVersion|keyof typeof google.cloud.networkconnectivity.v1.IPVersion|null);

ConsumerPscConfig ipVersion.

### network
    
    
    public network: string;

ConsumerPscConfig network.

### producerInstanceId
    
    
    public producerInstanceId: string;

ConsumerPscConfig producerInstanceId.

### producerInstanceMetadata
    
    
    public producerInstanceMetadata: { [k: string]: string };

ConsumerPscConfig producerInstanceMetadata.

### project
    
    
    public project: string;

ConsumerPscConfig project.

### serviceAttachmentIpAddressMap
    
    
    public serviceAttachmentIpAddressMap: { [k: string]: string };

ConsumerPscConfig serviceAttachmentIpAddressMap.

### state
    
    
    public state: (google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConfig.State|keyof typeof google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConfig.State);

ConsumerPscConfig state.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.networkconnectivity.v1.ServiceConnectionMap.IConsumerPscConfig): google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConfig;

Creates a new ConsumerPscConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConsumerPscConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.iconsumerpscconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ConsumerPscConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.consumerpscconfig-class)` | ConsumerPscConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConfig;

Decodes a ConsumerPscConfig message from the specified reader or buffer.

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
`[ConsumerPscConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.consumerpscconfig-class)` | ConsumerPscConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConfig;

Decodes a ConsumerPscConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ConsumerPscConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.consumerpscconfig-class)` | ConsumerPscConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.networkconnectivity.v1.ServiceConnectionMap.IConsumerPscConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ConsumerPscConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConsumerPscConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.iconsumerpscconfig)`   
ConsumerPscConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.networkconnectivity.v1.ServiceConnectionMap.IConsumerPscConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ConsumerPscConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConsumerPscConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.iconsumerpscconfig)`   
ConsumerPscConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConfig;

Creates a ConsumerPscConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ConsumerPscConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.consumerpscconfig-class)` | ConsumerPscConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ConsumerPscConfig

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

Converts this ConsumerPscConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ConsumerPscConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ConsumerPscConfig](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.consumerpscconfig-class)`   
ConsumerPscConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ConsumerPscConfig message.

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
