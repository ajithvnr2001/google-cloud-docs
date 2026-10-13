---
url: https://docs.cloud.google.com/nodejs/docs/reference/maintenance-api/latest/maintenance-api/protos.google.cloud.maintenance.api.v1beta.listresourcemaintenancesresponse
title: Class protos.google.cloud.maintenance.api.v1beta.ListResourceMaintenancesResponse (0.6.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:57:13.005693+00:00
---

# Class protos.google.cloud.maintenance.api.v1beta.ListResourceMaintenancesResponse (0.6.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/maintenance-api/latest/maintenance-api/protos.google.cloud.maintenance.api.v1beta.listresourcemaintenancesresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.maintenance.api.v1beta.ListResourceMaintenancesResponse (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.4.0  0.3.0 

Represents a ListResourceMaintenancesResponse.

## Implements

[protos.google.cloud.maintenance.api.v1beta.IListResourceMaintenancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/maintenance-api/latest/maintenance-api/protos.google.cloud.maintenance.api.v1beta.ilistresourcemaintenancesresponse)

## Package

[@google-cloud/maintenance-api](https://docs.cloud.google.com/nodejs/docs/reference/maintenance-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.maintenance.api.v1beta.IListResourceMaintenancesResponse);

Constructs a new ListResourceMaintenancesResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListResourceMaintenancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/maintenance-api/latest/maintenance-api/protos.google.cloud.maintenance.api.v1beta.ilistresourcemaintenancesresponse)`   
Properties to set  
  
## Properties 

### nextPageToken
    
    
    public nextPageToken: string;

ListResourceMaintenancesResponse nextPageToken.

### resourceMaintenances
    
    
    public resourceMaintenances: google.cloud.maintenance.api.v1beta.IResourceMaintenance[];

ListResourceMaintenancesResponse resourceMaintenances.

### unreachable
    
    
    public unreachable: string[];

ListResourceMaintenancesResponse unreachable.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.maintenance.api.v1beta.IListResourceMaintenancesResponse): google.cloud.maintenance.api.v1beta.ListResourceMaintenancesResponse;

Creates a new ListResourceMaintenancesResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListResourceMaintenancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/maintenance-api/latest/maintenance-api/protos.google.cloud.maintenance.api.v1beta.ilistresourcemaintenancesresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListResourceMaintenancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/maintenance-api/latest/maintenance-api/protos.google.cloud.maintenance.api.v1beta.listresourcemaintenancesresponse)` | ListResourceMaintenancesResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.maintenance.api.v1beta.ListResourceMaintenancesResponse;

Decodes a ListResourceMaintenancesResponse message from the specified reader or buffer.

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
`[ListResourceMaintenancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/maintenance-api/latest/maintenance-api/protos.google.cloud.maintenance.api.v1beta.listresourcemaintenancesresponse)` | ListResourceMaintenancesResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.maintenance.api.v1beta.ListResourceMaintenancesResponse;

Decodes a ListResourceMaintenancesResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListResourceMaintenancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/maintenance-api/latest/maintenance-api/protos.google.cloud.maintenance.api.v1beta.listresourcemaintenancesresponse)` | ListResourceMaintenancesResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.maintenance.api.v1beta.IListResourceMaintenancesResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListResourceMaintenancesResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListResourceMaintenancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/maintenance-api/latest/maintenance-api/protos.google.cloud.maintenance.api.v1beta.ilistresourcemaintenancesresponse)`   
ListResourceMaintenancesResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.maintenance.api.v1beta.IListResourceMaintenancesResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListResourceMaintenancesResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListResourceMaintenancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/maintenance-api/latest/maintenance-api/protos.google.cloud.maintenance.api.v1beta.ilistresourcemaintenancesresponse)`   
ListResourceMaintenancesResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.maintenance.api.v1beta.ListResourceMaintenancesResponse;

Creates a ListResourceMaintenancesResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListResourceMaintenancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/maintenance-api/latest/maintenance-api/protos.google.cloud.maintenance.api.v1beta.listresourcemaintenancesresponse)` | ListResourceMaintenancesResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListResourceMaintenancesResponse

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

Converts this ListResourceMaintenancesResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.maintenance.api.v1beta.ListResourceMaintenancesResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListResourceMaintenancesResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListResourceMaintenancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/maintenance-api/latest/maintenance-api/protos.google.cloud.maintenance.api.v1beta.listresourcemaintenancesresponse)`   
ListResourceMaintenancesResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListResourceMaintenancesResponse message.

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
