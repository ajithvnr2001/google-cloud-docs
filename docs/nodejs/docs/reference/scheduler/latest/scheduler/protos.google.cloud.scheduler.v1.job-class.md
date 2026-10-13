---
url: https://docs.cloud.google.com/nodejs/docs/reference/scheduler/latest/scheduler/protos.google.cloud.scheduler.v1.job-class
title: Class protos.google.cloud.scheduler.v1.Job (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:46.619784+00:00
---

# Class protos.google.cloud.scheduler.v1.Job (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/scheduler/latest/scheduler/protos.google.cloud.scheduler.v1.job-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.scheduler.v1.Job (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.4.0  5.2.0  3.3.1  3.2.1  3.0.5  2.3.0  2.2.6  2.1.1 

Represents a Job.

## Implements

[protos.google.cloud.scheduler.v1.IJob](https://docs.cloud.google.com/nodejs/docs/reference/scheduler/latest/scheduler/protos.google.cloud.scheduler.v1.ijob)

## Package

[@google-cloud/scheduler](https://docs.cloud.google.com/nodejs/docs/reference/scheduler/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.scheduler.v1.IJob);

Constructs a new Job.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IJob](https://docs.cloud.google.com/nodejs/docs/reference/scheduler/latest/scheduler/protos.google.cloud.scheduler.v1.ijob)`   
Properties to set  
  
## Properties 

### appEngineHttpTarget
    
    
    public appEngineHttpTarget?: (google.cloud.scheduler.v1.IAppEngineHttpTarget|null);

Job appEngineHttpTarget.

### attemptDeadline
    
    
    public attemptDeadline?: (google.protobuf.IDuration|null);

Job attemptDeadline.

### description
    
    
    public description: string;

Job description.

### httpTarget
    
    
    public httpTarget?: (google.cloud.scheduler.v1.IHttpTarget|null);

Job httpTarget.

### lastAttemptTime
    
    
    public lastAttemptTime?: (google.protobuf.ITimestamp|null);

Job lastAttemptTime.

### name
    
    
    public name: string;

Job name.

### pubsubTarget
    
    
    public pubsubTarget?: (google.cloud.scheduler.v1.IPubsubTarget|null);

Job pubsubTarget.

### retryConfig
    
    
    public retryConfig?: (google.cloud.scheduler.v1.IRetryConfig|null);

Job retryConfig.

### schedule
    
    
    public schedule: string;

Job schedule.

### scheduleTime
    
    
    public scheduleTime?: (google.protobuf.ITimestamp|null);

Job scheduleTime.

### state
    
    
    public state: (google.cloud.scheduler.v1.Job.State|keyof typeof google.cloud.scheduler.v1.Job.State);

Job state.

### status
    
    
    public status?: (google.rpc.IStatus|null);

Job status.

### target
    
    
    public target?: ("pubsubTarget"|"appEngineHttpTarget"|"httpTarget");

Job target.

### timeZone
    
    
    public timeZone: string;

Job timeZone.

### userUpdateTime
    
    
    public userUpdateTime?: (google.protobuf.ITimestamp|null);

Job userUpdateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.scheduler.v1.IJob): google.cloud.scheduler.v1.Job;

Creates a new Job instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IJob](https://docs.cloud.google.com/nodejs/docs/reference/scheduler/latest/scheduler/protos.google.cloud.scheduler.v1.ijob)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/nodejs/docs/reference/scheduler/latest/scheduler/protos.google.cloud.scheduler.v1.job-class)` | Job instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.scheduler.v1.Job;

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
`[Job](https://docs.cloud.google.com/nodejs/docs/reference/scheduler/latest/scheduler/protos.google.cloud.scheduler.v1.job-class)` | Job  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.scheduler.v1.Job;

Decodes a Job message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/nodejs/docs/reference/scheduler/latest/scheduler/protos.google.cloud.scheduler.v1.job-class)` | Job  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.scheduler.v1.IJob, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Job message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IJob](https://docs.cloud.google.com/nodejs/docs/reference/scheduler/latest/scheduler/protos.google.cloud.scheduler.v1.ijob)`   
Job message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.scheduler.v1.IJob, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Job message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IJob](https://docs.cloud.google.com/nodejs/docs/reference/scheduler/latest/scheduler/protos.google.cloud.scheduler.v1.ijob)`   
Job message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.scheduler.v1.Job;

Creates a Job message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/nodejs/docs/reference/scheduler/latest/scheduler/protos.google.cloud.scheduler.v1.job-class)` | Job  
  
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
    
    
    public static toObject(message: google.cloud.scheduler.v1.Job, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Job message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Job](https://docs.cloud.google.com/nodejs/docs/reference/scheduler/latest/scheduler/protos.google.cloud.scheduler.v1.job-class)`   
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

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
