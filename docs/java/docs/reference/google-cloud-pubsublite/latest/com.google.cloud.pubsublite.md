---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite
title: Package com.google.cloud.pubsublite (1.16.5) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:09.183269+00:00
---

# Package com.google.cloud.pubsublite (1.16.5)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Package com.google.cloud.pubsublite (1.16.5) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.5 (latest)  1.16.2  1.15.21  1.14.8  1.13.8  1.12.22  1.11.2  1.10.0  1.9.4  1.8.0  1.7.1  1.6.3  1.5.5  1.4.12 

[GitHub Repository](https://github.com/googleapis/java-pubsublite/tree/main//google-cloud-pubsublite/src/main/java/com/google/cloud/pubsublite)  
---  
  
## This package is not the recommended entry point to using this client library!

For this library, we recommend using [com.google.cloud.pubsublite.cloudpubsub](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub) for new applications.

## Client Classes

Client classes are the main entry point to using a package. They contain several variations of Java methods for each of the API's methods. 

Client |  Description  
---|---  
[com.google.cloud.pubsublite.AdminClient](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient) |  A client for performing Pub/Sub Lite admin operations.  
  
## Settings Classes

Settings classes can be used to configure credentials, endpoints, and retry settings for a Client. 

Settings |  Description  
---|---  
[com.google.cloud.pubsublite.AdminClientSettings](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings) |  Settings for construction a Pub/Sub Lite AdminClient.  
  
## Classes

Class |  Description  
---|---  
[com.google.cloud.pubsublite.AdminClientSettings.Builder](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.Builder) |   
[com.google.cloud.pubsublite.CloudRegion](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion) |  A wrapped string representing a Google Cloud region.  
[com.google.cloud.pubsublite.CloudRegionOrZone](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone) |   
[com.google.cloud.pubsublite.CloudZone](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone) |  A representation of a Google Cloud zone.  
[com.google.cloud.pubsublite.Constants](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Constants) |  Useful general constants for Pub/Sub Lite.  
[com.google.cloud.pubsublite.Endpoints](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Endpoints) |  Constructs regional endpoints from a CloudRegion.  
[com.google.cloud.pubsublite.ErrorCodes](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ErrorCodes) |  Pub/Sub Lite retryable error codes.  
[com.google.cloud.pubsublite.LocationPath](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.LocationPath) |  A string wrapper representing a project and location.  
[com.google.cloud.pubsublite.LocationPath.Builder](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.LocationPath.Builder) |   
[com.google.cloud.pubsublite.Message](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Message) |  A user message.  
[com.google.cloud.pubsublite.Message.Builder](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Message.Builder) |   
[com.google.cloud.pubsublite.MessageMetadata](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageMetadata) |  Information about a message in Pub/Sub Lite. Can be encoded in the string returned by the Cloud Pub/Sub com.google.cloud.pubsub.v1.Publisher#publish api or the com.google.pubsub.v1.PubsubMessage#getMessageId field on received messages.  
[com.google.cloud.pubsublite.Offset](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Offset) |  An offset in the partition.  
[com.google.cloud.pubsublite.Partition](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Partition) |  A partition of a topic.  
[com.google.cloud.pubsublite.PartitionLookupUtils](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.PartitionLookupUtils) |  Utilities for looking up information on partitions.  
[com.google.cloud.pubsublite.ProjectId](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectId) |   
[com.google.cloud.pubsublite.ProjectIdOrNumber](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectIdOrNumber) |   
[com.google.cloud.pubsublite.ProjectNumber](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber) |  A wrapper class for the [project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).  
[com.google.cloud.pubsublite.ProjectPath](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectPath) |  A string wrapper representing a project.  
[com.google.cloud.pubsublite.ProjectPath.Builder](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectPath.Builder) |   
[com.google.cloud.pubsublite.ReservationName](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationName) |  A string wrapper for the name of a reservation.  
[com.google.cloud.pubsublite.ReservationPath](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath) |  A string wrapper representing a reservation. Should be structured like: projects/<project number>/locations/<cloud region>/reservations/<id>  
[com.google.cloud.pubsublite.ReservationPath.Builder](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ReservationPath.Builder) |   
[com.google.cloud.pubsublite.SeekTarget](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SeekTarget) |  The target location to seek a subscription to.  
[com.google.cloud.pubsublite.SequencedMessage](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SequencedMessage) |  A message with its sequencing information in the partition.  
[com.google.cloud.pubsublite.SubscriptionName](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionName) |  A string wrapper for the name of a subscription.  
[com.google.cloud.pubsublite.SubscriptionPath](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath) |  A string wrapper representing a subscription. Should be structured like: projects/<project number>/locations/<cloud region or zone>/subscriptions/<id>  
[com.google.cloud.pubsublite.SubscriptionPath.Builder](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.Builder) |   
[com.google.cloud.pubsublite.TopicName](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicName) |  A string wrapper for the name of a topic.  
[com.google.cloud.pubsublite.TopicPath](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath) |  A string wrapper representing a topic. Should be structured like: projects/<project number>/locations/<cloud region or zone>/topics/<id>  
[com.google.cloud.pubsublite.TopicPath.Builder](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.Builder) |   
  
## Interfaces

Interface |  Description  
---|---  
[com.google.cloud.pubsublite.MessageTransformer](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageTransformer) |  A MessageTransformer details how to transform a message of one type to another. It is likely that either FromT or ToT will be a Message on publish and SequencedMessage on subscribe.  
  
## Enums

Enum |  Description  
---|---  
[com.google.cloud.pubsublite.BacklogLocation](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.BacklogLocation) |  BacklogLocation refers to a location with respect to the message backlog.  
[com.google.cloud.pubsublite.CloudRegionOrZone.Kind](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.Kind) |   
[com.google.cloud.pubsublite.SeekTarget.Kind](https://cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SeekTarget.Kind) |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-26 UTC."],[],[]] 
