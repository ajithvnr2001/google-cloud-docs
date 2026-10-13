---
url: https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1alpha.hierarchycontrollerdeploymentstate
title: Class protos.google.cloud.gkehub.configmanagement.v1alpha.HierarchyControllerDeploymentState (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:05:16.917496+00:00
---

# Class protos.google.cloud.gkehub.configmanagement.v1alpha.HierarchyControllerDeploymentState (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1alpha.hierarchycontrollerdeploymentstate

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gkehub.configmanagement.v1alpha.HierarchyControllerDeploymentState (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.4.0  6.1.0  6.0.1  5.0.0  4.5.0  4.4.0  4.2.0  3.4.0  3.3.1  3.2.2  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.1  1.1.4 

Represents a HierarchyControllerDeploymentState.

## Implements

[protos.google.cloud.gkehub.configmanagement.v1alpha.IHierarchyControllerDeploymentState](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1alpha.ihierarchycontrollerdeploymentstate)

## Package

[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.gkehub.configmanagement.v1alpha.IHierarchyControllerDeploymentState);

Constructs a new HierarchyControllerDeploymentState.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IHierarchyControllerDeploymentState](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1alpha.ihierarchycontrollerdeploymentstate)`   
Properties to set  
  
## Properties 

### extension
    
    
    public extension: (google.cloud.gkehub.configmanagement.v1alpha.DeploymentState|keyof typeof google.cloud.gkehub.configmanagement.v1alpha.DeploymentState);

HierarchyControllerDeploymentState extension.

### hnc
    
    
    public hnc: (google.cloud.gkehub.configmanagement.v1alpha.DeploymentState|keyof typeof google.cloud.gkehub.configmanagement.v1alpha.DeploymentState);

HierarchyControllerDeploymentState hnc.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.gkehub.configmanagement.v1alpha.IHierarchyControllerDeploymentState): google.cloud.gkehub.configmanagement.v1alpha.HierarchyControllerDeploymentState;

Creates a new HierarchyControllerDeploymentState instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IHierarchyControllerDeploymentState](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1alpha.ihierarchycontrollerdeploymentstate)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[HierarchyControllerDeploymentState](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1alpha.hierarchycontrollerdeploymentstate)` | HierarchyControllerDeploymentState instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.gkehub.configmanagement.v1alpha.HierarchyControllerDeploymentState;

Decodes a HierarchyControllerDeploymentState message from the specified reader or buffer.

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
`[HierarchyControllerDeploymentState](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1alpha.hierarchycontrollerdeploymentstate)` | HierarchyControllerDeploymentState  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.gkehub.configmanagement.v1alpha.HierarchyControllerDeploymentState;

Decodes a HierarchyControllerDeploymentState message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[HierarchyControllerDeploymentState](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1alpha.hierarchycontrollerdeploymentstate)` | HierarchyControllerDeploymentState  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.gkehub.configmanagement.v1alpha.IHierarchyControllerDeploymentState, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified HierarchyControllerDeploymentState message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IHierarchyControllerDeploymentState](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1alpha.ihierarchycontrollerdeploymentstate)`   
HierarchyControllerDeploymentState message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.gkehub.configmanagement.v1alpha.IHierarchyControllerDeploymentState, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified HierarchyControllerDeploymentState message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IHierarchyControllerDeploymentState](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1alpha.ihierarchycontrollerdeploymentstate)`   
HierarchyControllerDeploymentState message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.gkehub.configmanagement.v1alpha.HierarchyControllerDeploymentState;

Creates a HierarchyControllerDeploymentState message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[HierarchyControllerDeploymentState](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1alpha.hierarchycontrollerdeploymentstate)` | HierarchyControllerDeploymentState  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for HierarchyControllerDeploymentState

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

Converts this HierarchyControllerDeploymentState to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.gkehub.configmanagement.v1alpha.HierarchyControllerDeploymentState, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a HierarchyControllerDeploymentState message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[HierarchyControllerDeploymentState](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.configmanagement.v1alpha.hierarchycontrollerdeploymentstate)`   
HierarchyControllerDeploymentState  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a HierarchyControllerDeploymentState message.

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
