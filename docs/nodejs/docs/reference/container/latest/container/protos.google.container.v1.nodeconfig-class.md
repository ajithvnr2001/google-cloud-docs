---
url: https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.nodeconfig-class
title: Class protos.google.container.v1.NodeConfig (7.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:12.708651+00:00
---

# Class protos.google.container.v1.NodeConfig (7.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.nodeconfig-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.container.v1.NodeConfig (7.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.2.1 (latest)  7.1.0  6.8.0  6.7.0  6.1.0  5.19.0  5.17.0  5.15.1  5.14.0  5.10.0  5.9.0  5.8.0  5.6.0  5.5.0  5.4.1  5.1.0  4.11.0  4.10.0  4.9.0  4.7.1  4.4.0  4.3.0  4.2.0  4.1.3  3.0.0  2.6.0  2.5.0  2.4.4  2.3.2 

Represents a NodeConfig.

## Implements

[protos.google.container.v1.INodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.inodeconfig)

## Package

[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.container.v1.INodeConfig);

Constructs a new NodeConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.inodeconfig)`   
Properties to set  
  
## Properties 

### accelerators
    
    
    public accelerators: google.container.v1.IAcceleratorConfig[];

NodeConfig accelerators.

### advancedMachineFeatures
    
    
    public advancedMachineFeatures?: (google.container.v1.IAdvancedMachineFeatures|null);

NodeConfig advancedMachineFeatures.

### bootDisk
    
    
    public bootDisk?: (google.container.v1.IBootDisk|null);

NodeConfig bootDisk.

### bootDiskKmsKey
    
    
    public bootDiskKmsKey: string;

NodeConfig bootDiskKmsKey.

### confidentialNodes
    
    
    public confidentialNodes?: (google.container.v1.IConfidentialNodes|null);

NodeConfig confidentialNodes.

### consolidationDelay
    
    
    public consolidationDelay?: (google.protobuf.IDuration|null);

NodeConfig consolidationDelay.

### containerdConfig
    
    
    public containerdConfig?: (google.container.v1.IContainerdConfig|null);

NodeConfig containerdConfig.

### diskSizeGb
    
    
    public diskSizeGb: number;

NodeConfig diskSizeGb.

### diskType
    
    
    public diskType: string;

NodeConfig diskType.

### effectiveCgroupMode
    
    
    public effectiveCgroupMode: (google.container.v1.NodeConfig.EffectiveCgroupMode|keyof typeof google.container.v1.NodeConfig.EffectiveCgroupMode);

NodeConfig effectiveCgroupMode.

### enableConfidentialStorage
    
    
    public enableConfidentialStorage: boolean;

NodeConfig enableConfidentialStorage.

### ephemeralStorageLocalSsdConfig
    
    
    public ephemeralStorageLocalSsdConfig?: (google.container.v1.IEphemeralStorageLocalSsdConfig|null);

NodeConfig ephemeralStorageLocalSsdConfig.

### fastSocket
    
    
    public fastSocket?: (google.container.v1.IFastSocket|null);

NodeConfig fastSocket.

### flexStart
    
    
    public flexStart?: (boolean|null);

NodeConfig flexStart.

### gcfsConfig
    
    
    public gcfsConfig?: (google.container.v1.IGcfsConfig|null);

NodeConfig gcfsConfig.

### gpuDirectConfig
    
    
    public gpuDirectConfig?: (google.container.v1.IGPUDirectConfig|null);

NodeConfig gpuDirectConfig.

### gvnic
    
    
    public gvnic?: (google.container.v1.IVirtualNIC|null);

NodeConfig gvnic.

### imageType
    
    
    public imageType: string;

NodeConfig imageType.

### kubeletConfig
    
    
    public kubeletConfig?: (google.container.v1.INodeKubeletConfig|null);

NodeConfig kubeletConfig.

### labels
    
    
    public labels: { [k: string]: string };

NodeConfig labels.

### linuxNodeConfig
    
    
    public linuxNodeConfig?: (google.container.v1.ILinuxNodeConfig|null);

NodeConfig linuxNodeConfig.

### localNvmeSsdBlockConfig
    
    
    public localNvmeSsdBlockConfig?: (google.container.v1.ILocalNvmeSsdBlockConfig|null);

NodeConfig localNvmeSsdBlockConfig.

### localSsdCount
    
    
    public localSsdCount: number;

NodeConfig localSsdCount.

### localSsdEncryptionMode
    
    
    public localSsdEncryptionMode?: (google.container.v1.NodeConfig.LocalSsdEncryptionMode|keyof typeof google.container.v1.NodeConfig.LocalSsdEncryptionMode|null);

NodeConfig localSsdEncryptionMode.

### loggingConfig
    
    
    public loggingConfig?: (google.container.v1.INodePoolLoggingConfig|null);

NodeConfig loggingConfig.

### machineType
    
    
    public machineType: string;

NodeConfig machineType.

### maxRunDuration
    
    
    public maxRunDuration?: (google.protobuf.IDuration|null);

NodeConfig maxRunDuration.

### metadata
    
    
    public metadata: { [k: string]: string };

NodeConfig metadata.

### minCpuPlatform
    
    
    public minCpuPlatform: string;

NodeConfig minCpuPlatform.

### nodeGroup
    
    
    public nodeGroup: string;

NodeConfig nodeGroup.

### nodeImageConfig
    
    
    public nodeImageConfig?: (google.container.v1.ICustomImageConfig|null);

NodeConfig nodeImageConfig.

### oauthScopes
    
    
    public oauthScopes: string[];

NodeConfig oauthScopes.

### preemptible
    
    
    public preemptible: boolean;

NodeConfig preemptible.

### reservationAffinity
    
    
    public reservationAffinity?: (google.container.v1.IReservationAffinity|null);

NodeConfig reservationAffinity.

### resourceLabels
    
    
    public resourceLabels: { [k: string]: string };

NodeConfig resourceLabels.

### resourceManagerTags
    
    
    public resourceManagerTags?: (google.container.v1.IResourceManagerTags|null);

NodeConfig resourceManagerTags.

### sandboxConfig
    
    
    public sandboxConfig?: (google.container.v1.ISandboxConfig|null);

NodeConfig sandboxConfig.

### secondaryBootDisks
    
    
    public secondaryBootDisks: google.container.v1.ISecondaryBootDisk[];

NodeConfig secondaryBootDisks.

### secondaryBootDiskUpdateStrategy
    
    
    public secondaryBootDiskUpdateStrategy?: (google.container.v1.ISecondaryBootDiskUpdateStrategy|null);

NodeConfig secondaryBootDiskUpdateStrategy.

### serviceAccount
    
    
    public serviceAccount: string;

NodeConfig serviceAccount.

### shieldedInstanceConfig
    
    
    public shieldedInstanceConfig?: (google.container.v1.IShieldedInstanceConfig|null);

NodeConfig shieldedInstanceConfig.

### soleTenantConfig
    
    
    public soleTenantConfig?: (google.container.v1.ISoleTenantConfig|null);

NodeConfig soleTenantConfig.

### spot
    
    
    public spot: boolean;

NodeConfig spot.

### storagePools
    
    
    public storagePools: string[];

NodeConfig storagePools.

### tags
    
    
    public tags: string[];

NodeConfig tags.

### taintConfig
    
    
    public taintConfig?: (google.container.v1.ITaintConfig|null);

NodeConfig taintConfig.

### taints
    
    
    public taints: google.container.v1.INodeTaint[];

NodeConfig taints.

### windowsNodeConfig
    
    
    public windowsNodeConfig?: (google.container.v1.IWindowsNodeConfig|null);

NodeConfig windowsNodeConfig.

### workloadMetadataConfig
    
    
    public workloadMetadataConfig?: (google.container.v1.IWorkloadMetadataConfig|null);

NodeConfig workloadMetadataConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.container.v1.INodeConfig): google.container.v1.NodeConfig;

Creates a new NodeConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.inodeconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[NodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.nodeconfig-class)` | NodeConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.container.v1.NodeConfig;

Decodes a NodeConfig message from the specified reader or buffer.

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
`[NodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.nodeconfig-class)` | NodeConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.container.v1.NodeConfig;

Decodes a NodeConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[NodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.nodeconfig-class)` | NodeConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.container.v1.INodeConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified NodeConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.inodeconfig)`   
NodeConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.container.v1.INodeConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified NodeConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.inodeconfig)`   
NodeConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.container.v1.NodeConfig;

Creates a NodeConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[NodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.nodeconfig-class)` | NodeConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for NodeConfig

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

Converts this NodeConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.container.v1.NodeConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a NodeConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[NodeConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.nodeconfig-class)`   
NodeConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a NodeConfig message.

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
