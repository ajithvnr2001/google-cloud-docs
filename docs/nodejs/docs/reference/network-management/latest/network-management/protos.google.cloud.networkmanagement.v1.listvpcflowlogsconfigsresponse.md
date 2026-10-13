---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.listvpcflowlogsconfigsresponse
title: Class protos.google.cloud.networkmanagement.v1.ListVpcFlowLogsConfigsResponse (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:21.254755+00:00
---

# Class protos.google.cloud.networkmanagement.v1.ListVpcFlowLogsConfigsResponse (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.listvpcflowlogsconfigsresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networkmanagement.v1.ListVpcFlowLogsConfigsResponse (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.2.0  4.2.0  3.11.0  3.10.0  3.9.0  3.7.0  3.3.0  3.0.0  2.4.2  2.3.1  2.2.0  1.1.2  1.0.2 

Represents a ListVpcFlowLogsConfigsResponse.

## Implements

[protos.google.cloud.networkmanagement.v1.IListVpcFlowLogsConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.ilistvpcflowlogsconfigsresponse)

## Package

[@google-cloud/network-management](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.networkmanagement.v1.IListVpcFlowLogsConfigsResponse);

Constructs a new ListVpcFlowLogsConfigsResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListVpcFlowLogsConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.ilistvpcflowlogsconfigsresponse)`   
Properties to set  
  
## Properties 

### nextPageToken
    
    
    public nextPageToken: string;

ListVpcFlowLogsConfigsResponse nextPageToken.

### unreachable
    
    
    public unreachable: string[];

ListVpcFlowLogsConfigsResponse unreachable.

### vpcFlowLogsConfigs
    
    
    public vpcFlowLogsConfigs: google.cloud.networkmanagement.v1.IVpcFlowLogsConfig[];

ListVpcFlowLogsConfigsResponse vpcFlowLogsConfigs.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.networkmanagement.v1.IListVpcFlowLogsConfigsResponse): google.cloud.networkmanagement.v1.ListVpcFlowLogsConfigsResponse;

Creates a new ListVpcFlowLogsConfigsResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListVpcFlowLogsConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.ilistvpcflowlogsconfigsresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListVpcFlowLogsConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.listvpcflowlogsconfigsresponse)` | ListVpcFlowLogsConfigsResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.networkmanagement.v1.ListVpcFlowLogsConfigsResponse;

Decodes a ListVpcFlowLogsConfigsResponse message from the specified reader or buffer.

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
`[ListVpcFlowLogsConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.listvpcflowlogsconfigsresponse)` | ListVpcFlowLogsConfigsResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.networkmanagement.v1.ListVpcFlowLogsConfigsResponse;

Decodes a ListVpcFlowLogsConfigsResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListVpcFlowLogsConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.listvpcflowlogsconfigsresponse)` | ListVpcFlowLogsConfigsResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.networkmanagement.v1.IListVpcFlowLogsConfigsResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListVpcFlowLogsConfigsResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListVpcFlowLogsConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.ilistvpcflowlogsconfigsresponse)`   
ListVpcFlowLogsConfigsResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.networkmanagement.v1.IListVpcFlowLogsConfigsResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListVpcFlowLogsConfigsResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListVpcFlowLogsConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.ilistvpcflowlogsconfigsresponse)`   
ListVpcFlowLogsConfigsResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.networkmanagement.v1.ListVpcFlowLogsConfigsResponse;

Creates a ListVpcFlowLogsConfigsResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListVpcFlowLogsConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.listvpcflowlogsconfigsresponse)` | ListVpcFlowLogsConfigsResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListVpcFlowLogsConfigsResponse

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

Converts this ListVpcFlowLogsConfigsResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.networkmanagement.v1.ListVpcFlowLogsConfigsResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListVpcFlowLogsConfigsResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListVpcFlowLogsConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.listvpcflowlogsconfigsresponse)`   
ListVpcFlowLogsConfigsResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListVpcFlowLogsConfigsResponse message.

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
