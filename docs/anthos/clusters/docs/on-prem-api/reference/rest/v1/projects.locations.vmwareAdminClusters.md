---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest/v1/projects.locations.vmwareAdminClusters
title: REST Resource: projects.locations.vmwareAdminClusters \u00a0|\u00a0 GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:20.768676+00:00
---

# REST Resource: projects.locations.vmwareAdminClusters  |  GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest/v1/projects.locations.vmwareAdminClusters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  REST Resource: projects.locations.vmwareAdminClusters Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: VmwareAdminCluster
    * JSON representation
  * State
  * VmwareAdminVCenterConfig
    * JSON representation
  * VmwareAdminNetworkConfig
    * JSON representation
  * VmwareAdminHAControlPlaneConfig
    * JSON representation
  * VmwareAdminLoadBalancerConfig
    * JSON representation
  * VmwareAdminVipConfig
    * JSON representation
  * VmwareAdminF5BigIpConfig
    * JSON representation
  * VmwareAdminManualLbConfig
    * JSON representation
  * VmwareAdminMetalLbConfig
    * JSON representation
  * VmwareAdminSeesawConfig
    * JSON representation
  * VmwareAdminControlPlaneNodeConfig
    * JSON representation
  * VmwareAdminAddonNodeConfig
    * JSON representation
  * VmwarePlatformConfig
    * JSON representation
  * VmwareBundleConfig
    * JSON representation
  * VmwareAdminPreparedSecretsConfig
    * JSON representation
  * VmwareAdminAuthorizationConfig
    * JSON representation
  * VmwareAdminPrivateRegistryConfig
    * JSON representation
  * VmwareAdminProxy
    * JSON representation
  * Methods



## Resource: VmwareAdminCluster

Resource that represents a VMware admin cluster.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "uid": string,
      "etag": string,
      "createTime": string,
      "updateTime": string,
      "annotations": {
        string: string,
        ...
      },
      "state": enum ([State](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#State)),
      "endpoint": string,
      "reconciling": boolean,
      "localName": string,
      "bootstrapClusterMembership": string,
      "onPremVersion": string,
      "fleet": {
        object ([Fleet](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/Fleet))
      },
      "imageType": string,
      "vcenter": {
        object ([VmwareAdminVCenterConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminVCenterConfig))
      },
      "networkConfig": {
        object ([VmwareAdminNetworkConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminNetworkConfig))
      },
      "loadBalancer": {
        object ([VmwareAdminLoadBalancerConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminLoadBalancerConfig))
      },
      "controlPlaneNode": {
        object ([VmwareAdminControlPlaneNodeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminControlPlaneNodeConfig))
      },
      "addonNode": {
        object ([VmwareAdminAddonNodeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminAddonNodeConfig))
      },
      "antiAffinityGroups": {
        object ([VmwareAAGConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareAAGConfig))
      },
      "autoRepairConfig": {
        object ([VmwareAutoRepairConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareAutoRepairConfig))
      },
      "status": {
        object ([ResourceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus))
      },
      "platformConfig": {
        object ([VmwarePlatformConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwarePlatformConfig))
      },
      "preparedSecrets": {
        object ([VmwareAdminPreparedSecretsConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminPreparedSecretsConfig))
      },
      "authorization": {
        object ([VmwareAdminAuthorizationConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminAuthorizationConfig))
      },
      "validationCheck": {
        object ([ValidationCheck](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ValidationCheck))
      },
      "privateRegistryConfig": {
        object ([VmwareAdminPrivateRegistryConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminPrivateRegistryConfig))
      },
      "proxy": {
        object ([VmwareAdminProxy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminProxy))
      },
      "enableAdvancedCluster": boolean
    }  
  
Fields  
---  
`name` |  `string` Immutable. The VMware admin cluster resource name.  
`description` |  `string` A human readable description of this VMware admin cluster.  
`uid` |  `string` Output only. The unique identifier of the VMware admin cluster.  
`etag` |  `string` This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which VMware admin cluster was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which VMware admin cluster was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`annotations` |  `map (key: string, value: string)` Annotations on the VMware admin cluster. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#State)`)` Output only. The current state of VMware admin cluster.  
`endpoint` |  `string` Output only. The DNS name of VMware admin cluster's API server.  
`reconciling` |  `boolean` Output only. If set, there are currently changes in flight to the VMware admin cluster.  
`localName` |  `string` Output only. The object name of the VMware OnPremAdminCluster custom resource. This field is used to support conflicting names when enrolling existing clusters to the API. When used as a part of cluster enrollment, this field will differ from the ID in the resource name. For new clusters, this field will match the user provided cluster name and be visible in the last component of the resource name. It is not modifiable.All users should use this name to access their cluster using gkectl or kubectl and should expect to see the local name when viewing admin cluster controller logs.  
`bootstrapClusterMembership` |  `string` The bootstrap cluster this VMware admin cluster belongs to.  
`onPremVersion` |  `string` The Anthos clusters on the VMware version for the admin cluster.  
`fleet` |  `object (`[Fleet](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/Fleet)`)` Output only. Fleet configuration for the cluster.  
`imageType` |  `string` The OS image type for the VMware admin cluster.  
`vcenter` |  `object (`[VmwareAdminVCenterConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminVCenterConfig)`)` The VMware admin cluster VCenter configuration.  
`networkConfig` |  `object (`[VmwareAdminNetworkConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminNetworkConfig)`)` The VMware admin cluster network configuration.  
`loadBalancer` |  `object (`[VmwareAdminLoadBalancerConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminLoadBalancerConfig)`)` The VMware admin cluster load balancer configuration.  
`controlPlaneNode` |  `object (`[VmwareAdminControlPlaneNodeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminControlPlaneNodeConfig)`)` The VMware admin cluster control plane node configuration.  
`addonNode` |  `object (`[VmwareAdminAddonNodeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminAddonNodeConfig)`)` The VMware admin cluster addon node configuration.  
`antiAffinityGroups` |  `object (`[VmwareAAGConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareAAGConfig)`)` The VMware admin cluster anti affinity group configuration.  
`autoRepairConfig` |  `object (`[VmwareAutoRepairConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareAutoRepairConfig)`)` The VMware admin cluster auto repair configuration.  
`status` |  `object (`[ResourceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus)`)` Output only. ResourceStatus representing detailed cluster state.  
`platformConfig` |  `object (`[VmwarePlatformConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwarePlatformConfig)`)` The VMware platform configuration.  
`preparedSecrets` |  `object (`[VmwareAdminPreparedSecretsConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminPreparedSecretsConfig)`)` Output only. The VMware admin cluster prepared secrets configuration. It should always be enabled by the Central API, instead of letting users set it.  
`authorization` |  `object (`[VmwareAdminAuthorizationConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminAuthorizationConfig)`)` The VMware admin cluster authorization configuration.  
`validationCheck` |  `object (`[ValidationCheck](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ValidationCheck)`)` Output only. ValidationCheck represents the result of the preflight check job.  
`privateRegistryConfig` |  `object (`[VmwareAdminPrivateRegistryConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminPrivateRegistryConfig)`)` Configuration for registry.  
`proxy` |  `object (`[VmwareAdminProxy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminProxy)`)` Configuration for proxy.  
`enableAdvancedCluster` |  `boolean` Enable advanced cluster.  
  
## State

The lifecycle state of the VMware admin cluster.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`PROVISIONING` | The PROVISIONING state indicates the cluster is being created.  
`RUNNING` | The RUNNING state indicates the cluster has been created and is fully usable.  
`RECONCILING` | The RECONCILING state indicates that the cluster is being updated. It remains available, but potentially with degraded performance.  
`STOPPING` | The STOPPING state indicates the cluster is being deleted.  
`ERROR` | The ERROR state indicates the cluster is in a broken unrecoverable state.  
`DEGRADED` | The DEGRADED state indicates the cluster requires user action to restore full functionality.  
  
## VmwareAdminVCenterConfig

VmwareAdminVCenterConfig contains VCenter configuration for VMware admin cluster.

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
      "dataDisk": string,
      "storagePolicyName": string
    }  
  
Fields  
---  
`resourcePool` |  `string` The name of the vCenter resource pool for the admin cluster.  
`datastore` |  `string` The name of the vCenter datastore for the admin cluster.  
`datacenter` |  `string` The name of the vCenter datacenter for the admin cluster.  
`cluster` |  `string` The name of the vCenter cluster for the admin cluster.  
`folder` |  `string` The name of the vCenter folder for the admin cluster.  
`caCertData` |  `string` Contains the vCenter CA certificate public key for SSL verification.  
`address` |  `string` The vCenter IP address.  
`dataDisk` |  `string` The name of the virtual machine disk (VMDK) for the admin cluster.  
`storagePolicyName` |  `string` The name of the vCenter storage policy for the user cluster.  
  
## VmwareAdminNetworkConfig

VmwareAdminNetworkConfig contains network configuration for VMware admin cluster.

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
      "haControlPlaneConfig": {
        object ([VmwareAdminHAControlPlaneConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminHAControlPlaneConfig))
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
`vcenterNetwork` |  `string` vcenterNetwork specifies vCenter network name.  
`hostConfig` |  `object (`[VmwareHostConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareHostConfig)`)` Represents common network settings irrespective of the host's IP address.  
`haControlPlaneConfig` |  `object (`[VmwareAdminHAControlPlaneConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminHAControlPlaneConfig)`)` Configuration for HA admin cluster control plane.  
Union field `ip_configuration`. The type of IP configuration used by the VMware admin cluster. `ip_configuration` can be only one of the following:  
`staticIpConfig` |  `object (`[VmwareStaticIpConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareStaticIpConfig)`)` Configuration settings for a static IP configuration.  
`dhcpIpConfig` |  `object (`[VmwareDhcpIpConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareDhcpIpConfig)`)` Configuration settings for a DHCP IP configuration.  
  
## VmwareAdminHAControlPlaneConfig

Specifies HA admin control plane config.

JSON representation  
---  
      
    
    {
      "controlPlaneIpBlock": {
        object ([VmwareIpBlock](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareIpBlock))
      }
    }  
  
Fields  
---  
`controlPlaneIpBlock` |  `object (`[VmwareIpBlock](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareIpBlock)`)` Static IP addresses for the admin control plane nodes.  
  
## VmwareAdminLoadBalancerConfig

VmwareAdminLoadBalancerConfig contains load balancer configuration for VMware admin cluster.

JSON representation  
---  
      
    
    {
      "vipConfig": {
        object ([VmwareAdminVipConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminVipConfig))
      },
    
      // Union field load_balancer_configuration can be only one of the following:
      "f5Config": {
        object ([VmwareAdminF5BigIpConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminF5BigIpConfig))
      },
      "manualLbConfig": {
        object ([VmwareAdminManualLbConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminManualLbConfig))
      },
      "metalLbConfig": {
        object ([VmwareAdminMetalLbConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminMetalLbConfig))
      },
      "seesawConfig": {
        object ([VmwareAdminSeesawConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminSeesawConfig))
      }
      // End of list of possible types for union field load_balancer_configuration.
    }  
  
Fields  
---  
`vipConfig` |  `object (`[VmwareAdminVipConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminVipConfig)`)` The VIPs used by the load balancer.  
Union field `load_balancer_configuration`. The load balancer configuration to be user in the VMware admin cluster. `load_balancer_configuration` can be only one of the following:  
`f5Config` |  `object (`[VmwareAdminF5BigIpConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminF5BigIpConfig)`)` Configuration for F5 Big IP typed load balancers.  
`manualLbConfig` |  `object (`[VmwareAdminManualLbConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminManualLbConfig)`)` Manually configured load balancers.  
`metalLbConfig` |  `object (`[VmwareAdminMetalLbConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminMetalLbConfig)`)` MetalLB load balancers.  
`seesawConfig` |  `object (`[VmwareAdminSeesawConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareAdminSeesawConfig)`)` Output only. Configuration for Seesaw typed load balancers.  
  
## VmwareAdminVipConfig

VmwareAdminVipConfig for VMware load balancer configurations.

JSON representation  
---  
      
    
    {
      "controlPlaneVip": string,
      "addonsVip": string
    }  
  
Fields  
---  
`controlPlaneVip` |  `string` The VIP which you previously set aside for the Kubernetes API of the admin cluster.  
`addonsVip` |  `string` The VIP to configure the load balancer for add-ons.  
  
## VmwareAdminF5BigIpConfig

VmwareAdminF5BigIpConfig represents configuration parameters for an F5 BIG-IP load balancer.

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
  
## VmwareAdminManualLbConfig

JSON representation  
---  
      
    
    {
      "ingressHttpNodePort": integer,
      "ingressHttpsNodePort": integer,
      "controlPlaneNodePort": integer,
      "konnectivityServerNodePort": integer,
      "addonsNodePort": integer
    }  
  
Fields  
---  
`ingressHttpNodePort` |  `integer` NodePort for ingress service's http. The ingress service in the admin cluster is implemented as a Service of type NodePort (ex. 32527).  
`ingressHttpsNodePort` |  `integer` NodePort for ingress service's https. The ingress service in the admin cluster is implemented as a Service of type NodePort (ex. 30139).  
`controlPlaneNodePort` |  `integer` NodePort for control plane service. The Kubernetes API server in the admin cluster is implemented as a Service of type NodePort (ex. 30968).  
`konnectivityServerNodePort` |  `integer` NodePort for konnectivity server service running as a sidecar in each kube-apiserver pod (ex. 30564).  
`addonsNodePort` |  `integer` NodePort for add-ons server in the admin cluster.  
  
## VmwareAdminMetalLbConfig

VmwareAdminMetalLbConfig represents configuration parameters for a MetalLB load balancer. For admin clusters, currently no configurations is needed.

JSON representation  
---  
      
    
    {
      "enabled": boolean
    }  
  
Fields  
---  
`enabled` |  `boolean` Whether MetalLB is enabled.  
  
## VmwareAdminSeesawConfig

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
`group` |  `string` In general the following format should be used for the Seesaw group name: seesaw-for-[clusterName].  
`masterIp` |  `string` MasterIP is the IP announced by the master of Seesaw group.  
`ipBlocks[]` |  `object (`[VmwareIpBlock](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareIpBlock)`)` The IP Blocks to be used by the Seesaw load balancer  
`enableHa` |  `boolean` Enable two load balancer VMs to achieve a highly-available Seesaw load balancer.  
`vms[]` |  `string` Names of the VMs created for this Seesaw group.  
`stackdriverName` |  `string` Name to be used by Stackdriver.  
  
## VmwareAdminControlPlaneNodeConfig

VmwareAdminControlPlaneNodeConfig contains control plane node configuration for VMware admin cluster.

JSON representation  
---  
      
    
    {
      "cpus": string,
      "memory": string,
      "replicas": string
    }  
  
Fields  
---  
`cpus` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of vCPUs for the control-plane node of the admin cluster.  
`memory` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of mebibytes of memory for the control-plane node of the admin cluster.  
`replicas` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of control plane nodes for this VMware admin cluster. (default: 1 replica).  
  
## VmwareAdminAddonNodeConfig

VmwareAdminAddonNodeConfig contains add-on node configurations for VMware admin cluster.

JSON representation  
---  
      
    
    {
      "autoResizeConfig": {
        object ([VmwareAutoResizeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareAutoResizeConfig))
      }
    }  
  
Fields  
---  
`autoResizeConfig` |  `object (`[VmwareAutoResizeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareAutoResizeConfig)`)` VmwareAutoResizeConfig config specifies auto resize config.  
  
## VmwarePlatformConfig

VmwarePlatformConfig represents configuration for the VMware platform.

JSON representation  
---  
      
    
    {
      "requiredPlatformVersion": string,
      "platformVersion": string,
      "bundles": [
        {
          object ([VmwareBundleConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareBundleConfig))
        }
      ],
      "status": {
        object ([ResourceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus))
      }
    }  
  
Fields  
---  
`requiredPlatformVersion` |  `string` Input only. The required platform version e.g. 1.13.1. If the current platform version is lower than the target version, the platform version will be updated to the target version. If the target version is not installed in the platform (bundle versions), download the target version bundle.  
`platformVersion` |  `string` Output only. The platform version e.g. 1.13.2.  
`bundles[]` |  `object (`[VmwareBundleConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters#VmwareBundleConfig)`)` Output only. The list of bundles installed in the admin cluster.  
`status` |  `object (`[ResourceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus)`)` Output only. Resource status for the platform.  
  
## VmwareBundleConfig

VmwareBundleConfig represents configuration for the bundle.

JSON representation  
---  
      
    
    {
      "version": string,
      "status": {
        object ([ResourceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus))
      }
    }  
  
Fields  
---  
`version` |  `string` The version of the bundle.  
`status` |  `object (`[ResourceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus)`)` Output only. Resource status for the bundle.  
  
## VmwareAdminPreparedSecretsConfig

VmwareAdminPreparedSecretsConfig represents configuration for admin cluster prepared secrets.

JSON representation  
---  
      
    
    {
      "enabled": boolean
    }  
  
Fields  
---  
`enabled` |  `boolean` Whether prepared secrets is enabled.  
  
## VmwareAdminAuthorizationConfig

VmwareAdminAuthorizationConfig represents configuration for admin cluster authorization.

JSON representation  
---  
      
    
    {
      "viewerUsers": [
        {
          object ([ClusterUser](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ClusterUser))
        }
      ]
    }  
  
Fields  
---  
`viewerUsers[]` |  `object (`[ClusterUser](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ClusterUser)`)` For VMware admin clusters, users will be granted the cluster-viewer role on the cluster.  
  
## VmwareAdminPrivateRegistryConfig

VmwareAdminPrivateRegistryConfig represents configuration for admin cluster registry.

JSON representation  
---  
      
    
    {
      "address": string,
      "caCert": string
    }  
  
Fields  
---  
`address` |  `string` The registry address.  
`caCert` |  `string` When the container runtime pulls an image from private registry, the registry must prove its identity by presenting a certificate. The registry's certificate is signed by a certificate authority (CA). The container runtime uses the CA's certificate to validate the registry's certificate.  
  
## VmwareAdminProxy

VmwareAdminProxy represents configuration for admin cluster proxy.

JSON representation  
---  
      
    
    {
      "url": string,
      "noProxy": string
    }  
  
Fields  
---  
`url` |  `string` The HTTP address of proxy server.  
`noProxy` |  `string` A comma-separated list of IP addresses, IP address ranges, host names, and domain names that should not go through the proxy server. When Google Distributed Cloud sends a request to one of these addresses, hosts, or domains, the request is sent directly.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters/create)`

|  Creates a new VMware admin cluster in a given project and location.  
  
### `[enroll](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters/enroll)`

|  Enrolls an existing VMware admin cluster to the Anthos On-Prem API within a given project and location.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters/get)`

|  Gets details of a single VMware admin cluster.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters/list)`

|  Lists VMware admin clusters in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters/patch)`

|  Updates the parameters of a single VMware admin cluster.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-29 UTC."],[],[]] 
