---
url: https://docs.cloud.google.com/datastore/docs/eventarc/
title: Overview of event-driven architectures with Eventarc \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:57.066057+00:00
---

# Overview of event-driven architectures with Eventarc  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/eventarc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Guides ](https://docs.cloud.google.com/datastore/docs/concepts/overview)



Send feedback 

#  Overview of event-driven architectures with Eventarc Stay organized with collections  Save and categorize content based on your preferences. 

You can use [Eventarc](https://docs.cloud.google.com/eventarc/docs/overview) and Firestore in Datastore mode to build event-driven architectures. Firestore in Datastore mode provides triggers for Eventarc that generate events from changes to a particular entity in your database. The trigger can route events to a [supported destination](https://docs.cloud.google.com/eventarc/docs/event-providers-targets):

  * [Cloud Run functions (2nd gen)](https://docs.cloud.google.com/datastore/docs/extend-with-functions-2nd-gen)
  * [Cloud Run](https://docs.cloud.google.com/eventarc/docs/run/route-trigger-cloud-firestore)
  * [Google Kubernetes Engine](https://docs.cloud.google.com/eventarc/docs/gke/route-trigger-cloud-firestore)
  * [Workflows](https://docs.cloud.google.com/eventarc/docs/workflows/route-trigger-cloud-firestore)



Eventarc offers a standardized solution to manage the flow of state changes, called _events_ , between decoupled microservices. When triggered, Eventarc routes these events to various destinations while managing delivery, security, authorization, observability, and error-handling for you.

**Note:** Eventarc events use the [`CloudEvents`](https://cloudevents.io/) specification.

## Example use cases

An event-driven architecture is a system design pattern where services react to changes in state known as events. You can use this pattern alongside the scalability of Firestore to add more features to your app. For example, you might add the following capabilities:

  * Interoperability between different technology stacks

Replicate your data and transform it before sending it to an analytics system.

  * Parallel processing

Fan out operations for parallel processing. If you have multiple systems that operate based on entity changes, you can use the push-based streams in each consumer and route the event to multiple consumers.

  * Push-based event streams

Build push-based messaging designs. Clients can receive notifications without needing to poll remote services. Without the polling latency, you can better perform on-the-fly data processing and real-time analysis.

  * State monitoring and alerting

Use an event-driven architecture to add custom metrics to your database operations. Monitor and receive alerts on changes and updates. Detect anomalies.




## Limitations

Note the following limitations for Datastore mode triggers for Eventarc:

  * Ordering is not guaranteed. Rapid changes can trigger events in an unexpected order.
  * Events are delivered _at least_ once.

Make sure your event handler is idempotent and avoid producing unexpected results or side effects when an event is delivered more than once. Refer to [Building idempotent functions](https://cloud.google.com/blog/products/serverless/cloud-functions-pro-tips-building-idempotent-functions) to learn more.

  * A trigger is associated with a single database. You cannot create a trigger that matches multiple databases.

  * Deleting a database does not automatically delete any triggers for that database. The trigger stops delivering events but continues to exist until you [delete the trigger](https://docs.cloud.google.com/eventarc/docs/managing-triggers#trigger-delete).




## Eventarc and Firestore in Datastore mode locations

Eventarc does not support multi-regions for Firestore event triggers, but you can still create triggers for Firestore databases in multi-region locations. Eventarc maps Firestore multi-region locations to the following Eventarc regions:

Firestore multi-region | Eventarc region  
---|---  
`nam5` | `us-central1`  
`eur3` | `europe-west4`  
  
## Datastore mode and Native mode event interoperability

Eventarc supports event triggers for both Datastore mode and Native mode. These event triggers are interoperable with both database types. A Firestore in Native mode database can receive Datastore events, and a Firestore in Datastore mode database can receive Native mode events.

Event interoperability lets you share Eventarc code across Firestore databases of different types.

### Event conversions

If you apply a Native mode event trigger to a Datastore mode database, Eventarc makes the following conversions:

  * The namespace of the entity is stored in the event's `PartitionId` attribute.
  * Embedded entities are converted to Native mode `map` types.



## What's next

  * Learn about [event-driven architectures](https://docs.cloud.google.com/eventarc/docs/event-driven-architectures).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
