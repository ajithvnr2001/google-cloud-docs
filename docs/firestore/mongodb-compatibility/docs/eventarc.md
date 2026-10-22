---
url: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/eventarc/
title: Create event-driven architectures with Eventarc \u00a0|\u00a0 Firestore with MongoDB compatibility \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:42.275528+00:00
---

# Create event-driven architectures with Eventarc  |  Firestore with MongoDB compatibility  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/eventarc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore with MongoDB compatibility ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create event-driven architectures with Eventarc

You can use [Eventarc](https://docs.cloud.google.com/eventarc/docs/overview) and Firestore with MongoDB compatibility to build [event-driven architectures](https://docs.cloud.google.com/eventarc/docs/event-driven-architectures). Firestore with MongoDB compatibility triggers for Eventarc generate events from changes to a particular documents in your database. The trigger can route events to a [supported destination](https://docs.cloud.google.com/eventarc/docs/event-providers-targets):

  * Cloud Run functions (2nd gen) which supports the [Cloud Client Libraries](https://docs.cloud.google.com/firestore/docs/extend-with-functions-2nd-gen) and the [Firebase SDK](https://firebase.google.com/docs/firestore/extend-with-functions-2nd-gen)
  * [Cloud Run](https://docs.cloud.google.com/eventarc/docs/run/route-trigger-cloud-firestore)
  * [Google Kubernetes Engine](https://docs.cloud.google.com/eventarc/docs/gke/route-trigger-cloud-firestore)
  * [Workflows](https://docs.cloud.google.com/eventarc/docs/workflows/route-trigger-cloud-firestore)



Eventarc offers a standardized solution to manage the flow of state changes, called _events_ , between decoupled microservices. When triggered, Eventarc routes these events to various destinations while managing delivery, security, authorization, observability, and error-handling for you.

**Note:** Eventarc events use the [`CloudEvents`](https://cloudevents.io/) specification.

## Limitations

Note the following limitations for Firestore with MongoDB compatibility triggers for Eventarc:

  * Ordering is not guaranteed. Rapid changes can trigger events in an unexpected order.
  * Events are delivered _at least_ once.

Make sure your event handler is idempotent and avoid producing unexpected results or side effects when an event is delivered more than once. Refer to [Building idempotent functions](https://cloud.google.com/blog/products/serverless/cloud-functions-pro-tips-building-idempotent-functions) to learn more.

  * A trigger is associated with a single database. You cannot create a trigger that matches multiple databases.

  * Deleting a database does not automatically delete any triggers for that database. The trigger stops delivering events but continues to exist until you [delete the trigger](https://docs.cloud.google.com/eventarc/docs/managing-triggers#trigger-delete). If the database is recreated, any associated triggers will also need to be deleted and recreated to restore event delivery.

  * Firestore with MongoDB compatibility supports Cloud Run functions (2nd gen) and doesn't support Cloud Run functions (1st gen).

  * Firestore Enterprise edition databases don't support Datastore entity event types.

  * Documents larger than 10 MiB aren't included in the event payload. To retrieve the versioned document, use a [point-in-time recovery read time](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/use-pitr#read-pitr).




## What's next

  * Learn about [event-driven architectures](https://docs.cloud.google.com/eventarc/docs/event-driven-architectures).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
