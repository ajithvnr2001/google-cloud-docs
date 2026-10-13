---
url: https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics
title: REST Resource: admin.projects.locations.topics \u00a0|\u00a0 Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:48.550365+00:00
---

# REST Resource: admin.projects.locations.topics  |  Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)



Send feedback 

#  REST Resource: admin.projects.locations.topics Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Topic
    * JSON representation
  * PartitionConfig
    * JSON representation
  * Capacity
    * JSON representation
  * RetentionConfig
    * JSON representation
  * ReservationConfig
    * JSON representation
  * Methods



## Resource: Topic

Metadata about a topic resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "partitionConfig": {
        object ([PartitionConfig](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics#PartitionConfig))
      },
      "retentionConfig": {
        object ([RetentionConfig](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics#RetentionConfig))
      },
      "reservationConfig": {
        object ([ReservationConfig](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics#ReservationConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` The name of the topic. Structured like: projects/{project_number}/locations/{location}/topics/{topicId}  
`partitionConfig` |  `object (`[PartitionConfig](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics#PartitionConfig)`)` The settings for this topic's partitions.  
`retentionConfig` |  `object (`[RetentionConfig](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics#RetentionConfig)`)` The settings for this topic's message retention.  
`reservationConfig` |  `object (`[ReservationConfig](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics#ReservationConfig)`)` The settings for this topic's Reservation usage.  
  
## PartitionConfig

The settings for a topic's partitions.

JSON representation  
---  
      
    
    {
      "count": string,
    
      // Union field dimension can be only one of the following:
      "scale": integer,
      "capacity": {
        object ([Capacity](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics#Capacity))
      }
      // End of list of possible types for union field dimension.
    }  
  
Fields  
---  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of partitions in the topic. Must be at least 1.Once a topic has been created the number of partitions can be increased but not decreased. Message ordering is not guaranteed across a topic resize. For more information see <https://cloud.google.com/pubsub/lite/docs/topics#scaling_capacity>  
Union field `dimension`. The throughput dimension of this topic. `dimension` can be only one of the following:  
`scale  
**(deprecated)**` |  `integer` This item is deprecated!DEPRECATED: Use capacity instead which can express a superset of configurations.Every partition in the topic is allocated throughput equivalent to `scale` times the standard partition throughput (4 MiB/s). This is also reflected in the cost of this topic; a topic with `scale` of 2 and count of 10 is charged for 20 partitions. This value must be in the range [1,4].  
`capacity` |  `object (`[Capacity](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics#Capacity)`)` The capacity configuration.  
  
## Capacity

The throughput capacity configuration for each partition.

JSON representation  
---  
      
    
    {
      "publishMibPerSec": integer,
      "subscribeMibPerSec": integer
    }  
  
Fields  
---  
`publishMibPerSec` |  `integer` Publish throughput capacity per partition in MiB/s. Must be >= 4 and <= 16.  
`subscribeMibPerSec` |  `integer` Subscribe throughput capacity per partition in MiB/s. Must be >= 4 and <= 32.  
  
## RetentionConfig

The settings for a topic's message retention.

JSON representation  
---  
      
    
    {
      "perPartitionBytes": string,
      "period": string
    }  
  
Fields  
---  
`perPartitionBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The provisioned storage, in bytes, per partition. If the number of bytes stored in any of the topic's partitions grows beyond this value, older messages will be dropped to make room for newer ones, regardless of the value of `period`.  
`period` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` How long a published message is retained. If unset, messages will be retained as long as the bytes retained for each partition is below `perPartitionBytes`.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## ReservationConfig

The settings for this topic's Reservation usage.

JSON representation  
---  
      
    
    {
      "throughputReservation": string
    }  
  
Fields  
---  
`throughputReservation` |  `string` The Reservation to use for this topic's throughput capacity. Structured like: projects/{project_number}/locations/{location}/reservations/{reservationId}  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics/create)`

|  Creates a new topic.  
  
### `[delete](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics/delete)`

|  Deletes the specified topic.  
  
### `[get](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics/get)`

|  Returns the topic configuration.  
  
### `[getPartitions](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics/getPartitions)`

|  Returns the partition information for the requested topic.  
  
### `[list](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics/list)`

|  Returns the list of topics for the given project.  
  
### `[patch](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics/patch)`

|  Updates properties of the specified topic.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-17 UTC."],[],[]] 
