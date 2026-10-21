---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies
title: REST Resource: projects.locations.networkPolicies \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:08.096751+00:00
---

# REST Resource: projects.locations.networkPolicies  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  REST Resource: projects.locations.networkPolicies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: NetworkPolicy
    * JSON representation
  * NetworkService
    * JSON representation
  * State
  * Methods



## Resource: NetworkPolicy

Represents a network policy resource. Network policies are regional resources. You can use a network policy to enable or disable internet access and external IP access. Network policies are associated with a VMware Engine network, which might span across regions. For a given region, a network policy applies to all private clouds in the VMware Engine network associated with the policy.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "internetAccess": {
        object ([NetworkService](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies#NetworkService))
      },
      "externalIp": {
        object ([NetworkService](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies#NetworkService))
      },
      "edgeServicesCidr": string,
      "uid": string,
      "vmwareEngineNetwork": string,
      "description": string,
      "vmwareEngineNetworkCanonical": string
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The resource name of this network policy. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/networkPolicies/my-network-policy`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last update time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`internetAccess` |  `object (`[NetworkService](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies#NetworkService)`)` Network service that allows VMware workloads to access the internet.  
`externalIp` |  `object (`[NetworkService](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies#NetworkService)`)` Network service that allows External IP addresses to be assigned to VMware workloads. This service can only be enabled when `internetAccess` is also enabled.  
`edgeServicesCidr` |  `string` Required. IP address range in CIDR notation used to create internet access and external IP access. An RFC 1918 CIDR block, with a "/26" prefix, is required. The range cannot overlap with any prefixes either in the consumer VPC network or in use by the private clouds attached to that VPC network.  
`uid` |  `string` Output only. System-generated unique identifier for the resource.  
`vmwareEngineNetwork` |  `string` Optional. The relative resource name of the VMware Engine network. Specify the name in the following form: `projects/{project}/locations/{location}/vmwareEngineNetworks/{vmwareEngineNetworkId}` where `{project}` can either be a project number or a project ID.  
`description` |  `string` Optional. User-provided description for this network policy.  
`vmwareEngineNetworkCanonical` |  `string` Output only. The canonical name of the VMware Engine network in the form: `projects/{projectNumber}/locations/{location}/vmwareEngineNetworks/{vmwareEngineNetworkId}`  
  
## NetworkService

Represents a network service that is managed by a `NetworkPolicy` resource. A network service provides a way to control an aspect of external access to VMware workloads. For example, whether the VMware workloads in the private clouds governed by a network policy can access or be accessed from the internet.

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "state": enum ([State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies#State))
    }  
  
Fields  
---  
`enabled` |  `boolean` True if the service is enabled; false otherwise.  
`state` |  `enum (`[State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies#State)`)` Output only. State of the service. New values may be added to this enum when appropriate.  
  
## State

Enum State defines possible states of a network policy controlled service.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified service state. This is the default value.  
`UNPROVISIONED` | Service is not provisioned.  
`RECONCILING` | Service is in the process of being provisioned/deprovisioned.  
`ACTIVE` | Service is active.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies/create)`

|  Creates a new network policy in a given VMware Engine network of a project and location (region).  
  
### `[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies/delete)`

|  Deletes a `NetworkPolicy` resource.  
  
### `[fetchExternalAddresses](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies/fetchExternalAddresses)`

|  Lists external IP addresses assigned to VMware workload VMs within the scope of the given network policy.  
  
### `[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies/get)`

|  Retrieves a `NetworkPolicy` resource by its resource name.  
  
### `[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies/list)`

|  Lists `NetworkPolicy` resources in a specified project and location.  
  
### `[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPolicies/patch)`

|  Modifies a `NetworkPolicy` resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
