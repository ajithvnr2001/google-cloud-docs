---
url: https://docs.cloud.google.com/nodejs/docs/reference/workstations/latest/workstations/protos.google.cloud.workstations.v1beta.listworkstationconfigsresponse
title: Class protos.google.cloud.workstations.v1beta.ListWorkstationConfigsResponse (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:50.109455+00:00
---

# Class protos.google.cloud.workstations.v1beta.ListWorkstationConfigsResponse (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/workstations/latest/workstations/protos.google.cloud.workstations.v1beta.listworkstationconfigsresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.workstations.v1beta.ListWorkstationConfigsResponse (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.3.0  2.1.0  1.1.1  0.1.1 

Represents a ListWorkstationConfigsResponse.

## Implements

[protos.google.cloud.workstations.v1beta.IListWorkstationConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/workstations/latest/workstations/protos.google.cloud.workstations.v1beta.ilistworkstationconfigsresponse)

## Package

[@google-cloud/workstations](https://docs.cloud.google.com/nodejs/docs/reference/workstations/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.workstations.v1beta.IListWorkstationConfigsResponse);

Constructs a new ListWorkstationConfigsResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListWorkstationConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/workstations/latest/workstations/protos.google.cloud.workstations.v1beta.ilistworkstationconfigsresponse)`   
Properties to set  
  
## Properties 

### nextPageToken
    
    
    public nextPageToken: string;

ListWorkstationConfigsResponse nextPageToken.

### unreachable
    
    
    public unreachable: string[];

ListWorkstationConfigsResponse unreachable.

### workstationConfigs
    
    
    public workstationConfigs: google.cloud.workstations.v1beta.IWorkstationConfig[];

ListWorkstationConfigsResponse workstationConfigs.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.workstations.v1beta.IListWorkstationConfigsResponse): google.cloud.workstations.v1beta.ListWorkstationConfigsResponse;

Creates a new ListWorkstationConfigsResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListWorkstationConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/workstations/latest/workstations/protos.google.cloud.workstations.v1beta.ilistworkstationconfigsresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListWorkstationConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/workstations/latest/workstations/protos.google.cloud.workstations.v1beta.listworkstationconfigsresponse)` | ListWorkstationConfigsResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.workstations.v1beta.ListWorkstationConfigsResponse;

Decodes a ListWorkstationConfigsResponse message from the specified reader or buffer.

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
`[ListWorkstationConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/workstations/latest/workstations/protos.google.cloud.workstations.v1beta.listworkstationconfigsresponse)` | ListWorkstationConfigsResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.workstations.v1beta.ListWorkstationConfigsResponse;

Decodes a ListWorkstationConfigsResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListWorkstationConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/workstations/latest/workstations/protos.google.cloud.workstations.v1beta.listworkstationconfigsresponse)` | ListWorkstationConfigsResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.workstations.v1beta.IListWorkstationConfigsResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListWorkstationConfigsResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListWorkstationConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/workstations/latest/workstations/protos.google.cloud.workstations.v1beta.ilistworkstationconfigsresponse)`   
ListWorkstationConfigsResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.workstations.v1beta.IListWorkstationConfigsResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListWorkstationConfigsResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListWorkstationConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/workstations/latest/workstations/protos.google.cloud.workstations.v1beta.ilistworkstationconfigsresponse)`   
ListWorkstationConfigsResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.workstations.v1beta.ListWorkstationConfigsResponse;

Creates a ListWorkstationConfigsResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListWorkstationConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/workstations/latest/workstations/protos.google.cloud.workstations.v1beta.listworkstationconfigsresponse)` | ListWorkstationConfigsResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListWorkstationConfigsResponse

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

Converts this ListWorkstationConfigsResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.workstations.v1beta.ListWorkstationConfigsResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListWorkstationConfigsResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListWorkstationConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/workstations/latest/workstations/protos.google.cloud.workstations.v1beta.listworkstationconfigsresponse)`   
ListWorkstationConfigsResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListWorkstationConfigsResponse message.

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
