---
url: https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.validation-class
title: Class protos.google.cloud.datastream.v1alpha1.Validation (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:53.747743+00:00
---

# Class protos.google.cloud.datastream.v1alpha1.Validation (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.validation-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.datastream.v1alpha1.Validation (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.0.1  3.4.0  3.3.0  3.1.0  2.2.2  2.1.2  1.1.0  1.0.0  0.2.0 

Represents a Validation.

## Implements

[protos.google.cloud.datastream.v1alpha1.IValidation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ivalidation)

## Package

[@google-cloud/datastream](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.datastream.v1alpha1.IValidation);

Constructs a new Validation.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IValidation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ivalidation)`   
Properties to set  
  
## Properties 

### code
    
    
    public code: string;

Validation code.

### description
    
    
    public description: string;

Validation description.

### message
    
    
    public message: google.cloud.datastream.v1alpha1.IValidationMessage[];

Validation message.

### status
    
    
    public status: (google.cloud.datastream.v1alpha1.Validation.Status|keyof typeof google.cloud.datastream.v1alpha1.Validation.Status);

Validation status.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.datastream.v1alpha1.IValidation): google.cloud.datastream.v1alpha1.Validation;

Creates a new Validation instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IValidation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ivalidation)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Validation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.validation-class)` | Validation instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.datastream.v1alpha1.Validation;

Decodes a Validation message from the specified reader or buffer.

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
`[Validation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.validation-class)` | Validation  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.datastream.v1alpha1.Validation;

Decodes a Validation message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Validation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.validation-class)` | Validation  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.datastream.v1alpha1.IValidation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Validation message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IValidation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ivalidation)`   
Validation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.datastream.v1alpha1.IValidation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Validation message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IValidation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ivalidation)`   
Validation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.datastream.v1alpha1.Validation;

Creates a Validation message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Validation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.validation-class)` | Validation  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Validation

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

Converts this Validation to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.datastream.v1alpha1.Validation, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Validation message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Validation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.validation-class)`   
Validation  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Validation message.

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
