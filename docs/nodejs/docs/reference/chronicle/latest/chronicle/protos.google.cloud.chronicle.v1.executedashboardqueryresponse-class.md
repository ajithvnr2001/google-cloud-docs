---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.executedashboardqueryresponse-class
title: Class protos.google.cloud.chronicle.v1.ExecuteDashboardQueryResponse (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:32.863846+00:00
---

# Class protos.google.cloud.chronicle.v1.ExecuteDashboardQueryResponse (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.executedashboardqueryresponse-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.chronicle.v1.ExecuteDashboardQueryResponse (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents an ExecuteDashboardQueryResponse.

## Implements

[protos.google.cloud.chronicle.v1.IExecuteDashboardQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iexecutedashboardqueryresponse)

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.chronicle.v1.IExecuteDashboardQueryResponse);

Constructs a new ExecuteDashboardQueryResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IExecuteDashboardQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iexecutedashboardqueryresponse)`   
Properties to set  
  
## Properties 

### dataSources
    
    
    public dataSources: google.cloud.chronicle.v1.DataSource[];

ExecuteDashboardQueryResponse dataSources.

### languageFeatures
    
    
    public languageFeatures: google.cloud.chronicle.v1.LanguageFeature[];

ExecuteDashboardQueryResponse languageFeatures.

### lastBackendCacheRefreshedTime
    
    
    public lastBackendCacheRefreshedTime?: (google.protobuf.ITimestamp|null);

ExecuteDashboardQueryResponse lastBackendCacheRefreshedTime.

### queryRuntimeErrors
    
    
    public queryRuntimeErrors: google.cloud.chronicle.v1.IQueryRuntimeError[];

ExecuteDashboardQueryResponse queryRuntimeErrors.

### results
    
    
    public results: google.cloud.chronicle.v1.ExecuteDashboardQueryResponse.IColumnData[];

ExecuteDashboardQueryResponse results.

### timeWindow
    
    
    public timeWindow?: (google.type.IInterval|null);

ExecuteDashboardQueryResponse timeWindow.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.chronicle.v1.IExecuteDashboardQueryResponse): google.cloud.chronicle.v1.ExecuteDashboardQueryResponse;

Creates a new ExecuteDashboardQueryResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IExecuteDashboardQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iexecutedashboardqueryresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ExecuteDashboardQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.executedashboardqueryresponse-class)` | ExecuteDashboardQueryResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.chronicle.v1.ExecuteDashboardQueryResponse;

Decodes an ExecuteDashboardQueryResponse message from the specified reader or buffer.

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
`[ExecuteDashboardQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.executedashboardqueryresponse-class)` | ExecuteDashboardQueryResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.chronicle.v1.ExecuteDashboardQueryResponse;

Decodes an ExecuteDashboardQueryResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ExecuteDashboardQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.executedashboardqueryresponse-class)` | ExecuteDashboardQueryResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.chronicle.v1.IExecuteDashboardQueryResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ExecuteDashboardQueryResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IExecuteDashboardQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iexecutedashboardqueryresponse)`   
ExecuteDashboardQueryResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.chronicle.v1.IExecuteDashboardQueryResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ExecuteDashboardQueryResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IExecuteDashboardQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iexecutedashboardqueryresponse)`   
ExecuteDashboardQueryResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.chronicle.v1.ExecuteDashboardQueryResponse;

Creates an ExecuteDashboardQueryResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ExecuteDashboardQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.executedashboardqueryresponse-class)` | ExecuteDashboardQueryResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ExecuteDashboardQueryResponse

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

Converts this ExecuteDashboardQueryResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.chronicle.v1.ExecuteDashboardQueryResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an ExecuteDashboardQueryResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ExecuteDashboardQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.executedashboardqueryresponse-class)`   
ExecuteDashboardQueryResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an ExecuteDashboardQueryResponse message.

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
