---
url: https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.workload-class
title: Class protos.google.cloud.assuredworkloads.v1beta1.Workload (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:55:13.896676+00:00
---

# Class protos.google.cloud.assuredworkloads.v1beta1.Workload (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.workload-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.assuredworkloads.v1beta1.Workload (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  3.6.2  3.5.0  3.4.1  3.2.0  2.2.0  2.1.0  2.0.0  1.8.0  1.7.0  1.6.0  1.5.2  1.4.6 

Represents a Workload.

## Implements

[protos.google.cloud.assuredworkloads.v1beta1.IWorkload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload)

## Package

[@google-cloud/assured-workloads](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.assuredworkloads.v1beta1.IWorkload);

Constructs a new Workload.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IWorkload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload)`   
Properties to set  
  
## Properties 

### billingAccount
    
    
    public billingAccount: string;

Workload billingAccount.

### cjisSettings
    
    
    public cjisSettings?: (google.cloud.assuredworkloads.v1beta1.Workload.ICJISSettings|null);

Workload cjisSettings.

### complianceRegime
    
    
    public complianceRegime: (google.cloud.assuredworkloads.v1beta1.Workload.ComplianceRegime|keyof typeof google.cloud.assuredworkloads.v1beta1.Workload.ComplianceRegime);

Workload complianceRegime.

### complianceRegimeSettings
    
    
    public complianceRegimeSettings?: ("il4Settings"|"cjisSettings"|"fedrampHighSettings"|"fedrampModerateSettings");

Workload complianceRegimeSettings.

### compliantButDisallowedServices
    
    
    public compliantButDisallowedServices: string[];

Workload compliantButDisallowedServices.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Workload createTime.

### displayName
    
    
    public displayName: string;

Workload displayName.

### enableSovereignControls
    
    
    public enableSovereignControls: boolean;

Workload enableSovereignControls.

### etag
    
    
    public etag: string;

Workload etag.

### fedrampHighSettings
    
    
    public fedrampHighSettings?: (google.cloud.assuredworkloads.v1beta1.Workload.IFedrampHighSettings|null);

Workload fedrampHighSettings.

### fedrampModerateSettings
    
    
    public fedrampModerateSettings?: (google.cloud.assuredworkloads.v1beta1.Workload.IFedrampModerateSettings|null);

Workload fedrampModerateSettings.

### il4Settings
    
    
    public il4Settings?: (google.cloud.assuredworkloads.v1beta1.Workload.IIL4Settings|null);

Workload il4Settings.

### kajEnrollmentState
    
    
    public kajEnrollmentState: (google.cloud.assuredworkloads.v1beta1.Workload.KajEnrollmentState|keyof typeof google.cloud.assuredworkloads.v1beta1.Workload.KajEnrollmentState);

Workload kajEnrollmentState.

### kmsSettings
    
    
    public kmsSettings?: (google.cloud.assuredworkloads.v1beta1.Workload.IKMSSettings|null);

Workload kmsSettings.

### labels
    
    
    public labels: { [k: string]: string };

Workload labels.

### name
    
    
    public name: string;

Workload name.

### provisionedResourcesParent
    
    
    public provisionedResourcesParent: string;

Workload provisionedResourcesParent.

### resources
    
    
    public resources: google.cloud.assuredworkloads.v1beta1.Workload.IResourceInfo[];

Workload resources.

### resourceSettings
    
    
    public resourceSettings: google.cloud.assuredworkloads.v1beta1.Workload.IResourceSettings[];

Workload resourceSettings.

### saaEnrollmentResponse
    
    
    public saaEnrollmentResponse?: (google.cloud.assuredworkloads.v1beta1.Workload.ISaaEnrollmentResponse|null);

Workload saaEnrollmentResponse.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.assuredworkloads.v1beta1.IWorkload): google.cloud.assuredworkloads.v1beta1.Workload;

Creates a new Workload instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IWorkload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.workload-class)` | Workload instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.assuredworkloads.v1beta1.Workload;

Decodes a Workload message from the specified reader or buffer.

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
`[Workload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.workload-class)` | Workload  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.assuredworkloads.v1beta1.Workload;

Decodes a Workload message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.workload-class)` | Workload  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.assuredworkloads.v1beta1.IWorkload, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Workload message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IWorkload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload)`   
Workload message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.assuredworkloads.v1beta1.IWorkload, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Workload message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IWorkload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload)`   
Workload message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.assuredworkloads.v1beta1.Workload;

Creates a Workload message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.workload-class)` | Workload  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Workload

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

Converts this Workload to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.assuredworkloads.v1beta1.Workload, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Workload message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Workload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.workload-class)`   
Workload  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Workload message.

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
