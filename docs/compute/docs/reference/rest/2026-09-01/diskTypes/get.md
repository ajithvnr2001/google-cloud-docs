---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/diskTypes/get/
title: Method: diskTypes.get \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:02:47.358341+00:00
---

# Method: diskTypes.get  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/diskTypes/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: diskTypes.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-09-01

Returns the specified disk type.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/zones/{zone}/diskTypes/{diskType}?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`zone` |  `string` The name of the zone for this request.  
`diskType` |  `string` Name of the disk type to return.  
  
### Request body

The request body must be empty.

### Response body

Represents a Disk Type resource.

Google Compute Engine has two Disk Type resources:

  * [Regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDiskTypes)
  * [Zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/diskTypes)



You can choose from a variety of disk types based on your needs. For more information, read [Storage options](https://docs.cloud.google.com/compute/docs/disks).

The `diskTypes` resource represents disk types for a zonal persistent disk. For more information, read [Zonal persistent disks](https://docs.cloud.google.com/compute/docs/disks#pdspecs).

The `regionDiskTypes` resource represents disk types for a regional persistent disk. For more information, read [Regional persistent disks](https://docs.cloud.google.com/compute/docs/disks#repds).

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "validDiskSize": string,
      "deprecated": {
        "state": enum,
        "replacement": string,
        "deprecated": string,
        "obsolete": string,
        "deleted": string
      },
      "zone": string,
      "selfLink": string,
      "defaultDiskSizeGb": string,
      "region": string
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#diskType` for disk types.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Output only. Name of the resource.  
`description` |  `string` Output only. An optional description of this resource.  
`validDiskSize` |  `string` Output only. An optional textual description of the valid disk size, such as "10GB-10TB".  
`deprecated` |  `object` Output only. The deprecation status associated with this disk type.  
`deprecated.state` |  `enum` The deprecation state of this resource. This can be `ACTIVE`, `DEPRECATED`, `OBSOLETE`, or `DELETED`. Operations which communicate the end of life date for an image, can use `ACTIVE`. Operations which create a new resource using a `DEPRECATED` resource will return successfully, but with a warning indicating the deprecated resource and recommending its replacement. Operations which use `OBSOLETE` or `DELETED` resources will be rejected and result in an error.  
`deprecated.replacement` |  `string` The URL of the suggested replacement for a deprecated resource. The suggested replacement resource must be the same kind of resource as the deprecated resource.  
`deprecated.deprecated` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `DEPRECATED`. This is only informational and the status will not change unless the client explicitly changes it.  
`deprecated.obsolete` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `OBSOLETE`. This is only informational and the status will not change unless the client explicitly changes it.  
`deprecated.deleted` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `DELETED`. This is only informational and the status will not change unless the client explicitly changes it.  
`zone` |  `string` Output only. URL of the zone where the disk type resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`defaultDiskSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Server-defined default disk size in GB.  
`region` |  `string` Output only. URL of the region where the disk type resides. Only applicable for regional resources. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. Available from version 2026-09-01.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.diskTypes.get`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
