---
url: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/securing-with-vpc-sc/
title: VPC Service Controls \u00a0|\u00a0 Firestore with MongoDB compatibility \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:44.810461+00:00
---

# VPC Service Controls  |  Firestore with MongoDB compatibility  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/securing-with-vpc-sc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore with MongoDB compatibility ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VPC Service Controls

[VPC Service Controls](https://cloud.google.com/vpc-service-controls/) lets organizations define a perimeter around Google Cloud resources to mitigate data exfiltration risks. With VPC Service Controls, you create perimeters that protect the resources and data of services that you explicitly specify.

## Bundled Firestore services

The following APIs are bundled together in VPC Service Controls:

  * `firestore.googleapis.com`
  * `datastore.googleapis.com`
  * `firestorekeyvisualizer.googleapis.com`



When you restrict the `firestore.googleapis.com` service in a perimeter, the perimeter also restricts the `datastore.googleapis.com` and `firestorekeyvisualizer.googleapis.com` services.

### Restrict the datastore.googleapis.com service

The `datastore.googleapis.com` service is bundled under the `firestore.googleapis.com` service. To restrict the `datastore.googleapis.com` service, you must restrict the `firestore.googleapis.com` service as follows:

  * When creating a service perimeter using the Google Cloud console, add Firestore as the restricted service.
  * When creating a service perimeter using the Google Cloud CLI, use `firestore.googleapis.com` instead of `datastore.googleapis.com`.
        
        --perimeter-restricted-services=firestore.googleapis.com
        




### App Engine legacy bundled services for Datastore

[App Engine legacy bundled services for Datastore](https://cloud.google.com/appengine/docs/standard/python/bundled-services-overview) don't support service perimeters. Protecting the Datastore service with a service perimeter blocks traffic from App Engine legacy bundled services. Legacy bundled services include:

  * [Java 8 Datastore with App Engine APIs](https://cloud.google.com/appengine/docs/standard/java/datastore)
  * [Python 2 NDB client library for Datastore](https://cloud.google.com/appengine/docs/standard/python/ndb/creating-entities)
  * [Go 1.11 Datastore with App Engine APIs](https://cloud.google.com/appengine/docs/standard/go111/datastore)



## Restricted VIP

To use Firestore with MongoDB compatibility with restricted VIP, you must configure connectivity to the VIP domain used by Firestore with MongoDB compatibility. This domain and its IP addresses are used only by the Firestore with MongoDB compatibility service and are VPC Service Controls compliant.

For instructions, see [Configure Private Google Access in Firestore with MongoDB compatibility](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/configure-private-google-access).

## Egress protection on import and export operations

Firestore with MongoDB compatibility supports VPC Service Controls but requires additional configuration to get full egress protection on import and export operations. You must use the Firestore service agent to authorize import and export operations instead of the default App Engine service account. Use the following instructions to view and configure the authorization account for import and export operations.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
