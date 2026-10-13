---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.appendrowsresponse-class
title: Class protos.google.cloud.bigquery.storage.v1.AppendRowsResponse (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:35.916323+00:00
---

# Class protos.google.cloud.bigquery.storage.v1.AppendRowsResponse (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.appendrowsresponse-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.bigquery.storage.v1.AppendRowsResponse (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an AppendRowsResponse.

## Implements

[protos.google.cloud.bigquery.storage.v1.IAppendRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.iappendrowsresponse)

## Package

[@google-cloud/bigquery-storage-api](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.bigquery.storage.v1.IAppendRowsResponse);

Constructs a new AppendRowsResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAppendRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.iappendrowsresponse)`   
Properties to set  
  
## Properties 

### appendResult
    
    
    public appendResult?: (google.cloud.bigquery.storage.v1.AppendRowsResponse.IAppendResult|null);

AppendRowsResponse appendResult.

### error
    
    
    public error?: (google.rpc.IStatus|null);

AppendRowsResponse error.

### response
    
    
    public response?: ("appendResult"|"error");

AppendRowsResponse response.

### rowErrors
    
    
    public rowErrors: google.cloud.bigquery.storage.v1.IRowError[];

AppendRowsResponse rowErrors.

### updatedSchema
    
    
    public updatedSchema?: (google.cloud.bigquery.storage.v1.ITableSchema|null);

AppendRowsResponse updatedSchema.

### writeStream
    
    
    public writeStream: string;

AppendRowsResponse writeStream.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.bigquery.storage.v1.IAppendRowsResponse): google.cloud.bigquery.storage.v1.AppendRowsResponse;

Creates a new AppendRowsResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAppendRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.iappendrowsresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.appendrowsresponse-class)` | AppendRowsResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.bigquery.storage.v1.AppendRowsResponse;

Decodes an AppendRowsResponse message from the specified reader or buffer.

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
`[AppendRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.appendrowsresponse-class)` | AppendRowsResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.bigquery.storage.v1.AppendRowsResponse;

Decodes an AppendRowsResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.appendrowsresponse-class)` | AppendRowsResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.bigquery.storage.v1.IAppendRowsResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AppendRowsResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAppendRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.iappendrowsresponse)`   
AppendRowsResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.bigquery.storage.v1.IAppendRowsResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AppendRowsResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAppendRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.iappendrowsresponse)`   
AppendRowsResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.bigquery.storage.v1.AppendRowsResponse;

Creates an AppendRowsResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.appendrowsresponse-class)` | AppendRowsResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AppendRowsResponse

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

Converts this AppendRowsResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.bigquery.storage.v1.AppendRowsResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AppendRowsResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AppendRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.appendrowsresponse-class)`   
AppendRowsResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AppendRowsResponse message.

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

Last updated 2026-08-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-01 UTC."],[],[]] 
