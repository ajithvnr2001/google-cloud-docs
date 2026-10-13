---
url: https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.listgatewayrouteviewsrequest
title: Class protos.google.cloud.networkservices.v1.ListGatewayRouteViewsRequest (0.17.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:52.924728+00:00
---

# Class protos.google.cloud.networkservices.v1.ListGatewayRouteViewsRequest (0.17.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.listgatewayrouteviewsrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networkservices.v1.ListGatewayRouteViewsRequest (0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.13.0  0.12.0  0.9.0  0.8.1  0.7.0  0.2.1 

Represents a ListGatewayRouteViewsRequest.

## Implements

[protos.google.cloud.networkservices.v1.IListGatewayRouteViewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.ilistgatewayrouteviewsrequest)

## Package

[@google-cloud/networkservices](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.networkservices.v1.IListGatewayRouteViewsRequest);

Constructs a new ListGatewayRouteViewsRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListGatewayRouteViewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.ilistgatewayrouteviewsrequest)`   
Properties to set  
  
## Properties 

### pageSize
    
    
    public pageSize: number;

ListGatewayRouteViewsRequest pageSize.

### pageToken
    
    
    public pageToken: string;

ListGatewayRouteViewsRequest pageToken.

### parent
    
    
    public parent: string;

ListGatewayRouteViewsRequest parent.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.networkservices.v1.IListGatewayRouteViewsRequest): google.cloud.networkservices.v1.ListGatewayRouteViewsRequest;

Creates a new ListGatewayRouteViewsRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListGatewayRouteViewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.ilistgatewayrouteviewsrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListGatewayRouteViewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.listgatewayrouteviewsrequest)` | ListGatewayRouteViewsRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.networkservices.v1.ListGatewayRouteViewsRequest;

Decodes a ListGatewayRouteViewsRequest message from the specified reader or buffer.

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
`[ListGatewayRouteViewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.listgatewayrouteviewsrequest)` | ListGatewayRouteViewsRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.networkservices.v1.ListGatewayRouteViewsRequest;

Decodes a ListGatewayRouteViewsRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListGatewayRouteViewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.listgatewayrouteviewsrequest)` | ListGatewayRouteViewsRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.networkservices.v1.IListGatewayRouteViewsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListGatewayRouteViewsRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListGatewayRouteViewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.ilistgatewayrouteviewsrequest)`   
ListGatewayRouteViewsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.networkservices.v1.IListGatewayRouteViewsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListGatewayRouteViewsRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListGatewayRouteViewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.ilistgatewayrouteviewsrequest)`   
ListGatewayRouteViewsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.networkservices.v1.ListGatewayRouteViewsRequest;

Creates a ListGatewayRouteViewsRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListGatewayRouteViewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.listgatewayrouteviewsrequest)` | ListGatewayRouteViewsRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListGatewayRouteViewsRequest

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

Converts this ListGatewayRouteViewsRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.networkservices.v1.ListGatewayRouteViewsRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListGatewayRouteViewsRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListGatewayRouteViewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.listgatewayrouteviewsrequest)`   
ListGatewayRouteViewsRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListGatewayRouteViewsRequest message.

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
