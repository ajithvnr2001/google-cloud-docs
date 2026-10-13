---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.backendservicetlssettingssubjectaltname
title: Class protos.google.cloud.compute.v1.BackendServiceTlsSettingsSubjectAltName (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:03.393327+00:00
---

# Class protos.google.cloud.compute.v1.BackendServiceTlsSettingsSubjectAltName (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.backendservicetlssettingssubjectaltname

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.compute.v1.BackendServiceTlsSettingsSubjectAltName (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

Represents a BackendServiceTlsSettingsSubjectAltName.

## Implements

[protos.google.cloud.compute.v1.IBackendServiceTlsSettingsSubjectAltName](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ibackendservicetlssettingssubjectaltname)

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.compute.v1.IBackendServiceTlsSettingsSubjectAltName);

Constructs a new BackendServiceTlsSettingsSubjectAltName.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBackendServiceTlsSettingsSubjectAltName](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ibackendservicetlssettingssubjectaltname)`   
Properties to set  
  
## Properties 

### dnsName
    
    
    public dnsName?: (string|null);

BackendServiceTlsSettingsSubjectAltName dnsName.

### uniformResourceIdentifier
    
    
    public uniformResourceIdentifier?: (string|null);

BackendServiceTlsSettingsSubjectAltName uniformResourceIdentifier.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.compute.v1.IBackendServiceTlsSettingsSubjectAltName): google.cloud.compute.v1.BackendServiceTlsSettingsSubjectAltName;

Creates a new BackendServiceTlsSettingsSubjectAltName instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBackendServiceTlsSettingsSubjectAltName](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ibackendservicetlssettingssubjectaltname)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[BackendServiceTlsSettingsSubjectAltName](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.backendservicetlssettingssubjectaltname)` | BackendServiceTlsSettingsSubjectAltName instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.compute.v1.BackendServiceTlsSettingsSubjectAltName;

Decodes a BackendServiceTlsSettingsSubjectAltName message from the specified reader or buffer.

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
`[BackendServiceTlsSettingsSubjectAltName](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.backendservicetlssettingssubjectaltname)` | BackendServiceTlsSettingsSubjectAltName  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.compute.v1.BackendServiceTlsSettingsSubjectAltName;

Decodes a BackendServiceTlsSettingsSubjectAltName message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[BackendServiceTlsSettingsSubjectAltName](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.backendservicetlssettingssubjectaltname)` | BackendServiceTlsSettingsSubjectAltName  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.compute.v1.IBackendServiceTlsSettingsSubjectAltName, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BackendServiceTlsSettingsSubjectAltName message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBackendServiceTlsSettingsSubjectAltName](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ibackendservicetlssettingssubjectaltname)`   
BackendServiceTlsSettingsSubjectAltName message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.compute.v1.IBackendServiceTlsSettingsSubjectAltName, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BackendServiceTlsSettingsSubjectAltName message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBackendServiceTlsSettingsSubjectAltName](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ibackendservicetlssettingssubjectaltname)`   
BackendServiceTlsSettingsSubjectAltName message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.compute.v1.BackendServiceTlsSettingsSubjectAltName;

Creates a BackendServiceTlsSettingsSubjectAltName message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[BackendServiceTlsSettingsSubjectAltName](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.backendservicetlssettingssubjectaltname)` | BackendServiceTlsSettingsSubjectAltName  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for BackendServiceTlsSettingsSubjectAltName

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

Converts this BackendServiceTlsSettingsSubjectAltName to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.compute.v1.BackendServiceTlsSettingsSubjectAltName, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a BackendServiceTlsSettingsSubjectAltName message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[BackendServiceTlsSettingsSubjectAltName](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.backendservicetlssettingssubjectaltname)`   
BackendServiceTlsSettingsSubjectAltName  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a BackendServiceTlsSettingsSubjectAltName message.

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
