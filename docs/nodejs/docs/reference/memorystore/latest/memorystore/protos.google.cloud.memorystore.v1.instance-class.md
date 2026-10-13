---
url: https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.instance-class
title: Class protos.google.cloud.memorystore.v1.Instance (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:02:02.995552+00:00
---

# Class protos.google.cloud.memorystore.v1.Instance (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.instance-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.memorystore.v1.Instance (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.7.0  0.4.0  0.1.0 

Represents an Instance.

## Implements

[protos.google.cloud.memorystore.v1.IInstance](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.iinstance)

## Package

[@google-cloud/memorystore](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.memorystore.v1.IInstance);

Constructs a new Instance.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInstance](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.iinstance)`   
Properties to set  
  
## Properties 

### allowFewerZonesDeployment
    
    
    public allowFewerZonesDeployment: boolean;

Instance allowFewerZonesDeployment.

### asyncInstanceEndpointsDeletionEnabled
    
    
    public asyncInstanceEndpointsDeletionEnabled?: (boolean|null);

Instance asyncInstanceEndpointsDeletionEnabled.

### authorizationMode
    
    
    public authorizationMode: (google.cloud.memorystore.v1.Instance.AuthorizationMode|keyof typeof google.cloud.memorystore.v1.Instance.AuthorizationMode);

Instance authorizationMode.

### automatedBackupConfig
    
    
    public automatedBackupConfig?: (google.cloud.memorystore.v1.IAutomatedBackupConfig|null);

Instance automatedBackupConfig.

### availableMaintenanceVersions
    
    
    public availableMaintenanceVersions: string[];

Instance availableMaintenanceVersions.

### backupCollection
    
    
    public backupCollection?: (string|null);

Instance backupCollection.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Instance createTime.

### crossInstanceReplicationConfig
    
    
    public crossInstanceReplicationConfig?: (google.cloud.memorystore.v1.ICrossInstanceReplicationConfig|null);

Instance crossInstanceReplicationConfig.

### deletionProtectionEnabled
    
    
    public deletionProtectionEnabled?: (boolean|null);

Instance deletionProtectionEnabled.

### discoveryEndpoints
    
    
    public discoveryEndpoints: google.cloud.memorystore.v1.IDiscoveryEndpoint[];

Instance discoveryEndpoints.

### effectiveMaintenanceVersion
    
    
    public effectiveMaintenanceVersion?: (string|null);

Instance effectiveMaintenanceVersion.

### encryptionInfo
    
    
    public encryptionInfo?: (google.cloud.memorystore.v1.IEncryptionInfo|null);

Instance encryptionInfo.

### endpoints
    
    
    public endpoints: google.cloud.memorystore.v1.Instance.IInstanceEndpoint[];

Instance endpoints.

### engineConfigs
    
    
    public engineConfigs: { [k: string]: string };

Instance engineConfigs.

### engineVersion
    
    
    public engineVersion: string;

Instance engineVersion.

### gcsSource
    
    
    public gcsSource?: (google.cloud.memorystore.v1.Instance.IGcsBackupSource|null);

Instance gcsSource.

### importSources
    
    
    public importSources?: ("gcsSource"|"managedBackupSource");

Instance importSources.

### kmsKey
    
    
    public kmsKey?: (string|null);

Instance kmsKey.

### labels
    
    
    public labels: { [k: string]: string };

Instance labels.

### maintenancePolicy
    
    
    public maintenancePolicy?: (google.cloud.memorystore.v1.IMaintenancePolicy|null);

Instance maintenancePolicy.

### maintenanceSchedule
    
    
    public maintenanceSchedule?: (google.cloud.memorystore.v1.IMaintenanceSchedule|null);

Instance maintenanceSchedule.

### maintenanceVersion
    
    
    public maintenanceVersion?: (string|null);

Instance maintenanceVersion.

### managedBackupSource
    
    
    public managedBackupSource?: (google.cloud.memorystore.v1.Instance.IManagedBackupSource|null);

Instance managedBackupSource.

### migrationConfig
    
    
    public migrationConfig?: (google.cloud.memorystore.v1.IMigrationConfig|null);

Instance migrationConfig.

### mode
    
    
    public mode: (google.cloud.memorystore.v1.Instance.Mode|keyof typeof google.cloud.memorystore.v1.Instance.Mode);

Instance mode.

### name
    
    
    public name: string;

Instance name.

### nodeConfig
    
    
    public nodeConfig?: (google.cloud.memorystore.v1.INodeConfig|null);

Instance nodeConfig.

### nodeType
    
    
    public nodeType: (google.cloud.memorystore.v1.Instance.NodeType|keyof typeof google.cloud.memorystore.v1.Instance.NodeType);

Instance nodeType.

### ondemandMaintenance
    
    
    public ondemandMaintenance?: (boolean|null);

Instance ondemandMaintenance.

### persistenceConfig
    
    
    public persistenceConfig?: (google.cloud.memorystore.v1.IPersistenceConfig|null);

Instance persistenceConfig.

### pscAttachmentDetails
    
    
    public pscAttachmentDetails: google.cloud.memorystore.v1.IPscAttachmentDetail[];

Instance pscAttachmentDetails.

### pscAutoConnections
    
    
    public pscAutoConnections: google.cloud.memorystore.v1.IPscAutoConnection[];

Instance pscAutoConnections.

### replicaCount
    
    
    public replicaCount?: (number|null);

Instance replicaCount.

### rotateServerCertificate
    
    
    public rotateServerCertificate?: (boolean|null);

Instance rotateServerCertificate.

### satisfiesPzi
    
    
    public satisfiesPzi?: (boolean|null);

Instance satisfiesPzi.

### satisfiesPzs
    
    
    public satisfiesPzs?: (boolean|null);

Instance satisfiesPzs.

### serverCaMode
    
    
    public serverCaMode?: (google.cloud.memorystore.v1.Instance.ServerCaMode|keyof typeof google.cloud.memorystore.v1.Instance.ServerCaMode|null);

Instance serverCaMode.

### serverCaPool
    
    
    public serverCaPool?: (string|null);

Instance serverCaPool.

### shardCount
    
    
    public shardCount: number;

Instance shardCount.

### simulateMaintenanceEvent
    
    
    public simulateMaintenanceEvent?: (boolean|null);

Instance simulateMaintenanceEvent.

### state
    
    
    public state: (google.cloud.memorystore.v1.Instance.State|keyof typeof google.cloud.memorystore.v1.Instance.State);

Instance state.

### stateInfo
    
    
    public stateInfo?: (google.cloud.memorystore.v1.Instance.IStateInfo|null);

Instance stateInfo.

### transitEncryptionMode
    
    
    public transitEncryptionMode: (google.cloud.memorystore.v1.Instance.TransitEncryptionMode|keyof typeof google.cloud.memorystore.v1.Instance.TransitEncryptionMode);

Instance transitEncryptionMode.

### uid
    
    
    public uid: string;

Instance uid.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Instance updateTime.

### zoneDistributionConfig
    
    
    public zoneDistributionConfig?: (google.cloud.memorystore.v1.IZoneDistributionConfig|null);

Instance zoneDistributionConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.memorystore.v1.IInstance): google.cloud.memorystore.v1.Instance;

Creates a new Instance instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInstance](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.iinstance)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.instance-class)` | Instance instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.memorystore.v1.Instance;

Decodes an Instance message from the specified reader or buffer.

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
`[Instance](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.instance-class)` | Instance  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.memorystore.v1.Instance;

Decodes an Instance message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.instance-class)` | Instance  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.memorystore.v1.IInstance, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Instance message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInstance](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.iinstance)`   
Instance message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.memorystore.v1.IInstance, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Instance message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInstance](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.iinstance)`   
Instance message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.memorystore.v1.Instance;

Creates an Instance message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.instance-class)` | Instance  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Instance

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

Converts this Instance to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.memorystore.v1.Instance, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Instance message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Instance](https://docs.cloud.google.com/nodejs/docs/reference/memorystore/latest/memorystore/protos.google.cloud.memorystore.v1.instance-class)`   
Instance  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Instance message.

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
