---
url: https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools
title: REST Resource: projects.locations.workerPools \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:15.368727+00:00
---

# REST Resource: projects.locations.workerPools  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Reference ](https://docs.cloud.google.com/build/docs/api)



Send feedback 

#  REST Resource: projects.locations.workerPools Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: WorkerPool
    * JSON representation
  * State
  * PrivatePoolV1Config
    * JSON representation
  * WorkerConfig
    * JSON representation
  * NetworkConfig
    * JSON representation
  * EgressOption
  * PrivateServiceConnect
    * JSON representation
  * Methods



## Resource: WorkerPool

Configuration for a `WorkerPool`.

Cloud Build owns and maintains a pool of workers for general use and have no access to a project's private network. By default, builds submitted to Cloud Build will use a worker from this pool.

If your build needs access to resources on a private network, create and use a `WorkerPool` to run your builds. Private `WorkerPool`s give your builds access to any single VPC network that you administer, including any on-prem resources connected to that VPC network. For an overview of private pools, see [Private pools overview](https://cloud.google.com/build/docs/private-pools/private-pools-overview).

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "uid": string,
      "annotations": {
        string: string,
        ...
      },
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "state": enum ([State](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools#State)),
      "etag": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "privatePoolV1Config": {
        object ([PrivatePoolV1Config](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools#PrivatePoolV1Config))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the `WorkerPool`, with format `projects/{project}/locations/{location}/workerPools/{workerPool}`. The value of `{workerPool}` is provided by `workerPoolId` in `workerPools.create` request and the value of `{location}` is determined by the endpoint accessed.  
`displayName` |  `string` A user-specified, human-readable name for the `WorkerPool`. If provided, this value must be 1-63 characters.  
`uid` |  `string` Output only. A unique identifier for the `WorkerPool`.  
`annotations` |  `map (key: string, value: string)` User specified annotations. See <https://google.aip.dev/128#annotations> for more details such as format and size limitations.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the request to create the `WorkerPool` was received.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the request to update the `WorkerPool` was received.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the request to delete the `WorkerPool` was received.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools#State)`)` Output only. `WorkerPool` state.  
`etag` |  `string` Output only. Checksum computed by the server. May be sent on update and delete requests to ensure that the client has an up-to-date value before proceeding.  
Configuration for the `WorkerPool`. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`privatePoolV1Config` |  `object (`[PrivatePoolV1Config](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools#PrivatePoolV1Config)`)` Private Pool configuration.  
End of mutually exclusive fields.  
  
## State

State of the `WorkerPool`.

Enums  
---  
`STATE_UNSPECIFIED` | State of the `WorkerPool` is unknown.  
`CREATING` | `WorkerPool` is being created.  
`RUNNING` | `WorkerPool` is running.  
`DELETING` | `WorkerPool` is being deleted: cancelling builds and draining workers.  
`DELETED` | `WorkerPool` is deleted.  
`UPDATING` | `WorkerPool` is being updated; new builds cannot be run.  
  
## PrivatePoolV1Config

Configuration for a V1 `PrivatePool`.

JSON representation  
---  
      
    
    {
      "workerConfig": {
        object ([WorkerConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools#WorkerConfig))
      },
      "networkConfig": {
        object ([NetworkConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools#NetworkConfig))
      },
      "privateServiceConnect": {
        object ([PrivateServiceConnect](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools#PrivateServiceConnect))
      }
    }  
  
Fields  
---  
`workerConfig` |  `object (`[WorkerConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools#WorkerConfig)`)` Machine configuration for the workers in the pool.  
`networkConfig` |  `object (`[NetworkConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools#NetworkConfig)`)` Network configuration for the pool.  
`privateServiceConnect` |  `object (`[PrivateServiceConnect](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools#PrivateServiceConnect)`)` Immutable. Private Service Connect(PSC) Network configuration for the pool.  
  
## WorkerConfig

Defines the configuration to be used for creating workers in the pool.

JSON representation  
---  
      
    
    {
      "machineType": string,
      "diskSizeGb": string,
      "workerRelease": string,
      "rankedMachineSeries": [
        enum ([MachineSeries](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/MachineSeries))
      ],
      "enableNestedVirtualization": boolean
    }  
  
Fields  
---  
`machineType` |  `string` Optional. Machine type of a worker, such as `e2-medium`. See [Worker pool config file](https://cloud.google.com/build/docs/private-pools/worker-pool-config-file-schema). If left blank, Cloud Build will use a sensible default.  
`diskSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size of the disk attached to the worker, in GB. See [Worker pool config file](https://cloud.google.com/build/docs/private-pools/worker-pool-config-file-schema). Specify a value of up to 4000. If `0` is specified, Cloud Build will use a standard disk size.  
`workerRelease` |  `string` Optional. Option to specify which release or release channel (rapid|regular|stable) to use to run this build.  
`rankedMachineSeries[]` |  `enum (`[MachineSeries](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/MachineSeries)`)` Optional. Ranked list (earlier items have higher priority) of Machine Series to consider when provisioning Worker VMs. A concrete machine type will be selected based on machine availability in the given region.  
`enableNestedVirtualization` |  `boolean` Optional. Enable nested virtualization on the worker, if supported by the machine type. By default, nested virtualization is disabled.  
  
## NetworkConfig

Defines the network configuration for the pool.

JSON representation  
---  
      
    
    {
      "peeredNetwork": string,
      "egressOption": enum ([EgressOption](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools#EgressOption)),
      "peeredNetworkIpRange": string
    }  
  
Fields  
---  
`peeredNetwork` |  `string` Required. Immutable. The network definition that the workers are peered to. If this section is left empty, the workers will be peered to `WorkerPool.project_id` on the service producer network. Must be in the format `projects/{project}/global/networks/{network}`, where `{project}` is a project number, such as `12345`, and `{network}` is the name of a VPC network in the project. See [Understanding network configuration options](https://cloud.google.com/build/docs/private-pools/set-up-private-pool-environment)  
`egressOption` |  `enum (`[EgressOption](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools#EgressOption)`)` Option to configure network egress for the workers.  
`peeredNetworkIpRange` |  `string` Immutable. Subnet IP range within the peered network. This is specified in CIDR notation with a slash and the subnet prefix size. You can optionally specify an IP address before the subnet prefix value. e.g. `192.168.0.0/29` would specify an IP range starting at 192.168.0.0 with a prefix size of 29 bits. `/16` would specify a prefix size of 16 bits, with an automatically determined IP within the peered VPC. If unspecified, a value of `/24` will be used.  
  
## EgressOption

Defines the egress option for the pool.

Enums  
---  
`EGRESS_OPTION_UNSPECIFIED` | If set, defaults to PUBLIC_EGRESS.  
`NO_PUBLIC_EGRESS` | If set, workers are created without any public address, which prevents network egress to public IPs unless a network proxy is configured.  
`PUBLIC_EGRESS` | If set, workers are created with a public address which allows for public internet egress.  
  
## PrivateServiceConnect

Defines the Private Service Connect network configuration for the pool.

JSON representation  
---  
      
    
    {
      "networkAttachment": string,
      "publicIpAddressDisabled": boolean,
      "routeAllTraffic": boolean
    }  
  
Fields  
---  
`networkAttachment` |  `string` Required. Immutable. The network attachment that the worker network interface is peered to. Must be in the format `projects/{project}/regions/{region}/networkAttachments/{networkAttachment}`. The region of network attachment must be the same as the worker pool. See [Network Attachments](https://cloud.google.com/vpc/docs/about-network-attachments)  
`publicIpAddressDisabled` |  `boolean` Required. Immutable. Disable public IP on the primary network interface.If true, workers are created without any public address, which prevents network egress to public IPs unless a network proxy is configured. If false, workers are created with a public address which allows for public internet egress. The public address only applies to traffic through the primary network interface. If `routeAllTraffic` is set to true, all traffic will go through the non-primary network interface, this boolean has no effect.  
`routeAllTraffic` |  `boolean` Immutable. Route all traffic through PSC interface. Enable this if you want full control of traffic in the private pool. Configure Cloud NAT for the subnet of network attachment if you need to access public Internet.If false, Only route RFC 1918 (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16) and RFC 6598 (100.64.0.0/10) through PSC interface.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools/create)`

|  Creates a `WorkerPool`.  
  
### `[delete](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools/delete)`

|  Deletes a `WorkerPool`.  
  
### `[get](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools/get)`

|  Returns details of a `WorkerPool`.  
  
### `[list](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools/list)`

|  Lists `WorkerPool`s.  
  
### `[patch](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools/patch)`

|  Updates a `WorkerPool`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
