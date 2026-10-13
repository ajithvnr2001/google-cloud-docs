---
url: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ingestaudiencemembersrequest
title: Class protos.google.ads.datamanager.v1.IngestAudienceMembersRequest (1.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:27.962337+00:00
---

# Class protos.google.ads.datamanager.v1.IngestAudienceMembersRequest (1.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ingestaudiencemembersrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.datamanager.v1.IngestAudienceMembersRequest (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.5.0  0.4.0  0.3.0  0.1.0 

Represents an IngestAudienceMembersRequest.

## Implements

[protos.google.ads.datamanager.v1.IIngestAudienceMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iingestaudiencemembersrequest)

## Package

[@google-ads/datamanager](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ads.datamanager.v1.IIngestAudienceMembersRequest);

Constructs a new IngestAudienceMembersRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IIngestAudienceMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iingestaudiencemembersrequest)`   
Properties to set  
  
## Properties 

### audienceMembers
    
    
    public audienceMembers: google.ads.datamanager.v1.IAudienceMember[];

IngestAudienceMembersRequest audienceMembers.

### consent
    
    
    public consent?: (google.ads.datamanager.v1.IConsent|null);

IngestAudienceMembersRequest consent.

### destinations
    
    
    public destinations: google.ads.datamanager.v1.IDestination[];

IngestAudienceMembersRequest destinations.

### encoding
    
    
    public encoding: (google.ads.datamanager.v1.Encoding|keyof typeof google.ads.datamanager.v1.Encoding);

IngestAudienceMembersRequest encoding.

### encryptionInfo
    
    
    public encryptionInfo?: (google.ads.datamanager.v1.IEncryptionInfo|null);

IngestAudienceMembersRequest encryptionInfo.

### termsOfService
    
    
    public termsOfService?: (google.ads.datamanager.v1.ITermsOfService|null);

IngestAudienceMembersRequest termsOfService.

### validateOnly
    
    
    public validateOnly: boolean;

IngestAudienceMembersRequest validateOnly.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.ads.datamanager.v1.IIngestAudienceMembersRequest): google.ads.datamanager.v1.IngestAudienceMembersRequest;

Creates a new IngestAudienceMembersRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IIngestAudienceMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iingestaudiencemembersrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[IngestAudienceMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ingestaudiencemembersrequest)` | IngestAudienceMembersRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ads.datamanager.v1.IngestAudienceMembersRequest;

Decodes an IngestAudienceMembersRequest message from the specified reader or buffer.

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
`[IngestAudienceMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ingestaudiencemembersrequest)` | IngestAudienceMembersRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ads.datamanager.v1.IngestAudienceMembersRequest;

Decodes an IngestAudienceMembersRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[IngestAudienceMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ingestaudiencemembersrequest)` | IngestAudienceMembersRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.ads.datamanager.v1.IIngestAudienceMembersRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified IngestAudienceMembersRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IIngestAudienceMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iingestaudiencemembersrequest)`   
IngestAudienceMembersRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ads.datamanager.v1.IIngestAudienceMembersRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified IngestAudienceMembersRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IIngestAudienceMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iingestaudiencemembersrequest)`   
IngestAudienceMembersRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ads.datamanager.v1.IngestAudienceMembersRequest;

Creates an IngestAudienceMembersRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[IngestAudienceMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ingestaudiencemembersrequest)` | IngestAudienceMembersRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for IngestAudienceMembersRequest

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

Converts this IngestAudienceMembersRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ads.datamanager.v1.IngestAudienceMembersRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an IngestAudienceMembersRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IngestAudienceMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ingestaudiencemembersrequest)`   
IngestAudienceMembersRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an IngestAudienceMembersRequest message.

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
