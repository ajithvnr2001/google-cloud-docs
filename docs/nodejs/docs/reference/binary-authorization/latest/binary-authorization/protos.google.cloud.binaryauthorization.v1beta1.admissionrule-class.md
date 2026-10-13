---
url: https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.admissionrule-class
title: Class protos.google.cloud.binaryauthorization.v1beta1.AdmissionRule (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:32.507695+00:00
---

# Class protos.google.cloud.binaryauthorization.v1beta1.AdmissionRule (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.admissionrule-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.binaryauthorization.v1beta1.AdmissionRule (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.5.0  4.4.0  4.2.0  3.7.0  2.5.0  2.2.1  2.1.1  1.5.1  1.4.0  1.3.0  1.2.0  1.1.6 

Represents an AdmissionRule.

## Implements

[protos.google.cloud.binaryauthorization.v1beta1.IAdmissionRule](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iadmissionrule)

## Package

[@google-cloud/binary-authorization](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.binaryauthorization.v1beta1.IAdmissionRule);

Constructs a new AdmissionRule.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAdmissionRule](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iadmissionrule)`   
Properties to set  
  
## Properties 

### enforcementMode
    
    
    public enforcementMode: (google.cloud.binaryauthorization.v1beta1.AdmissionRule.EnforcementMode|keyof typeof google.cloud.binaryauthorization.v1beta1.AdmissionRule.EnforcementMode);

AdmissionRule enforcementMode.

### evaluationMode
    
    
    public evaluationMode: (google.cloud.binaryauthorization.v1beta1.AdmissionRule.EvaluationMode|keyof typeof google.cloud.binaryauthorization.v1beta1.AdmissionRule.EvaluationMode);

AdmissionRule evaluationMode.

### requireAttestationsBy
    
    
    public requireAttestationsBy: string[];

AdmissionRule requireAttestationsBy.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.binaryauthorization.v1beta1.IAdmissionRule): google.cloud.binaryauthorization.v1beta1.AdmissionRule;

Creates a new AdmissionRule instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAdmissionRule](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iadmissionrule)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AdmissionRule](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.admissionrule-class)` | AdmissionRule instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.binaryauthorization.v1beta1.AdmissionRule;

Decodes an AdmissionRule message from the specified reader or buffer.

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
`[AdmissionRule](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.admissionrule-class)` | AdmissionRule  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.binaryauthorization.v1beta1.AdmissionRule;

Decodes an AdmissionRule message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AdmissionRule](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.admissionrule-class)` | AdmissionRule  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.binaryauthorization.v1beta1.IAdmissionRule, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AdmissionRule message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAdmissionRule](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iadmissionrule)`   
AdmissionRule message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.binaryauthorization.v1beta1.IAdmissionRule, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AdmissionRule message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAdmissionRule](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iadmissionrule)`   
AdmissionRule message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.binaryauthorization.v1beta1.AdmissionRule;

Creates an AdmissionRule message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AdmissionRule](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.admissionrule-class)` | AdmissionRule  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AdmissionRule

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

Converts this AdmissionRule to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.binaryauthorization.v1beta1.AdmissionRule, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AdmissionRule message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AdmissionRule](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.admissionrule-class)`   
AdmissionRule  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AdmissionRule message.

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
