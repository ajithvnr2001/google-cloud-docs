---
url: https://docs.cloud.google.com/nodejs/docs/reference/clientgateways/latest/clientgateways/protos.google.cloud.beyondcorp.clientgateways.v1.listclientgatewaysresponse
title: Class protos.google.cloud.beyondcorp.clientgateways.v1.ListClientGatewaysResponse (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:10.203195+00:00
---

# Class protos.google.cloud.beyondcorp.clientgateways.v1.ListClientGatewaysResponse (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/clientgateways/latest/clientgateways/protos.google.cloud.beyondcorp.clientgateways.v1.listclientgatewaysresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.beyondcorp.clientgateways.v1.ListClientGatewaysResponse (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  0.3.2  0.2.3 

Represents a ListClientGatewaysResponse.

## Implements

[protos.google.cloud.beyondcorp.clientgateways.v1.IListClientGatewaysResponse](https://docs.cloud.google.com/nodejs/docs/reference/clientgateways/latest/clientgateways/protos.google.cloud.beyondcorp.clientgateways.v1.ilistclientgatewaysresponse)

## Package

[@google-cloud/clientgateways](https://docs.cloud.google.com/nodejs/docs/reference/clientgateways/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.beyondcorp.clientgateways.v1.IListClientGatewaysResponse);

Constructs a new ListClientGatewaysResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListClientGatewaysResponse](https://docs.cloud.google.com/nodejs/docs/reference/clientgateways/latest/clientgateways/protos.google.cloud.beyondcorp.clientgateways.v1.ilistclientgatewaysresponse)`   
Properties to set  
  
## Properties 

### clientGateways
    
    
    public clientGateways: google.cloud.beyondcorp.clientgateways.v1.IClientGateway[];

ListClientGatewaysResponse clientGateways.

### nextPageToken
    
    
    public nextPageToken: string;

ListClientGatewaysResponse nextPageToken.

### unreachable
    
    
    public unreachable: string[];

ListClientGatewaysResponse unreachable.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.beyondcorp.clientgateways.v1.IListClientGatewaysResponse): google.cloud.beyondcorp.clientgateways.v1.ListClientGatewaysResponse;

Creates a new ListClientGatewaysResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListClientGatewaysResponse](https://docs.cloud.google.com/nodejs/docs/reference/clientgateways/latest/clientgateways/protos.google.cloud.beyondcorp.clientgateways.v1.ilistclientgatewaysresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListClientGatewaysResponse](https://docs.cloud.google.com/nodejs/docs/reference/clientgateways/latest/clientgateways/protos.google.cloud.beyondcorp.clientgateways.v1.listclientgatewaysresponse)` | ListClientGatewaysResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.beyondcorp.clientgateways.v1.ListClientGatewaysResponse;

Decodes a ListClientGatewaysResponse message from the specified reader or buffer.

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
`[ListClientGatewaysResponse](https://docs.cloud.google.com/nodejs/docs/reference/clientgateways/latest/clientgateways/protos.google.cloud.beyondcorp.clientgateways.v1.listclientgatewaysresponse)` | ListClientGatewaysResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.beyondcorp.clientgateways.v1.ListClientGatewaysResponse;

Decodes a ListClientGatewaysResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListClientGatewaysResponse](https://docs.cloud.google.com/nodejs/docs/reference/clientgateways/latest/clientgateways/protos.google.cloud.beyondcorp.clientgateways.v1.listclientgatewaysresponse)` | ListClientGatewaysResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.beyondcorp.clientgateways.v1.IListClientGatewaysResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListClientGatewaysResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListClientGatewaysResponse](https://docs.cloud.google.com/nodejs/docs/reference/clientgateways/latest/clientgateways/protos.google.cloud.beyondcorp.clientgateways.v1.ilistclientgatewaysresponse)`   
ListClientGatewaysResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.beyondcorp.clientgateways.v1.IListClientGatewaysResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListClientGatewaysResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListClientGatewaysResponse](https://docs.cloud.google.com/nodejs/docs/reference/clientgateways/latest/clientgateways/protos.google.cloud.beyondcorp.clientgateways.v1.ilistclientgatewaysresponse)`   
ListClientGatewaysResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.beyondcorp.clientgateways.v1.ListClientGatewaysResponse;

Creates a ListClientGatewaysResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListClientGatewaysResponse](https://docs.cloud.google.com/nodejs/docs/reference/clientgateways/latest/clientgateways/protos.google.cloud.beyondcorp.clientgateways.v1.listclientgatewaysresponse)` | ListClientGatewaysResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListClientGatewaysResponse

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

Converts this ListClientGatewaysResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.beyondcorp.clientgateways.v1.ListClientGatewaysResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListClientGatewaysResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListClientGatewaysResponse](https://docs.cloud.google.com/nodejs/docs/reference/clientgateways/latest/clientgateways/protos.google.cloud.beyondcorp.clientgateways.v1.listclientgatewaysresponse)`   
ListClientGatewaysResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListClientGatewaysResponse message.

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
