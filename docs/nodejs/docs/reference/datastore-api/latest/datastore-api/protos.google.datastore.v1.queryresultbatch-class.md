---
url: https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.queryresultbatch-class
title: Class protos.google.datastore.v1.QueryResultBatch (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:47:52.766494+00:00
---

# Class protos.google.datastore.v1.QueryResultBatch (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.queryresultbatch-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.datastore.v1.QueryResultBatch (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a QueryResultBatch.

## Implements

[protos.google.datastore.v1.IQueryResultBatch](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.iqueryresultbatch)

## Package

[@google-cloud/datastore-api](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.datastore.v1.IQueryResultBatch);

Constructs a new QueryResultBatch.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IQueryResultBatch](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.iqueryresultbatch)`   
Properties to set  
  
## Properties 

### endCursor
    
    
    public endCursor: (Uint8Array|Buffer|string);

QueryResultBatch endCursor.

### entityResults
    
    
    public entityResults: google.datastore.v1.IEntityResult[];

QueryResultBatch entityResults.

### entityResultType
    
    
    public entityResultType: (google.datastore.v1.EntityResult.ResultType|keyof typeof google.datastore.v1.EntityResult.ResultType);

QueryResultBatch entityResultType.

### moreResults
    
    
    public moreResults: (google.datastore.v1.QueryResultBatch.MoreResultsType|keyof typeof google.datastore.v1.QueryResultBatch.MoreResultsType);

QueryResultBatch moreResults.

### readTime
    
    
    public readTime?: (google.protobuf.ITimestamp|null);

QueryResultBatch readTime.

### skippedCursor
    
    
    public skippedCursor: (Uint8Array|Buffer|string);

QueryResultBatch skippedCursor.

### skippedResults
    
    
    public skippedResults: number;

QueryResultBatch skippedResults.

### snapshotVersion
    
    
    public snapshotVersion: (number|Long|string);

QueryResultBatch snapshotVersion.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.datastore.v1.IQueryResultBatch): google.datastore.v1.QueryResultBatch;

Creates a new QueryResultBatch instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IQueryResultBatch](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.iqueryresultbatch)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[QueryResultBatch](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.queryresultbatch-class)` | QueryResultBatch instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.datastore.v1.QueryResultBatch;

Decodes a QueryResultBatch message from the specified reader or buffer.

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
`[QueryResultBatch](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.queryresultbatch-class)` | QueryResultBatch  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.datastore.v1.QueryResultBatch;

Decodes a QueryResultBatch message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[QueryResultBatch](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.queryresultbatch-class)` | QueryResultBatch  
  
### encode(message, writer)
    
    
    public static encode(message: google.datastore.v1.IQueryResultBatch, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified QueryResultBatch message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IQueryResultBatch](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.iqueryresultbatch)`   
QueryResultBatch message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.datastore.v1.IQueryResultBatch, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified QueryResultBatch message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IQueryResultBatch](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.iqueryresultbatch)`   
QueryResultBatch message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.datastore.v1.QueryResultBatch;

Creates a QueryResultBatch message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[QueryResultBatch](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.queryresultbatch-class)` | QueryResultBatch  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for QueryResultBatch

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

Converts this QueryResultBatch to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.datastore.v1.QueryResultBatch, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a QueryResultBatch message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[QueryResultBatch](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.queryresultbatch-class)`   
QueryResultBatch  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a QueryResultBatch message.

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
