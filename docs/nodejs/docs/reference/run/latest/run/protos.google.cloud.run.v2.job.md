---
url: https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.job
title: Class protos.google.cloud.run.v2.Job (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:13.631339+00:00
---

# Class protos.google.cloud.run.v2.Job (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.job

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.run.v2.Job (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  3.3.0  3.2.0  2.1.0  1.5.0  1.0.2  0.5.0  0.4.2  0.2.3 

Represents a Job.

## Implements

[protos.google.cloud.run.v2.IJob](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.ijob)

## Package

[@google-cloud/run](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.run.v2.IJob);

Constructs a new Job.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IJob](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.ijob)`   
Properties to set  
  
## Properties 

### annotations
    
    
    public annotations: { [k: string]: string };

Job annotations.

### binaryAuthorization
    
    
    public binaryAuthorization?: (google.cloud.run.v2.IBinaryAuthorization|null);

Job binaryAuthorization.

### client
    
    
    public client: string;

Job client.

### clientVersion
    
    
    public clientVersion: string;

Job clientVersion.

### conditions
    
    
    public conditions: google.cloud.run.v2.ICondition[];

Job conditions.

### createExecution
    
    
    public createExecution?: ("startExecutionToken"|"runExecutionToken");

Job createExecution.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Job createTime.

### creator
    
    
    public creator: string;

Job creator.

### deleteTime
    
    
    public deleteTime?: (google.protobuf.ITimestamp|null);

Job deleteTime.

### etag
    
    
    public etag: string;

Job etag.

### executionCount
    
    
    public executionCount: number;

Job executionCount.

### expireTime
    
    
    public expireTime?: (google.protobuf.ITimestamp|null);

Job expireTime.

### generation
    
    
    public generation: (number|Long|string);

Job generation.

### labels
    
    
    public labels: { [k: string]: string };

Job labels.

### lastModifier
    
    
    public lastModifier: string;

Job lastModifier.

### latestCreatedExecution
    
    
    public latestCreatedExecution?: (google.cloud.run.v2.IExecutionReference|null);

Job latestCreatedExecution.

### launchStage
    
    
    public launchStage: (google.api.LaunchStage|keyof typeof google.api.LaunchStage);

Job launchStage.

### name
    
    
    public name: string;

Job name.

### observedGeneration
    
    
    public observedGeneration: (number|Long|string);

Job observedGeneration.

### reconciling
    
    
    public reconciling: boolean;

Job reconciling.

### runExecutionToken
    
    
    public runExecutionToken?: (string|null);

Job runExecutionToken.

### satisfiesPzs
    
    
    public satisfiesPzs: boolean;

Job satisfiesPzs.

### startExecutionToken
    
    
    public startExecutionToken?: (string|null);

Job startExecutionToken.

### template
    
    
    public template?: (google.cloud.run.v2.IExecutionTemplate|null);

Job template.

### terminalCondition
    
    
    public terminalCondition?: (google.cloud.run.v2.ICondition|null);

Job terminalCondition.

### uid
    
    
    public uid: string;

Job uid.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Job updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.run.v2.IJob): google.cloud.run.v2.Job;

Creates a new Job instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IJob](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.ijob)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.job)` | Job instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.run.v2.Job;

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
`[Job](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.job)` | Job  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.run.v2.Job;

Decodes a Job message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.job)` | Job  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.run.v2.IJob, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Job message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IJob](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.ijob)`   
Job message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.run.v2.IJob, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Job message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IJob](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.ijob)`   
Job message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.run.v2.Job;

Creates a Job message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.job)` | Job  
  
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
    
    
    public static toObject(message: google.cloud.run.v2.Job, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Job message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Job](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.job)`   
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
