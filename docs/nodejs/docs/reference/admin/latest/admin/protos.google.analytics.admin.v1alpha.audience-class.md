---
url: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.audience-class
title: Class protos.google.analytics.admin.v1alpha.Audience (10.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:42:19.455521+00:00
---

# Class protos.google.analytics.admin.v1alpha.Audience (10.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.audience-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.analytics.admin.v1alpha.Audience (10.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  10.1.0  9.2.0  7.6.0  7.3.0  4.6.0  4.5.1  4.4.0 

Represents an Audience.

## Implements

[protos.google.analytics.admin.v1alpha.IAudience](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iaudience)

## Package

[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.analytics.admin.v1alpha.IAudience);

Constructs a new Audience.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAudience](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iaudience)`   
Properties to set  
  
## Properties 

### adsPersonalizationEnabled
    
    
    public adsPersonalizationEnabled: boolean;

Audience adsPersonalizationEnabled.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Audience createTime.

### description
    
    
    public description: string;

Audience description.

### displayName
    
    
    public displayName: string;

Audience displayName.

### eventTrigger
    
    
    public eventTrigger?: (google.analytics.admin.v1alpha.IAudienceEventTrigger|null);

Audience eventTrigger.

### exclusionDurationMode
    
    
    public exclusionDurationMode: (google.analytics.admin.v1alpha.Audience.AudienceExclusionDurationMode|keyof typeof google.analytics.admin.v1alpha.Audience.AudienceExclusionDurationMode);

Audience exclusionDurationMode.

### filterClauses
    
    
    public filterClauses: google.analytics.admin.v1alpha.IAudienceFilterClause[];

Audience filterClauses.

### membershipDurationDays
    
    
    public membershipDurationDays: number;

Audience membershipDurationDays.

### name
    
    
    public name: string;

Audience name.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.analytics.admin.v1alpha.IAudience): google.analytics.admin.v1alpha.Audience;

Creates a new Audience instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAudience](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iaudience)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Audience](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.audience-class)` | Audience instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.analytics.admin.v1alpha.Audience;

Decodes an Audience message from the specified reader or buffer.

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
`[Audience](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.audience-class)` | Audience  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.analytics.admin.v1alpha.Audience;

Decodes an Audience message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Audience](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.audience-class)` | Audience  
  
### encode(message, writer)
    
    
    public static encode(message: google.analytics.admin.v1alpha.IAudience, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Audience message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAudience](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iaudience)`   
Audience message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.analytics.admin.v1alpha.IAudience, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Audience message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAudience](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iaudience)`   
Audience message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.analytics.admin.v1alpha.Audience;

Creates an Audience message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Audience](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.audience-class)` | Audience  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Audience

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

Converts this Audience to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.analytics.admin.v1alpha.Audience, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Audience message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Audience](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.audience-class)`   
Audience  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Audience message.

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
