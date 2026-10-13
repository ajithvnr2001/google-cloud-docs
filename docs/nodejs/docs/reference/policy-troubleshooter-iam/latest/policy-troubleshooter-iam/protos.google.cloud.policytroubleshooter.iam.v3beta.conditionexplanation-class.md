---
url: https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3beta.conditionexplanation-class
title: Class protos.google.cloud.policytroubleshooter.iam.v3beta.ConditionExplanation (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:15.837515+00:00
---

# Class protos.google.cloud.policytroubleshooter.iam.v3beta.ConditionExplanation (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3beta.conditionexplanation-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.policytroubleshooter.iam.v3beta.ConditionExplanation (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.7.0  0.6.1 

Represents a ConditionExplanation.

## Implements

[protos.google.cloud.policytroubleshooter.iam.v3beta.IConditionExplanation](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3beta.iconditionexplanation)

## Package

[@google-cloud/policy-troubleshooter-iam](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.policytroubleshooter.iam.v3beta.IConditionExplanation);

Constructs a new ConditionExplanation.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConditionExplanation](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3beta.iconditionexplanation)`   
Properties to set  
  
## Properties 

### errors
    
    
    public errors: google.rpc.IStatus[];

ConditionExplanation errors.

### evaluationStates
    
    
    public evaluationStates: google.cloud.policytroubleshooter.iam.v3beta.ConditionExplanation.IEvaluationState[];

ConditionExplanation evaluationStates.

### value
    
    
    public value?: (google.protobuf.IValue|null);

ConditionExplanation value.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.policytroubleshooter.iam.v3beta.IConditionExplanation): google.cloud.policytroubleshooter.iam.v3beta.ConditionExplanation;

Creates a new ConditionExplanation instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConditionExplanation](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3beta.iconditionexplanation)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ConditionExplanation](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3beta.conditionexplanation-class)` | ConditionExplanation instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.policytroubleshooter.iam.v3beta.ConditionExplanation;

Decodes a ConditionExplanation message from the specified reader or buffer.

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
`[ConditionExplanation](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3beta.conditionexplanation-class)` | ConditionExplanation  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.policytroubleshooter.iam.v3beta.ConditionExplanation;

Decodes a ConditionExplanation message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ConditionExplanation](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3beta.conditionexplanation-class)` | ConditionExplanation  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.policytroubleshooter.iam.v3beta.IConditionExplanation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ConditionExplanation message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConditionExplanation](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3beta.iconditionexplanation)`   
ConditionExplanation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.policytroubleshooter.iam.v3beta.IConditionExplanation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ConditionExplanation message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConditionExplanation](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3beta.iconditionexplanation)`   
ConditionExplanation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.policytroubleshooter.iam.v3beta.ConditionExplanation;

Creates a ConditionExplanation message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ConditionExplanation](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3beta.conditionexplanation-class)` | ConditionExplanation  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ConditionExplanation

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

Converts this ConditionExplanation to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.policytroubleshooter.iam.v3beta.ConditionExplanation, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ConditionExplanation message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ConditionExplanation](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3beta.conditionexplanation-class)`   
ConditionExplanation  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ConditionExplanation message.

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
