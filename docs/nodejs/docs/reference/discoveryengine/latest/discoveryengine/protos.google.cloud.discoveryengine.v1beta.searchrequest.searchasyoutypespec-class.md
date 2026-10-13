---
url: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.searchrequest.searchasyoutypespec-class
title: Class protos.google.cloud.discoveryengine.v1beta.SearchRequest.SearchAsYouTypeSpec (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:02.095448+00:00
---

# Class protos.google.cloud.discoveryengine.v1beta.SearchRequest.SearchAsYouTypeSpec (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.searchrequest.searchasyoutypespec-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.discoveryengine.v1beta.SearchRequest.SearchAsYouTypeSpec (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  3.3.0  3.1.0  2.9.0  2.8.0  2.6.0  2.2.0  2.0.1  1.14.0  1.10.0  1.9.0  1.7.0  1.6.0  1.4.1  1.3.1  1.2.0  1.0.0  0.6.0  0.5.0  0.3.1  0.2.0 

Represents a SearchAsYouTypeSpec.

## Implements

[protos.google.cloud.discoveryengine.v1beta.SearchRequest.ISearchAsYouTypeSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.searchrequest.isearchasyoutypespec)

## Package

[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.discoveryengine.v1beta.SearchRequest.ISearchAsYouTypeSpec);

Constructs a new SearchAsYouTypeSpec.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISearchAsYouTypeSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.searchrequest.isearchasyoutypespec)`   
Properties to set  
  
## Properties 

### condition
    
    
    public condition: (google.cloud.discoveryengine.v1beta.SearchRequest.SearchAsYouTypeSpec.Condition|keyof typeof google.cloud.discoveryengine.v1beta.SearchRequest.SearchAsYouTypeSpec.Condition);

SearchAsYouTypeSpec condition.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.discoveryengine.v1beta.SearchRequest.ISearchAsYouTypeSpec): google.cloud.discoveryengine.v1beta.SearchRequest.SearchAsYouTypeSpec;

Creates a new SearchAsYouTypeSpec instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISearchAsYouTypeSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.searchrequest.isearchasyoutypespec)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SearchAsYouTypeSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.searchrequest.searchasyoutypespec-class)` | SearchAsYouTypeSpec instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.discoveryengine.v1beta.SearchRequest.SearchAsYouTypeSpec;

Decodes a SearchAsYouTypeSpec message from the specified reader or buffer.

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
`[SearchAsYouTypeSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.searchrequest.searchasyoutypespec-class)` | SearchAsYouTypeSpec  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.discoveryengine.v1beta.SearchRequest.SearchAsYouTypeSpec;

Decodes a SearchAsYouTypeSpec message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SearchAsYouTypeSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.searchrequest.searchasyoutypespec-class)` | SearchAsYouTypeSpec  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.discoveryengine.v1beta.SearchRequest.ISearchAsYouTypeSpec, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SearchAsYouTypeSpec message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISearchAsYouTypeSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.searchrequest.isearchasyoutypespec)`   
SearchAsYouTypeSpec message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.discoveryengine.v1beta.SearchRequest.ISearchAsYouTypeSpec, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SearchAsYouTypeSpec message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISearchAsYouTypeSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.searchrequest.isearchasyoutypespec)`   
SearchAsYouTypeSpec message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.discoveryengine.v1beta.SearchRequest.SearchAsYouTypeSpec;

Creates a SearchAsYouTypeSpec message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SearchAsYouTypeSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.searchrequest.searchasyoutypespec-class)` | SearchAsYouTypeSpec  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SearchAsYouTypeSpec

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

Converts this SearchAsYouTypeSpec to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.discoveryengine.v1beta.SearchRequest.SearchAsYouTypeSpec, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SearchAsYouTypeSpec message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SearchAsYouTypeSpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.searchrequest.searchasyoutypespec-class)`   
SearchAsYouTypeSpec  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SearchAsYouTypeSpec message.

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
