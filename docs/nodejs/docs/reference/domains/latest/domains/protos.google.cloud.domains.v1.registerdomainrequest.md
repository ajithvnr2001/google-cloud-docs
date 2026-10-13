---
url: https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1.registerdomainrequest
title: Class protos.google.cloud.domains.v1.RegisterDomainRequest (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:32.717735+00:00
---

# Class protos.google.cloud.domains.v1.RegisterDomainRequest (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1.registerdomainrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.domains.v1.RegisterDomainRequest (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  4.0.1  3.1.0  2.2.2  2.1.2  1.2.0  1.1.0  1.0.8 

Represents a RegisterDomainRequest.

## Implements

[protos.google.cloud.domains.v1.IRegisterDomainRequest](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1.iregisterdomainrequest)

## Package

[@google-cloud/domains](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.domains.v1.IRegisterDomainRequest);

Constructs a new RegisterDomainRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRegisterDomainRequest](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1.iregisterdomainrequest)`   
Properties to set  
  
## Properties 

### contactNotices
    
    
    public contactNotices: google.cloud.domains.v1.ContactNotice[];

RegisterDomainRequest contactNotices.

### domainNotices
    
    
    public domainNotices: google.cloud.domains.v1.DomainNotice[];

RegisterDomainRequest domainNotices.

### parent
    
    
    public parent: string;

RegisterDomainRequest parent.

### registration
    
    
    public registration?: (google.cloud.domains.v1.IRegistration|null);

RegisterDomainRequest registration.

### validateOnly
    
    
    public validateOnly: boolean;

RegisterDomainRequest validateOnly.

### yearlyPrice
    
    
    public yearlyPrice?: (google.type.IMoney|null);

RegisterDomainRequest yearlyPrice.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.domains.v1.IRegisterDomainRequest): google.cloud.domains.v1.RegisterDomainRequest;

Creates a new RegisterDomainRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRegisterDomainRequest](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1.iregisterdomainrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[RegisterDomainRequest](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1.registerdomainrequest)` | RegisterDomainRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.domains.v1.RegisterDomainRequest;

Decodes a RegisterDomainRequest message from the specified reader or buffer.

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
`[RegisterDomainRequest](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1.registerdomainrequest)` | RegisterDomainRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.domains.v1.RegisterDomainRequest;

Decodes a RegisterDomainRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[RegisterDomainRequest](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1.registerdomainrequest)` | RegisterDomainRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.domains.v1.IRegisterDomainRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RegisterDomainRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRegisterDomainRequest](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1.iregisterdomainrequest)`   
RegisterDomainRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.domains.v1.IRegisterDomainRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RegisterDomainRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRegisterDomainRequest](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1.iregisterdomainrequest)`   
RegisterDomainRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.domains.v1.RegisterDomainRequest;

Creates a RegisterDomainRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[RegisterDomainRequest](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1.registerdomainrequest)` | RegisterDomainRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for RegisterDomainRequest

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

Converts this RegisterDomainRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.domains.v1.RegisterDomainRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a RegisterDomainRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[RegisterDomainRequest](https://docs.cloud.google.com/nodejs/docs/reference/domains/latest/domains/protos.google.cloud.domains.v1.registerdomainrequest)`   
RegisterDomainRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a RegisterDomainRequest message.

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
