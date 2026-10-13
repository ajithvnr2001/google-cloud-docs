---
url: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.matchedquery
title: Class protos.google.cloud.geminidataanalytics.v1.MatchedQuery (0.13.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:37:43.333549+00:00
---

# Class protos.google.cloud.geminidataanalytics.v1.MatchedQuery (0.13.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.matchedquery

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.geminidataanalytics.v1.MatchedQuery (0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.13.0  0.7.0  0.6.0  0.4.0  0.2.0 

Represents a MatchedQuery.

## Implements

[protos.google.cloud.geminidataanalytics.v1.IMatchedQuery](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.imatchedquery)

## Package

[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.geminidataanalytics.v1.IMatchedQuery);

Constructs a new MatchedQuery.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMatchedQuery](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.imatchedquery)`   
Properties to set  
  
## Properties 

### exampleQuery
    
    
    public exampleQuery?: (google.cloud.geminidataanalytics.v1.IExampleQuery|null);

MatchedQuery exampleQuery.

### queryParameterValues
    
    
    public queryParameterValues: google.cloud.geminidataanalytics.v1.IQueryParameterValues[];

MatchedQuery queryParameterValues.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.geminidataanalytics.v1.IMatchedQuery): google.cloud.geminidataanalytics.v1.MatchedQuery;

Creates a new MatchedQuery instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMatchedQuery](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.imatchedquery)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[MatchedQuery](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.matchedquery)` | MatchedQuery instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.geminidataanalytics.v1.MatchedQuery;

Decodes a MatchedQuery message from the specified reader or buffer.

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
`[MatchedQuery](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.matchedquery)` | MatchedQuery  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.geminidataanalytics.v1.MatchedQuery;

Decodes a MatchedQuery message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[MatchedQuery](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.matchedquery)` | MatchedQuery  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.geminidataanalytics.v1.IMatchedQuery, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MatchedQuery message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMatchedQuery](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.imatchedquery)`   
MatchedQuery message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.geminidataanalytics.v1.IMatchedQuery, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MatchedQuery message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMatchedQuery](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.imatchedquery)`   
MatchedQuery message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.geminidataanalytics.v1.MatchedQuery;

Creates a MatchedQuery message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[MatchedQuery](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.matchedquery)` | MatchedQuery  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for MatchedQuery

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

Converts this MatchedQuery to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.geminidataanalytics.v1.MatchedQuery, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a MatchedQuery message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[MatchedQuery](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.matchedquery)`   
MatchedQuery  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a MatchedQuery message.

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
