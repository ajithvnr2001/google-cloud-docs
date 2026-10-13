---
url: https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.preview-class
title: Class protos.google.cloud.config.v1.Preview (0.15.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:00.987751+00:00
---

# Class protos.google.cloud.config.v1.Preview (0.15.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.preview-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.config.v1.Preview (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.14.0  0.12.0  0.7.0  0.5.0  0.2.0  0.1.1 

Represents a Preview.

## Implements

[protos.google.cloud.config.v1.IPreview](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ipreview)

## Package

[@google-cloud/config](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.config.v1.IPreview);

Constructs a new Preview.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPreview](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ipreview)`   
Properties to set  
  
## Properties 

### annotations
    
    
    public annotations: { [k: string]: string };

Preview annotations.

### artifactsGcsBucket
    
    
    public artifactsGcsBucket?: (string|null);

Preview artifactsGcsBucket.

### blueprint
    
    
    public blueprint?: "terraformBlueprint";

Preview blueprint.

### build
    
    
    public build: string;

Preview build.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Preview createTime.

### deployment
    
    
    public deployment: string;

Preview deployment.

### errorCode
    
    
    public errorCode: (google.cloud.config.v1.Preview.ErrorCode|keyof typeof google.cloud.config.v1.Preview.ErrorCode);

Preview errorCode.

### errorLogs
    
    
    public errorLogs: string;

Preview errorLogs.

### errorStatus
    
    
    public errorStatus?: (google.rpc.IStatus|null);

Preview errorStatus.

### labels
    
    
    public labels: { [k: string]: string };

Preview labels.

### logs
    
    
    public logs: string;

Preview logs.

### name
    
    
    public name: string;

Preview name.

### previewArtifacts
    
    
    public previewArtifacts?: (google.cloud.config.v1.IPreviewArtifacts|null);

Preview previewArtifacts.

### previewMode
    
    
    public previewMode: (google.cloud.config.v1.Preview.PreviewMode|keyof typeof google.cloud.config.v1.Preview.PreviewMode);

Preview previewMode.

### providerConfig
    
    
    public providerConfig?: (google.cloud.config.v1.IProviderConfig|null);

Preview providerConfig.

### serviceAccount
    
    
    public serviceAccount: string;

Preview serviceAccount.

### state
    
    
    public state: (google.cloud.config.v1.Preview.State|keyof typeof google.cloud.config.v1.Preview.State);

Preview state.

### terraformBlueprint
    
    
    public terraformBlueprint?: (google.cloud.config.v1.ITerraformBlueprint|null);

Preview terraformBlueprint.

### tfErrors
    
    
    public tfErrors: google.cloud.config.v1.ITerraformError[];

Preview tfErrors.

### tfVersion
    
    
    public tfVersion: string;

Preview tfVersion.

### tfVersionConstraint
    
    
    public tfVersionConstraint?: (string|null);

Preview tfVersionConstraint.

### workerPool
    
    
    public workerPool?: (string|null);

Preview workerPool.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.config.v1.IPreview): google.cloud.config.v1.Preview;

Creates a new Preview instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPreview](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ipreview)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Preview](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.preview-class)` | Preview instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.config.v1.Preview;

Decodes a Preview message from the specified reader or buffer.

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
`[Preview](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.preview-class)` | Preview  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.config.v1.Preview;

Decodes a Preview message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Preview](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.preview-class)` | Preview  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.config.v1.IPreview, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Preview message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPreview](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ipreview)`   
Preview message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.config.v1.IPreview, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Preview message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPreview](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ipreview)`   
Preview message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.config.v1.Preview;

Creates a Preview message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Preview](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.preview-class)` | Preview  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Preview

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

Converts this Preview to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.config.v1.Preview, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Preview message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Preview](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.preview-class)`   
Preview  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Preview message.

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
