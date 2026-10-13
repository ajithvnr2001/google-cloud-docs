---
url: https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.upgradedistribution
title: Class protos.grafeas.v1.UpgradeDistribution (7.0.2) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:26.554625+00:00
---

# Class protos.grafeas.v1.UpgradeDistribution (7.0.2)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.upgradedistribution

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.grafeas.v1.UpgradeDistribution (7.0.2) Stay organized with collections  Save and categorize content based on your preferences. 

7.0.2 (latest)  7.0.1  6.8.0  6.7.0  6.5.0  5.6.0  5.0.1  4.7.0  4.4.2  4.3.0  3.4.0  3.3.0  3.2.0  3.1.8 

Represents an UpgradeDistribution.

## Implements

[protos.grafeas.v1.IUpgradeDistribution](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.iupgradedistribution)

## Package

[@google-cloud/containeranalysis](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: grafeas.v1.IUpgradeDistribution);

Constructs a new UpgradeDistribution.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpgradeDistribution](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.iupgradedistribution)`   
Properties to set  
  
## Properties 

### classification
    
    
    public classification: string;

UpgradeDistribution classification.

### cpeUri
    
    
    public cpeUri: string;

UpgradeDistribution cpeUri.

### cve
    
    
    public cve: string[];

UpgradeDistribution cve.

### severity
    
    
    public severity: string;

UpgradeDistribution severity.

## Methods 

### create(properties)
    
    
    public static create(properties?: grafeas.v1.IUpgradeDistribution): grafeas.v1.UpgradeDistribution;

Creates a new UpgradeDistribution instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpgradeDistribution](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.iupgradedistribution)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[UpgradeDistribution](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.upgradedistribution)` | UpgradeDistribution instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): grafeas.v1.UpgradeDistribution;

Decodes an UpgradeDistribution message from the specified reader or buffer.

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
`[UpgradeDistribution](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.upgradedistribution)` | UpgradeDistribution  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): grafeas.v1.UpgradeDistribution;

Decodes an UpgradeDistribution message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[UpgradeDistribution](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.upgradedistribution)` | UpgradeDistribution  
  
### encode(message, writer)
    
    
    public static encode(message: grafeas.v1.IUpgradeDistribution, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpgradeDistribution message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpgradeDistribution](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.iupgradedistribution)`   
UpgradeDistribution message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: grafeas.v1.IUpgradeDistribution, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpgradeDistribution message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpgradeDistribution](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.iupgradedistribution)`   
UpgradeDistribution message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): grafeas.v1.UpgradeDistribution;

Creates an UpgradeDistribution message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[UpgradeDistribution](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.upgradedistribution)` | UpgradeDistribution  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for UpgradeDistribution

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

Converts this UpgradeDistribution to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: grafeas.v1.UpgradeDistribution, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an UpgradeDistribution message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[UpgradeDistribution](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.upgradedistribution)`   
UpgradeDistribution  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an UpgradeDistribution message.

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
