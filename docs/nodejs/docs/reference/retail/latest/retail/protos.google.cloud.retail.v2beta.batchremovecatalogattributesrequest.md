---
url: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.batchremovecatalogattributesrequest
title: Class protos.google.cloud.retail.v2beta.BatchRemoveCatalogAttributesRequest (5.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:20.473715+00:00
---

# Class protos.google.cloud.retail.v2beta.BatchRemoveCatalogAttributesRequest (5.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.batchremovecatalogattributesrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.retail.v2beta.BatchRemoveCatalogAttributesRequest (5.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.4.0 (latest)  5.3.1  5.0.1  4.4.0  4.3.0  3.6.0  3.5.0  3.1.0  2.4.1  2.3.1  2.1.1  2.0.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.2  1.1.6 

Represents a BatchRemoveCatalogAttributesRequest.

## Implements

[protos.google.cloud.retail.v2beta.IBatchRemoveCatalogAttributesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ibatchremovecatalogattributesrequest)

## Package

[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.retail.v2beta.IBatchRemoveCatalogAttributesRequest);

Constructs a new BatchRemoveCatalogAttributesRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBatchRemoveCatalogAttributesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ibatchremovecatalogattributesrequest)`   
Properties to set  
  
## Properties 

### attributeKeys
    
    
    public attributeKeys: string[];

BatchRemoveCatalogAttributesRequest attributeKeys.

### attributesConfig
    
    
    public attributesConfig: string;

BatchRemoveCatalogAttributesRequest attributesConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.retail.v2beta.IBatchRemoveCatalogAttributesRequest): google.cloud.retail.v2beta.BatchRemoveCatalogAttributesRequest;

Creates a new BatchRemoveCatalogAttributesRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBatchRemoveCatalogAttributesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ibatchremovecatalogattributesrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[BatchRemoveCatalogAttributesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.batchremovecatalogattributesrequest)` | BatchRemoveCatalogAttributesRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.retail.v2beta.BatchRemoveCatalogAttributesRequest;

Decodes a BatchRemoveCatalogAttributesRequest message from the specified reader or buffer.

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
`[BatchRemoveCatalogAttributesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.batchremovecatalogattributesrequest)` | BatchRemoveCatalogAttributesRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.retail.v2beta.BatchRemoveCatalogAttributesRequest;

Decodes a BatchRemoveCatalogAttributesRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[BatchRemoveCatalogAttributesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.batchremovecatalogattributesrequest)` | BatchRemoveCatalogAttributesRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.retail.v2beta.IBatchRemoveCatalogAttributesRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BatchRemoveCatalogAttributesRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBatchRemoveCatalogAttributesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ibatchremovecatalogattributesrequest)`   
BatchRemoveCatalogAttributesRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.retail.v2beta.IBatchRemoveCatalogAttributesRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BatchRemoveCatalogAttributesRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBatchRemoveCatalogAttributesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ibatchremovecatalogattributesrequest)`   
BatchRemoveCatalogAttributesRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.retail.v2beta.BatchRemoveCatalogAttributesRequest;

Creates a BatchRemoveCatalogAttributesRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[BatchRemoveCatalogAttributesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.batchremovecatalogattributesrequest)` | BatchRemoveCatalogAttributesRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for BatchRemoveCatalogAttributesRequest

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

Converts this BatchRemoveCatalogAttributesRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.retail.v2beta.BatchRemoveCatalogAttributesRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a BatchRemoveCatalogAttributesRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[BatchRemoveCatalogAttributesRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.batchremovecatalogattributesrequest)`   
BatchRemoveCatalogAttributesRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a BatchRemoveCatalogAttributesRequest message.

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
