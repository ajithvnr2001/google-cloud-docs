---
url: https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p4beta1.iampolicyanalysisquery-class
title: Class protos.google.cloud.asset.v1p4beta1.IamPolicyAnalysisQuery (5.5.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:27:09.122058+00:00
---

# Class protos.google.cloud.asset.v1p4beta1.IamPolicyAnalysisQuery (5.5.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p4beta1.iampolicyanalysisquery-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.asset.v1p4beta1.IamPolicyAnalysisQuery (5.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  7.0.1  6.3.3  5.5.0  5.3.0  5.2.0  5.1.0  5.0.1  4.6.3  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  3.23.1  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.1  3.15.5  3.14.1  3.13.0 

Represents an IamPolicyAnalysisQuery.

## Package

[@google-cloud/asset](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.asset.v1p4beta1.IIamPolicyAnalysisQuery);

Constructs a new IamPolicyAnalysisQuery.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IIamPolicyAnalysisQuery](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p4beta1.iiampolicyanalysisquery)`   
Properties to set  
  
## Properties 

### accessSelector
    
    
    public accessSelector?: (google.cloud.asset.v1p4beta1.IamPolicyAnalysisQuery.IAccessSelector|null);

IamPolicyAnalysisQuery accessSelector.

### identitySelector
    
    
    public identitySelector?: (google.cloud.asset.v1p4beta1.IamPolicyAnalysisQuery.IIdentitySelector|null);

IamPolicyAnalysisQuery identitySelector.

### parent
    
    
    public parent: string;

IamPolicyAnalysisQuery parent.

### resourceSelector
    
    
    public resourceSelector?: (google.cloud.asset.v1p4beta1.IamPolicyAnalysisQuery.IResourceSelector|null);

IamPolicyAnalysisQuery resourceSelector.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.asset.v1p4beta1.IIamPolicyAnalysisQuery): google.cloud.asset.v1p4beta1.IamPolicyAnalysisQuery;

Creates a new IamPolicyAnalysisQuery instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IIamPolicyAnalysisQuery](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p4beta1.iiampolicyanalysisquery)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[IamPolicyAnalysisQuery](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p4beta1.iampolicyanalysisquery-class)` | IamPolicyAnalysisQuery instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.asset.v1p4beta1.IamPolicyAnalysisQuery;

Decodes an IamPolicyAnalysisQuery message from the specified reader or buffer.

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
`[IamPolicyAnalysisQuery](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p4beta1.iampolicyanalysisquery-class)` | IamPolicyAnalysisQuery  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.asset.v1p4beta1.IamPolicyAnalysisQuery;

Decodes an IamPolicyAnalysisQuery message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[IamPolicyAnalysisQuery](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p4beta1.iampolicyanalysisquery-class)` | IamPolicyAnalysisQuery  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.asset.v1p4beta1.IIamPolicyAnalysisQuery, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified IamPolicyAnalysisQuery message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IIamPolicyAnalysisQuery](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p4beta1.iiampolicyanalysisquery)`   
IamPolicyAnalysisQuery message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.asset.v1p4beta1.IIamPolicyAnalysisQuery, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified IamPolicyAnalysisQuery message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IIamPolicyAnalysisQuery](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p4beta1.iiampolicyanalysisquery)`   
IamPolicyAnalysisQuery message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.asset.v1p4beta1.IamPolicyAnalysisQuery;

Creates an IamPolicyAnalysisQuery message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[IamPolicyAnalysisQuery](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p4beta1.iampolicyanalysisquery-class)` | IamPolicyAnalysisQuery  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for IamPolicyAnalysisQuery

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

Converts this IamPolicyAnalysisQuery to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.asset.v1p4beta1.IamPolicyAnalysisQuery, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an IamPolicyAnalysisQuery message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IamPolicyAnalysisQuery](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p4beta1.iampolicyanalysisquery-class)`   
IamPolicyAnalysisQuery  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an IamPolicyAnalysisQuery message.

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
