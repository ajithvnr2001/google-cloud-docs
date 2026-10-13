---
url: https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3.conditioncontext-class
title: Class protos.google.cloud.policytroubleshooter.iam.v3.ConditionContext (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:04.343261+00:00
---

# Class protos.google.cloud.policytroubleshooter.iam.v3.ConditionContext (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3.conditioncontext-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.policytroubleshooter.iam.v3.ConditionContext (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.7.0  0.6.1 

Represents a ConditionContext.

## Implements

[protos.google.cloud.policytroubleshooter.iam.v3.IConditionContext](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3.iconditioncontext)

## Package

[@google-cloud/policy-troubleshooter-iam](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.policytroubleshooter.iam.v3.IConditionContext);

Constructs a new ConditionContext.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConditionContext](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3.iconditioncontext)`   
Properties to set  
  
## Properties 

### destination
    
    
    public destination?: (google.cloud.policytroubleshooter.iam.v3.ConditionContext.IPeer|null);

ConditionContext destination.

### effectiveTags
    
    
    public effectiveTags: google.cloud.policytroubleshooter.iam.v3.ConditionContext.IEffectiveTag[];

ConditionContext effectiveTags.

### request
    
    
    public request?: (google.cloud.policytroubleshooter.iam.v3.ConditionContext.IRequest|null);

ConditionContext request.

### resource
    
    
    public resource?: (google.cloud.policytroubleshooter.iam.v3.ConditionContext.IResource|null);

ConditionContext resource.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.policytroubleshooter.iam.v3.IConditionContext): google.cloud.policytroubleshooter.iam.v3.ConditionContext;

Creates a new ConditionContext instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConditionContext](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3.iconditioncontext)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ConditionContext](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3.conditioncontext-class)` | ConditionContext instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.policytroubleshooter.iam.v3.ConditionContext;

Decodes a ConditionContext message from the specified reader or buffer.

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
`[ConditionContext](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3.conditioncontext-class)` | ConditionContext  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.policytroubleshooter.iam.v3.ConditionContext;

Decodes a ConditionContext message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ConditionContext](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3.conditioncontext-class)` | ConditionContext  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.policytroubleshooter.iam.v3.IConditionContext, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ConditionContext message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConditionContext](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3.iconditioncontext)`   
ConditionContext message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.policytroubleshooter.iam.v3.IConditionContext, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ConditionContext message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConditionContext](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3.iconditioncontext)`   
ConditionContext message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.policytroubleshooter.iam.v3.ConditionContext;

Creates a ConditionContext message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ConditionContext](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3.conditioncontext-class)` | ConditionContext  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ConditionContext

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

Converts this ConditionContext to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.policytroubleshooter.iam.v3.ConditionContext, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ConditionContext message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ConditionContext](https://docs.cloud.google.com/nodejs/docs/reference/policy-troubleshooter-iam/latest/policy-troubleshooter-iam/protos.google.cloud.policytroubleshooter.iam.v3.conditioncontext-class)`   
ConditionContext  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ConditionContext message.

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
