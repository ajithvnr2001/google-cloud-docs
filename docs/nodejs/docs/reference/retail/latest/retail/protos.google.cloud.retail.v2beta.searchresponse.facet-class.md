---
url: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.searchresponse.facet-class
title: Class protos.google.cloud.retail.v2beta.SearchResponse.Facet (5.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:39.298630+00:00
---

# Class protos.google.cloud.retail.v2beta.SearchResponse.Facet (5.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.searchresponse.facet-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.retail.v2beta.SearchResponse.Facet (5.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.4.0 (latest)  5.3.1  5.0.1  4.4.0  4.3.0  3.6.0  3.5.0  3.1.0  2.4.1  2.3.1  2.1.1  2.0.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.2  1.1.6 

Represents a Facet.

## Implements

[protos.google.cloud.retail.v2beta.SearchResponse.IFacet](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.searchresponse.ifacet)

## Package

[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.retail.v2beta.SearchResponse.IFacet);

Constructs a new Facet.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFacet](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.searchresponse.ifacet)`   
Properties to set  
  
## Properties 

### dynamicFacet
    
    
    public dynamicFacet: boolean;

Facet dynamicFacet.

### key
    
    
    public key: string;

Facet key.

### values
    
    
    public values: google.cloud.retail.v2beta.SearchResponse.Facet.IFacetValue[];

Facet values.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.retail.v2beta.SearchResponse.IFacet): google.cloud.retail.v2beta.SearchResponse.Facet;

Creates a new Facet instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFacet](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.searchresponse.ifacet)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Facet](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.searchresponse.facet-class)` | Facet instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.retail.v2beta.SearchResponse.Facet;

Decodes a Facet message from the specified reader or buffer.

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
`[Facet](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.searchresponse.facet-class)` | Facet  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.retail.v2beta.SearchResponse.Facet;

Decodes a Facet message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Facet](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.searchresponse.facet-class)` | Facet  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.retail.v2beta.SearchResponse.IFacet, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Facet message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFacet](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.searchresponse.ifacet)`   
Facet message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.retail.v2beta.SearchResponse.IFacet, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Facet message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFacet](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.searchresponse.ifacet)`   
Facet message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.retail.v2beta.SearchResponse.Facet;

Creates a Facet message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Facet](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.searchresponse.facet-class)` | Facet  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Facet

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

Converts this Facet to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.retail.v2beta.SearchResponse.Facet, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Facet message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Facet](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.searchresponse.facet-class)`   
Facet  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Facet message.

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
