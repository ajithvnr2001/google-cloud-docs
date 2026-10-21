---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts
title: REST Resource: services.rollouts \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:28.924736+00:00
---

# REST Resource: services.rollouts  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  REST Resource: services.rollouts Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Rollout
    * JSON representation
  * RolloutStatus
  * TrafficPercentStrategy
    * JSON representation
  * DeleteServiceStrategy
  * Methods



## Resource: Rollout

A rollout resource that defines how service configuration versions are pushed to control plane systems. Typically, you create a new version of the service config, and then create a Rollout to push the service config.

JSON representation  
---  
      
    
    {
      "rolloutId": string,
      "createTime": string,
      "createdBy": string,
      "status": enum ([RolloutStatus](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts#RolloutStatus)),
      "serviceName": string,
    
      // Union field strategy can be only one of the following:
      "trafficPercentStrategy": {
        object ([TrafficPercentStrategy](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts#TrafficPercentStrategy))
      },
      "deleteServiceStrategy": {
        object ([DeleteServiceStrategy](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts#DeleteServiceStrategy))
      }
      // End of list of possible types for union field strategy.
    }  
  
Fields  
---  
`rolloutId` |  `string` Optional. Unique identifier of this Rollout. Must be no longer than 63 characters and only lower case letters, digits, '.', '_' and '-' are allowed.If not specified by client, the server will generate one. The generated id will have the form of , where "date" is the create date in ISO 8601 format. "revision number" is a monotonically increasing positive number that is reset every day for each service. An example of the generated rolloutId is '2016-02-16r1'  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Creation time of the rollout. Readonly.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`createdBy` |  `string` The user who created the Rollout. Readonly.  
`status` |  `enum (`[RolloutStatus](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts#RolloutStatus)`)` The status of this rollout. Readonly. In case of a failed rollout, the system will automatically rollback to the current Rollout version. Readonly.  
`serviceName` |  `string` The name of the service associated with this Rollout.  
Union field `strategy`. Strategy that defines which versions of service configurations should be pushed and how they should be used at runtime. `strategy` can be only one of the following:  
`trafficPercentStrategy` |  `object (`[TrafficPercentStrategy](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts#TrafficPercentStrategy)`)` Google Service Control selects service configurations based on traffic percentage.  
`deleteServiceStrategy` |  `object (`[DeleteServiceStrategy](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts#DeleteServiceStrategy)`)` The strategy associated with a rollout to delete a `ManagedService`. Readonly.  
  
## RolloutStatus

Status of a Rollout.

Enums  
---  
`ROLLOUT_STATUS_UNSPECIFIED` | No status specified.  
`IN_PROGRESS` | The Rollout is in progress.  
`SUCCESS` | The Rollout has completed successfully.  
`CANCELLED` | The Rollout has been cancelled. This can happen if you have overlapping Rollout pushes, and the previous ones will be cancelled.  
`FAILED` | The Rollout has failed and the rollback attempt has failed too.  
`PENDING` | The Rollout has not started yet and is pending for execution.  
`FAILED_ROLLED_BACK` | The Rollout has failed and rolled back to the previous successful Rollout.  
  
## TrafficPercentStrategy

Strategy that specifies how clients of Google Service Controller want to send traffic to use different config versions. This is generally used by API proxy to split traffic based on your configured percentage for each config version.

One example of how to gradually rollout a new service configuration using this strategy: Day 1
    
    
    Rollout {
      id: "example.googleapis.com/rollout_20160206"
      trafficPercentStrategy {
        percentages: {
          "example.googleapis.com/20160201": 70.00
          "example.googleapis.com/20160206": 30.00
        }
      }
    }
    

Day 2
    
    
    Rollout {
      id: "example.googleapis.com/rollout_20160207"
      trafficPercentStrategy: {
        percentages: {
          "example.googleapis.com/20160206": 100.00
        }
      }
    }
    

JSON representation  
---  
      
    
    {
      "percentages": {
        string: number,
        ...
      }
    }  
  
Fields  
---  
`percentages` |  `map (key: string, value: number)` Maps service configuration IDs to their corresponding traffic percentage. key is the service configuration ID, Value is the traffic percentage which must be greater than 0.0 and the sum must equal to 100.0.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## DeleteServiceStrategy

Strategy used to delete a service. This strategy is a placeholder only used by the system generated rollout to delete a service.

## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts/create)`

|  Creates a new service configuration rollout.  
  
### `[get](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts/get)`

|  Gets a service configuration `[rollout](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts#Rollout)`.  
  
### `[list](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts/list)`

|  Lists the history of the service configuration rollouts for a managed service, from the newest to the oldest.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
