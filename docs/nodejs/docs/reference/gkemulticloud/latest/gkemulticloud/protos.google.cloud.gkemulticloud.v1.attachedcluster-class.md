---
url: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.attachedcluster-class
title: Class protos.google.cloud.gkemulticloud.v1.AttachedCluster (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:36.421235+00:00
---

# Class protos.google.cloud.gkemulticloud.v1.AttachedCluster (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.attachedcluster-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gkemulticloud.v1.AttachedCluster (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.4.0  2.3.0  2.1.0  2.0.1  1.5.0  1.1.0  0.3.2  0.1.4 

Represents an AttachedCluster.

## Implements

[protos.google.cloud.gkemulticloud.v1.IAttachedCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iattachedcluster)

## Package

[@google-cloud/gkemulticloud](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.gkemulticloud.v1.IAttachedCluster);

Constructs a new AttachedCluster.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAttachedCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iattachedcluster)`   
Properties to set  
  
## Properties 

### annotations
    
    
    public annotations: { [k: string]: string };

AttachedCluster annotations.

### authorization
    
    
    public authorization?: (google.cloud.gkemulticloud.v1.IAttachedClustersAuthorization|null);

AttachedCluster authorization.

### binaryAuthorization
    
    
    public binaryAuthorization?: (google.cloud.gkemulticloud.v1.IBinaryAuthorization|null);

AttachedCluster binaryAuthorization.

### clusterRegion
    
    
    public clusterRegion: string;

AttachedCluster clusterRegion.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

AttachedCluster createTime.

### description
    
    
    public description: string;

AttachedCluster description.

### distribution
    
    
    public distribution: string;

AttachedCluster distribution.

### errors
    
    
    public errors: google.cloud.gkemulticloud.v1.IAttachedClusterError[];

AttachedCluster errors.

### etag
    
    
    public etag: string;

AttachedCluster etag.

### fleet
    
    
    public fleet?: (google.cloud.gkemulticloud.v1.IFleet|null);

AttachedCluster fleet.

### kubernetesVersion
    
    
    public kubernetesVersion: string;

AttachedCluster kubernetesVersion.

### loggingConfig
    
    
    public loggingConfig?: (google.cloud.gkemulticloud.v1.ILoggingConfig|null);

AttachedCluster loggingConfig.

### monitoringConfig
    
    
    public monitoringConfig?: (google.cloud.gkemulticloud.v1.IMonitoringConfig|null);

AttachedCluster monitoringConfig.

### name
    
    
    public name: string;

AttachedCluster name.

### oidcConfig
    
    
    public oidcConfig?: (google.cloud.gkemulticloud.v1.IAttachedOidcConfig|null);

AttachedCluster oidcConfig.

### platformVersion
    
    
    public platformVersion: string;

AttachedCluster platformVersion.

### proxyConfig
    
    
    public proxyConfig?: (google.cloud.gkemulticloud.v1.IAttachedProxyConfig|null);

AttachedCluster proxyConfig.

### reconciling
    
    
    public reconciling: boolean;

AttachedCluster reconciling.

### securityPostureConfig
    
    
    public securityPostureConfig?: (google.cloud.gkemulticloud.v1.ISecurityPostureConfig|null);

AttachedCluster securityPostureConfig.

### state
    
    
    public state: (google.cloud.gkemulticloud.v1.AttachedCluster.State|keyof typeof google.cloud.gkemulticloud.v1.AttachedCluster.State);

AttachedCluster state.

### systemComponentsConfig
    
    
    public systemComponentsConfig?: (google.cloud.gkemulticloud.v1.ISystemComponentsConfig|null);

AttachedCluster systemComponentsConfig.

### tags
    
    
    public tags: { [k: string]: string };

AttachedCluster tags.

### uid
    
    
    public uid: string;

AttachedCluster uid.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

AttachedCluster updateTime.

### workloadIdentityConfig
    
    
    public workloadIdentityConfig?: (google.cloud.gkemulticloud.v1.IWorkloadIdentityConfig|null);

AttachedCluster workloadIdentityConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.gkemulticloud.v1.IAttachedCluster): google.cloud.gkemulticloud.v1.AttachedCluster;

Creates a new AttachedCluster instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAttachedCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iattachedcluster)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AttachedCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.attachedcluster-class)` | AttachedCluster instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.gkemulticloud.v1.AttachedCluster;

Decodes an AttachedCluster message from the specified reader or buffer.

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
`[AttachedCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.attachedcluster-class)` | AttachedCluster  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.gkemulticloud.v1.AttachedCluster;

Decodes an AttachedCluster message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AttachedCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.attachedcluster-class)` | AttachedCluster  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.gkemulticloud.v1.IAttachedCluster, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AttachedCluster message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAttachedCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iattachedcluster)`   
AttachedCluster message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.gkemulticloud.v1.IAttachedCluster, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AttachedCluster message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAttachedCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iattachedcluster)`   
AttachedCluster message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.gkemulticloud.v1.AttachedCluster;

Creates an AttachedCluster message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AttachedCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.attachedcluster-class)` | AttachedCluster  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AttachedCluster

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

Converts this AttachedCluster to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.gkemulticloud.v1.AttachedCluster, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AttachedCluster message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AttachedCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.attachedcluster-class)`   
AttachedCluster  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AttachedCluster message.

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
