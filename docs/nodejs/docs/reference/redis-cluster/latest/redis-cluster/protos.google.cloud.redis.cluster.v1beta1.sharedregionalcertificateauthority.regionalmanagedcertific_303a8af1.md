---
url: https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1beta1.sharedregionalcertificateauthority.regionalmanagedcertificateauthority.regionalcertchain
title: Class protos.google.cloud.redis.cluster.v1beta1.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.RegionalCertChain (0.15.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:11.624742+00:00
---

# Class protos.google.cloud.redis.cluster.v1beta1.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.RegionalCertChain (0.15.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1beta1.sharedregionalcertificateauthority.regionalmanagedcertificateauthority.regionalcertchain

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.redis.cluster.v1beta1.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.RegionalCertChain (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.0  0.12.0  0.11.0  0.8.0  0.7.1  0.6.0  0.5.0  0.1.0 

Represents a RegionalCertChain.

## Implements

[protos.google.cloud.redis.cluster.v1beta1.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.IRegionalCertChain](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1beta1.sharedregionalcertificateauthority.regionalmanagedcertificateauthority.iregionalcertchain)

## Package

[@google-cloud/redis-cluster](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.redis.cluster.v1beta1.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.IRegionalCertChain);

Constructs a new RegionalCertChain.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRegionalCertChain](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1beta1.sharedregionalcertificateauthority.regionalmanagedcertificateauthority.iregionalcertchain)`   
Properties to set  
  
## Properties 

### certificates
    
    
    public certificates: string[];

RegionalCertChain certificates.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.redis.cluster.v1beta1.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.IRegionalCertChain): google.cloud.redis.cluster.v1beta1.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.RegionalCertChain;

Creates a new RegionalCertChain instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRegionalCertChain](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1beta1.sharedregionalcertificateauthority.regionalmanagedcertificateauthority.iregionalcertchain)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[RegionalCertChain](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1beta1.sharedregionalcertificateauthority.regionalmanagedcertificateauthority.regionalcertchain)` | RegionalCertChain instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.redis.cluster.v1beta1.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.RegionalCertChain;

Decodes a RegionalCertChain message from the specified reader or buffer.

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
`[RegionalCertChain](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1beta1.sharedregionalcertificateauthority.regionalmanagedcertificateauthority.regionalcertchain)` | RegionalCertChain  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.redis.cluster.v1beta1.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.RegionalCertChain;

Decodes a RegionalCertChain message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[RegionalCertChain](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1beta1.sharedregionalcertificateauthority.regionalmanagedcertificateauthority.regionalcertchain)` | RegionalCertChain  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.redis.cluster.v1beta1.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.IRegionalCertChain, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RegionalCertChain message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRegionalCertChain](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1beta1.sharedregionalcertificateauthority.regionalmanagedcertificateauthority.iregionalcertchain)`   
RegionalCertChain message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.redis.cluster.v1beta1.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.IRegionalCertChain, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RegionalCertChain message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRegionalCertChain](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1beta1.sharedregionalcertificateauthority.regionalmanagedcertificateauthority.iregionalcertchain)`   
RegionalCertChain message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.redis.cluster.v1beta1.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.RegionalCertChain;

Creates a RegionalCertChain message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[RegionalCertChain](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1beta1.sharedregionalcertificateauthority.regionalmanagedcertificateauthority.regionalcertchain)` | RegionalCertChain  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for RegionalCertChain

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

Converts this RegionalCertChain to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.redis.cluster.v1beta1.SharedRegionalCertificateAuthority.RegionalManagedCertificateAuthority.RegionalCertChain, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a RegionalCertChain message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[RegionalCertChain](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1beta1.sharedregionalcertificateauthority.regionalmanagedcertificateauthority.regionalcertchain)`   
RegionalCertChain  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a RegionalCertChain message.

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
