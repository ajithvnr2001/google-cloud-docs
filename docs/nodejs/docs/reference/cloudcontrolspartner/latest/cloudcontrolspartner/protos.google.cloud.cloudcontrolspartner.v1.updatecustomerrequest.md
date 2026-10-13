---
url: https://docs.cloud.google.com/nodejs/docs/reference/cloudcontrolspartner/latest/cloudcontrolspartner/protos.google.cloud.cloudcontrolspartner.v1.updatecustomerrequest
title: Class protos.google.cloud.cloudcontrolspartner.v1.UpdateCustomerRequest (0.8.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:47.273965+00:00
---

# Class protos.google.cloud.cloudcontrolspartner.v1.UpdateCustomerRequest (0.8.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/cloudcontrolspartner/latest/cloudcontrolspartner/protos.google.cloud.cloudcontrolspartner.v1.updatecustomerrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.cloudcontrolspartner.v1.UpdateCustomerRequest (0.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.1 (latest)  0.4.0  0.3.1  0.1.0 

Represents an UpdateCustomerRequest.

## Implements

[protos.google.cloud.cloudcontrolspartner.v1.IUpdateCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/cloudcontrolspartner/latest/cloudcontrolspartner/protos.google.cloud.cloudcontrolspartner.v1.iupdatecustomerrequest)

## Package

[@google-cloud/cloudcontrolspartner](https://docs.cloud.google.com/nodejs/docs/reference/cloudcontrolspartner/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.cloudcontrolspartner.v1.IUpdateCustomerRequest);

Constructs a new UpdateCustomerRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/cloudcontrolspartner/latest/cloudcontrolspartner/protos.google.cloud.cloudcontrolspartner.v1.iupdatecustomerrequest)`   
Properties to set  
  
## Properties 

### customer
    
    
    public customer?: (google.cloud.cloudcontrolspartner.v1.ICustomer|null);

UpdateCustomerRequest customer.

### updateMask
    
    
    public updateMask?: (google.protobuf.IFieldMask|null);

UpdateCustomerRequest updateMask.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.cloudcontrolspartner.v1.IUpdateCustomerRequest): google.cloud.cloudcontrolspartner.v1.UpdateCustomerRequest;

Creates a new UpdateCustomerRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/cloudcontrolspartner/latest/cloudcontrolspartner/protos.google.cloud.cloudcontrolspartner.v1.iupdatecustomerrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[UpdateCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/cloudcontrolspartner/latest/cloudcontrolspartner/protos.google.cloud.cloudcontrolspartner.v1.updatecustomerrequest)` | UpdateCustomerRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.cloudcontrolspartner.v1.UpdateCustomerRequest;

Decodes an UpdateCustomerRequest message from the specified reader or buffer.

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
`[UpdateCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/cloudcontrolspartner/latest/cloudcontrolspartner/protos.google.cloud.cloudcontrolspartner.v1.updatecustomerrequest)` | UpdateCustomerRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.cloudcontrolspartner.v1.UpdateCustomerRequest;

Decodes an UpdateCustomerRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[UpdateCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/cloudcontrolspartner/latest/cloudcontrolspartner/protos.google.cloud.cloudcontrolspartner.v1.updatecustomerrequest)` | UpdateCustomerRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.cloudcontrolspartner.v1.IUpdateCustomerRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateCustomerRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/cloudcontrolspartner/latest/cloudcontrolspartner/protos.google.cloud.cloudcontrolspartner.v1.iupdatecustomerrequest)`   
UpdateCustomerRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.cloudcontrolspartner.v1.IUpdateCustomerRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateCustomerRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/cloudcontrolspartner/latest/cloudcontrolspartner/protos.google.cloud.cloudcontrolspartner.v1.iupdatecustomerrequest)`   
UpdateCustomerRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.cloudcontrolspartner.v1.UpdateCustomerRequest;

Creates an UpdateCustomerRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[UpdateCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/cloudcontrolspartner/latest/cloudcontrolspartner/protos.google.cloud.cloudcontrolspartner.v1.updatecustomerrequest)` | UpdateCustomerRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for UpdateCustomerRequest

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

Converts this UpdateCustomerRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.cloudcontrolspartner.v1.UpdateCustomerRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an UpdateCustomerRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[UpdateCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/cloudcontrolspartner/latest/cloudcontrolspartner/protos.google.cloud.cloudcontrolspartner.v1.updatecustomerrequest)`   
UpdateCustomerRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an UpdateCustomerRequest message.

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
