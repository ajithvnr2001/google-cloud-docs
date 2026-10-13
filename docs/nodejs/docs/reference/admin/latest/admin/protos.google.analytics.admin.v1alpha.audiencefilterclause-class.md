---
url: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.audiencefilterclause-class
title: Class protos.google.analytics.admin.v1alpha.AudienceFilterClause (10.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:42:20.610579+00:00
---

# Class protos.google.analytics.admin.v1alpha.AudienceFilterClause (10.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.audiencefilterclause-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.analytics.admin.v1alpha.AudienceFilterClause (10.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  10.1.0  9.2.0  7.6.0  7.3.0  4.6.0  4.5.1  4.4.0 

Represents an AudienceFilterClause.

## Implements

[protos.google.analytics.admin.v1alpha.IAudienceFilterClause](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iaudiencefilterclause)

## Package

[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.analytics.admin.v1alpha.IAudienceFilterClause);

Constructs a new AudienceFilterClause.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAudienceFilterClause](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iaudiencefilterclause)`   
Properties to set  
  
## Properties 

### clauseType
    
    
    public clauseType: (google.analytics.admin.v1alpha.AudienceFilterClause.AudienceClauseType|keyof typeof google.analytics.admin.v1alpha.AudienceFilterClause.AudienceClauseType);

AudienceFilterClause clauseType.

### filter
    
    
    public filter?: ("simpleFilter"|"sequenceFilter");

AudienceFilterClause filter.

### sequenceFilter
    
    
    public sequenceFilter?: (google.analytics.admin.v1alpha.IAudienceSequenceFilter|null);

AudienceFilterClause sequenceFilter.

### simpleFilter
    
    
    public simpleFilter?: (google.analytics.admin.v1alpha.IAudienceSimpleFilter|null);

AudienceFilterClause simpleFilter.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.analytics.admin.v1alpha.IAudienceFilterClause): google.analytics.admin.v1alpha.AudienceFilterClause;

Creates a new AudienceFilterClause instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAudienceFilterClause](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iaudiencefilterclause)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AudienceFilterClause](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.audiencefilterclause-class)` | AudienceFilterClause instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.analytics.admin.v1alpha.AudienceFilterClause;

Decodes an AudienceFilterClause message from the specified reader or buffer.

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
`[AudienceFilterClause](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.audiencefilterclause-class)` | AudienceFilterClause  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.analytics.admin.v1alpha.AudienceFilterClause;

Decodes an AudienceFilterClause message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AudienceFilterClause](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.audiencefilterclause-class)` | AudienceFilterClause  
  
### encode(message, writer)
    
    
    public static encode(message: google.analytics.admin.v1alpha.IAudienceFilterClause, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AudienceFilterClause message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAudienceFilterClause](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iaudiencefilterclause)`   
AudienceFilterClause message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.analytics.admin.v1alpha.IAudienceFilterClause, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AudienceFilterClause message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAudienceFilterClause](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iaudiencefilterclause)`   
AudienceFilterClause message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.analytics.admin.v1alpha.AudienceFilterClause;

Creates an AudienceFilterClause message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AudienceFilterClause](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.audiencefilterclause-class)` | AudienceFilterClause  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AudienceFilterClause

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

Converts this AudienceFilterClause to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.analytics.admin.v1alpha.AudienceFilterClause, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AudienceFilterClause message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AudienceFilterClause](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.audiencefilterclause-class)`   
AudienceFilterClause  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AudienceFilterClause message.

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
