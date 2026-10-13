---
url: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.listsingletenanthsminstancesresponse
title: Class protos.google.cloud.kms.v1.ListSingleTenantHsmInstancesResponse (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:08:58.314675+00:00
---

# Class protos.google.cloud.kms.v1.ListSingleTenantHsmInstancesResponse (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.listsingletenanthsminstancesresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.kms.v1.ListSingleTenantHsmInstancesResponse (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.7.0  5.6.0  5.3.0  4.5.0  4.3.0  3.5.1  3.4.0  3.3.1  3.1.0  2.11.0  2.10.0  2.9.0  2.8.1  2.7.0  2.6.0  2.5.0  2.4.4  2.3.3 

Represents a ListSingleTenantHsmInstancesResponse.

## Implements

[protos.google.cloud.kms.v1.IListSingleTenantHsmInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistsingletenanthsminstancesresponse)

## Package

[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.kms.v1.IListSingleTenantHsmInstancesResponse);

Constructs a new ListSingleTenantHsmInstancesResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListSingleTenantHsmInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistsingletenanthsminstancesresponse)`   
Properties to set  
  
## Properties 

### nextPageToken
    
    
    public nextPageToken: string;

ListSingleTenantHsmInstancesResponse nextPageToken.

### singleTenantHsmInstances
    
    
    public singleTenantHsmInstances: google.cloud.kms.v1.ISingleTenantHsmInstance[];

ListSingleTenantHsmInstancesResponse singleTenantHsmInstances.

### totalSize
    
    
    public totalSize: number;

ListSingleTenantHsmInstancesResponse totalSize.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.kms.v1.IListSingleTenantHsmInstancesResponse): google.cloud.kms.v1.ListSingleTenantHsmInstancesResponse;

Creates a new ListSingleTenantHsmInstancesResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListSingleTenantHsmInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistsingletenanthsminstancesresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListSingleTenantHsmInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.listsingletenanthsminstancesresponse)` | ListSingleTenantHsmInstancesResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.kms.v1.ListSingleTenantHsmInstancesResponse;

Decodes a ListSingleTenantHsmInstancesResponse message from the specified reader or buffer.

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
`[ListSingleTenantHsmInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.listsingletenanthsminstancesresponse)` | ListSingleTenantHsmInstancesResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.kms.v1.ListSingleTenantHsmInstancesResponse;

Decodes a ListSingleTenantHsmInstancesResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListSingleTenantHsmInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.listsingletenanthsminstancesresponse)` | ListSingleTenantHsmInstancesResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.kms.v1.IListSingleTenantHsmInstancesResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListSingleTenantHsmInstancesResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListSingleTenantHsmInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistsingletenanthsminstancesresponse)`   
ListSingleTenantHsmInstancesResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.kms.v1.IListSingleTenantHsmInstancesResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListSingleTenantHsmInstancesResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListSingleTenantHsmInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistsingletenanthsminstancesresponse)`   
ListSingleTenantHsmInstancesResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.kms.v1.ListSingleTenantHsmInstancesResponse;

Creates a ListSingleTenantHsmInstancesResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListSingleTenantHsmInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.listsingletenanthsminstancesresponse)` | ListSingleTenantHsmInstancesResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListSingleTenantHsmInstancesResponse

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

Converts this ListSingleTenantHsmInstancesResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.kms.v1.ListSingleTenantHsmInstancesResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListSingleTenantHsmInstancesResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListSingleTenantHsmInstancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.listsingletenanthsminstancesresponse)`   
ListSingleTenantHsmInstancesResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListSingleTenantHsmInstancesResponse message.

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
