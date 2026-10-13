---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.consumerpscconnection-class
title: Class protos.google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConnection (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:25.101544+00:00
---

# Class protos.google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConnection (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.consumerpscconnection-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConnection (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.6.0  4.2.0  3.6.0  3.2.0  2.3.3  2.2.0  2.1.2  1.5.0  1.4.2  1.3.0  1.2.1  1.1.6 

Represents a ConsumerPscConnection.

## Implements

[protos.google.cloud.networkconnectivity.v1.ServiceConnectionMap.IConsumerPscConnection](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.iconsumerpscconnection)

## Package

[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.networkconnectivity.v1.ServiceConnectionMap.IConsumerPscConnection);

Constructs a new ConsumerPscConnection.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConsumerPscConnection](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.iconsumerpscconnection)`   
Properties to set  
  
## Properties 

### error
    
    
    public error?: (google.rpc.IStatus|null);

ConsumerPscConnection error.

### errorInfo
    
    
    public errorInfo?: (google.rpc.IErrorInfo|null);

ConsumerPscConnection errorInfo.

### errorType
    
    
    public errorType: (google.cloud.networkconnectivity.v1.ConnectionErrorType|keyof typeof google.cloud.networkconnectivity.v1.ConnectionErrorType);

ConsumerPscConnection errorType.

### forwardingRule
    
    
    public forwardingRule: string;

ConsumerPscConnection forwardingRule.

### gceOperation
    
    
    public gceOperation: string;

ConsumerPscConnection gceOperation.

### ip
    
    
    public ip: string;

ConsumerPscConnection ip.

### ipVersion
    
    
    public ipVersion?: (google.cloud.networkconnectivity.v1.IPVersion|keyof typeof google.cloud.networkconnectivity.v1.IPVersion|null);

ConsumerPscConnection ipVersion.

### network
    
    
    public network: string;

ConsumerPscConnection network.

### producerInstanceId
    
    
    public producerInstanceId: string;

ConsumerPscConnection producerInstanceId.

### producerInstanceMetadata
    
    
    public producerInstanceMetadata: { [k: string]: string };

ConsumerPscConnection producerInstanceMetadata.

### project
    
    
    public project: string;

ConsumerPscConnection project.

### pscConnectionId
    
    
    public pscConnectionId: string;

ConsumerPscConnection pscConnectionId.

### selectedSubnetwork
    
    
    public selectedSubnetwork: string;

ConsumerPscConnection selectedSubnetwork.

### serviceAttachmentUri
    
    
    public serviceAttachmentUri: string;

ConsumerPscConnection serviceAttachmentUri.

### state
    
    
    public state: (google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConnection.State|keyof typeof google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConnection.State);

ConsumerPscConnection state.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.networkconnectivity.v1.ServiceConnectionMap.IConsumerPscConnection): google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConnection;

Creates a new ConsumerPscConnection instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConsumerPscConnection](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.iconsumerpscconnection)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ConsumerPscConnection](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.consumerpscconnection-class)` | ConsumerPscConnection instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConnection;

Decodes a ConsumerPscConnection message from the specified reader or buffer.

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
`[ConsumerPscConnection](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.consumerpscconnection-class)` | ConsumerPscConnection  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConnection;

Decodes a ConsumerPscConnection message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ConsumerPscConnection](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.consumerpscconnection-class)` | ConsumerPscConnection  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.networkconnectivity.v1.ServiceConnectionMap.IConsumerPscConnection, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ConsumerPscConnection message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConsumerPscConnection](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.iconsumerpscconnection)`   
ConsumerPscConnection message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.networkconnectivity.v1.ServiceConnectionMap.IConsumerPscConnection, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ConsumerPscConnection message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConsumerPscConnection](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.iconsumerpscconnection)`   
ConsumerPscConnection message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConnection;

Creates a ConsumerPscConnection message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ConsumerPscConnection](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.consumerpscconnection-class)` | ConsumerPscConnection  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ConsumerPscConnection

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

Converts this ConsumerPscConnection to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.networkconnectivity.v1.ServiceConnectionMap.ConsumerPscConnection, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ConsumerPscConnection message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ConsumerPscConnection](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.serviceconnectionmap.consumerpscconnection-class)`   
ConsumerPscConnection  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ConsumerPscConnection message.

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
