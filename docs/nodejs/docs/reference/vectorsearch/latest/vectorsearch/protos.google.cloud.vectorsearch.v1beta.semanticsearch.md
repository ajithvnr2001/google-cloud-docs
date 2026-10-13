---
url: https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.semanticsearch
title: Class protos.google.cloud.vectorsearch.v1beta.SemanticSearch (0.13.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:30.187713+00:00
---

# Class protos.google.cloud.vectorsearch.v1beta.SemanticSearch (0.13.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.semanticsearch

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.vectorsearch.v1beta.SemanticSearch (0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.13.0  0.8.0  0.6.0  0.5.0  0.4.0  0.2.0  0.1.0 

Represents a SemanticSearch.

## Implements

[protos.google.cloud.vectorsearch.v1beta.ISemanticSearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.isemanticsearch)

## Package

[@google-cloud/vectorsearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.vectorsearch.v1beta.ISemanticSearch);

Constructs a new SemanticSearch.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISemanticSearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.isemanticsearch)`   
Properties to set  
  
## Properties 

### filter
    
    
    public filter?: (google.protobuf.IStruct|null);

SemanticSearch filter.

### outputFields
    
    
    public outputFields?: (google.cloud.vectorsearch.v1beta.IOutputFields|null);

SemanticSearch outputFields.

### searchField
    
    
    public searchField: string;

SemanticSearch searchField.

### searchHint
    
    
    public searchHint?: (google.cloud.vectorsearch.v1beta.ISearchHint|null);

SemanticSearch searchHint.

### searchText
    
    
    public searchText: string;

SemanticSearch searchText.

### taskType
    
    
    public taskType: (google.cloud.vectorsearch.v1beta.EmbeddingTaskType|keyof typeof google.cloud.vectorsearch.v1beta.EmbeddingTaskType);

SemanticSearch taskType.

### topK
    
    
    public topK?: (number|null);

SemanticSearch topK.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.vectorsearch.v1beta.ISemanticSearch): google.cloud.vectorsearch.v1beta.SemanticSearch;

Creates a new SemanticSearch instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISemanticSearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.isemanticsearch)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SemanticSearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.semanticsearch)` | SemanticSearch instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.vectorsearch.v1beta.SemanticSearch;

Decodes a SemanticSearch message from the specified reader or buffer.

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
`[SemanticSearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.semanticsearch)` | SemanticSearch  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.vectorsearch.v1beta.SemanticSearch;

Decodes a SemanticSearch message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SemanticSearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.semanticsearch)` | SemanticSearch  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.vectorsearch.v1beta.ISemanticSearch, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SemanticSearch message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISemanticSearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.isemanticsearch)`   
SemanticSearch message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.vectorsearch.v1beta.ISemanticSearch, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SemanticSearch message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISemanticSearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.isemanticsearch)`   
SemanticSearch message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.vectorsearch.v1beta.SemanticSearch;

Creates a SemanticSearch message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SemanticSearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.semanticsearch)` | SemanticSearch  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SemanticSearch

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

Converts this SemanticSearch to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.vectorsearch.v1beta.SemanticSearch, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SemanticSearch message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SemanticSearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.semanticsearch)`   
SemanticSearch  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SemanticSearch message.

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
