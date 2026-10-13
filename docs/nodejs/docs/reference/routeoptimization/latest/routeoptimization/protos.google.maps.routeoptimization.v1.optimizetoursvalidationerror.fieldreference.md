---
url: https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursvalidationerror.fieldreference
title: Class protos.google.maps.routeoptimization.v1.OptimizeToursValidationError.FieldReference (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:13:40.690684+00:00
---

# Class protos.google.maps.routeoptimization.v1.OptimizeToursValidationError.FieldReference (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursvalidationerror.fieldreference

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.routeoptimization.v1.OptimizeToursValidationError.FieldReference (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.3.0  0.2.0  0.1.0 

Represents a FieldReference.

## Implements

[protos.google.maps.routeoptimization.v1.OptimizeToursValidationError.IFieldReference](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursvalidationerror.ifieldreference)

## Package

[@googlemaps/routeoptimization](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.maps.routeoptimization.v1.OptimizeToursValidationError.IFieldReference);

Constructs a new FieldReference.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFieldReference](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursvalidationerror.ifieldreference)`   
Properties to set  
  
## Properties 

### index
    
    
    public index?: (number|null);

FieldReference index.

### indexOrKey
    
    
    public indexOrKey?: ("index"|"key");

FieldReference indexOrKey.

### key
    
    
    public key?: (string|null);

FieldReference key.

### name
    
    
    public name: string;

FieldReference name.

### subField
    
    
    public subField?: (google.maps.routeoptimization.v1.OptimizeToursValidationError.IFieldReference|null);

FieldReference subField.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.maps.routeoptimization.v1.OptimizeToursValidationError.IFieldReference): google.maps.routeoptimization.v1.OptimizeToursValidationError.FieldReference;

Creates a new FieldReference instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFieldReference](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursvalidationerror.ifieldreference)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FieldReference](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursvalidationerror.fieldreference)` | FieldReference instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.maps.routeoptimization.v1.OptimizeToursValidationError.FieldReference;

Decodes a FieldReference message from the specified reader or buffer.

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
`[FieldReference](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursvalidationerror.fieldreference)` | FieldReference  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.maps.routeoptimization.v1.OptimizeToursValidationError.FieldReference;

Decodes a FieldReference message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FieldReference](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursvalidationerror.fieldreference)` | FieldReference  
  
### encode(message, writer)
    
    
    public static encode(message: google.maps.routeoptimization.v1.OptimizeToursValidationError.IFieldReference, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FieldReference message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFieldReference](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursvalidationerror.ifieldreference)`   
FieldReference message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.maps.routeoptimization.v1.OptimizeToursValidationError.IFieldReference, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FieldReference message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFieldReference](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursvalidationerror.ifieldreference)`   
FieldReference message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.maps.routeoptimization.v1.OptimizeToursValidationError.FieldReference;

Creates a FieldReference message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FieldReference](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursvalidationerror.fieldreference)` | FieldReference  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FieldReference

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

Converts this FieldReference to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.maps.routeoptimization.v1.OptimizeToursValidationError.FieldReference, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FieldReference message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FieldReference](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.optimizetoursvalidationerror.fieldreference)`   
FieldReference  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FieldReference message.

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
