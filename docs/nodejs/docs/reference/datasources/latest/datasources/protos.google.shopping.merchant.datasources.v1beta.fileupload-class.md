---
url: https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.fileupload-class
title: Class protos.google.shopping.merchant.datasources.v1beta.FileUpload (0.12.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:16:28.910099+00:00
---

# Class protos.google.shopping.merchant.datasources.v1beta.FileUpload (0.12.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.fileupload-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.datasources.v1beta.FileUpload (0.12.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.1 (latest)  0.11.0  0.3.0  0.2.0  0.1.0 

Represents a FileUpload.

## Implements

[protos.google.shopping.merchant.datasources.v1beta.IFileUpload](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.ifileupload)

## Package

[@google-shopping/datasources](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.shopping.merchant.datasources.v1beta.IFileUpload);

Constructs a new FileUpload.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFileUpload](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.ifileupload)`   
Properties to set  
  
## Properties 

### dataSourceId
    
    
    public dataSourceId: (number|Long|string);

FileUpload dataSourceId.

### issues
    
    
    public issues: google.shopping.merchant.datasources.v1beta.FileUpload.IIssue[];

FileUpload issues.

### itemsCreated
    
    
    public itemsCreated: (number|Long|string);

FileUpload itemsCreated.

### itemsTotal
    
    
    public itemsTotal: (number|Long|string);

FileUpload itemsTotal.

### itemsUpdated
    
    
    public itemsUpdated: (number|Long|string);

FileUpload itemsUpdated.

### name
    
    
    public name: string;

FileUpload name.

### processingState
    
    
    public processingState: (google.shopping.merchant.datasources.v1beta.FileUpload.ProcessingState|keyof typeof google.shopping.merchant.datasources.v1beta.FileUpload.ProcessingState);

FileUpload processingState.

### uploadTime
    
    
    public uploadTime?: (google.protobuf.ITimestamp|null);

FileUpload uploadTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.shopping.merchant.datasources.v1beta.IFileUpload): google.shopping.merchant.datasources.v1beta.FileUpload;

Creates a new FileUpload instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFileUpload](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.ifileupload)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FileUpload](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.fileupload-class)` | FileUpload instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.shopping.merchant.datasources.v1beta.FileUpload;

Decodes a FileUpload message from the specified reader or buffer.

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
`[FileUpload](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.fileupload-class)` | FileUpload  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.shopping.merchant.datasources.v1beta.FileUpload;

Decodes a FileUpload message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FileUpload](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.fileupload-class)` | FileUpload  
  
### encode(message, writer)
    
    
    public static encode(message: google.shopping.merchant.datasources.v1beta.IFileUpload, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FileUpload message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFileUpload](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.ifileupload)`   
FileUpload message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.shopping.merchant.datasources.v1beta.IFileUpload, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FileUpload message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFileUpload](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.ifileupload)`   
FileUpload message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.shopping.merchant.datasources.v1beta.FileUpload;

Creates a FileUpload message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FileUpload](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.fileupload-class)` | FileUpload  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FileUpload

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

Converts this FileUpload to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.shopping.merchant.datasources.v1beta.FileUpload, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FileUpload message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FileUpload](https://docs.cloud.google.com/nodejs/docs/reference/datasources/latest/datasources/protos.google.shopping.merchant.datasources.v1beta.fileupload-class)`   
FileUpload  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FileUpload message.

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
