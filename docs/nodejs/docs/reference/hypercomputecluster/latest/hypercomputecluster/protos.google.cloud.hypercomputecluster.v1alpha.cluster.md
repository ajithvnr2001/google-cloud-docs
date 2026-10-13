---
url: https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.cluster
title: Class protos.google.cloud.hypercomputecluster.v1alpha.Cluster (0.5.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:23:06.713813+00:00
---

# Class protos.google.cloud.hypercomputecluster.v1alpha.Cluster (0.5.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.cluster

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.hypercomputecluster.v1alpha.Cluster (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.2.0  0.1.0 

Represents a Cluster.

## Implements

[protos.google.cloud.hypercomputecluster.v1alpha.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icluster)

## Package

[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.hypercomputecluster.v1alpha.ICluster);

Constructs a new Cluster.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icluster)`   
Properties to set  
  
## Properties 

### compute
    
    
    public compute?: (google.cloud.hypercomputecluster.v1alpha.ICompute|null);

Cluster compute.

### computeResources
    
    
    public computeResources: { [k: string]: google.cloud.hypercomputecluster.v1alpha.IComputeResource };

Cluster computeResources.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Cluster createTime.

### description
    
    
    public description: string;

Cluster description.

### labels
    
    
    public labels: { [k: string]: string };

Cluster labels.

### maintenancePolicy
    
    
    public maintenancePolicy?: (google.cloud.hypercomputecluster.v1alpha.IMaintenancePolicy|null);

Cluster maintenancePolicy.

### name
    
    
    public name: string;

Cluster name.

### networkResources
    
    
    public networkResources: { [k: string]: google.cloud.hypercomputecluster.v1alpha.INetworkResource };

Cluster networkResources.

### orchestrator
    
    
    public orchestrator?: (google.cloud.hypercomputecluster.v1alpha.IOrchestrator|null);

Cluster orchestrator.

### reconciling
    
    
    public reconciling: boolean;

Cluster reconciling.

### storageResources
    
    
    public storageResources: { [k: string]: google.cloud.hypercomputecluster.v1alpha.IStorageResource };

Cluster storageResources.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Cluster updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.hypercomputecluster.v1alpha.ICluster): google.cloud.hypercomputecluster.v1alpha.Cluster;

Creates a new Cluster instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icluster)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.cluster)` | Cluster instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.hypercomputecluster.v1alpha.Cluster;

Decodes a Cluster message from the specified reader or buffer.

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
`[Cluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.cluster)` | Cluster  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.hypercomputecluster.v1alpha.Cluster;

Decodes a Cluster message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.cluster)` | Cluster  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.hypercomputecluster.v1alpha.ICluster, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Cluster message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icluster)`   
Cluster message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.hypercomputecluster.v1alpha.ICluster, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Cluster message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.icluster)`   
Cluster message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.hypercomputecluster.v1alpha.Cluster;

Creates a Cluster message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.cluster)` | Cluster  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Cluster

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

Converts this Cluster to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.hypercomputecluster.v1alpha.Cluster, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Cluster message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Cluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1alpha.cluster)`   
Cluster  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Cluster message.

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
