---
url: https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.build-class
title: Class protos.google.devtools.cloudbuild.v1.Build (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:35.742508+00:00
---

# Class protos.google.devtools.cloudbuild.v1.Build (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.build-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.devtools.cloudbuild.v1.Build (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.6.0  5.5.0  5.1.0  4.8.0  4.7.0  4.1.1  4.0.0  3.6.0  3.3.0  3.2.0  3.1.2  2.6.0  2.5.0  2.4.0  2.3.2  2.2.7 

Represents a Build.

## Implements

[protos.google.devtools.cloudbuild.v1.IBuild](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.ibuild)

## Package

[@google-cloud/cloudbuild](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.devtools.cloudbuild.v1.IBuild);

Constructs a new Build.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBuild](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.ibuild)`   
Properties to set  
  
## Properties 

### approval
    
    
    public approval?: (google.devtools.cloudbuild.v1.IBuildApproval|null);

Build approval.

### artifacts
    
    
    public artifacts?: (google.devtools.cloudbuild.v1.IArtifacts|null);

Build artifacts.

### availableSecrets
    
    
    public availableSecrets?: (google.devtools.cloudbuild.v1.ISecrets|null);

Build availableSecrets.

### buildTriggerId
    
    
    public buildTriggerId: string;

Build buildTriggerId.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Build createTime.

### dependencies
    
    
    public dependencies: google.devtools.cloudbuild.v1.IDependency[];

Build dependencies.

### failureInfo
    
    
    public failureInfo?: (google.devtools.cloudbuild.v1.Build.IFailureInfo|null);

Build failureInfo.

### finishTime
    
    
    public finishTime?: (google.protobuf.ITimestamp|null);

Build finishTime.

### gitConfig
    
    
    public gitConfig?: (google.devtools.cloudbuild.v1.IGitConfig|null);

Build gitConfig.

### id
    
    
    public id: string;

Build id.

### images
    
    
    public images: string[];

Build images.

### logsBucket
    
    
    public logsBucket: string;

Build logsBucket.

### logUrl
    
    
    public logUrl: string;

Build logUrl.

### name
    
    
    public name: string;

Build name.

### options
    
    
    public options?: (google.devtools.cloudbuild.v1.IBuildOptions|null);

Build options.

### projectId
    
    
    public projectId: string;

Build projectId.

### queueTtl
    
    
    public queueTtl?: (google.protobuf.IDuration|null);

Build queueTtl.

### results
    
    
    public results?: (google.devtools.cloudbuild.v1.IResults|null);

Build results.

### secrets
    
    
    public secrets: google.devtools.cloudbuild.v1.ISecret[];

Build secrets.

### serviceAccount
    
    
    public serviceAccount: string;

Build serviceAccount.

### source
    
    
    public source?: (google.devtools.cloudbuild.v1.ISource|null);

Build source.

### sourceProvenance
    
    
    public sourceProvenance?: (google.devtools.cloudbuild.v1.ISourceProvenance|null);

Build sourceProvenance.

### startTime
    
    
    public startTime?: (google.protobuf.ITimestamp|null);

Build startTime.

### status
    
    
    public status: (google.devtools.cloudbuild.v1.Build.Status|keyof typeof google.devtools.cloudbuild.v1.Build.Status);

Build status.

### statusDetail
    
    
    public statusDetail: string;

Build statusDetail.

### steps
    
    
    public steps: google.devtools.cloudbuild.v1.IBuildStep[];

Build steps.

### substitutions
    
    
    public substitutions: { [k: string]: string };

Build substitutions.

### tags
    
    
    public tags: string[];

Build tags.

### timeout
    
    
    public timeout?: (google.protobuf.IDuration|null);

Build timeout.

### timing
    
    
    public timing: { [k: string]: google.devtools.cloudbuild.v1.ITimeSpan };

Build timing.

### warnings
    
    
    public warnings: google.devtools.cloudbuild.v1.Build.IWarning[];

Build warnings.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.devtools.cloudbuild.v1.IBuild): google.devtools.cloudbuild.v1.Build;

Creates a new Build instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBuild](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.ibuild)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Build](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.build-class)` | Build instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.devtools.cloudbuild.v1.Build;

Decodes a Build message from the specified reader or buffer.

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
`[Build](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.build-class)` | Build  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.devtools.cloudbuild.v1.Build;

Decodes a Build message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Build](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.build-class)` | Build  
  
### encode(message, writer)
    
    
    public static encode(message: google.devtools.cloudbuild.v1.IBuild, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Build message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBuild](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.ibuild)`   
Build message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.devtools.cloudbuild.v1.IBuild, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Build message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBuild](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.ibuild)`   
Build message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.devtools.cloudbuild.v1.Build;

Creates a Build message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Build](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.build-class)` | Build  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Build

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

Converts this Build to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.devtools.cloudbuild.v1.Build, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Build message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Build](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.build-class)`   
Build  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Build message.

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
