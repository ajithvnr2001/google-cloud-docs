---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores
title: REST Resource: projects.locations.datastores \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:04.541669+00:00
---

# REST Resource: projects.locations.datastores  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  REST Resource: projects.locations.datastores Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Datastore
    * JSON representation
  * NfsDatastore
    * JSON representation
  * GoogleFileService
    * JSON representation
  * ThirdPartyFileService
    * JSON representation
  * GoogleVmwareFileService
  * State
  * Methods



## Resource: Datastore

Represents a datastore resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "description": string,
      "clusters": [
        string
      ],
      "nfsDatastore": {
        object ([NfsDatastore](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores#NfsDatastore))
      },
      "state": enum ([State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores#State)),
      "uid": string,
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The resource name of this datastore. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/datastores/datastore`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last update time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`description` |  `string` Optional. User-provided description for this datastore  
`clusters[]` |  `string` Output only. Clusters to which the datastore is attached.  
`nfsDatastore` |  `object (`[NfsDatastore](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores#NfsDatastore)`)` Required. Settings for the NFS datastore.  
`state` |  `enum (`[State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores#State)`)` Output only. The state of the Datastore.  
`uid` |  `string` Output only. System-generated unique identifier for the resource.  
`etag` |  `string` Optional. Checksum that may be sent on update and delete requests to ensure that the user-provided value is up to date before the server processes a request. The server computes checksums based on the value of other fields in the request.  
  
## NfsDatastore

The NFS datastore configuration.

JSON representation  
---  
      
    
    {
    
      // Union field FileServiceOption can be only one of the following:
      "googleFileService": {
        object ([GoogleFileService](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores#GoogleFileService))
      },
      "thirdPartyFileService": {
        object ([ThirdPartyFileService](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores#ThirdPartyFileService))
      },
      "googleVmwareFileService": {
        object ([GoogleVmwareFileService](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores#GoogleVmwareFileService))
      }
      // End of list of possible types for union field FileServiceOption.
    }  
  
Fields  
---  
Union field `FileServiceOption`. The file service option of the NFS datastore. `FileServiceOption` can be only one of the following:  
`googleFileService` |  `object (`[GoogleFileService](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores#GoogleFileService)`)` Google file service configuration  
`thirdPartyFileService` |  `object (`[ThirdPartyFileService](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores#ThirdPartyFileService)`)` Third party file service configuration  
`googleVmwareFileService` |  `object (`[GoogleVmwareFileService](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores#GoogleVmwareFileService)`)` GCVE file service configuration  
  
## GoogleFileService

Google service file service configuration

JSON representation  
---  
      
    
    {
    
      // Union field FileServiceOption can be only one of the following:
      "netappVolume": string,
      "filestoreInstance": string
      // End of list of possible types for union field FileServiceOption.
    }  
  
Fields  
---  
Union field `FileServiceOption`. Google service file service name `FileServiceOption` can be only one of the following:  
`netappVolume` |  `string` Google netapp volume resource name e.g. projects/my-project/locations/me-west1-b/volumes/my-volume  
`filestoreInstance` |  `string` Google filestore instance resource name e.g. projects/my-project/locations/me-west1-b/instances/my-instance  
  
## ThirdPartyFileService

Third party file service configuration

JSON representation  
---  
      
    
    {
      "servers": [
        string
      ],
      "fileShare": string,
      "network": string
    }  
  
Fields  
---  
`servers[]` |  `string` Required. Server IP addresses of the NFS file service. NFS v3, provide a single IP address or DNS name. Multiple servers can be supported in future when NFS 4.1 protocol support is enabled.  
`fileShare` |  `string` Required. Required Mount Folder name  
`network` |  `string` Required. Required to identify vpc peering used for NFS access network name of NFS's vpc e.g. projects/project-id/global/networks/my-network_id  
  
## GoogleVmwareFileService

This type has no fields.

Volume message captures user inputs for creation of file services managed by GCVE

## State

The state of the Datastore

Enums  
---  
`STATE_UNSPECIFIED` | The default value. This value should never be used.  
`CREATING` | The NFS volume is being created.  
`ACTIVE` | The NFS volume is active.  
`UPDATING` | The NFS volume is being updated.  
`DELETING` | The NFS volume is being deleted.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores/create)`

|  Creates a new `Datastore` resource in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores/delete)`

|  Deletes a `Datastore` resource.  
  
### `[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores/get)`

|  Retrieves a `Datastore` resource by its resource name.  
  
### `[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores/list)`

|  Lists `Datastore` resources in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.datastores/patch)`

|  Modifies a Datastore resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
