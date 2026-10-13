---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.job
title: Class protos.google.cloud.dataproc.v1.Job (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:48.504679+00:00
---

# Class protos.google.cloud.dataproc.v1.Job (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.job

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataproc.v1.Job (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.8.0  6.7.0  6.6.0  5.13.0  5.12.0  5.10.0  5.9.0  5.7.0  5.5.0  5.4.0  4.5.0  4.3.1  4.1.1  3.2.0  3.1.0  3.0.0  2.5.0  2.4.4 

Represents a Job.

## Implements

[protos.google.cloud.dataproc.v1.IJob](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ijob)

## Package

[@google-cloud/dataproc](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataproc.v1.IJob);

Constructs a new Job.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IJob](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ijob)`   
Properties to set  
  
## Properties 

### done
    
    
    public done: boolean;

Job done.

### driverControlFilesUri
    
    
    public driverControlFilesUri: string;

Job driverControlFilesUri.

### driverOutputResourceUri
    
    
    public driverOutputResourceUri: string;

Job driverOutputResourceUri.

### driverSchedulingConfig
    
    
    public driverSchedulingConfig?: (google.cloud.dataproc.v1.IDriverSchedulingConfig|null);

Job driverSchedulingConfig.

### flinkJob
    
    
    public flinkJob?: (google.cloud.dataproc.v1.IFlinkJob|null);

Job flinkJob.

### hadoopJob
    
    
    public hadoopJob?: (google.cloud.dataproc.v1.IHadoopJob|null);

Job hadoopJob.

### hiveJob
    
    
    public hiveJob?: (google.cloud.dataproc.v1.IHiveJob|null);

Job hiveJob.

### jobUuid
    
    
    public jobUuid: string;

Job jobUuid.

### labels
    
    
    public labels: { [k: string]: string };

Job labels.

### pigJob
    
    
    public pigJob?: (google.cloud.dataproc.v1.IPigJob|null);

Job pigJob.

### placement
    
    
    public placement?: (google.cloud.dataproc.v1.IJobPlacement|null);

Job placement.

### prestoJob
    
    
    public prestoJob?: (google.cloud.dataproc.v1.IPrestoJob|null);

Job prestoJob.

### pysparkJob
    
    
    public pysparkJob?: (google.cloud.dataproc.v1.IPySparkJob|null);

Job pysparkJob.

### reference
    
    
    public reference?: (google.cloud.dataproc.v1.IJobReference|null);

Job reference.

### scheduling
    
    
    public scheduling?: (google.cloud.dataproc.v1.IJobScheduling|null);

Job scheduling.

### sparkJob
    
    
    public sparkJob?: (google.cloud.dataproc.v1.ISparkJob|null);

Job sparkJob.

### sparkRJob
    
    
    public sparkRJob?: (google.cloud.dataproc.v1.ISparkRJob|null);

Job sparkRJob.

### sparkSqlJob
    
    
    public sparkSqlJob?: (google.cloud.dataproc.v1.ISparkSqlJob|null);

Job sparkSqlJob.

### status
    
    
    public status?: (google.cloud.dataproc.v1.IJobStatus|null);

Job status.

### statusHistory
    
    
    public statusHistory: google.cloud.dataproc.v1.IJobStatus[];

Job statusHistory.

### trinoJob
    
    
    public trinoJob?: (google.cloud.dataproc.v1.ITrinoJob|null);

Job trinoJob.

### typeJob
    
    
    public typeJob?: ("hadoopJob"|"sparkJob"|"pysparkJob"|"hiveJob"|"pigJob"|"sparkRJob"|"sparkSqlJob"|"prestoJob"|"trinoJob"|"flinkJob");

Job typeJob.

### yarnApplications
    
    
    public yarnApplications: google.cloud.dataproc.v1.IYarnApplication[];

Job yarnApplications.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataproc.v1.IJob): google.cloud.dataproc.v1.Job;

Creates a new Job instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IJob](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ijob)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.job)` | Job instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataproc.v1.Job;

Decodes a Job message from the specified reader or buffer.

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
`[Job](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.job)` | Job  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataproc.v1.Job;

Decodes a Job message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.job)` | Job  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataproc.v1.IJob, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Job message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IJob](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ijob)`   
Job message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataproc.v1.IJob, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Job message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IJob](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ijob)`   
Job message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataproc.v1.Job;

Creates a Job message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.job)` | Job  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Job

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

Converts this Job to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataproc.v1.Job, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Job message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Job](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.job)`   
Job  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Job message.

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
