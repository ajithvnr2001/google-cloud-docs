---
url: https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.listtasksrequest
title: Class protos.google.cloud.tasks.v2beta3.ListTasksRequest (7.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:39.087384+00:00
---

# Class protos.google.cloud.tasks.v2beta3.ListTasksRequest (7.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.listtasksrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.tasks.v2beta3.ListTasksRequest (7.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.2.1 (latest)  7.2.0  7.1.1  5.5.2  3.1.2  3.0.5  2.5.0  2.4.2  2.3.6 

Represents a ListTasksRequest.

## Implements

[protos.google.cloud.tasks.v2beta3.IListTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.ilisttasksrequest)

## Package

[@google-cloud/tasks](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.tasks.v2beta3.IListTasksRequest);

Constructs a new ListTasksRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.ilisttasksrequest)`   
Properties to set  
  
## Properties 

### pageSize
    
    
    public pageSize: number;

ListTasksRequest pageSize.

### pageToken
    
    
    public pageToken: string;

ListTasksRequest pageToken.

### parent
    
    
    public parent: string;

ListTasksRequest parent.

### responseView
    
    
    public responseView: (google.cloud.tasks.v2beta3.Task.View|keyof typeof google.cloud.tasks.v2beta3.Task.View);

ListTasksRequest responseView.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.tasks.v2beta3.IListTasksRequest): google.cloud.tasks.v2beta3.ListTasksRequest;

Creates a new ListTasksRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.ilisttasksrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.listtasksrequest)` | ListTasksRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.tasks.v2beta3.ListTasksRequest;

Decodes a ListTasksRequest message from the specified reader or buffer.

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
`[ListTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.listtasksrequest)` | ListTasksRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.tasks.v2beta3.ListTasksRequest;

Decodes a ListTasksRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.listtasksrequest)` | ListTasksRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.tasks.v2beta3.IListTasksRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListTasksRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.ilisttasksrequest)`   
ListTasksRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.tasks.v2beta3.IListTasksRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListTasksRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.ilisttasksrequest)`   
ListTasksRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.tasks.v2beta3.ListTasksRequest;

Creates a ListTasksRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.listtasksrequest)` | ListTasksRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListTasksRequest

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

Converts this ListTasksRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.tasks.v2beta3.ListTasksRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListTasksRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.listtasksrequest)`   
ListTasksRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListTasksRequest message.

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
