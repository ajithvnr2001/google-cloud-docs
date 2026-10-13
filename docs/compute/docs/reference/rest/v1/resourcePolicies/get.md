---
url: https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/get/
title: Method: resourcePolicies.get \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:55:33.684079+00:00
---

# Method: resourcePolicies.get  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: resourcePolicies.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
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
  * Authorization scopes
  * IAM Permissions
  * Try it!



Retrieves all information of the specified resource policy.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/resourcePolicies/{resourcePolicy}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`region` |  `string` Name of the region for this request.  
`resourcePolicy` |  `string` Name of the resource policy to retrieve.  
  
### Request body

The request body must be empty.

### Response body

Represents a Resource Policy resource. You can use resource policies to schedule actions for some Compute Engine resources. For example, you can use them to [schedule persistent disk snapshots](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots).

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
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
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#resourcePolicies` for resource policies.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`selfLink` |  `string` Output only. Server-defined fully-qualified URL for this resource.  
`region` |  `string`  
`description` |  `string`  
`name` |  `string` The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`status` |  `enum` Output only. The status of resource policy creation.  
`resourceStatus` |  `object` Output only. The system status of the resource policy.  
`resourceStatus.instanceSchedulePolicy` |  `object` Output only. Specifies a set of output values reffering to the instanceSchedulePolicy system status. This field should have the same name as corresponding policy field.  
`resourceStatus.instanceSchedulePolicy.nextRunStartTime` |  `string` Output only. The next time the schedule is planned to run. The actual time might be slightly different. The timestamp is an RFC3339 string.  
`resourceStatus.instanceSchedulePolicy.lastRunStartTime` |  `string` Output only. The last time the schedule successfully ran. The timestamp is an RFC3339 string.  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`snapshotSchedulePolicy` |  `object` Resource policy for persistent disks for creating snapshots.  
`snapshotSchedulePolicy.schedule` |  `object` A Vm Maintenance Policy specifies what kind of infrastructure maintenance we are allowed to perform on this VM and when. Schedule that is applied to disks covered by this policy.  
`snapshotSchedulePolicy.schedule.hourlySchedule` |  `object`  
`snapshotSchedulePolicy.schedule.hourlySchedule.hoursInCycle` |  `integer` Defines a schedule with units measured in hours. The value determines how many hours pass between the start of each cycle.  
`snapshotSchedulePolicy.schedule.hourlySchedule.startTime` |  `string` Time within the window to start the operations. It must be in format "HH:MM", where HH : [00-23] and MM : [00-00] GMT.  
`snapshotSchedulePolicy.schedule.hourlySchedule.duration` |  `string` Output only. Duration of the time window, automatically chosen to be smallest possible in the given scenario.  
`snapshotSchedulePolicy.schedule.dailySchedule` |  `object`  
`snapshotSchedulePolicy.schedule.dailySchedule.daysInCycle` |  `integer` Defines a schedule with units measured in days. The value determines how many days pass between the start of each cycle.  
`snapshotSchedulePolicy.schedule.dailySchedule.startTime` |  `string` Start time of the window. This must be in UTC format that resolves to one of `00:00`, `04:00`, `08:00`, `12:00`, `16:00`, or `20:00`. For example, both `13:00-5` and `08:00` are valid.  
`snapshotSchedulePolicy.schedule.dailySchedule.duration` |  `string` Output only. A predetermined duration for the window, automatically chosen to be the smallest possible in the given scenario.  
`snapshotSchedulePolicy.schedule.weeklySchedule` |  `object`  
`snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks[]` |  `object` Up to 7 intervals/windows, one for each day of the week.  
`snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks[].day` |  `enum` Defines a schedule that runs on specific days of the week. Specify one or more days. The following options are available: MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY.  
`snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks[].startTime` |  `string` Time within the window to start the operations. It must be in format "HH:MM", where HH : [00-23] and MM : [00-00] GMT.  
`snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks[].duration` |  `string` Output only. Duration of the time window, automatically chosen to be smallest possible in the given scenario.  
`snapshotSchedulePolicy.retentionPolicy` |  `object` Retention policy applied to snapshots created by this resource policy.  
`snapshotSchedulePolicy.retentionPolicy.maxRetentionDays` |  `integer` Maximum age of the snapshot that is allowed to be kept.  
`snapshotSchedulePolicy.retentionPolicy.onSourceDiskDelete` |  `enum` Specifies the behavior to apply to scheduled snapshots when the source disk is deleted.  
`snapshotSchedulePolicy.snapshotProperties` |  `object` Properties with which snapshots are created such as labels, encryption keys.  
`snapshotSchedulePolicy.snapshotProperties.labels` |  `map (key: string, value: string)` Labels to apply to scheduled snapshots. These can be later modified by the `setLabels` method. Label values may be empty.  
`snapshotSchedulePolicy.snapshotProperties.storageLocations[]` |  `string` Cloud Storage bucket storage location of the auto snapshot (regional or multi-regional).  
`snapshotSchedulePolicy.snapshotProperties.guestFlush` |  `boolean` Indication to perform a 'guest aware' snapshot.  
`snapshotSchedulePolicy.snapshotProperties.chainName` |  `string` Chain name that the snapshot is created in.  
`groupPlacementPolicy` |  `object` Resource policy for instances for placement configuration.  
`groupPlacementPolicy.vmCount` |  `integer` Number of VMs in this placement group. Google does not recommend that you use this field unless you use a compact policy and you want your policy to work only if it contains this exact number of VMs.  
`groupPlacementPolicy.availabilityDomainCount` |  `integer` The number of availability domains to spread instances across. If two instances are in different availability domain, they are not in the same low latency network.  
`groupPlacementPolicy.collocation` |  `enum` Specifies network collocation  
`groupPlacementPolicy.gpuTopology` |  `string` Specifies the shape of the GPU slice, in slice based GPU families eg. A4X.  
`groupPlacementPolicy.acceleratorTopologyMode` |  `enum` Specifies the connection mode for the accelerator topology. If not specified, the default is AUTO_CONNECT.  
`instanceSchedulePolicy` |  `object` Resource policy for scheduling instance operations.  
`instanceSchedulePolicy.vmStartSchedule` |  `object` Specifies the schedule for starting instances.  
`instanceSchedulePolicy.vmStartSchedule.schedule` |  `string` Specifies the frequency for the operation, using the unix-cron format.  
`instanceSchedulePolicy.vmStopSchedule` |  `object` Specifies the schedule for stopping instances.  
`instanceSchedulePolicy.vmStopSchedule.schedule` |  `string` Specifies the frequency for the operation, using the unix-cron format.  
`instanceSchedulePolicy.timeZone` |  `string` Specifies the time zone to be used in interpreting Schedule.schedule. The value of this field must be a time zone name from the tz database: <https://wikipedia.org/wiki/Tz_database>.  
`instanceSchedulePolicy.startTime` |  `string` The start time of the schedule. The timestamp is an RFC3339 string.  
`instanceSchedulePolicy.expirationTime` |  `string` The expiration time of the schedule. The timestamp is an RFC3339 string.  
`diskConsistencyGroupPolicy` |  `object` Resource policy for disk consistency groups.  
`workloadPolicy` |  `object` Resource policy for defining instance placement for MIGs.  
`workloadPolicy.type` |  `enum` Specifies the intent of the instance placement in the MIG.  
`workloadPolicy.maxTopologyDistance` |  `enum` Specifies the maximum distance between instances.  
`workloadPolicy.acceleratorTopology` |  `string` Specifies the topology required to create a partition for VMs that have interconnected GPUs.  
`workloadPolicy.acceleratorTopologyMode` |  `enum` Specifies the connection mode for the accelerator topology. If not specified, the default is AUTO_CONNECT.  
End of mutually exclusive fields.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.resourcePolicies.get`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
