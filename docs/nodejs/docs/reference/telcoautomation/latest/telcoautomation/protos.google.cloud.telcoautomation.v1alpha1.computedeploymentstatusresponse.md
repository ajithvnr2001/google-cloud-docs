---
url: https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.computedeploymentstatusresponse
title: Class protos.google.cloud.telcoautomation.v1alpha1.ComputeDeploymentStatusResponse (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:59:55.479166+00:00
---

# Class protos.google.cloud.telcoautomation.v1alpha1.ComputeDeploymentStatusResponse (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.computedeploymentstatusresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.telcoautomation.v1alpha1.ComputeDeploymentStatusResponse (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.1.0 

Represents a ComputeDeploymentStatusResponse.

## Implements

[protos.google.cloud.telcoautomation.v1alpha1.IComputeDeploymentStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.icomputedeploymentstatusresponse)

## Package

[@google-cloud/telcoautomation](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.telcoautomation.v1alpha1.IComputeDeploymentStatusResponse);

Constructs a new ComputeDeploymentStatusResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IComputeDeploymentStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.icomputedeploymentstatusresponse)`   
Properties to set  
  
## Properties 

### aggregatedStatus
    
    
    public aggregatedStatus: (google.cloud.telcoautomation.v1alpha1.Status|keyof typeof google.cloud.telcoautomation.v1alpha1.Status);

ComputeDeploymentStatusResponse aggregatedStatus.

### name
    
    
    public name: string;

ComputeDeploymentStatusResponse name.

### resourceStatuses
    
    
    public resourceStatuses: google.cloud.telcoautomation.v1alpha1.IResourceStatus[];

ComputeDeploymentStatusResponse resourceStatuses.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.telcoautomation.v1alpha1.IComputeDeploymentStatusResponse): google.cloud.telcoautomation.v1alpha1.ComputeDeploymentStatusResponse;

Creates a new ComputeDeploymentStatusResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IComputeDeploymentStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.icomputedeploymentstatusresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ComputeDeploymentStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.computedeploymentstatusresponse)` | ComputeDeploymentStatusResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.telcoautomation.v1alpha1.ComputeDeploymentStatusResponse;

Decodes a ComputeDeploymentStatusResponse message from the specified reader or buffer.

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
`[ComputeDeploymentStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.computedeploymentstatusresponse)` | ComputeDeploymentStatusResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.telcoautomation.v1alpha1.ComputeDeploymentStatusResponse;

Decodes a ComputeDeploymentStatusResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ComputeDeploymentStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.computedeploymentstatusresponse)` | ComputeDeploymentStatusResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.telcoautomation.v1alpha1.IComputeDeploymentStatusResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ComputeDeploymentStatusResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IComputeDeploymentStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.icomputedeploymentstatusresponse)`   
ComputeDeploymentStatusResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.telcoautomation.v1alpha1.IComputeDeploymentStatusResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ComputeDeploymentStatusResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IComputeDeploymentStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.icomputedeploymentstatusresponse)`   
ComputeDeploymentStatusResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.telcoautomation.v1alpha1.ComputeDeploymentStatusResponse;

Creates a ComputeDeploymentStatusResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ComputeDeploymentStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.computedeploymentstatusresponse)` | ComputeDeploymentStatusResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ComputeDeploymentStatusResponse

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

Converts this ComputeDeploymentStatusResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.telcoautomation.v1alpha1.ComputeDeploymentStatusResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ComputeDeploymentStatusResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ComputeDeploymentStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/telcoautomation/latest/telcoautomation/protos.google.cloud.telcoautomation.v1alpha1.computedeploymentstatusresponse)`   
ComputeDeploymentStatusResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ComputeDeploymentStatusResponse message.

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
