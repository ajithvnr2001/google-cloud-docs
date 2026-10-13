---
url: https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.buildtrigger
title: Class protos.google.devtools.cloudbuild.v1.BuildTrigger (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:25:28.939454+00:00
---

# Class protos.google.devtools.cloudbuild.v1.BuildTrigger (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.buildtrigger

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.devtools.cloudbuild.v1.BuildTrigger (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.6.0  5.5.0  5.1.0  4.8.0  4.7.0  4.1.1  4.0.0  3.6.0  3.3.0  3.2.0  3.1.2  2.6.0  2.5.0  2.4.0  2.3.2  2.2.7 

Represents a BuildTrigger.

## Implements

[protos.google.devtools.cloudbuild.v1.IBuildTrigger](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.ibuildtrigger)

## Package

[@google-cloud/cloudbuild](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.devtools.cloudbuild.v1.IBuildTrigger);

Constructs a new BuildTrigger.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBuildTrigger](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.ibuildtrigger)`   
Properties to set  
  
## Properties 

### autodetect
    
    
    public autodetect?: (boolean|null);

BuildTrigger autodetect.

### build
    
    
    public build?: (google.devtools.cloudbuild.v1.IBuild|null);

BuildTrigger build.

### buildTemplate
    
    
    public buildTemplate?: ("autodetect"|"build"|"filename"|"gitFileSource");

BuildTrigger buildTemplate.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

BuildTrigger createTime.

### description
    
    
    public description: string;

BuildTrigger description.

### disabled
    
    
    public disabled: boolean;

BuildTrigger disabled.

### filename
    
    
    public filename?: (string|null);

BuildTrigger filename.

### filter
    
    
    public filter: string;

BuildTrigger filter.

### gitFileSource
    
    
    public gitFileSource?: (google.devtools.cloudbuild.v1.IGitFileSource|null);

BuildTrigger gitFileSource.

### github
    
    
    public github?: (google.devtools.cloudbuild.v1.IGitHubEventsConfig|null);

BuildTrigger github.

### id
    
    
    public id: string;

BuildTrigger id.

### ignoredFiles
    
    
    public ignoredFiles: string[];

BuildTrigger ignoredFiles.

### includedFiles
    
    
    public includedFiles: string[];

BuildTrigger includedFiles.

### name
    
    
    public name: string;

BuildTrigger name.

### pubsubConfig
    
    
    public pubsubConfig?: (google.devtools.cloudbuild.v1.IPubsubConfig|null);

BuildTrigger pubsubConfig.

### repositoryEventConfig
    
    
    public repositoryEventConfig?: (google.devtools.cloudbuild.v1.IRepositoryEventConfig|null);

BuildTrigger repositoryEventConfig.

### resourceName
    
    
    public resourceName: string;

BuildTrigger resourceName.

### serviceAccount
    
    
    public serviceAccount: string;

BuildTrigger serviceAccount.

### sourceToBuild
    
    
    public sourceToBuild?: (google.devtools.cloudbuild.v1.IGitRepoSource|null);

BuildTrigger sourceToBuild.

### substitutions
    
    
    public substitutions: { [k: string]: string };

BuildTrigger substitutions.

### tags
    
    
    public tags: string[];

BuildTrigger tags.

### triggerTemplate
    
    
    public triggerTemplate?: (google.devtools.cloudbuild.v1.IRepoSource|null);

BuildTrigger triggerTemplate.

### webhookConfig
    
    
    public webhookConfig?: (google.devtools.cloudbuild.v1.IWebhookConfig|null);

BuildTrigger webhookConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.devtools.cloudbuild.v1.IBuildTrigger): google.devtools.cloudbuild.v1.BuildTrigger;

Creates a new BuildTrigger instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBuildTrigger](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.ibuildtrigger)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[BuildTrigger](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.buildtrigger)` | BuildTrigger instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.devtools.cloudbuild.v1.BuildTrigger;

Decodes a BuildTrigger message from the specified reader or buffer.

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
`[BuildTrigger](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.buildtrigger)` | BuildTrigger  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.devtools.cloudbuild.v1.BuildTrigger;

Decodes a BuildTrigger message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[BuildTrigger](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.buildtrigger)` | BuildTrigger  
  
### encode(message, writer)
    
    
    public static encode(message: google.devtools.cloudbuild.v1.IBuildTrigger, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BuildTrigger message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBuildTrigger](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.ibuildtrigger)`   
BuildTrigger message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.devtools.cloudbuild.v1.IBuildTrigger, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BuildTrigger message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBuildTrigger](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.ibuildtrigger)`   
BuildTrigger message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.devtools.cloudbuild.v1.BuildTrigger;

Creates a BuildTrigger message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[BuildTrigger](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.buildtrigger)` | BuildTrigger  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for BuildTrigger

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

Converts this BuildTrigger to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.devtools.cloudbuild.v1.BuildTrigger, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a BuildTrigger message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[BuildTrigger](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.buildtrigger)`   
BuildTrigger  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a BuildTrigger message.

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
