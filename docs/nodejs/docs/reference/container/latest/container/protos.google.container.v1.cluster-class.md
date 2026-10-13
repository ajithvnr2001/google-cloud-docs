---
url: https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.cluster-class
title: Class protos.google.container.v1.Cluster (7.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:37:35.963209+00:00
---

# Class protos.google.container.v1.Cluster (7.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.cluster-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.container.v1.Cluster (7.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.2.1 (latest)  7.1.0  6.8.0  6.7.0  6.1.0  5.19.0  5.17.0  5.15.1  5.14.0  5.10.0  5.9.0  5.8.0  5.6.0  5.5.0  5.4.1  5.1.0  4.11.0  4.10.0  4.9.0  4.7.1  4.4.0  4.3.0  4.2.0  4.1.3  3.0.0  2.6.0  2.5.0  2.4.4  2.3.2 

Represents a Cluster.

## Implements

[protos.google.container.v1.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.icluster)

## Package

[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.container.v1.ICluster);

Constructs a new Cluster.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICluster](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.icluster)`   
Properties to set  
  
## Properties 

### addonsConfig
    
    
    public addonsConfig?: (google.container.v1.IAddonsConfig|null);

Cluster addonsConfig.

### alphaClusterFeatureGates
    
    
    public alphaClusterFeatureGates: string[];

Cluster alphaClusterFeatureGates.

### anonymousAuthenticationConfig
    
    
    public anonymousAuthenticationConfig?: (google.container.v1.IAnonymousAuthenticationConfig|null);

Cluster anonymousAuthenticationConfig.

### authenticatorGroupsConfig
    
    
    public authenticatorGroupsConfig?: (google.container.v1.IAuthenticatorGroupsConfig|null);

Cluster authenticatorGroupsConfig.

### autopilot
    
    
    public autopilot?: (google.container.v1.IAutopilot|null);

Cluster autopilot.

### autoscaling
    
    
    public autoscaling?: (google.container.v1.IClusterAutoscaling|null);

Cluster autoscaling.

### binaryAuthorization
    
    
    public binaryAuthorization?: (google.container.v1.IBinaryAuthorization|null);

Cluster binaryAuthorization.

### clusterIpv4Cidr
    
    
    public clusterIpv4Cidr: string;

Cluster clusterIpv4Cidr.

### compliancePostureConfig
    
    
    public compliancePostureConfig?: (google.container.v1.ICompliancePostureConfig|null);

Cluster compliancePostureConfig.

### conditions
    
    
    public conditions: google.container.v1.IStatusCondition[];

Cluster conditions.

### confidentialNodes
    
    
    public confidentialNodes?: (google.container.v1.IConfidentialNodes|null);

Cluster confidentialNodes.

### controlPlaneEgress
    
    
    public controlPlaneEgress?: (google.container.v1.IControlPlaneEgress|null);

Cluster controlPlaneEgress.

### controlPlaneEndpointsConfig
    
    
    public controlPlaneEndpointsConfig?: (google.container.v1.IControlPlaneEndpointsConfig|null);

Cluster controlPlaneEndpointsConfig.

### costManagementConfig
    
    
    public costManagementConfig?: (google.container.v1.ICostManagementConfig|null);

Cluster costManagementConfig.

### createTime
    
    
    public createTime: string;

Cluster createTime.

### currentEmulatedVersion
    
    
    public currentEmulatedVersion: string;

Cluster currentEmulatedVersion.

### currentMasterVersion
    
    
    public currentMasterVersion: string;

Cluster currentMasterVersion.

### currentNodeCount
    
    
    public currentNodeCount: number;

Cluster currentNodeCount.

### currentNodeVersion
    
    
    public currentNodeVersion: string;

Cluster currentNodeVersion.

### databaseEncryption
    
    
    public databaseEncryption?: (google.container.v1.IDatabaseEncryption|null);

Cluster databaseEncryption.

### defaultMaxPodsConstraint
    
    
    public defaultMaxPodsConstraint?: (google.container.v1.IMaxPodsConstraint|null);

Cluster defaultMaxPodsConstraint.

### description
    
    
    public description: string;

Cluster description.

### enableK8sBetaApis
    
    
    public enableK8sBetaApis?: (google.container.v1.IK8sBetaAPIConfig|null);

Cluster enableK8sBetaApis.

### enableKubernetesAlpha
    
    
    public enableKubernetesAlpha: boolean;

Cluster enableKubernetesAlpha.

### enableTpu
    
    
    public enableTpu: boolean;

Cluster enableTpu.

### endpoint
    
    
    public endpoint: string;

Cluster endpoint.

### enterpriseConfig
    
    
    public enterpriseConfig?: (google.container.v1.IEnterpriseConfig|null);

Cluster enterpriseConfig.

### etag
    
    
    public etag: string;

Cluster etag.

### expireTime
    
    
    public expireTime: string;

Cluster expireTime.

### fleet
    
    
    public fleet?: (google.container.v1.IFleet|null);

Cluster fleet.

### gkeAutoUpgradeConfig
    
    
    public gkeAutoUpgradeConfig?: (google.container.v1.IGkeAutoUpgradeConfig|null);

Cluster gkeAutoUpgradeConfig.

### id
    
    
    public id: string;

Cluster id.

### identityServiceConfig
    
    
    public identityServiceConfig?: (google.container.v1.IIdentityServiceConfig|null);

Cluster identityServiceConfig.

### initialClusterVersion
    
    
    public initialClusterVersion: string;

Cluster initialClusterVersion.

### initialNodeCount
    
    
    public initialNodeCount: number;

Cluster initialNodeCount.

### instanceGroupUrls
    
    
    public instanceGroupUrls: string[];

Cluster instanceGroupUrls.

### ipAllocationPolicy
    
    
    public ipAllocationPolicy?: (google.container.v1.IIPAllocationPolicy|null);

Cluster ipAllocationPolicy.

### labelFingerprint
    
    
    public labelFingerprint: string;

Cluster labelFingerprint.

### legacyAbac
    
    
    public legacyAbac?: (google.container.v1.ILegacyAbac|null);

Cluster legacyAbac.

### location
    
    
    public location: string;

Cluster location.

### locations
    
    
    public locations: string[];

Cluster locations.

### loggingConfig
    
    
    public loggingConfig?: (google.container.v1.ILoggingConfig|null);

Cluster loggingConfig.

### loggingService
    
    
    public loggingService: string;

Cluster loggingService.

### maintenancePolicy
    
    
    public maintenancePolicy?: (google.container.v1.IMaintenancePolicy|null);

Cluster maintenancePolicy.

### managedMachineLearningDiagnosticsConfig
    
    
    public managedMachineLearningDiagnosticsConfig?: (google.container.v1.IManagedMachineLearningDiagnosticsConfig|null);

Cluster managedMachineLearningDiagnosticsConfig.

### managedOpentelemetryConfig
    
    
    public managedOpentelemetryConfig?: (google.container.v1.IManagedOpenTelemetryConfig|null);

Cluster managedOpentelemetryConfig.

### masterAuth
    
    
    public masterAuth?: (google.container.v1.IMasterAuth|null);

Cluster masterAuth.

### masterAuthorizedNetworksConfig
    
    
    public masterAuthorizedNetworksConfig?: (google.container.v1.IMasterAuthorizedNetworksConfig|null);

Cluster masterAuthorizedNetworksConfig.

### meshCertificates
    
    
    public meshCertificates?: (google.container.v1.IMeshCertificates|null);

Cluster meshCertificates.

### monitoringConfig
    
    
    public monitoringConfig?: (google.container.v1.IMonitoringConfig|null);

Cluster monitoringConfig.

### monitoringService
    
    
    public monitoringService: string;

Cluster monitoringService.

### name
    
    
    public name: string;

Cluster name.

### network
    
    
    public network: string;

Cluster network.

### networkConfig
    
    
    public networkConfig?: (google.container.v1.INetworkConfig|null);

Cluster networkConfig.

### networkPolicy
    
    
    public networkPolicy?: (google.container.v1.INetworkPolicy|null);

Cluster networkPolicy.

### nodeConfig
    
    
    public nodeConfig?: (google.container.v1.INodeConfig|null);

Cluster nodeConfig.

### nodeCreationConfig
    
    
    public nodeCreationConfig?: (google.container.v1.INodeCreationConfig|null);

Cluster nodeCreationConfig.

### nodeIpv4CidrSize
    
    
    public nodeIpv4CidrSize: number;

Cluster nodeIpv4CidrSize.

### nodePoolAutoConfig
    
    
    public nodePoolAutoConfig?: (google.container.v1.INodePoolAutoConfig|null);

Cluster nodePoolAutoConfig.

### nodePoolDefaults
    
    
    public nodePoolDefaults?: (google.container.v1.INodePoolDefaults|null);

Cluster nodePoolDefaults.

### nodePools
    
    
    public nodePools: google.container.v1.INodePool[];

Cluster nodePools.

### notificationConfig
    
    
    public notificationConfig?: (google.container.v1.INotificationConfig|null);

Cluster notificationConfig.

### podAutoscaling
    
    
    public podAutoscaling?: (google.container.v1.IPodAutoscaling|null);

Cluster podAutoscaling.

### privateClusterConfig
    
    
    public privateClusterConfig?: (google.container.v1.IPrivateClusterConfig|null);

Cluster privateClusterConfig.

### rbacBindingConfig
    
    
    public rbacBindingConfig?: (google.container.v1.IRBACBindingConfig|null);

Cluster rbacBindingConfig.

### releaseChannel
    
    
    public releaseChannel?: (google.container.v1.IReleaseChannel|null);

Cluster releaseChannel.

### resourceLabels
    
    
    public resourceLabels: { [k: string]: string };

Cluster resourceLabels.

### resourceUsageExportConfig
    
    
    public resourceUsageExportConfig?: (google.container.v1.IResourceUsageExportConfig|null);

Cluster resourceUsageExportConfig.

### rollbackSafeUpgrade
    
    
    public rollbackSafeUpgrade?: (google.container.v1.IRollbackSafeUpgrade|null);

Cluster rollbackSafeUpgrade.

### satisfiesPzi
    
    
    public satisfiesPzi?: (boolean|null);

Cluster satisfiesPzi.

### satisfiesPzs
    
    
    public satisfiesPzs?: (boolean|null);

Cluster satisfiesPzs.

### scheduleUpgradeConfig
    
    
    public scheduleUpgradeConfig?: (google.container.v1.IScheduleUpgradeConfig|null);

Cluster scheduleUpgradeConfig.

### secretManagerConfig
    
    
    public secretManagerConfig?: (google.container.v1.ISecretManagerConfig|null);

Cluster secretManagerConfig.

### secretSyncConfig
    
    
    public secretSyncConfig?: (google.container.v1.ISecretSyncConfig|null);

Cluster secretSyncConfig.

### securityPostureConfig
    
    
    public securityPostureConfig?: (google.container.v1.ISecurityPostureConfig|null);

Cluster securityPostureConfig.

### selfLink
    
    
    public selfLink: string;

Cluster selfLink.

### servicesIpv4Cidr
    
    
    public servicesIpv4Cidr: string;

Cluster servicesIpv4Cidr.

### shieldedNodes
    
    
    public shieldedNodes?: (google.container.v1.IShieldedNodes|null);

Cluster shieldedNodes.

### status
    
    
    public status: (google.container.v1.Cluster.Status|keyof typeof google.container.v1.Cluster.Status);

Cluster status.

### statusMessage
    
    
    public statusMessage: string;

Cluster statusMessage.

### subnetwork
    
    
    public subnetwork: string;

Cluster subnetwork.

### tpuIpv4CidrBlock
    
    
    public tpuIpv4CidrBlock: string;

Cluster tpuIpv4CidrBlock.

### userManagedKeysConfig
    
    
    public userManagedKeysConfig?: (google.container.v1.IUserManagedKeysConfig|null);

Cluster userManagedKeysConfig.

### verticalPodAutoscaling
    
    
    public verticalPodAutoscaling?: (google.container.v1.IVerticalPodAutoscaling|null);

Cluster verticalPodAutoscaling.

### workloadIdentityConfig
    
    
    public workloadIdentityConfig?: (google.container.v1.IWorkloadIdentityConfig|null);

Cluster workloadIdentityConfig.

### zone
    
    
    public zone: string;

Cluster zone.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.container.v1.ICluster): google.container.v1.Cluster;

Creates a new Cluster instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICluster](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.icluster)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.cluster-class)` | Cluster instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.container.v1.Cluster;

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
`[Cluster](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.cluster-class)` | Cluster  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.container.v1.Cluster;

Decodes a Cluster message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.cluster-class)` | Cluster  
  
### encode(message, writer)
    
    
    public static encode(message: google.container.v1.ICluster, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Cluster message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICluster](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.icluster)`   
Cluster message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.container.v1.ICluster, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Cluster message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICluster](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.icluster)`   
Cluster message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.container.v1.Cluster;

Creates a Cluster message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.cluster-class)` | Cluster  
  
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
    
    
    public static toObject(message: google.container.v1.Cluster, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Cluster message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Cluster](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.cluster-class)`   
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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
