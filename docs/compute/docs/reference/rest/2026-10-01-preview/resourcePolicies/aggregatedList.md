---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/resourcePolicies/aggregatedList/
title: Method: resourcePolicies.aggregatedList \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:09.042406+00:00
---

# Method: resourcePolicies.aggregatedList  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/resourcePolicies/aggregatedList/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: resourcePolicies.aggregatedList Stay organized with collections  Save and categorize content based on your preferences. 

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
        * JSON representation
        * JSON representation
        * JSON representation
      * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-10-01-preview

Retrieves an aggregated list of resource policies.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/aggregated/resourcePolicies?$apiVersion=2026-10-01-preview`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
  
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
`includeAllScopes` |  `boolean` Indicates whether every visible scope for each scope type (zone, region, global) should be included in the response. For new resource types added after this field, the flag has no effect as new resource types will always include every visible scope for each scope type in response. For resource types which predate this field, if this flag is omitted or false, only scopes of the scope types where the resource type is expected to be found will be included.  
`serviceProjectNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The Shared VPC service project id or service project number for which aggregated list request is invoked for subnetworks list-usable api.  
  
### Request body

The request body must be empty.

### Response body

Contains a list of resourcePolicies.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "items": {
        string: {
          "resourcePolicies": [
            {
              "kind": string,
              "id": string,
              "creationTimestamp": string,
              "selfLink": string,
              "region": string,
              "description": string,
              "name": string,
              "status": enum,
              "resourceStatus": {
                "instanceSchedulePolicy": {
                  "nextRunStartTime": string,
                  "lastRunStartTime": string
                }
              },
    
              // The following is a list of mutually exclusive fields. At most one of the
              // fields will be set in a response:
              "snapshotSchedulePolicy": {
                "schedule": {
    
                  // The following is a list of mutually exclusive fields. At most one of the
                  // fields will be set in a response:
                  "hourlySchedule": {
                    "hoursInCycle": integer,
                    "startTime": string,
                    "duration": string
                  },
                  "dailySchedule": {
                    "daysInCycle": integer,
                    "startTime": string,
                    "duration": string
                  },
                  "weeklySchedule": {
                    "dayOfWeeks": [
                      {
                        "day": enum,
                        "startTime": string,
                        "duration": string
                      }
                    ]
                  }
                  // End of mutually exclusive fields.
                },
                "retentionPolicy": {
                  "maxRetentionDays": integer,
                  "onSourceDiskDelete": enum
                },
                "snapshotProperties": {
                  "labels": {
                    string: string,
                    ...
                  },
                  "storageLocations": [
                    string
                  ],
                  "guestFlush": boolean,
                  "chainName": string
                }
              },
              "groupPlacementPolicy": {
                "vmCount": integer,
                "availabilityDomainCount": integer,
                "collocation": enum,
                "gpuTopology": string,
                "acceleratorTopologyMode": enum
              },
              "instanceSchedulePolicy": {
                "vmStartSchedule": {
                  "schedule": string
                },
                "vmStopSchedule": {
                  "schedule": string
                },
                "timeZone": string,
                "startTime": string,
                "expirationTime": string
              },
              "diskConsistencyGroupPolicy": ,
              "workloadPolicy": {
                "type": enum,
                "maxTopologyDistance": enum,
                "acceleratorTopology": string,
                "acceleratorTopologyMode": enum
              }
              // End of mutually exclusive fields.
            }
          ],
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
        },
        ...
      },
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
      },
      "etag": string,
      "unreachables": [
        string
      ]
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of resource.  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items` |  `map (key: string, value: object)` A list of ResourcePolicy resources.**Key:** Name of the scope containing this set of resourcePolicies.  
`items.resourcePolicies[]` |  `object` A list of resourcePolicies contained in this scope.  
`items.resourcePolicies[].snapshotSchedulePolicy` |  `object` Resource policy for persistent disks for creating snapshots.  
`items.resourcePolicies[].snapshotSchedulePolicy.schedule` |  `object` A Vm Maintenance Policy specifies what kind of infrastructure maintenance we are allowed to perform on this VM and when. Schedule that is applied to disks covered by this policy.  
`items.resourcePolicies[].snapshotSchedulePolicy.schedule.hourlySchedule` |  `object`  
`items.resourcePolicies[].snapshotSchedulePolicy.schedule.hourlySchedule.hoursInCycle` |  `integer` Defines a schedule with units measured in hours. The value determines how many hours pass between the start of each cycle.  
`items.resourcePolicies[].snapshotSchedulePolicy.schedule.hourlySchedule.startTime` |  `string` Time within the window to start the operations. It must be in format "HH:MM", where HH : [00-23] and MM : [00-00] GMT.  
`items.resourcePolicies[].snapshotSchedulePolicy.schedule.hourlySchedule.duration` |  `string` Output only. Duration of the time window, automatically chosen to be smallest possible in the given scenario.  
`items.resourcePolicies[].snapshotSchedulePolicy.schedule.dailySchedule` |  `object`  
`items.resourcePolicies[].snapshotSchedulePolicy.schedule.dailySchedule.daysInCycle` |  `integer` Defines a schedule with units measured in days. The value determines how many days pass between the start of each cycle.  
`items.resourcePolicies[].snapshotSchedulePolicy.schedule.dailySchedule.startTime` |  `string` Start time of the window. This must be in UTC format that resolves to one of `00:00`, `04:00`, `08:00`, `12:00`, `16:00`, or `20:00`. For example, both `13:00-5` and `08:00` are valid.  
`items.resourcePolicies[].snapshotSchedulePolicy.schedule.dailySchedule.duration` |  `string` Output only. A predetermined duration for the window, automatically chosen to be the smallest possible in the given scenario.  
`items.resourcePolicies[].snapshotSchedulePolicy.schedule.weeklySchedule` |  `object`  
`items.resourcePolicies[].snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks[]` |  `object` Up to 7 intervals/windows, one for each day of the week.  
`items.resourcePolicies[].snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks[].day` |  `enum` Defines a schedule that runs on specific days of the week. Specify one or more days. The following options are available: MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY.  
`items.resourcePolicies[].snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks[].startTime` |  `string` Time within the window to start the operations. It must be in format "HH:MM", where HH : [00-23] and MM : [00-00] GMT.  
`items.resourcePolicies[].snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks[].duration` |  `string` Output only. Duration of the time window, automatically chosen to be smallest possible in the given scenario.  
`items.resourcePolicies[].snapshotSchedulePolicy.retentionPolicy` |  `object` Retention policy applied to snapshots created by this resource policy.  
`items.resourcePolicies[].snapshotSchedulePolicy.retentionPolicy.maxRetentionDays` |  `integer` Maximum age of the snapshot that is allowed to be kept.  
`items.resourcePolicies[].snapshotSchedulePolicy.retentionPolicy.onSourceDiskDelete` |  `enum` Specifies the behavior to apply to scheduled snapshots when the source disk is deleted.  
`items.resourcePolicies[].snapshotSchedulePolicy.snapshotProperties` |  `object` Properties with which snapshots are created such as labels, encryption keys.  
`items.resourcePolicies[].snapshotSchedulePolicy.snapshotProperties.labels` |  `map (key: string, value: string)` Labels to apply to scheduled snapshots. These can be later modified by the `setLabels` method. Label values may be empty.  
`items.resourcePolicies[].snapshotSchedulePolicy.snapshotProperties.storageLocations[]` |  `string` Cloud Storage bucket storage location of the auto snapshot (regional or multi-regional).  
`items.resourcePolicies[].snapshotSchedulePolicy.snapshotProperties.guestFlush` |  `boolean` Indication to perform a 'guest aware' snapshot.  
`items.resourcePolicies[].snapshotSchedulePolicy.snapshotProperties.chainName` |  `string` Chain name that the snapshot is created in.  
`items.resourcePolicies[].groupPlacementPolicy` |  `object` Resource policy for instances for placement configuration.  
`items.resourcePolicies[].groupPlacementPolicy.vmCount` |  `integer` Number of VMs in this placement group. Google does not recommend that you use this field unless you use a compact policy and you want your policy to work only if it contains this exact number of VMs.  
`items.resourcePolicies[].groupPlacementPolicy.availabilityDomainCount` |  `integer` The number of availability domains to spread instances across. If two instances are in different availability domain, they are not in the same low latency network.  
`items.resourcePolicies[].groupPlacementPolicy.collocation` |  `enum` Specifies network collocation  
`items.resourcePolicies[].groupPlacementPolicy.gpuTopology` |  `string` Specifies the shape of the GPU slice, in slice based GPU families eg. A4X.  
`items.resourcePolicies[].groupPlacementPolicy.acceleratorTopologyMode` |  `enum` Specifies the connection mode for the accelerator topology. If not specified, the default is AUTO_CONNECT.  
`items.resourcePolicies[].instanceSchedulePolicy` |  `object` Resource policy for scheduling instance operations.  
`items.resourcePolicies[].instanceSchedulePolicy.vmStartSchedule` |  `object` Specifies the schedule for starting instances.  
`items.resourcePolicies[].instanceSchedulePolicy.vmStartSchedule.schedule` |  `string` Specifies the frequency for the operation, using the unix-cron format.  
`items.resourcePolicies[].instanceSchedulePolicy.vmStopSchedule` |  `object` Specifies the schedule for stopping instances.  
`items.resourcePolicies[].instanceSchedulePolicy.vmStopSchedule.schedule` |  `string` Specifies the frequency for the operation, using the unix-cron format.  
`items.resourcePolicies[].instanceSchedulePolicy.timeZone` |  `string` Specifies the time zone to be used in interpreting Schedule.schedule. The value of this field must be a time zone name from the tz database: <https://wikipedia.org/wiki/Tz_database>.  
`items.resourcePolicies[].instanceSchedulePolicy.startTime` |  `string` The start time of the schedule. The timestamp is an RFC3339 string.  
`items.resourcePolicies[].instanceSchedulePolicy.expirationTime` |  `string` The expiration time of the schedule. The timestamp is an RFC3339 string.  
`items.resourcePolicies[].diskConsistencyGroupPolicy` |  `object` Resource policy for disk consistency groups.  
`items.resourcePolicies[].workloadPolicy` |  `object` Resource policy for defining instance placement for MIGs.  
`items.resourcePolicies[].workloadPolicy.type` |  `enum` Specifies the intent of the instance placement in the MIG.  
`items.resourcePolicies[].workloadPolicy.maxTopologyDistance` |  `enum` Specifies the maximum distance between instances.  
`items.resourcePolicies[].workloadPolicy.acceleratorTopology` |  `string` Specifies the topology required to create a partition for VMs that have interconnected GPUs.  
`items.resourcePolicies[].workloadPolicy.acceleratorTopologyMode` |  `enum` Specifies the connection mode for the accelerator topology. If not specified, the default is AUTO_CONNECT.  
`items.resourcePolicies[].kind` |  `string` Output only. Type of the resource. Always `compute#resourcePolicies` for resource policies.  
`items.resourcePolicies[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items.resourcePolicies[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items.resourcePolicies[].selfLink` |  `string` Output only. Server-defined fully-qualified URL for this resource.  
`items.resourcePolicies[].region` |  `string`  
`items.resourcePolicies[].description` |  `string`  
`items.resourcePolicies[].name` |  `string` The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`items.resourcePolicies[].status` |  `enum` Output only. The status of resource policy creation.  
`items.resourcePolicies[].resourceStatus` |  `object` Output only. The system status of the resource policy.  
`items.resourcePolicies[].resourceStatus.instanceSchedulePolicy` |  `object` Output only. Specifies a set of output values reffering to the instanceSchedulePolicy system status. This field should have the same name as corresponding policy field.  
`items.resourcePolicies[].resourceStatus.instanceSchedulePolicy.nextRunStartTime` |  `string` Output only. The next time the schedule is planned to run. The actual time might be slightly different. The timestamp is an RFC3339 string.  
`items.resourcePolicies[].resourceStatus.instanceSchedulePolicy.lastRunStartTime` |  `string` Output only. The last time the schedule successfully ran. The timestamp is an RFC3339 string.  
`items.warning` |  `object` Informational warning which replaces the list of resourcePolicies when the list is empty.  
`items.warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`items.warning.message` |  `string` Output only. A human-readable description of the warning code.  
`items.warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`items.warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`items.warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
`nextPageToken` |  `string` Output only. This token allows you to get the next page of results for list requests. If the number of results is larger than `maxResults`, use the `nextPageToken` as a value for the query parameter `pageToken` in the next list request. Subsequent list requests will have their own `nextPageToken` to continue paging through the results.  
`selfLink` |  `string` Output only. Server-defined URL for this resource.  
`warning` |  `object` Output only. Informational warning message.  
`warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`warning.message` |  `string` Output only. A human-readable description of the warning code.  
`warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
`etag` |  `string`  
`unreachables[]` |  `string` Output only. Unreachable resources.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.resourcePolicies.list`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
