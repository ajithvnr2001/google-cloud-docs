---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools
title: REST Resource: projects.locations.vmwareClusters.vmwareNodePools \u00a0|\u00a0 GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:16.753983+00:00
---

# REST Resource: projects.locations.vmwareClusters.vmwareNodePools  |  GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  REST Resource: projects.locations.vmwareClusters.vmwareNodePools Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: VmwareNodePool
    * JSON representation
  * State
  * VmwareNodePoolAutoscalingConfig
    * JSON representation
  * VmwareNodeConfig
    * JSON representation
  * VmwareVsphereConfig
    * JSON representation
  * VmwareVsphereTag
    * JSON representation
  * Methods



## Resource: VmwareNodePool

Resource VmwareNodePool represents a VMware node pool.

##

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "uid": string,
      "state": enum ([State](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools#State)),
      "reconciling": boolean,
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "etag": string,
      "annotations": {
        string: string,
        ...
      },
      "nodePoolAutoscaling": {
        object ([VmwareNodePoolAutoscalingConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools#VmwareNodePoolAutoscalingConfig))
      },
      "config": {
        object ([VmwareNodeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools#VmwareNodeConfig))
      },
      "status": {
        object ([ResourceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus))
      },
      "onPremVersion": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. The resource name of this node pool.  
`displayName` |  `string` The display name for the node pool.  
`uid` |  `string` Output only. The unique identifier of the node pool.  
`state` |  `enum (`[State](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools#State)`)` Output only. The current state of the node pool.  
`reconciling` |  `boolean` Output only. If set, there are currently changes in flight to the node pool.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this node pool was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this node pool was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this node pool was deleted. If the resource is not deleted, this must be emptyUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control.  
`annotations` |  `map (key: string, value: string)` Annotations on the node pool. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`nodePoolAutoscaling` |  `object (`[VmwareNodePoolAutoscalingConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools#VmwareNodePoolAutoscalingConfig)`)` Node pool autoscaling config for the node pool.  
`config` |  `object (`[VmwareNodeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools#VmwareNodeConfig)`)` Required. The node configuration of the node pool.  
`status` |  `object (`[ResourceStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ResourceStatus)`)` Output only. ResourceStatus representing the detailed VMware node pool state.  
`onPremVersion` |  `string` Anthos version for the node pool. Defaults to the user cluster version.  
  
## State

The lifecycle state of the node pool.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`PROVISIONING` | The PROVISIONING state indicates the node pool is being created.  
`RUNNING` | The RUNNING state indicates the node pool has been created and is fully usable.  
`RECONCILING` | The RECONCILING state indicates that the node pool is being updated. It remains available, but potentially with degraded performance.  
`STOPPING` | The STOPPING state indicates the cluster is being deleted  
`ERROR` | The ERROR state indicates the node pool is in a broken unrecoverable state.  
`DEGRADED` | The DEGRADED state indicates the node pool requires user action to restore full functionality.  
  
## VmwareNodePoolAutoscalingConfig

NodePoolAutoscaling config for the NodePool to allow for the kubernetes to scale NodePool.

JSON representation  
---  
      
    
    {
      "minReplicas": integer,
      "maxReplicas": integer
    }  
  
Fields  
---  
`minReplicas` |  `integer` Minimum number of replicas in the NodePool.  
`maxReplicas` |  `integer` Maximum number of replicas in the NodePool.  
  
## VmwareNodeConfig

Parameters that describe the configuration of all nodes within a given node pool.

JSON representation  
---  
      
    
    {
      "cpus": string,
      "memoryMb": string,
      "replicas": string,
      "imageType": string,
      "image": string,
      "bootDiskSizeGb": string,
      "taints": [
        {
          object ([NodeTaint](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/NodeTaint))
        }
      ],
      "labels": {
        string: string,
        ...
      },
      "vsphereConfig": {
        object ([VmwareVsphereConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools#VmwareVsphereConfig))
      },
      "enableLoadBalancer": boolean
    }  
  
Fields  
---  
`cpus` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of CPUs for each node in the node pool.  
`memoryMb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The megabytes of memory for each node in the node pool.  
`replicas` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of nodes in the node pool.  
`imageType` |  `string` Required. The OS image to be used for each node in a node pool. Currently `cos`, `cos_cgv2`, `ubuntu`, `ubuntu_cgv2`, `ubuntu_containerd` and `windows` are supported.  
`image` |  `string` The OS image name in vCenter, only valid when using Windows.  
`bootDiskSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` VMware disk size to be used during creation.  
`taints[]` |  `object (`[NodeTaint](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/NodeTaint)`)` The initial taints assigned to nodes of this node pool.  
`labels` |  `map (key: string, value: string)` The map of Kubernetes labels (key/value pairs) to be applied to each node. These will added in addition to any default label(s) that Kubernetes may apply to the node. In case of conflict in label keys, the applied set may differ depending on the Kubernetes version -- it's best to assume the behavior is undefined and conflicts should be avoided. For more information, including usage and the valid values, see: <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`vsphereConfig` |  `object (`[VmwareVsphereConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools#VmwareVsphereConfig)`)` Specifies the vSphere config for node pool.  
`enableLoadBalancer` |  `boolean` Allow node pool traffic to be load balanced. Only works for clusters with MetalLB load balancers.  
  
## VmwareVsphereConfig

VmwareVsphereConfig represents configuration for the VMware VCenter for node pool.

JSON representation  
---  
      
    
    {
      "datastore": string,
      "tags": [
        {
          object ([VmwareVsphereTag](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools#VmwareVsphereTag))
        }
      ],
      "hostGroups": [
        string
      ]
    }  
  
Fields  
---  
`datastore` |  `string` The name of the vCenter datastore. Inherited from the user cluster.  
`tags[]` |  `object (`[VmwareVsphereTag](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools#VmwareVsphereTag)`)` Tags to apply to VMs.  
`hostGroups[]` |  `string` Vsphere host groups to apply to all VMs in the node pool  
  
## VmwareVsphereTag

VmwareVsphereTag describes a vSphere tag to be placed on VMs in the node pool. For more information, see <https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-E8E854DD-AA97-4E0C-8419-CE84F93C4058.html>

JSON representation  
---  
      
    
    {
      "category": string,
      "tag": string
    }  
  
Fields  
---  
`category` |  `string` The Vsphere tag category.  
`tag` |  `string` The Vsphere tag name.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools/create)`

|  Creates a new VMware node pool in a given project, location and VMWare cluster.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools/delete)`

|  Deletes a single VMware node pool.  
  
### `[enroll](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools/enroll)`

|  Enrolls a VMware node pool to Anthos On-Prem API  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools/get)`

|  Gets details of a single VMware node pool.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools/list)`

|  Lists VMware node pools in a given project, location and VMWare cluster.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools/patch)`

|  Updates the parameters of a single VMware node pool.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-29 UTC."],[],[]] 
