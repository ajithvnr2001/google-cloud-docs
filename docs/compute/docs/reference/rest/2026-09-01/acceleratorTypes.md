---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/acceleratorTypes/
title: REST Resource: acceleratorTypes \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:01:26.025658+00:00
---

# REST Resource: acceleratorTypes  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/acceleratorTypes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: acceleratorTypes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AcceleratorType
    * JSON representation
  * Methods



## Resource: AcceleratorType

Represents an Accelerator Type resource.

Google Cloud Platform provides graphics processing units (accelerators) that you can add to VM instances to improve or accelerate performance when working with intensive workloads. For more information, read [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "deprecated": {
        "state": enum,
        "replacement": string,
        "deprecated": string,
        "obsolete": string,
        "deleted": string
      },
      "zone": string,
      "selfLink": string,
      "maximumCardsPerInstance": integer,
      "resourceMetadata": {
        "resourceType": string,
        "apiVersion": string
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. The type of the resource. Always `compute#acceleratorType` for accelerator types.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Output only. Name of the resource.  
`description` |  `string` Output only. An optional textual description of the resource.  
`deprecated` |  `object` Output only. The deprecation status associated with this accelerator type.  
`deprecated.state` |  `enum` The deprecation state of this resource. This can be `ACTIVE`, `DEPRECATED`, `OBSOLETE`, or `DELETED`. Operations which communicate the end of life date for an image, can use `ACTIVE`. Operations which create a new resource using a `DEPRECATED` resource will return successfully, but with a warning indicating the deprecated resource and recommending its replacement. Operations which use `OBSOLETE` or `DELETED` resources will be rejected and result in an error.  
`deprecated.replacement` |  `string` The URL of the suggested replacement for a deprecated resource. The suggested replacement resource must be the same kind of resource as the deprecated resource.  
`deprecated.deprecated` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `DEPRECATED`. This is only informational and the status will not change unless the client explicitly changes it.  
`deprecated.obsolete` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `OBSOLETE`. This is only informational and the status will not change unless the client explicitly changes it.  
`deprecated.deleted` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `DELETED`. This is only informational and the status will not change unless the client explicitly changes it.  
`zone` |  `string` Output only. The name of the zone where the accelerator type resides, such as us-central1-a. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.  
`selfLink` |  `string` Output only. Server-defined, fully qualified URL for this resource.  
`maximumCardsPerInstance` |  `integer` Output only. Maximum number of accelerator cards allowed per instance.  
`resourceMetadata` |  `object` Output only. Contains standard resource metadata for an AcceleratorType resource. It is populated for each instance of the AcceleratorType resource, and includes the `apiVersion` the instance was retrieved through, and its canonical `resourceType` name. Available from version 2026-09-01.  
`resourceMetadata.resourceType` |  `string` The canonical resource type name in the format of a resource type as defined by [AIP-123](https://google.aip.dev/123). For example, `"compute.googleapis.com/Instance"`.  
`resourceMetadata.apiVersion` |  `string` The version of the API interface that this resource was retrieved through. For example, `"2025-01-01"` or `"2025-01-01-preview"`.  
  
## Methods  
  
---  
  
### `[aggregatedList](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/acceleratorTypes/aggregatedList)`

|  Retrieves an aggregated list of accelerator types.  
  
### `[get](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/acceleratorTypes/get)`

|  Returns the specified accelerator type.  
  
### `[list](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/acceleratorTypes/list)`

|  Retrieves a list of accelerator types that are available to the specified project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
