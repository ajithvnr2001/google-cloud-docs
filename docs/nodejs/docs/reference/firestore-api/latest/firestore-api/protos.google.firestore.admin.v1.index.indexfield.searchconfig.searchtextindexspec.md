---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.index.indexfield.searchconfig.searchtextindexspec
title: Class protos.google.firestore.admin.v1.Index.IndexField.SearchConfig.SearchTextIndexSpec (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:44:33.629203+00:00
---

# Class protos.google.firestore.admin.v1.Index.IndexField.SearchConfig.SearchTextIndexSpec (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.index.indexfield.searchconfig.searchtextindexspec

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.firestore.admin.v1.Index.IndexField.SearchConfig.SearchTextIndexSpec (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a SearchTextIndexSpec.

## Implements

[protos.google.firestore.admin.v1.Index.IndexField.SearchConfig.ISearchTextIndexSpec](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.index.indexfield.searchconfig.isearchtextindexspec)

## Package

[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.firestore.admin.v1.Index.IndexField.SearchConfig.ISearchTextIndexSpec);

Constructs a new SearchTextIndexSpec.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISearchTextIndexSpec](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.index.indexfield.searchconfig.isearchtextindexspec)`   
Properties to set  
  
## Properties 

### indexType
    
    
    public indexType: (google.firestore.admin.v1.Index.IndexField.SearchConfig.TextIndexType|keyof typeof google.firestore.admin.v1.Index.IndexField.SearchConfig.TextIndexType);

SearchTextIndexSpec indexType.

### matchType
    
    
    public matchType: (google.firestore.admin.v1.Index.IndexField.SearchConfig.TextMatchType|keyof typeof google.firestore.admin.v1.Index.IndexField.SearchConfig.TextMatchType);

SearchTextIndexSpec matchType.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.firestore.admin.v1.Index.IndexField.SearchConfig.ISearchTextIndexSpec): google.firestore.admin.v1.Index.IndexField.SearchConfig.SearchTextIndexSpec;

Creates a new SearchTextIndexSpec instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISearchTextIndexSpec](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.index.indexfield.searchconfig.isearchtextindexspec)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SearchTextIndexSpec](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.index.indexfield.searchconfig.searchtextindexspec)` | SearchTextIndexSpec instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.firestore.admin.v1.Index.IndexField.SearchConfig.SearchTextIndexSpec;

Decodes a SearchTextIndexSpec message from the specified reader or buffer.

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
`[SearchTextIndexSpec](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.index.indexfield.searchconfig.searchtextindexspec)` | SearchTextIndexSpec  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.firestore.admin.v1.Index.IndexField.SearchConfig.SearchTextIndexSpec;

Decodes a SearchTextIndexSpec message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SearchTextIndexSpec](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.index.indexfield.searchconfig.searchtextindexspec)` | SearchTextIndexSpec  
  
### encode(message, writer)
    
    
    public static encode(message: google.firestore.admin.v1.Index.IndexField.SearchConfig.ISearchTextIndexSpec, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SearchTextIndexSpec message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISearchTextIndexSpec](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.index.indexfield.searchconfig.isearchtextindexspec)`   
SearchTextIndexSpec message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.firestore.admin.v1.Index.IndexField.SearchConfig.ISearchTextIndexSpec, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SearchTextIndexSpec message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISearchTextIndexSpec](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.index.indexfield.searchconfig.isearchtextindexspec)`   
SearchTextIndexSpec message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.firestore.admin.v1.Index.IndexField.SearchConfig.SearchTextIndexSpec;

Creates a SearchTextIndexSpec message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SearchTextIndexSpec](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.index.indexfield.searchconfig.searchtextindexspec)` | SearchTextIndexSpec  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SearchTextIndexSpec

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

Converts this SearchTextIndexSpec to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.firestore.admin.v1.Index.IndexField.SearchConfig.SearchTextIndexSpec, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SearchTextIndexSpec message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SearchTextIndexSpec](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.admin.v1.index.indexfield.searchconfig.searchtextindexspec)`   
SearchTextIndexSpec  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SearchTextIndexSpec message.

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

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
