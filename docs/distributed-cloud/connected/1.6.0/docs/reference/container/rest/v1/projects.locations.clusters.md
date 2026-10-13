---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters
title: REST Resource: projects.locations.clusters \u00a0|\u00a0 Google Distributed Cloud connected, version 1.6.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:54.320582+00:00
---

# REST Resource: projects.locations.clusters  |  Google Distributed Cloud connected, version 1.6.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters

Select versionkeyboard_arrow_down

  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
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
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/apis)



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
        object ([Fleet](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters#Fleet))
      },
      "networking": {
        object ([ClusterNetworking](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters#ClusterNetworking))
      },
      "authorization": {
        object ([Authorization](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters#Authorization))
      },
      "defaultMaxPodsPerNode": integer,
      "endpoint": string,
      "clusterCaCertificate": string,
      "maintenancePolicy": {
        object ([MaintenancePolicy](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters#MaintenancePolicy))
      },
      "controlPlaneVersion": string,
      "nodeVersion": string
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the cluster.  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The time when the cluster was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The time when the cluster was last updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`labels` |  `map (key: string, value: string)` Labels associated with this resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`fleet` |  `object (`[Fleet](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters#Fleet)`)` Optional. Fleet configuration.  
`networking` |  `object (`[ClusterNetworking](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters#ClusterNetworking)`)` Required. Cluster-wide networking configuration.  
`authorization` |  `object (`[Authorization](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters#Authorization)`)` Required. Immutable. RBAC policy that will be applied and managed by GEC.  
`defaultMaxPodsPerNode` |  `integer` Optional. The default maximum number of pods per node used if a maximum value is not specified explicitly for a node pool in this cluster. If unspecified, the Kubernetes default value will be used.  
`endpoint` |  `string` Output only. The IP address of the Kubernetes API server.  
`clusterCaCertificate` |  `string` Output only. The PEM-encoded public certificate of the cluster's CA.  
`maintenancePolicy` |  `object (`[MaintenancePolicy](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters#MaintenancePolicy)`)` Optional. Cluster-wide maintenance policy configuration.  
`controlPlaneVersion` |  `string` Output only. The control plane release version  
`nodeVersion` |  `string` Output only. The lowest release version among all worker nodes. This field can be empty if the cluster does not have any worker nodes.  
  
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
        object ([ClusterUser](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters#ClusterUser))
      }
    }  
  
Fields  
---  
`adminUsers` |  `object (`[ClusterUser](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters#ClusterUser)`)` Required. User that will be granted the cluster-admin role on the cluster, providing full access to the cluster. Currently, this is a singular field, but will be expanded to allow multiple admins in the future.  
  
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
        object ([MaintenanceWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters#MaintenanceWindow))
      }
    }  
  
Fields  
---  
`window` |  `object (`[MaintenanceWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters#MaintenanceWindow)`)` Specifies the maintenance window in which maintenance may be performed.  
  
## MaintenanceWindow

Maintenance window configuration

JSON representation  
---  
      
    
    {
      "recurringWindow": {
        object ([RecurringTimeWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters#RecurringTimeWindow))
      }
    }  
  
Fields  
---  
`recurringWindow` |  `object (`[RecurringTimeWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters#RecurringTimeWindow)`)` Configuration of a recurring maintenance window.  
  
## RecurringTimeWindow

Represents an arbitrary window of time that recurs.

JSON representation  
---  
      
    
    {
      "window": {
        object ([TimeWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters#TimeWindow))
      },
      "recurrence": string
    }  
  
Fields  
---  
`window` |  `object (`[TimeWindow](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters#TimeWindow)`)` The window of the first recurrence.  
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
`startTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` The time that the window first starts.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`endTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` The time that the window ends. The end time must take place after the start time.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters/create)`

|  Creates a new Cluster in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters/delete)`

|  Deletes a single Cluster.  
  
### `[generateAccessToken](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters/generateAccessToken)`

|  Generates an access token for a Cluster.  
  
### `[get](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters/get)`

|  Gets details of a single Cluster.  
  
### `[list](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters/list)`

|  Lists Clusters in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters/patch)`

|  Updates the parameters of a single Cluster.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
