---
url: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupConsumerActivations
title: REST Resource: projects.locations.multicastGroupConsumerActivations \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:29:08.856322+00:00
---

# REST Resource: projects.locations.multicastGroupConsumerActivations  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupConsumerActivations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Reference ](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest)



Send feedback 

#  REST Resource: projects.locations.multicastGroupConsumerActivations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: MulticastGroupConsumerActivation
    * JSON representation
  * Methods



## Resource: MulticastGroupConsumerActivation

Multicast group consumer activation resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "multicastConsumerAssociation": string,
      "description": string,
      "resourceState": enum ([ConsumerResourceState](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/ConsumerResourceState)),
      "state": {
        object ([MulticastResourceState](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/MulticastResourceState))
      },
      "uniqueId": string,
      "multicastGroupRangeActivation": string,
      "logConfig": {
        object ([MulticastLogConfig](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/MulticastLogConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the multicast group consumer activation. Use the following format: `projects/*/locations/*/multicastGroupConsumerActivations/*`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] The timestamp when the multicast group consumer activation was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] The timestamp when the multicast group consumer activation was most recently updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key-value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`multicastConsumerAssociation` |  `string` Required. The resource name of the multicast consumer association that is in the same zone as this multicast group consumer activation. Use the following format: `projects/*/locations/*/multicastConsumerAssociations/*`.  
`description` |  `string` Optional. An optional text description of the multicast group consumer activation.  
`resourceState  
**(deprecated)**` |  `enum (`[ConsumerResourceState](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/ConsumerResourceState)`)` This item is deprecated!Output only. [Deprecated] The resource state of the multicast group consumer activation. Use the state field instead.  
`state` |  `object (`[MulticastResourceState](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/MulticastResourceState)`)` Output only. [Output only] The state of the resource.  
`uniqueId` |  `string` Output only. [Output only] The Google-generated UUID for the resource. This value is unique across all multicast group consumer activation resources. If a group consumer activation is deleted and another with the same name is created, the new group consumer activation is assigned a different uniqueId.  
`multicastGroupRangeActivation` |  `string` Required. The resource name of the multicast group range activation created by the admin in the same zone as this multicast group consumer activation. Use the following format: // `projects/*/locations/*/multicastGroupRangeActivations/*`.  
`logConfig` |  `object (`[MulticastLogConfig](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/MulticastLogConfig)`)` Optional. Specifies the logging options for the activities performed related to the multicast group consumer activation. Defaults to false. If logging is enabled, logs are exported to Cloud Logging.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupConsumerActivations/create)`

|  Creates a new multicast group consumer activation in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupConsumerActivations/delete)`

|  Deletes a single multicast group consumer activation.  
  
### `[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupConsumerActivations/get)`

|  Gets details of a single multicast group consumer activation.  
  
### `[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupConsumerActivations/list)`

|  Lists multicast group consumer activations in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupConsumerActivations/patch)`

|  Updates the parameters of a single multicast group consumer activation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-22 UTC."],[],[]] 
