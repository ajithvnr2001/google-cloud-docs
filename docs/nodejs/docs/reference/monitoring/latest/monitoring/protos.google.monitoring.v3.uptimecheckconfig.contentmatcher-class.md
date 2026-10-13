---
url: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.contentmatcher-class
title: Class protos.google.monitoring.v3.UptimeCheckConfig.ContentMatcher (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:50.489362+00:00
---

# Class protos.google.monitoring.v3.UptimeCheckConfig.ContentMatcher (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.contentmatcher-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.monitoring.v3.UptimeCheckConfig.ContentMatcher (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.4.0  5.2.0  4.0.0  3.0.4  2.3.5 

Represents a ContentMatcher.

## Implements

[protos.google.monitoring.v3.UptimeCheckConfig.IContentMatcher](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.icontentmatcher)

## Package

[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.monitoring.v3.UptimeCheckConfig.IContentMatcher);

Constructs a new ContentMatcher.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IContentMatcher](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.icontentmatcher)`   
Properties to set  
  
## Properties 

### additionalMatcherInfo
    
    
    public additionalMatcherInfo?: "jsonPathMatcher";

ContentMatcher additionalMatcherInfo.

### content
    
    
    public content: string;

ContentMatcher content.

### jsonPathMatcher
    
    
    public jsonPathMatcher?: (google.monitoring.v3.UptimeCheckConfig.ContentMatcher.IJsonPathMatcher|null);

ContentMatcher jsonPathMatcher.

### matcher
    
    
    public matcher: (google.monitoring.v3.UptimeCheckConfig.ContentMatcher.ContentMatcherOption|keyof typeof google.monitoring.v3.UptimeCheckConfig.ContentMatcher.ContentMatcherOption);

ContentMatcher matcher.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.monitoring.v3.UptimeCheckConfig.IContentMatcher): google.monitoring.v3.UptimeCheckConfig.ContentMatcher;

Creates a new ContentMatcher instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IContentMatcher](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.icontentmatcher)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ContentMatcher](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.contentmatcher-class)` | ContentMatcher instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.monitoring.v3.UptimeCheckConfig.ContentMatcher;

Decodes a ContentMatcher message from the specified reader or buffer.

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
`[ContentMatcher](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.contentmatcher-class)` | ContentMatcher  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.monitoring.v3.UptimeCheckConfig.ContentMatcher;

Decodes a ContentMatcher message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ContentMatcher](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.contentmatcher-class)` | ContentMatcher  
  
### encode(message, writer)
    
    
    public static encode(message: google.monitoring.v3.UptimeCheckConfig.IContentMatcher, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ContentMatcher message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IContentMatcher](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.icontentmatcher)`   
ContentMatcher message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.monitoring.v3.UptimeCheckConfig.IContentMatcher, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ContentMatcher message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IContentMatcher](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.icontentmatcher)`   
ContentMatcher message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.monitoring.v3.UptimeCheckConfig.ContentMatcher;

Creates a ContentMatcher message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ContentMatcher](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.contentmatcher-class)` | ContentMatcher  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ContentMatcher

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

Converts this ContentMatcher to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.monitoring.v3.UptimeCheckConfig.ContentMatcher, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ContentMatcher message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ContentMatcher](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.uptimecheckconfig.contentmatcher-class)`   
ContentMatcher  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ContentMatcher message.

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
