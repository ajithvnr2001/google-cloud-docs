---
url: https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.issuematchdata
title: Class protos.google.cloud.contactcenterinsights.v1.IssueMatchData (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:08.858098+00:00
---

# Class protos.google.cloud.contactcenterinsights.v1.IssueMatchData (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.issuematchdata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.contactcenterinsights.v1.IssueMatchData (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.0.1  4.1.3  3.9.0  3.8.0  3.7.0  3.6.0  3.3.0  3.1.0  2.7.0  2.6.0  2.4.1  2.3.0  2.1.2  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.2 

Represents an IssueMatchData.

## Implements

[protos.google.cloud.contactcenterinsights.v1.IIssueMatchData](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.iissuematchdata)

## Package

[@google-cloud/contact-center-insights](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.contactcenterinsights.v1.IIssueMatchData);

Constructs a new IssueMatchData.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IIssueMatchData](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.iissuematchdata)`   
Properties to set  
  
## Properties 

### issueAssignment
    
    
    public issueAssignment?: (google.cloud.contactcenterinsights.v1.IIssueAssignment|null);

IssueMatchData issueAssignment.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.contactcenterinsights.v1.IIssueMatchData): google.cloud.contactcenterinsights.v1.IssueMatchData;

Creates a new IssueMatchData instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IIssueMatchData](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.iissuematchdata)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[IssueMatchData](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.issuematchdata)` | IssueMatchData instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.contactcenterinsights.v1.IssueMatchData;

Decodes an IssueMatchData message from the specified reader or buffer.

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
`[IssueMatchData](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.issuematchdata)` | IssueMatchData  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.contactcenterinsights.v1.IssueMatchData;

Decodes an IssueMatchData message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[IssueMatchData](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.issuematchdata)` | IssueMatchData  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.contactcenterinsights.v1.IIssueMatchData, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified IssueMatchData message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IIssueMatchData](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.iissuematchdata)`   
IssueMatchData message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.contactcenterinsights.v1.IIssueMatchData, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified IssueMatchData message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IIssueMatchData](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.iissuematchdata)`   
IssueMatchData message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.contactcenterinsights.v1.IssueMatchData;

Creates an IssueMatchData message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[IssueMatchData](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.issuematchdata)` | IssueMatchData  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for IssueMatchData

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

Converts this IssueMatchData to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.contactcenterinsights.v1.IssueMatchData, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an IssueMatchData message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IssueMatchData](https://docs.cloud.google.com/nodejs/docs/reference/contact-center-insights/latest/contact-center-insights/protos.google.cloud.contactcenterinsights.v1.issuematchdata)`   
IssueMatchData  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an IssueMatchData message.

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
