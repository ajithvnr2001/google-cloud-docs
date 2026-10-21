---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest/v1/projects.locations.vmwareClusters
title: REST Resource: projects.locations.vmwareClusters \u00a0|\u00a0 GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:21.958034+00:00
---

# REST Resource: projects.locations.vmwareClusters  |  GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest/v1/projects.locations.vmwareClusters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  REST Resource: projects.locations.vmwareClusters Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: VmwareCluster
    * JSON representation
  * State
  * VmwareControlPlaneNodeConfig
    * JSON representation
  * VmwareControlPlaneVsphereConfig
    * JSON representation
  * VmwareStorageConfig
    * JSON representation
  * VmwareNetworkConfig
    * JSON representation
  * VmwareControlPlaneV2Config
    * JSON representation
  * VmwareLoadBalancerConfig
    * JSON representation
  * VmwareVipConfig
    * JSON representation
  * VmwareF5BigIpConfig
    * JSON representation
  * VmwareManualLbConfig
    * JSON representation
  * VmwareSeesawConfig
    * JSON representation
  * VmwareMetalLbConfig
    * JSON representation
  * VmwareAddressPool
    * JSON representation
  * VmwareVCenterConfig
    * JSON representation
  * VmwareDataplaneV2Config
    * JSON representation
  * VmwareClusterUpgradePolicy
    * JSON representation
  * Methods



## Resource: VmwareCluster

Resource that represents a VMware user cluster.

##

JSON representation  
---  
      
    
    {
      "name": string,
      "adminClusterMembership": string,
      "description": string,
      "onPremVersion": string,
      "uid": string,
      "state": enum ([State](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#State)),
      "endpoint": string,
      "reconciling": boolean,
      "createTime": string,
      "updateTime": string,
      "localName": string,
      "etag": string,
      "annotations": {
        string: string,
        ...
      },
      "controlPlaneNode": {
        object ([VmwareControlPlaneNodeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareControlPlaneNodeConfig))
      },
      "antiAffinityGroups": {
        object ([VmwareAAGConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareAAGConfig))
      },
      "storage": {
        object ([VmwareStorageConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareStorageConfig))
      },
      "networkConfig": {
        object ([VmwareNetworkConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareNetworkConfig))
      },
      "loadBalancer": {
        object ([VmwareLoadBalancerConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareLoadBalancerConfig))
      },
      "vcenter": {
        object ([VmwareVCenterConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareVCenterConfig))
      },
      "status": {
        object ([ResourceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus))
      },
      "dataplaneV2": {
        object ([VmwareDataplaneV2Config](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareDataplaneV2Config))
      },
      "vmTrackingEnabled": boolean,
      "autoRepairConfig": {
        object ([VmwareAutoRepairConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareAutoRepairConfig))
      },
      "fleet": {
        object ([Fleet](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/Fleet))
      },
      "authorization": {
        object ([Authorization](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/Authorization))
      },
      "deleteTime": string,
      "validationCheck": {
        object ([ValidationCheck](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ValidationCheck))
      },
      "adminClusterName": string,
      "enableControlPlaneV2": boolean,
      "binaryAuthorization": {
        object ([BinaryAuthorization](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BinaryAuthorization))
      },
      "upgradePolicy": {
        object ([VmwareClusterUpgradePolicy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareClusterUpgradePolicy))
      },
      "disableBundledIngress": boolean,
      "enableAdvancedCluster": boolean
    }  
  
Fields  
---  
`name` |  `string` Immutable. The VMware user cluster resource name.  
`adminClusterMembership` |  `string` Required. The admin cluster this VMware user cluster belongs to. This is the full resource name of the admin cluster's fleet membership. In the future, references to other resource types might be allowed if admin clusters are modeled as their own resources.  
`description` |  `string` A human readable description of this VMware user cluster.  
`onPremVersion` |  `string` Required. The Anthos clusters on the VMware version for your user cluster.  
`uid` |  `string` Output only. The unique identifier of the VMware user cluster.  
`state` |  `enum (`[State](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#State)`)` Output only. The current state of VMware user cluster.  
`endpoint` |  `string` Output only. The DNS name of VMware user cluster's API server.  
`reconciling` |  `boolean` Output only. If set, there are currently changes in flight to the VMware user cluster.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which VMware user cluster was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which VMware user cluster was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`localName` |  `string` Output only. The object name of the VMware OnPremUserCluster custom resource on the associated admin cluster. This field is used to support conflicting names when enrolling existing clusters to the API. When used as a part of cluster enrollment, this field will differ from the ID in the resource name. For new clusters, this field will match the user provided cluster name and be visible in the last component of the resource name. It is not modifiable.All users should use this name to access their cluster using gkectl or kubectl and should expect to see the local name when viewing admin cluster controller logs.  
`etag` |  `string` This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control.  
`annotations` |  `map (key: string, value: string)` Annotations on the VMware user cluster. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`controlPlaneNode` |  `object (`[VmwareControlPlaneNodeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareControlPlaneNodeConfig)`)` VMware user cluster control plane nodes must have either 1 or 3 replicas.  
`antiAffinityGroups` |  `object (`[VmwareAAGConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareAAGConfig)`)` AAGConfig specifies whether to spread VMware user cluster nodes across at least three physical hosts in the datacenter.  
`storage` |  `object (`[VmwareStorageConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareStorageConfig)`)` Storage configuration.  
`networkConfig` |  `object (`[VmwareNetworkConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareNetworkConfig)`)` The VMware user cluster network configuration.  
`loadBalancer` |  `object (`[VmwareLoadBalancerConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareLoadBalancerConfig)`)` Load balancer configuration.  
`vcenter` |  `object (`[VmwareVCenterConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareVCenterConfig)`)` VmwareVCenterConfig specifies vCenter config for the user cluster. If unspecified, it is inherited from the admin cluster.  
`status` |  `object (`[ResourceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus)`)` Output only. ResourceStatus representing detailed cluster state.  
`dataplaneV2` |  `object (`[VmwareDataplaneV2Config](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareDataplaneV2Config)`)` VmwareDataplaneV2Config specifies configuration for Dataplane V2.  
`vmTrackingEnabled` |  `boolean` Enable VM tracking.  
`autoRepairConfig` |  `object (`[VmwareAutoRepairConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareAutoRepairConfig)`)` Configuration for auto repairing.  
`fleet` |  `object (`[Fleet](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/Fleet)`)` Output only. Fleet configuration for the cluster.  
`authorization` |  `object (`[Authorization](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/Authorization)`)` RBAC policy that will be applied and managed by the Anthos On-Prem API.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which VMware user cluster was deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`validationCheck` |  `object (`[ValidationCheck](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ValidationCheck)`)` Output only. ValidationCheck represents the result of the preflight check job.  
`adminClusterName` |  `string` Output only. The resource name of the VMware admin cluster hosting this user cluster.  
`enableControlPlaneV2` |  `boolean` Enable control plane V2. Default to false.  
`binaryAuthorization` |  `object (`[BinaryAuthorization](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BinaryAuthorization)`)` Binary Authorization related configurations.  
`upgradePolicy` |  `object (`[VmwareClusterUpgradePolicy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareClusterUpgradePolicy)`)` Specifies upgrade policy for the cluster.  
`disableBundledIngress` |  `boolean` Disable bundled ingress.  
`enableAdvancedCluster` |  `boolean` Enable advanced cluster.  
  
## State

The lifecycle state of the VMware user cluster.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`PROVISIONING` | The PROVISIONING state indicates the cluster is being created.  
`RUNNING` | The RUNNING state indicates the cluster has been created and is fully usable.  
`RECONCILING` | The RECONCILING state indicates that the cluster is being updated. It remains available, but potentially with degraded performance.  
`STOPPING` | The STOPPING state indicates the cluster is being deleted.  
`ERROR` | The ERROR state indicates the cluster is in a broken unrecoverable state.  
`DEGRADED` | The DEGRADED state indicates the cluster requires user action to restore full functionality.  
  
## VmwareControlPlaneNodeConfig

Specifies control plane node config for the VMware user cluster.

JSON representation  
---  
      
    
    {
      "cpus": string,
      "memory": string,
      "replicas": string,
      "autoResizeConfig": {
        object ([VmwareAutoResizeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareAutoResizeConfig))
      },
      "vsphereConfig": {
        object ([VmwareControlPlaneVsphereConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareControlPlaneVsphereConfig))
      }
    }  
  
Fields  
---  
`cpus` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of CPUs for each admin cluster node that serve as control planes for this VMware user cluster. (default: 4 CPUs)  
`memory` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The megabytes of memory for each admin cluster node that serves as a control plane for this VMware user cluster (default: 8192 MB memory).  
`replicas` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of control plane nodes for this VMware user cluster. (default: 1 replica).  
`autoResizeConfig` |  `object (`[VmwareAutoResizeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareAutoResizeConfig)`)` AutoResizeConfig provides auto resizing configurations.  
`vsphereConfig` |  `object (`[VmwareControlPlaneVsphereConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareControlPlaneVsphereConfig)`)` Vsphere-specific config.  
  
## VmwareControlPlaneVsphereConfig

Specifies control plane node config.

JSON representation  
---  
      
    
    {
      "datastore": string,
      "storagePolicyName": string
    }  
  
Fields  
---  
`datastore` |  `string` The Vsphere datastore used by the control plane Node.  
`storagePolicyName` |  `string` The Vsphere storage policy used by the control plane Node.  
  
## VmwareStorageConfig

Specifies vSphere CSI components deployment config in the VMware user cluster.

JSON representation  
---  
      
    
    {
      "vsphereCsiDisabled": boolean
    }  
  
Fields  
---  
`vsphereCsiDisabled` |  `boolean` Whether or not to deploy vSphere CSI components in the VMware user cluster. Enabled by default.  
  
## VmwareNetworkConfig

Specifies network config for the VMware user cluster.

JSON representation  
---  
      
    
    {
      "serviceAddressCidrBlocks": [
        string
      ],
      "podAddressCidrBlocks": [
        string
      ],
      "vcenterNetwork": string,
      "hostConfig": {
        object ([VmwareHostConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareHostConfig))
      },
      "controlPlaneV2Config": {
        object ([VmwareControlPlaneV2Config](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareControlPlaneV2Config))
      },
    
      // Union field ip_configuration can be only one of the following:
      "staticIpConfig": {
        object ([VmwareStaticIpConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareStaticIpConfig))
      },
      "dhcpIpConfig": {
        object ([VmwareDhcpIpConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareDhcpIpConfig))
      }
      // End of list of possible types for union field ip_configuration.
    }  
  
Fields  
---  
`serviceAddressCidrBlocks[]` |  `string` Required. All services in the cluster are assigned an RFC1918 IPv4 address from these ranges. Only a single range is supported. This field cannot be changed after creation.  
`podAddressCidrBlocks[]` |  `string` Required. All pods in the cluster are assigned an RFC1918 IPv4 address from these ranges. Only a single range is supported. This field cannot be changed after creation.  
`vcenterNetwork` |  `string` vcenterNetwork specifies vCenter network name. Inherited from the admin cluster.  
`hostConfig` |  `object (`[VmwareHostConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareHostConfig)`)` Represents common network settings irrespective of the host's IP address.  
`controlPlaneV2Config` |  `object (`[VmwareControlPlaneV2Config](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareControlPlaneV2Config)`)` Configuration for control plane V2 mode.  
Union field `ip_configuration`. The type of IP configuration used by the VMware user cluster. `ip_configuration` can be only one of the following:  
`staticIpConfig` |  `object (`[VmwareStaticIpConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareStaticIpConfig)`)` Configuration settings for a static IP configuration.  
`dhcpIpConfig` |  `object (`[VmwareDhcpIpConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareDhcpIpConfig)`)` Configuration settings for a DHCP IP configuration.  
  
## VmwareControlPlaneV2Config

Specifies control plane V2 config.

JSON representation  
---  
      
    
    {
      "controlPlaneIpBlock": {
        object ([VmwareIpBlock](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareIpBlock))
      }
    }  
  
Fields  
---  
`controlPlaneIpBlock` |  `object (`[VmwareIpBlock](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareIpBlock)`)` Static IP addresses for the control plane nodes.  
  
## VmwareLoadBalancerConfig

Specifies the locad balancer config for the VMware user cluster.

JSON representation  
---  
      
    
    {
      "vipConfig": {
        object ([VmwareVipConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareVipConfig))
      },
    
      // Union field load_balancer_configuration can be only one of the following:
      "f5Config": {
        object ([VmwareF5BigIpConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareF5BigIpConfig))
      },
      "manualLbConfig": {
        object ([VmwareManualLbConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareManualLbConfig))
      },
      "seesawConfig": {
        object ([VmwareSeesawConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareSeesawConfig))
      },
      "metalLbConfig": {
        object ([VmwareMetalLbConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareMetalLbConfig))
      }
      // End of list of possible types for union field load_balancer_configuration.
    }  
  
Fields  
---  
`vipConfig` |  `object (`[VmwareVipConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareVipConfig)`)` The VIPs used by the load balancer.  
Union field `load_balancer_configuration`. The load balancer configuration to be used in the user cluster. `load_balancer_configuration` can be only one of the following:  
`f5Config` |  `object (`[VmwareF5BigIpConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareF5BigIpConfig)`)` Configuration for F5 Big IP typed load balancers.  
`manualLbConfig` |  `object (`[VmwareManualLbConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareManualLbConfig)`)` Manually configured load balancers.  
`seesawConfig` |  `object (`[VmwareSeesawConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareSeesawConfig)`)` Output only. Configuration for Seesaw typed load balancers.  
`metalLbConfig` |  `object (`[VmwareMetalLbConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareMetalLbConfig)`)` Configuration for MetalLB typed load balancers.  
  
## VmwareVipConfig

Specifies the VIP config for the VMware user cluster load balancer.

JSON representation  
---  
      
    
    {
      "controlPlaneVip": string,
      "ingressVip": string
    }  
  
Fields  
---  
`controlPlaneVip` |  `string` The VIP which you previously set aside for the Kubernetes API of this cluster.  
`ingressVip` |  `string` The VIP which you previously set aside for ingress traffic into this cluster.  
  
## VmwareF5BigIpConfig

Represents configuration parameters for an F5 BIG-IP load balancer.

JSON representation  
---  
      
    
    {
      "address": string,
      "partition": string,
      "snatPool": string
    }  
  
Fields  
---  
`address` |  `string` The load balancer's IP address.  
`partition` |  `string` The preexisting partition to be used by the load balancer. This partition is usually created for the admin cluster for example: 'my-f5-admin-partition'.  
`snatPool` |  `string` The pool name. Only necessary, if using SNAT.  
  
## VmwareManualLbConfig

Represents configuration parameters for an already existing manual load balancer. Given the nature of manual load balancers it is expected that said load balancer will be fully managed by users.

IMPORTANT: Please note that the Anthos On-Prem API will not generate or update ManualLB configurations it can only bind a pre-existing configuration to a new VMware user cluster.

JSON representation  
---  
      
    
    {
      "ingressHttpNodePort": integer,
      "ingressHttpsNodePort": integer,
      "controlPlaneNodePort": integer,
      "konnectivityServerNodePort": integer
    }  
  
Fields  
---  
`ingressHttpNodePort` |  `integer` NodePort for ingress service's http. The ingress service in the admin cluster is implemented as a Service of type NodePort (ex. 32527).  
`ingressHttpsNodePort` |  `integer` NodePort for ingress service's https. The ingress service in the admin cluster is implemented as a Service of type NodePort (ex. 30139).  
`controlPlaneNodePort` |  `integer` NodePort for control plane service. The Kubernetes API server in the admin cluster is implemented as a Service of type NodePort (ex. 30968).  
`konnectivityServerNodePort` |  `integer` NodePort for konnectivity server service running as a sidecar in each kube-apiserver pod (ex. 30564).  
  
## VmwareSeesawConfig

VmwareSeesawConfig represents configuration parameters for an already existing Seesaw load balancer.

IMPORTANT: Please note that the Anthos On-Prem API will not generate or update Seesaw configurations it can only bind a pre-existing configuration to a new user cluster.

IMPORTANT: When attempting to create a user cluster with a pre-existing Seesaw load balancer you will need to follow some preparation steps before calling the 'vmwareClusters.create' API method. First you will need to create the user cluster's namespace via kubectl. The namespace will need to use the following naming convention : -gke-onprem-mgmt or -gke-onprem-mgmt depending on whether you used the 'VmwareCluster.local_name' to disambiguate collisions; for more context see the documentation of 'VmwareCluster.local_name'. Once the namespace is created you will need to create a secret resource via kubectl. This secret will contain copies of your Seesaw credentials. The Secret must be called 'user-cluster-creds' and contain Seesaw's SSH and Cert credentials. The credentials must be keyed with the following names: 'seesaw-ssh-private-key', 'seesaw-ssh-public-key', 'seesaw-ssh-ca-key', 'seesaw-ssh-ca-cert'.

JSON representation  
---  
      
    
    {
      "group": string,
      "masterIp": string,
      "ipBlocks": [
        {
          object ([VmwareIpBlock](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareIpBlock))
        }
      ],
      "enableHa": boolean,
      "vms": [
        string
      ],
      "stackdriverName": string
    }  
  
Fields  
---  
`group` |  `string` Required. In general the following format should be used for the Seesaw group name: seesaw-for-[clusterName].  
`masterIp` |  `string` Required. MasterIP is the IP announced by the master of Seesaw group.  
`ipBlocks[]` |  `object (`[VmwareIpBlock](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareIpBlock)`)` Required. The IP Blocks to be used by the Seesaw load balancer  
`enableHa` |  `boolean` Enable two load balancer VMs to achieve a highly-available Seesaw load balancer.  
`vms[]` |  `string` Names of the VMs created for this Seesaw group.  
`stackdriverName` |  `string` Name to be used by Stackdriver.  
  
## VmwareMetalLbConfig

Represents configuration parameters for the MetalLB load balancer.

JSON representation  
---  
      
    
    {
      "addressPools": [
        {
          object ([VmwareAddressPool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareAddressPool))
        }
      ]
    }  
  
Fields  
---  
`addressPools[]` |  `object (`[VmwareAddressPool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters#VmwareAddressPool)`)` Required. AddressPools is a list of non-overlapping IP pools used by load balancer typed services. All addresses must be routable to load balancer nodes. IngressVIP must be included in the pools.  
  
## VmwareAddressPool

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
  
## VmwareVCenterConfig

Represents configuration for the VMware VCenter for the user cluster.

JSON representation  
---  
      
    
    {
      "resourcePool": string,
      "datastore": string,
      "datacenter": string,
      "cluster": string,
      "folder": string,
      "caCertData": string,
      "address": string,
      "storagePolicyName": string
    }  
  
Fields  
---  
`resourcePool` |  `string` The name of the vCenter resource pool for the user cluster.  
`datastore` |  `string` The name of the vCenter datastore for the user cluster.  
`datacenter` |  `string` The name of the vCenter datacenter for the user cluster.  
`cluster` |  `string` The name of the vCenter cluster for the user cluster.  
`folder` |  `string` The name of the vCenter folder for the user cluster.  
`caCertData` |  `string` Contains the vCenter CA certificate public key for SSL verification.  
`address` |  `string` Output only. The vCenter IP address.  
`storagePolicyName` |  `string` The name of the vCenter storage policy for the user cluster.  
  
## VmwareDataplaneV2Config

Contains configurations for Dataplane V2, which is optimized dataplane for Kubernetes networking. For more information, see: <https://cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2>

JSON representation  
---  
      
    
    {
      "dataplaneV2Enabled": boolean,
      "windowsDataplaneV2Enabled": boolean,
      "advancedNetworking": boolean,
      "forwardMode": string
    }  
  
Fields  
---  
`dataplaneV2Enabled` |  `boolean` Enables Dataplane V2.  
`windowsDataplaneV2Enabled` |  `boolean` Enable Dataplane V2 for clusters with Windows nodes.  
`advancedNetworking` |  `boolean` Enable advanced networking which requires dataplaneV2Enabled to be set true.  
`forwardMode` |  `string` Configure ForwardMode for Dataplane v2.  
  
## VmwareClusterUpgradePolicy

VmwareClusterUpgradePolicy defines the cluster upgrade policy.

JSON representation  
---  
      
    
    {
      "controlPlaneOnly": boolean
    }  
  
Fields  
---  
`controlPlaneOnly` |  `boolean` Controls whether the upgrade applies to the control plane only.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters/create)`

|  Creates a new VMware user cluster in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters/delete)`

|  Deletes a single VMware Cluster.  
  
### `[enroll](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters/enroll)`

|  Enrolls an existing VMware user cluster and its node pools to the Anthos On-Prem API within a given project and location.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters/get)`

|  Gets details of a single VMware Cluster.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters/list)`

|  Lists VMware Clusters in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters/patch)`

|  Updates the parameters of a single VMware cluster.  
  
### `[queryVersionConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters/queryVersionConfig)`

|  Queries the VMware user cluster version config.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-29 UTC."],[],[]] 
