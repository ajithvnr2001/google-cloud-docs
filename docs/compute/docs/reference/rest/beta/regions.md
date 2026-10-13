---
url: https://docs.cloud.google.com/compute/docs/reference/rest/beta/regions/
title: REST Resource: regions \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:26.080951+00:00
---

# REST Resource: regions  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/beta/regions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: regions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Region
    * JSON representation
      * JSON representation
      * JSON representation
  * Methods



## Resource: Region

Represents a Region resource.

A region is a geographical area where a resource is located. For more information, read [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources).

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "status": enum,
      "zones": [
        string
      ],
      "quotas": [
        {
          "metric": enum,
          "limit": number,
          "usage": number,
          "owner": string
        }
      ],
      "deprecated": {
        "state": enum,
        "replacement": string,
        "deprecated": string,
        "obsolete": string,
        "deleted": string,
        "stateOverride": {
          "locationRolloutPolicies": {
            string: string,
            ...
          },
          "defaultRolloutTime": string
        }
      },
      "selfLink": string,
      "supportsPzs": boolean,
      "quotaStatusWarning": {
        "code": enum,
        "message": string,
        "data": [
          {
            "key": string,
            "value": string
          }
        ]
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#region` for regions.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Output only. Name of the resource.  
`description` |  `string` Output only. Textual description of the resource.  
`status` |  `enum` Output only. Status of the region, either `UP` or `DOWN`.  
`zones[]` |  `string` Output only. A list of zones available in this region, in the form of resource URLs.  
`quotas[]` |  `object` Output only. Quotas assigned to this region.  
`quotas[].metric` |  `enum` Output only. Name of the quota metric.  
`quotas[].limit` |  `number` Output only. Quota limit for this metric.  
`quotas[].usage` |  `number` Output only. Current usage of this metric.  
`quotas[].owner` |  `string` Output only. Owning resource. This is the resource on which this quota is applied.  
`deprecated` |  `object` Output only. The deprecation status associated with this region.  
`deprecated.state` |  `enum` The deprecation state of this resource. This can be `ACTIVE`, `DEPRECATED`, `OBSOLETE`, or `DELETED`. Operations which communicate the end of life date for an image, can use `ACTIVE`. Operations which create a new resource using a `DEPRECATED` resource will return successfully, but with a warning indicating the deprecated resource and recommending its replacement. Operations which use `OBSOLETE` or `DELETED` resources will be rejected and result in an error.  
`deprecated.replacement` |  `string` The URL of the suggested replacement for a deprecated resource. The suggested replacement resource must be the same kind of resource as the deprecated resource.  
`deprecated.deprecated` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `DEPRECATED`. This is only informational and the status will not change unless the client explicitly changes it.  
`deprecated.obsolete` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `OBSOLETE`. This is only informational and the status will not change unless the client explicitly changes it.  
`deprecated.deleted` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `DELETED`. This is only informational and the status will not change unless the client explicitly changes it.  
`deprecated.stateOverride` |  `object` The rollout policy for this deprecation. This policy is only enforced by image family views. The rollout policy restricts the zones where the associated resource is considered in a deprecated state. When the rollout policy does not include the user specified zone, or if the zone is rolled out, the associated resource is considered in a deprecated state.The rollout policy for this deprecation is read-only, except for allowlisted users. This field might not be configured. To view the latest non-deprecated image in a specific zone, use the `imageFamilyViews.get` method.  
`deprecated.stateOverride.locationRolloutPolicies` |  `map (key: string, value: string)` Location based rollout policies to apply to the resource.Currently only zone names are supported and must be represented as valid URLs, like: zones/us-central1-a.The value expects an [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the update is considered rolled out to the specified location.  
`deprecated.stateOverride.defaultRolloutTime` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the update is considered rolled out to any zone that is not explicitly stated.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`supportsPzs` |  `boolean` Output only. Reserved for future use.  
`quotaStatusWarning` |  `object` Output only. Warning of fetching the `quotas` field for this region. This field is populated only if fetching of the `quotas` field fails.  
`quotaStatusWarning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`quotaStatusWarning.message` |  `string` Output only. A human-readable description of the warning code.  
`quotaStatusWarning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`quotaStatusWarning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`quotaStatusWarning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/compute/docs/reference/rest/beta/regions/get)`

|  Returns the specified Region resource.  
  
### `[list](https://docs.cloud.google.com/compute/docs/reference/rest/beta/regions/list)`

|  Retrieves the list of region resources available to the specified project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-14 UTC."],[],[]] 
