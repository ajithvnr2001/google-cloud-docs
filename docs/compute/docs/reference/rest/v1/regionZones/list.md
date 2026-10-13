---
url: https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionZones/list/
title: Method: regionZones.list \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:40:06.889723+00:00
---

# Method: regionZones.list  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionZones/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: regionZones.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
      * JSON representation
      * JSON representation
        * JSON representation
        * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Retrieves the list of Zone resources under the specific region available to the specified project.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/zones`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`region` |  `string` Region for this request.  
  
### Query parameters

Parameters  
---  
`maxResults` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The maximum number of results per page that should be returned. If the number of available results is larger than `maxResults`, Compute Engine returns a `nextPageToken` that can be used to get the next page of results in subsequent list requests. Acceptable values are `0` to `500`, inclusive. (Default: `500`)  
`pageToken` |  `string` Specifies a page token to use. Set `pageToken` to the `nextPageToken` returned by a previous list request to get the next page of results.  
`filter` |  `string` A filter expression that filters resources listed in the response. Most Compute resources support two types of filter expressions: expressions that support regular expressions and expressions that follow API improvement proposal [AIP-160](https://google.aip.dev/160). These two types of filter expressions cannot be mixed in one request.If you want to use AIP-160, your expression must specify the field name, an operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The operator must be either `=`, `!=`, `>`, `<`, `<=`, `>=` or `:`.For example, if you are filtering Compute Engine instances, you can exclude instances named `example-instance` by specifying `name != example-instance`.The `:*` comparison can be used to test whether a key has been defined. For example, to find all objects with `owner` label use:
    
    
    labels.owner:*
    

You can also filter nested fields. For example, you could specify `scheduling.automaticRestart = false` to include instances only if they are not scheduled for automatic restarts. You can use filtering on nested fields to filter based on [resource labels](https://docs.cloud.google.com/compute/docs/labeling-resources).To filter on multiple expressions, provide each separate expression within parentheses. For example:
    
    
    (scheduling.automaticRestart = true)
    (cpuPlatform = "Intel Skylake")
    

By default, each expression is an `AND` expression. However, you can include `AND` and `OR` expressions explicitly. For example:
    
    
    (cpuPlatform = "Intel Skylake") OR
    (cpuPlatform = "Intel Broadwell") AND
    (scheduling.automaticRestart = true)
    

If you want to use a regular expression, use the `eq` (equal) or `ne` (not equal) operator against a single un-parenthesized expression with or without quotes or against multiple parenthesized expressions. Examples:`fieldname eq unquoted literal` `fieldname eq 'single quoted literal'` `fieldname eq "double quoted literal"` `(fieldname1 eq literal) (fieldname2 ne "literal")`The literal value is interpreted as a regular expression using Google [RE2](https://github.com/google/re2/wiki/Syntax) library syntax. The literal value must match the entire field.For example, to filter for instances that do not end with name "instance", you would use `name ne .*instance`.You cannot combine constraints on multiple fields using regular expressions.  
`orderBy` |  `string` Sorts list results by a certain order. By default, results are returned in alphanumerical order based on the resource name.You can also sort results in descending order based on the creation timestamp using `orderBy="creationTimestamp desc"`. This sorts results based on the `creationTimestamp` field in reverse chronological order (newest result first). Use this to sort resources like operations so that the newest operation is returned first.Currently, only sorting by `name` or `creationTimestamp desc` is supported.  
`returnPartialSuccess` |  `boolean` Opt-in for partial success behavior which provides partial results in case of failure. The default value is false.For example, when partial success behavior is enabled, aggregatedList for a single zone scope either returns all resources in the zone or no resources, with an error code.  
  
### Request body

The request body must be empty.

### Response body

Contains a list of zone resources.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "items": [
        {
          "kind": string,
          "id": string,
          "creationTimestamp": string,
          "name": string,
          "description": string,
          "status": enum,
          "deprecated": {
            "state": enum,
            "replacement": string,
            "deprecated": string,
            "obsolete": string,
            "deleted": string
          },
          "region": string,
          "selfLink": string,
          "availableCpuPlatforms": [
            string
          ],
          "supportsPzs": boolean,
          "resourceStatus": {
            "upcomingMaintenances": [
              {
                "type": enum,
                "subType": enum,
                "targetResource": string,
                "windowStartTime": {
                  "year": integer,
                  "month": integer,
                  "day": integer,
                  "hours": integer,
                  "minutes": integer,
                  "seconds": integer,
                  "nanos": integer,
    
                  // The following is a list of mutually exclusive fields. At most one of the
                  // fields will be set in a response:
                  "utcOffset": string,
                  "timeZone": {
                    "id": string,
                    "version": string
                  }
                  // End of mutually exclusive fields.
                },
                "windowEndTime": {
                  "year": integer,
                  "month": integer,
                  "day": integer,
                  "hours": integer,
                  "minutes": integer,
                  "seconds": integer,
                  "nanos": integer,
    
                  // The following is a list of mutually exclusive fields. At most one of the
                  // fields will be set in a response:
                  "utcOffset": string,
                  "timeZone": {
                    "id": string,
                    "version": string
                  }
                  // End of mutually exclusive fields.
                }
              }
            ]
          }
        }
      ],
      "nextPageToken": string,
      "selfLink": string,
      "warning": {
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
`kind` |  `string` Output only. Type of resource.  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items[]` |  `object` A list of Zone resources.  
`items[].kind` |  `string` Output only. Type of the resource. Always `compute#zone` for zones.  
`items[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](http://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].name` |  `string` Output only. Name of the resource.  
`items[].description` |  `string` Output only. Textual description of the resource.  
`items[].status` |  `enum` Output only. Status of the zone, either `UP` or `DOWN`.  
`items[].deprecated` |  `object` Output only. The deprecation status associated with this zone.  
`items[].deprecated.state` |  `enum` The deprecation state of this resource. This can be `ACTIVE`, `DEPRECATED`, `OBSOLETE`, or `DELETED`. Operations which communicate the end of life date for an image, can use `ACTIVE`. Operations which create a new resource using a `DEPRECATED` resource will return successfully, but with a warning indicating the deprecated resource and recommending its replacement. Operations which use `OBSOLETE` or `DELETED` resources will be rejected and result in an error.  
`items[].deprecated.replacement` |  `string` The URL of the suggested replacement for a deprecated resource. The suggested replacement resource must be the same kind of resource as the deprecated resource.  
`items[].deprecated.deprecated` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `DEPRECATED`. This is only informational and the status will not change unless the client explicitly changes it.  
`items[].deprecated.obsolete` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `OBSOLETE`. This is only informational and the status will not change unless the client explicitly changes it.  
`items[].deprecated.deleted` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `DELETED`. This is only informational and the status will not change unless the client explicitly changes it.  
`items[].region` |  `string` Output only. Full URL reference to the region which hosts the zone.  
`items[].selfLink` |  `string` Output only. Server-defined URL for the resource.  
`items[].availableCpuPlatforms[]` |  `string` Output only. Available cpu/platform selections for the zone.  
`items[].supportsPzs` |  `boolean` Output only. Reserved for future use.  
`items[].resourceStatus` |  `object`  
`items[].resourceStatus.upcomingMaintenances[]` |  `object` Output only. The upcoming maintenance schedule.  
`items[].resourceStatus.upcomingMaintenances[].type` |  `enum`  
`items[].resourceStatus.upcomingMaintenances[].subType` |  `enum` The maintenance type in which the zone is during the given window.  
`items[].resourceStatus.upcomingMaintenances[].targetResource` |  `string` The target resource that the maintenance window is for. For example, "projects/my-project/zones/us-central1-a".  
`items[].resourceStatus.upcomingMaintenances[].windowStartTime` |  `object` The start civil timestamp of the window. This contains a time zone.  
`items[].resourceStatus.upcomingMaintenances[].windowStartTime.year` |  `integer` Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year.  
`items[].resourceStatus.upcomingMaintenances[].windowStartTime.month` |  `integer` Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month.  
`items[].resourceStatus.upcomingMaintenances[].windowStartTime.day` |  `integer` Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day.  
`items[].resourceStatus.upcomingMaintenances[].windowStartTime.hours` |  `integer` Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value "24:00:00" for scenarios like business closing time.  
`items[].resourceStatus.upcomingMaintenances[].windowStartTime.minutes` |  `integer` Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0.  
`items[].resourceStatus.upcomingMaintenances[].windowStartTime.seconds` |  `integer` Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds.  
`items[].resourceStatus.upcomingMaintenances[].windowStartTime.nanos` |  `integer` Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0.  
`items[].resourceStatus.upcomingMaintenances[].windowStartTime.utcOffset` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`items[].resourceStatus.upcomingMaintenances[].windowStartTime.timeZone` |  `object` Time zone.  
`items[].resourceStatus.upcomingMaintenances[].windowStartTime.timeZone.id` |  `string` IANA Time Zone Database time zone. For example "America/New_York".  
`items[].resourceStatus.upcomingMaintenances[].windowStartTime.timeZone.version` |  `string` Optional. IANA Time Zone Database version number. For example "2019a".  
`items[].resourceStatus.upcomingMaintenances[].windowEndTime` |  `object` The end civil timestamp of the window (not inclusive). This contains a time zone.  
`items[].resourceStatus.upcomingMaintenances[].windowEndTime.year` |  `integer` Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year.  
`items[].resourceStatus.upcomingMaintenances[].windowEndTime.month` |  `integer` Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month.  
`items[].resourceStatus.upcomingMaintenances[].windowEndTime.day` |  `integer` Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day.  
`items[].resourceStatus.upcomingMaintenances[].windowEndTime.hours` |  `integer` Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value "24:00:00" for scenarios like business closing time.  
`items[].resourceStatus.upcomingMaintenances[].windowEndTime.minutes` |  `integer` Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0.  
`items[].resourceStatus.upcomingMaintenances[].windowEndTime.seconds` |  `integer` Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds.  
`items[].resourceStatus.upcomingMaintenances[].windowEndTime.nanos` |  `integer` Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0.  
`items[].resourceStatus.upcomingMaintenances[].windowEndTime.utcOffset` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`items[].resourceStatus.upcomingMaintenances[].windowEndTime.timeZone` |  `object` Time zone.  
`items[].resourceStatus.upcomingMaintenances[].windowEndTime.timeZone.id` |  `string` IANA Time Zone Database time zone. For example "America/New_York".  
`items[].resourceStatus.upcomingMaintenances[].windowEndTime.timeZone.version` |  `string` Optional. IANA Time Zone Database version number. For example "2019a".  
`nextPageToken` |  `string` Output only. This token allows you to get the next page of results for list requests. If the number of results is larger than `maxResults`, use the `nextPageToken` as a value for the query parameter `pageToken` in the next list request. Subsequent list requests will have their own `nextPageToken` to continue paging through the results.  
`selfLink` |  `string` Output only. Server-defined URL for this resource.  
`warning` |  `object` Output only. Informational warning message.  
`warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`warning.message` |  `string` Output only. A human-readable description of the warning code.  
`warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.zones.list`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
