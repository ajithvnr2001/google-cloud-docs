---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.updateauthorizedviewrequest
title: Class protos.google.bigtable.admin.v2.UpdateAuthorizedViewRequest (0.9.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:00.604302+00:00
---

# Class protos.google.bigtable.admin.v2.UpdateAuthorizedViewRequest (0.9.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.updateauthorizedviewrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.bigtable.admin.v2.UpdateAuthorizedViewRequest (0.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.0 (latest)  0.8.0  0.2.0 

Represents an UpdateAuthorizedViewRequest.

## Implements

[protos.google.bigtable.admin.v2.IUpdateAuthorizedViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.iupdateauthorizedviewrequest)

## Package

[@google-cloud/bigtable-api](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.bigtable.admin.v2.IUpdateAuthorizedViewRequest);

Constructs a new UpdateAuthorizedViewRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateAuthorizedViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.iupdateauthorizedviewrequest)`   
Properties to set  
  
## Properties 

### authorizedView
    
    
    public authorizedView?: (google.bigtable.admin.v2.IAuthorizedView|null);

UpdateAuthorizedViewRequest authorizedView.

### ignoreWarnings
    
    
    public ignoreWarnings: boolean;

UpdateAuthorizedViewRequest ignoreWarnings.

### updateMask
    
    
    public updateMask?: (google.protobuf.IFieldMask|null);

UpdateAuthorizedViewRequest updateMask.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.bigtable.admin.v2.IUpdateAuthorizedViewRequest): google.bigtable.admin.v2.UpdateAuthorizedViewRequest;

Creates a new UpdateAuthorizedViewRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateAuthorizedViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.iupdateauthorizedviewrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[UpdateAuthorizedViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.updateauthorizedviewrequest)` | UpdateAuthorizedViewRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.bigtable.admin.v2.UpdateAuthorizedViewRequest;

Decodes an UpdateAuthorizedViewRequest message from the specified reader or buffer.

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
`[UpdateAuthorizedViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.updateauthorizedviewrequest)` | UpdateAuthorizedViewRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.bigtable.admin.v2.UpdateAuthorizedViewRequest;

Decodes an UpdateAuthorizedViewRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[UpdateAuthorizedViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.updateauthorizedviewrequest)` | UpdateAuthorizedViewRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.bigtable.admin.v2.IUpdateAuthorizedViewRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateAuthorizedViewRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateAuthorizedViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.iupdateauthorizedviewrequest)`   
UpdateAuthorizedViewRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.bigtable.admin.v2.IUpdateAuthorizedViewRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateAuthorizedViewRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateAuthorizedViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.iupdateauthorizedviewrequest)`   
UpdateAuthorizedViewRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.bigtable.admin.v2.UpdateAuthorizedViewRequest;

Creates an UpdateAuthorizedViewRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[UpdateAuthorizedViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.updateauthorizedviewrequest)` | UpdateAuthorizedViewRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for UpdateAuthorizedViewRequest

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

Converts this UpdateAuthorizedViewRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.bigtable.admin.v2.UpdateAuthorizedViewRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an UpdateAuthorizedViewRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[UpdateAuthorizedViewRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.updateauthorizedviewrequest)`   
UpdateAuthorizedViewRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an UpdateAuthorizedViewRequest message.

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
