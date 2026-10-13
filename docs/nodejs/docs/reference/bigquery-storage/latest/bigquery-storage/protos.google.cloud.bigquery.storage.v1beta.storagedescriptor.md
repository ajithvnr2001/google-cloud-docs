---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1beta.storagedescriptor
title: Class protos.google.cloud.bigquery.storage.v1beta.StorageDescriptor (5.1.2) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:48.853578+00:00
---

# Class protos.google.cloud.bigquery.storage.v1beta.StorageDescriptor (5.1.2)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1beta.storagedescriptor

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.bigquery.storage.v1beta.StorageDescriptor (5.1.2) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.2 (latest)  5.1.1  4.10.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.1  4.1.0  4.0.0  3.4.0  3.2.0  3.1.1  2.8.0  2.7.0  2.6.2  2.5.4  2.3.0 

Represents a StorageDescriptor.

## Package

[@google-cloud/bigquery-storage](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.bigquery.storage.v1beta.IStorageDescriptor);

Constructs a new StorageDescriptor.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IStorageDescriptor](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1beta.istoragedescriptor)`   
Properties to set  
  
## Properties 

### inputFormat
    
    
    public inputFormat: string;

StorageDescriptor inputFormat.

### locationUri
    
    
    public locationUri: string;

StorageDescriptor locationUri.

### outputFormat
    
    
    public outputFormat: string;

StorageDescriptor outputFormat.

### serdeInfo
    
    
    public serdeInfo?: (google.cloud.bigquery.storage.v1beta.ISerDeInfo|null);

StorageDescriptor serdeInfo.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.bigquery.storage.v1beta.IStorageDescriptor): google.cloud.bigquery.storage.v1beta.StorageDescriptor;

Creates a new StorageDescriptor instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IStorageDescriptor](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1beta.istoragedescriptor)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[StorageDescriptor](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1beta.storagedescriptor)` | StorageDescriptor instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.bigquery.storage.v1beta.StorageDescriptor;

Decodes a StorageDescriptor message from the specified reader or buffer.

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
`[StorageDescriptor](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1beta.storagedescriptor)` | StorageDescriptor  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.bigquery.storage.v1beta.StorageDescriptor;

Decodes a StorageDescriptor message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[StorageDescriptor](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1beta.storagedescriptor)` | StorageDescriptor  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.bigquery.storage.v1beta.IStorageDescriptor, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified StorageDescriptor message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IStorageDescriptor](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1beta.istoragedescriptor)`   
StorageDescriptor message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.bigquery.storage.v1beta.IStorageDescriptor, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified StorageDescriptor message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IStorageDescriptor](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1beta.istoragedescriptor)`   
StorageDescriptor message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.bigquery.storage.v1beta.StorageDescriptor;

Creates a StorageDescriptor message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[StorageDescriptor](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1beta.storagedescriptor)` | StorageDescriptor  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for StorageDescriptor

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

Converts this StorageDescriptor to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.bigquery.storage.v1beta.StorageDescriptor, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a StorageDescriptor message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[StorageDescriptor](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage/latest/bigquery-storage/protos.google.cloud.bigquery.storage.v1beta.storagedescriptor)`   
StorageDescriptor  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a StorageDescriptor message.

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

Last updated 2026-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-16 UTC."],[],[]] 
