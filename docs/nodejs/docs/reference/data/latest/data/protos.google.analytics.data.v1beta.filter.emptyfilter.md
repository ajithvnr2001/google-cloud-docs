---
url: https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.filter.emptyfilter
title: Class protos.google.analytics.data.v1beta.Filter.EmptyFilter (7.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:32.502321+00:00
---

# Class protos.google.analytics.data.v1beta.Filter.EmptyFilter (7.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.filter.emptyfilter

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.analytics.data.v1beta.Filter.EmptyFilter (7.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.2.1 (latest)  7.2.0  7.1.0  6.1.0  6.0.0  4.12.0  4.11.0  4.9.0  4.8.0  4.6.0  4.5.0  3.2.1 

Represents an EmptyFilter.

## Implements

[protos.google.analytics.data.v1beta.Filter.IEmptyFilter](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.filter.iemptyfilter)

## Package

[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.analytics.data.v1beta.Filter.IEmptyFilter);

Constructs a new EmptyFilter.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEmptyFilter](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.filter.iemptyfilter)`   
Properties to set  
  
## Methods 

### create(properties)
    
    
    public static create(properties?: google.analytics.data.v1beta.Filter.IEmptyFilter): google.analytics.data.v1beta.Filter.EmptyFilter;

Creates a new EmptyFilter instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEmptyFilter](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.filter.iemptyfilter)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[EmptyFilter](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.filter.emptyfilter)` | EmptyFilter instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.analytics.data.v1beta.Filter.EmptyFilter;

Decodes an EmptyFilter message from the specified reader or buffer.

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
`[EmptyFilter](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.filter.emptyfilter)` | EmptyFilter  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.analytics.data.v1beta.Filter.EmptyFilter;

Decodes an EmptyFilter message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[EmptyFilter](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.filter.emptyfilter)` | EmptyFilter  
  
### encode(message, writer)
    
    
    public static encode(message: google.analytics.data.v1beta.Filter.IEmptyFilter, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EmptyFilter message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEmptyFilter](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.filter.iemptyfilter)`   
EmptyFilter message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.analytics.data.v1beta.Filter.IEmptyFilter, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EmptyFilter message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEmptyFilter](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.filter.iemptyfilter)`   
EmptyFilter message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.analytics.data.v1beta.Filter.EmptyFilter;

Creates an EmptyFilter message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[EmptyFilter](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.filter.emptyfilter)` | EmptyFilter  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for EmptyFilter

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

Converts this EmptyFilter to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.analytics.data.v1beta.Filter.EmptyFilter, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an EmptyFilter message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[EmptyFilter](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1beta.filter.emptyfilter)`   
EmptyFilter  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an EmptyFilter message.

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
