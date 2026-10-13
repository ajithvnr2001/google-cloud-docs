---
url: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awscluster-class
title: Class protos.google.cloud.gkemulticloud.v1.AwsCluster (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:39.504247+00:00
---

# Class protos.google.cloud.gkemulticloud.v1.AwsCluster (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awscluster-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gkemulticloud.v1.AwsCluster (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.4.0  2.3.0  2.1.0  2.0.1  1.5.0  1.1.0  0.3.2  0.1.4 

Represents an AwsCluster.

## Implements

[protos.google.cloud.gkemulticloud.v1.IAwsCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iawscluster)

## Package

[@google-cloud/gkemulticloud](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.gkemulticloud.v1.IAwsCluster);

Constructs a new AwsCluster.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAwsCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iawscluster)`   
Properties to set  
  
## Properties 

### annotations
    
    
    public annotations: { [k: string]: string };

AwsCluster annotations.

### authorization
    
    
    public authorization?: (google.cloud.gkemulticloud.v1.IAwsAuthorization|null);

AwsCluster authorization.

### awsRegion
    
    
    public awsRegion: string;

AwsCluster awsRegion.

### binaryAuthorization
    
    
    public binaryAuthorization?: (google.cloud.gkemulticloud.v1.IBinaryAuthorization|null);

AwsCluster binaryAuthorization.

### clusterCaCertificate
    
    
    public clusterCaCertificate: string;

AwsCluster clusterCaCertificate.

### controlPlane
    
    
    public controlPlane?: (google.cloud.gkemulticloud.v1.IAwsControlPlane|null);

AwsCluster controlPlane.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

AwsCluster createTime.

### description
    
    
    public description: string;

AwsCluster description.

### endpoint
    
    
    public endpoint: string;

AwsCluster endpoint.

### errors
    
    
    public errors: google.cloud.gkemulticloud.v1.IAwsClusterError[];

AwsCluster errors.

### etag
    
    
    public etag: string;

AwsCluster etag.

### fleet
    
    
    public fleet?: (google.cloud.gkemulticloud.v1.IFleet|null);

AwsCluster fleet.

### loggingConfig
    
    
    public loggingConfig?: (google.cloud.gkemulticloud.v1.ILoggingConfig|null);

AwsCluster loggingConfig.

### monitoringConfig
    
    
    public monitoringConfig?: (google.cloud.gkemulticloud.v1.IMonitoringConfig|null);

AwsCluster monitoringConfig.

### name
    
    
    public name: string;

AwsCluster name.

### networking
    
    
    public networking?: (google.cloud.gkemulticloud.v1.IAwsClusterNetworking|null);

AwsCluster networking.

### reconciling
    
    
    public reconciling: boolean;

AwsCluster reconciling.

### state
    
    
    public state: (google.cloud.gkemulticloud.v1.AwsCluster.State|keyof typeof google.cloud.gkemulticloud.v1.AwsCluster.State);

AwsCluster state.

### uid
    
    
    public uid: string;

AwsCluster uid.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

AwsCluster updateTime.

### workloadIdentityConfig
    
    
    public workloadIdentityConfig?: (google.cloud.gkemulticloud.v1.IWorkloadIdentityConfig|null);

AwsCluster workloadIdentityConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.gkemulticloud.v1.IAwsCluster): google.cloud.gkemulticloud.v1.AwsCluster;

Creates a new AwsCluster instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAwsCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iawscluster)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AwsCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awscluster-class)` | AwsCluster instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.gkemulticloud.v1.AwsCluster;

Decodes an AwsCluster message from the specified reader or buffer.

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
`[AwsCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awscluster-class)` | AwsCluster  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.gkemulticloud.v1.AwsCluster;

Decodes an AwsCluster message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AwsCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awscluster-class)` | AwsCluster  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.gkemulticloud.v1.IAwsCluster, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AwsCluster message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAwsCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iawscluster)`   
AwsCluster message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.gkemulticloud.v1.IAwsCluster, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AwsCluster message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAwsCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iawscluster)`   
AwsCluster message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.gkemulticloud.v1.AwsCluster;

Creates an AwsCluster message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AwsCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awscluster-class)` | AwsCluster  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AwsCluster

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

Converts this AwsCluster to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.gkemulticloud.v1.AwsCluster, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AwsCluster message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AwsCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.awscluster-class)`   
AwsCluster  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AwsCluster message.

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
