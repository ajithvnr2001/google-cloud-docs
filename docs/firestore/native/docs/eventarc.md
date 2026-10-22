---
url: https://docs.cloud.google.com/firestore/native/docs/eventarc/
title: Create event-driven architectures with Eventarc \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:28:15.329206+00:00
---

# Create event-driven architectures with Eventarc  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/eventarc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create event-driven architectures with Eventarc

You can use [Eventarc](https://docs.cloud.google.com/eventarc/docs/overview) and Firestore to build [event-driven architectures](https://docs.cloud.google.com/eventarc/docs/event-driven-architectures). Firestore triggers for Eventarc generate events from changes to a particular documents in your database. The trigger can route events to a [supported destination](https://docs.cloud.google.com/eventarc/docs/event-providers-targets):

  * Cloud Run functions (2nd gen) which supports the [Cloud Client Libraries](https://docs.cloud.google.com/firestore/docs/extend-with-functions-2nd-gen) and the [Firebase SDK](https://firebase.google.com/docs/firestore/extend-with-functions-2nd-gen)
  * [Cloud Run](https://docs.cloud.google.com/eventarc/docs/run/route-trigger-cloud-firestore)
  * [Google Kubernetes Engine](https://docs.cloud.google.com/eventarc/docs/gke/route-trigger-cloud-firestore)
  * [Workflows](https://docs.cloud.google.com/eventarc/docs/workflows/route-trigger-cloud-firestore)



Eventarc offers a standardized solution to manage the flow of state changes, called _events_ , between decoupled microservices. When triggered, Eventarc routes these events to various destinations while managing delivery, security, authorization, observability, and error-handling for you.

**Note:** Eventarc events use the [`CloudEvents`](https://cloudevents.io/) specification.

## Limitations

Note the following limitations for Firestore triggers for Eventarc:

  * Ordering is not guaranteed. Rapid changes can trigger events in an unexpected order.
  * Events are delivered _at least_ once.

Make sure your event handler is idempotent and avoid producing unexpected results or side effects when an event is delivered more than once. Refer to [Building idempotent functions](https://cloud.google.com/blog/products/serverless/cloud-functions-pro-tips-building-idempotent-functions) to learn more.

  * A trigger is associated with a single database. You cannot create a trigger that matches multiple databases.

  * Deleting a database does not automatically delete any triggers for that database. The trigger stops delivering events but continues to exist until you [delete the trigger](https://docs.cloud.google.com/eventarc/docs/managing-triggers#trigger-delete). If the database is recreated, any associated triggers will also need to be deleted and recreated to restore event delivery.




## Differences between Cloud Run functions 2nd gen and 1st gen

Cloud Run functions (2nd gen) uses Eventarc events for all runtimes. Previously, Cloud Run functions (1st gen) used Eventarc events for [only some runtimes](https://docs.cloud.google.com/functions/docs/writing/write-event-driven-functions). Eventarc events introduce the following differences from [Cloud Run functions (1st gen)](https://docs.cloud.google.com/firestore/docs/extend-with-functions).

  * The Firestore triggers for Eventarc support additional destinations besides Cloud Run functions. You can route `CloudEvents` to a number of [destinations](https://docs.cloud.google.com/eventarc/docs/event-providers-targets) including, but not limited to Cloud Run, GKE, and Workflows.

  * Firestore triggers for Eventarc retrieve the trigger definition at the start of a database write operation and uses that definition to decide if Firestore should emit an event. The write operation does not take into account any changes to trigger definition that might happen as it runs.

Cloud Run functions (1st gen) retrieves the trigger definition during the evaluation of the database write, and changes to the trigger during evaluation can affect if Firestore emits an event or not.




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

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
