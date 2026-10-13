---
url: https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2.function-class
title: Class protos.google.cloud.functions.v2.Function (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:39.094297+00:00
---

# Class protos.google.cloud.functions.v2.Function (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2.function-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.functions.v2.Function (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  4.0.1  3.6.0  3.3.0  3.1.0  2.4.1  2.3.1  2.2.3  1.2.0  1.1.9 

Represents a Function.

## Implements

[protos.google.cloud.functions.v2.IFunction](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2.ifunction)

## Package

[@google-cloud/functions](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.functions.v2.IFunction);

Constructs a new Function.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFunction](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2.ifunction)`   
Properties to set  
  
## Properties 

### buildConfig
    
    
    public buildConfig?: (google.cloud.functions.v2.IBuildConfig|null);

Function buildConfig.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Function createTime.

### description
    
    
    public description: string;

Function description.

### environment
    
    
    public environment: (google.cloud.functions.v2.Environment|keyof typeof google.cloud.functions.v2.Environment);

Function environment.

### eventTrigger
    
    
    public eventTrigger?: (google.cloud.functions.v2.IEventTrigger|null);

Function eventTrigger.

### kmsKeyName
    
    
    public kmsKeyName: string;

Function kmsKeyName.

### labels
    
    
    public labels: { [k: string]: string };

Function labels.

### name
    
    
    public name: string;

Function name.

### satisfiesPzs
    
    
    public satisfiesPzs: boolean;

Function satisfiesPzs.

### serviceConfig
    
    
    public serviceConfig?: (google.cloud.functions.v2.IServiceConfig|null);

Function serviceConfig.

### state
    
    
    public state: (google.cloud.functions.v2.Function.State|keyof typeof google.cloud.functions.v2.Function.State);

Function state.

### stateMessages
    
    
    public stateMessages: google.cloud.functions.v2.IStateMessage[];

Function stateMessages.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Function updateTime.

### url
    
    
    public url: string;

Function url.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.functions.v2.IFunction): google.cloud.functions.v2.Function;

Creates a new Function instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFunction](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2.ifunction)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Function](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2.function-class)` | Function instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.functions.v2.Function;

Decodes a Function message from the specified reader or buffer.

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
`[Function](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2.function-class)` | Function  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.functions.v2.Function;

Decodes a Function message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Function](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2.function-class)` | Function  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.functions.v2.IFunction, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Function message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFunction](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2.ifunction)`   
Function message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.functions.v2.IFunction, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Function message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFunction](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2.ifunction)`   
Function message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.functions.v2.Function;

Creates a Function message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Function](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2.function-class)` | Function  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Function

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

Converts this Function to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.functions.v2.Function, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Function message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Function](https://docs.cloud.google.com/nodejs/docs/reference/functions/latest/functions/protos.google.cloud.functions.v2.function-class)`   
Function  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Function message.

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
