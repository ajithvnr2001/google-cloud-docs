---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.guardrail.llmpolicy-class
title: Class protos.google.cloud.ces.v1.Guardrail.LlmPolicy (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:34.358781+00:00
---

# Class protos.google.cloud.ces.v1.Guardrail.LlmPolicy (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.guardrail.llmpolicy-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ces.v1.Guardrail.LlmPolicy (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Represents a LlmPolicy.

## Implements

[protos.google.cloud.ces.v1.Guardrail.ILlmPolicy](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.guardrail.illmpolicy)

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ces.v1.Guardrail.ILlmPolicy);

Constructs a new LlmPolicy.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILlmPolicy](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.guardrail.illmpolicy)`   
Properties to set  
  
## Properties 

### allowShortUtterance
    
    
    public allowShortUtterance: boolean;

LlmPolicy allowShortUtterance.

### failOpen
    
    
    public failOpen: boolean;

LlmPolicy failOpen.

### maxConversationMessages
    
    
    public maxConversationMessages: number;

LlmPolicy maxConversationMessages.

### modelSettings
    
    
    public modelSettings?: (google.cloud.ces.v1.IModelSettings|null);

LlmPolicy modelSettings.

### policyScope
    
    
    public policyScope: (google.cloud.ces.v1.Guardrail.LlmPolicy.PolicyScope|keyof typeof google.cloud.ces.v1.Guardrail.LlmPolicy.PolicyScope);

LlmPolicy policyScope.

### prompt
    
    
    public prompt: string;

LlmPolicy prompt.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ces.v1.Guardrail.ILlmPolicy): google.cloud.ces.v1.Guardrail.LlmPolicy;

Creates a new LlmPolicy instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILlmPolicy](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.guardrail.illmpolicy)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[LlmPolicy](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.guardrail.llmpolicy-class)` | LlmPolicy instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ces.v1.Guardrail.LlmPolicy;

Decodes a LlmPolicy message from the specified reader or buffer.

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
`[LlmPolicy](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.guardrail.llmpolicy-class)` | LlmPolicy  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ces.v1.Guardrail.LlmPolicy;

Decodes a LlmPolicy message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[LlmPolicy](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.guardrail.llmpolicy-class)` | LlmPolicy  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ces.v1.Guardrail.ILlmPolicy, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LlmPolicy message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILlmPolicy](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.guardrail.illmpolicy)`   
LlmPolicy message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ces.v1.Guardrail.ILlmPolicy, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LlmPolicy message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILlmPolicy](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.guardrail.illmpolicy)`   
LlmPolicy message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ces.v1.Guardrail.LlmPolicy;

Creates a LlmPolicy message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[LlmPolicy](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.guardrail.llmpolicy-class)` | LlmPolicy  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for LlmPolicy

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

Converts this LlmPolicy to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ces.v1.Guardrail.LlmPolicy, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a LlmPolicy message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[LlmPolicy](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.guardrail.llmpolicy-class)`   
LlmPolicy  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a LlmPolicy message.

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
