---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.gcrule.intersection
title: Class protos.google.bigtable.admin.v2.GcRule.Intersection (0.9.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:15.183313+00:00
---

# Class protos.google.bigtable.admin.v2.GcRule.Intersection (0.9.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.gcrule.intersection

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.bigtable.admin.v2.GcRule.Intersection (0.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.0 (latest)  0.8.0  0.2.0 

Represents an Intersection.

## Implements

[protos.google.bigtable.admin.v2.GcRule.IIntersection](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.gcrule.iintersection)

## Package

[@google-cloud/bigtable-api](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.bigtable.admin.v2.GcRule.IIntersection);

Constructs a new Intersection.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IIntersection](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.gcrule.iintersection)`   
Properties to set  
  
## Properties 

### rules
    
    
    public rules: google.bigtable.admin.v2.IGcRule[];

Intersection rules.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.bigtable.admin.v2.GcRule.IIntersection): google.bigtable.admin.v2.GcRule.Intersection;

Creates a new Intersection instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IIntersection](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.gcrule.iintersection)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Intersection](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.gcrule.intersection)` | Intersection instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.bigtable.admin.v2.GcRule.Intersection;

Decodes an Intersection message from the specified reader or buffer.

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
`[Intersection](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.gcrule.intersection)` | Intersection  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.bigtable.admin.v2.GcRule.Intersection;

Decodes an Intersection message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Intersection](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.gcrule.intersection)` | Intersection  
  
### encode(message, writer)
    
    
    public static encode(message: google.bigtable.admin.v2.GcRule.IIntersection, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Intersection message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IIntersection](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.gcrule.iintersection)`   
Intersection message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.bigtable.admin.v2.GcRule.IIntersection, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Intersection message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IIntersection](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.gcrule.iintersection)`   
Intersection message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.bigtable.admin.v2.GcRule.Intersection;

Creates an Intersection message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Intersection](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.gcrule.intersection)` | Intersection  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Intersection

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

Converts this Intersection to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.bigtable.admin.v2.GcRule.Intersection, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Intersection message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Intersection](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/bigtable-api/protos.google.bigtable.admin.v2.gcrule.intersection)`   
Intersection  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Intersection message.

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
