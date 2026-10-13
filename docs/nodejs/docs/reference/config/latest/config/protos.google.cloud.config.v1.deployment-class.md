---
url: https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.deployment-class
title: Class protos.google.cloud.config.v1.Deployment (0.15.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:52.154141+00:00
---

# Class protos.google.cloud.config.v1.Deployment (0.15.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.deployment-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.config.v1.Deployment (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.14.0  0.12.0  0.7.0  0.5.0  0.2.0  0.1.1 

Represents a Deployment.

## Implements

[protos.google.cloud.config.v1.IDeployment](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideployment)

## Package

[@google-cloud/config](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.config.v1.IDeployment);

Constructs a new Deployment.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeployment](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideployment)`   
Properties to set  
  
## Properties 

### annotations
    
    
    public annotations: { [k: string]: string };

Deployment annotations.

### artifactsGcsBucket
    
    
    public artifactsGcsBucket?: (string|null);

Deployment artifactsGcsBucket.

### blueprint
    
    
    public blueprint?: "terraformBlueprint";

Deployment blueprint.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Deployment createTime.

### deleteBuild
    
    
    public deleteBuild: string;

Deployment deleteBuild.

### deleteLogs
    
    
    public deleteLogs: string;

Deployment deleteLogs.

### deleteResults
    
    
    public deleteResults?: (google.cloud.config.v1.IApplyResults|null);

Deployment deleteResults.

### errorCode
    
    
    public errorCode: (google.cloud.config.v1.Deployment.ErrorCode|keyof typeof google.cloud.config.v1.Deployment.ErrorCode);

Deployment errorCode.

### errorLogs
    
    
    public errorLogs: string;

Deployment errorLogs.

### importExistingResources
    
    
    public importExistingResources?: (boolean|null);

Deployment importExistingResources.

### labels
    
    
    public labels: { [k: string]: string };

Deployment labels.

### latestRevision
    
    
    public latestRevision: string;

Deployment latestRevision.

### lockState
    
    
    public lockState: (google.cloud.config.v1.Deployment.LockState|keyof typeof google.cloud.config.v1.Deployment.LockState);

Deployment lockState.

### name
    
    
    public name: string;

Deployment name.

### providerConfig
    
    
    public providerConfig?: (google.cloud.config.v1.IProviderConfig|null);

Deployment providerConfig.

### quotaValidation
    
    
    public quotaValidation: (google.cloud.config.v1.QuotaValidation|keyof typeof google.cloud.config.v1.QuotaValidation);

Deployment quotaValidation.

### serviceAccount
    
    
    public serviceAccount?: (string|null);

Deployment serviceAccount.

### state
    
    
    public state: (google.cloud.config.v1.Deployment.State|keyof typeof google.cloud.config.v1.Deployment.State);

Deployment state.

### stateDetail
    
    
    public stateDetail: string;

Deployment stateDetail.

### terraformBlueprint
    
    
    public terraformBlueprint?: (google.cloud.config.v1.ITerraformBlueprint|null);

Deployment terraformBlueprint.

### tfErrors
    
    
    public tfErrors: google.cloud.config.v1.ITerraformError[];

Deployment tfErrors.

### tfVersion
    
    
    public tfVersion: string;

Deployment tfVersion.

### tfVersionConstraint
    
    
    public tfVersionConstraint?: (string|null);

Deployment tfVersionConstraint.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Deployment updateTime.

### workerPool
    
    
    public workerPool?: (string|null);

Deployment workerPool.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.config.v1.IDeployment): google.cloud.config.v1.Deployment;

Creates a new Deployment instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeployment](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideployment)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.deployment-class)` | Deployment instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.config.v1.Deployment;

Decodes a Deployment message from the specified reader or buffer.

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
`[Deployment](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.deployment-class)` | Deployment  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.config.v1.Deployment;

Decodes a Deployment message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.deployment-class)` | Deployment  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.config.v1.IDeployment, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Deployment message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeployment](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideployment)`   
Deployment message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.config.v1.IDeployment, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Deployment message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeployment](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideployment)`   
Deployment message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.config.v1.Deployment;

Creates a Deployment message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.deployment-class)` | Deployment  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Deployment

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

Converts this Deployment to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.config.v1.Deployment, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Deployment message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Deployment](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.deployment-class)`   
Deployment  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Deployment message.

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
