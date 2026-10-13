---
url: https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1.lifecyclepolicy-class
title: Class protos.google.cloud.batch.v1.LifecyclePolicy (3.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:18.163415+00:00
---

# Class protos.google.cloud.batch.v1.LifecyclePolicy (3.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1.lifecyclepolicy-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.batch.v1.LifecyclePolicy (3.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.1 (latest)  2.4.0  2.3.0  1.16.0  1.15.0  1.12.0  1.11.0  1.8.0  1.7.0  1.5.0  1.4.0  1.3.0  1.1.0  0.7.1  0.6.1  0.5.0  0.3.2 

Represents a LifecyclePolicy.

## Implements

[protos.google.cloud.batch.v1.ILifecyclePolicy](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1.ilifecyclepolicy)

## Package

[@google-cloud/batch](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.batch.v1.ILifecyclePolicy);

Constructs a new LifecyclePolicy.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILifecyclePolicy](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1.ilifecyclepolicy)`   
Properties to set  
  
## Properties 

### action
    
    
    public action: (google.cloud.batch.v1.LifecyclePolicy.Action|keyof typeof google.cloud.batch.v1.LifecyclePolicy.Action);

LifecyclePolicy action.

### actionCondition
    
    
    public actionCondition?: (google.cloud.batch.v1.LifecyclePolicy.IActionCondition|null);

LifecyclePolicy actionCondition.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.batch.v1.ILifecyclePolicy): google.cloud.batch.v1.LifecyclePolicy;

Creates a new LifecyclePolicy instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILifecyclePolicy](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1.ilifecyclepolicy)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[LifecyclePolicy](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1.lifecyclepolicy-class)` | LifecyclePolicy instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.batch.v1.LifecyclePolicy;

Decodes a LifecyclePolicy message from the specified reader or buffer.

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
`[LifecyclePolicy](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1.lifecyclepolicy-class)` | LifecyclePolicy  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.batch.v1.LifecyclePolicy;

Decodes a LifecyclePolicy message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[LifecyclePolicy](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1.lifecyclepolicy-class)` | LifecyclePolicy  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.batch.v1.ILifecyclePolicy, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LifecyclePolicy message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILifecyclePolicy](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1.ilifecyclepolicy)`   
LifecyclePolicy message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.batch.v1.ILifecyclePolicy, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LifecyclePolicy message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILifecyclePolicy](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1.ilifecyclepolicy)`   
LifecyclePolicy message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.batch.v1.LifecyclePolicy;

Creates a LifecyclePolicy message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[LifecyclePolicy](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1.lifecyclepolicy-class)` | LifecyclePolicy  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for LifecyclePolicy

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

Converts this LifecyclePolicy to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.batch.v1.LifecyclePolicy, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a LifecyclePolicy message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[LifecyclePolicy](https://docs.cloud.google.com/nodejs/docs/reference/batch/latest/batch/protos.google.cloud.batch.v1.lifecyclepolicy-class)`   
LifecyclePolicy  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a LifecyclePolicy message.

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
