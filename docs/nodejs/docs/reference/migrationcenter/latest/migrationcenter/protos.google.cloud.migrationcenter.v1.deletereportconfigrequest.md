---
url: https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.deletereportconfigrequest
title: Class protos.google.cloud.migrationcenter.v1.DeleteReportConfigRequest (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:27:50.365256+00:00
---

# Class protos.google.cloud.migrationcenter.v1.DeleteReportConfigRequest (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.deletereportconfigrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.migrationcenter.v1.DeleteReportConfigRequest (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.1.0 

Represents a DeleteReportConfigRequest.

## Implements

[protos.google.cloud.migrationcenter.v1.IDeleteReportConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.ideletereportconfigrequest)

## Package

[@google-cloud/migrationcenter](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.migrationcenter.v1.IDeleteReportConfigRequest);

Constructs a new DeleteReportConfigRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeleteReportConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.ideletereportconfigrequest)`   
Properties to set  
  
## Properties 

### force
    
    
    public force: boolean;

DeleteReportConfigRequest force.

### name
    
    
    public name: string;

DeleteReportConfigRequest name.

### requestId
    
    
    public requestId: string;

DeleteReportConfigRequest requestId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.migrationcenter.v1.IDeleteReportConfigRequest): google.cloud.migrationcenter.v1.DeleteReportConfigRequest;

Creates a new DeleteReportConfigRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeleteReportConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.ideletereportconfigrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DeleteReportConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.deletereportconfigrequest)` | DeleteReportConfigRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.migrationcenter.v1.DeleteReportConfigRequest;

Decodes a DeleteReportConfigRequest message from the specified reader or buffer.

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
`[DeleteReportConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.deletereportconfigrequest)` | DeleteReportConfigRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.migrationcenter.v1.DeleteReportConfigRequest;

Decodes a DeleteReportConfigRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DeleteReportConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.deletereportconfigrequest)` | DeleteReportConfigRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.migrationcenter.v1.IDeleteReportConfigRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeleteReportConfigRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeleteReportConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.ideletereportconfigrequest)`   
DeleteReportConfigRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.migrationcenter.v1.IDeleteReportConfigRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeleteReportConfigRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeleteReportConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.ideletereportconfigrequest)`   
DeleteReportConfigRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.migrationcenter.v1.DeleteReportConfigRequest;

Creates a DeleteReportConfigRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DeleteReportConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.deletereportconfigrequest)` | DeleteReportConfigRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DeleteReportConfigRequest

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

Converts this DeleteReportConfigRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.migrationcenter.v1.DeleteReportConfigRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DeleteReportConfigRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DeleteReportConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/migrationcenter/latest/migrationcenter/protos.google.cloud.migrationcenter.v1.deletereportconfigrequest)`   
DeleteReportConfigRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DeleteReportConfigRequest message.

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
