---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.endpointinfo
title: Class protos.google.cloud.networkmanagement.v1.EndpointInfo (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:17.667683+00:00
---

# Class protos.google.cloud.networkmanagement.v1.EndpointInfo (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.endpointinfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networkmanagement.v1.EndpointInfo (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.2.0  4.2.0  3.11.0  3.10.0  3.9.0  3.7.0  3.3.0  3.0.0  2.4.2  2.3.1  2.2.0  1.1.2  1.0.2 

Represents an EndpointInfo.

## Implements

[protos.google.cloud.networkmanagement.v1.IEndpointInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.iendpointinfo)

## Package

[@google-cloud/network-management](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.networkmanagement.v1.IEndpointInfo);

Constructs a new EndpointInfo.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEndpointInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.iendpointinfo)`   
Properties to set  
  
## Properties 

### destinationIp
    
    
    public destinationIp: string;

EndpointInfo destinationIp.

### destinationNetworkUri
    
    
    public destinationNetworkUri: string;

EndpointInfo destinationNetworkUri.

### destinationPort
    
    
    public destinationPort: number;

EndpointInfo destinationPort.

### protocol
    
    
    public protocol: string;

EndpointInfo protocol.

### sourceAgentUri
    
    
    public sourceAgentUri: string;

EndpointInfo sourceAgentUri.

### sourceIp
    
    
    public sourceIp: string;

EndpointInfo sourceIp.

### sourceNetworkUri
    
    
    public sourceNetworkUri: string;

EndpointInfo sourceNetworkUri.

### sourcePort
    
    
    public sourcePort: number;

EndpointInfo sourcePort.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.networkmanagement.v1.IEndpointInfo): google.cloud.networkmanagement.v1.EndpointInfo;

Creates a new EndpointInfo instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEndpointInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.iendpointinfo)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[EndpointInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.endpointinfo)` | EndpointInfo instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.networkmanagement.v1.EndpointInfo;

Decodes an EndpointInfo message from the specified reader or buffer.

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
`[EndpointInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.endpointinfo)` | EndpointInfo  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.networkmanagement.v1.EndpointInfo;

Decodes an EndpointInfo message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[EndpointInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.endpointinfo)` | EndpointInfo  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.networkmanagement.v1.IEndpointInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EndpointInfo message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEndpointInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.iendpointinfo)`   
EndpointInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.networkmanagement.v1.IEndpointInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EndpointInfo message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEndpointInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.iendpointinfo)`   
EndpointInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.networkmanagement.v1.EndpointInfo;

Creates an EndpointInfo message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[EndpointInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.endpointinfo)` | EndpointInfo  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for EndpointInfo

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

Converts this EndpointInfo to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.networkmanagement.v1.EndpointInfo, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an EndpointInfo message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[EndpointInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.endpointinfo)`   
EndpointInfo  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an EndpointInfo message.

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
