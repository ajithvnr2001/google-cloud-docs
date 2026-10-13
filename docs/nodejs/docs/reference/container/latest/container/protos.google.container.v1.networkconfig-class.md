---
url: https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.networkconfig-class
title: Class protos.google.container.v1.NetworkConfig (7.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:10.889201+00:00
---

# Class protos.google.container.v1.NetworkConfig (7.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.networkconfig-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.container.v1.NetworkConfig (7.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.2.1 (latest)  7.1.0  6.8.0  6.7.0  6.1.0  5.19.0  5.17.0  5.15.1  5.14.0  5.10.0  5.9.0  5.8.0  5.6.0  5.5.0  5.4.1  5.1.0  4.11.0  4.10.0  4.9.0  4.7.1  4.4.0  4.3.0  4.2.0  4.1.3  3.0.0  2.6.0  2.5.0  2.4.4  2.3.2 

Represents a NetworkConfig.

## Implements

[protos.google.container.v1.INetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.inetworkconfig)

## Package

[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.container.v1.INetworkConfig);

Constructs a new NetworkConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.inetworkconfig)`   
Properties to set  
  
## Properties 

### datapathProvider
    
    
    public datapathProvider: (google.container.v1.DatapathProvider|keyof typeof google.container.v1.DatapathProvider);

NetworkConfig datapathProvider.

### dataplaneV2Config
    
    
    public dataplaneV2Config?: (google.container.v1.IDataplaneV2Config|null);

NetworkConfig dataplaneV2Config.

### defaultEnablePrivateNodes
    
    
    public defaultEnablePrivateNodes?: (boolean|null);

NetworkConfig defaultEnablePrivateNodes.

### defaultSnatStatus
    
    
    public defaultSnatStatus?: (google.container.v1.IDefaultSnatStatus|null);

NetworkConfig defaultSnatStatus.

### disableL4LbFirewallReconciliation
    
    
    public disableL4LbFirewallReconciliation?: (boolean|null);

NetworkConfig disableL4LbFirewallReconciliation.

### dnsConfig
    
    
    public dnsConfig?: (google.container.v1.IDNSConfig|null);

NetworkConfig dnsConfig.

### enableCiliumClusterwideNetworkPolicy
    
    
    public enableCiliumClusterwideNetworkPolicy?: (boolean|null);

NetworkConfig enableCiliumClusterwideNetworkPolicy.

### enableFqdnNetworkPolicy
    
    
    public enableFqdnNetworkPolicy?: (boolean|null);

NetworkConfig enableFqdnNetworkPolicy.

### enableIntraNodeVisibility
    
    
    public enableIntraNodeVisibility: boolean;

NetworkConfig enableIntraNodeVisibility.

### enableL4ilbSubsetting
    
    
    public enableL4ilbSubsetting: boolean;

NetworkConfig enableL4ilbSubsetting.

### enableMultiNetworking
    
    
    public enableMultiNetworking: boolean;

NetworkConfig enableMultiNetworking.

### gatewayApiConfig
    
    
    public gatewayApiConfig?: (google.container.v1.IGatewayAPIConfig|null);

NetworkConfig gatewayApiConfig.

### inTransitEncryptionConfig
    
    
    public inTransitEncryptionConfig?: (google.container.v1.InTransitEncryptionConfig|keyof typeof google.container.v1.InTransitEncryptionConfig|null);

NetworkConfig inTransitEncryptionConfig.

### network
    
    
    public network: string;

NetworkConfig network.

### networkPerformanceConfig
    
    
    public networkPerformanceConfig?: (google.container.v1.NetworkConfig.IClusterNetworkPerformanceConfig|null);

NetworkConfig networkPerformanceConfig.

### privateIpv6GoogleAccess
    
    
    public privateIpv6GoogleAccess: (google.container.v1.PrivateIPv6GoogleAccess|keyof typeof google.container.v1.PrivateIPv6GoogleAccess);

NetworkConfig privateIpv6GoogleAccess.

### serviceExternalIpsConfig
    
    
    public serviceExternalIpsConfig?: (google.container.v1.IServiceExternalIPsConfig|null);

NetworkConfig serviceExternalIpsConfig.

### subnetwork
    
    
    public subnetwork: string;

NetworkConfig subnetwork.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.container.v1.INetworkConfig): google.container.v1.NetworkConfig;

Creates a new NetworkConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.inetworkconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[NetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.networkconfig-class)` | NetworkConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.container.v1.NetworkConfig;

Decodes a NetworkConfig message from the specified reader or buffer.

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
`[NetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.networkconfig-class)` | NetworkConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.container.v1.NetworkConfig;

Decodes a NetworkConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[NetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.networkconfig-class)` | NetworkConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.container.v1.INetworkConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified NetworkConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.inetworkconfig)`   
NetworkConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.container.v1.INetworkConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified NetworkConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.inetworkconfig)`   
NetworkConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.container.v1.NetworkConfig;

Creates a NetworkConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[NetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.networkconfig-class)` | NetworkConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for NetworkConfig

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

Converts this NetworkConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.container.v1.NetworkConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a NetworkConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[NetworkConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.networkconfig-class)`   
NetworkConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a NetworkConfig message.

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
