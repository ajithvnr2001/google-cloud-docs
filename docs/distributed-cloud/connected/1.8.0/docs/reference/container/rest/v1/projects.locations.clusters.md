---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters
title: REST Resource: projects.locations.clusters \u00a0|\u00a0 Google Distributed Cloud connected, version 1.8.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:06:25.656920+00:00
---

# REST Resource: projects.locations.clusters  |  Google Distributed Cloud connected, version 1.8.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/apis)



Send feedback 

#  REST Resource: projects.locations.clusters Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Cluster
    * JSON representation
  * Fleet
    * JSON representation
  * ClusterNetworking
    * JSON representation
  * Authorization
    * JSON representation
  * ClusterUser
    * JSON representation
  * MaintenancePolicy
    * JSON representation
  * MaintenanceWindow
    * JSON representation
  * RecurringTimeWindow
    * JSON representation
  * TimeWindow
    * JSON representation
  * MaintenanceExclusionWindow
    * JSON representation
  * ControlPlane
    * JSON representation
  * Remote
  * Local
    * JSON representation
  * SharedDeploymentPolicy
  * SystemAddonsConfig
    * JSON representation
  * Ingress
    * JSON representation
  * VMServiceConfig
    * JSON representation
  * ControlPlaneEncryption
    * JSON representation
  * Status
  * MaintenanceEvent
    * JSON representation
  * Type
  * Schedule
  * State
  * ReleaseChannel
  * SurvivabilityConfig
    * JSON representation
  * ConnectionState
    * JSON representation
  * State
  * ExternalLoadBalancerPool
    * JSON representation
  * ZoneStorageEncryption
    * JSON representation
  * Methods



## Resource: Cluster

A Google Distributed Cloud Edge Kubernetes cluster.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "fleet": {
        object ([Fleet](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#Fleet))
      },
      "networking": {
        object ([ClusterNetworking](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#ClusterNetworking))
      },
      "authorization": {
        object ([Authorization](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#Authorization))
      },
      "defaultMaxPodsPerNode": integer,
      "endpoint": string,
      "port": integer,
      "clusterCaCertificate": string,
      "maintenancePolicy": {
        object ([MaintenancePolicy](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#MaintenancePolicy))
      },
      "controlPlaneVersion": string,
      "nodeVersion": string,
      "controlPlane": {
        object ([ControlPlane](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#ControlPlane))
      },
      "systemAddonsConfig": {
        object ([SystemAddonsConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#SystemAddonsConfig))
      },
      "externalLoadBalancerIpv4AddressPools": [
        string
      ],
      "controlPlaneEncryption": {
        object ([ControlPlaneEncryption](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#ControlPlaneEncryption))
      },
      "status": enum ([Status](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#Status)),
      "maintenanceEvents": [
        {
          object ([MaintenanceEvent](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#MaintenanceEvent))
        }
      ],
      "targetVersion": string,
      "releaseChannel": enum ([ReleaseChannel](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#ReleaseChannel)),
      "survivabilityConfig": {
        object ([SurvivabilityConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#SurvivabilityConfig))
      },
      "externalLoadBalancerIpv6AddressPools": [
        string
      ],
      "connectionState": {
        object ([ConnectionState](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#ConnectionState))
      },
      "externalLoadBalancerAddressPools": [
        {
          object ([ExternalLoadBalancerPool](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#ExternalLoadBalancerPool))
        }
      ],
      "zoneStorageEncryption": {
        object ([ZoneStorageEncryption](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#ZoneStorageEncryption))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the cluster.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the cluster was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the cluster was last updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Labels associated with this resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`fleet` |  `object (`[Fleet](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#Fleet)`)` Required. Fleet configuration.  
`networking` |  `object (`[ClusterNetworking](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#ClusterNetworking)`)` Required. Cluster-wide networking configuration.  
`authorization` |  `object (`[Authorization](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#Authorization)`)` Required. Immutable. RBAC policy that will be applied and managed by GEC.  
`defaultMaxPodsPerNode` |  `integer` Optional. The default maximum number of pods per node used if a maximum value is not specified explicitly for a node pool in this cluster. If unspecified, the Kubernetes default value will be used.  
`endpoint` |  `string` Output only. The IP address of the Kubernetes API server.  
`port` |  `integer` Output only. The port number of the Kubernetes API server.  
`clusterCaCertificate` |  `string` Output only. The PEM-encoded public certificate of the cluster's CA.  
`maintenancePolicy` |  `object (`[MaintenancePolicy](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#MaintenancePolicy)`)` Optional. Cluster-wide maintenance policy configuration.  
`controlPlaneVersion` |  `string` Output only. The control plane release version  
`nodeVersion` |  `string` Output only. The lowest release version among all worker nodes. This field can be empty if the cluster does not have any worker nodes.  
`controlPlane` |  `object (`[ControlPlane](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#ControlPlane)`)` Optional. The configuration of the cluster control plane.  
`systemAddonsConfig` |  `object (`[SystemAddonsConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#SystemAddonsConfig)`)` Optional. The configuration of the system add-ons.  
`externalLoadBalancerIpv4AddressPools[]` |  `string` Optional. IPv4 address pools for cluster data plane external load balancing.  
`controlPlaneEncryption` |  `object (`[ControlPlaneEncryption](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#ControlPlaneEncryption)`)` Optional. Remote control plane disk encryption options. This field is only used when enabling CMEK support.  
`status` |  `enum (`[Status](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#Status)`)` Output only. The current status of the cluster.  
`maintenanceEvents[]` |  `object (`[MaintenanceEvent](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#MaintenanceEvent)`)` Output only. All the maintenance events scheduled for the cluster, including the ones ongoing, planned for the future and done in the past (up to 90 days).  
`targetVersion` |  `string` Optional. The target cluster version. For example: "1.5.0".  
`releaseChannel` |  `enum (`[ReleaseChannel](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#ReleaseChannel)`)` Optional. The release channel a cluster is subscribed to.  
`survivabilityConfig` |  `object (`[SurvivabilityConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#SurvivabilityConfig)`)` Optional. Configuration of the cluster survivability, e.g., for the case when network connectivity is lost. Note: This only applies to local control plane clusters.  
`externalLoadBalancerIpv6AddressPools[]` |  `string` Optional. IPv6 address pools for cluster data plane external load balancing.  
`connectionState` |  `object (`[ConnectionState](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#ConnectionState)`)` Output only. The current connection state of the cluster.  
`externalLoadBalancerAddressPools[]` |  `object (`[ExternalLoadBalancerPool](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#ExternalLoadBalancerPool)`)` Optional. External load balancer pools for cluster.  
`zoneStorageEncryption` |  `object (`[ZoneStorageEncryption](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#ZoneStorageEncryption)`)` Optional. The zone storage encryption configuration  
  
## Fleet

Fleet related configuration.

Fleets are a Google Cloud concept for logically organizing clusters, letting you use and manage multi-cluster capabilities and apply consistent policies across your systems.

JSON representation  
---  
      
    
    {
      "project": string,
      "membership": string
    }  
  
Fields  
---  
`project` |  `string` Required. The name of the Fleet host project where this cluster will be registered.Project names are formatted as `projects/<project-number>`.  
`membership` |  `string` Output only. The name of the managed Hub Membership resource associated to this cluster.Membership names are formatted as `projects/<project-number>/locations/global/membership/<cluster-id>`.  
  
## ClusterNetworking

Cluster-wide networking configuration.

JSON representation  
---  
      
    
    {
      "clusterIpv4CidrBlocks": [
        string
      ],
      "servicesIpv4CidrBlocks": [
        string
      ]
    }  
  
Fields  
---  
`clusterIpv4CidrBlocks[]` |  `string` Required. All pods in the cluster are assigned an RFC1918 IPv4 address from these blocks. Only a single block is supported. This field cannot be changed after creation.  
`servicesIpv4CidrBlocks[]` |  `string` Required. All services in the cluster are assigned an RFC1918 IPv4 address from these blocks. Only a single block is supported. This field cannot be changed after creation.  
  
## Authorization

RBAC policy that will be applied and managed by GEC.

JSON representation  
---  
      
    
    {
      "adminUsers": {
        object ([ClusterUser](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#ClusterUser))
      }
    }  
  
Fields  
---  
`adminUsers` |  `object (`[ClusterUser](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#ClusterUser)`)` Required. User that will be granted the cluster-admin role on the cluster, providing full access to the cluster. Currently, this is a singular field, but will be expanded to allow multiple admins in the future.  
  
## ClusterUser

A user principal for an RBAC policy.

JSON representation  
---  
      
    
    {
      "username": string
    }  
  
Fields  
---  
`username` |  `string` Required. An active Google username.  
  
## MaintenancePolicy

Maintenance policy configuration.

JSON representation  
---  
      
    
    {
      "window": {
        object ([MaintenanceWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#MaintenanceWindow))
      },
      "maintenanceExclusions": [
        {
          object ([MaintenanceExclusionWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#MaintenanceExclusionWindow))
        }
      ]
    }  
  
Fields  
---  
`window` |  `object (`[MaintenanceWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#MaintenanceWindow)`)` Specifies the maintenance window in which maintenance may be performed.  
`maintenanceExclusions[]` |  `object (`[MaintenanceExclusionWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#MaintenanceExclusionWindow)`)` Optional. Exclusions to automatic maintenance. Non-emergency maintenance should not occur in these windows. Each exclusion has a unique name and may be active or expired. The max number of maintenance exclusions allowed at a given time is 3.  
  
## MaintenanceWindow

Maintenance window configuration

JSON representation  
---  
      
    
    {
      "recurringWindow": {
        object ([RecurringTimeWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#RecurringTimeWindow))
      }
    }  
  
Fields  
---  
`recurringWindow` |  `object (`[RecurringTimeWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#RecurringTimeWindow)`)` Configuration of a recurring maintenance window.  
  
## RecurringTimeWindow

Represents an arbitrary window of time that recurs.

JSON representation  
---  
      
    
    {
      "window": {
        object ([TimeWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#TimeWindow))
      },
      "recurrence": string
    }  
  
Fields  
---  
`window` |  `object (`[TimeWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#TimeWindow)`)` The window of the first recurrence.  
`recurrence` |  `string` An RRULE (<https://tools.ietf.org/html/rfc5545#section-3.8.5.3>) for how this window recurs. They go on for the span of time between the start and end time.  
  
## TimeWindow

Represents an arbitrary window of time.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time that the window first starts.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time that the window ends. The end time must take place after the start time.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## MaintenanceExclusionWindow

Represents a maintenance exclusion window.

JSON representation  
---  
      
    
    {
      "window": {
        object ([TimeWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#TimeWindow))
      },
      "id": string
    }  
  
Fields  
---  
`window` |  `object (`[TimeWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#TimeWindow)`)` Optional. The time window.  
`id` |  `string` Optional. A unique (per cluster) id for the window.  
  
## ControlPlane

Configuration of the cluster control plane.

JSON representation  
---  
      
    
    {
    
      // Union field config can be only one of the following:
      "remote": {
        object ([Remote](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#Remote))
      },
      "local": {
        object ([Local](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#Local))
      }
      // End of list of possible types for union field config.
    }  
  
Fields  
---  
Union field `config`.`config` can be only one of the following:  
`remote` |  `object (`[Remote](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#Remote)`)` Remote control plane configuration.  
`local` |  `object (`[Local](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#Local)`)` Local control plane configuration.Warning: Local control plane clusters must be created in their own project. Local control plane clusters cannot coexist in the same project with any other type of clusters, including non-GDCE clusters. Mixing local control plane GDCE clusters with any other type of clusters in the same project can result in data loss.  
  
## Remote

This type has no fields.

Configuration specific to clusters with a control plane hosted remotely.

## Local

Configuration specific to clusters with a control plane hosted locally.

Warning: Local control plane clusters must be created in their own project. Local control plane clusters cannot coexist in the same project with any other type of clusters, including non-GDCE clusters. Mixing local control plane GDCE clusters with any other type of clusters in the same project can result in data loss.

JSON representation  
---  
      
    
    {
      "nodeLocation": string,
      "nodeCount": integer,
      "machineFilter": string,
      "sharedDeploymentPolicy": enum ([SharedDeploymentPolicy](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#SharedDeploymentPolicy)),
      "controlPlaneNodeStorageSchema": string
    }  
  
Fields  
---  
`nodeLocation` |  `string` Name of the Google Distributed Cloud Edge zones where this node pool will be created. For example: `us-central1-edge-customer-a`.  
`nodeCount` |  `integer` The number of nodes to serve as replicas of the Control Plane.  
`machineFilter` |  `string` Only machines matching this filter will be allowed to host control plane nodes. The filtering language accepts strings like "name=", and is documented here: [AIP-160](https://google.aip.dev/160).  
`sharedDeploymentPolicy` |  `enum (`[SharedDeploymentPolicy](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#SharedDeploymentPolicy)`)` Policy configuration about how user applications are deployed.  
`controlPlaneNodeStorageSchema` |  `string` Optional. Name for the storage schema of control plane nodes.Warning: Configurable node local storage schema feature is an experimental feature, and is not recommended for general use in production clusters/nodepools.  
  
## SharedDeploymentPolicy

Represents the policy configuration about how user applications are deployed.

Enums  
---  
`SHARED_DEPLOYMENT_POLICY_UNSPECIFIED` | Unspecified.  
`ALLOWED` | User applications can be deployed both on control plane and worker nodes.  
`DISALLOWED` | User applications can not be deployed on control plane nodes and can only be deployed on worker nodes.  
  
## SystemAddonsConfig

Config that customers are allowed to define for GDCE system add-ons.

JSON representation  
---  
      
    
    {
      "ingress": {
        object ([Ingress](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#Ingress))
      },
      "vmServiceConfig": {
        object ([VMServiceConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#VMServiceConfig))
      }
    }  
  
Fields  
---  
`ingress` |  `object (`[Ingress](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#Ingress)`)` Optional. Config for Ingress.  
`vmServiceConfig` |  `object (`[VMServiceConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#VMServiceConfig)`)` Optional. Config for VM Service.  
  
## Ingress

Config for the Ingress add-on which allows customers to create an Ingress object to manage external access to the servers in a cluster. The add-on consists of istiod and istio-ingress.

JSON representation  
---  
      
    
    {
      "disabled": boolean,
      "ipv4Vip": string
    }  
  
Fields  
---  
`disabled` |  `boolean` Optional. Whether Ingress is disabled.  
`ipv4Vip` |  `string` Optional. Ingress VIP.  
  
## VMServiceConfig

VMServiceConfig defines the configuration for GDCE VM Service.

JSON representation  
---  
      
    
    {
      "vmmEnabled": boolean
    }  
  
Fields  
---  
`vmmEnabled` |  `boolean` Optional. Whether VMM is enabled.  
  
## ControlPlaneEncryption

Configuration for Customer-managed KMS key support for control plane nodes.

JSON representation  
---  
      
    
    {
      "kmsKey": string,
      "kmsKeyActiveVersion": string,
      "kmsKeyState": enum ([KmsKeyState](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/KmsKeyState)),
      "kmsStatus": {
        object ([Status](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/Status))
      },
      "resourceState": enum ([ResourceState](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/ResourceState))
    }  
  
Fields  
---  
`kmsKey` |  `string` Optional. The Cloud KMS CryptoKey e.g. projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey} to use for protecting control plane disks. If not specified, a Google-managed key will be used instead.  
`kmsKeyActiveVersion` |  `string` Output only. The Cloud KMS CryptoKeyVersion currently in use for protecting control plane disks. Only applicable if kmsKey is set.  
`kmsKeyState` |  `enum (`[KmsKeyState](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/KmsKeyState)`)` Output only. Availability of the Cloud KMS CryptoKey. If not `KEY_AVAILABLE`, then nodes may go offline as they cannot access their local data. This can be caused by a lack of permissions to use the key, or if the key is disabled or deleted.  
`kmsStatus` |  `object (`[Status](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/Status)`)` Output only. Error status returned by Cloud KMS when using this key. This field may be populated only if `kmsKeyState` is not `KMS_KEY_STATE_KEY_AVAILABLE`. If populated, this field contains the error status reported by Cloud KMS.  
`resourceState` |  `enum (`[ResourceState](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/ResourceState)`)` Output only. The current resource state associated with the cmek.  
  
## Status

Indicates the status of the cluster.

Enums  
---  
`STATUS_UNSPECIFIED` | Status unknown.  
`PROVISIONING` | The cluster is being created.  
`RUNNING` | The cluster is created and fully usable.  
`DELETING` | The cluster is being deleted.  
`ERROR` | The status indicates that some errors occurred while reconciling/deleting the cluster.  
`RECONCILING` | The cluster is undergoing some work such as version upgrades, etc.  
  
## MaintenanceEvent

A Maintenance Event is an operation that could cause temporary disruptions to the cluster workloads, including Google-driven or user-initiated cluster upgrades, user-initiated cluster configuration changes that require restarting nodes, etc.

JSON representation  
---  
      
    
    {
      "uuid": string,
      "targetVersion": string,
      "operation": string,
      "type": enum ([Type](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#Type)),
      "schedule": enum ([Schedule](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#Schedule)),
      "state": enum ([State](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#State)),
      "createTime": string,
      "startTime": string,
      "endTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`uuid` |  `string` Output only. UUID of the maintenance event.  
`targetVersion` |  `string` Output only. The target version of the cluster.  
`operation` |  `string` Output only. The operation for running the maintenance event. Specified in the format projects/*/locations/*/operations/*. If the maintenance event is split into multiple operations (e.g. due to maintenance windows), the latest one is recorded.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#Type)`)` Output only. The type of the maintenance event.  
`schedule` |  `enum (`[Schedule](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#Schedule)`)` Output only. The schedule of the maintenance event.  
`state` |  `enum (`[State](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#State)`)` Output only. The state of the maintenance event.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the maintenance event request was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the maintenance event started.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the maintenance event ended, either successfully or not. If the maintenance event is split into multiple maintenance windows, endTime is only updated when the whole flow ends.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the maintenance event message was updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Type

Indicates the maintenance event type.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified.  
`USER_INITIATED_UPGRADE` | Upgrade initiated by users.  
`GOOGLE_DRIVEN_UPGRADE` | Upgrade driven by Google.  
  
## Schedule

Indicates when the maintenance event should be performed.

Enums  
---  
`SCHEDULE_UNSPECIFIED` | Unspecified.  
`IMMEDIATELY` | Immediately after receiving the request.  
  
## State

Indicates the maintenance event state.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified.  
`RECONCILING` | The maintenance event is ongoing. The cluster might be unusable.  
`SUCCEEDED` | The maintenance event succeeded.  
`FAILED` | The maintenance event failed.  
  
## ReleaseChannel

The release channel a cluster is subscribed to.

Enums  
---  
`RELEASE_CHANNEL_UNSPECIFIED` | Unspecified release channel. This will default to the REGULAR channel.  
`NONE` | No release channel.  
`REGULAR` | Regular release channel.  
  
## SurvivabilityConfig

Configuration of the cluster survivability, e.g., for the case when network connectivity is lost.

JSON representation  
---  
      
    
    {
      "offlineRebootTtl": string
    }  
  
Fields  
---  
`offlineRebootTtl` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Time period that allows the cluster nodes to be rebooted and become functional without network connectivity to Google. The default 0 means not allowed. The maximum is 7 days.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## ConnectionState

ConnectionState holds the current connection state from the cluster to Google.

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#State_1)),
      "updateTime": string
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters#State_1)`)` Output only. The current connection state.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the connection state was last changed.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## State

The connection state.

Enums  
---  
`STATE_UNSPECIFIED` | Unknown connection state.  
`DISCONNECTED` | This cluster is currently disconnected from Google.  
`CONNECTED` | This cluster is currently connected to Google.  
`CONNECTED_AND_SYNCING` | This cluster is currently connected to Google, but may have recently reconnected after a disconnection. It is still syncing back.  
  
## ExternalLoadBalancerPool

External load balancer pool with custom config such as name, manual/auto assign, non-overlapping ipv4 and optional ipv6 address range.

JSON representation  
---  
      
    
    {
      "addressPool": string,
      "ipv4Range": [
        string
      ],
      "ipv6Range": [
        string
      ],
      "avoidBuggyIps": boolean,
      "manualAssign": boolean
    }  
  
Fields  
---  
`addressPool` |  `string` Optional. Name of the external load balancer pool.  
`ipv4Range[]` |  `string` Required. Non-overlapping IPv4 address range of the external load balancer pool.  
`ipv6Range[]` |  `string` Optional. Non-overlapping IPv6 address range of the external load balancer pool.  
`avoidBuggyIps` |  `boolean` Optional. If true, the pool omits IP addresses ending in .0 and .255. Some network hardware drops traffic to these special addresses. Its default value is false.  
`manualAssign` |  `boolean` Optional. If true, addresses in this pool are not automatically assigned to Kubernetes Services. If true, an IP address in this pool is used only when it is specified explicitly by a service. Its default value is false.  
  
## ZoneStorageEncryption

Configuration for Zone Storage CMEK Support

JSON representation  
---  
      
    
    {
      "kmsKey": string,
      "kmsKeyActiveVersion": string,
      "resourceState": enum ([ResourceState](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/ResourceState))
    }  
  
Fields  
---  
`kmsKey` |  `string` Optional. The Cloud KMS Key  
`kmsKeyActiveVersion` |  `string` Output only. The Cloud KMS CryptoKeyVersion currently used for encryption/decryption  
`resourceState` |  `enum (`[ResourceState](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/ResourceState)`)` Output only. The current resource state of the CMEK  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters/create)`

|  Creates a new Cluster in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters/delete)`

|  Deletes a single Cluster.  
  
### `[generateAccessToken](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters/generateAccessToken)`

|  Generates an access token for a Cluster.  
  
### `[generateOfflineCredential](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters/generateOfflineCredential)`

|  Generates an offline credential for a Cluster.  
  
### `[get](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters/get)`

|  Gets details of a single Cluster.  
  
### `[list](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters/list)`

|  Lists Clusters in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters/patch)`

|  Updates the parameters of a single Cluster.  
  
### `[upgrade](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/container/rest/v1/projects.locations.clusters/upgrade)`

|  Upgrades a single cluster.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
