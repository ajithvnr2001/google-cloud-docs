---
url: https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.createunitkindrequest
title: Class protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateUnitKindRequest (0.6.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:18:15.377616+00:00
---

# Class protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateUnitKindRequest (0.6.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.createunitkindrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateUnitKindRequest (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.4.0 

Represents a CreateUnitKindRequest.

## Implements

[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitkindrequest)

## Package

[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitKindRequest);

Constructs a new CreateUnitKindRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitkindrequest)`   
Properties to set  
  
## Properties 

### parent
    
    
    public parent: string;

CreateUnitKindRequest parent.

### requestId
    
    
    public requestId: string;

CreateUnitKindRequest requestId.

### unitKind
    
    
    public unitKind?: (google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind|null);

CreateUnitKindRequest unitKind.

### unitKindId
    
    
    public unitKindId: string;

CreateUnitKindRequest unitKindId.

### validateOnly
    
    
    public validateOnly: boolean;

CreateUnitKindRequest validateOnly.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitKindRequest): google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateUnitKindRequest;

Creates a new CreateUnitKindRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitkindrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CreateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.createunitkindrequest)` | CreateUnitKindRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateUnitKindRequest;

Decodes a CreateUnitKindRequest message from the specified reader or buffer.

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
`[CreateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.createunitkindrequest)` | CreateUnitKindRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateUnitKindRequest;

Decodes a CreateUnitKindRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CreateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.createunitkindrequest)` | CreateUnitKindRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitKindRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateUnitKindRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitkindrequest)`   
CreateUnitKindRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitKindRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateUnitKindRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitkindrequest)`   
CreateUnitKindRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateUnitKindRequest;

Creates a CreateUnitKindRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CreateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.createunitkindrequest)` | CreateUnitKindRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CreateUnitKindRequest

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

Converts this CreateUnitKindRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateUnitKindRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CreateUnitKindRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CreateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.createunitkindrequest)`   
CreateUnitKindRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CreateUnitKindRequest message.

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
