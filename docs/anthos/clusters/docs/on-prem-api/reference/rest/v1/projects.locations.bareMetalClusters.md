---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest/v1/projects.locations.bareMetalClusters
title: REST Resource: projects.locations.bareMetalClusters \u00a0|\u00a0 GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:16.470927+00:00
---

# REST Resource: projects.locations.bareMetalClusters  |  GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest/v1/projects.locations.bareMetalClusters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  REST Resource: projects.locations.bareMetalClusters Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: BareMetalCluster
    * JSON representation
  * State
  * BareMetalNetworkConfig
    * JSON representation
  * BareMetalIslandModeCidrConfig
    * JSON representation
  * BareMetalMultipleNetworkInterfacesConfig
    * JSON representation
  * BareMetalSrIovConfig
    * JSON representation
  * BareMetalControlPlaneConfig
    * JSON representation
  * BareMetalControlPlaneNodePoolConfig
    * JSON representation
  * BareMetalApiServerArgument
    * JSON representation
  * BareMetalLoadBalancerConfig
    * JSON representation
  * BareMetalVipConfig
    * JSON representation
  * BareMetalPortConfig
    * JSON representation
  * BareMetalMetalLbConfig
    * JSON representation
  * BareMetalLoadBalancerAddressPool
    * JSON representation
  * BareMetalLoadBalancerNodePoolConfig
    * JSON representation
  * BareMetalManualLbConfig
    * JSON representation
  * BareMetalBgpLbConfig
    * JSON representation
  * BareMetalBgpPeerConfig
    * JSON representation
  * BareMetalStorageConfig
    * JSON representation
  * BareMetalProxyConfig
    * JSON representation
  * BareMetalClusterOperationsConfig
    * JSON representation
  * BareMetalMaintenanceConfig
    * JSON representation
  * BareMetalWorkloadNodeConfig
    * JSON representation
  * ContainerRuntime
  * BareMetalSecurityConfig
    * JSON representation
  * BareMetalMaintenanceStatus
    * JSON representation
  * BareMetalMachineDrainStatus
    * JSON representation
  * BareMetalDrainingMachine
    * JSON representation
  * BareMetalDrainedMachine
    * JSON representation
  * BareMetalNodeAccessConfig
    * JSON representation
  * BareMetalOsEnvironmentConfig
    * JSON representation
  * BareMetalClusterUpgradePolicy
    * JSON representation
  * NodePoolPolicy
  * Methods



## Resource: BareMetalCluster

Resource that represents a bare metal user cluster.

JSON representation  
---  
      
    
    {
      "name": string,
      "adminClusterMembership": string,
      "description": string,
      "bareMetalVersion": string,
      "uid": string,
      "state": enum ([State](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#State)),
      "endpoint": string,
      "reconciling": boolean,
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "localName": string,
      "etag": string,
      "annotations": {
        string: string,
        ...
      },
      "networkConfig": {
        object ([BareMetalNetworkConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalNetworkConfig))
      },
      "controlPlane": {
        object ([BareMetalControlPlaneConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalControlPlaneConfig))
      },
      "loadBalancer": {
        object ([BareMetalLoadBalancerConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalLoadBalancerConfig))
      },
      "storage": {
        object ([BareMetalStorageConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalStorageConfig))
      },
      "proxy": {
        object ([BareMetalProxyConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalProxyConfig))
      },
      "clusterOperations": {
        object ([BareMetalClusterOperationsConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalClusterOperationsConfig))
      },
      "maintenanceConfig": {
        object ([BareMetalMaintenanceConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalMaintenanceConfig))
      },
      "nodeConfig": {
        object ([BareMetalWorkloadNodeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalWorkloadNodeConfig))
      },
      "fleet": {
        object ([Fleet](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/Fleet))
      },
      "status": {
        object ([ResourceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus))
      },
      "validationCheck": {
        object ([ValidationCheck](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ValidationCheck))
      },
      "securityConfig": {
        object ([BareMetalSecurityConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalSecurityConfig))
      },
      "maintenanceStatus": {
        object ([BareMetalMaintenanceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalMaintenanceStatus))
      },
      "adminClusterName": string,
      "nodeAccessConfig": {
        object ([BareMetalNodeAccessConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalNodeAccessConfig))
      },
      "osEnvironmentConfig": {
        object ([BareMetalOsEnvironmentConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalOsEnvironmentConfig))
      },
      "binaryAuthorization": {
        object ([BinaryAuthorization](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BinaryAuthorization))
      },
      "upgradePolicy": {
        object ([BareMetalClusterUpgradePolicy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalClusterUpgradePolicy))
      },
      "localNamespace": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. The bare metal user cluster resource name.  
`adminClusterMembership` |  `string` Required. The admin cluster this bare metal user cluster belongs to. This is the full resource name of the admin cluster's fleet membership.  
`description` |  `string` A human readable description of this bare metal user cluster.  
`bareMetalVersion` |  `string` Required. The Anthos clusters on bare metal version for your user cluster.  
`uid` |  `string` Output only. The unique identifier of the bare metal user cluster.  
`state` |  `enum (`[State](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#State)`)` Output only. The current state of the bare metal user cluster.  
`endpoint` |  `string` Output only. The IP address of the bare metal user cluster's API server.  
`reconciling` |  `boolean` Output only. If set, there are currently changes in flight to the bare metal user cluster.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the bare metal user cluster was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the bare metal user cluster was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the bare metal user cluster was deleted. If the resource is not deleted, this must be emptyUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`localName` |  `string` Output only. The object name of the bare metal user cluster custom resource on the associated admin cluster. This field is used to support conflicting names when enrolling existing clusters to the API. When used as a part of cluster enrollment, this field will differ from the name in the resource name. For new clusters, this field will match the user provided cluster name and be visible in the last component of the resource name. It is not modifiable.When the local name and cluster name differ, the local name is used in the admin cluster controller logs. You use the cluster name when accessing the cluster using bmctl and kubectl.  
`etag` |  `string` Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control.  
`annotations` |  `map (key: string, value: string)` Annotations on the bare metal user cluster. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`networkConfig` |  `object (`[BareMetalNetworkConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalNetworkConfig)`)` Required. Network configuration.  
`controlPlane` |  `object (`[BareMetalControlPlaneConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalControlPlaneConfig)`)` Required. Control plane configuration.  
`loadBalancer` |  `object (`[BareMetalLoadBalancerConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalLoadBalancerConfig)`)` Required. Load balancer configuration.  
`storage` |  `object (`[BareMetalStorageConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalStorageConfig)`)` Required. Storage configuration.  
`proxy` |  `object (`[BareMetalProxyConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalProxyConfig)`)` Proxy configuration.  
`clusterOperations` |  `object (`[BareMetalClusterOperationsConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalClusterOperationsConfig)`)` Cluster operations configuration.  
`maintenanceConfig` |  `object (`[BareMetalMaintenanceConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalMaintenanceConfig)`)` Maintenance configuration.  
`nodeConfig` |  `object (`[BareMetalWorkloadNodeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalWorkloadNodeConfig)`)` Workload node configuration.  
`fleet` |  `object (`[Fleet](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/Fleet)`)` Output only. Fleet configuration for the cluster.  
`status` |  `object (`[ResourceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus)`)` Output only. Detailed cluster status.  
`validationCheck` |  `object (`[ValidationCheck](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ValidationCheck)`)` Output only. The result of the preflight check.  
`securityConfig` |  `object (`[BareMetalSecurityConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalSecurityConfig)`)` Security related setting configuration.  
`maintenanceStatus` |  `object (`[BareMetalMaintenanceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalMaintenanceStatus)`)` Output only. Status of on-going maintenance tasks.  
`adminClusterName` |  `string` Output only. The resource name of the bare metal admin cluster managing this user cluster.  
`nodeAccessConfig` |  `object (`[BareMetalNodeAccessConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalNodeAccessConfig)`)` Node access related configurations.  
`osEnvironmentConfig` |  `object (`[BareMetalOsEnvironmentConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalOsEnvironmentConfig)`)` OS environment related configurations.  
`binaryAuthorization` |  `object (`[BinaryAuthorization](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BinaryAuthorization)`)` Binary Authorization related configurations.  
`upgradePolicy` |  `object (`[BareMetalClusterUpgradePolicy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalClusterUpgradePolicy)`)` The cluster upgrade policy.  
`localNamespace` |  `string` Output only. The namespace of the cluster.  
  
## State

The lifecycle state of the bare metal user cluster.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`PROVISIONING` | The PROVISIONING state indicates the cluster is being created.  
`RUNNING` | The RUNNING state indicates the cluster has been created and is fully usable.  
`RECONCILING` | The RECONCILING state indicates that the cluster is being updated. It remains available, but potentially with degraded performance.  
`STOPPING` | The STOPPING state indicates the cluster is being deleted.  
`ERROR` | The ERROR state indicates the cluster is in a broken unrecoverable state.  
`DEGRADED` | The DEGRADED state indicates the cluster requires user action to restore full functionality.  
  
## BareMetalNetworkConfig

Specifies the cluster network configuration.

JSON representation  
---  
      
    
    {
      "advancedNetworking": boolean,
      "multipleNetworkInterfacesConfig": {
        object ([BareMetalMultipleNetworkInterfacesConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalMultipleNetworkInterfacesConfig))
      },
      "srIovConfig": {
        object ([BareMetalSrIovConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalSrIovConfig))
      },
    
      // Union field cluster_cidr_configuration can be only one of the following:
      "islandModeCidr": {
        object ([BareMetalIslandModeCidrConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalIslandModeCidrConfig))
      }
      // End of list of possible types for union field cluster_cidr_configuration.
    }  
  
Fields  
---  
`advancedNetworking` |  `boolean` Enables the use of advanced Anthos networking features, such as Bundled Load Balancing with BGP or the egress NAT gateway. Setting configuration for advanced networking features will automatically set this flag.  
`multipleNetworkInterfacesConfig` |  `object (`[BareMetalMultipleNetworkInterfacesConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalMultipleNetworkInterfacesConfig)`)` Configuration for multiple network interfaces.  
`srIovConfig` |  `object (`[BareMetalSrIovConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalSrIovConfig)`)` Configuration for SR-IOV.  
Union field `cluster_cidr_configuration`. The CIDR configuration to be used in the bare metal user cluster. `cluster_cidr_configuration` can be only one of the following:  
`islandModeCidr` |  `object (`[BareMetalIslandModeCidrConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalIslandModeCidrConfig)`)` Configuration for island mode CIDR. In an island-mode network, nodes have unique IP addresses, but pods don't have unique addresses across clusters. This doesn't cause problems because pods in one cluster never directly communicate with pods in another cluster. Instead, there are gateways that mediate between a pod in one cluster and a pod in another cluster.  
  
## BareMetalIslandModeCidrConfig

Specifies the cluster CIDR configuration while running in island mode.

JSON representation  
---  
      
    
    {
      "serviceAddressCidrBlocks": [
        string
      ],
      "podAddressCidrBlocks": [
        string
      ]
    }  
  
Fields  
---  
`serviceAddressCidrBlocks[]` |  `string` Required. All services in the cluster are assigned an RFC1918 IPv4 address from these ranges. This field is mutable after creation starting with version 1.15.  
`podAddressCidrBlocks[]` |  `string` Required. All pods in the cluster are assigned an RFC1918 IPv4 address from these ranges. This field cannot be changed after creation.  
  
## BareMetalMultipleNetworkInterfacesConfig

Specifies the multiple networking interfaces cluster configuration.

JSON representation  
---  
      
    
    {
      "enabled": boolean
    }  
  
Fields  
---  
`enabled` |  `boolean` Whether to enable multiple network interfaces for your pods.When set networkConfig.advanced_networking is automatically set to true.  
  
## BareMetalSrIovConfig

Specifies the SR-IOV networking operator config.

JSON representation  
---  
      
    
    {
      "enabled": boolean
    }  
  
Fields  
---  
`enabled` |  `boolean` Whether to install the SR-IOV operator.  
  
## BareMetalControlPlaneConfig

Specifies the control plane configuration.

JSON representation  
---  
      
    
    {
      "controlPlaneNodePoolConfig": {
        object ([BareMetalControlPlaneNodePoolConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalControlPlaneNodePoolConfig))
      },
      "apiServerArgs": [
        {
          object ([BareMetalApiServerArgument](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalApiServerArgument))
        }
      ]
    }  
  
Fields  
---  
`controlPlaneNodePoolConfig` |  `object (`[BareMetalControlPlaneNodePoolConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalControlPlaneNodePoolConfig)`)` Required. Configures the node pool running the control plane.  
`apiServerArgs[]` |  `object (`[BareMetalApiServerArgument](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalApiServerArgument)`)` Customizes the default API server args. Only a subset of customized flags are supported. For the exact format, refer to the [API server documentation](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/).  
  
## BareMetalControlPlaneNodePoolConfig

Specifies the control plane node pool configuration.

JSON representation  
---  
      
    
    {
      "nodePoolConfig": {
        object ([BareMetalNodePoolConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalNodePoolConfig))
      }
    }  
  
Fields  
---  
`nodePoolConfig` |  `object (`[BareMetalNodePoolConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalNodePoolConfig)`)` Required. The generic configuration for a node pool running the control plane.  
  
## BareMetalApiServerArgument

Represents an arg name->value pair. Only a subset of customized flags are supported. For the exact format, refer to the [API server documentation](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/).

JSON representation  
---  
      
    
    {
      "argument": string,
      "value": string
    }  
  
Fields  
---  
`argument` |  `string` Required. The argument name as it appears on the API Server command line, make sure to remove the leading dashes.  
`value` |  `string` Required. The value of the arg as it will be passed to the API Server command line.  
  
## BareMetalLoadBalancerConfig

Specifies the load balancer configuration.

JSON representation  
---  
      
    
    {
      "vipConfig": {
        object ([BareMetalVipConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalVipConfig))
      },
      "portConfig": {
        object ([BareMetalPortConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalPortConfig))
      },
    
      // Union field load_balancer_configuration can be only one of the following:
      "metalLbConfig": {
        object ([BareMetalMetalLbConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalMetalLbConfig))
      },
      "manualLbConfig": {
        object ([BareMetalManualLbConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalManualLbConfig))
      },
      "bgpLbConfig": {
        object ([BareMetalBgpLbConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalBgpLbConfig))
      }
      // End of list of possible types for union field load_balancer_configuration.
    }  
  
Fields  
---  
`vipConfig` |  `object (`[BareMetalVipConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalVipConfig)`)` The VIPs used by the load balancer.  
`portConfig` |  `object (`[BareMetalPortConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalPortConfig)`)` Configures the ports that the load balancer will listen on.  
Union field `load_balancer_configuration`. The load balancer configuration for the bare metal user cluster. `load_balancer_configuration` can be only one of the following:  
`metalLbConfig` |  `object (`[BareMetalMetalLbConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalMetalLbConfig)`)` Configuration for MetalLB load balancers.  
`manualLbConfig` |  `object (`[BareMetalManualLbConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalManualLbConfig)`)` Manually configured load balancers.  
`bgpLbConfig` |  `object (`[BareMetalBgpLbConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalBgpLbConfig)`)` Configuration for BGP typed load balancers.When set networkConfig.advanced_networking is automatically set to true.  
  
## BareMetalVipConfig

Specifies the VIP config for the bare metal load balancer.

JSON representation  
---  
      
    
    {
      "controlPlaneVip": string,
      "ingressVip": string
    }  
  
Fields  
---  
`controlPlaneVip` |  `string` The VIP which you previously set aside for the Kubernetes API of this bare metal user cluster.  
`ingressVip` |  `string` The VIP which you previously set aside for ingress traffic into this bare metal user cluster.  
  
## BareMetalPortConfig

Specifies load balancer ports for the bare metal user cluster.

JSON representation  
---  
      
    
    {
      "controlPlaneLoadBalancerPort": integer
    }  
  
Fields  
---  
`controlPlaneLoadBalancerPort` |  `integer` The port that control plane hosted load balancers will listen on.  
  
## BareMetalMetalLbConfig

Represents configuration parameters for a MetalLB load balancer.

JSON representation  
---  
      
    
    {
      "addressPools": [
        {
          object ([BareMetalLoadBalancerAddressPool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalLoadBalancerAddressPool))
        }
      ],
      "loadBalancerNodePoolConfig": {
        object ([BareMetalLoadBalancerNodePoolConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalLoadBalancerNodePoolConfig))
      }
    }  
  
Fields  
---  
`addressPools[]` |  `object (`[BareMetalLoadBalancerAddressPool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalLoadBalancerAddressPool)`)` Required. AddressPools is a list of non-overlapping IP pools used by load balancer typed services. All addresses must be routable to load balancer nodes. IngressVIP must be included in the pools.  
`loadBalancerNodePoolConfig` |  `object (`[BareMetalLoadBalancerNodePoolConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalLoadBalancerNodePoolConfig)`)` Specifies the node pool running the load balancer. L2 connectivity is required among nodes in this pool. If missing, the control plane node pool is used as the load balancer pool.  
  
## BareMetalLoadBalancerAddressPool

Represents an IP pool used by the load balancer.

JSON representation  
---  
      
    
    {
      "pool": string,
      "addresses": [
        string
      ],
      "avoidBuggyIps": boolean,
      "manualAssign": boolean
    }  
  
Fields  
---  
`pool` |  `string` Required. The name of the address pool.  
`addresses[]` |  `string` Required. The addresses that are part of this pool. Each address must be either in the CIDR form (1.2.3.0/24) or range form (1.2.3.1-1.2.3.5).  
`avoidBuggyIps` |  `boolean` If true, avoid using IPs ending in .0 or .255. This avoids buggy consumer devices mistakenly dropping IPv4 traffic for those special IP addresses.  
`manualAssign` |  `boolean` If true, prevent IP addresses from being automatically assigned.  
  
## BareMetalLoadBalancerNodePoolConfig

Specifies the load balancer's node pool configuration.

JSON representation  
---  
      
    
    {
      "nodePoolConfig": {
        object ([BareMetalNodePoolConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalNodePoolConfig))
      }
    }  
  
Fields  
---  
`nodePoolConfig` |  `object (`[BareMetalNodePoolConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalNodePoolConfig)`)` The generic configuration for a node pool running a load balancer.  
  
## BareMetalManualLbConfig

Represents configuration parameters for a manual load balancer.

JSON representation  
---  
      
    
    {
      "enabled": boolean
    }  
  
Fields  
---  
`enabled` |  `boolean` Whether manual load balancing is enabled.  
  
## BareMetalBgpLbConfig

BareMetalBgpLbConfig represents configuration parameters for a Border Gateway Protocol (BGP) load balancer.

JSON representation  
---  
      
    
    {
      "asn": string,
      "bgpPeerConfigs": [
        {
          object ([BareMetalBgpPeerConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalBgpPeerConfig))
        }
      ],
      "addressPools": [
        {
          object ([BareMetalLoadBalancerAddressPool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalLoadBalancerAddressPool))
        }
      ],
      "loadBalancerNodePoolConfig": {
        object ([BareMetalLoadBalancerNodePoolConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalLoadBalancerNodePoolConfig))
      }
    }  
  
Fields  
---  
`asn` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. BGP autonomous system number (ASN) of the cluster. This field can be updated after cluster creation.  
`bgpPeerConfigs[]` |  `object (`[BareMetalBgpPeerConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalBgpPeerConfig)`)` Required. The list of BGP peers that the cluster will connect to. At least one peer must be configured for each control plane node.Control plane nodes will connect to these peers to advertise the control plane VIP. The Services load balancer also uses these peers by default.This field can be updated after cluster creation.  
`addressPools[]` |  `object (`[BareMetalLoadBalancerAddressPool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalLoadBalancerAddressPool)`)` Required. AddressPools is a list of non-overlapping IP pools used by load balancer typed services. All addresses must be routable to load balancer nodes. IngressVIP must be included in the pools.  
`loadBalancerNodePoolConfig` |  `object (`[BareMetalLoadBalancerNodePoolConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalLoadBalancerNodePoolConfig)`)` Specifies the node pool running data plane load balancing. L2 connectivity is required among nodes in this pool. If missing, the control plane node pool is used for data plane load balancing.  
  
## BareMetalBgpPeerConfig

BareMetalBgpPeerConfig represents configuration parameters for a Border Gateway Protocol (BGP) peer.

JSON representation  
---  
      
    
    {
      "asn": string,
      "ipAddress": string,
      "controlPlaneNodes": [
        string
      ]
    }  
  
Fields  
---  
`asn` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. BGP autonomous system number (ASN) for the network that contains the external peer device.  
`ipAddress` |  `string` Required. The IP address of the external peer device.  
`controlPlaneNodes[]` |  `string` The IP address of the control plane node that connects to the external peer. If you don't specify any control plane nodes, all control plane nodes can connect to the external peer. If you specify one or more IP addresses, only the nodes specified participate in peering sessions.  
  
## BareMetalStorageConfig

BareMetalStorageConfig specifies the cluster storage configuration.

JSON representation  
---  
      
    
    {
      "lvpShareConfig": {
        object ([BareMetalLvpShareConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalLvpShareConfig))
      },
      "lvpNodeMountsConfig": {
        object ([BareMetalLvpConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalLvpConfig))
      }
    }  
  
Fields  
---  
`lvpShareConfig` |  `object (`[BareMetalLvpShareConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalLvpShareConfig)`)` Required. Specifies the config for local PersistentVolumes backed by subdirectories in a shared filesystem. These subdirectores are automatically created during cluster creation.  
`lvpNodeMountsConfig` |  `object (`[BareMetalLvpConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalLvpConfig)`)` Required. Specifies the config for local PersistentVolumes backed by mounted node disks. These disks need to be formatted and mounted by the user, which can be done before or after cluster creation.  
  
## BareMetalProxyConfig

Specifies the cluster proxy configuration.

JSON representation  
---  
      
    
    {
      "uri": string,
      "noProxy": [
        string
      ]
    }  
  
Fields  
---  
`uri` |  `string` Required. Specifies the address of your proxy server. Examples: `http://domain`Do not provide credentials in the format `http://(username:password@)domain` these will be rejected by the server.  
`noProxy[]` |  `string` A list of IPs, hostnames, and domains that should skip the proxy. Examples: ["127.0.0.1", "example.com", ".corp", "localhost"].  
  
## BareMetalClusterOperationsConfig

Specifies the bare metal user cluster's observability infrastructure.

JSON representation  
---  
      
    
    {
      "enableApplicationLogs": boolean
    }  
  
Fields  
---  
`enableApplicationLogs` |  `boolean` Whether collection of application logs/metrics should be enabled (in addition to system logs/metrics).  
  
## BareMetalMaintenanceConfig

Specifies configurations to put bare metal nodes in and out of maintenance.

JSON representation  
---  
      
    
    {
      "maintenanceAddressCidrBlocks": [
        string
      ]
    }  
  
Fields  
---  
`maintenanceAddressCidrBlocks[]` |  `string` Required. All IPv4 address from these ranges will be placed into maintenance mode. Nodes in maintenance mode will be cordoned and drained. When both of these are true, the "baremetal.cluster.gke.io/maintenance" annotation will be set on the node resource.  
  
## BareMetalWorkloadNodeConfig

Specifies the workload node configurations.

JSON representation  
---  
      
    
    {
      "maxPodsPerNode": string,
      "containerRuntime": enum ([ContainerRuntime](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#ContainerRuntime))
    }  
  
Fields  
---  
`maxPodsPerNode` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The maximum number of pods a node can run. The size of the CIDR range assigned to the node will be derived from this parameter.  
`containerRuntime` |  `enum (`[ContainerRuntime](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#ContainerRuntime)`)` Specifies which container runtime will be used.  
  
## ContainerRuntime

The runtime used to run containers in a this user cluster.

Enums  
---  
`CONTAINER_RUNTIME_UNSPECIFIED` | No container runtime selected.  
`CONTAINERD` | Containerd runtime.  
  
## BareMetalSecurityConfig

Specifies the security related settings for the bare metal user cluster.

JSON representation  
---  
      
    
    {
      "authorization": {
        object ([Authorization](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/Authorization))
      }
    }  
  
Fields  
---  
`authorization` |  `object (`[Authorization](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/Authorization)`)` Configures user access to the user cluster.  
  
## BareMetalMaintenanceStatus

Represents the maintenance status of the bare metal user cluster.

JSON representation  
---  
      
    
    {
      "machineDrainStatus": {
        object ([BareMetalMachineDrainStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalMachineDrainStatus))
      }
    }  
  
Fields  
---  
`machineDrainStatus` |  `object (`[BareMetalMachineDrainStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalMachineDrainStatus)`)` The maintenance status of node machines.  
  
## BareMetalMachineDrainStatus

Represents the status of node machines that are undergoing drain operations.

JSON representation  
---  
      
    
    {
      "drainingMachines": [
        {
          object ([BareMetalDrainingMachine](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalDrainingMachine))
        }
      ],
      "drainedMachines": [
        {
          object ([BareMetalDrainedMachine](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalDrainedMachine))
        }
      ]
    }  
  
Fields  
---  
`drainingMachines[]` |  `object (`[BareMetalDrainingMachine](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalDrainingMachine)`)` The list of draning machines.  
`drainedMachines[]` |  `object (`[BareMetalDrainedMachine](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#BareMetalDrainedMachine)`)` The list of drained machines.  
  
## BareMetalDrainingMachine

Represents a machine that is currently draining.

JSON representation  
---  
      
    
    {
      "nodeIp": string,
      "podCount": integer
    }  
  
Fields  
---  
`nodeIp` |  `string` Draining machine IP address.  
`podCount` |  `integer` The count of pods yet to drain.  
  
## BareMetalDrainedMachine

Represents a machine that is currently drained.

JSON representation  
---  
      
    
    {
      "nodeIp": string
    }  
  
Fields  
---  
`nodeIp` |  `string` Drained machine IP address.  
  
## BareMetalNodeAccessConfig

Specifies the node access related settings for the bare metal user cluster.

JSON representation  
---  
      
    
    {
      "loginUser": string
    }  
  
Fields  
---  
`loginUser` |  `string` LoginUser is the user name used to access node machines. It defaults to "root" if not set.  
  
## BareMetalOsEnvironmentConfig

Specifies operating system settings for cluster provisioning.

JSON representation  
---  
      
    
    {
      "packageRepoExcluded": boolean
    }  
  
Fields  
---  
`packageRepoExcluded` |  `boolean` Whether the package repo should not be included when initializing bare metal machines.  
  
## BareMetalClusterUpgradePolicy

BareMetalClusterUpgradePolicy defines the cluster upgrade policy.

JSON representation  
---  
      
    
    {
      "policy": enum ([NodePoolPolicy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#NodePoolPolicy)),
      "pause": boolean
    }  
  
Fields  
---  
`policy` |  `enum (`[NodePoolPolicy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#NodePoolPolicy)`)` Specifies which upgrade policy to use.  
`pause` |  `boolean` Output only. Pause is used to show the upgrade pause status. It's view only for now.  
  
## NodePoolPolicy

Specifies the upgrade policy for worker node pools.

Enums  
---  
`NODE_POOL_POLICY_UNSPECIFIED` | No upgrade policy selected.  
`SERIAL` | Upgrade worker node pools sequentially.  
`CONCURRENT` | Upgrade all worker node pools in parallel.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters/create)`

|  Creates a new bare metal cluster in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters/delete)`

|  Deletes a single bare metal Cluster.  
  
### `[enroll](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters/enroll)`

|  Enrolls an existing bare metal user cluster and its node pools to the Anthos On-Prem API within a given project and location.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters/get)`

|  Gets details of a single bare metal Cluster.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters/list)`

|  Lists bare metal clusters in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters/patch)`

|  Updates the parameters of a single bare metal Cluster.  
  
### `[queryVersionConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters/queryVersionConfig)`

|  Queries the bare metal user cluster version config.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-29 UTC."],[],[]] 
