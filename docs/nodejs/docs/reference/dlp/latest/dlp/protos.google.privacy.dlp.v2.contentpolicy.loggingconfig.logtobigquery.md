---
url: https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.contentpolicy.loggingconfig.logtobigquery
title: Class protos.google.privacy.dlp.v2.ContentPolicy.LoggingConfig.LogToBigQuery (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:27.041692+00:00
---

# Class protos.google.privacy.dlp.v2.ContentPolicy.LoggingConfig.LogToBigQuery (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.contentpolicy.loggingconfig.logtobigquery

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.privacy.dlp.v2.ContentPolicy.LoggingConfig.LogToBigQuery (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  7.0.1  6.6.0  6.2.0  6.1.0  5.13.0  5.11.0  5.10.0  5.7.0  5.5.0  5.3.0  5.0.0  4.4.2  4.2.0  4.1.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.8 

Represents a LogToBigQuery.

## Implements

[protos.google.privacy.dlp.v2.ContentPolicy.LoggingConfig.ILogToBigQuery](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.contentpolicy.loggingconfig.ilogtobigquery)

## Package

[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.privacy.dlp.v2.ContentPolicy.LoggingConfig.ILogToBigQuery);

Constructs a new LogToBigQuery.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILogToBigQuery](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.contentpolicy.loggingconfig.ilogtobigquery)`   
Properties to set  
  
## Properties 

### datasetId
    
    
    public datasetId: string;

LogToBigQuery datasetId.

### projectId
    
    
    public projectId: string;

LogToBigQuery projectId.

### tableId
    
    
    public tableId: string;

LogToBigQuery tableId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.privacy.dlp.v2.ContentPolicy.LoggingConfig.ILogToBigQuery): google.privacy.dlp.v2.ContentPolicy.LoggingConfig.LogToBigQuery;

Creates a new LogToBigQuery instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILogToBigQuery](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.contentpolicy.loggingconfig.ilogtobigquery)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[LogToBigQuery](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.contentpolicy.loggingconfig.logtobigquery)` | LogToBigQuery instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.privacy.dlp.v2.ContentPolicy.LoggingConfig.LogToBigQuery;

Decodes a LogToBigQuery message from the specified reader or buffer.

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
`[LogToBigQuery](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.contentpolicy.loggingconfig.logtobigquery)` | LogToBigQuery  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.privacy.dlp.v2.ContentPolicy.LoggingConfig.LogToBigQuery;

Decodes a LogToBigQuery message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[LogToBigQuery](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.contentpolicy.loggingconfig.logtobigquery)` | LogToBigQuery  
  
### encode(message, writer)
    
    
    public static encode(message: google.privacy.dlp.v2.ContentPolicy.LoggingConfig.ILogToBigQuery, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LogToBigQuery message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILogToBigQuery](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.contentpolicy.loggingconfig.ilogtobigquery)`   
LogToBigQuery message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.privacy.dlp.v2.ContentPolicy.LoggingConfig.ILogToBigQuery, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LogToBigQuery message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILogToBigQuery](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.contentpolicy.loggingconfig.ilogtobigquery)`   
LogToBigQuery message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.privacy.dlp.v2.ContentPolicy.LoggingConfig.LogToBigQuery;

Creates a LogToBigQuery message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[LogToBigQuery](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.contentpolicy.loggingconfig.logtobigquery)` | LogToBigQuery  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for LogToBigQuery

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

Converts this LogToBigQuery to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.privacy.dlp.v2.ContentPolicy.LoggingConfig.LogToBigQuery, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a LogToBigQuery message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[LogToBigQuery](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.contentpolicy.loggingconfig.logtobigquery)`   
LogToBigQuery  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a LogToBigQuery message.

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
