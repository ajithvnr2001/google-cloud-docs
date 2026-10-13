---
url: https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.template.templatemetadata-class
title: Class protos.google.cloud.modelarmor.v1.Template.TemplateMetadata (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:11:56.087801+00:00
---

# Class protos.google.cloud.modelarmor.v1.Template.TemplateMetadata (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.template.templatemetadata-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.modelarmor.v1.Template.TemplateMetadata (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0 

Represents a TemplateMetadata.

## Implements

[protos.google.cloud.modelarmor.v1.Template.ITemplateMetadata](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.template.itemplatemetadata)

## Package

[@google-cloud/modelarmor](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.modelarmor.v1.Template.ITemplateMetadata);

Constructs a new TemplateMetadata.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ITemplateMetadata](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.template.itemplatemetadata)`   
Properties to set  
  
## Properties 

### customLlmResponseSafetyErrorCode
    
    
    public customLlmResponseSafetyErrorCode: number;

TemplateMetadata customLlmResponseSafetyErrorCode.

### customLlmResponseSafetyErrorMessage
    
    
    public customLlmResponseSafetyErrorMessage: string;

TemplateMetadata customLlmResponseSafetyErrorMessage.

### customPromptSafetyErrorCode
    
    
    public customPromptSafetyErrorCode: number;

TemplateMetadata customPromptSafetyErrorCode.

### customPromptSafetyErrorMessage
    
    
    public customPromptSafetyErrorMessage: string;

TemplateMetadata customPromptSafetyErrorMessage.

### enforcementType
    
    
    public enforcementType: (google.cloud.modelarmor.v1.Template.TemplateMetadata.EnforcementType|keyof typeof google.cloud.modelarmor.v1.Template.TemplateMetadata.EnforcementType);

TemplateMetadata enforcementType.

### ignorePartialInvocationFailures
    
    
    public ignorePartialInvocationFailures: boolean;

TemplateMetadata ignorePartialInvocationFailures.

### logSanitizeOperations
    
    
    public logSanitizeOperations: boolean;

TemplateMetadata logSanitizeOperations.

### logTemplateOperations
    
    
    public logTemplateOperations: boolean;

TemplateMetadata logTemplateOperations.

### modalities
    
    
    public modalities: google.cloud.modelarmor.v1.Modality[];

TemplateMetadata modalities.

### multiLanguageDetection
    
    
    public multiLanguageDetection?: (google.cloud.modelarmor.v1.Template.TemplateMetadata.IMultiLanguageDetection|null);

TemplateMetadata multiLanguageDetection.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.modelarmor.v1.Template.ITemplateMetadata): google.cloud.modelarmor.v1.Template.TemplateMetadata;

Creates a new TemplateMetadata instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ITemplateMetadata](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.template.itemplatemetadata)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[TemplateMetadata](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.template.templatemetadata-class)` | TemplateMetadata instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.modelarmor.v1.Template.TemplateMetadata;

Decodes a TemplateMetadata message from the specified reader or buffer.

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
`[TemplateMetadata](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.template.templatemetadata-class)` | TemplateMetadata  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.modelarmor.v1.Template.TemplateMetadata;

Decodes a TemplateMetadata message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[TemplateMetadata](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.template.templatemetadata-class)` | TemplateMetadata  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.modelarmor.v1.Template.ITemplateMetadata, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified TemplateMetadata message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ITemplateMetadata](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.template.itemplatemetadata)`   
TemplateMetadata message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.modelarmor.v1.Template.ITemplateMetadata, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified TemplateMetadata message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ITemplateMetadata](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.template.itemplatemetadata)`   
TemplateMetadata message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.modelarmor.v1.Template.TemplateMetadata;

Creates a TemplateMetadata message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[TemplateMetadata](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.template.templatemetadata-class)` | TemplateMetadata  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for TemplateMetadata

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

Converts this TemplateMetadata to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.modelarmor.v1.Template.TemplateMetadata, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a TemplateMetadata message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[TemplateMetadata](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.template.templatemetadata-class)`   
TemplateMetadata  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a TemplateMetadata message.

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
