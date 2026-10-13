---
url: https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta.membershipfeaturespec
title: Class protos.google.cloud.gkehub.v1beta.MembershipFeatureSpec (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:28.700876+00:00
---

# Class protos.google.cloud.gkehub.v1beta.MembershipFeatureSpec (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta.membershipfeaturespec

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gkehub.v1beta.MembershipFeatureSpec (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.4.0  6.1.0  6.0.1  5.0.0  4.5.0  4.4.0  4.2.0  3.4.0  3.3.1  3.2.2  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.1  1.1.4 

Represents a MembershipFeatureSpec.

## Implements

[protos.google.cloud.gkehub.v1beta.IMembershipFeatureSpec](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta.imembershipfeaturespec)

## Package

[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.gkehub.v1beta.IMembershipFeatureSpec);

Constructs a new MembershipFeatureSpec.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMembershipFeatureSpec](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta.imembershipfeaturespec)`   
Properties to set  
  
## Properties 

### configmanagement
    
    
    public configmanagement?: (google.cloud.gkehub.configmanagement.v1beta.IMembershipSpec|null);

MembershipFeatureSpec configmanagement.

### featureSpec
    
    
    public featureSpec?: ("configmanagement"|"mesh"|"policycontroller");

MembershipFeatureSpec featureSpec.

### mesh
    
    
    public mesh?: (google.cloud.gkehub.servicemesh.v1beta.IMembershipSpec|null);

MembershipFeatureSpec mesh.

### policycontroller
    
    
    public policycontroller?: (google.cloud.gkehub.policycontroller.v1beta.IMembershipSpec|null);

MembershipFeatureSpec policycontroller.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.gkehub.v1beta.IMembershipFeatureSpec): google.cloud.gkehub.v1beta.MembershipFeatureSpec;

Creates a new MembershipFeatureSpec instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMembershipFeatureSpec](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta.imembershipfeaturespec)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[MembershipFeatureSpec](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta.membershipfeaturespec)` | MembershipFeatureSpec instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.gkehub.v1beta.MembershipFeatureSpec;

Decodes a MembershipFeatureSpec message from the specified reader or buffer.

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
`[MembershipFeatureSpec](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta.membershipfeaturespec)` | MembershipFeatureSpec  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.gkehub.v1beta.MembershipFeatureSpec;

Decodes a MembershipFeatureSpec message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[MembershipFeatureSpec](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta.membershipfeaturespec)` | MembershipFeatureSpec  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.gkehub.v1beta.IMembershipFeatureSpec, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MembershipFeatureSpec message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMembershipFeatureSpec](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta.imembershipfeaturespec)`   
MembershipFeatureSpec message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.gkehub.v1beta.IMembershipFeatureSpec, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MembershipFeatureSpec message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMembershipFeatureSpec](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta.imembershipfeaturespec)`   
MembershipFeatureSpec message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.gkehub.v1beta.MembershipFeatureSpec;

Creates a MembershipFeatureSpec message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[MembershipFeatureSpec](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta.membershipfeaturespec)` | MembershipFeatureSpec  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for MembershipFeatureSpec

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

Converts this MembershipFeatureSpec to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.gkehub.v1beta.MembershipFeatureSpec, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a MembershipFeatureSpec message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[MembershipFeatureSpec](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta.membershipfeaturespec)`   
MembershipFeatureSpec  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a MembershipFeatureSpec message.

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
