---
url: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.jobrun-class
title: Class protos.google.cloud.deploy.v1.JobRun (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:39.245708+00:00
---

# Class protos.google.cloud.deploy.v1.JobRun (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.jobrun-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.deploy.v1.JobRun (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.0.1  4.4.0  4.3.0  4.0.0  3.6.0  3.5.0  3.4.0  3.1.0  3.0.0  2.5.0  2.4.1  2.3.1  2.2.2  2.1.1  1.0.0  0.2.0 

Represents a JobRun.

## Implements

[protos.google.cloud.deploy.v1.IJobRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ijobrun)

## Package

[@google-cloud/deploy](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.deploy.v1.IJobRun);

Constructs a new JobRun.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IJobRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ijobrun)`   
Properties to set  
  
## Properties 

### advanceChildRolloutJobRun
    
    
    public advanceChildRolloutJobRun?: (google.cloud.deploy.v1.IAdvanceChildRolloutJobRun|null);

JobRun advanceChildRolloutJobRun.

### createChildRolloutJobRun
    
    
    public createChildRolloutJobRun?: (google.cloud.deploy.v1.ICreateChildRolloutJobRun|null);

JobRun createChildRolloutJobRun.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

JobRun createTime.

### deployJobRun
    
    
    public deployJobRun?: (google.cloud.deploy.v1.IDeployJobRun|null);

JobRun deployJobRun.

### endTime
    
    
    public endTime?: (google.protobuf.ITimestamp|null);

JobRun endTime.

### etag
    
    
    public etag: string;

JobRun etag.

### jobId
    
    
    public jobId: string;

JobRun jobId.

### jobRun
    
    
    public jobRun?: ("deployJobRun"|"verifyJobRun"|"predeployJobRun"|"postdeployJobRun"|"createChildRolloutJobRun"|"advanceChildRolloutJobRun");

JobRun jobRun.

### name
    
    
    public name: string;

JobRun name.

### phaseId
    
    
    public phaseId: string;

JobRun phaseId.

### postdeployJobRun
    
    
    public postdeployJobRun?: (google.cloud.deploy.v1.IPostdeployJobRun|null);

JobRun postdeployJobRun.

### predeployJobRun
    
    
    public predeployJobRun?: (google.cloud.deploy.v1.IPredeployJobRun|null);

JobRun predeployJobRun.

### startTime
    
    
    public startTime?: (google.protobuf.ITimestamp|null);

JobRun startTime.

### state
    
    
    public state: (google.cloud.deploy.v1.JobRun.State|keyof typeof google.cloud.deploy.v1.JobRun.State);

JobRun state.

### uid
    
    
    public uid: string;

JobRun uid.

### verifyJobRun
    
    
    public verifyJobRun?: (google.cloud.deploy.v1.IVerifyJobRun|null);

JobRun verifyJobRun.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.deploy.v1.IJobRun): google.cloud.deploy.v1.JobRun;

Creates a new JobRun instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IJobRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ijobrun)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[JobRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.jobrun-class)` | JobRun instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.deploy.v1.JobRun;

Decodes a JobRun message from the specified reader or buffer.

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
`[JobRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.jobrun-class)` | JobRun  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.deploy.v1.JobRun;

Decodes a JobRun message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[JobRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.jobrun-class)` | JobRun  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.deploy.v1.IJobRun, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified JobRun message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IJobRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ijobrun)`   
JobRun message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.deploy.v1.IJobRun, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified JobRun message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IJobRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.ijobrun)`   
JobRun message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.deploy.v1.JobRun;

Creates a JobRun message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[JobRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.jobrun-class)` | JobRun  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for JobRun

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

Converts this JobRun to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.deploy.v1.JobRun, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a JobRun message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[JobRun](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.jobrun-class)`   
JobRun  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a JobRun message.

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
