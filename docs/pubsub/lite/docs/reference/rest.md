---
url: https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/
title: Pub/Sub Lite API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:58.371701+00:00
---

# Pub/Sub Lite API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)



Send feedback 

#  Pub/Sub Lite API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v1.admin.projects.locations.operations
  * REST Resource: v1.admin.projects.locations.reservations
  * REST Resource: v1.admin.projects.locations.reservations.topics
  * REST Resource: v1.admin.projects.locations.subscriptions
  * REST Resource: v1.admin.projects.locations.topics
  * REST Resource: v1.admin.projects.locations.topics.subscriptions
  * REST Resource: v1.cursor.projects.locations.subscriptions
  * REST Resource: v1.cursor.projects.locations.subscriptions.cursors
  * REST Resource: v1.topicStats.projects.locations.topics



## Service: pubsublite.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://pubsublite.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. The service might have multiple service endpoints. This Pub/Sub Lite service has the following [regional](https://cloud.google.com/pubsub/lite/docs/locations#regions_and_zones) service endpoints and all URIs below are relative to these service endpoints:

  * `https://REGION_NAME-pubsublite.googleapis.com`



## REST Resource: [v1.admin.projects.locations.operations](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.operations/cancel)` |  `POST /v1/admin/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.operations/delete)` |  `DELETE /v1/admin/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.operations/get)` |  `GET /v1/admin/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.operations/list)` |  `GET /v1/admin/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.admin.projects.locations.reservations](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.reservations)

Methods  
---  
`[create](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.reservations/create)` |  `POST /v1/admin/{parent=projects/*/locations/*}/reservations`   
Creates a new reservation.  
`[delete](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.reservations/delete)` |  `DELETE /v1/admin/{name=projects/*/locations/*/reservations/*}`   
Deletes the specified reservation.  
`[get](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.reservations/get)` |  `GET /v1/admin/{name=projects/*/locations/*/reservations/*}`   
Returns the reservation configuration.  
`[list](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.reservations/list)` |  `GET /v1/admin/{parent=projects/*/locations/*}/reservations`   
Returns the list of reservations for the given project.  
`[patch](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.reservations/patch)` |  `PATCH /v1/admin/{reservation.name=projects/*/locations/*/reservations/*}`   
Updates properties of the specified reservation.  
  
## REST Resource: [v1.admin.projects.locations.reservations.topics](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.reservations.topics)

Methods  
---  
`[list](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.reservations.topics/list)` |  `GET /v1/admin/{name=projects/*/locations/*/reservations/*}/topics`   
Lists the topics attached to the specified reservation.  
  
## REST Resource: [v1.admin.projects.locations.subscriptions](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.subscriptions)

Methods  
---  
`[create](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.subscriptions/create)` |  `POST /v1/admin/{parent=projects/*/locations/*}/subscriptions`   
Creates a new subscription.  
`[delete](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.subscriptions/delete)` |  `DELETE /v1/admin/{name=projects/*/locations/*/subscriptions/*}`   
Deletes the specified subscription.  
`[get](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.subscriptions/get)` |  `GET /v1/admin/{name=projects/*/locations/*/subscriptions/*}`   
Returns the subscription configuration.  
`[list](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.subscriptions/list)` |  `GET /v1/admin/{parent=projects/*/locations/*}/subscriptions`   
Returns the list of subscriptions for the given project.  
`[patch](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.subscriptions/patch)` |  `PATCH /v1/admin/{subscription.name=projects/*/locations/*/subscriptions/*}`   
Updates properties of the specified subscription.  
`[seek](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.subscriptions/seek)` |  `POST /v1/admin/{name=projects/*/locations/*/subscriptions/*}:seek`   
Performs an out-of-band seek for a subscription to a specified target, which may be timestamps or named positions within the message backlog.  
  
## REST Resource: [v1.admin.projects.locations.topics](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics)

Methods  
---  
`[create](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics/create)` |  `POST /v1/admin/{parent=projects/*/locations/*}/topics`   
Creates a new topic.  
`[delete](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics/delete)` |  `DELETE /v1/admin/{name=projects/*/locations/*/topics/*}`   
Deletes the specified topic.  
`[get](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics/get)` |  `GET /v1/admin/{name=projects/*/locations/*/topics/*}`   
Returns the topic configuration.  
`[getPartitions](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics/getPartitions)` |  `GET /v1/admin/{name=projects/*/locations/*/topics/*}/partitions`   
Returns the partition information for the requested topic.  
`[list](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics/list)` |  `GET /v1/admin/{parent=projects/*/locations/*}/topics`   
Returns the list of topics for the given project.  
`[patch](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics/patch)` |  `PATCH /v1/admin/{topic.name=projects/*/locations/*/topics/*}`   
Updates properties of the specified topic.  
  
## REST Resource: [v1.admin.projects.locations.topics.subscriptions](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics.subscriptions)

Methods  
---  
`[list](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics.subscriptions/list)` |  `GET /v1/admin/{name=projects/*/locations/*/topics/*}/subscriptions`   
Lists the subscriptions attached to the specified topic.  
  
## REST Resource: [v1.cursor.projects.locations.subscriptions](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/cursor.projects.locations.subscriptions)

Methods  
---  
`[commitCursor](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/cursor.projects.locations.subscriptions/commitCursor)` |  `POST /v1/cursor/{subscription=projects/*/locations/*/subscriptions/*}:commitCursor`   
Updates the committed cursor.  
  
## REST Resource: [v1.cursor.projects.locations.subscriptions.cursors](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/cursor.projects.locations.subscriptions.cursors)

Methods  
---  
`[list](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/cursor.projects.locations.subscriptions.cursors/list)` |  `GET /v1/cursor/{parent=projects/*/locations/*/subscriptions/*}/cursors`   
Returns all committed cursor information for a subscription.  
  
## REST Resource: [v1.topicStats.projects.locations.topics](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/topicStats.projects.locations.topics)

Methods  
---  
`[computeHeadCursor](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/topicStats.projects.locations.topics/computeHeadCursor)` |  `POST /v1/topicStats/{topic=projects/*/locations/*/topics/*}:computeHeadCursor`   
Compute the head cursor for the partition.  
`[computeMessageStats](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/topicStats.projects.locations.topics/computeMessageStats)` |  `POST /v1/topicStats/{topic=projects/*/locations/*/topics/*}:computeMessageStats`   
Compute statistics about a range of messages in a given topic and partition.  
`[computeTimeCursor](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/topicStats.projects.locations.topics/computeTimeCursor)` |  `POST /v1/topicStats/{topic=projects/*/locations/*/topics/*}:computeTimeCursor`   
Compute the corresponding cursor for a publish or event time in a topic partition.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-17 UTC."],[],[]] 
