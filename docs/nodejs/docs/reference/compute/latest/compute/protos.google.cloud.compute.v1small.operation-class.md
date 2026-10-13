---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1small.operation-class
title: Class protos.google.cloud.compute.v1small.Operation (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:39.992623+00:00
---

# Class protos.google.cloud.compute.v1small.Operation (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1small.operation-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.compute.v1small.Operation (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

Represents an Operation.

## Implements

[protos.google.cloud.compute.v1small.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1small.ioperation)

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.compute.v1small.IOperation);

Constructs a new Operation.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1small.ioperation)`   
Properties to set  
  
## Properties 

### clientOperationId
    
    
    public clientOperationId?: (string|null);

Operation clientOperationId.

### creationTimestamp
    
    
    public creationTimestamp?: (string|null);

Operation creationTimestamp.

### description
    
    
    public description?: (string|null);

Operation description.

### endTime
    
    
    public endTime?: (string|null);

Operation endTime.

### error
    
    
    public error?: (google.cloud.compute.v1small.IError|null);

Operation error.

### httpErrorMessage
    
    
    public httpErrorMessage?: (string|null);

Operation httpErrorMessage.

### httpErrorStatusCode
    
    
    public httpErrorStatusCode?: (number|null);

Operation httpErrorStatusCode.

### id
    
    
    public id?: (number|Long|string|null);

Operation id.

### insertTime
    
    
    public insertTime?: (string|null);

Operation insertTime.

### kind
    
    
    public kind?: (string|null);

Operation kind.

### name
    
    
    public name?: (string|null);

Operation name.

### operationType
    
    
    public operationType?: (string|null);

Operation operationType.

### progress
    
    
    public progress?: (number|null);

Operation progress.

### region
    
    
    public region?: (string|null);

Operation region.

### selfLink
    
    
    public selfLink?: (string|null);

Operation selfLink.

### startTime
    
    
    public startTime?: (string|null);

Operation startTime.

### status
    
    
    public status?: (google.cloud.compute.v1small.Operation.Status|keyof typeof google.cloud.compute.v1small.Operation.Status|null);

Operation status.

### statusMessage
    
    
    public statusMessage?: (string|null);

Operation statusMessage.

### targetId
    
    
    public targetId?: (number|Long|string|null);

Operation targetId.

### targetLink
    
    
    public targetLink?: (string|null);

Operation targetLink.

### user
    
    
    public user?: (string|null);

Operation user.

### warnings
    
    
    public warnings: google.cloud.compute.v1small.IWarnings[];

Operation warnings.

### zone
    
    
    public zone?: (string|null);

Operation zone.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.compute.v1small.IOperation): google.cloud.compute.v1small.Operation;

Creates a new Operation instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1small.ioperation)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1small.operation-class)` | Operation instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.compute.v1small.Operation;

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
`[Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1small.operation-class)` | Operation  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.compute.v1small.Operation;

Decodes an Operation message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1small.operation-class)` | Operation  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.compute.v1small.IOperation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Operation message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1small.ioperation)`   
Operation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.compute.v1small.IOperation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Operation message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1small.ioperation)`   
Operation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.compute.v1small.Operation;

Creates an Operation message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1small.operation-class)` | Operation  
  
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
    
    
    public static toObject(message: google.cloud.compute.v1small.Operation, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Operation message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1small.operation-class)`   
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
