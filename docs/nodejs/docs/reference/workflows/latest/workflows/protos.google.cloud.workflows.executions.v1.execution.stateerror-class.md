---
url: https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.execution.stateerror-class
title: Class protos.google.cloud.workflows.executions.v1.Execution.StateError (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:00.856397+00:00
---

# Class protos.google.cloud.workflows.executions.v1.Execution.StateError (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.execution.stateerror-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.workflows.executions.v1.Execution.StateError (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  4.3.0  3.1.1  2.3.2  2.2.0  1.4.0  1.3.1  1.2.6 

Represents a StateError.

## Implements

[protos.google.cloud.workflows.executions.v1.Execution.IStateError](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.execution.istateerror)

## Package

[@google-cloud/workflows](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.workflows.executions.v1.Execution.IStateError);

Constructs a new StateError.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IStateError](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.execution.istateerror)`   
Properties to set  
  
## Properties 

### details
    
    
    public details: string;

StateError details.

### type
    
    
    public type: (google.cloud.workflows.executions.v1.Execution.StateError.Type|keyof typeof google.cloud.workflows.executions.v1.Execution.StateError.Type);

StateError type.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.workflows.executions.v1.Execution.IStateError): google.cloud.workflows.executions.v1.Execution.StateError;

Creates a new StateError instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IStateError](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.execution.istateerror)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[StateError](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.execution.stateerror-class)` | StateError instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.workflows.executions.v1.Execution.StateError;

Decodes a StateError message from the specified reader or buffer.

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
`[StateError](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.execution.stateerror-class)` | StateError  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.workflows.executions.v1.Execution.StateError;

Decodes a StateError message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[StateError](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.execution.stateerror-class)` | StateError  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.workflows.executions.v1.Execution.IStateError, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified StateError message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IStateError](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.execution.istateerror)`   
StateError message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.workflows.executions.v1.Execution.IStateError, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified StateError message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IStateError](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.execution.istateerror)`   
StateError message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.workflows.executions.v1.Execution.StateError;

Creates a StateError message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[StateError](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.execution.stateerror-class)` | StateError  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for StateError

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

Converts this StateError to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.workflows.executions.v1.Execution.StateError, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a StateError message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[StateError](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.execution.stateerror-class)`   
StateError  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a StateError message.

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
