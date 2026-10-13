---
url: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubresource
title: Class protos.google.cloud.apihub.v1.ApiHubResource (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:05:42.781921+00:00
---

# Class protos.google.cloud.apihub.v1.ApiHubResource (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubresource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apihub.v1.ApiHubResource (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an ApiHubResource.

## Implements

[protos.google.cloud.apihub.v1.IApiHubResource](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iapihubresource)

## Package

[@google-cloud/apihub](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.apihub.v1.IApiHubResource);

Constructs a new ApiHubResource.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IApiHubResource](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iapihubresource)`   
Properties to set  
  
## Properties 

### api
    
    
    public api?: (google.cloud.apihub.v1.IApi|null);

ApiHubResource api.

### definition
    
    
    public definition?: (google.cloud.apihub.v1.IDefinition|null);

ApiHubResource definition.

### deployment
    
    
    public deployment?: (google.cloud.apihub.v1.IDeployment|null);

ApiHubResource deployment.

### operation
    
    
    public operation?: (google.cloud.apihub.v1.IApiOperation|null);

ApiHubResource operation.

### resource
    
    
    public resource?: ("api"|"operation"|"deployment"|"spec"|"definition"|"version");

ApiHubResource resource.

### spec
    
    
    public spec?: (google.cloud.apihub.v1.ISpec|null);

ApiHubResource spec.

### version
    
    
    public version?: (google.cloud.apihub.v1.IVersion|null);

ApiHubResource version.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.apihub.v1.IApiHubResource): google.cloud.apihub.v1.ApiHubResource;

Creates a new ApiHubResource instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IApiHubResource](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iapihubresource)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ApiHubResource](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubresource)` | ApiHubResource instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.apihub.v1.ApiHubResource;

Decodes an ApiHubResource message from the specified reader or buffer.

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
`[ApiHubResource](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubresource)` | ApiHubResource  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.apihub.v1.ApiHubResource;

Decodes an ApiHubResource message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ApiHubResource](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubresource)` | ApiHubResource  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.apihub.v1.IApiHubResource, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ApiHubResource message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IApiHubResource](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iapihubresource)`   
ApiHubResource message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.apihub.v1.IApiHubResource, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ApiHubResource message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IApiHubResource](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iapihubresource)`   
ApiHubResource message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.apihub.v1.ApiHubResource;

Creates an ApiHubResource message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ApiHubResource](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubresource)` | ApiHubResource  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ApiHubResource

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

Converts this ApiHubResource to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.apihub.v1.ApiHubResource, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an ApiHubResource message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ApiHubResource](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.apihubresource)`   
ApiHubResource  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an ApiHubResource message.

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
