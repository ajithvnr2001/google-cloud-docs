---
url: https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.protobuf.value
title: Class protos.google.protobuf.Value (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:37:01.222794+00:00
---

# Class protos.google.protobuf.Value (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.protobuf.value

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.protobuf.Value (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  4.2.2  4.1.2  3.3.0  3.2.8 

Represents a Value.

## Implements

[protos.google.protobuf.IValue](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.protobuf.ivalue)

## Package

[@google-cloud/billing-budgets](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.protobuf.IValue);

Constructs a new Value.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IValue](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.protobuf.ivalue)`   
Properties to set  
  
## Properties 

### boolValue
    
    
    public boolValue?: (boolean|null);

Value boolValue.

### kind
    
    
    public kind?: ("nullValue"|"numberValue"|"stringValue"|"boolValue"|"structValue"|"listValue");

Value kind.

### listValue
    
    
    public listValue?: (google.protobuf.IListValue|null);

Value listValue.

### nullValue
    
    
    public nullValue?: (google.protobuf.NullValue|keyof typeof google.protobuf.NullValue|null);

Value nullValue.

### numberValue
    
    
    public numberValue?: (number|null);

Value numberValue.

### stringValue
    
    
    public stringValue?: (string|null);

Value stringValue.

### structValue
    
    
    public structValue?: (google.protobuf.IStruct|null);

Value structValue.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.protobuf.IValue): google.protobuf.Value;

Creates a new Value instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IValue](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.protobuf.ivalue)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Value](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.protobuf.value)` | Value instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.protobuf.Value;

Decodes a Value message from the specified reader or buffer.

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
`[Value](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.protobuf.value)` | Value  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.protobuf.Value;

Decodes a Value message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Value](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.protobuf.value)` | Value  
  
### encode(message, writer)
    
    
    public static encode(message: google.protobuf.IValue, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Value message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IValue](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.protobuf.ivalue)`   
Value message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.protobuf.IValue, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Value message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IValue](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.protobuf.ivalue)`   
Value message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.protobuf.Value;

Creates a Value message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Value](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.protobuf.value)` | Value  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Value

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

Converts this Value to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.protobuf.Value, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Value message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Value](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.protobuf.value)`   
Value  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Value message.

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
