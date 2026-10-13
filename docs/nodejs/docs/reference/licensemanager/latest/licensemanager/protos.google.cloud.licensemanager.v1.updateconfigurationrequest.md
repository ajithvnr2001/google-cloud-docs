---
url: https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.updateconfigurationrequest
title: Class protos.google.cloud.licensemanager.v1.UpdateConfigurationRequest (0.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:13.800852+00:00
---

# Class protos.google.cloud.licensemanager.v1.UpdateConfigurationRequest (0.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.updateconfigurationrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.licensemanager.v1.UpdateConfigurationRequest (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an UpdateConfigurationRequest.

## Implements

[protos.google.cloud.licensemanager.v1.IUpdateConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.iupdateconfigurationrequest)

## Package

[@google-cloud/licensemanager](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.licensemanager.v1.IUpdateConfigurationRequest);

Constructs a new UpdateConfigurationRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.iupdateconfigurationrequest)`   
Properties to set  
  
## Properties 

### configuration
    
    
    public configuration?: (google.cloud.licensemanager.v1.IConfiguration|null);

UpdateConfigurationRequest configuration.

### requestId
    
    
    public requestId: string;

UpdateConfigurationRequest requestId.

### updateMask
    
    
    public updateMask?: (google.protobuf.IFieldMask|null);

UpdateConfigurationRequest updateMask.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.licensemanager.v1.IUpdateConfigurationRequest): google.cloud.licensemanager.v1.UpdateConfigurationRequest;

Creates a new UpdateConfigurationRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.iupdateconfigurationrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[UpdateConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.updateconfigurationrequest)` | UpdateConfigurationRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.licensemanager.v1.UpdateConfigurationRequest;

Decodes an UpdateConfigurationRequest message from the specified reader or buffer.

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
`[UpdateConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.updateconfigurationrequest)` | UpdateConfigurationRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.licensemanager.v1.UpdateConfigurationRequest;

Decodes an UpdateConfigurationRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[UpdateConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.updateconfigurationrequest)` | UpdateConfigurationRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.licensemanager.v1.IUpdateConfigurationRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateConfigurationRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.iupdateconfigurationrequest)`   
UpdateConfigurationRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.licensemanager.v1.IUpdateConfigurationRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateConfigurationRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.iupdateconfigurationrequest)`   
UpdateConfigurationRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.licensemanager.v1.UpdateConfigurationRequest;

Creates an UpdateConfigurationRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[UpdateConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.updateconfigurationrequest)` | UpdateConfigurationRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for UpdateConfigurationRequest

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

Converts this UpdateConfigurationRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.licensemanager.v1.UpdateConfigurationRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an UpdateConfigurationRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[UpdateConfigurationRequest](https://docs.cloud.google.com/nodejs/docs/reference/licensemanager/latest/licensemanager/protos.google.cloud.licensemanager.v1.updateconfigurationrequest)`   
UpdateConfigurationRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an UpdateConfigurationRequest message.

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
