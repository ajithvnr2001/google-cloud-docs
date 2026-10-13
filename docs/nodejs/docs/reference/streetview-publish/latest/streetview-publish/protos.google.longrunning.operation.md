---
url: https://docs.cloud.google.com/nodejs/docs/reference/streetview-publish/latest/streetview-publish/protos.google.longrunning.operation
title: Class protos.google.longrunning.Operation (0.5.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:30.967080+00:00
---

# Class protos.google.longrunning.Operation (0.5.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/streetview-publish/latest/streetview-publish/protos.google.longrunning.operation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.longrunning.Operation (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.3.0  0.2.1  0.1.0 

Represents an Operation.

## Implements

[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/streetview-publish/latest/streetview-publish/protos.google.longrunning.ioperation)

## Package

[@googlemaps/streetview-publish](https://docs.cloud.google.com/nodejs/docs/reference/streetview-publish/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.longrunning.IOperation);

Constructs a new Operation.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOperation](https://docs.cloud.google.com/nodejs/docs/reference/streetview-publish/latest/streetview-publish/protos.google.longrunning.ioperation)`   
Properties to set  
  
## Properties 

### done
    
    
    public done: boolean;

Operation done.

### error
    
    
    public error?: (google.rpc.IStatus|null);

Operation error.

### metadata
    
    
    public metadata?: (google.protobuf.IAny|null);

Operation metadata.

### name
    
    
    public name: string;

Operation name.

### response
    
    
    public response?: (google.protobuf.IAny|null);

Operation response.

### result
    
    
    public result?: ("error"|"response");

Operation result.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.longrunning.IOperation): google.longrunning.Operation;

Creates a new Operation instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOperation](https://docs.cloud.google.com/nodejs/docs/reference/streetview-publish/latest/streetview-publish/protos.google.longrunning.ioperation)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/nodejs/docs/reference/streetview-publish/latest/streetview-publish/protos.google.longrunning.operation)` | Operation instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.longrunning.Operation;

Decodes an Operation message from the specified reader or buffer.

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
`[Operation](https://docs.cloud.google.com/nodejs/docs/reference/streetview-publish/latest/streetview-publish/protos.google.longrunning.operation)` | Operation  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.longrunning.Operation;

Decodes an Operation message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/nodejs/docs/reference/streetview-publish/latest/streetview-publish/protos.google.longrunning.operation)` | Operation  
  
### encode(message, writer)
    
    
    public static encode(message: google.longrunning.IOperation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Operation message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOperation](https://docs.cloud.google.com/nodejs/docs/reference/streetview-publish/latest/streetview-publish/protos.google.longrunning.ioperation)`   
Operation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.longrunning.IOperation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Operation message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOperation](https://docs.cloud.google.com/nodejs/docs/reference/streetview-publish/latest/streetview-publish/protos.google.longrunning.ioperation)`   
Operation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.longrunning.Operation;

Creates an Operation message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/nodejs/docs/reference/streetview-publish/latest/streetview-publish/protos.google.longrunning.operation)` | Operation  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Operation

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

Converts this Operation to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.longrunning.Operation, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Operation message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Operation](https://docs.cloud.google.com/nodejs/docs/reference/streetview-publish/latest/streetview-publish/protos.google.longrunning.operation)`   
Operation  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Operation message.

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
