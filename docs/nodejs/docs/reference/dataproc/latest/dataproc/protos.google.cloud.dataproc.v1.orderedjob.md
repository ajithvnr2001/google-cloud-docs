---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.orderedjob
title: Class protos.google.cloud.dataproc.v1.OrderedJob (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:56.143601+00:00
---

# Class protos.google.cloud.dataproc.v1.OrderedJob (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.orderedjob

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataproc.v1.OrderedJob (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.8.0  6.7.0  6.6.0  5.13.0  5.12.0  5.10.0  5.9.0  5.7.0  5.5.0  5.4.0  4.5.0  4.3.1  4.1.1  3.2.0  3.1.0  3.0.0  2.5.0  2.4.4 

Represents an OrderedJob.

## Implements

[protos.google.cloud.dataproc.v1.IOrderedJob](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iorderedjob)

## Package

[@google-cloud/dataproc](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataproc.v1.IOrderedJob);

Constructs a new OrderedJob.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOrderedJob](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iorderedjob)`   
Properties to set  
  
## Properties 

### flinkJob
    
    
    public flinkJob?: (google.cloud.dataproc.v1.IFlinkJob|null);

OrderedJob flinkJob.

### hadoopJob
    
    
    public hadoopJob?: (google.cloud.dataproc.v1.IHadoopJob|null);

OrderedJob hadoopJob.

### hiveJob
    
    
    public hiveJob?: (google.cloud.dataproc.v1.IHiveJob|null);

OrderedJob hiveJob.

### jobType
    
    
    public jobType?: ("hadoopJob"|"sparkJob"|"pysparkJob"|"hiveJob"|"pigJob"|"sparkRJob"|"sparkSqlJob"|"prestoJob"|"trinoJob"|"flinkJob");

OrderedJob jobType.

### labels
    
    
    public labels: { [k: string]: string };

OrderedJob labels.

### pigJob
    
    
    public pigJob?: (google.cloud.dataproc.v1.IPigJob|null);

OrderedJob pigJob.

### prerequisiteStepIds
    
    
    public prerequisiteStepIds: string[];

OrderedJob prerequisiteStepIds.

### prestoJob
    
    
    public prestoJob?: (google.cloud.dataproc.v1.IPrestoJob|null);

OrderedJob prestoJob.

### pysparkJob
    
    
    public pysparkJob?: (google.cloud.dataproc.v1.IPySparkJob|null);

OrderedJob pysparkJob.

### scheduling
    
    
    public scheduling?: (google.cloud.dataproc.v1.IJobScheduling|null);

OrderedJob scheduling.

### sparkJob
    
    
    public sparkJob?: (google.cloud.dataproc.v1.ISparkJob|null);

OrderedJob sparkJob.

### sparkRJob
    
    
    public sparkRJob?: (google.cloud.dataproc.v1.ISparkRJob|null);

OrderedJob sparkRJob.

### sparkSqlJob
    
    
    public sparkSqlJob?: (google.cloud.dataproc.v1.ISparkSqlJob|null);

OrderedJob sparkSqlJob.

### stepId
    
    
    public stepId: string;

OrderedJob stepId.

### trinoJob
    
    
    public trinoJob?: (google.cloud.dataproc.v1.ITrinoJob|null);

OrderedJob trinoJob.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataproc.v1.IOrderedJob): google.cloud.dataproc.v1.OrderedJob;

Creates a new OrderedJob instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOrderedJob](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iorderedjob)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[OrderedJob](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.orderedjob)` | OrderedJob instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataproc.v1.OrderedJob;

Decodes an OrderedJob message from the specified reader or buffer.

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
`[OrderedJob](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.orderedjob)` | OrderedJob  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataproc.v1.OrderedJob;

Decodes an OrderedJob message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[OrderedJob](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.orderedjob)` | OrderedJob  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataproc.v1.IOrderedJob, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OrderedJob message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOrderedJob](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iorderedjob)`   
OrderedJob message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataproc.v1.IOrderedJob, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OrderedJob message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOrderedJob](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iorderedjob)`   
OrderedJob message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataproc.v1.OrderedJob;

Creates an OrderedJob message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[OrderedJob](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.orderedjob)` | OrderedJob  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for OrderedJob

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

Converts this OrderedJob to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataproc.v1.OrderedJob, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an OrderedJob message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[OrderedJob](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.orderedjob)`   
OrderedJob  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an OrderedJob message.

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
