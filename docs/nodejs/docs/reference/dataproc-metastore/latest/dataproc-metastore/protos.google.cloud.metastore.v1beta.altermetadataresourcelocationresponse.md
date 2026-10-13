---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.altermetadataresourcelocationresponse
title: Class protos.google.cloud.metastore.v1beta.AlterMetadataResourceLocationResponse (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:27.659897+00:00
---

# Class protos.google.cloud.metastore.v1beta.AlterMetadataResourceLocationResponse (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.altermetadataresourcelocationresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.metastore.v1beta.AlterMetadataResourceLocationResponse (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.1.0  4.1.0  3.5.0  3.4.1  3.1.2  2.2.0  2.1.0  2.0.0  1.3.0  1.2.0  1.1.6 

Represents an AlterMetadataResourceLocationResponse.

## Implements

[protos.google.cloud.metastore.v1beta.IAlterMetadataResourceLocationResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.ialtermetadataresourcelocationresponse)

## Package

[@google-cloud/dataproc-metastore](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.metastore.v1beta.IAlterMetadataResourceLocationResponse);

Constructs a new AlterMetadataResourceLocationResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAlterMetadataResourceLocationResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.ialtermetadataresourcelocationresponse)`   
Properties to set  
  
## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.metastore.v1beta.IAlterMetadataResourceLocationResponse): google.cloud.metastore.v1beta.AlterMetadataResourceLocationResponse;

Creates a new AlterMetadataResourceLocationResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAlterMetadataResourceLocationResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.ialtermetadataresourcelocationresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AlterMetadataResourceLocationResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.altermetadataresourcelocationresponse)` | AlterMetadataResourceLocationResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.metastore.v1beta.AlterMetadataResourceLocationResponse;

Decodes an AlterMetadataResourceLocationResponse message from the specified reader or buffer.

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
`[AlterMetadataResourceLocationResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.altermetadataresourcelocationresponse)` | AlterMetadataResourceLocationResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.metastore.v1beta.AlterMetadataResourceLocationResponse;

Decodes an AlterMetadataResourceLocationResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AlterMetadataResourceLocationResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.altermetadataresourcelocationresponse)` | AlterMetadataResourceLocationResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.metastore.v1beta.IAlterMetadataResourceLocationResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AlterMetadataResourceLocationResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAlterMetadataResourceLocationResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.ialtermetadataresourcelocationresponse)`   
AlterMetadataResourceLocationResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.metastore.v1beta.IAlterMetadataResourceLocationResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AlterMetadataResourceLocationResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAlterMetadataResourceLocationResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.ialtermetadataresourcelocationresponse)`   
AlterMetadataResourceLocationResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.metastore.v1beta.AlterMetadataResourceLocationResponse;

Creates an AlterMetadataResourceLocationResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AlterMetadataResourceLocationResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.altermetadataresourcelocationresponse)` | AlterMetadataResourceLocationResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AlterMetadataResourceLocationResponse

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

Converts this AlterMetadataResourceLocationResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.metastore.v1beta.AlterMetadataResourceLocationResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AlterMetadataResourceLocationResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AlterMetadataResourceLocationResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataproc-metastore/latest/dataproc-metastore/protos.google.cloud.metastore.v1beta.altermetadataresourcelocationresponse)`   
AlterMetadataResourceLocationResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AlterMetadataResourceLocationResponse message.

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
