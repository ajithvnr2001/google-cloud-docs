---
url: https://docs.cloud.google.com/nodejs/docs/reference/filestore/latest/filestore/protos.google.cloud.filestore.v1beta1.share-class
title: Class protos.google.cloud.filestore.v1beta1.Share (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:10.605195+00:00
---

# Class protos.google.cloud.filestore.v1beta1.Share (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/filestore/latest/filestore/protos.google.cloud.filestore.v1beta1.share-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.filestore.v1beta1.Share (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  4.0.1  3.3.0  2.4.1  2.3.1  2.2.0  2.1.0  1.1.2  1.0.1 

Represents a Share.

## Implements

[protos.google.cloud.filestore.v1beta1.IShare](https://docs.cloud.google.com/nodejs/docs/reference/filestore/latest/filestore/protos.google.cloud.filestore.v1beta1.ishare)

## Package

[@google-cloud/filestore](https://docs.cloud.google.com/nodejs/docs/reference/filestore/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.filestore.v1beta1.IShare);

Constructs a new Share.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IShare](https://docs.cloud.google.com/nodejs/docs/reference/filestore/latest/filestore/protos.google.cloud.filestore.v1beta1.ishare)`   
Properties to set  
  
## Properties 

### backup
    
    
    public backup?: (string|null);

Share backup.

### capacityGb
    
    
    public capacityGb: (number|Long|string);

Share capacityGb.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Share createTime.

### description
    
    
    public description: string;

Share description.

### labels
    
    
    public labels: { [k: string]: string };

Share labels.

### mountName
    
    
    public mountName: string;

Share mountName.

### name
    
    
    public name: string;

Share name.

### nfsExportOptions
    
    
    public nfsExportOptions: google.cloud.filestore.v1beta1.INfsExportOptions[];

Share nfsExportOptions.

### source
    
    
    public source?: "backup";

Share source.

### state
    
    
    public state: (google.cloud.filestore.v1beta1.Share.State|keyof typeof google.cloud.filestore.v1beta1.Share.State);

Share state.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.filestore.v1beta1.IShare): google.cloud.filestore.v1beta1.Share;

Creates a new Share instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IShare](https://docs.cloud.google.com/nodejs/docs/reference/filestore/latest/filestore/protos.google.cloud.filestore.v1beta1.ishare)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Share](https://docs.cloud.google.com/nodejs/docs/reference/filestore/latest/filestore/protos.google.cloud.filestore.v1beta1.share-class)` | Share instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.filestore.v1beta1.Share;

Decodes a Share message from the specified reader or buffer.

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
`[Share](https://docs.cloud.google.com/nodejs/docs/reference/filestore/latest/filestore/protos.google.cloud.filestore.v1beta1.share-class)` | Share  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.filestore.v1beta1.Share;

Decodes a Share message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Share](https://docs.cloud.google.com/nodejs/docs/reference/filestore/latest/filestore/protos.google.cloud.filestore.v1beta1.share-class)` | Share  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.filestore.v1beta1.IShare, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Share message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IShare](https://docs.cloud.google.com/nodejs/docs/reference/filestore/latest/filestore/protos.google.cloud.filestore.v1beta1.ishare)`   
Share message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.filestore.v1beta1.IShare, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Share message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IShare](https://docs.cloud.google.com/nodejs/docs/reference/filestore/latest/filestore/protos.google.cloud.filestore.v1beta1.ishare)`   
Share message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.filestore.v1beta1.Share;

Creates a Share message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Share](https://docs.cloud.google.com/nodejs/docs/reference/filestore/latest/filestore/protos.google.cloud.filestore.v1beta1.share-class)` | Share  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Share

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

Converts this Share to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.filestore.v1beta1.Share, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Share message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Share](https://docs.cloud.google.com/nodejs/docs/reference/filestore/latest/filestore/protos.google.cloud.filestore.v1beta1.share-class)`   
Share  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Share message.

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
