---
url: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azurecluster-class
title: Class protos.google.cloud.gkemulticloud.v1.AzureCluster (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:44.218367+00:00
---

# Class protos.google.cloud.gkemulticloud.v1.AzureCluster (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azurecluster-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gkemulticloud.v1.AzureCluster (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.4.0  2.3.0  2.1.0  2.0.1  1.5.0  1.1.0  0.3.2  0.1.4 

Represents an AzureCluster.

## Implements

[protos.google.cloud.gkemulticloud.v1.IAzureCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iazurecluster)

## Package

[@google-cloud/gkemulticloud](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.gkemulticloud.v1.IAzureCluster);

Constructs a new AzureCluster.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAzureCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iazurecluster)`   
Properties to set  
  
## Properties 

### annotations
    
    
    public annotations: { [k: string]: string };

AzureCluster annotations.

### authorization
    
    
    public authorization?: (google.cloud.gkemulticloud.v1.IAzureAuthorization|null);

AzureCluster authorization.

### azureClient
    
    
    public azureClient: string;

AzureCluster azureClient.

### azureRegion
    
    
    public azureRegion: string;

AzureCluster azureRegion.

### azureServicesAuthentication
    
    
    public azureServicesAuthentication?: (google.cloud.gkemulticloud.v1.IAzureServicesAuthentication|null);

AzureCluster azureServicesAuthentication.

### clusterCaCertificate
    
    
    public clusterCaCertificate: string;

AzureCluster clusterCaCertificate.

### controlPlane
    
    
    public controlPlane?: (google.cloud.gkemulticloud.v1.IAzureControlPlane|null);

AzureCluster controlPlane.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

AzureCluster createTime.

### description
    
    
    public description: string;

AzureCluster description.

### endpoint
    
    
    public endpoint: string;

AzureCluster endpoint.

### errors
    
    
    public errors: google.cloud.gkemulticloud.v1.IAzureClusterError[];

AzureCluster errors.

### etag
    
    
    public etag: string;

AzureCluster etag.

### fleet
    
    
    public fleet?: (google.cloud.gkemulticloud.v1.IFleet|null);

AzureCluster fleet.

### loggingConfig
    
    
    public loggingConfig?: (google.cloud.gkemulticloud.v1.ILoggingConfig|null);

AzureCluster loggingConfig.

### managedResources
    
    
    public managedResources?: (google.cloud.gkemulticloud.v1.IAzureClusterResources|null);

AzureCluster managedResources.

### monitoringConfig
    
    
    public monitoringConfig?: (google.cloud.gkemulticloud.v1.IMonitoringConfig|null);

AzureCluster monitoringConfig.

### name
    
    
    public name: string;

AzureCluster name.

### networking
    
    
    public networking?: (google.cloud.gkemulticloud.v1.IAzureClusterNetworking|null);

AzureCluster networking.

### reconciling
    
    
    public reconciling: boolean;

AzureCluster reconciling.

### resourceGroupId
    
    
    public resourceGroupId: string;

AzureCluster resourceGroupId.

### state
    
    
    public state: (google.cloud.gkemulticloud.v1.AzureCluster.State|keyof typeof google.cloud.gkemulticloud.v1.AzureCluster.State);

AzureCluster state.

### uid
    
    
    public uid: string;

AzureCluster uid.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

AzureCluster updateTime.

### workloadIdentityConfig
    
    
    public workloadIdentityConfig?: (google.cloud.gkemulticloud.v1.IWorkloadIdentityConfig|null);

AzureCluster workloadIdentityConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.gkemulticloud.v1.IAzureCluster): google.cloud.gkemulticloud.v1.AzureCluster;

Creates a new AzureCluster instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAzureCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iazurecluster)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AzureCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azurecluster-class)` | AzureCluster instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.gkemulticloud.v1.AzureCluster;

Decodes an AzureCluster message from the specified reader or buffer.

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
`[AzureCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azurecluster-class)` | AzureCluster  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.gkemulticloud.v1.AzureCluster;

Decodes an AzureCluster message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AzureCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azurecluster-class)` | AzureCluster  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.gkemulticloud.v1.IAzureCluster, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AzureCluster message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAzureCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iazurecluster)`   
AzureCluster message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.gkemulticloud.v1.IAzureCluster, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AzureCluster message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAzureCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.iazurecluster)`   
AzureCluster message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.gkemulticloud.v1.AzureCluster;

Creates an AzureCluster message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AzureCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azurecluster-class)` | AzureCluster  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AzureCluster

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

Converts this AzureCluster to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.gkemulticloud.v1.AzureCluster, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AzureCluster message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AzureCluster](https://docs.cloud.google.com/nodejs/docs/reference/gkemulticloud/latest/gkemulticloud/protos.google.cloud.gkemulticloud.v1.azurecluster-class)`   
AzureCluster  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AzureCluster message.

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
