---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest/v1/projects.locations.bareMetalAdminClusters
title: REST Resource: projects.locations.bareMetalAdminClusters \u00a0|\u00a0 GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:15.420128+00:00
---

# REST Resource: projects.locations.bareMetalAdminClusters  |  GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest/v1/projects.locations.bareMetalAdminClusters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  REST Resource: projects.locations.bareMetalAdminClusters Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: BareMetalAdminCluster
    * JSON representation
  * State
  * BareMetalAdminNetworkConfig
    * JSON representation
  * BareMetalAdminIslandModeCidrConfig
    * JSON representation
  * BareMetalAdminMultipleNetworkInterfacesConfig
    * JSON representation
  * BareMetalAdminControlPlaneConfig
    * JSON representation
  * BareMetalAdminControlPlaneNodePoolConfig
    * JSON representation
  * BareMetalAdminApiServerArgument
    * JSON representation
  * BareMetalAdminLoadBalancerConfig
    * JSON representation
  * BareMetalAdminVipConfig
    * JSON representation
  * BareMetalAdminPortConfig
    * JSON representation
  * BareMetalAdminManualLbConfig
    * JSON representation
  * BareMetalAdminBgpLbConfig
    * JSON representation
  * BareMetalAdminBgpPeerConfig
    * JSON representation
  * BareMetalAdminLoadBalancerAddressPool
    * JSON representation
  * BareMetalAdminLoadBalancerNodePoolConfig
    * JSON representation
  * BareMetalAdminStorageConfig
    * JSON representation
  * BareMetalAdminClusterOperationsConfig
    * JSON representation
  * BareMetalAdminMaintenanceConfig
    * JSON representation
  * BareMetalAdminMaintenanceStatus
    * JSON representation
  * BareMetalAdminMachineDrainStatus
    * JSON representation
  * BareMetalAdminDrainingMachine
    * JSON representation
  * BareMetalAdminDrainedMachine
    * JSON representation
  * BareMetalAdminWorkloadNodeConfig
    * JSON representation
  * BareMetalAdminProxyConfig
    * JSON representation
  * BareMetalAdminSecurityConfig
    * JSON representation
  * BareMetalAdminNodeAccessConfig
    * JSON representation
  * BareMetalAdminOsEnvironmentConfig
    * JSON representation
  * Methods



## Resource: BareMetalAdminCluster

Resource that represents a bare metal admin cluster.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "uid": string,
      "bareMetalVersion": string,
      "state": enum ([State](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#State)),
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
        object ([BareMetalAdminNetworkConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminNetworkConfig))
      },
      "controlPlane": {
        object ([BareMetalAdminControlPlaneConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminControlPlaneConfig))
      },
      "loadBalancer": {
        object ([BareMetalAdminLoadBalancerConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminLoadBalancerConfig))
      },
      "storage": {
        object ([BareMetalAdminStorageConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminStorageConfig))
      },
      "fleet": {
        object ([Fleet](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/Fleet))
      },
      "clusterOperations": {
        object ([BareMetalAdminClusterOperationsConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminClusterOperationsConfig))
      },
      "status": {
        object ([ResourceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus))
      },
      "maintenanceConfig": {
        object ([BareMetalAdminMaintenanceConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminMaintenanceConfig))
      },
      "maintenanceStatus": {
        object ([BareMetalAdminMaintenanceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminMaintenanceStatus))
      },
      "validationCheck": {
        object ([ValidationCheck](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ValidationCheck))
      },
      "nodeConfig": {
        object ([BareMetalAdminWorkloadNodeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminWorkloadNodeConfig))
      },
      "proxy": {
        object ([BareMetalAdminProxyConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminProxyConfig))
      },
      "securityConfig": {
        object ([BareMetalAdminSecurityConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminSecurityConfig))
      },
      "nodeAccessConfig": {
        object ([BareMetalAdminNodeAccessConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminNodeAccessConfig))
      },
      "osEnvironmentConfig": {
        object ([BareMetalAdminOsEnvironmentConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminOsEnvironmentConfig))
      },
      "binaryAuthorization": {
        object ([BinaryAuthorization](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BinaryAuthorization))
      }
    }  
  
Fields  
---  
`name` |  `string` Immutable. The bare metal admin cluster resource name.  
`description` |  `string` A human readable description of this bare metal admin cluster.  
`uid` |  `string` Output only. The unique identifier of the bare metal admin cluster.  
`bareMetalVersion` |  `string` The Anthos clusters on bare metal version for the bare metal admin cluster.  
`state` |  `enum (`[State](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#State)`)` Output only. The current state of the bare metal admin cluster.  
`endpoint` |  `string` Output only. The IP address name of bare metal admin cluster's API server.  
`reconciling` |  `boolean` Output only. If set, there are currently changes in flight to the bare metal Admin Cluster.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this bare metal admin cluster was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this bare metal admin cluster was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this bare metal admin cluster was deleted. If the resource is not deleted, this must be emptyUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`localName` |  `string` Output only. The object name of the bare metal cluster custom resource. This field is used to support conflicting names when enrolling existing clusters to the API. When used as a part of cluster enrollment, this field will differ from the ID in the resource name. For new clusters, this field will match the user provided cluster name and be visible in the last component of the resource name. It is not modifiable.All users should use this name to access their cluster using gkectl or kubectl and should expect to see the local name when viewing admin cluster controller logs.  
`etag` |  `string` This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control.  
`annotations` |  `map (key: string, value: string)` Annotations on the bare metal admin cluster. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`networkConfig` |  `object (`[BareMetalAdminNetworkConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminNetworkConfig)`)` Network configuration.  
`controlPlane` |  `object (`[BareMetalAdminControlPlaneConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminControlPlaneConfig)`)` Control plane configuration.  
`loadBalancer` |  `object (`[BareMetalAdminLoadBalancerConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminLoadBalancerConfig)`)` Load balancer configuration.  
`storage` |  `object (`[BareMetalAdminStorageConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminStorageConfig)`)` Storage configuration.  
`fleet` |  `object (`[Fleet](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/Fleet)`)` Output only. Fleet configuration for the cluster.  
`clusterOperations` |  `object (`[BareMetalAdminClusterOperationsConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminClusterOperationsConfig)`)` Cluster operations configuration.  
`status` |  `object (`[ResourceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus)`)` Output only. ResourceStatus representing detailed cluster status.  
`maintenanceConfig` |  `object (`[BareMetalAdminMaintenanceConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminMaintenanceConfig)`)` Maintenance configuration.  
`maintenanceStatus` |  `object (`[BareMetalAdminMaintenanceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminMaintenanceStatus)`)` Output only. MaintenanceStatus representing state of maintenance.  
`validationCheck` |  `object (`[ValidationCheck](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ValidationCheck)`)` Output only. ValidationCheck representing the result of the preflight check.  
`nodeConfig` |  `object (`[BareMetalAdminWorkloadNodeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminWorkloadNodeConfig)`)` Workload node configuration.  
`proxy` |  `object (`[BareMetalAdminProxyConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminProxyConfig)`)` Proxy configuration.  
`securityConfig` |  `object (`[BareMetalAdminSecurityConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminSecurityConfig)`)` Security related configuration.  
`nodeAccessConfig` |  `object (`[BareMetalAdminNodeAccessConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminNodeAccessConfig)`)` Node access related configurations.  
`osEnvironmentConfig` |  `object (`[BareMetalAdminOsEnvironmentConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminOsEnvironmentConfig)`)` OS environment related configurations.  
`binaryAuthorization` |  `object (`[BinaryAuthorization](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BinaryAuthorization)`)` Binary Authorization related configurations.  
  
## State

The lifecycle state of the bare metal admin cluster.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`PROVISIONING` | The PROVISIONING state indicates the cluster is being created.  
`RUNNING` | The RUNNING state indicates the cluster has been created and is fully usable.  
`RECONCILING` | The RECONCILING state indicates that the cluster is being updated. It remains available, but potentially with degraded performance.  
`STOPPING` | The STOPPING state indicates the cluster is being deleted.  
`ERROR` | The ERROR state indicates the cluster is in a broken unrecoverable state.  
`DEGRADED` | The DEGRADED state indicates the cluster requires user action to restore full functionality.  
  
## BareMetalAdminNetworkConfig

BareMetalAdminNetworkConfig specifies the cluster network configuration.

JSON representation  
---  
      
    
    {
      "advancedNetworking": boolean,
      "multipleNetworkInterfacesConfig": {
        object ([BareMetalAdminMultipleNetworkInterfacesConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminMultipleNetworkInterfacesConfig))
      },
    
      // Union field cluster_cidr_configuration can be only one of the following:
      "islandModeCidr": {
        object ([BareMetalAdminIslandModeCidrConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminIslandModeCidrConfig))
      }
      // End of list of possible types for union field cluster_cidr_configuration.
    }  
  
Fields  
---  
`advancedNetworking` |  `boolean` Enables the use of advanced Anthos networking features, such as Bundled Load Balancing with BGP or the egress NAT gateway. Setting configuration for advanced networking features will automatically set this flag.  
`multipleNetworkInterfacesConfig` |  `object (`[BareMetalAdminMultipleNetworkInterfacesConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminMultipleNetworkInterfacesConfig)`)` Configuration for multiple network interfaces.  
Union field `cluster_cidr_configuration`. The CIDR configuration to be used in the admin cluster. `cluster_cidr_configuration` can be only one of the following:  
`islandModeCidr` |  `object (`[BareMetalAdminIslandModeCidrConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminIslandModeCidrConfig)`)` Configuration for Island mode CIDR.  
  
## BareMetalAdminIslandModeCidrConfig

BareMetalAdminIslandModeCidrConfig specifies the cluster CIDR configuration while running in island mode.

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
`serviceAddressCidrBlocks[]` |  `string` Required. All services in the cluster are assigned an RFC1918 IPv4 address from these ranges. This field cannot be changed after creation.  
`podAddressCidrBlocks[]` |  `string` Required. All pods in the cluster are assigned an RFC1918 IPv4 address from these ranges. This field cannot be changed after creation.  
  
## BareMetalAdminMultipleNetworkInterfacesConfig

Specifies the multiple networking interfaces cluster configuration.

JSON representation  
---  
      
    
    {
      "enabled": boolean
    }  
  
Fields  
---  
`enabled` |  `boolean` Whether to enable multiple network interfaces for your pods.When set networkConfig.advanced_networking is automatically set to true.  
  
## BareMetalAdminControlPlaneConfig

BareMetalAdminControlPlaneConfig specifies the control plane configuration.

JSON representation  
---  
      
    
    {
      "controlPlaneNodePoolConfig": {
        object ([BareMetalAdminControlPlaneNodePoolConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminControlPlaneNodePoolConfig))
      },
      "apiServerArgs": [
        {
          object ([BareMetalAdminApiServerArgument](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminApiServerArgument))
        }
      ]
    }  
  
Fields  
---  
`controlPlaneNodePoolConfig` |  `object (`[BareMetalAdminControlPlaneNodePoolConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminControlPlaneNodePoolConfig)`)` Required. Configures the node pool running the control plane. If specified the corresponding NodePool will be created for the cluster's control plane. The NodePool will have the same name and namespace as the cluster.  
`apiServerArgs[]` |  `object (`[BareMetalAdminApiServerArgument](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminApiServerArgument)`)` Customizes the default API server args. Only a subset of customized flags are supported. Please refer to the API server documentation below to know the exact format: <https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/>  
  
## BareMetalAdminControlPlaneNodePoolConfig

BareMetalAdminControlPlaneNodePoolConfig specifies the control plane node pool configuration. We have a control plane specific node pool config so that we can flexible about supporting control plane specific fields in the future.

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
  
## BareMetalAdminApiServerArgument

BareMetalAdminApiServerArgument represents an arg name->value pair. Only a subset of customized flags are supported. Please refer to the API server documentation below to know the exact format: <https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/>

JSON representation  
---  
      
    
    {
      "argument": string,
      "value": string
    }  
  
Fields  
---  
`argument` |  `string` Required. The argument name as it appears on the API Server command line please make sure to remove the leading dashes.  
`value` |  `string` Required. The value of the arg as it will be passed to the API Server command line.  
  
## BareMetalAdminLoadBalancerConfig

BareMetalAdminLoadBalancerConfig specifies the load balancer configuration.

JSON representation  
---  
      
    
    {
      "vipConfig": {
        object ([BareMetalAdminVipConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminVipConfig))
      },
      "portConfig": {
        object ([BareMetalAdminPortConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminPortConfig))
      },
    
      // Union field load_balancer_configuration can be only one of the following:
      "manualLbConfig": {
        object ([BareMetalAdminManualLbConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminManualLbConfig))
      },
      "bgpLbConfig": {
        object ([BareMetalAdminBgpLbConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminBgpLbConfig))
      }
      // End of list of possible types for union field load_balancer_configuration.
    }  
  
Fields  
---  
`vipConfig` |  `object (`[BareMetalAdminVipConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminVipConfig)`)` The VIPs used by the load balancer.  
`portConfig` |  `object (`[BareMetalAdminPortConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminPortConfig)`)` Configures the ports that the load balancer will listen on.  
Union field `load_balancer_configuration`. The load balancer configuration to be used in the admin cluster. `load_balancer_configuration` can be only one of the following:  
`manualLbConfig` |  `object (`[BareMetalAdminManualLbConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminManualLbConfig)`)` Manually configured load balancers.  
`bgpLbConfig` |  `object (`[BareMetalAdminBgpLbConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminBgpLbConfig)`)` Configuration for BGP typed load balancers.  
  
## BareMetalAdminVipConfig

BareMetalAdminVipConfig for bare metal load balancer configurations.

JSON representation  
---  
      
    
    {
      "controlPlaneVip": string
    }  
  
Fields  
---  
`controlPlaneVip` |  `string` The VIP which you previously set aside for the Kubernetes API of this bare metal admin cluster.  
  
## BareMetalAdminPortConfig

BareMetalAdminPortConfig is the specification of load balancer ports.

JSON representation  
---  
      
    
    {
      "controlPlaneLoadBalancerPort": integer
    }  
  
Fields  
---  
`controlPlaneLoadBalancerPort` |  `integer` The port that control plane hosted load balancers will listen on.  
  
## BareMetalAdminManualLbConfig

BareMetalAdminManualLbConfig represents configuration parameters for a manual load balancer.

JSON representation  
---  
      
    
    {
      "enabled": boolean
    }  
  
Fields  
---  
`enabled` |  `boolean` Whether manual load balancing is enabled.  
  
## BareMetalAdminBgpLbConfig

BareMetalAdminBgpLbConfig represents configuration parameters for a Border Gateway Protocol (BGP) load balancer.

JSON representation  
---  
      
    
    {
      "asn": string,
      "bgpPeerConfigs": [
        {
          object ([BareMetalAdminBgpPeerConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminBgpPeerConfig))
        }
      ],
      "addressPools": [
        {
          object ([BareMetalAdminLoadBalancerAddressPool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminLoadBalancerAddressPool))
        }
      ],
      "loadBalancerNodePoolConfig": {
        object ([BareMetalAdminLoadBalancerNodePoolConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminLoadBalancerNodePoolConfig))
      }
    }  
  
Fields  
---  
`asn` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. BGP autonomous system number (ASN) of the cluster. This field can be updated after cluster creation.  
`bgpPeerConfigs[]` |  `object (`[BareMetalAdminBgpPeerConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminBgpPeerConfig)`)` Required. The list of BGP peers that the cluster will connect to. At least one peer must be configured for each control plane node.Control plane nodes will connect to these peers to advertise the control plane VIP. The Services load balancer also uses these peers by default.This field can be updated after cluster creation.  
`addressPools[]` |  `object (`[BareMetalAdminLoadBalancerAddressPool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminLoadBalancerAddressPool)`)` Required. AddressPools is a list of non-overlapping IP pools used by load balancer typed services. All addresses must be routable to load balancer nodes. IngressVIP must be included in the pools.  
`loadBalancerNodePoolConfig` |  `object (`[BareMetalAdminLoadBalancerNodePoolConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminLoadBalancerNodePoolConfig)`)` Specifies the node pool running data plane load balancing. L2 connectivity is required among nodes in this pool. If missing, the control plane node pool is used for data plane load balancing.  
  
## BareMetalAdminBgpPeerConfig

BareMetalAdminBgpPeerConfig represents configuration parameters for a Border Gateway Protocol (BGP) peer.

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
  
## BareMetalAdminLoadBalancerAddressPool

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
  
## BareMetalAdminLoadBalancerNodePoolConfig

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
  
## BareMetalAdminStorageConfig

BareMetalAdminStorageConfig specifies the cluster storage configuration.

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
  
## BareMetalAdminClusterOperationsConfig

BareMetalAdminClusterOperationsConfig specifies the admin cluster's observability infrastructure.

JSON representation  
---  
      
    
    {
      "enableApplicationLogs": boolean
    }  
  
Fields  
---  
`enableApplicationLogs` |  `boolean` Whether collection of application logs/metrics should be enabled (in addition to system logs/metrics).  
  
## BareMetalAdminMaintenanceConfig

BareMetalAdminMaintenanceConfig specifies configurations to put bare metal Admin cluster CRs nodes in and out of maintenance.

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
  
## BareMetalAdminMaintenanceStatus

BareMetalAdminMaintenanceStatus represents the maintenance status for bare metal Admin cluster CR's nodes.

JSON representation  
---  
      
    
    {
      "machineDrainStatus": {
        object ([BareMetalAdminMachineDrainStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminMachineDrainStatus))
      }
    }  
  
Fields  
---  
`machineDrainStatus` |  `object (`[BareMetalAdminMachineDrainStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminMachineDrainStatus)`)` Represents the status of draining and drained machine nodes. This is used to show the progress of cluster upgrade.  
  
## BareMetalAdminMachineDrainStatus

BareMetalAdminMachineDrainStatus represents the status of bare metal node machines that are undergoing drain operations.

JSON representation  
---  
      
    
    {
      "drainingMachines": [
        {
          object ([BareMetalAdminDrainingMachine](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminDrainingMachine))
        }
      ],
      "drainedMachines": [
        {
          object ([BareMetalAdminDrainedMachine](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminDrainedMachine))
        }
      ]
    }  
  
Fields  
---  
`drainingMachines[]` |  `object (`[BareMetalAdminDrainingMachine](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminDrainingMachine)`)` The list of draning machines.  
`drainedMachines[]` |  `object (`[BareMetalAdminDrainedMachine](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminDrainedMachine)`)` The list of drained machines.  
  
## BareMetalAdminDrainingMachine

BareMetalAdminDrainingMachine represents the machines that are currently draining.

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
  
## BareMetalAdminDrainedMachine

BareMetalAdminDrainedMachine represents the machines that are drained.

JSON representation  
---  
      
    
    {
      "nodeIp": string
    }  
  
Fields  
---  
`nodeIp` |  `string` Drained machine IP address.  
  
## BareMetalAdminWorkloadNodeConfig

BareMetalAdminWorkloadNodeConfig specifies the workload node configurations.

JSON representation  
---  
      
    
    {
      "maxPodsPerNode": string
    }  
  
Fields  
---  
`maxPodsPerNode` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The maximum number of pods a node can run. The size of the CIDR range assigned to the node will be derived from this parameter. By default 110 Pods are created per Node. Upper bound is 250 for both HA and non-HA admin cluster. Lower bound is 64 for non-HA admin cluster and 32 for HA admin cluster.  
  
## BareMetalAdminProxyConfig

BareMetalAdminProxyConfig specifies the cluster proxy configuration.

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
`uri` |  `string` Required. Specifies the address of your proxy server. Examples: `http://domain`WARNING: Do not provide credentials in the format `http://(username:password@)domain` these will be rejected by the server.  
`noProxy[]` |  `string` A list of IPs, hostnames, and domains that should skip the proxy. Examples: ["127.0.0.1", "example.com", ".corp", "localhost"].  
  
## BareMetalAdminSecurityConfig

Specifies the security related settings for the bare metal admin cluster.

JSON representation  
---  
      
    
    {
      "authorization": {
        object ([Authorization](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/Authorization))
      }
    }  
  
Fields  
---  
`authorization` |  `object (`[Authorization](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/Authorization)`)` Configures user access to the admin cluster.  
  
## BareMetalAdminNodeAccessConfig

Specifies the node access related settings for the bare metal admin cluster.

JSON representation  
---  
      
    
    {
      "loginUser": string
    }  
  
Fields  
---  
`loginUser` |  `string` Required. LoginUser is the user name used to access node machines. It defaults to "root" if not set.  
  
## BareMetalAdminOsEnvironmentConfig

Specifies operating system operation settings for cluster provisioning.

JSON representation  
---  
      
    
    {
      "packageRepoExcluded": boolean
    }  
  
Fields  
---  
`packageRepoExcluded` |  `boolean` Whether the package repo should be added when initializing bare metal machines.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters/create)`

|  Creates a new bare metal admin cluster in a given project and location.  
  
### `[enroll](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters/enroll)`

|  Enrolls an existing bare metal admin cluster to the Anthos On-Prem API within a given project and location.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters/get)`

|  Gets details of a single bare metal admin cluster.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters/list)`

|  Lists bare metal admin clusters in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters/patch)`

|  Updates the parameters of a single bare metal admin cluster.  
  
### `[queryVersionConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters/queryVersionConfig)`

|  Queries the bare metal admin cluster version config.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-29 UTC."],[],[]] 
