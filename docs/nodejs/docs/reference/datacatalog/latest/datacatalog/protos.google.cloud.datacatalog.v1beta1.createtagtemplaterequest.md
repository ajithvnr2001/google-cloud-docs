---
url: https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1beta1.createtagtemplaterequest
title: Class protos.google.cloud.datacatalog.v1beta1.CreateTagTemplateRequest (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:17.941211+00:00
---

# Class protos.google.cloud.datacatalog.v1beta1.CreateTagTemplateRequest (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1beta1.createtagtemplaterequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.datacatalog.v1beta1.CreateTagTemplateRequest (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  4.7.0  4.6.0  4.5.0  4.1.1  3.3.1  3.2.1  2.5.0  2.4.2  2.3.4 

Represents a CreateTagTemplateRequest.

## Implements

[protos.google.cloud.datacatalog.v1beta1.ICreateTagTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1beta1.icreatetagtemplaterequest)

## Package

[@google-cloud/datacatalog](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.datacatalog.v1beta1.ICreateTagTemplateRequest);

Constructs a new CreateTagTemplateRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateTagTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1beta1.icreatetagtemplaterequest)`   
Properties to set  
  
## Properties 

### parent
    
    
    public parent: string;

CreateTagTemplateRequest parent.

### tagTemplate
    
    
    public tagTemplate?: (google.cloud.datacatalog.v1beta1.ITagTemplate|null);

CreateTagTemplateRequest tagTemplate.

### tagTemplateId
    
    
    public tagTemplateId: string;

CreateTagTemplateRequest tagTemplateId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.datacatalog.v1beta1.ICreateTagTemplateRequest): google.cloud.datacatalog.v1beta1.CreateTagTemplateRequest;

Creates a new CreateTagTemplateRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateTagTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1beta1.icreatetagtemplaterequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CreateTagTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1beta1.createtagtemplaterequest)` | CreateTagTemplateRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.datacatalog.v1beta1.CreateTagTemplateRequest;

Decodes a CreateTagTemplateRequest message from the specified reader or buffer.

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
`[CreateTagTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1beta1.createtagtemplaterequest)` | CreateTagTemplateRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.datacatalog.v1beta1.CreateTagTemplateRequest;

Decodes a CreateTagTemplateRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CreateTagTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1beta1.createtagtemplaterequest)` | CreateTagTemplateRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.datacatalog.v1beta1.ICreateTagTemplateRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateTagTemplateRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateTagTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1beta1.icreatetagtemplaterequest)`   
CreateTagTemplateRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.datacatalog.v1beta1.ICreateTagTemplateRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateTagTemplateRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateTagTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1beta1.icreatetagtemplaterequest)`   
CreateTagTemplateRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.datacatalog.v1beta1.CreateTagTemplateRequest;

Creates a CreateTagTemplateRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CreateTagTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1beta1.createtagtemplaterequest)` | CreateTagTemplateRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CreateTagTemplateRequest

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

Converts this CreateTagTemplateRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.datacatalog.v1beta1.CreateTagTemplateRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CreateTagTemplateRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CreateTagTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1beta1.createtagtemplaterequest)`   
CreateTagTemplateRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CreateTagTemplateRequest message.

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
