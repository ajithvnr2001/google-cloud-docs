---
url: https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1beta.ociconfig
title: Class protos.google.cloud.gkehub.configmanagement.v1beta.OciConfig (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:05:25.387258+00:00
---

# Class protos.google.cloud.gkehub.configmanagement.v1beta.OciConfig (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1beta.ociconfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gkehub.configmanagement.v1beta.OciConfig (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.4.0  6.1.0  6.0.1  5.0.0  4.5.0  4.4.0  4.2.0  3.4.0  3.3.1  3.2.2  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.1  1.1.4 

Represents an OciConfig.

## Implements

[protos.google.cloud.gkehub.configmanagement.v1beta.IOciConfig](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1beta.iociconfig)

## Package

[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.gkehub.configmanagement.v1beta.IOciConfig);

Constructs a new OciConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOciConfig](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1beta.iociconfig)`   
Properties to set  
  
## Properties 

### gcpServiceAccountEmail
    
    
    public gcpServiceAccountEmail: string;

OciConfig gcpServiceAccountEmail.

### policyDir
    
    
    public policyDir: string;

OciConfig policyDir.

### secretType
    
    
    public secretType: string;

OciConfig secretType.

### syncRepo
    
    
    public syncRepo: string;

OciConfig syncRepo.

### syncWaitSecs
    
    
    public syncWaitSecs: (number|Long|string);

OciConfig syncWaitSecs.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.gkehub.configmanagement.v1beta.IOciConfig): google.cloud.gkehub.configmanagement.v1beta.OciConfig;

Creates a new OciConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOciConfig](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1beta.iociconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[OciConfig](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1beta.ociconfig)` | OciConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.gkehub.configmanagement.v1beta.OciConfig;

Decodes an OciConfig message from the specified reader or buffer.

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
`[OciConfig](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1beta.ociconfig)` | OciConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.gkehub.configmanagement.v1beta.OciConfig;

Decodes an OciConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[OciConfig](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1beta.ociconfig)` | OciConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.gkehub.configmanagement.v1beta.IOciConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OciConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOciConfig](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1beta.iociconfig)`   
OciConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.gkehub.configmanagement.v1beta.IOciConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OciConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOciConfig](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1beta.iociconfig)`   
OciConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.gkehub.configmanagement.v1beta.OciConfig;

Creates an OciConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[OciConfig](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1beta.ociconfig)` | OciConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for OciConfig

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

Converts this OciConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.gkehub.configmanagement.v1beta.OciConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an OciConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[OciConfig](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1beta.ociconfig)`   
OciConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an OciConfig message.

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
